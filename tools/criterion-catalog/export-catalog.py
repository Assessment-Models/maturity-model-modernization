#!/usr/bin/env python3
"""Export criteria-catalog.yaml to criteria-catalog.json.

Stdlib only. Parses the YAML subset used by the catalog file (nested
mappings and sequences with 2-step indents, folded scalars ">-" and ">",
flow lists, flow maps, quoted and plain scalars, full-line and trailing
comments), verifies catalog invariants, and writes the JSON export with
key order mirroring the source document.

Run from anywhere: paths resolve relative to this file.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "criteria-catalog.yaml")
DST = os.path.join(HERE, "criteria-catalog.json")


def strip_comment(line):
    out = []
    quote = None
    for ch in line:
        if quote:
            out.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ('"', "'"):
            quote = ch
            out.append(ch)
            continue
        if ch == "#" and out and out[-1] in (" ", "\t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def split_flow(s):
    parts, cur, depth, quote = [], [], 0, None
    for ch in s:
        if quote:
            cur.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ('"', "'"):
            quote = ch
            cur.append(ch)
            continue
        if ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    if cur:
        parts.append("".join(cur))
    return parts


def parse_flow(s):
    s = s.strip()
    if s == "":
        return None
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [parse_flow(p) for p in split_flow(inner)] if inner else []
    if s.startswith("{") and s.endswith("}"):
        inner = s[1:-1].strip()
        obj = {}
        if inner:
            for part in split_flow(inner):
                k, v = part.split(":", 1)
                obj[k.strip()] = parse_flow(v)
        return obj
    if len(s) > 1 and s[0] == s[-1] and s[0] in ('"', "'"):
        return s[1:-1]
    low = s.lower()
    if low in ("true", "false", "null"):
        return {"true": True, "false": False, "null": None}[low]
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


class Line:
    __slots__ = ("indent", "text", "no")

    def __init__(self, no, indent, text):
        self.no, self.indent, self.text = no, indent, text


def load_lines(path):
    lines = []
    with open(path, encoding="utf-8") as fh:
        for no, raw in enumerate(fh, 1):
            stripped = strip_comment(raw.rstrip("\n")).rstrip()
            if not stripped.strip():
                continue
            if stripped.lstrip().startswith("#"):
                continue
            lines.append(Line(no, len(stripped) - len(stripped.lstrip(" ")), stripped.strip()))
    return lines


KEY_RE = re.compile(r"^([A-Za-z0-9_][^:]*?):(\s+(.*))?$")


def parse_block(lines, i, indent):
    """Parse the block starting at lines[i] whose items sit at `indent`."""
    if lines[i].text.startswith("- ") or lines[i].text == "-":
        return parse_seq(lines, i, indent)
    return parse_map(lines, i, indent)


def parse_seq(lines, i, indent):
    items = []
    while i < len(lines) and lines[i].indent == indent and (lines[i].text.startswith("- ") or lines[i].text == "-"):
        rest = lines[i].text[2:].strip() if lines[i].text != "-" else ""
        if rest == "":
            i += 1
            if i < len(lines) and lines[i].indent > indent:
                val, i = parse_block(lines, i, lines[i].indent)
                items.append(val)
            else:
                items.append(None)
        elif KEY_RE.match(rest):
            synth = Line(lines[i].no, indent + 2, rest)
            val, i = parse_map(lines, i + 1, indent + 2, first=[synth])
            items.append(val)
        else:
            items.append(parse_flow(rest))
            i += 1
    return items, i


def parse_map(lines, i, indent, first=None):
    obj = {}
    pending = list(first) if first else []
    while pending or (i < len(lines) and lines[i].indent == indent):
        if pending:
            ln = pending.pop(0)
        else:
            ln = lines[i]
            i += 1
        m = KEY_RE.match(ln.text)
        if not m:
            raise SystemExit("line %d: not a mapping entry: %r" % (ln.no, ln.text))
        key, _, val = m.group(1), m.group(2) or "", m.group(3)
        key = key.strip()
        val = (val or "").strip()
        if val in (">-", ">", "|", "|-"):
            content = []
            while i < len(lines) and lines[i].indent > indent:
                content.append(lines[i].text)
                i += 1
            if val in ("|", "|-", ">", ">-"):
                pass
            obj[key] = " ".join(content).strip()
        elif val == "":
            if i < len(lines) and (lines[i].indent > indent or (lines[i].indent == indent and lines[i].text.startswith("- "))):
                if lines[i].indent == indent:
                    obj[key], i = parse_seq(lines, i, indent)
                else:
                    obj[key], i = parse_block(lines, i, lines[i].indent)
            else:
                obj[key] = None
        else:
            obj[key] = parse_flow(val)
    if i < len(lines) and lines[i].indent > indent:
        raise SystemExit("line %d: unconsumed deeper line: %r" % (lines[i].no, lines[i].text))
    return obj, i


def parse(path):
    lines = load_lines(path)
    val, i = parse_map(lines, 0, 0)
    if i != len(lines):
        raise SystemExit("stopped at line %d of %d: %r" % (lines[i].no, len(lines), lines[i].text))
    return val


def check(cat, fail):
    def err(msg):
        fail.append(msg)

    if cat.get("catalog") != "ama-framework":
        err("catalog")
    if cat.get("status") != "normative":
        err("status")
    if cat.get("version") != "0.4.0":
        err("version: %r" % cat.get("version"))
    labels = [lv["label"] for lv in cat["scales"]["criterion"]["levels"]]
    if labels != ["Inadequate", "Weak", "Adequate", "Strong", "Leading"]:
        err("scale labels: %r" % labels)
    if cat["criticality_scale"] != ["low", "medium", "high", "critical"]:
        err("criticality_scale")
    if cat["confidence_scale"] != ["low", "medium", "high"]:
        err("confidence_scale")
    if cat["assessment_rules"].get("version") != 1:
        err("assessment_rules.version")
    if cat["interpretation_rules"].get("version") != 1:
        err("interpretation_rules.version")
    dom_ids = [d["id"] for d in cat["domains"]]
    if len(dom_ids) != 10 or len(set(dom_ids)) != 10:
        err("domains: %r" % dom_ids)

    req = ["id", "name", "proposition", "assessment_type", "status", "definition",
           "assessment_intent", "assessment_question", "applicability_rule",
           "assessment_method", "scale_reference", "evidence_requirements",
           "interpretation_guidance", "modernization_relevance",
           "domain_applicability", "related_criteria"]
    types = {"condition", "demand", "exposure", "readiness", "target", "criticality", "changeability"}
    seen, count = {}, 0
    for dim in cat["dimensions"]:
        did = dim["id"]
        if not re.match(r"^D[1-8]$", did):
            err("dimension id %r" % did)
        for sub in dim["subdimensions"]:
            sid = sub["id"]
            if not re.match(r"^%s\.\d+$" % did, sid):
                err("subdimension id %r under %r" % (sid, did))
            for crit in sub["criteria"]:
                count += 1
                cid = crit["id"]
                if not re.match(r"^%s\.\d+$" % sid, cid):
                    err("criterion id %r under %r" % (cid, sid))
                if crit.get("status") != "modeled":
                    err("%s status %r" % (cid, crit.get("status")))
                if crit.get("assessment_type") not in types:
                    err("%s type %r" % (cid, crit.get("assessment_type")))
                for k in req:
                    if k not in crit:
                        err("%s missing %s" % (cid, k))
                if not isinstance(crit.get("evidence_requirements"), list) or not crit["evidence_requirements"]:
                    err("%s evidence_requirements" % cid)
                if not isinstance(crit.get("domain_applicability"), list):
                    err("%s domain_applicability" % cid)
                for d in crit.get("domain_applicability", []):
                    if d not in dom_ids:
                        err("%s domain_applicability %r" % (cid, d))
                for r in crit.get("related_criteria", []):
                    seen.setdefault(r, cid)
                seen[cid] = seen.get(cid)
    if count != 49:
        err("criterion count %d" % count)
    for want in ["D4.3.1", "D4.3.2", "D6.2.1", "D6.2.2", "D5.4.1", "D1.1.1"]:
        if want not in [c["id"] for d in cat["dimensions"] for s in d["subdimensions"] for c in s["criteria"]]:
            err("expected criterion %s" % want)
    d541 = [c for d in cat["dimensions"] for s in d["subdimensions"] for c in s["criteria"] if c["id"] == "D5.4.1"][0]
    if "Managed duplication is surviving design choice" not in d541["interpretation_guidance"]:
        err("D5.4.1 interpretation_guidance spot check")
    if "Duplication review" not in d541["assessment_method"]:
        err("D5.4.1 assessment_method spot check")
    linked = seen["D1.2.1"]
    if linked != "D1.1.1":
        err("related_criteria spot check: %r" % linked)


def write_json(cat):
    with open(DST, "w", encoding="utf-8") as fh:
        json.dump(cat, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    return os.path.getsize(DST)


APP_EMBED = os.path.join(HERE, "..", "assessment-app", "catalog.js")
EMBED_HEADER = """/* AMAF criterion catalog, machine export v{version} (embedded).
 * Generated by export-catalog.py; do not edit by hand. The embedded copy
 * lets the instrument run standalone from file:// and offline; a served
 * deployment may instead fetch criteria-catalog.json.
 */
window.AMAF_CATALOG = """


def write_embed(cat):
    target = os.path.normpath(APP_EMBED)
    if not os.path.isdir(os.path.dirname(target)):
        return None
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(EMBED_HEADER.format(version=cat.get("version", "?")))
        json.dump(cat, fh, indent=2, ensure_ascii=False)
        fh.write(";\n")
    return os.path.getsize(target)


def main():
    cat = parse(SRC)
    fail = []
    check(cat, fail)
    for f in fail:
        sys.stderr.write("FAIL %s\n" % f)
    if fail:
        sys.exit(1)
    size = write_json(cat)
    emb = write_embed(cat)
    msg = "ok: %d bytes, 49 criteria" % size
    if emb:
        msg += "; app embed %d bytes" % emb
    sys.stdout.write(msg + "\n")


if __name__ == "__main__":
    main()
