# Metamodel Entities

The framework is modeled as a taxonomy and assessment metamodel rather than maintained as a static assessment spreadsheet. Several distinct entities must not be collapsed into one object.

## Core model entities

| Entity | Purpose |
|--------|---------|
| Architecture Modernization Assessment Framework | Defines the assessment structure, dimensions, taxonomy, criteria, scales, and assessment rules |
| Assessment Dimension | Organizes a major aspect of modernization assessment |
| Assessment Subdimension | Provides a specific grouping of concerns within a dimension |
| Assessment Criterion | Defines an assessable proposition, concern, or condition |
| Assessment Scale | Defines the scoring semantics and score interpretation |
| Architecture Domain | Identifies the architecture discipline being assessed |
| Architecture Concern | Defines the domain-specific concern to evaluate |
| Assessment Method | Defines how a criterion is assessed, including quantitative or qualitative methods |
| Assessment Rule | Defines applicability, aggregation, interpretation, thresholds, and assessment logic |
| Architecture Modernization Assessment | An instantiated assessment for a defined organization, scope, subject, and context |
| Assessment Subject | The architecture, architectural element, capability, system, portfolio, domain, or scope under evaluation |
| Assessment Result | A scored or otherwise evaluated criterion for a specific assessment subject |
| Evidence | Information supporting an assessment result |
| Assessment Finding | An interpreted observation arising from assessment evidence and results |
| Modernization Opportunity | A recognized opportunity or need for architectural change |
| Modernization Objective | The outcome or change objective associated with the modernization opportunity |
| Target Architecture | The desired architecture state against which change is directed |
| Modernization Intervention | A proposed architectural or organizational response |
| Capability Implication | Capability required, improved, introduced, retired, or transformed |
| Architecture Decision | A decision governing architecture change or realization |
| Modernization Initiative | A coordinated effort to realize one or more modernization interventions |
| Outcome | A result achieved through modernization |
| Value Realization | The value evidenced through the modernization outcome |

## Why the separation matters

This structure permits the framework to evolve independently from individual assessment instances, assessed architectures, modernization initiatives, and execution plans. It preserves traceability from the assessment criterion through evidence, findings, modernization objectives, architecture decisions, initiatives, and outcomes.

Entity schemas, identifiers, and lifecycle definitions are being formalized per [ROADMAP.md](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/ROADMAP.md) slice S6.
