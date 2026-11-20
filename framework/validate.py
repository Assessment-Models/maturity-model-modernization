#!/usr/bin/env python3
"""AMAF model validator (stdlib only).

Validates the framework/ artifacts against each other and against the
criterion catalog:

1. JSON Schema (subset: type, const, enum, pattern, properties, required,
   additionalProperties, items, minItems, uniqueItems, minLength, minimum,
   maximum, $ref to #/$defs/... and common.schema.json#/$defs/...) over the
   worked example instance bundle (examples/integration-instance.yaml),
   the four package schemas and the relationship registry.
2. Semantic re-derivation of the machine rules (rules/amaf-rules.yaml) over
   the example: gap arithmetic, evidence corroboration and staleness,
   finding classes and floors, severity derivation (R-SEV-1..5), parking
   (R-OPP-2), opportunity required content and profiles (R-PRI-1..6),
   referential integrity of every record id, and end-to-end chain coverage
   (every severe or material finding either closed by an initiative stage
   or parked with a reason).

YAML loading reuses the catalog exporter parser
(tools/criterion-catalog/export-catalog.py), which covers the YAML subset
these files use. Exit code 0 and one line of output means ok.

Usage: python3 framework/validate.py
"""

import importlib.util
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

# ---------------------------------------------------------------- load YAML


def load_parser():
    path = os.path.join(REPO, "tools", "criterion-catalog", "export-catalog.py")
    spec = importlib.util.spec_from_file_location("amaf_catalog_export", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_yaml(parser, relpath):
    return parser.parse(os.path.join(REPO, relpath))


# ------------------------------------------------- JSON Schema (subset)


class SchemaError(Exception):
    pass


def kind_of(value):
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    if value is None:
        return "null"
    return "unknown"


TYPE_MATCH = {
    "object": ("object",),
    "array": ("array",),
    "string": ("string",),
    "integer": ("integer",),
    "number": ("integer", "number"),
    "boolean": ("boolean",),
    "null": ("null",),
}


def resolve_ref(doc, common, ref):
    """Resolve a $ref; returns (node, owning_document).

    Refs inside a resolved definition (such as common's modelReference
    pointing at its own identifier) must keep resolving against the
    document that defines them, so the owning document travels along.
    """
    if ref.startswith("#/"):
        owner = doc
    elif ref.startswith("common.schema.json#/"):
        owner = common
        ref = ref[len("common.schema.json"):]  # already "#/$defs/..."
    else:
        raise SchemaError("unsupported $ref: %s" % ref)
    node = owner
    for part in ref[2:].split("/"):
        node = node[part]
    return node, owner


def check_schema(value, schema, path, errors, doc, common):
    if "$ref" in schema:
        target, owner = resolve_ref(doc, common, schema["$ref"])
        check_schema(value, target, path, errors, owner, common)
        return

    if "type" in schema:
        types = schema["type"]
        if isinstance(types, str):
            types = [types]
        allowed = set()
        for t in types:
            allowed.update(TYPE_MATCH[t])
        if kind_of(value) not in allowed:
            errors.append("%s: expected type %s, got %s" % (path, "|".join(types), kind_of(value)))
            return

    if "const" in schema and value != schema["const"]:
        errors.append("%s: expected const %r, got %r" % (path, schema["const"], value))

    if "enum" in schema and value not in schema["enum"]:
        errors.append("%s: %r not in enum %r" % (path, value, schema["enum"]))

    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append("%s: %r does not match %r" % (path, value, schema["pattern"]))
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append("%s: shorter than minLength %d" % (path, schema["minLength"]))

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append("%s: below minimum %r" % (path, schema["minimum"]))
        if "maximum" in schema and value > schema["maximum"]:
            errors.append("%s: above maximum %r" % (path, schema["maximum"]))

    if isinstance(value, dict):
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errors.append("%s: missing required key %r" % (path, key))
        for key, sub in props.items():
            if key in value:
                check_schema(value[key], sub, "%s.%s" % (path, key), errors, doc, common)
        addl = schema.get("additionalProperties")
        if addl is False:
            for key in value:
                if key not in props:
                    errors.append("%s: additional property %r" % (path, key))
        elif isinstance(addl, dict):
            for key in value:
                if key not in props:
                    check_schema(value[key], addl, "%s.%s" % (path, key), errors, doc, common)

    if isinstance(value, list):
        if "items" in schema:
            for idx, item in enumerate(value):
                check_schema(item, schema["items"], "%s[%d]" % (path, idx), errors, doc, common)
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append("%s: fewer than %d items" % (path, schema["minItems"]))
        if schema.get("uniqueItems"):
            seen = []
            for item in value:
                if item in seen:
                    errors.append("%s: duplicate item %r" % (path, item))
                seen.append(item)


def load_schema(name):
    with open(os.path.join(HERE, "schemas", name), encoding="utf-8") as fh:
        return json.load(fh)


def validate_doc(instance, schema_file, errors, label):
    doc = load_schema(schema_file)
    common = load_schema("common.schema.json")
    local = []
    data = dict(instance)
    data["schema"] = doc.get("properties", {}).get("schema", {}).get("const", "amaf")
    check_schema(data, doc, label, local, doc, common)
    for err in local:
        errors.append("%s: %s" % (schema_file, err))


# ------------------------------------------------------------ support


def fail(errors, msg):
    errors.append(msg)


def d(s):
    return date(*[int(x) for x in s.split("-")])


def months_before(ref, months=12):
    """Approximate 12-month window: same calendar day 12 months earlier."""
    y, m = ref.year, ref.month - months
    while m <= 0:
        y -= 1
        m += 12
    try:
        return date(y, m, ref.day)
    except ValueError:  # e.g. Feb 29
        return date(y, m, 28)


def collect_ids(records, key):
    return [r[key] for r in records]


def index_by(records, key):
    out = {}
    for r in records:
        out[r[key]] = r
    return out


# ------------------------------------------------------ semantic checks


def catalog_index(cat):
    dims = {}
    subs = {}
    crits = {}
    for dim in cat["dimensions"]:
        dims[dim["id"]] = dim
        for sub in dim.get("subdimensions", []):
            subs[sub["id"]] = sub
            for c in sub.get("criteria", []):
                crits[c["id"]] = c
    return dims, subs, crits


def criterion_exists(cid, dims, subs, crits):
    parts = cid.split(".")
    if len(parts) == 1:
        return cid in dims
    if len(parts) == 2:
        return cid in subs
    return cid in crits


def supporting_evidence_for(result_id, evidence):
    return [
        ev for ev in evidence
        if ev.get("result") == result_id
        and ev.get("relation") == "supports"
        and ev.get("status") != "superseded"
    ]


def derive_severity(result):
    """R-SEV-1..4: first satisfied row against basis results."""
    score = result.get("score")
    gap = result.get("gap")
    crit = result.get("criticality")
    atype = result.get("assessment_type")
    if (
        score == 1
        or (gap is not None and gap >= 3)
        or (atype == "exposure" and result.get("tolerance") == "outside" and crit in ("high", "critical"))
    ):
        return "severe"
    if (
        (score == 2 and crit in ("high", "critical"))
        or (atype == "demand" and result.get("committed"))
        or (score == 2 and gap == 2)
    ):
        return "material"
    if score == 2 or (score is not None and score >= 3 and gap == 2):
        return "moderate"
    return "minor"


def finding_class_ok(finding, results_by_id):
    for rid in finding["basis"]:
        res = results_by_id.get(rid)
        if res is None:
            continue
        score, atype, gap = res.get("score"), res.get("assessment_type"), res.get("gap")
        cls = finding["class"]
        if cls == "deficiency" and atype in ("condition", "target") and score <= 2:
            return True
        if cls == "exposure" and atype == "exposure" and score <= 2:
            return True
        if cls == "demand" and atype == "demand" and score <= 2:
            return True
        if cls == "constraint" and atype in ("changeability", "readiness") and score <= 2:
            return True
        # interpretation_rules v2: a sustained deliberate-excess overshoot
        # derives the constraint class, against the target rationale; the
        # sustained review must be recorded on the finding.
        if (cls == "constraint" and score is not None and score >= 3
                and gap is not None and gap <= -2
                and "deliberate-excess" in (finding.get("notes") or "")):
            return True
        if cls == "strength" and score >= 4 and res.get("confidence") == "high":
            return True
    return False


def profile_satisfied(profile_name, sig, findings_in, has_target):
    if profile_name == "critical":
        return (
            sig["modernization_need"]["level"] == "high"
            and sig["strategic_importance"]["level"] == "high"
            and any(f["class"] == "exposure" and f.get("severity") in ("material", "severe") for f in findings_in)
        )
    if profile_name == "strategic":
        return (
            sig["future_demand"]["level"] == "high"
            and sig["value_potential"]["level"] in ("medium", "high")
            and has_target
        )
    if profile_name == "risk_driven":
        return (
            sig["exposure"]["level"] == "high"
            and sig["modernization_need"]["level"] in ("medium", "high")
        )
    if profile_name == "opportunity_driven":
        return (
            sig["value_potential"]["level"] == "high"
            and sig["feasibility"]["level"] in ("medium", "high")
            and not any(f["class"] == "exposure" and f.get("severity") == "severe" for f in findings_in)
        )
    return False


DOMINANCE = ["critical", "strategic", "risk_driven", "opportunity_driven"]


def check_bundle(bundle, cat, errors):
    dims, subs, crits = catalog_index(cat)

    inst = bundle["assessment_instance"]
    opp_pack = bundle["opportunity_set"]
    ctx = bundle["contextualization"]
    rea = bundle["realization"]

    subjects = inst["subjects"]
    results = inst["results"]
    evidence = inst["evidence"]
    findings = inst["findings"]
    opportunities = opp_pack["opportunities"]
    objectives = opp_pack.get("objectives", [])
    targets = opp_pack.get("target_positions", [])
    templates = ctx.get("templates", [])
    implications = ctx.get("implications", [])
    interventions = rea.get("interventions", [])
    capabilities = rea.get("capability_implications", [])
    decisions = rea.get("decisions", [])
    initiatives = rea.get("initiatives", [])
    outcomes = rea.get("outcomes", [])
    values = rea.get("value_realizations", [])

    subj_ids = set(collect_ids(subjects, "id"))
    res_ids = set(collect_ids(results, "id"))
    ev_ids = set(collect_ids(evidence, "id"))
    fn_ids = set(collect_ids(findings, "id"))
    opp_ids = set(collect_ids(opportunities, "id"))
    obj_ids = set(collect_ids(objectives, "id"))
    tgt_ids = set(collect_ids(targets, "id"))
    it_ids = set(collect_ids(templates, "id"))
    imp_ids = set(collect_ids(implications, "id"))
    iv_ids = set(collect_ids(interventions, "id"))
    cap_ids = set(collect_ids(capabilities, "id"))
    dec_ids = set(collect_ids(decisions, "id"))
    init_ids = set(collect_ids(initiatives, "id"))
    out_ids = set(collect_ids(outcomes, "id"))
    vr_ids = set(collect_ids(values, "id"))

    def expect(cond, msg):
        if not cond:
            fail(errors, msg)

    def refs_ok(value, universe, label):
        expect(value in universe, "%s: %r not found" % (label, value))

    # results: uniqueness, subject, criterion, gap arithmetic
    seen_pairs = set()
    for res in results:
        refs_ok(res["subject"], subj_ids, "result %s subject" % res["id"])
        expect(criterion_exists(res["criterion"], dims, subs, crits),
               "result %s criterion %s not in catalog" % (res["id"], res["criterion"]))
        pair = (res["subject"], res["criterion"])
        expect(pair not in seen_pairs, "duplicate (subject, criterion): %r" % (pair,))
        seen_pairs.add(pair)
        if res.get("applicable") == "yes":
            expect("score" in res, "result %s: applicable but no score" % res["id"])
            if "target" in res and "score" in res:
                expect(res.get("gap") == res["target"] - res["score"],
                       "result %s: gap %r != target - score" % (res["id"], res.get("gap")))
            if res.get("score") in (1, 5):
                expect(res.get("anchor_rationale"), "result %s: extreme score without anchor_rationale (R-SCO-1)" % res["id"])
        if "tolerance" in res:
            expect(res["assessment_type"] == "exposure", "result %s: tolerance outside an exposure result" % res["id"])
        if "committed" in res:
            expect(res["assessment_type"] == "demand", "result %s: committed outside a demand result" % res["id"])

    # evidence: refs, staleness, conflicts
    assessment_date = d(inst["assessment"]["date"])
    window = months_before(assessment_date, 12)
    for ev in evidence:
        refs_ok(ev["subject"], subj_ids, "evidence %s subject" % ev["id"])
        expect(criterion_exists(ev["criterion"], dims, subs, crits),
               "evidence %s criterion %s not in catalog" % (ev["id"], ev["criterion"]))
        if "result" in ev:
            refs_ok(ev["result"], res_ids, "evidence %s result" % ev["id"])
        if ev.get("relation") == "conflicts":
            expect(ev.get("resolves_conflict"), "evidence %s conflicts without resolution record (R-CONF-3)" % ev["id"])
            if ev.get("resolves_conflict"):
                refs_ok(ev["resolves_conflict"], ev_ids, "evidence %s resolution ref" % ev["id"])
                expect(any(e["id"] == ev["resolves_conflict"] and e.get("result") == ev.get("result")
                           for e in evidence),
                       "evidence %s resolves against a different result" % ev["id"])
        if ev.get("status") != "superseded" and "date" in ev:
            expect(d(ev["date"]) >= window,
                   "evidence %s stale for a condition context (R-CONF-2)" % ev["id"])

    # extreme-score corroboration and confidence caps
    for res in results:
        if res.get("applicable") != "yes" or res.get("score") not in (1, 5):
            continue
        sup = supporting_evidence_for(res["id"], evidence)
        sources = {s.get("source") for s in sup}
        direct = [s for s in sup if s.get("class") == "direct"]
        expect(len(sup) >= 2 and len(direct) >= 1 and len(sources) >= 2,
               "result %s: extreme score uncorroborated (R-SUF-2)" % res["id"])
        if len(sup) < 2 or len(direct) < 1 or len(sources) < 2:
            expect(res.get("confidence") in ("low", "medium"),
                   "result %s: uncorroborated extreme above confidence cap" % res["id"])

    # findings: refs, floor, class, severity
    for fn in findings:
        for rid in fn["basis"]:
            refs_ok(rid, res_ids, "finding %s basis" % fn["id"])
        for eid in fn.get("evidence", []):
            refs_ok(eid, ev_ids, "finding %s evidence" % fn["id"])
        for rid in fn["basis"]:
            res = next(r for r in results if r["id"] == rid)
            expect(res.get("confidence") in ("medium", "high"),
                   "finding %s basis %s below the medium floor (R-FLR-1)" % (fn["id"], rid))
        expect(finding_class_ok(fn, {r["id"]: r for r in results}),
               "finding %s: class %s not derivable from its basis (R-FND-1..5)" % (fn["id"], fn["class"]))
        if fn["class"] == "strength":
            expect("severity" not in fn, "finding %s: strength carries severity (R-SEV-5)" % fn["id"])
        else:
            derived = "minor"
            for rid in fn["basis"]:
                res = next(r for r in results if r["id"] == rid)
                if SEV_RANK[derive_severity(res)] > SEV_RANK[derived]:
                    derived = derive_severity(res)
            expect(fn.get("severity") == derived,
                   "finding %s: severity %r != derived %r (R-SEV-1..4)" % (fn["id"], fn.get("severity"), derived))

    # opportunities: refs, required content semantics, profiles, parking
    findings_by_id = index_by(findings, "id")
    for opp in opportunities:
        for key in ("finding_ids", "asset_findings", "constraint_findings"):
            for fid in opp.get(key, []):
                refs_ok(fid, fn_ids, "opportunity %s %s" % (opp["id"], key))
        for dim in opp["dimensions"]:
            expect(criterion_exists(dim, dims, subs, crits),
                   "opportunity %s dimension %s not in catalog" % (opp["id"], dim))
        for g in opp["closes_gap_profile"]:
            expect(criterion_exists(g["criterion"], dims, subs, crits),
                   "opportunity %s gap criterion %s not in catalog" % (opp["id"], g["criterion"]))
            if "result" in g:
                refs_ok(g["result"], res_ids, "opportunity %s gap result" % opp["id"])
                res = next(r for r in results if r["id"] == g["result"])
                expect(g["target"] == res.get("target"),
                       "opportunity %s: gap target %r != result %s target %r" % (opp["id"], g["target"], res["id"], res.get("target")))
        refs_ok(opp["target_position"], tgt_ids, "opportunity %s target_position" % opp["id"])
        for fid in opp["finding_ids"]:
            fn = findings_by_id.get(fid)
            expect(fn is not None and fn.get("status") != "parked",
                   "opportunity %s draws parked finding %s" % (opp["id"], fid))
        findings_in = [findings_by_id[fid] for fid in opp["finding_ids"] if fid in findings_by_id]
        sig = opp["significance"]
        for factor, entry in sig.items():
            for b in entry["basis"]:
                if re.match(r"^(F|RES|EV|O|SUB)-", b):
                    known = b in fn_ids or b in res_ids or b in ev_ids or b in opp_ids or b in subj_ids
                    expect(known, "opportunity %s factor %s cites %s which does not exist" % (opp["id"], factor, b))
        sat = [p for p in DOMINANCE if profile_satisfied(p, sig, findings_in, True)]
        if opp.get("status") == "standby":
            # R-PRI-4: nothing satisfied is standby with a recorded review
            # date, never force-fit.
            expect(not sat, "opportunity %s is standby but satisfies %r (R-PRI-4)" % (opp["id"], sat))
            expect(opp["profile"]["primary"] == "standby",
                   "opportunity %s: standby requires profile primary standby (R-PRI-4)" % opp["id"])
            expect(opp.get("review_date"), "opportunity %s: standby without a review date (R-PRI-4)" % opp["id"])
        else:
            expect(sat, "opportunity %s satisfies no profile; status should be standby (R-PRI-4)" % opp["id"])
            expect(opp["profile"]["primary"] == sat[0],
                   "opportunity %s: primary %r != first satisfied %r (R-PRI-4 dominance)" % (opp["id"], opp["profile"]["primary"], sat[0]))
            if "secondary" in opp["profile"]:
                expect(opp["profile"]["secondary"] in sat[1:],
                       "opportunity %s: secondary %r not satisfied" % (opp["id"], opp["profile"]["secondary"]))

    # R-OPP-2: every severe or material finding drawn in or parked
    drawn = set()
    for opp in opportunities:
        drawn.update(opp["finding_ids"])
        drawn.update(opp.get("asset_findings", []))
        drawn.update(opp.get("constraint_findings", []))
    for fn in findings:
        if fn["class"] == "strength":
            continue
        if fn.get("severity") in ("material", "severe"):
            expect(fn["id"] in drawn or "parked" in (fn.get("notes") or ""),
                   "finding %s (%s) neither drawn into an opportunity nor parked (R-OPP-2)" % (fn["id"], fn.get("severity")))

    # objectives and dependencies
    for ob in objectives:
        refs_ok(ob["opportunity"], opp_ids, "objective %s opportunity" % ob["id"])
        for dep in ob.get("dependencies", []):
            refs_ok(dep["id"], opp_ids | init_ids | obj_ids | iv_ids | out_ids,
                   "objective %s dependency" % ob["id"])
            expect(dep.get("basis"), "objective %s dependency without basis (R-PRI-6)" % ob["id"])

    for tgt in targets:
        for rid in tgt.get("derived_from_results", []):
            refs_ok(rid, res_ids, "target %s derived_from" % tgt["id"])

    # contextualization: refs, templates, co-occurrence
    for imp in implications:
        expect(criterion_exists(imp["criterion"], dims, subs, crits),
               "implication %s criterion %s not in catalog" % (imp["id"], imp["criterion"]))
        for co in imp.get("co_occurrence_with", []):
            expect(criterion_exists(co, dims, subs, crits),
                   "implication %s co_occurrence %s not in catalog" % (imp["id"], co))
        if "template" in imp:
            refs_ok(imp["template"], it_ids, "implication %s template" % imp["id"])
        expect(imp.get("provenance"), "implication %s without provenance" % imp["id"])

    # realization: refs and chain coverage
    for iv in interventions:
        refs_ok(iv["opportunity"], opp_ids, "intervention %s opportunity" % iv["id"])
    for cap in capabilities:
        refs_ok(cap["intervention"], iv_ids, "capability %s intervention" % cap["id"])
        if "affected_dimension" in cap:
            expect(criterion_exists(cap["affected_dimension"], dims, subs, crits),
                   "capability %s affected_dimension not in catalog" % cap["id"])
    option_ids = set()
    for opp in opportunities:
        for opt in opp.get("option_set", []):
            option_ids.add(opt["id"])
    for dec in decisions:
        if "intervention" in dec:
            refs_ok(dec["intervention"], iv_ids, "decision %s intervention" % dec["id"])
        if "decides" in dec:
            refs_ok(dec["decides"], iv_ids, "decision %s decides" % dec["id"])
        for opt in dec.get("options_considered", []):
            refs_ok(opt, option_ids, "decision %s option" % dec["id"])
    stage_closes = set()
    for ini in initiatives:
        if "intervention" in ini:
            refs_ok(ini["intervention"], iv_ids, "initiative %s intervention" % ini["id"])
        for dep in ini.get("depends_on", []):
            refs_ok(dep, init_ids, "initiative %s depends_on" % ini["id"])
        for pre in ini.get("preparatory", []):
            refs_ok(pre, init_ids, "initiative %s preparatory" % ini["id"])
        for fid in ini.get("closes_findings", []):
            refs_ok(fid, fn_ids, "initiative %s closes_findings" % ini["id"])
            stage_closes.add(fid)
        for ob in ini.get("objectives", []):
            refs_ok(ob, obj_ids, "initiative %s objective" % ini["id"])
        for st in ini.get("stages", []):
            for fid in st.get("closes", []):
                refs_ok(fid, fn_ids, "initiative %s stage %s closes" % (ini["id"], st["id"]))
                stage_closes.add(fid)
    for out in outcomes:
        if "initiative" in out:
            refs_ok(out["initiative"], init_ids, "outcome %s initiative" % out["id"])
    for vr in values:
        if "outcome" in vr:
            refs_ok(vr["outcome"], out_ids, "value %s outcome" % vr["id"])
        if "opportunity" in vr:
            refs_ok(vr["opportunity"], opp_ids, "value %s opportunity" % vr["id"])
        for fid in vr.get("basis_findings", []):
            refs_ok(fid, fn_ids, "value %s basis_findings" % vr["id"])
        if vr.get("status") == "evidenced":
            expect(vr.get("successor_assessment") is None or isinstance(vr.get("successor_assessment"), str),
                   "value %s successor_assessment malformed" % vr["id"])

    # end-to-end chain: severe/material findings closed by some stage (or parked)
    for fn in findings:
        if fn["class"] == "strength" or fn.get("severity") not in ("material", "severe"):
            continue
        expect(fn["id"] in stage_closes or "parked" in (fn.get("notes") or ""),
               "finding %s never closed by any initiative stage; value chain incomplete (R-PREP-1)" % fn["id"])

    # Opportunities without an intervention are legitimate (a fresh
    # assessment yields opportunities before any committed change), so the
    # chain check here covers findings-to-findings coverage, not forced
    # realization. The example's realization tail exercises O-1 only; O-2
    # stays a recorded enabling dependency (R-PRI-6).

    return {
        "subjects": len(subjects),
        "results": len(results),
        "evidence": len(evidence),
        "findings": len(findings),
        "opportunities": len(opportunities),
        "implications": len(implications),
        "stages": sum(len(i.get("stages", [])) for i in initiatives),
        "values": len(values),
    }


SEV_RANK = {"minor": 0, "moderate": 1, "material": 2, "severe": 3}


def check_metamodel(manifest, rules, cat, parser, errors):
    def expect(cond, msg):
        if not cond:
            fail(errors, msg)

    # every artifact the manifest declares parses as machine-readable YAML
    for art in manifest.get("artifacts", []):
        for fname in ([art["file"]] if "file" in art else []) + art.get("files", []):
            expect(os.path.isfile(os.path.join(HERE, "metamodel", fname)),
                   "metamodel: declared artifact file %s missing" % fname)
    for pkg in manifest.get("entity_packages", []):
        expect(os.path.isfile(os.path.join(HERE, "metamodel", pkg["home"])),
               "metamodel: entity package home %s missing" % pkg["home"])

    rels = manifest.get("relationships", [])
    expect(len(rels) == 30, "metamodel: expected 30 relationships, found %d" % len(rels))
    ids = [r.get("id") for r in rels]
    expect(len(set(ids)) == len(ids), "metamodel: duplicate relationship ids")
    for r in rels:
        expect(re.match(r"^R-[0-9]{2}$", r.get("id", "")),
               "metamodel: relationship id %r malformed" % r.get("id"))
    kinds = manifest["relationship_vocabulary"]["amaf_kinds"]
    for r in rels:
        expect(r.get("kind") in kinds,
               "metamodel: relationship %s kind %r not in ama_kinds" % (r.get("id"), r.get("kind")))
        expect(r.get("opendea") is None or isinstance(r.get("opendea"), str),
               "metamodel: relationship %s opendea mapping malformed" % r.get("id"))
    doc_numbers = sorted({r["doc"] for r in rels if isinstance(r.get("doc"), int)})
    expect(doc_numbers == list(range(1, 19)),
           "metamodel: documented relationships 1-18 not fully covered: %r" % doc_numbers)

    # rule set: unique ids, shape, catalog version
    expect(rules["rule_set"]["catalog_version"] == cat["version"],
           "rules: catalog_version %r != catalog %r" % (rules["rule_set"]["catalog_version"], cat["version"]))
    rule_ids = [r.get("id") for r in rules.get("rules", [])]
    expect(len(set(rule_ids)) == len(rule_ids), "rules: duplicate rule ids")
    for rid in rule_ids:
        expect(re.match(r"^R-[A-Z]+-[0-9]+$", rid), "rules: rule id %r malformed" % rid)
    kinds_seen = {r.get("kind") for r in rules["rules"]}
    expect(kinds_seen <= {"scoring", "confidence", "corroboration", "sufficiency", "aggregation",
                          "gap", "weighting", "maturity-bridge", "findings-floor", "finding-class",
                          "severity", "opportunity", "prioritization", "dependency"},
           "rules: unexpected rule kind(s): %r" % (kinds_seen,))

    # entity registry covers the model packages
    modeled = set()
    for pkg in manifest.get("entity_packages", []):
        modeled.update(pkg.get("entities", []))
    required_entities = {
        "assessment-framework", "assessment-dimension", "assessment-subdimension",
        "assessment-criterion", "assessment-scale", "architecture-domain",
        "architecture-concern", "assessment-method", "assessment-rule",
        "assessment", "assessment-subject", "assessment-result", "evidence",
        "assessment-finding",
        "modernization-opportunity", "modernization-objective", "target-architecture",
        "domain-pack", "implication-template", "domain-implication",
        "modernization-intervention", "capability-implication", "architecture-decision",
        "modernization-initiative", "outcome", "value-realization",
    }
    missing = required_entities - modeled
    expect(not missing, "metamodel: entity registry missing: %r" % sorted(missing))


BUNDLE_FILES = [
    "framework/examples/integration-instance.yaml",
    "framework/examples/onboarding-instance.yaml",
    "framework/examples/integration-reassessment.yaml",
]


def main():
    errors = []
    parser = load_parser()

    cat = json.load(open(os.path.join(REPO, "tools", "criterion-catalog", "criteria-catalog.json"), encoding="utf-8"))
    manifest = load_yaml(parser, "framework/metamodel/amaf-metamodel.yaml")
    rules = load_yaml(parser, "framework/rules/amaf-rules.yaml")

    # map YAML schema relationships / metamodel entities if present in file form
    rel_schema = load_schema("relationship.schema.json")
    common = load_schema("common.schema.json")
    for r in manifest.get("relationships", []):
        check_schema(r, rel_schema, "relationship %s" % r.get("id"), errors, rel_schema, common)

    check_metamodel(manifest, rules, cat, parser, errors)

    # every worked example bundle validates against the schemas and the
    # rule set is re-derived over each (S7: multi-bundle validation)
    total = {}
    bundle_stats = []
    for relpath in BUNDLE_FILES:
        bundle = load_yaml(parser, relpath)
        label = os.path.basename(relpath)
        validate_doc(bundle["assessment_instance"], "assessment-instance.schema.json", errors, "%s instance" % label)
        validate_doc(bundle["opportunity_set"], "modernization-opportunity.schema.json", errors, "%s opportunity_set" % label)
        validate_doc(bundle["contextualization"], "architecture-contextualization.schema.json", errors, "%s contextualization" % label)
        validate_doc(bundle["realization"], "modernization-realization.schema.json", errors, "%s realization" % label)
        stats = check_bundle(bundle, cat, errors)
        stats["label"] = label
        bundle_stats.append(stats)
        for k, v in stats.items():
            if isinstance(v, int):
                total[k] = total.get(k, 0) + v

    if errors:
        print("NOT OK (%d)" % len(errors))
        for e in errors:
            print("  -", e)
        return 1
    parts = []
    for st in bundle_stats:
        parts.append("%s (%d results, %d evidence, %d findings, %d opportunities, %d implications, %d stages)" % (
            st["label"], st["results"], st["evidence"], st["findings"], st["opportunities"],
            st["implications"], st["stages"]))
    print("ok: %d instance bundles, 4 package schemas, relationship registry, rule set, catalog cross-checks; " % len(bundle_stats)
          + "; ".join(parts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
