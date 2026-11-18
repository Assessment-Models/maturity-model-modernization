#!/usr/bin/env python3
"""Level 1 — local model validation for maturity-model-modernization (CR-AM-11 §14).

Checks:
  1. model.yaml parses and matches the Assessment-Models manifest contract
     (`Assessment-Models/assessment-ci/schemas/model-manifest.schema.json`)
  2. the §15 contract handshake is well formed (contract id + version + source)
  3. maturity/scale.yaml declares exactly 5 levels with ordinals 0..4 and the
     expected identifiers, plus a conformant ordering/progression contract
  4. maturity/model/modernization.yaml carries the model identity, its level
     references resolve against the scale, and its version is coherent with
     the manifest
  5. maturity/model/criteria.yaml (v1.1.0+): catalog identity, 4 practice
     areas, fully formed criteria with L0..L4 anchors, unique ids, weights
     summing to 100
  6. maturity/model/scoring.yaml: weighted-mean aggregation contract and a
     band-resolution mirror that matches the canonical v2 bands exactly
  7. every examples/*.yaml: criterion ids resolve against the catalog, scores
     are within [0, 100], the weighted mean matches aggregated_score, the
     resolved band/level match the canonical v2 bands, and the
     effort-adjusted value applies that band's effort multiplier

Exit 0 with OK when clean; exit 1 listing every failure otherwise.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


def load(rel: str):
    p = ROOT / rel
    if not p.is_file():
        errors.append(f"missing file: {rel}")
        return {}
    return yaml.safe_load(p.read_text()) or {}


manifest = load("model.yaml")
scale = load("maturity/scale.yaml")
register = load("maturity/model/modernization.yaml")
catalog = load("maturity/model/criteria.yaml")
scoring = load("maturity/model/scoring.yaml")

# 1 — manifest shape
for key in ("id", "type", "name", "version", "conformance"):
    if key not in manifest:
        errors.append(f"model.yaml: missing required field {key}")
if manifest.get("type") not in ("maturity-model", "assessment-model", "assessment-tool"):
    errors.append(f"model.yaml: invalid type {manifest.get('type')!r}")

# 2 — contract handshake
conf = manifest.get("conformance") or {}
contract = conf.get("contract") or {}
if not contract.get("id"):
    errors.append("model.yaml: conformance.contract.id is required")
if not conf.get("version"):
    errors.append("model.yaml: conformance.version is required")
src = conf.get("source") or {}
if not src.get("organization") or not src.get("repository"):
    errors.append("model.yaml: conformance.source organization+repository are required")

# 3 — scale
EXPECTED_LEVELS = ['L0', 'L1', 'L2', 'L3', 'L4']
levels_actual = scale.get("levels") or []
if len(levels_actual) != len(EXPECTED_LEVELS):
    errors.append(f"scale: expected {len(EXPECTED_LEVELS)} levels, found {len(levels_actual)}")
for i, lvl in enumerate(levels_actual):
    if lvl.get("ordinal") != i:
        errors.append(f"scale: level {i} ordinal is {lvl.get('ordinal')!r}, expected {i}")
    if lvl.get("id") not in EXPECTED_LEVELS:
        errors.append(f"scale: unexpected level id {lvl.get('id')!r}")
    if not lvl.get("name") or not lvl.get("definition"):
        errors.append(f"scale: level {lvl.get('id')} requires name and definition")
if scale.get("ordering") != "ascending":
    errors.append("scale: ordering must be 'ascending'")
prog = scale.get("progression") or {}
if not prog.get("topology") or not prog.get("function"):
    errors.append("scale: progression requires topology and function")

# 4 — register identity + level resolution + version coherence
if register.get("repo_id") != manifest.get("id"):
    errors.append(
        f"register repo_id {register.get('repo_id')!r} != manifest id {manifest.get('id')!r}"
    )
if not register.get("id"):
    errors.append("register: canonical model id is required")
if str(register.get("version")) != str(manifest.get("version")):
    errors.append(
        f"register version {register.get('version')!r} != manifest version "
        f"{manifest.get('version')!r}"
    )
scale_ids = {l.get("id") for l in levels_actual}
for ref in register.get("scale_levels", []) or []:
    if ref not in scale_ids:
        errors.append(f"register: scale level {ref!r} does not exist in the scale")

# 5 — criteria catalog
catalog_criteria: dict[str, dict] = {}
catalog_weight_total = 0.0
if not catalog:
    errors.append("criteria catalog: missing or empty maturity/model/criteria.yaml")
else:
    if catalog.get("model") != register.get("id"):
        errors.append(
            f"criteria catalog: model {catalog.get('model')!r} != register id "
            f"{register.get('id')!r}"
        )
    if str(catalog.get("version")) != str(manifest.get("version")):
        errors.append(
            f"criteria catalog: version {catalog.get('version')!r} != manifest version "
            f"{manifest.get('version')!r}"
        )
    areas = catalog.get("practice_areas") or []
    if len(areas) < 4:
        errors.append(f"criteria catalog: expected 4 practice areas, found {len(areas)}")
    area_ids = [a.get("id") for a in areas]
    if len(area_ids) != len(set(area_ids)):
        errors.append("criteria catalog: duplicate practice area ids")
    n_criteria = 0
    for area in areas:
        if not area.get("id") or not area.get("name"):
            errors.append("criteria catalog: practice area requires id and name")
        for c in area.get("criteria") or []:
            n_criteria += 1
            cid = c.get("id")
            if not cid:
                errors.append("criteria catalog: criterion without id")
                continue
            if cid in catalog_criteria:
                errors.append(f"criteria catalog: duplicate criterion id {cid!r}")
                continue
            catalog_criteria[cid] = c
            for key in ("name", "definition", "assessment_question"):
                if not c.get(key):
                    errors.append(f"criterion {cid}: missing {key}")
            w = c.get("weight")
            if not isinstance(w, (int, float)) or w <= 0:
                errors.append(f"criterion {cid}: weight must be a positive number")
            else:
                catalog_weight_total += float(w)
            anchors = c.get("level_anchors") or {}
            for lvl in EXPECTED_LEVELS:
                if not str(anchors.get(lvl) or "").strip():
                    errors.append(f"criterion {cid}: missing level anchor for {lvl}")
            if not (c.get("evidence") or []):
                errors.append(f"criterion {cid}: evidence expectations are required")
    if n_criteria < 10:
        errors.append(f"criteria catalog: expected at least 10 criteria, found {n_criteria}")
    if abs(catalog_weight_total - 100.0) > 0.001:
        errors.append(
            f"criteria catalog: criterion weights must sum to 100, found {catalog_weight_total}"
        )

# 6 — scoring model (band mirror checked against the CANONICAL v2 bands)
V2_BANDS = [('level-1-emergent', (0, 20), 'Emergent', 1.0, 'L0'), ('level-2-structured', (21, 45), 'Structured', 1.5, 'L1'), ('level-3-systematic', (46, 70), 'Systematic', 2.5, 'L2'), ('level-4-adaptive', (71, 88), 'Adaptive', 4.0, 'L3'), ('level-5-self-optimising', (89, 100), 'Self-Optimising', 6.0, 'L4')]


def band_for(score: float):
    for band_id, rng, name, mult, lvl in V2_BANDS:
        if rng[0] <= score <= rng[1]:
            return band_id, name, mult, lvl
    return None, None, None, None


if not scoring:
    errors.append("scoring model: missing or empty maturity/model/scoring.yaml")
else:
    if scoring.get("model") != register.get("id"):
        errors.append(
            f"scoring model: model {scoring.get('model')!r} != register id {register.get('id')!r}"
        )
    if str(scoring.get("version")) != str(manifest.get("version")):
        errors.append(
            f"scoring model: version {scoring.get('version')!r} != manifest version "
            f"{manifest.get('version')!r}"
        )
    if (scoring.get("aggregation") or {}).get("method") != "weighted_mean":
        errors.append("scoring model: aggregation.method must be 'weighted_mean'")
    mirror = (scoring.get("band_resolution") or {}).get("bands") or []
    if len(mirror) != len(V2_BANDS):
        errors.append(
            f"scoring model: band mirror must carry {len(V2_BANDS)} bands, found {len(mirror)}"
        )
    for got, want in zip(mirror, V2_BANDS):
        want_id, want_rng, want_name, want_mult, want_lvl = want
        rng = got.get("range") or []
        if (
            got.get("id") != want_id
            or got.get("name") != want_name
            or len(rng) != 2
            or rng[0] != want_rng[0]
            or rng[1] != want_rng[1]
            or float(got.get("effort_multiplier")) != want_mult
            or got.get("scale_level") != want_lvl
        ):
            errors.append(
                f"scoring model: band mirror for {want_id!r} drifts from the canonical v2 bands"
            )

# 7 — every worked example: catalog resolution + scoring maths
examples_dir = ROOT / "examples"
example_files = sorted(examples_dir.glob("*.yaml")) if examples_dir.is_dir() else []
if not example_files:
    errors.append("examples: no worked examples found under examples/")
for ex_path in example_files:
    ex = yaml.safe_load(ex_path.read_text()) or {}
    label = f"example {ex_path.name}"
    if ex.get("model") != register.get("id"):
        errors.append(f"{label}: model {ex.get('model')!r} != register id {register.get('id')!r}")
    entries = [e for e in (ex.get("criterion_scores") or []) if not e.get("not_applicable")]
    applicable = [e for e in entries if e.get("criterion") in catalog_criteria]
    for e in entries:
        cid = e.get("criterion")
        if cid not in catalog_criteria:
            errors.append(f"{label}: criterion {cid!r} does not exist in the catalog")
        s = e.get("score")
        if not isinstance(s, (int, float)) or not (0 <= s <= 100):
            errors.append(f"{label}: score for {cid!r} must be a number in [0, 100]")
    if len(entries) < (scoring.get("aggregation") or {}).get("minimum_applicable_criteria", 10):
        errors.append(f"{label}: too few applicable criteria for a defensible aggregate")
    weight_sum = sum(
        float(catalog_criteria[e["criterion"]].get("weight") or 0)
        for e in applicable
        if isinstance(e.get("score"), (int, float))
    )
    if weight_sum <= 0:
        errors.append(f"{label}: no applicable weighted criteria")
        continue
    weighted = sum(
        float(e["score"]) * float(catalog_criteria[e["criterion"]].get("weight") or 0)
        for e in applicable
        if isinstance(e.get("score"), (int, float))
    )
    expected_agg = weighted / weight_sum
    agg = ex.get("aggregated_score")
    if not isinstance(agg, (int, float)):
        errors.append(f"{label}: aggregated_score must be numeric")
        continue
    if not (0 <= agg <= 100):
        errors.append(f"{label}: aggregated_score {agg} is outside [0, 100]")
    if abs(float(agg) - expected_agg) > 0.01:
        errors.append(
            f"{label}: aggregated_score {agg} != weighted mean of catalog scores ({expected_agg:.2f})"
        )
    band_id, band_name, mult, lvl = band_for(float(agg))
    if band_id is None:
        errors.append(f"{label}: aggregated_score {agg} resolves to no canonical v2 band")
        continue
    declared = ex.get("resolved_band")
    if declared != band_id:
        errors.append(f"{label}: resolved_band {declared!r} != computed {band_id!r}")
    declared_lvl = ex.get("resolved_level")
    if declared_lvl is not None and declared_lvl != lvl:
        errors.append(f"{label}: resolved_level {declared_lvl!r} != computed {lvl!r}")
    eav = ex.get("effort_adjusted_value")
    if eav is not None and mult is not None:
        expected = round(float(agg) * float(mult), 2)
        if abs(float(eav) - expected) > 0.01:
            errors.append(
                f"{label}: effort_adjusted_value {eav} != aggregated_score * "
                f"effort_multiplier ({expected})"
            )

if errors:
    print(f"FAIL — {len(errors)} error(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(
    f"OK — maturity-model-modernization {manifest.get('version')}: manifest + scale "
    f"({len(levels_actual)} levels) + register + catalog ({len(catalog_criteria)} criteria, "
    f"{len(catalog.get('practice_areas') or [])} areas) + scoring + {len(example_files)} "
    f"example(s) valid"
)
