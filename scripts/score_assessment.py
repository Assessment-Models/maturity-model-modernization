#!/usr/bin/env python3
"""Score a modernization maturity assessment against the criteria catalog.

Usage:
    python scripts/score_assessment.py examples/modernization-2026.yaml
    python scripts/score_assessment.py assessment.yaml --json

Loads the criteria catalog (maturity/model/criteria.yaml) and the scoring
model (maturity/model/scoring.yaml), validates the assessment against them,
and prints a score report: per-practice-area weighted means, the aggregated
score, the resolved canonical v2 band with its scale level, and the
effort-adjusted value. With --json, emits the same result as a JSON object.

Exit 0 on a valid, scored assessment; exit 1 with a list of problems
otherwise. This is a scoring utility, not a gate: the CI gate is
scripts/local_validate.py.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load(path: Path):
    return yaml.safe_load(path.read_text()) or {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("assessment", help="path to an assessment YAML file")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = parser.parse_args()

    assessment_path = Path(args.assessment)
    if not assessment_path.is_file():
        print(f"FAIL — assessment file not found: {assessment_path}", file=sys.stderr)
        return 1

    catalog = load(ROOT / "maturity/model/criteria.yaml")
    scoring = load(ROOT / "maturity/model/scoring.yaml")
    assessment = load(assessment_path)

    problems: list[str] = []

    # Index the catalog.
    criteria: dict[str, dict] = {}
    areas: dict[str, dict] = {}
    for area in catalog.get("practice_areas") or []:
        areas[area["id"]] = {"name": area.get("name"), "criteria": []}
        for c in area.get("criteria") or []:
            criteria[c["id"]] = c
            areas[area["id"]]["criteria"].append(c["id"])

    # Validate and collect scores.
    scores: dict[str, float] = {}
    for e in assessment.get("criterion_scores") or []:
        cid = e.get("criterion")
        if e.get("not_applicable"):
            continue
        if cid not in criteria:
            problems.append(f"criterion {cid!r} does not exist in the catalog")
            continue
        s = e.get("score")
        if not isinstance(s, (int, float)) or not (0 <= s <= 100):
            problems.append(f"score for {cid!r} must be a number in [0, 100]")
            continue
        if cid in scores:
            problems.append(f"criterion {cid!r} scored more than once")
        scores[cid] = float(s)

    minimum = (scoring.get("aggregation") or {}).get("minimum_applicable_criteria", 10)
    if len(scores) < minimum:
        problems.append(f"at least {minimum} applicable criteria are required, found {len(scores)}")

    if problems:
        print(f"FAIL — {len(problems)} problem(s):", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    # Weighted mean per practice area, then overall (renormalised).
    def weighted_mean(cids: list[str]) -> tuple[float, float]:
        w = sum(float(criteria[c]["weight"]) for c in cids if c in scores)
        v = sum(scores[c] * float(criteria[c]["weight"]) for c in cids if c in scores)
        return (v / w if w else 0.0), w

    area_results = []
    for aid, area in areas.items():
        value, _ = weighted_mean(area["criteria"])
        area_results.append({"id": aid, "name": area["name"], "score": round(value, 2)})

    total_value, _ = weighted_mean(list(scores))
    aggregate = round(total_value, 2)

    band = None
    for b in (scoring.get("band_resolution") or {}).get("bands") or []:
        lo, hi = b.get("range") or [0, -1]
        if lo <= aggregate <= hi:
            band = b
            break
    if band is None:
        print(f"FAIL — aggregate {aggregate} resolves to no band", file=sys.stderr)
        return 1

    multiplier = float(band["effort_multiplier"])
    result = {
        "model": assessment.get("model") or catalog.get("model"),
        "assessment": assessment.get("id") or assessment_path.name,
        "criteria_scored": len(scores),
        "criteria_total": len(criteria),
        "practice_areas": area_results,
        "aggregated_score": aggregate,
        "resolved_band": band["id"],
        "band_name": band["name"],
        "resolved_level": band["scale_level"],
        "effort_multiplier": multiplier,
        "effort_adjusted_value": round(aggregate * multiplier, 2),
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"Assessment        : {result['assessment']}")
    print(f"Criteria scored  : {result['criteria_scored']} / {result['criteria_total']}")
    print("Practice areas:")
    for a in area_results:
        print(f"  {a['name']:<38} {a['score']:>6.2f}")
    print(f"Aggregated score : {aggregate:.2f}")
    print(f"Resolved band    : {band['id']} ({band['name']}), scale level {band['scale_level']}")
    print(f"Effort multiplier: {multiplier}x")
    print(f"Effort-adj. value: {result['effort_adjusted_value']:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
