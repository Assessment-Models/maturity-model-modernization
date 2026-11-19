# The Criterion Model: Criteria as Modeled Propositions

The assessment criterion is the most important unit of assessment. It is not simply a question or a descriptive heading. A criterion is a **structured proposition** that describes a condition capable of being evaluated against a defined context and evidence.

## Worked example

> ### D5 · Structural Integrity & Complexity
>
> **SD5.2 · Coupling & Dependencies**
>
> **Criterion**: Architectural components can be modified, deployed, or evolved with a degree of independence appropriate to their responsibilities and change requirements.
>
> **Assessment interpretation**: Evaluates the extent to which dependencies and coupling between architectural elements constrain change, increase risk, or create disproportionate modernization effort.
>
> **Evidence examples**:
> - Dependency and integration maps
> - Change impact analysis
> - Release and deployment history
> - Failure propagation records
> - Engineering observations
> - Architecture models
>
> **Modernization implication**: Excessive coupling may indicate a need for boundary restructuring, dependency reduction, component separation, interface modernization, platform changes, or architectural redesign.

## Modeled criterion attributes

| Attribute | Description |
|-----------|-------------|
| Criterion ID | Stable identifier |
| Name | Human-readable criterion name |
| Definition | Normative meaning of the criterion |
| Assessment Intent | What the criterion is intended to evaluate |
| Assessment Question | Optional question used to guide inquiry |
| Assessment Type | Condition, demand, exposure, readiness, target, or other defined type |
| Applicability Rule | Conditions under which it should be assessed |
| Assessment Method | Method for establishing the result |
| Scale Reference | Scale used to evaluate the criterion |
| Evidence Requirement | Expected evidence or acceptable evidence types |
| Interpretation Guidance | How the result should be interpreted |
| Modernization Relevance | Why the criterion matters to modernization |
| Domain Applicability | Architecture domains to which the criterion relates |
| Assessment Weight | Optional weighting for a specific assessment context |
| Related Criteria | Related, complementary, dependent, or overlapping criteria |

## ID and domain conventions

The architecture discipline is **not** encoded into the criterion identifier or criterion definition wherever the criterion is common. Domain applicability is a separate relationship.

This permits a common criterion to be reused in Enterprise Architecture, Business Architecture, Data Architecture, and Software Architecture, while domain-specific criteria can be introduced where genuinely necessary.

The criterion catalog ([`tools/criterion-catalog/`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml)) is the normative home for modeled criteria. See [ROADMAP.md](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/ROADMAP.md) slice S1 for the completion plan.
