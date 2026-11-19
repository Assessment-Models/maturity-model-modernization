# D3 · Architecture Baseline & Condition

**Assessment objective**: establish what exists, what it comprises, how it is constituted, and its current condition.

*Normative source: the fully modeled criteria for this dimension (definitions, assessment questions, applicability rules, evidence requirements, interpretation guidance, and domain applicability) live in the [criterion catalog](../../tools/criterion-catalog/criteria-catalog.yaml).*

## Subdimensions and assessment criteria

| Subdimension | Assessment criteria |
|--------------|---------------------|
| D3.1 Architecture Inventory | Completeness, visibility, classification, and inventory of architectural elements |
| D3.2 Architecture Representation | Availability, accuracy, fidelity, and consistency of architectural models and documentation |
| D3.3 Architecture State | Actual deployed, operational, implemented, or realized architecture versus declared architecture |
| D3.4 Lifecycle Condition | Age, lifecycle stage, support status, maintenance condition, and obsolescence |
| D3.5 Architecture Coverage | Coverage of relevant business, technical, operational, and stakeholder concerns |
| D3.6 Baseline Integrity | Reliability of the baseline, evidence, dependencies, ownership, and traceability |

## Modernization signals

- The architecture is unknown, undocumented, or poorly understood.
- The declared architecture differs significantly from the implemented architecture.
- Critical elements are obsolete or unsupported.
- The architecture cannot be reliably assessed because its baseline is incomplete.
- Architectural assets are duplicated, unmanaged, or poorly governed.

## Interpretation notes

This dimension is especially important because modernization decisions made against an unreliable baseline can create unnecessary interventions or overlook material risks.

D3.3 (Architecture State) captures the declared-versus-implemented gap. Where the gap is material, baseline restoration or discovery work may need to **precede** assessment completion in other dimensions, and assessment confidence in D3 should bound the confidence of dependent findings. Baseline weakness is therefore both a modernization signal in itself and a constraint on the rest of the assessment.
