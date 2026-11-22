/* AMAF assessment instrument v1 self test. Run: node selftest.js
 * Exercises the catalog export, gap semantics, confidence assignment,
 * corroboration caps, band profiles, finding candidates, severity
 * derivation, CSV header equality with the scoring template, and the
 * JSON round trip. Exits nonzero on the first failure.
 */
"use strict";

var fs = require("fs");
var path = require("path");

global.window = {};
require("./catalog.js");
var CATALOG = global.window.AMAF_CATALOG;
var A = require("./logic.js");

var failures = 0;
function ok(cond, label) {
  if (cond) { console.log("PASS " + label); }
  else { failures++; console.log("FAIL " + label); }
}
function eq(actual, expected, label) {
  var same = JSON.stringify(actual) === JSON.stringify(expected);
  ok(same, label + (same ? "" : " (got " + JSON.stringify(actual) + ", want " + JSON.stringify(expected) + ")"));
}

/* catalog */
ok(CATALOG && CATALOG.catalog === "ama-framework", "catalog identity");
eq(CATALOG.version, "2.0.0", "catalog version");
var flat = A.flatten(CATALOG);
eq(flat.length, 49, "49 criteria");
ok(flat.every(function (e) { return e.criterion.status === "modeled"; }), "all criteria modeled");
var dims = {};
flat.forEach(function (e) { dims[e.dimensionId] = true; });
eq(Object.keys(dims).sort(), ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"], "dimensions D1 to D8");
ok(["D4.3.1", "D4.3.2", "D6.2.1", "D6.2.2"].every(function (id) { return A.criterionById(CATALOG, id); }), "split subdimension ids exist");
eq(CATALOG.assessment_rules.version, 1, "assessment_rules v1");
eq(CATALOG.interpretation_rules.version, 2, "interpretation_rules v2");
eq(CATALOG.scales.criterion.levels.map(function (l) { return l.label; }),
  ["Inadequate", "Weak", "Adequate", "Strong", "Leading"], "scale labels");

/* instance and results */
var inst = A.newInstance("TEST-1");
inst.assessment.date = "2026-06-30";
inst.subjects[0].name = "Integration architecture (portfolio)";
var sid = inst.subjects[0].id;
A.setResult(inst, sid, "D1.1.1", { applicable: "yes", score: 2, target: 4, criticality: "critical", confidence: "medium" });
eq(A.getResult(inst, sid, "D1.1.1").score, 2, "result stored");
eq(A.gap(A.getResult(inst, sid, "D1.1.1")), 2, "gap = target - score (worked example: 2 vs 4 -> 2)");
eq(A.gapReads(2), "shortfall of 2", "gap read");
eq(A.gapReads(-2), "overshoot of 2 (deliberate-excess review)", "oversoot review read");
eq(A.gap(A.getResult(inst, sid, "D1.1.1") === undefined ? {} : { applicable: "no", score: 2, target: 4 }), null, "inapplicable results carry no gap");

/* confidence */
var items = [
  { id: "E1", subjectId: sid, criterionId: "D1.1.1", description: "a", class: "direct", source: "srcA", date: "2026-06-01", relation: "supports" },
  { id: "E2", subjectId: sid, criterionId: "D1.1.1", description: "b", class: "indirect", source: "srcB", date: "2026-06-02", relation: "supports" }
];
eq(A.suggestedConfidence(items, "2026-06-30", "condition").value, "high", "two independent items, one direct -> high");
eq(A.suggestedConfidence([items[0]], "2026-06-30", "condition").value, "medium", "single direct item -> medium");
eq(A.suggestedConfidence([items[1]], "2026-06-30", "condition").value, "low", "single indirect item -> low");
eq(A.suggestedConfidence([items[1], { id: "E3", subjectId: sid, criterionId: "D1.1.1", description: "c", class: "indirect", source: "srcC", date: "2026-06-03", relation: "supports" }], "2026-06-30", "condition").value, "medium", "two independent indirect -> medium");
var conflict = items.concat([{ id: "E4", subjectId: sid, criterionId: "D1.1.1", description: "d", class: "direct", source: "srcD", date: "2026-06-04", relation: "conflicts" }]);
eq(A.suggestedConfidence(conflict, "2026-06-30", "condition").value, "low", "unresolved conflict caps at low");
var stale = { id: "E5", subjectId: sid, criterionId: "D1.1.1", description: "e", class: "direct", source: "srcE", date: "2024-01-01", relation: "supports" };
eq(A.suggestedConfidence([stale], "2026-06-30", "condition").value, "low", "stale direct item: medium downgraded one level to low");
eq(A.suggestedConfidence(items.concat([stale]), "2026-06-30", "condition").value, "medium", "stale downgrade applies to high too: one stale item in a set drops high to medium");

/* corroboration */
eq(A.corroboration(items).ok, true, "extreme corroboration satisfied");
eq(A.corroboration([items[0]]).ok, false, "single item does not corroborate an extreme score");
var r5 = { applicable: "yes", score: 5, confidence: "high", target: null };
var eff = A.effectiveConfidence(r5, [items[0]], "2026-06-30", "condition");
eq(eff.value, "medium", "uncorroborated extreme capped at medium");
ok(eff.capped, "cap flagged");
eq(A.effectiveConfidence(r5, items, "2026-06-30", "condition").value, "high", "corroborated extreme keeps high");
var r5storedLow = { applicable: "yes", score: 5, confidence: "low", target: null };
eq(A.effectiveConfidence(r5storedLow, items, "2026-06-30", "condition").value, "low", "cap never raises a stored low");

/* profiles */
var pro = [
  { score: 1, assessmentType: "condition" },
  { score: 2, assessmentType: "condition" },
  { score: 4, assessmentType: "condition" },
  { score: 3, assessmentType: "condition" },
  { score: 2, assessmentType: "demand" }
];
var bp = A.bandProfile(pro);
eq(bp.byType.condition.count, 4, "profile partitioned by type");
eq(bp.byType.condition[2], 1, "band counts (condition, band 2)");
eq(bp.byType.demand[2], 1, "band counts (demand kept separate, band 2)");
eq(bp.total.count, 5, "total count");
var share = A.belowAdequacyShare([{ score: 1 }, { score: 2 }, { score: 3 }]);
eq(Math.round(share.share * 1000) / 1000, 0.667, "below-adequacy share");
eq(A.median([1, 2, 3, 4]), 2.5, "median of even list");
eq(A.minConfidence(["high", "medium", "high"]), "medium", "minimum confidence");
eq(A.criticalityOverlay([{ criticality: "critical", score: 3 }, { criticality: "high", score: 2 }, { criticality: "critical", score: 4 }, { criticality: "medium", score: 1 }]), 2, "criticality overlay counts high/critical at or below adequacy");

/* finding candidates and severity */
A.setResult(inst, sid, "D5.4.1", { applicable: "yes", score: 1, target: 4, criticality: "high", confidence: "high" });
inst.evidence.push({ id: "E6", subjectId: sid, criterionId: "D5.4.1", description: "map", class: "direct", source: "srcF", date: "2026-06-01", relation: "supports" },
  { id: "E7", subjectId: sid, criterionId: "D5.4.1", description: "count", class: "indirect", source: "srcG", date: "2026-06-02", relation: "supports" });
var cands = A.findingCandidates(CATALOG, inst, sid);
var d541 = cands.filter(function (c) { return c.criterionId === "D5.4.1"; })[0];
ok(d541 && d541.cls === "deficiency", "condition score 1 -> deficiency candidate");
eq(d541.suggestedSeverity, "severe", "score 1 -> severe");
var d111 = cands.filter(function (c) { return c.criterionId === "D1.1.1"; })[0];
ok(d111 && d111.cls === "deficiency" && !d111.belowFloor, "worked example stays a candidate at medium confidence");
A.setResult(inst, sid, "D4.2.1", { applicable: "yes", score: 2, criticality: "high", confidence: "medium" });
var cands2 = A.findingCandidates(CATALOG, inst, sid);
var d421 = cands2.filter(function (c) { return c.criterionId === "D4.2.1"; })[0];
if (d421) {
  ok(d421.cls === "deficiency" || d421.cls === "constraint" || d421.cls === "exposure" || d421.cls === "demand",
    "candidate class derived from type (" + (d421 && A.criterionById(CATALOG, "D4.2.1").criterion.assessment_type) + " -> " + (d421 && d421.cls) + ")");
}
var sevProbe = A.suggestedSeverity({ applicable: "yes", score: 2, criticality: "crit", committed: false, tolerance: "" }, "exposure", 2);
eq(sevProbe, "material", "score 2 at high/critical criticality with gap 2 -> material");
var sevCommit = A.suggestedSeverity({ applicable: "yes", score: 2, criticality: "low", committed: true, tolerance: "" }, "demand", null);
eq(sevCommit, "material", "committed demand -> material");
var sevTol = A.suggestedSeverity({ applicable: "yes", score: 2, criticality: "critical", committed: false, tolerance: "outside" }, "exposure", null);
eq(sevTol, "severe", "exposure outside tolerance at critical criticality -> severe");
var sevMod = A.suggestedSeverity({ applicable: "yes", score: 2, criticality: "low", committed: false, tolerance: "" }, "condition", null);
eq(sevMod, "moderate", "score 2 without escalation -> moderate");

/* interpretation_rules v2: sustained deliberate-excess overshoot derives a
   constraint candidate (against the target rationale) at minor severity */
eq(A.findingClass(5, "exposure", -2), "constraint", "overshoot gap -2 -> constraint class (target rationale)");
eq(A.findingClass(5, "exposure", 0), null, "no overshoot, no class at score 5");
eq(A.findingClass(4, "condition", null), null, "score 4 without gap -> no class");
eq(A.findingClass(2, "changeability", null), "constraint", "score 2 changeability -> constraint (unchanged)");
eq(A.suggestedSeverity({ applicable: "yes", score: 5, criticality: "high", committed: false, tolerance: "" }, "exposure", -2), "minor", "sustained-overshoot constraint lands in minor");

/* strength class needs score >= 4 with high confidence */
A.setResult(inst, sid, "D2.1.1", { applicable: "yes", score: 5, confidence: "high" });
A.setResult(inst, sid, "D3.1.1", { applicable: "yes", score: 4, confidence: "low" });
var cands3 = A.findingCandidates(CATALOG, inst, sid);
ok(cands3.some(function (c) { return c.criterionId === "D2.1.1" && c.cls === "strength" && !c.soleExtremeUnverified; }) === false, "uncorroborated strength at score 5 flagged");
var c321 = A.findingCandidates(CATALOG, inst, sid);
var strengthCand = c321.filter(function (c) { return c.cls === "strength"; });
ok(strengthCand.every(function (c) { return c.criterionId !== "D3.1.1"; }), "strength requires high confidence");

/* CSV header equality with the scoring template */
var tplCsv = fs.readFileSync(path.join(__dirname, "..", "criterion-catalog", "scoring-template.csv"), "utf8");
var tplHeader = tplCsv.split(/\r?\n/)[0].split(",");
eq(A.CSV_COLUMNS, tplHeader, "CSV columns equal scoring template header");
var csv = A.toCsv(CATALOG, inst);
eq(csv.split(/\r?\n/)[0].split(","), tplHeader, "CSV export header row equals scoring template header");
var rows = csv.trim().split(/\n/);
eq(rows.length, 1 + 49 * inst.subjects.length, "CSV row count = header + criteria x subjects");
var first = rows[1].split(",");
eq(first[0], "TEST-1", "CSV assessment_id");
eq(first[1], "Integration architecture (portfolio)", "CSV subject name");
ok(first[6] === "yes" && first[7] === "2" && first[8] === "Weak" && first[9] === "critical" && first[10] === "medium" && first[11] === "4" && first[12] === "2", "CSV worked example row matches D1.1.1");
ok(rows.some(function (r) { return r.indexOf('E54' ) < 0; }), "no accidental template text");

/* JSON round trip */
var back = A.fromJson(A.toJson(inst));
eq(back.assessment.id, "TEST-1", "JSON round trip assessment id");
eq(Object.keys(back.results).length, Object.keys(inst.results).length, "JSON round trip results count");
ok(A.fromJson(A.toJson(inst)).evidence.length === inst.evidence.length, "JSON round trip evidence count");
var broken = JSON.parse(A.toJson(inst));
broken.schema = "wrong";
var errs = A.validateInstance(broken);
ok(errs.length > 0, "schema validation catches wrong schema");

/* CSV escaping */
eq(A.csvEscape('plain'), "plain", "plain CSV field untouched");
eq(A.csvEscape('has,comma'), '"has,comma"', "comma field quoted");
eq(A.csvEscape('say "hi"'), '"say ""hi"""', "quotes doubled");

console.log(failures === 0 ? "\nALL GREEN" : "\n" + failures + " FAILURE(S)");
process.exit(failures === 0 ? 0 : 1);
