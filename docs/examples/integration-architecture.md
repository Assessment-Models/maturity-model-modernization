# Worked Example: Integration Architecture Modernization

An illustrative end-to-end pass through the framework: one modernization opportunity, a shared assessment basis, and multiple contextualized architectural implications.

## Scenario

The organization is assessing its integration architecture.

## Assessment summary

| Assessment concern | Result |
|--------------------|--------|
| Strategic alignment | Integration is critical to ecosystem expansion |
| Future demand | New partners and real-time interactions are expected |
| Baseline condition | Multiple integration mechanisms, undocumented interfaces |
| Fitness | Current integrations function but onboarding is slow |
| Structural complexity | High coupling and duplicated integration logic |
| Risk | Fragile dependencies and limited ownership |
| Readiness | Teams have skills but limited automated testing |
| Target state | Standardized, discoverable, independently manageable integration services |

## Interpretation

The common assessment establishes that the modernization need is **not merely a technology upgrade**. It identifies a modernization opportunity characterized by:

- High strategic relevance.
- Increasing future demand.
- Structural fragmentation.
- Limited changeability.
- Integration risk.
- A defined target state.
- A potentially favorable value proposition.

## Domain fan-out

The opportunity fans out into domain-specific modernization implications:

| Architecture | Modernization implication |
|--------------|---------------------------|
| Enterprise Architecture | Align ecosystem integration strategy and investment |
| Business Architecture | Simplify partner onboarding and cross-business interaction |
| Information Systems Architecture | Reduce integration redundancy and system dependency |
| Data Architecture | Standardize data exchange, semantics, and ownership |
| Service Architecture | Establish consistent service contracts, discoverability, and governance |
| Software Architecture | Introduce modular integration components and decoupled interfaces |
| Systems Architecture | Clarify system boundaries and manage integration dependencies as explicit, verifiable interfaces |
| Technology Architecture | Modernize integration platforms, runtime, connectivity, and tooling |
| Solution Architecture | Define target integration patterns and solution boundaries |
| Implementation Architecture | Automate configuration, testing, deployment, and operational realization |

## The point of the example

This is the intended behavior of the framework: **one modernization opportunity, a shared assessment basis, and multiple contextualized architectural implications.** The domain rows are not separate assessments; they are linked interpretations of the same evidence.

## Re-derivation from the domain packs

The domain packs ([slice S4](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/ROADMAP.md)) are complete, and this example is re-derivable purely from them, per the derivation rules of the [domain pack index](../contextualization/domain-packs.md). Each implication is produced by the finding class template of its pack, instantiated with the worked example's basis findings:

| Architecture | Implication | Derived from |
|--------------|-------------|--------------|
| [Enterprise](../contextualization/domain-packs/enterprise.md) | Align ecosystem integration strategy and investment | Deficiency and demand templates, basis F-1, F-5 |
| [Business](../contextualization/domain-packs/business.md) | Simplify partner onboarding and cross-business interaction | Deficiency and demand templates, basis F-1, F-5 |
| [Information Systems](../contextualization/domain-packs/information-systems.md) | Reduce integration redundancy and system dependency | Deficiency template, basis F-1, F-2 |
| [Data](../contextualization/domain-packs/data.md) | Standardize data exchange, semantics, and ownership | Deficiency template, basis F-1, F-2 |
| [Technology](../contextualization/domain-packs/technology.md) | Modernize integration platforms, runtime, connectivity, and tooling | Deficiency template, basis F-1; constraint F-6 stages it |
| [Systems](../contextualization/domain-packs/systems.md) | Clarify system boundaries and manage integration dependencies as explicit, verifiable interfaces | Constraint and exposure templates, basis F-3, F-4 |
| [Service](../contextualization/domain-packs/service.md) | Establish consistent service contracts, discoverability, and governance | Deficiency template, basis F-1, F-2 |
| [Software](../contextualization/domain-packs/software.md) | Introduce modular integration components and decoupled interfaces | Deficiency template, basis F-1, F-3; constraint F-6 stages it |
| [Solution](../contextualization/domain-packs/solution.md) | Define target integration patterns and solution boundaries | Deficiency template, basis F-1, F-7 |
| [Implementation](../contextualization/domain-packs/implementation.md) | Automate configuration, testing, deployment, and operational realization | Constraint and demand templates, basis F-1, F-2, F-6 |

The derivation is the validation test: every implication above is the pack's worked implication, produced by its templates with no step that is not in the pack or the [interpretation logic](../methodology/interpretation-logic.md).

## Machine record and follow-on examples

This example exists as a machine-validated bundle, [`framework/examples/integration-instance.yaml`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/examples/integration-instance.yaml), which also carries the opportunity, contextualization, and realization structures and passes [`framework/validate.py`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/validate.py). Two further worked examples extend it: a second, independent assessment of this same subject forms the [comparability study](inter-rater-comparability.md), and a different subject and organisational context, the onboarding stream of a mutual insurer, is worked in [customer onboarding](customer-onboarding.md). The instrument coverage exercised by all three is tabulated in the [validation notes](../validation/validation-notes.md).
