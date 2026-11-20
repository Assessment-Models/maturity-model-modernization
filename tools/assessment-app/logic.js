/* AMAF assessment instrument, logic layer (v1).
 * Pure functions implementing the assessment_rules (v1) and
 * interpretation_rules (v1) of the AMAF criterion catalog:
 * gap semantics, confidence assignment, extreme-score corroboration,
 * band profiles, descriptive statistics, criticality overlay,
 * finding candidates, severity derivation, CSV/JSON export.
 * No DOM access, no storage access; safe to run under Node for self tests.
 */
(function (root) {
  "use strict";

  var AMAF = {};
  AMAF.SCHEMA = "amaf-assessment";
  AMAF.SCHEMA_VERSION = 1;

  AMAF.LABELS = { 1: "Inadequate", 2: "Weak", 3: "Adequate", 4: "Strong", 5: "Leading" };
  AMAF.CONF_ORDER = { low: 0, medium: 1, high: 2 };
  AMAF.CRITICALITY = ["low", "medium", "high", "critical"];
  AMAF.CONFIDENCE = ["low", "medium", "high"];
  AMAF.APPLICABLE = ["yes", "no", "deferred"];
  AMAF.SEVERITY = ["minor", "moderate", "material", "severe"];
  AMAF.EVIDENCE_CLASSES = ["direct", "indirect"];
  AMAF.EVIDENCE_RELATIONS = ["supports", "conflicts"];

  /* ---------- instance model ---------- */

  AMAF.newInstance = function (assessmentId) {
    return {
      schema: AMAF.SCHEMA,
      schema_version: AMAF.SCHEMA_VERSION,
      assessment: { id: assessmentId || "", organization: "", date: "", scope: "" },
      subjects: [{ id: "s1", name: "Subject 1" }],
      results: {},
      evidence: [],
      findings: []
    };
  };

  AMAF.resultKey = function (subjectId, criterionId) {
    return subjectId + "|" + criterionId;
  };

  AMAF.getDefaultResult = function () {
    return {
      applicable: "",
      score: null,
      target: null,
      criticality: "",
      confidence: "",
      committed: false,
      tolerance: "",
      commentary: "",
      recommendation: ""
    };
  };

  AMAF.getResult = function (instance, subjectId, criterionId) {
    var k = AMAF.resultKey(subjectId, criterionId);
    var r = instance.results[k];
    var d = AMAF.getDefaultResult();
    if (r) {
      for (var p in d) {
        if (Object.prototype.hasOwnProperty.call(r, p)) d[p] = r[p];
      }
    }
    return d;
  };

  AMAF.setResult = function (instance, subjectId, criterionId, patch) {
    var k = AMAF.resultKey(subjectId, criterionId);
    var cur = instance.results[k];
    if (!cur) cur = instance.results[k] = AMAF.getDefaultResult();
    for (var p in patch) {
      if (Object.prototype.hasOwnProperty.call(patch, p)) cur[p] = patch[p];
    }
    if (cur.applicable !== "yes") {
      /* an inapplicable or deferred decision is recorded, not scored */
      if (cur.applicable === "no" || cur.applicable === "deferred") {
        cur.score = null;
      }
    }
    return cur;
  };

  AMAF.newEvidenceItem = function (subjectId, criterionId) {
    return {
      id: "E" + Math.floor(Math.random() * 1000000).toString(36),
      subjectId: subjectId,
      criterionId: criterionId,
      description: "",
      class: "direct",
      source: "",
      date: "",
      relation: "supports"
    };
  };

  AMAF.evidenceFor = function (instance, subjectId, criterionId) {
    return instance.evidence.filter(function (e) {
      return e.subjectId === subjectId && e.criterionId === criterionId;
    });
  };

  AMAF.subject = function (instance, subjectId) {
    for (var i = 0; i < instance.subjects.length; i++) {
      if (instance.subjects[i].id === subjectId) return instance.subjects[i];
    }
    return null;
  };

  /* ---------- catalog helpers ---------- */

  AMAF.flatten = function (catalog) {
    var out = [];
    catalog.dimensions.forEach(function (d) {
      d.subdimensions.forEach(function (s) {
        s.criteria.forEach(function (c) {
          out.push({
            criterion: c,
            dimensionId: d.id,
            dimensionName: d.id + " " + d.name,
            subdimensionId: s.id,
            subdimensionName: s.id + " " + s.name
          });
        });
      });
    });
    return out;
  };

  AMAF.criterionById = function (catalog, id) {
    var all = AMAF.flatten(catalog);
    for (var i = 0; i < all.length; i++) if (all[i].criterion.id === id) return all[i];
    return null;
  };

  /* ---------- gap semantics (assessment_rules.gap) ---------- */

  AMAF.gap = function (result) {
    if (result.applicable !== "yes") return null;
    if (typeof result.score !== "number" || typeof result.target !== "number") return null;
    return result.target - result.score;
  };

  AMAF.gapReads = function (gap) {
    if (gap === null || typeof gap !== "number") return "";
    if (gap > 0) return "shortfall of " + gap;
    if (gap === 0) return "no action";
    if (gap <= -2) return "overshoot of " + (-gap) + " (deliberate-excess review)";
    return "overshoot of " + (-gap);
  };

  /* ---------- confidence (assessment_rules.confidence) ---------- */

  function daysBetween(aIso, bIso) {
    var a = new Date(aIso), b = new Date(bIso);
    if (isNaN(a.getTime()) || isNaN(b.getTime())) return null;
    return Math.round((b.getTime() - a.getTime()) / 86400000);
  }

  AMAF.suggestedConfidence = function (items, assessmentDate, assessmentType) {
    var notes = [];
    if (!items || items.length === 0) {
      return { value: "low", notes: ["No evidence items; assertion level."] };
    }
    var conflicts = items.filter(function (e) { return e.relation === "conflicts"; });
    if (conflicts.length > 0) {
      return { value: "low", notes: ["Unresolved material conflict; unresolved conflict caps at low."] };
    }
    var direct = items.filter(function (e) { return e.class === "direct"; });
    var others = items.length - direct.length;
    var sources = {};
    items.forEach(function (e) { sources[(e.source || "") + "|" + (e.id || "")] = true; });
    var distinctSources = Object.keys(sources).length;

    var value;
    if (items.length >= 2 && direct.length >= 1 && distinctSources >= 2) {
      value = "high";
      notes.push("Two or more independent items, at least one direct.");
    } else if (direct.length >= 1 && others === 0 && items.length === 1) {
      value = "medium";
      notes.push("One direct item.");
    } else if (direct.length >= 1 && distinctSources < 2) {
      value = "medium";
      notes.push("Direct item(s) from a single source; independence not shown.");
    } else if (direct.length === 0 && distinctSources >= 2) {
      value = "medium";
      notes.push("Two or more indirect items from independent sources in agreement.");
    } else {
      value = "low";
      notes.push("Assertion-level or single indirect item only.");
    }

    if (assessmentType === "condition" && assessmentDate) {
      var stale = false;
      items.forEach(function (e) {
        var d = daysBetween(e.date, assessmentDate);
        if (d !== null && d > 365) stale = true;
      });
      if (stale) {
        value = AMAF.CONF_ORDER[value] > 0 ? ["", "low", "medium"][AMAF.CONF_ORDER[value]] : "low";
        notes.push("An item is older than 12 months; downgraded one level for a condition criterion.");
      }
    }
    return { value: value, notes: notes };
  };

  AMAF.corroboration = function (items) {
    /* extreme scores 1 and 5 need: >=2 items, >=1 direct, >=2 independent sources */
    var direct = (items || []).filter(function (e) { return e.class === "direct"; });
    var sources = {};
    (items || []).forEach(function (e) { sources[(e.source || "") + "|" + (e.id || "")] = true; });
    var ok = (items || []).length >= 2 && direct.length >= 1 && Object.keys(sources).length >= 2;
    return { ok: ok };
  };

  AMAF.effectiveConfidence = function (result, items, assessmentDate, assessmentType) {
    var sug = AMAF.suggestedConfidence(items, assessmentDate, assessmentType);
    var value = result.confidence || sug.value;
    var capped = false;
    var extreme = result.applicable === "yes" && (result.score === 1 || result.score === 5);
    if (extreme && result.score !== null) {
      var cor = AMAF.corroboration(items);
      if (!cor.ok && AMAF.CONF_ORDER[value] > AMAF.CONF_ORDER.medium) {
        value = "medium";
        capped = true;
      }
    }
    var notes = sug.notes.slice();
    if (capped) {
      notes.push("Extreme score without required corroboration; capped at medium and may not be the sole basis of a finding.");
    }
    return { value: value, suggested: sug.value, capped: capped, notes: notes };
  };

  /* ---------- profiles (assessment_rules.aggregation) ---------- */

  /* No arithmetic means anywhere: profiles are count-based, per assessment type. */

  AMAF.bandProfile = function (results) {
    /* results: [{score, assessmentType}] */
    var byType = {};
    var i, t, b;
    results.forEach(function (r) {
      t = r.assessmentType || "unknown";
      if (!byType[t]) byType[t] = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, count: 0 };
      byType[t][r.score]++;
      byType[t].count++;
    });
    var total = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, count: 0 };
    for (t in byType) {
      for (b = 1; b <= 5; b++) total[b] += byType[t][b];
      total.count += byType[t].count;
    }
    return { byType: byType, total: total };
  };

  AMAF.belowAdequacyShare = function (results) {
    /* score 2 or lower over applicable results; descriptive only */
    if (!results.length) return { share: null, below: 0, total: 0 };
    var below = results.filter(function (r) { return r.score <= 2; }).length;
    return { share: below / results.length, below: below, total: results.length };
  };

  AMAF.median = function (scores) {
    if (!scores.length) return null;
    var s = scores.slice().sort(function (a, b) { return a - b; });
    var mid = Math.floor(s.length / 2);
    return s.length % 2 ? s[mid] : (s[mid - 1] + s[mid]) / 2;
  };

  AMAF.minConfidence = function (confidences) {
    var vals = confidences.filter(function (c) { return c && AMAF.CONF_ORDER[c] !== undefined; });
    if (!vals.length) return null;
    var min = "high";
    vals.forEach(function (c) {
      if (AMAF.CONF_ORDER[c] < AMAF.CONF_ORDER[min]) min = c;
    });
    return min;
  };

  AMAF.criticalityOverlay = function (results) {
    /* high or critical results at or below adequacy (score <= 3) */
    return results.filter(function (r) {
      return (r.criticality === "high" || r.criticality === "critical") && r.score <= 3;
    }).length;
  };

  AMAF.profileFor = function (catalog, instance, subjectId, groupingId) {
    /* groupingId: dimension id or subdimension id */
    var rows = [];
    AMAF.flatten(catalog).forEach(function (entry) {
      if (groupingId && entry.dimensionId !== groupingId && entry.subdimensionId !== groupingId) return;
      var r = AMAF.getResult(instance, subjectId, entry.criterion.id);
      if (r.applicable === "yes" && typeof r.score === "number") {
        rows.push({
          resultKey: AMAF.resultKey(subjectId, entry.criterion.id),
          criterionId: entry.criterion.id,
          score: r.score,
          assessmentType: entry.criterion.assessment_type,
          confidence: r.confidence,
          criticality: r.criticality
        });
      }
    });
    var profile = AMAF.bandProfile(rows);
    var confidences = rows.map(function (r) { return r.confidence; });
    return {
      bands: profile,
      belowAdequacy: AMAF.belowAdequacyShare(rows),
      median: AMAF.median(rows.map(function (r) { return r.score; })),
      minConfidence: AMAF.minConfidence(confidences),
      criticalityOverlay: AMAF.criticalityOverlay(rows),
      resultKeys: rows.map(function (r) { return r.resultKey; })
    };
  };

  /* ---------- findings (interpretation_rules.findings) ---------- */

  /* interpretation_rules v2: a sustained deliberate-excess overshoot
   * (gap of -2 or less, score above target both bands) derives the same
   * class as a path constraint, against the target rationale. */
  AMAF.findingClass = function (score, assessmentType, gap) {
    if (score <= 2) {
      if (assessmentType === "condition" || assessmentType === "target") return "deficiency";
      if (assessmentType === "exposure") return "exposure";
      if (assessmentType === "demand") return "demand";
      if (assessmentType === "changeability" || assessmentType === "readiness") return "constraint";
      return null;
    }
    if (typeof gap === "number" && typeof score === "number" && score >= 3 && gap <= -2) {
      return "constraint";
    }
    return null;
  };

  AMAF.suggestedSeverity = function (result, assessmentType, gap) {
    var c = result.criticality;
    if (typeof result.score === "number" && result.score === 1) return "severe";
    if (typeof gap === "number" && gap >= 3) return "severe";
    if (assessmentType === "exposure" && result.tolerance === "outside" &&
        (c === "high" || c === "critical")) return "severe";
    if (typeof result.score === "number" && result.score === 2 &&
        (c === "high" || c === "critical")) return "material";
    if (assessmentType === "demand" && result.committed === true) return "material";
    if (typeof gap === "number" && gap === 2 && typeof result.score === "number" && result.score <= 2) return "material";
    if (typeof result.score === "number" && result.score === 2) return "moderate";
    if (typeof gap === "number" && gap === 2) return "moderate";
    return "minor";
  };

  AMAF.findingCandidates = function (catalog, instance, subjectId) {
    var assessmentDate = instance.assessment && instance.assessment.date;
    var out = [];
    AMAF.flatten(catalog).forEach(function (entry) {
      var cid = entry.criterion.id;
      var r = AMAF.getResult(instance, subjectId, cid);
      if (r.applicable !== "yes" || typeof r.score !== "number") return;
      var items = AMAF.evidenceFor(instance, subjectId, cid);
      var eff = AMAF.effectiveConfidence(r, items, assessmentDate, entry.criterion.assessment_type);
      var gap = AMAF.gap(r);
      var cls = AMAF.findingClass(r.score, entry.criterion.assessment_type, gap);
      var isStrength = r.score >= 4 && eff.value === "high";
      var extreme = r.score === 1 || r.score === 5;
      var corrob = extreme ? AMAF.corroboration(items) : { ok: true };
      if (cls) {
        out.push({
          kind: "candidate",
          resultKey: AMAF.resultKey(subjectId, cid),
          subjectId: subjectId,
          criterionId: cid,
          criterionName: entry.criterion.name,
          assessmentType: entry.criterion.assessment_type,
          cls: cls,
          score: r.score,
          target: r.target,
          gap: gap,
          confidence: eff.value,
          suggestedSeverity: AMAF.suggestedSeverity(r, entry.criterion.assessment_type, gap),
          belowFloor: eff.value === "low",
          soleExtremeUnverified: extreme && !corrob.ok,
          deliberateExcess: cls === "constraint" && typeof gap === "number" && gap <= -2 && r.score >= 3,
          notes: eff.notes
        });
      }
      if (isStrength) {
        out.push({
          kind: "strength",
          resultKey: AMAF.resultKey(subjectId, cid),
          subjectId: subjectId,
          criterionId: cid,
          criterionName: entry.criterion.name,
          assessmentType: entry.criterion.assessment_type,
          cls: "strength",
          score: r.score,
          target: r.target,
          gap: gap,
          confidence: eff.value,
          suggestedSeverity: null,
          belowFloor: false,
          soleExtremeUnverified: r.score === 5 && !corrob.ok,
          notes: []
        });
      }
    });
    return out;
  };

  AMAF.newFinding = function (subjectId) {
    return {
      id: "F" + Math.floor(Math.random() * 1000000).toString(36),
      subjectId: subjectId,
      cls: "deficiency",
      severity: "moderate",
      statement: "",
      basis: [],
      evidenceIds: [],
      severityOverride: false,
      notes: ""
    };
  };

  AMAF.findingWarnings = function (finding, instance, catalog) {
    var w = [];
    var count = 0;
    finding.basis.forEach(function (key) {
      var parts = key.split("|");
      var entry = AMAF.criterionById(catalog, parts[1]);
      if (!entry) return;
      var r = AMAF.getResult(instance, parts[0], parts[1]);
      var items = AMAF.evidenceFor(instance, parts[0], parts[1]);
      var eff = AMAF.effectiveConfidence(r, items, instance.assessment.date, entry.criterion.assessment_type);
      if (eff.value === "low") {
        w.push(entry.criterion.id + " is at low confidence.");
      }
      if ((r.score === 1 || r.score === 5) && !AMAF.corroboration(items).ok) {
        w.push(entry.criterion.id + " is an uncorroborated extreme score.");
      }
      count++;
    });
    if (count === 0) w.push("The finding has no basis results; a finding without basis is an assertion.");
    return w;
  };

  /* ---------- export ---------- */

  AMAF.csvEscape = function (v) {
    var s = v === null || v === undefined ? "" : String(v);
    if (/[",\n]/.test(s)) {
      return '"' + s.replace(/"/g, '""') + '"';
    }
    return s;
  };

  AMAF.CSV_COLUMNS = [
    "assessment_id", "subject", "dimension", "subdimension", "criterion_id",
    "criterion", "applicable", "score", "score_label", "criticality",
    "confidence", "target", "gap", "evidence", "commentary", "recommendation"
  ];

  AMAF.toCsv = function (catalog, instance) {
    var lines = [AMAF.CSV_COLUMNS.join(",")];
    var organized = [];
    instance.subjects.forEach(function (s) { organized.push(s); });
    AMAF.flatten(catalog).forEach(function (entry) {
      organized.forEach(function (s) {
        var r = instance.results[AMAF.resultKey(s.id, entry.criterion.id)];
        var has = !!r;
        var res = has ? r : AMAF.getDefaultResult();
        var items = AMAF.evidenceFor(instance, s.id, entry.criterion.id);
        var gap = has ? AMAF.gap(res) : null;
        var row = [
          instance.assessment.id,
          s.name,
          entry.dimensionName,
          entry.subdimensionName,
          entry.criterion.id,
          entry.criterion.name,
          has ? res.applicable : "",
          has && typeof res.score === "number" ? res.score : "",
          has && typeof res.score === "number" ? AMAF.LABELS[res.score] : "",
          has ? res.criticality : "",
          has ? res.confidence : "",
          has && typeof res.target === "number" ? res.target : "",
          typeof gap === "number" ? gap : "",
          items.map(function (e) { return e.description; }).filter(function (d) { return d; }).join("; "),
          has ? res.commentary : "",
          has ? res.recommendation : ""
        ];
        lines.push(row.map(AMAF.csvEscape).join(","));
      });
    });
    return lines.join("\n") + "\n";
  };

  AMAF.toJson = function (instance) {
    return JSON.stringify(instance, null, 2);
  };

  AMAF.fromJson = function (text) {
    var obj = JSON.parse(text);
    var errs = AMAF.validateInstance(obj);
    if (errs.length) throw new Error("Invalid instance: " + errs.join(" "));
    return obj;
  };

  AMAF.validateInstance = function (obj) {
    var errs = [];
    if (!obj || typeof obj !== "object") return ["not an object"];
    if (obj.schema !== AMAF.SCHEMA) errs.push("schema is " + JSON.stringify(obj.schema));
    if (obj.schema_version !== AMAF.SCHEMA_VERSION) errs.push("schema_version is " + JSON.stringify(obj.schema_version));
    if (!obj.assessment || typeof obj.assessment.id !== "string") errs.push("assessment.id missing");
    if (!Array.isArray(obj.subjects) || !obj.subjects.length) errs.push("subjects missing");
    if (!obj.results || typeof obj.results !== "object") errs.push("results missing");
    if (!Array.isArray(obj.evidence)) errs.push("evidence missing");
    if (!Array.isArray(obj.findings)) errs.push("findings missing");
    var ids = {};
    (obj.subjects || []).forEach(function (s) {
      if (!s || !s.id || typeof s.name !== "string") errs.push("bad subject " + JSON.stringify(s));
      if (s && ids[s.id]) errs.push("duplicate subject id " + s.id);
      if (s) ids[s.id] = true;
    });
    var critIds = {};
    (obj.evidence || []).forEach(function (e) {
      if (!e || !e.criterionId) errs.push("evidence item without criterionId");
      if (e) critIds[e.id] = (critIds[e.id] || 0) + 1;
      if (e && critIds[e.id] > 1) errs.push("duplicate evidence id " + e.id);
    });
    return errs;
  };

  /* export for browser and Node */
  if (typeof module !== "undefined" && module.exports) {
    module.exports = AMAF;
  } else {
    root.AMAF = AMAF;
  }
})(typeof window !== "undefined" ? window : globalThis);
