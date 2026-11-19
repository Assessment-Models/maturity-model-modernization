# Framework Model Artifacts

Home of the formal AMAF model artifacts: the metamodel, entity schemas, machine rules, and a validated end-to-end example instance, per [ROADMAP.md](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/ROADMAP.md) slice S6. The structure follows the [model structure](../docs/realization/model-structure.md).

Status: populated (S6). One command validates the whole set:

```
python3 framework/validate.py
```

Exit 0 and one `ok:` line means the example instance validates against all package schemas and every machine rule re-derivation, the relationship registry, the rule set, and the criterion catalog cross-checks all pass. The validator is stdlib-only and reuses the catalog exporter parser ([`tools/criterion-catalog/export-catalog.py`](../tools/criterion-catalog/export-catalog.py)).

## Three interconnected artifacts

Per the ROADMAP S6 drill, the model is published as three distinct but interconnected artifacts:

1. **Assessment Framework** ([`metamodel/assessment-framework-model.yaml`](metamodel/assessment-framework-model.yaml)): the reusable structure; dimensions, subdimensions, criteria, scales, methods, rules, domains.
2. **Assessment Instance** ([`metamodel/assessment-instance-model.yaml`](metamodel/assessment-instance-model.yaml)): one execution; context, scope, subjects, criterion results, evidence, findings.
3. **Modernization Realization** ([`metamodel/modernization-opportunity-model.yaml`](metamodel/modernization-opportunity-model.yaml), [`metamodel/architecture-contextualization-model.yaml`](metamodel/architecture-contextualization-model.yaml), [`metamodel/modernization-realization-model.yaml`](metamodel/modernization-realization-model.yaml)): from findings to value; opportunities, domain fan-out, interventions, initiatives, outcomes, value realization.

The registry of all three, with lineage, identifier conventions, versioning policy, lifecycle stages, contract evaluation, and the 30-relationship registry, is [`metamodel/amaf-metamodel.yaml`](metamodel/amaf-metamodel.yaml).

## Contents

| Path | Class | What it is |
|------|-------|------------|
| `metamodel/amaf-metamodel.yaml` | Normative | Metamodel manifest: lineage (OpenDEA `dea-metamodel` pin), entity packages, identifier and versioning conventions, lifecycle stages, contract evaluation, 30-relationship registry |
| `metamodel/assessment-framework-model.yaml` | Normative | The framework package model |
| `metamodel/assessment-instance-model.yaml` | Normative | The instance package model |
| `metamodel/modernization-opportunity-model.yaml` | Normative | The opportunity package model |
| `metamodel/architecture-contextualization-model.yaml` | Normative | The contextualization package model (domain packs, templates, implications) |
| `metamodel/modernization-realization-model.yaml` | Normative | The realization package model (interventions, decisions, initiatives, outcomes, value) |
| `schemas/common.schema.json` | Normative | Shared definitions: identifier, version, modelReference, AMAF enums, nine-factor significance |
| `schemas/assessment-instance.schema.json` | Normative | Instance document schema (assessment, subjects, results, evidence, findings) |
| `schemas/assessment-framework.schema.json` | Normative | Framework document schema |
| `schemas/modernization-opportunity.schema.json` | Normative | Opportunity document schema (opportunities, objectives, target positions) |
| `schemas/architecture-contextualization.schema.json` | Normative | Contextualization document schema (packs, templates, implications) |
| `schemas/modernization-realization.schema.json` | Normative | Realization document schema |
| `schemas/relationship.schema.json` | Normative | Typed relationship edge schema (one registry entry) |
| `rules/amaf-rules.yaml` | Normative | Machine rule set v1: 37 rules (R-SCO-1 .. R-PREP-1) with parameters, expressions, and normative sources, mirroring catalog assessment_rules v1 and interpretation_rules v1 |
| `examples/integration-instance.yaml` | Informative | The worked end-to-end example: the docs integration instance formalized as model records, from criterion scores and evidence through findings, one opportunity with profiled prioritization, domain implications, an intervention, decision, staged initiatives with a preparatory P-1 and re-assessment gate, to an observed outcome and value realization |
| `validate.py` | Derived tool | Stdlib validator: JSON Schema subset checks plus semantic re-derivation of the rules over the example |

The example's assessment and opportunity sections restate the documented worked example ([interpretation logic](../docs/methodology/interpretation-logic.md), [prioritization](../docs/methodology/prioritization.md), the [integration example](../docs/examples/integration-architecture.md)); the realization tail is an illustrative extension, marked informative.

## Design constraints honored

- The framework evolves independently from assessment instances, assessed architectures, initiatives, and execution plans (three artifacts, separate lifecycles).
- Criterion identity never encodes architecture disciplines; domain applicability is a relationship, and the fan-out happens in the contextualization package.
- Assessment rules are model entities, not prose only: every applicability, scoring, confidence, sufficiency, aggregation, gap, weighting, finding, severity, opportunity, prioritization, and dependency constraint carries a rule id in `rules/amaf-rules.yaml`.
- Traceability from criterion to value realization is representable end to end without free-text workarounds: the example proves it, and `validate.py` re-derives the chain (gap arithmetic, corroboration, classes, floors, severity, parking, dominance ordering, stage coverage of severe and material findings).

## Identifier conventions

Declared in the metamodel manifest: criterion ids follow the `D[1-8](.n){0,2}` pattern; record ids use prefixes `AS-` (assessment), `SUB-` (subject), `RES-` (result), `EV-` (evidence), `F-` (finding), `O-` (opportunity), `OBJ-` (objective), `TGT-` (target architecture position), `IMP-` (domain implication) with `IT-` (implication template), `IV-` (intervention), `CAP-` (capability implication), `DEC-` (architecture decision), `INIT-` (initiative), `OUT-` (outcome), `VR-` (value realization); rule ids follow `R-<KIND>-<n>`.

## Contract evaluation summary

Recorded in the metamodel manifest against the pinned `technehub-labs/dea-metamodel` contract suite:

- **AMAF conforms now**: `conformance-contract` (common identifier/version/modelReference shapes) and `maturity-scale-contract` (declared through the repository handshake in `model.yaml`).
- **Recommended adopt (S7 decision)**: `assessment-contract`, the natural home for assessment instances on the OpenDEA AssessmentResult/AssessmentExecution lineage.
- **Not applicable now**: `benchmark-contract` (no cohort comparisons in scope) and `scoring-contract` (AMAF aggregation is band profiles; composite scoring machinery does not apply to the criterion scale side).
- **Extension declared, not published**: the modernization chain (opportunity, implication, intervention, initiative, outcome, value realization) has no published contract family; the entities are declared AMAF-owned here. Promotion to an organisation contract family would follow the dea-metamodel change request process and is deliberately not attempted from this repo.

## Pointers

- Catalog: [`tools/criterion-catalog/`](../tools/criterion-catalog/) (criteria, scales, machine rules source of truth for the criteria side)
- Assessment instrument: [`tools/assessment-app/`](../tools/assessment-app/) (implements the same rule set interactively)
- Methodology and metamodel prose: [`docs/metamodel/`](../docs/metamodel/), [`docs/methodology/`](../docs/methodology/)
