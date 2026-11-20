# Validation Notes

This page records how the instrument was tested for the validation slice, what the consistency review found and changed, and how the [maturity model bridge](../methodology/maturity-bridge.md) was calibrated. It is the test-report companion to the [coverage argument](coverage-argument.md), which argues that the criterion taxonomy covers its problem space.

The framework's test harness is [`framework/validate.py`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/validate.py): a dependency-free Python 3 validator that re-derives finding classes, severities, confidence effects, opportunity synthesis, profile dominance, realization chain coverage, and metamodel conformance from the recorded facts, and fails on any violation. Every quantitative claim below is checkable by running it.

## Instrument testing matrix

Three complete assessment bundles are validated end to end, chosen to vary subject kind, organisation context, criteria, and profile space:

| Bundle | Instrument story | Subject kind & context | Machine record |
|--------|------------------|------------------------|----------------|
| [`integration-instance.yaml`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/examples/integration-instance.yaml) | Original end-to-end pass: exposure tolerance breach, committed demand, readiness-gated realization tail with capability, decision, and outcome records; 7 results, 14 evidence, 7 findings, 2 opportunities, 4 implications, 4 stages | Portfolio subject; technology estate context | Team A of the [comparability study](../examples/inter-rater-comparability.md) |
| [`onboarding-instance.yaml`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/examples/onboarding-instance.yaml) | Different organisation context and subject kind: the sustained-overshoot finding, a standby opportunity, and the maturity bridge in the forward direction; 10 results, 17 evidence, 9 findings, 2 opportunities, 5 implications, 3 stages | Capability-level subject (customer onboarding value stream); mutual insurer context | The [customer onboarding example](../examples/customer-onboarding.md) |
| [`integration-reassessment.yaml`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/examples/integration-reassessment.yaml) | Independent second assessment of the same subject: in-record evidence conflict resolution, score-level divergence preserved, maturity bridge readiness-direction flag; 7 results, 13 evidence, 7 findings, 2 opportunities, 2 implications, 3 stages | Same portfolio subject, independent team B | The [comparability study](../examples/inter-rater-comparability.md) |

Per-bundle counts above are printed by the validator on every green run. Together the bundles exercise:

- **14 distinct criteria across all 8 dimensions** (D1.1.1, D2.3.1, D2.4.1, D3.2.1, D3.5.1, D4.1.1, D4.3.2, D4.4.1, D5.2.1, D5.4.1, D6.2.1, D6.3.1, D7.4.1, D8.1.1), about 29 percent of the catalog, chosen per the [worked examples](../examples/integration-architecture.md) rather than for count.
- **6 of 7 nominal assessment types**: condition, exposure, target, changeability, demand, and readiness. The seventh, the criticality type (one catalog criterion), is not exercised; a worked criticality assessment is future content, not a rule gap.
- **8 of 10 domain packs in machine-validated implications**: enterprise, information systems, software, and technology (integration, team A); business, data, software, technology, and implementation (onboarding); data and service (reassessment, team B). The systems and solution packs appear only in the documentation fan-outs; carrying them into machine bundles is future content, not a rule gap.
- **The full profile space**: Critical Modernization primary with Strategic Modernization secondary; Strategic Modernization alone; and standby where no profile condition is satisfied, with a required review date.
- **Both severity ends of the overshoot path** and the full severity range: severe, material, moderate, and minor findings all occur, each derived by rule.

## The comparability test

The slice's acceptance criterion is that two independent assessments of the same subject produce comparable profiles. This was executed as a real study, documented on its own [page](../examples/inter-rater-comparability.md): 6 of 7 results score identically; the single score-level divergence (D3.2.1, score 1 versus 2) is preserved, documented, and localised to its evidence basis; all 7 finding classes match; the one severity difference is that same divergence propagated by rule; and the opportunity sets, statuses, primary and secondary profiles are identical across both assessments. The validator's own re-derivation confirms both profiles machine-forced, in both bundles, from independently recorded evidence.

## Consistency review: findings and dispositions

The consistency review compared the machine rule set, the catalog, the methodology pages, and the worked examples. It found four defects and one stale reference; all were fixed within this slice:

| Finding | Disposition |
|---------|-------------|
| The catalog's `findings.overshoot` note said the sustained deliberate-excess overshoot becomes a constraint finding, but the machine interpretation rules had no path to express it: the constraint class row only covered below-target scores | Catalog v0.4.1: interpretation_rules v2 extends the constraint class row to include sustained deliberate-excess overshoot (gap <= -2, review sustained); [`framework/validate.py`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/validate.py) and the [assessment app](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/assessment-app/logic.js) implement the same derivation |
| The minor severity row ("adequate result with a set target above it") was machine-unreachable: no rule path produced it, so the severity ladder could never reach its floor | Catalog v0.4.1 rewords the row to its canonical reachable case, the sustained-overshoot constraint finding (R-SEV-4); exercised for real by the onboarding bundle's F-7 |
| Standby opportunities were described in the prioritization method but could not be represented in the machine model: no profile value for them existed | [`framework/schemas/common.schema.json`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/schemas/common.schema.json) adds `standby` to the profile enum; the validator requires a standby opportunity to satisfy no profile, carry `primary: standby`, and set a review date; exercised by the onboarding bundle's O-2 |
| The taxonomy overview page cited the catalog as v0.2.0, three normative revisions behind | Updated to v0.4.1 |

Two documentation corrections surfaced earlier, during the S6 machine rule re-derivation, and belong on this record for completeness: the integration worked example's F-6 severity (moderate, corrected to material per R-SEV-2) and RES-07 confidence (medium, corrected to high, required by strength F-7's evidence rule). Both are already in the main text; the machine bundles restate the corrected values and pass.

## Calibration with the maturity model

The bridge between this framework and the Architecture Modernization Maturity Model is deliberately narrow: a maturity result enters as one direct-class evidence item, never as a score, and conversion is prohibited in both directions (R-MB1, R-MB2). Every live clause of the bridge was exercised in the bundles:

- **Evidence entry with confidence effect** (R-MB3): the onboarding bundle's EV-12 enters a current practice-band L2 result as exactly one direct-class practice evidence item for D7.4.1; together with an independent corroborating item from the subject's own delivery records it lifts the result's confidence to high, exactly as R-MB3 requires (a bridge item never carries high confidence alone). The reassessment bundle's EV-B11 does the same for its readiness result, and the confidence difference between the two integration assessments is precisely this effect.
- **Calibration flag, low-readiness direction** (R-MB4 second clause): the reassessment records a readiness score of 2 against practice maturity at L2, which triggers the flag and its required subject-specific explanation on RES-06B (the subject's automated-testing gap is structural, not a practice-wide pattern).
- **Honest gap**: the bridge's other flag (R-MB4 first clause, a readiness score of 4 or 5 against practice maturity at L0) has no worked example in the bundles; it is implemented in the validator and the app logic but not yet demonstrated with a record. Future content, not a rule gap.

## Negative testing

Rule sets are only real if their violations fail. Nine mutations were applied to the bundles, one at a time, and the validator caught every one; each was then reverted and the bundles re-validated green:

1. Removing the deliberate-excess note from an overshoot finding (the constraint-from-overshoot class requires its recorded basis).
2. Making a standby opportunity satisfy a profile condition.
3. Marking an active opportunity's profile as standby.
4. A gap that does not equal target minus score.
5. A recorded severity the re-derivation does not reproduce.
6. Evidence older than the change horizon (staleness).
7. Deleting an evidence record that a finding's corroboration math depends on.
8. Lowering a material finding's severity to moderate.
9. A standby opportunity missing its review date.

The [assessment app](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/assessment-app/selftest.js) carries its own negative probes, including five overshoot probes added with the v0.4.1 logic; its self-test runs green against the regenerated catalog embed.

## Verification commands

```bash
python3 framework/validate.py
node tools/assessment-app/selftest.js
node tools/criterion-catalog/export-catalog.py
```

The first re-derives everything recorded above from the three bundles and exits nonzero on any violation; the second exercises the app's scoring, finding, and overshoot logic; the third regenerates the catalog JSON and app embed and confirms they match the checked-in artifacts. All three run green on the main branch at this slice.
