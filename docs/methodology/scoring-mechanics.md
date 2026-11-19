# Scoring Mechanics: Scale Semantics by Assessment Type

*Scales and attributes are defined in [Assessment Scales & Attributes](assessment-scales.md); the framework's four independent assessment types are defined in [The Evidence Model](evidence-model.md). This page fixes how the shared 1-5 scale is applied per type. Terminology follows the [glossary](../framework/glossary.md); the machine-readable form of these rules is the `assessment_rules` section of the [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml).*

## One scale, seven readings

The five-point scale is shared by every criterion, but the scale's question differs by assessment type. The type is a property of the criterion, normative in the catalog; an assessor never re-decides it.

| Assessment type | The score measures | Score 3 (Adequate) means | Score 5 (Leading) means |
|-----------------|--------------------|--------------------------|--------------------------|
| Condition | Adequacy of the current state against current expectations | The proposition holds for current expectations, with identified deficiencies | The subject demonstrably exceeds expectations and optimizes for them |
| Demand | Demonstrated capacity to meet recorded anticipated demand | The subject can plausibly meet the recorded demand; capability not yet demonstrated | The anticipated demand is fully accounted for in current design, with margin |
| Exposure | Whether the subject's exposure is known and within stated tolerance | Exposure is identified and tolerance is mostly respected | Exposure is comprehensively known, monitored, and inside tolerance with early warning |
| Criticality | Whether the subject's criticality is established and accepted | Criticality is established and accepted by the relevant stakeholders | Criticality is established, accepted, and drives investment and attention |
| Readiness | Capacity to execute change on the subject | Execution capacity exists for change of typical scale, with identified limits | Capacity is strong, proven, and instrumented across the change portfolio |
| Changeability | Ease, speed, cost, and risk of changing the subject, against a realistic change portfolio | Change happens at tolerable effort and risk for typical changes | Change is routine, fast, low-risk, and evidence-backed for demanding changes |
| Target | Clarity and viability of the defined target position | A target is defined and defensible, with open questions resolved as they arise | The target is explicit, viable, economic, and traceable to the opportunity |

## The uniform direction rule

Every score is a judgment about the **subject**, never a magnitude of a problem or requirement:

- Demand criteria are never scored "how far away the future is." They are scored as the subject's demonstrated capacity to meet the recorded anticipated demand. A bigger demand does not mean a bigger score.
- Criticality criteria are never scored "how important the subject is." They are scored as whether that criticality is established and accepted; the weight itself is carried by the criticality attribute on every criterion.
- Exposure criteria are never scored "how much risk exists." They are scored as knowledge and tolerance alignment: unknown exposure scores low; well-managed exposure scores high.

Higher is stronger on the criterion's own semantics, on all types.

## The anchoring procedure

Given a criterion and its evidence, scoring proceeds in four steps:

1. **Read the criterion as modeled.** The catalog's `assessment_question` frames what must be answered; `applicability_rule` gates whether the criterion is assessed at all. A non-applicable criterion is recorded as such, never scored.
2. **Establish the reference expectation for the type** from the table above: current expectations (condition), recorded anticipated demand (demand), stated tolerance (exposure), accepted criticality (criticality), the change portfolio (readiness, changeability), or the defined target position (target).
3. **Locate the observed answer between the anchors.** Score 1: material failure against the reference expectation. Score 3: holds, with identified deficiencies or opportunities. Score 5: demonstrably strong, optimized, or advanced. Scores 2 and 4 are the intermediate positions; the criterion's `interpretation_guidance` states what to privilege and what not to penalize.
4. **Record the anchor rationale.** The commentary field names the anchors the score sits between and references the evidence items by identifier. A score without an anchor rationale fails review.

## What the score is not

- A score is not a verdict on the organization: it is a judgment on the proposition, for the assessed subject and scope.
- A score is not deferred until evidence is perfect: evidence quality is carried by the [confidence](evidence-mechanics.md) attribute, not by inflating or deflating the score.
- A score is not a finding: findings are interpreted statements derived from results under [interpretation logic](interpretation-logic.md).

## Reproducibility guards

Two assessors with the same evidence produce the same score because:

- The type reading, reference expectation, and anchors are normative (this page and the catalog `assessment_rules`).
- Interpretation guidance and score guards are normative per criterion.
- Scores are assigned from recorded evidence items only, with confidence and sufficiency enforced per [evidence mechanics](evidence-mechanics.md), including corroboration for extreme scores (1 and 5).
- Anchor rationales are mandatory in the commentary, so divergence is visible in review rather than hidden in intuition.
