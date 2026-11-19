# Assessment Scales and Attributes

## The core criterion assessment scale

A consistent five-point scale is used across all criteria:

| Score | Label | Meaning |
|-------|-------|---------|
| 1 | Inadequate | Material deficiency; fails expectations or creates significant exposure |
| 2 | Weak | Partially adequate; significant limitations, weaknesses, or improvement needs exist |
| 3 | Adequate | Generally satisfies current expectations, with identified deficiencies or opportunities |
| 4 | Strong | Performs well; limited weaknesses and well-managed improvement needs |
| 5 | Leading | Highly effective, optimized, or strategically advanced relative to defined expectations |

## Additional assessment attributes

Every criterion result carries more than a score:

| Attribute | Purpose |
|-----------|---------|
| Applicability | Determines whether a criterion applies to the assessment scope |
| Assessment Score | Criterion result on the defined scale |
| Criticality | Importance of the criterion to the assessed architecture and organizational context |
| Evidence | Supporting observations, artifacts, metrics, records, interviews, or findings |
| Confidence | Reliability and sufficiency of the assessment evidence |
| Target Score | Desired future condition |
| Gap | Difference between current condition and target condition |
| Assessment Commentary | Qualitative explanation of the result |
| Recommendation | Suggested response or modernization direction |
| Assessed Scope | Architecture, entity, component, capability, or area to which the finding applies |

## Reading scores correctly

A low assessment score does **not** automatically imply a modernization requirement. A criterion must be interpreted in the context of criticality, strategic relevance, future demand, risk, target condition, and evidence:

- An obsolete component may score poorly but be immaterial to the organization.
- A seemingly healthy architecture may warrant substantial modernization because it cannot support a critical strategic direction.

Scale semantics per assessment type, evidence confidence levels, and aggregation rules are normative in [Scoring Mechanics](scoring-mechanics.md), [Evidence Mechanics](evidence-mechanics.md), and [Aggregation, Gap, and Weighting Mechanics](aggregation-mechanics.md); their machine-readable form lives in the catalog's `assessment_rules` section.
