# D4 · Architectural Fitness & Performance

**Assessment objective**: evaluate whether the architecture is fit for its intended purpose and performs adequately under existing and anticipated conditions.

*Normative source: the fully modeled criteria for this dimension (definitions, assessment questions, applicability rules, evidence requirements, interpretation guidance, and domain applicability) live in the [criterion catalog](../../tools/criterion-catalog/criteria-catalog.yaml).*

## Subdimensions and assessment criteria

| Subdimension | Assessment criteria |
|--------------|---------------------|
| D4.1 Functional Adequacy | Ability to fulfill intended functions, responsibilities, and requirements |
| D4.2 Performance & Efficiency | Throughput, responsiveness, resource efficiency, capacity, and utilization |
| D4.3 Quality Attributes | Two independently assessable criteria: D4.3.1 Service quality attributes (reliability, availability, resilience, recoverability, scalability) and D4.3.2 Change-supporting quality attributes (maintainability, adaptability, understandability, testability, deployability) |
| D4.4 Interoperability & Integration | Compatibility, connectivity, interface integrity, integration capability, and exchange |
| D4.5 Operational Effectiveness | Effectiveness in supporting operations, execution, management, and service delivery |
| D4.6 Requirement Fulfillment | Adequacy against functional, non-functional, stakeholder, and contextual requirements |

## Modernization signals

- Performance no longer meets requirements.
- Functional gaps or quality deficiencies affect value delivery.
- Integration is costly, fragile, or unreliable.
- The architecture cannot scale to expected demand.
- Operational effectiveness is impaired.

## Interpretation notes

D4 answers the **fitness-for-purpose** question, which is distinct from the structural question (D5) and the exposure question (D6). An architecture can perform adequately today while being structurally brittle, or be structurally coherent while failing its purpose. Fitness findings under current conditions should be read together with D1.4 (Future Alignment) and D2 (Drivers) to distinguish present inadequacy from anticipated inadequacy; only the combination establishes the modernization case.

D4.3 is assessed as two criteria because its attribute families fail independently and take different evidence: D4.3.1 (service quality attributes) is a condition on operational behavior, while D4.3.2 (change-supporting quality attributes) is assessed as changeability against the subject's change demand.
