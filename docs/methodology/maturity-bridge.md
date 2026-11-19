# The Maturity Model Bridge: D7 and the Practice Bands

*This page fixes the relationship between the criterion catalog's assessment mechanics and the governed Architecture Modernization Maturity Model (L0-L4 practice bands), without collapsing one instrument into the other. Terminology follows the [glossary](../framework/glossary.md); the machine-readable form is the `assessment_rules.maturity_bridge` section of the [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml).*

## Two instruments, two subjects

| | AMAF criterion catalog | Maturity model |
|---|-----------------------------|-----------------|
| Subject | The architecture under assessment | The organization's modernization practice |
| Question | How does the subject score against its criteria | What practice band (L0-L4) the modernization capability operates in |
| Scale | The five-point criterion scale | The five practice bands, canonical v2 (dea:maturity-bands-v2) |
| Governed by | AMAF catalog, versioned independently | `model.yaml`, `maturity/scale.yaml`, release v1.1.0 |

The maturity model is the readiness instrument for dimension D7 (Adaptability & Modernization Readiness) in the sense defined here: its result enters D7 assessment as **evidence**, never as a substitute for scored criteria.

## The bridge rules

**R-MB1 (evidence, not scores).** A current maturity model result enters D7 assessment as one **direct-class practice evidence item** for readiness criteria (for example D7.4 delivery capacity), dated and scoped to the assessed organization. For subject-level changeability criteria (for example D4.3.2), it is indirect context at most: those criteria require architecture-specific evidence.

**R-MB2 (no conversion).** There is no arithmetic mapping between L0-L4 and the 1-5 criterion scale, in either direction. Band levels are never converted into scores, and scores are never aggregated into a band claim. "We are L2" is a statement about practice, not about any architecture's readiness score, and an assessment never reports a D7 score as a band.

**R-MB3 (confidence applies).** The maturity result, as one evidence item, feeds [evidence mechanics](evidence-mechanics.md) normally: a single current instrument result meets the medium rule on its own; high confidence for a D7 criterion still requires an independent corroborating item (for example, delivery records from the subject's own change history). An out-of-date result (older than the practice's change horizon, one year by default) downgrades one level, like any other item.

**R-MB4 (calibration flags).** The two instruments cross-check each other:

- A readiness criterion score of 4 or 5 (Strong or Leading) on a change-execution criterion, while the assessed practice maturity is L0, is implausible without direct architecture-level corroboration. The assessor records the contradiction and either supplies that corroboration or reviews the score downward.
- A readiness criterion score of 1 or 2 while practice maturity is L2 or higher requires a recorded subject-specific explanation (typically the subject is structurally hostile to change despite good practice; see D5 evidence).

Calibration flags never override evidence in either direction; they force the contradiction to be resolved in the record.

**R-MB5 (separation preserved).** AMAF does not measure practice maturity, and the maturity model does not assess architecture subjects. In AMAF reports, maturity results appear only as evidence references and calibration context. The maturity model's own publications never cite catalog scores as band evidence.

## Why not converge the scales

Convergence would collapse **readiness derived from capability** with **readiness derived from knowing**: an organization can hold a strong practice band and still own an unmodernizable architecture, and a modernizable subject can sit inside a weak practice. The decision value is in the combination of both facts, which the bridge preserves as explicitly separate evidence classes, exactly as the four assessment types remain separate in [the evidence model](evidence-model.md).
