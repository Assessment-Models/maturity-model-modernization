/* AMAF assessment instrument v1, UI layer.
 * Wires the DOM to the pure functions in logic.js. Local-first:
 * autosaves to localStorage, exports JSON and CSV (scoring template
 * format), imports JSON. The v0.1 store under "amaf-v01" is left alone.
 */
(function () {
  "use strict";

  var catalog = window.AMAF_CATALOG;
  var AMAF = window.AMAF;
  var STORE_KEY = "amaf-instrument-store";
  var store = { instances: {}, current: null };
  var instance = null;
  var currentKey = null;
  var ui = {};

  /* ---------- tiny helpers ---------- */

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    attrs = attrs || {};
    Object.keys(attrs).forEach(function (k) {
      if (k === "class") node.className = attrs[k];
      else if (k === "text") node.textContent = attrs[k];
      else if (k === "html") node.innerHTML = attrs[k];
      else if (k.slice(0, 2) === "on") node.addEventListener(k.slice(2), attrs[k]);
      else node.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { if (c) node.appendChild(c); });
    return node;
  }
  function $(id) { return document.getElementById(id); }
  function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }
  function pick(list, value, titles) {
    var s = el("select");
    list.forEach(function (v, i) {
      var o = el("option", { value: v, text: titles ? titles[i] : v });
      if (String(v) === String(value)) o.selected = true;
      s.appendChild(o);
    });
    return s;
  }

  function save() {
    store.instances[currentKey] = instance;
    store.current = currentKey;
    try { localStorage.setItem(STORE_KEY, JSON.stringify(store)); }
    catch (e) { /* storage unavailable (e.g. some file:// contexts); exports still work */ }
  }
  function load() {
    try {
      var raw = localStorage.getItem(STORE_KEY);
      if (raw) store = JSON.parse(raw);
    } catch (e) { store = { instances: {}, current: null }; }
    if (!store.instances) store.instances = {};
    if (!store.current || !store.instances[store.current]) {
      var first = Object.keys(store.instances)[0] || null;
      store.current = first;
    }
    if (store.current) {
      currentKey = store.current;
      instance = store.instances[currentKey];
    } else {
      currentKey = "inst-" + Date.now().toString(36);
      instance = AMAF.newInstance("ASSESSMENT-1");
      store.instances[currentKey] = instance;
      store.current = currentKey;
      save();
    }
  }

  function download(name, text, type) {
    var blob = new Blob([text], { type: type || "text/plain;charset=utf-8" });
    var a = el("a", { href: URL.createObjectURL(blob), download: name });
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  function firstSubjectId() { return instance.subjects[0].id; }

  /* ---------- tabs ---------- */

  ui.tabs = {};
  ["instance", "scoring", "evidence", "profiles", "io"].forEach(function (name) {
    ui.tabs[name] = $("tab-" + name);
  });
  $("tabs").addEventListener("click", function (ev) {
    var btn = ev.target.closest("button");
    if (!btn) return;
    Object.keys(ui.tabs).forEach(function (t) {
      ui.tabs[t].classList.toggle("hidden", t !== btn.dataset.tab);
    });
    Array.prototype.forEach.call($("tabs").children, function (b) {
      b.classList.toggle("active", b === btn);
    });
    render();
  });
  function openTab(name) {
    var btn = $("tabs").querySelector('[data-tab="' + name + '"]');
    if (btn) btn.click();
    else render();
  }

  /* ---------- instance tab ---------- */

  function bindInstance() {
    if (boundOnce.instance) { syncInstanceFields(); return; }
    boundOnce.instance = true;
    [["f-assessment-id", "id"], ["f-organization", "organization"], ["f-date", "date"], ["f-scope", "scope"]].forEach(function (pair) {
      $(pair[0]).addEventListener("change", function () {
        instance.assessment[pair[1]] = $(pair[0]).value;
        save();
        renderSaved();
      });
    });
    $("add-subject").addEventListener("click", function () {
      var n = instance.subjects.length + 1;
      var used = {};
      instance.subjects.forEach(function (s) { used[s.id] = true; });
      var id = "s" + n;
      var k = n;
      while (used[id]) { k++; id = "s" + k; }
      instance.subjects.push({ id: id, name: "Subject " + k });
      save();
      render();
    });
    syncInstanceFields();
  }

  function syncInstanceFields() {
    $("f-assessment-id").value = instance.assessment.id;
    $("f-organization").value = instance.assessment.organization;
    $("f-date").value = instance.assessment.date;
    $("f-scope").value = instance.assessment.scope;
  }

  function renderSubjects() {
    var tb = $("subjects-table").querySelector("tbody");
    clear(tb);
    instance.subjects.forEach(function (s, idx) {
      var idInput = el("input", { type: "text", value: s.id });
      idInput.addEventListener("change", function () {
        var nid = idInput.value.trim();
        if (!nid || nid === s.id) { idInput.value = s.id; return; }
        var clash = instance.subjects.some(function (o) { return o.id === nid; });
        if (clash) { idInput.value = s.id; return; }
        Object.keys(instance.results).forEach(function (key) {
          if (key.indexOf(s.id + "|") === 0) {
            instance.results[nid + "|" + key.slice(s.id.length + 1)] = instance.results[key];
            delete instance.results[key];
          }
        });
        instance.evidence.forEach(function (e) { if (e.subjectId === s.id) e.subjectId = nid; });
        instance.findings.forEach(function (f) { if (f.subjectId === s.id) f.subjectId = nid; });
        s.id = nid;
        save();
        render();
      });
      var nameInput = el("input", { type: "text", value: s.name });
      nameInput.addEventListener("change", function () { s.name = nameInput.value; save(); renderSaved(); });
      var del = el("button", { class: "btn danger small", text: "Remove" });
      del.addEventListener("click", function () {
        var keys = Object.keys(instance.results).filter(function (k) { return k.indexOf(s.id + "|") === 0; });
        var msg = "Remove subject " + (s.name || s.id) + " with its " + keys.length + " recorded results";
        if (!window.confirm(msg + "?")) return;
        keys.forEach(function (k) { delete instance.results[k]; });
        instance.evidence = instance.evidence.filter(function (e) { return e.subjectId !== s.id; });
        instance.findings = instance.findings.filter(function (f) { return f.subjectId !== s.id; });
        instance.subjects = instance.subjects.filter(function (o) { return o.id !== s.id; });
        if (!instance.subjects.length) instance.subjects.push({ id: "s1", name: "Subject 1" });
        save();
        render();
      });
      tb.appendChild(el("tr", null, [el("td", null, [idInput]), el("td", null, [nameInput]), el("td", null, [del])]));
    });
  }

  /* ---------- subject selects ---------- */

  function renderSubjectSelect(sel, value) {
    clear(sel);
    instance.subjects.forEach(function (s) {
      var o = el("option", { value: s.id, text: s.name || s.id });
      if (s.id === value) o.selected = true;
      sel.appendChild(o);
    });
    if (!sel.querySelector("option[value='" + value + "']") && sel.firstChild) sel.selectedIndex = 0;
  }
  function refreshSubjectSelects() {
    ["scoring-subject", "evidence-subject", "profiles-subject"].forEach(function (id) {
      if (!ui[id + "-bound"]) {
        ui[id] = id;
        $(id).addEventListener("change", function () { render(); });
        $(id).setAttribute("data-bound", "1");
        ui[id + "-bound"] = true;
      }
    });
  }
  function selectedSubject(id) {
    var v = $(id).value;
    if (!v || !AMAF.subject(instance, v)) v = firstSubjectId();
    return v;
  }

  /* ---------- scoring tab ---------- */

  function renderScoring() {
    var subjectId = selectedSubject("scoring-subject");
    var wrap = $("scoring-wrap");
    clear(wrap);
    var flat = AMAF.flatten(catalog);

    catalog.dimensions.forEach(function (dim) {
      var body = el("div", { class: "dim-body" });
      var dimScored = 0;
      var dimTotal = 0;
      dim.subdimensions.forEach(function (sub) {
        var subWrap = el("div", { class: "sub" });
        subWrap.appendChild(el("h4", { text: sub.id + " " + sub.name }));
        sub.criteria.forEach(function (crit) {
          dimTotal++;
          var row = critRow(subjectId, dim, sub, crit, flat);
          if (row.scored) dimScored++;
          subWrap.appendChild(row.node);
        });
        body.appendChild(subWrap);
      });
      var name = el("h3", { text: dim.id + " " + dim.name });
      var head = el("div", { class: "dim-head" }, [name, el("span", { class: "hint", text: dimScored + " of " + dimTotal + " assessed" })]);
      head.addEventListener("click", function () { body.classList.toggle("hidden"); });
      wrap.appendChild(el("div", { class: "dim" }, [head, body]));
    });

    var count = 0;
    Object.keys(instance.results).forEach(function (k) {
      if (k.indexOf(subjectId + "|") === 0 && instance.results[k].applicable === "yes" && typeof instance.results[k].score === "number") count++;
    });
    $("scoring-summary").textContent = count + " of " + flat.length + " criteria scored for this subject.";
  }

  function selectWith(list, value, allowEmpty, emptyTitle) {
    var s = el("select", { class: "crit-controls" });
    if (allowEmpty) {
      var o = el("option", { value: "", text: emptyTitle || "-" });
      s.appendChild(o);
    }
    list.forEach(function (v) {
      var o = el("option", { value: v, text: String(v) });
      if (String(value) === String(v)) o.selected = true;
      s.appendChild(o);
    });
    if (allowEmpty && (value === "" || value === null || value === undefined)) s.value = "";
    return s;
  }

  function critRow(subjectId, dim, sub, crit, flat) {
    var r = AMAF.getResult(instance, subjectId, crit.id);
    var items = AMAF.evidenceFor(instance, subjectId, crit.id);
    var node = el("div", { class: "crit-row" });

    var nameCol = el("div", { class: "crit-name" }, [
      el("strong", { text: crit.id + " " + crit.name }),
      el("small", { text: crit.assessment_type + (items.length ? " | " + items.length + " evidence item" + (items.length > 1 ? "s" : "") : "") })
    ]);
    var detailsBtn = el("button", { class: "linklike", text: "guidance & notes" });
    var details = el("div", { class: "crit-details hidden" });

    function rebuildDetails() {
      clear(details);
      var rr = AMAF.getResult(instance, subjectId, crit.id);
      var eff = AMAF.effectiveConfidence(rr, items, instance.assessment.date, crit.assessment_type);
      details.appendChild(el("div", { class: "prose", html: "<b>Question.</b> " + escapeHtml(crit.assessment_question) }));
      details.appendChild(el("div", { class: "prose", html: "<b>Interpretation guidance.</b> " + escapeHtml(crit.interpretation_guidance) }));
      details.appendChild(el("div", { class: "prose", html: "<b>Applicability.</b> " + escapeHtml(crit.applicability_rule) }));
      var reqs = el("div", { class: "prose", html: "<b>Evidence requirements.</b><br>" + crit.evidence_requirements.map(escapeHtml).join("<br>") });
      details.appendChild(reqs);

      var note = el("div", { class: "conf-note" + (eff.value === "low" ? "" : " ok") });
      var noteText = "Suggested confidence: " + eff.suggested + ". Effective: " + eff.value + ".";
      eff.notes.forEach(function (n) { noteText += " " + n; });
      note.textContent = noteText;
      details.appendChild(note);
      var apply = el("button", { class: "btn outline small", text: "Apply suggested confidence" });
      apply.addEventListener("click", function () {
        AMAF.setResult(instance, subjectId, crit.id, { confidence: eff.suggested });
        save(); render();
      });
      details.appendChild(apply);

      if (crit.assessment_type === "demand") {
        var lab = el("label", { class: "prose" });
        lab.appendChild(document.createTextNode("The organization has committed to this demand "));
        var cb = el("input", { type: "checkbox" });
        cb.checked = rr.committed === true;
        cb.addEventListener("change", function () { AMAF.setResult(instance, subjectId, crit.id, { committed: cb.checked }); save(); render(); });
        lab.appendChild(cb);
        details.appendChild(lab);
      }
      if (crit.assessment_type === "exposure") {
        var tolWrap = el("label", { class: "prose", text: "Risk position against stated tolerance" });
        var tol = pick(["", "inside", "outside"], rr.tolerance || "", ["not stated", "inside tolerance", "outside tolerance"]);
        tol.addEventListener("change", function () { AMAF.setResult(instance, subjectId, crit.id, { tolerance: tol.value }); save(); render(); });
        tolWrap.appendChild(tol);
        details.appendChild(tolWrap);
      }

      var comLabel = el("label", { class: "prose", text: "Commentary" });
      var com = el("textarea", { rows: "2" });
      com.value = rr.commentary || "";
      com.addEventListener("change", function () { AMAF.setResult(instance, subjectId, crit.id, { commentary: com.value }); save(); });
      comLabel.appendChild(com);
      details.appendChild(comLabel);

      var recLabel = el("label", { class: "prose", text: "Recommendation" });
      var rec = el("textarea", { rows: "2" });
      rec.value = rr.recommendation || "";
      rec.addEventListener("change", function () { AMAF.setResult(instance, subjectId, crit.id, { recommendation: rec.value }); save(); });
      recLabel.appendChild(rec);
      details.appendChild(recLabel);

      var evBtn = el("button", { class: "btn outline small", text: "Manage evidence" });
      evBtn.addEventListener("click", function () {
        renderSubjectSelect($("evidence-subject"), subjectId);
        var cs = $("evidence-criterion");
        Array.prototype.forEach.call(cs.options, function (o) { o.selected = o.value === crit.id; });
        openTab("evidence");
      });
      details.appendChild(evBtn);
    }

    detailsBtn.addEventListener("click", function () {
      rebuildDetails();
      details.classList.toggle("hidden");
    });

    var appSel = pick(["", "yes", "no", "deferred"], r.applicable || "", ["assess", "yes", "no", "deferred"]);
    appSel.setAttribute("class", "crit-controls");
    appSel.addEventListener("change", function () {
      AMAF.setResult(instance, subjectId, crit.id, { applicable: appSel.value });
      save(); render();
    });

    var scoreSel = selectWith([1, 2, 3, 4, 5], r.score, true);
    scoreSel.addEventListener("change", function () {
      AMAF.setResult(instance, subjectId, crit.id, { score: scoreSel.value === "" ? null : Number(scoreSel.value) });
      save(); render();
    });
    var targetSel = selectWith([1, 2, 3, 4, 5], r.target, true);
    targetSel.addEventListener("change", function () {
      AMAF.setResult(instance, subjectId, crit.id, { target: targetSel.value === "" ? null : Number(targetSel.value) });
      save(); render();
    });

    var gap = AMAF.gap(r);
    var gapCell = el("div", { class: "gap-cell" });
    if (typeof gap === "number") {
      var cls = gap > 0 ? "gap-shortfall" : (gap <= -2 ? "gap-overshoot" : (gap < 0 ? "gap-overshoot" : "gap-ok"));
      var txt = gap > 0 ? "+" + gap : String(gap);
      if (gap === 0) txt = "0";
      if (gap <= -2) txt = gap + " review";
      gapCell.appendChild(el("span", { class: cls, text: txt }));
    }

    var critSel = pick(["", "low", "medium", "high", "critical"], r.criticality || "", ["-", "low", "medium", "high", "critical"]);
    critSel.setAttribute("class", "crit-controls");
    critSel.addEventListener("change", function () {
      AMAF.setResult(instance, subjectId, crit.id, { criticality: critSel.value });
      save(); render();
    });

    var effConf = AMAF.effectiveConfidence(r, items, instance.assessment.date, crit.assessment_type);
    var confSel = pick(["", "low", "medium", "high"], r.confidence || "", ["-", "low", "medium", "high"]);
    confSel.setAttribute("class", "crit-controls");
    confSel.addEventListener("change", function () {
      AMAF.setResult(instance, subjectId, crit.id, { confidence: confSel.value });
      save(); render();
    });
    if (r.confidence && effConf.value !== r.confidence) {
      confSel.style.borderColor = "#8a5b00";
    }

    node.appendChild(nameCol);
    node.appendChild(appSel);
    node.appendChild(scoreSel);
    node.appendChild(targetSel);
    node.appendChild(gapCell);
    node.appendChild(critSel);
    node.appendChild(confSel);
    node.appendChild(detailsBtn);
    node.appendChild(details);
    node.setAttribute("style", "grid-column: 1 / -1; display: contents;");
    details.style.gridColumn = "1 / -1";
    return { node: node, scored: r.applicable === "yes" && typeof r.score === "number" };
  }

  function escapeHtml(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  /* ---------- evidence tab ---------- */

  function renderEvidenceCriterionOptions(subjectId) {
    var cs = $("evidence-criterion");
    var current = cs.value;
    clear(cs);
    AMAF.flatten(catalog).forEach(function (entry) {
      var r = AMAF.getResult(instance, subjectId, entry.criterion.id);
      var label = entry.criterion.id + " " + entry.criterion.name + " (" + entry.criterion.assessment_type + ")";
      if (r.applicable === "yes") label += " *";
      cs.appendChild(el("option", { value: entry.criterion.id, text: label }));
    });
    if (current && cs.querySelector("option[value='" + current + "']")) cs.value = current;
  }

  function renderEvidence() {
    if (!ui["evidence-criterion-bound"]) {
      $("evidence-criterion").addEventListener("change", function () { renderEvidence(); });
      ui["evidence-criterion-bound"] = true;
    }
    var subjectId = selectedSubject("evidence-subject");
    renderEvidenceCriterionOptions(subjectId);
    var cid = $("evidence-criterion").value;
    var list = $("evidence-list");
    clear(list);

    var r = AMAF.getResult(instance, subjectId, cid);
    var eff = AMAF.effectiveConfidence(r, AMAF.evidenceFor(instance, subjectId, cid), instance.assessment.date, AMAF.criterionById(catalog, cid).criterion.assessment_type);
    list.appendChild(el("div", { class: "hint", text: "Effective confidence for this result: " + eff.value + (eff.capped ? " (capped; extreme score without corroboration)" : "") + ". " + eff.notes.join(" ") }));

    var items = AMAF.evidenceFor(instance, subjectId, cid);
    if (!items.length) list.appendChild(el("p", { class: "hint", text: "No evidence items linked to this criterion yet." }));
    items.forEach(function (item) {
      var desc = el("input", { type: "text", value: item.description, placeholder: "What the item is or shows" });
      desc.addEventListener("change", function () { item.description = desc.value; save(); render(); });
      var klass = pick(["direct", "indirect"], item.class);
      klass.addEventListener("change", function () { item.class = klass.value; save(); render(); });
      var source = el("input", { type: "text", value: item.source, placeholder: "Source (independence: distinct sources)" });
      source.addEventListener("change", function () { item.source = source.value; save(); render(); });
      var date = el("input", { type: "date", value: item.date });
      date.addEventListener("change", function () { item.date = date.value; save(); render(); });
      var rel = pick(["supports", "conflicts"], item.relation);
      rel.addEventListener("change", function () { item.relation = rel.value; save(); render(); });
      var del = el("button", { class: "btn danger small", text: "Remove" });
      del.addEventListener("click", function () {
        instance.evidence = instance.evidence.filter(function (e) { return e !== item; });
        save(); render();
      });
      list.appendChild(el("div", { class: "ev-item" }, [
        desc,
        el("div", null, [klass, rel, el("span", { class: "tag " + (item.class === "direct" ? "direct" : ""), text: item.class })]),
        source,
        date,
        del,
        el("span", { class: "tag " + (item.relation === "conflicts" ? "conflicts" : ""), text: item.relation })
      ]));
    });
  }

  /* ---------- profiles tab ---------- */

  function renderProfiles() {
    var subjectId = selectedSubject("profiles-subject");
    var wrap = $("profiles-wrap");
    clear(wrap);

    catalog.dimensions.forEach(function (dim) {
      var p = AMAF.profileFor(catalog, instance, subjectId, dim.id);
      if (!p.resultKeys.length) return;
      var box = el("div", { class: "prof-dim" });
      box.appendChild(el("h3", { text: dim.id + " " + dim.name + " | " + p.resultKeys.length + " scored results" }));

      var tbl = el("table", { class: "table prof-table" });
      var thead = el("thead", null, [el("tr", null, ["assessment type", "1 Inadequate", "2 Weak", "3 Adequate", "4 Strong", "5 Leading", "count"].map(function (h) { return el("th", { text: h }); }))]);
      tbl.appendChild(thead);
      var tbody = el("tbody");
      Object.keys(p.bands.byType).sort().forEach(function (t) {
        var b = p.bands.byType[t];
        tbody.appendChild(el("tr", null, [
          el("td", { text: t }),
          el("td", { text: String(b[1]) }), el("td", { text: String(b[2]) }),
          el("td", { text: String(b[3]) }), el("td", { text: String(b[4]) }),
          el("td", { text: String(b[5]) }), el("td", { text: String(b.count) })
        ]));
      });
      var tot = p.bands.total;
      tbody.appendChild(el("tr", null, [
        el("td", { text: "all types (display only)" }),
        el("td", { text: String(tot[1]) }), el("td", { text: String(tot[2]) }),
        el("td", { text: String(tot[3]) }), el("td", { text: String(tot[4]) }),
        el("td", { text: String(tot[5]) }), el("td", { text: String(tot.count) })
      ]));
      tbl.appendChild(tbody);
      box.appendChild(el("p", { class: "hint", text: "Profiles are partitioned by assessment type; the all-types row is a count check, never a finding basis." }));
      box.appendChild(tbl);

      var shareTxt = p.belowAdequacy.share === null ? "no scored results" :
        p.belowAdequacy.below + " of " + p.belowAdequacy.total + " at or below adequacy (" + Math.round(p.belowAdequacy.share * 100) + "%; descriptive)";
      box.appendChild(el("div", { class: "distrib", html: "Below-adequacy share: " + shareTxt +
        ". Median: " + (p.median === null ? "n/a" : p.median) + " (descriptive). Minimum confidence: " + (p.minConfidence || "not recorded") +
        ". Criticality overlay: " + p.criticalityOverlay + " result(s) at or below adequacy carrying high or critical criticality." }));
      wrap.appendChild(box);
    });

    /* finding candidates */
    wrap.appendChild(el("h3", { text: "Finding candidates (derived, per interpretation rules v1)" }));
    var cands = AMAF.findingCandidates(catalog, instance, subjectId);
    if (!cands.length) {
      wrap.appendChild(el("p", { class: "hint", text: "No finding candidates for this subject yet: candidates arise from applicable results at score 2 or below (class by assessment type), or strengths at score 4 or above with high confidence." }));
    }
    cands.forEach(function (c) {
      var lines = el("div", { class: "cand " + c.cls });
      var head = el("strong", { text: c.cls.toUpperCase() + " | " + c.criterionId + " " + c.criterionName });
      lines.appendChild(el("div", null, [el("span", { class: "cls-tag", text: c.assessmentType }), head]));
      var info = "score " + c.score + (c.target ? ", target " + c.target : "") + (typeof c.gap === "number" ? ", gap " + (c.gap > 0 ? "+" + c.gap : c.gap) : "") + ", confidence " + c.confidence;
      if (c.suggestedSeverity) info += ", suggested severity " + c.suggestedSeverity;
      lines.appendChild(el("div", { text: info }));
      if (c.belowFloor) {
        lines.appendChild(el("div", { class: "warn-line", text: "Below the findings floor (low confidence): carried as an unverified observation, not a finding." }));
      }
      if (c.soleExtremeUnverified) {
        lines.appendChild(el("div", { class: "warn-line", text: "Extreme score without required corroboration: may not be the sole basis of a finding." }));
      }
      if (!c.belowFloor && !c.soleExtremeUnverified) {
        var btn = el("button", { class: "btn small", text: "Record as finding" });
        btn.addEventListener("click", function () {
          var f = AMAF.newFinding(subjectId);
          f.cls = c.cls;
          f.severity = c.suggestedSeverity || "moderate";
          f.basis = [c.resultKey];
          f.statement = "";
          instance.findings.push(f);
          save(); renderProfiles();
        });
        lines.appendChild(btn);
      }
      wrap.appendChild(lines);
    });

    /* recorded findings */
    wrap.appendChild(el("h3", { text: "Recorded findings" }));
    var mine = instance.findings.filter(function (f) { return f.subjectId === subjectId; });
    if (!mine.length) wrap.appendChild(el("p", { class: "hint", text: "No findings recorded for this subject yet." }));
    mine.forEach(function (f) {
      var box = el("div", { class: "finding" });
      box.appendChild(el("div", null, [
        el("span", { class: "cls-tag", text: f.cls }),
        el("strong", { text: f.id }),
        el("span", { text: " | basis: " + f.basis.join(", ") })
      ]));
      var sta = el("textarea", { rows: "2", placeholder: "Finding statement, faithful to its basis results" });
      sta.value = f.statement;
      sta.addEventListener("change", function () { f.statement = sta.value; save(); });
      var sev = pick(["minor", "moderate", "material", "severe"], f.severity);
      sev.addEventListener("change", function () { f.severity = sev.value; f.severityOverride = true; save(); });
      var clsSel = pick(["deficiency", "exposure", "demand", "constraint", "strength"], f.cls);
      clsSel.addEventListener("change", function () { f.cls = clsSel.value; save(); });
      var del = el("button", { class: "btn danger small", text: "Remove" });
      del.addEventListener("click", function () {
        instance.findings = instance.findings.filter(function (o) { return o !== f; });
        save(); render();
      });
      AMAF.findingWarnings(f, instance, catalog).forEach(function (w) {
        box.appendChild(el("div", { class: "warn-line", text: w }));
      });
      box.appendChild(sta);
      box.appendChild(el("div", { class: "toolbar" }, [el("label", { text: "Class " }, [clsSel]), el("label", { text: "Severity " }, [sev]), del]));
      wrap.appendChild(box);
    });
  }

  /* ---------- io tab ---------- */

  function renderSaved() {
    var tb = $("saved-instances").querySelector("tbody");
    if (!tb) return;
    clear(tb);
    Object.keys(store.instances).forEach(function (key) {
      var inst = store.instances[key];
      var count = Object.keys(inst.results || {}).length;
      var loadBtn = el("button", { class: "btn small", text: "Open" });
      loadBtn.addEventListener("click", function () {
        currentKey = key;
        instance = store.instances[key];
        store.current = key;
        save();
        render();
      });
      var delBtn = el("button", { class: "btn danger small", text: "Delete" });
      delBtn.addEventListener("click", function () {
        if (!window.confirm("Delete stored instance " + (inst.assessment && inst.assessment.id) + "?")) return;
        delete store.instances[key];
        if (currentKey === key) {
          var first = Object.keys(store.instances)[0] || null;
          if (first) { currentKey = first; instance = store.instances[first]; }
          else {
            currentKey = "inst-" + Date.now().toString(36);
            instance = AMAF.newInstance("ASSESSMENT-1");
            store.instances[currentKey] = instance;
          }
          store.current = currentKey;
        }
        save();
        render();
      });
      tb.appendChild(el("tr", null, [
        el("td", { text: (inst.assessment && inst.assessment.id) + (key === currentKey ? " (open)" : "") }),
        el("td", { text: inst.assessment && inst.assessment.organization }),
        el("td", { text: inst.assessment && inst.assessment.date }),
        el("td", { text: String((inst.subjects || []).length) }),
        el("td", { text: String(count) }),
        el("td", null, [loadBtn, delBtn])
      ]));
    });
  }

  function bindIo() {
    $("btn-export-json").addEventListener("click", function () {
      download((instance.assessment.id || "assessment") + ".json", AMAF.toJson(instance), "application/json");
    });
    $("btn-export-csv").addEventListener("click", function () {
      download("scoring-" + (instance.assessment.id || "assessment") + ".csv", AMAF.toCsv(catalog, instance), "text/csv");
    });
    $("btn-new-instance").addEventListener("click", function () {
      currentKey = "inst-" + Date.now().toString(36);
      instance = AMAF.newInstance("ASSESSMENT-" + (Object.keys(store.instances).length + 1));
      store.instances[currentKey] = instance;
      store.current = currentKey;
      save();
      render();
    });
    $("file-import-json").addEventListener("change", function () {
      var file = $("file-import-json").files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var inst = AMAF.fromJson(String(reader.result));
          currentKey = "inst-" + Date.now().toString(36);
          store.instances[currentKey] = inst;
          store.current = currentKey;
          instance = inst;
          save();
          $("validate-out").textContent = "Imported " + inst.assessment.id + ": " + inst.subjects.length + " subject(s), " + Object.keys(inst.results).length + " recorded result(s).";
          render();
        } catch (err) {
          $("validate-out").textContent = "Import failed: " + err.message;
        }
      };
      reader.readAsText(file);
      $("file-import-json").value = "";
    });
  }

  /* ---------- render ---------- */

  function render() {
    bindInstanceOnce();
    bindIoOnce();
    refreshSubjectSelects();
    renderSubjects();
    renderSubjectSelect($("scoring-subject"), ui.lastScoringSubject || firstSubjectId());
    renderSubjectSelect($("evidence-subject"), ui.lastEvidenceSubject || firstSubjectId());
    renderSubjectSelect($("profiles-subject"), ui.lastProfilesSubject || firstSubjectId());
    renderScoring();
    renderEvidence();
    renderProfiles();
    renderSaved();
    bindInstance();
  }

  var boundOnce = {};
  function bindInstanceOnce() {
    if (boundOnce.instance) return;
    boundOnce.instance = true;
  }
  function bindIoOnce() {
    if (boundOnce.io) return;
    boundOnce.io = true;
    bindIo();
  }

  /* keep last selected subject per tab so re-renders do not reset choices */
  ["scoring-subject", "evidence-subject", "profiles-subject"].forEach(function (id) {
    document.addEventListener("change", function (ev) {
      if (ev.target && ev.target.id === id) {
        ui[{
          "scoring-subject": "lastScoringSubject",
          "evidence-subject": "lastEvidenceSubject",
          "profiles-subject": "lastProfilesSubject"
        }[id]] = ev.target.value;
      }
    });
  });

  /* ---------- boot ---------- */

  var critCount = AMAF.flatten(catalog).length;
  $("catalog-badge").textContent = "catalog v" + catalog.version + " | " + critCount + " criteria | assessment_rules v" + catalog.assessment_rules.version + " | interpretation_rules v" + catalog.interpretation_rules.version;
  load();
  render();
})();
