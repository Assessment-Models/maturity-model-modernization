#!/usr/bin/env python3
"""AMAF criterion catalog validator (stdlib only).

The sibling of the maturity model's Level 1 validator
(scripts/local_validate.py), covering the AMAF catalog to the same
machine-checking standard (ROADMAP slice S9). Three families of checks:

1. Schema: every criterion carries exactly the modeled attribute set
   (16 fields), with the expected type per attribute, valid assessment
   types, modeled status, non-empty prose fields, structured list
   fields, and catalog structure (8 dimensions D1..D8, subdimension and
   criterion id patterns, unique ids, 10 unique domains).
2. ID stability: the catalog's dimensional, subdimensional and
   criterion identity (ids and names) matches the committed baseline
   (framework/ids/criteria-baseline.txt) exactly, in both directions:
   no ID disappears, none appears, none is renamed, without a
   deliberate baseline update in the same change-set.
3. Cross-reference integrity: every related_criteria and
   domain_applicability entry resolves to a defined catalog object;
   no criterion references itself.

Plus version coherence: the catalog version declared by the YAML source
agrees with the committed JSON export, the app embed
(tools/assessment-app/catalog.js), and the machine rule set pin
(framework/rules/amaf-rules.yaml), and the independent
assessment_rules / interpretation_rules counters agree between source
and export.

YAML loading reuses the catalog exporter parser
(tools/criterion-catalog/export-catalog.py). Exit 0 with one line of
output means ok; exit 1 lists every failure.

Usage: python3 framework/validate_catalog.py
"""

import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

CATALOG_YAML = os.path.join(REPO, "tools", "criterion-catalog", "criteria-catalog.yaml")
CATALOG_JSON = os.path.join(REPO, "tools", "criterion-catalog", "criteria-catalog.json")
BASELINE = os.path.join(HERE, "ids", "criteria-baseline.txt")
RULES = os.path.join(HERE, "rules", "amaf-rules.yaml")
EMBED = os.path.join(REPO, "tools", "assessment-app", "catalog.js")

EXPECTED_DIMENSIONS = 8
EXPECTED_DOMAINS = 10
EXPECTED_CRITERIA = 49

ASSESSMENT_TYPES = {"condition", "demand", "exposure", "readiness",
                    "target", "criticality", "changeability"}

TEXT_FIELDS = ("name", "proposition", "definition", "assessment_intent",
               "assessment_question", "applicability_rule", "assessment_method",
               "interpretation_guidance", "modernization_relevance")

CRITERION_KEYS = {"id", "name", "proposition", "assessment_type", "status",
                  *TEXT_FIELDS, "scale_reference", "evidence_requirements",
                  "domain_applicability", "related_criteria"}


def load_parser():
    path = os.path.join(REPO, "tools", "criterion-catalog", "export-catalog.py")
    spec = importlib.util.spec_from_file_location("amaf_catalog_export", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def iter_criteria(cat):
    for dim in cat.get("dimensions") or []:
        for sub in dim.get("subdimensions") or []:
            for crit in sub.get("criteria") or []:
                yield dim, sub, crit


def check_schema(cat, errors):
    dims = cat.get("dimensions") or []
    if len(dims) != EXPECTED_DIMENSIONS:
        errors.append("dimensions: expected %d, found %d"
                      % (EXPECTED_DIMENSIONS, len(dims)))
    dim_ids = []

    for dim in dims:
        did = dim.get("id")
        if not re.match(r"^D[1-%d]$" % EXPECTED_DIMENSIONS, str(did)):
            errors.append("dimension id %r does not match pattern" % did)
        if did in dim_ids:
            errors.append("duplicate dimension id %r" % did)
        dim_ids.append(did)
        if not isinstance(dim.get("name"), str) or not dim["name"].strip():
            errors.append("dimension %s: missing name" % did)
        if not isinstance(dim.get("objective"), str) or not dim["objective"].strip():
            errors.append("dimension %s: missing objective" % did)

        sub_ids = []
        for sub in dim.get("subdimensions") or []:
            sid = sub.get("id")
            if not re.match(r"^%s\.\d+$" % did, str(sid)):
                errors.append("subdimension id %r does not sit under dimension %r" % (sid, did))
            if sid in sub_ids:
                errors.append("duplicate subdimension id %r" % sid)
            sub_ids.append(sid)
            if not isinstance(sub.get("name"), str) or not sub["name"].strip():
                errors.append("subdimension %s: missing name" % sid)
            if not sub.get("criteria"):
                errors.append("subdimension %s: missing criteria list" % sid)
            for crit in sub.get("criteria") or []:
                cid = crit.get("id")
                if not re.match(r"^%s\.\d+$" % sid, str(cid)):
                    errors.append("criterion id %r does not sit under subdimension %r" % (cid, sid))

    count = sum(1 for _ in iter_criteria(cat))
    if count != EXPECTED_CRITERIA:
        errors.append("criterion count: expected %d, found %d"
                      % (EXPECTED_CRITERIA, count))

    domains = cat.get("domains") or []
    dom_ids = [d.get("id") for d in domains]
    if len(dom_ids) != EXPECTED_DOMAINS or len(set(dom_ids)) != EXPECTED_DOMAINS:
        errors.append("domains: expected %d unique, found %r"
                      % (EXPECTED_DOMAINS, dom_ids))

    scale_ids = set()
    scales = ((cat.get("scales") or {}).get("criterion") or {})
    if scales.get("id"):
        scale_ids.add(scales["id"])

    crit_ids = []
    for _dim, _sub, crit in iter_criteria(cat):
        cid = crit.get("id")
        if cid in crit_ids:
            errors.append("duplicate criterion id %r" % cid)
        crit_ids.append(cid)

        extra = set(crit) - CRITERION_KEYS
        missing = CRITERION_KEYS - set(crit)
        if extra:
            errors.append("%s: unexpected keys %s" % (cid, sorted(extra)))
        if missing:
            errors.append("%s: missing keys %s" % (cid, sorted(missing)))

        if crit.get("status") != "modeled":
            errors.append("%s: status %r is not 'modeled'" % (cid, crit.get("status")))
        if crit.get("assessment_type") not in ASSESSMENT_TYPES:
            errors.append("%s: assessment_type %r not in %s"
                          % (cid, crit.get("assessment_type"), sorted(ASSESSMENT_TYPES)))
        for key in ("proposition",) + TEXT_FIELDS:
            if not isinstance(crit.get(key), str) or not crit[key].strip():
                errors.append("%s: %s must be non-empty text" % (cid, key))
        if crit.get("scale_reference") not in scale_ids:
            errors.append("%s: scale_reference %r not a declared scale"
                          % (cid, crit.get("scale_reference")))
        ev = crit.get("evidence_requirements")
        if not isinstance(ev, list) or not ev:
            errors.append("%s: evidence_requirements must be a non-empty list" % cid)
        elif not all(isinstance(e, str) and e.strip() for e in ev):
            errors.append("%s: evidence_requirements entries must be non-empty text" % cid)
        da = crit.get("domain_applicability")
        if not isinstance(da, list):
            errors.append("%s: domain_applicability must be a list" % cid)
        elif not all(d in dom_ids for d in da):
            errors.append("%s: domain_applicability entries unresolved: %r"
                         % (cid, [d for d in da if d not in dom_ids]))
        rc = crit.get("related_criteria")
        if not isinstance(rc, list):
            errors.append("%s: related_criteria must be a list" % cid)
        elif any(not isinstance(r, str) or not r.strip() for r in rc):
            errors.append("%s: related_criteria entries must be non-empty ids" % cid)
    return crit_ids


def check_cross_references(cat, crit_ids, errors):
    crit_set = set(crit_ids)
    dom_set = set(d.get("id") for d in cat.get("domains") or [])
    for _dim, _sub, crit in iter_criteria(cat):
        cid = crit.get("id")
        for ref in crit.get("related_criteria") or []:
            if ref == cid:
                errors.append("%s: related_criteria points at itself" % cid)
            elif ref not in crit_set:
                errors.append("%s: related_criteria %r does not resolve" % (cid, ref))
        for ref in crit.get("domain_applicability") or []:
            if ref not in dom_set:
                errors.append("%s: domain_applicability %r does not resolve" % (cid, ref))
    dangling = sorted(set(
        ref
        for _d, _s, c in iter_criteria(cat)
        for ref in (c.get("related_criteria") or [])
        if ref not in crit_set))
    if dangling:
        errors.append("cross-reference summary, unresolved related_criteria: %r" % dangling)


def parse_baseline(errors):
    if not os.path.isfile(BASELINE):
        errors.append("missing baseline: framework/ids/criteria-baseline.txt")
        return None
    records = {"dimension": [], "subdimension": [], "criterion": []}
    with open(BASELINE, encoding="utf-8") as fh:
        for no, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split(None, 2)
            if len(parts) != 3 or parts[0] not in records:
                errors.append("baseline line %d: malformed record %r" % (no, line))
                continue
            records[parts[0]].append((parts[1], parts[2]))
    return records


def check_id_stability(cat, baseline, errors):
    if baseline is None:
        return
    for kind, actual in (
        ("dimension", [(d.get("id"), d.get("name")) for d in cat.get("dimensions") or []]),
        ("subdimension", [(s.get("id"), s.get("name"))
                          for d in cat.get("dimensions") or []
                          for s in d.get("subdimensions") or []]),
        ("criterion", [(c.get("id"), c.get("name")) for _d, _s, c in iter_criteria(cat)]),
    ):
        want = baseline[kind]
        want_map = dict(want)
        actual_map = {}
        for rid, name in actual:
            if rid in actual_map:
                errors.append("baseline %s: duplicate catalog id %r" % (kind, rid))
            actual_map[rid] = name
        for rid, name in want_map.items():
            if rid not in actual_map:
                errors.append("baseline %s %s (%s) absent from catalog; restoring it is "
                              "an id stability fix, otherwise update the baseline "
                              "deliberately" % (kind, rid, name))
            elif name is not None and actual_map[rid] != name:
                errors.append("baseline %s %s: name drift (baseline: %r)"
                              % (kind, rid, name))
        for rid, name in actual_map.items():
            if rid not in want_map:
                errors.append("catalog %s %r is not in the baseline; add it there in the "
                              "same change-set (ids are stable)" % (kind, rid))
            elif want_map[rid] is None or name is None:
                errors.append("catalog %s %r: missing name" % (kind, rid))


def check_version_coherence(cat, errors):
    # JSON export
    try:
        with open(CATALOG_JSON, encoding="utf-8") as fh:
            export = json.load(fh)
    except Exception as exc:
        errors.append("criteria-catalog.json unreadable: %s" % exc)
        export = {}
    if export.get("version") != cat.get("version"):
        errors.append("export version %r != catalog version %r"
                      % (export.get("version"), cat.get("version")))
    for counter in ("assessment_rules", "interpretation_rules"):
        got = (export.get(counter) or {}).get("version")
        want = (cat.get(counter) or {}).get("version")
        if want is None:
            errors.append("catalog is missing the %s counter" % counter)
        elif got != want:
            errors.append("export %s version %r != catalog %r"
                          % (counter, got, want))

    # rule-set pin
    parser = load_parser()
    rules = parser.parse(RULES)
    pin = ((rules.get("rule_set") or {}).get("catalog_version"))
    if pin != cat.get("version"):
        errors.append("rules catalog_version %r != catalog version %r"
                      % (pin, cat.get("version")))

    # app embed
    try:
        with open(EMBED, encoding="utf-8") as fh:
            embed = fh.read(4000)
    except Exception as exc:
        errors.append("catalog.js unreadable: %s" % exc)
        embed = ""
    header = re.search(r"machine export v([0-9.]+)", embed)
    if not header or header.group(1) != cat.get("version"):
        errors.append("catalog.js embed header does not declare catalog version %r"
                      % cat.get("version"))
    m = re.search(r'window\.AMAF_CATALOG\s*=\s*"?\{', embed)
    # the embedded payload follows the header; verify the version inside it
    m2 = re.search(r'"version":\s*"([0-9.]+)"', embed)
    if not m or not m2 or m2.group(1) != cat.get("version"):
        errors.append("catalog.js embedded payload version does not match %r" % cat.get("version"))


def main():
    errors = []
    parser = load_parser()
    try:
        cat = parser.parse(CATALOG_YAML)
    except SystemExit:
        raise
    except Exception as exc:
        print("FAIL - criteria-catalog.yaml does not parse: %s" % exc)
        return 1

    if cat.get("catalog") != "ama-framework":
        errors.append("catalog identity %r is not 'ama-framework'" % cat.get("catalog"))
    if cat.get("status") != "normative":
        errors.append("catalog status %r is not 'normative'" % cat.get("status"))

    crit_ids = check_schema(cat, errors)
    check_cross_references(cat, crit_ids, errors)
    check_id_stability(cat, parse_baseline(errors), errors)
    check_version_coherence(cat, errors)

    if errors:
        print("FAIL - %d error(s):" % len(errors))
        for e in errors:
            print("  - %s" % e)
        return 1
    print("ok: catalog %s valid; %d criteria; ids match baseline; versions coherent"
          % (cat.get("version"), len(crit_ids)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
