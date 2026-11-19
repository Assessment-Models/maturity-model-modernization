# Implementation Architecture Pack

Contextualization pack for the implementation architecture domain (catalog domain id `implementation`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Implementation architecture covers realization mechanisms: implementation patterns, build and deployment pipelines, configuration, environments, automation of build, test, deploy, and operate. Typical subjects: a delivery pipeline and its environments, a realization approach, the engineering mechanics behind a platform or product.

## Domain concern catalog

| Concern | Reads | Evaluates, in implementation terms |
|---------|-------|-------------------------------------|
| Pipeline health | D4.5, D3.6 | Whether build, test, and deploy run fast, trusted, and reproducibly |
| Configuration discipline | D3.2, D3.3 | Configured versus recorded configuration; environment drift |
| Release mechanics | D4.4, D5.2 | Deployment coupling: what must be deployed together, and how risky that is |
| Automation coverage | D4.3, D7.4 | What verification runs automatically versus what humans hero |
| Environment readiness | D7.3, D3.6 | Whether environments can stand up and serve modernization increments |
| Delivery risk visibility | D6.3, D7.6 | Whether execution constraints and failure modes are known before go-live |
| Realization fidelity | D5.6, D3.3 | Whether what ships matches what was designed, automatically checked |
| Target realization model | D8.6, D8.1 | The target delivery mechanics for the target architecture |

## Vocabulary mapping

| Common term | Implementation vocabulary |
|-------------|---------------------------|
| Baseline (condition) | Pipeline and environment condition as running today |
| Fitness | Delivery effectiveness: speed, trust, reproducibility of the mechanics |
| Coupling | Deployment and release coupling across components |
| Fragmentation | Divergent environments, scripts, and per-team tooling |
| Drift | Configured versus recorded environment and configuration |
| Exposure | Execution risk surfacing at deploy time (the worst place to meet it) |
| Readiness | Engineering mechanics able to carry the planned changes |
| Target state | Target delivery model: pipelines, environments, automation as designed |
| Opportunity | A realization move: automate, standardize, decouple releases |

## Evidence sources

- Pipeline definitions and run records (durations, failure rates, manual steps)
- Configuration repositories versus live configuration; environment inventories
- Release records: what deployed, with what, how often, with what rollback
- Incident records at deploy and release time
- Automation coverage data: what tests gate what changes
- Build and release engineers, environment owners

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Pipeline automation | Fitness and readiness findings: build, test, deploy run without ceremony |
| Configuration as code | Drift findings: environments erected from records, not memory |
| Test automation establishment | Verification and readiness findings: automated integration and contract tests as gates (the explicit constraint-finding response for fragile integration estates) |
| Release decoupling | Deployment coupling findings: independent deployment over synchronized big-bang releases |
| Rollback and observability establishment | Delivery risk findings: reversible releases and watched rollouts |
| Environment standardization | Fragmentation findings: one shape of environment, reproducibly produced |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "<Manual or fragile delivery mechanics> make every integration change a ceremony; automate via <pattern> and gate the seams." |
| Exposure | "Deliveries whose failure modes are unknown (<element>) need reversible releases and watched rollouts before cadence rises." |
| Demand | "Committed change volume (<basis>) forces the mechanics upgrade now: automate the paths the change will travel, not the ones it might." |
| Constraint | "Where test automation is absent (<basis>), it gates the whole path: stand it up first as the preparatory initiative of the program." |
| Strength | "Existing pipeline or IaC assets (<basis>) extend to the new components; wire the new services into them, do not fork them." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with constraint F-6 (delivery capacity limited by absent automated testing) against severe findings F-1, F-2, the constraint and demand templates derive:

> **Automate configuration, testing, deployment, and operational realization.**

Derivation note: standardized integration services arrive through repeatable delivery: configuration as code, automated tests at the new seams (closing F-6), and decoupled releases; the constraint template makes this the program's first staged work. Basis F-1, F-2; constraint F-6.

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The implementation implication for O-1 realizes the [software](software.md) modularization implication through pipelines and lands the [technology](technology.md) platform implication in standardized environments. Link record: opportunity O-1, domain `implementation`, implication statement above, basis F-1, F-2, F-6.
