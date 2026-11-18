# Framework Model Artifacts (Scaffold)

This directory is the future home of the formal AMAF model artifacts: the metamodel expressed as schemas and model files suitable for modeling in OpenDEA, following the [model structure](../docs/realization/model-structure.md).

## Intended contents (per ROADMAP slice S6)

- **Assessment Framework Model**: dimensions, subdimensions, criteria, scales, methods, rules, domain applicability.
- **Assessment Instance Model**: assessment context, scope, subjects, criterion results, evidence, findings.
- **Modernization Opportunity Model**: drivers, objectives, value hypothesis, priority, target state.
- **Architecture Contextualization Model**: domain implication profiles per architecture domain.
- **Modernization Realization Model**: decisions, capability changes, interventions, initiatives, roadmaps, outcomes, value realization.

## Design constraints

- The framework evolves independently from assessment instances, assessed architectures, initiatives, and execution plans.
- Criterion identity never encodes architecture disciplines; domain applicability is a relationship.
- Assessment rules (applicability, aggregation, interpretation, thresholds) are expressed in the model, not only in prose.
- Traceability from criterion to value realization is representable end-to-end without free-text workarounds.

Status: scaffold. Entity definitions currently live in [`docs/metamodel/`](../docs/metamodel/entities.md).
