# Comparability Study: Two Independent Assessments of One Integration Subject

The validation slice defines its acceptance test literally: "two independent assessments of the same subject produce comparable profiles." This page documents that test executed for real. Team A performed the [integration architecture assessment](integration-architecture.md), recorded 2026-04-02. Team B assessed the same subject independently on 2026-04-16, gathering its own evidence and recording its own judgments without reference to Team A's record.

Both records are machine-validated by the same validator under the same rules (catalog v0.4.1, `assessment_rules` v1, `interpretation_rules` v2): [`framework/examples/integration-instance.yaml`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/examples/integration-instance.yaml) (Team A) and [`framework/examples/integration-reassessment.yaml`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/examples/integration-reassessment.yaml) (Team B). The validator re-derives every finding class, severity, confidence effect, profile, and dominance decision in both bundles; nothing on this page is asserted that the rules do not force.

## Result-level comparison

| Team A | Team B | Criterion | Score A | Score B | Confidence A | Confidence B | Verdict |
|--------|--------|-----------|---------|---------|--------------|--------------|---------|
| RES-01 | RES-01B | D5.4.1 Fragmentation & Duplication | 1 | 1 | high | high | agree |
| RES-02 | RES-02B | D3.2.1 Interface Standardization | 1 | 2 | high | high | divergence |
| RES-03 | RES-03B | D5.2.1 Coupling & Decoupling | 2 | 2 | high | high | agree |
| RES-04 | RES-04B | D6.3.1 Operations Risk Exposure (outside tolerance) | 2 | 2 | high | high | agree |
| RES-05 | RES-05B | D4.4.1 Technology Obsolescence & Demand (committed) | 2 | 2 | medium | medium | agree |
| RES-06 | RES-06B | D7.4.1 Engineering & Delivery Readiness | 2 | 2 | medium | high | scores agree; confidence differs (explained below) |
| RES-07 | RES-07B | D8.1.1 Target State Definition | 4 | 4 | high | high | agree |

Six of seven results score identically, including the exposure-outside-tolerance judgment and the committed-demand judgment, both of which require real interpretation of evidence.

## The one score divergence

RES-02 (Team A) and RES-02B (Team B) assess the same baseline-representation question and disagree: score 1 versus 2, producing findings F-2 (severe) and F-B2 (material).

The divergence is genuine, and the framework localizes it precisely. Team A's evidence covered a strict re-count in which 24 of 30 sampled interfaces lacked a current representation: score 1, severe finding. Team B's re-sample found 15 of 30 undocumented and weighted the estate model lag accordingly: score 2, high criticality, so a material finding (R-SEV-2). Both evidence sets pass the corroboration, staleness, and conflict rules; both findings follow mechanically from the recorded scores; and F-B2 carries an explicit cross-reference note documenting that this is a known, score-level inter-rater divergence with its evidence basis. What differs is the evidence base, not the interpretation machinery, and because class and severity are derived rather than asserted, the two records remain directly comparable: a reader can state exactly which evidence difference produced the profile difference.

## The one confidence difference

RES-06/RES-06B score identically (2) but Team B records high confidence where Team A recorded medium. This is mechanical, not judgment drift: Team B's evidence window includes a current maturity-model practice result (band L2, evidence EV-B11) which corroborates the readiness result per the [maturity bridge](../methodology/maturity-bridge.md). The same bridge fact triggers the R-MB4 practice-versus-readiness flag, and the record carries the required subject-specific explanation: the automated-testing readiness gap is subject-specific, not a practice-wide pattern. So the confidence gain and the calibration flag are both rule-driven consequences of a richer evidence set.

## Finding-level comparison

All seven findings match in class; one differs in severity, and it is precisely the score divergence above, propagated by the severity rules:

| Pair | Class | Severity A | Severity B |
|------|-------|------------|------------|
| F-1 / F-B1 | Deficiency | Severe | Severe |
| F-2 / F-B2 | Deficiency | Severe | Material (the divergence above) |
| F-3 / F-B3 | Constraint | Material | Material |
| F-4 / F-B4 | Exposure | Severe | Severe |
| F-5 / F-B5 | Demand | Material | Material |
| F-6 / F-B6 | Constraint | Material | Material |
| F-7 / F-B7 | Strength | None | None |

The strength finding and the severe exposure finding agree exactly despite fully independent evidence selection, because both teams recorded the same fact patterns and the rules drew the same conclusions. The evidence layer also differs structurally where the facts differ (Team B's set is 13 items to Team A's 14, with its own resolved evidence conflict), yet the derived layers converge anyway.

## Profile comparison

The decisive comparison is at the [opportunity and profile](../methodology/prioritization.md) layer, which is where "comparable profiles" gets its meaning:

| | Team A (O-1 / O-2) | Team B (O-B1 / O-B2) |
|--|--------------------|----------------------|
| Integration service standardization | active; primary Critical Modernization, secondary Strategic Modernization | active; primary Critical Modernization, secondary Strategic Modernization |
| Partner onboarding simplification | active; primary Strategic Modernization | active; primary Strategic Modernization |

Identical opportunity statements, identical statuses, identical primary and secondary profiles, derived by rule from two independent records. The one score-level divergence does not cross any profile threshold: both syntheses identify the same two opportunities, and B's O-B1 closes the same gap profile over its own results. The instrument's design goal, that profiles be sensitive to subject state but robust to assessor identity, holds for this study.

## What the rules force and what they permit

- **Forced agreement**: finding class from the recorded type and score; severity from score, gap, criticality, and tolerance; confidence effects from corroboration, staleness, and conflict resolution; opportunity synthesis from the finding set; the dominance order among profiles; and the required opportunity content (subject region, course of change, gap profile, significance factors with bases).
- **Permitted variation**: evidence selection and sampling; the scores that evidence supports; confidence as derived from the evidence base; and appended assessor notes.
- **The design principle**: direct judgment is expressed only in the evidence layer, where it can be examined and audited; everything above the evidence layer is re-derivable by rule from the record, enforced in CI by [`framework/validate.py`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/validate.py). Comparability is structural, not aspirational.

Instrument coverage across this study and the [customer onboarding example](customer-onboarding.md) is tabulated in the [validation notes](../validation/validation-notes.md).
