# Software Architecture Pack

Contextualization pack for the software architecture domain (catalog domain id `software`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Software architecture covers software structure: modules, components, codebases, design patterns, and the qualities the code carries, including technical debt and test discipline. Typical subjects: an application or codebase, a component cluster, an integration codebase, the software behind a capability.

## Domain concern catalog

| Concern | Reads | Evaluates, in software terms |
|---------|-------|-------------------------------|
| Module structure | D5.5, D5.1 | Whether responsibilities localize in modules with clean interfaces |
| Codebase health | D3.2, D3.4 | Understandable, maintained code versus rotted, patched history |
| Dependency discipline | D5.2, D5.6 | What depends on what inside and across codebases, and whether intended |
| Test autonomy | D4.3, D7.4 | Whether change can be verified without full-stack heroics |
| Duplicated logic | D5.4 | Same integration or business rule implemented in several codebases |
| Intent conformance | D5.6, D3.3 | Architecture documents versus the code that actually runs |
| Debt exposure | D6.3, D6.4 | What the accumulated debt will cost, at change time |
| Target software position | D8.1, D8.6 | Target component model and migration path |

## Vocabulary mapping

| Common term | Software vocabulary |
|-------------|---------------------|
| Baseline (condition) | Codebase and component condition as maintained today |
| Fitness | Software qualities: behavior, testability, performance |
| Coupling | Code-level dependency: imports, calls, shared internals |
| Fragmentation | Duplicated logic and copy-paste code paths |
| Drift | Architecture intent versus implemented code |
| Exposure | Technical debt exposure at change time |
| Readiness | Engineering capacity and test automation to absorb change |
| Target state | Target component and interface model |
| Opportunity | A software move: modularize, decouple, consolidate logic, automate tests |

## Evidence sources

- Repositories, dependency and import graphs, build records
- Static analysis: complexity, duplication, coupling measures
- Test suites, coverage, and their actual runtimes (can they run, and in minutes or days?)
- Design documents versus code reality (checked, not asserted)
- Change records: how long a typical change takes and what it breaks
- Engineers and technical leads: the people who actually change the code

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Modularization | Structure findings: extract modules with owned responsibilities |
| Interface decoupling | Coupling findings: replace shared internals and reaching-in with defined interfaces |
| Logic consolidation | Fragmentation findings: one implementation of each rule, reused |
| Test automation establishment | Readiness and verification findings: fast, autonomous tests as the safety net for everything else |
| Componentization for integration | Missing integration layer: integration logic lives in components, not sprinkled through business code |
| Architecture record establishment | Drift findings: record decisions, then enforce them with checks |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "<Duplicated or entangled logic> in code (<element>) resists change; consolidate or decouple via <pattern>, with tests as the precondition." |
| Exposure | "Where debt puts safe change outside reach (<element>), pay it back at the seams you must cross, not everywhere." |
| Demand | "Committed functional or interaction demand (<basis>) lands in components with defined ownership, not in the closest open file." |
| Constraint | "Where test automation is absent (<basis>), establish it before loosening any coupling: unverified decoupling is just moved chaos." |
| Strength | "Where tests and structure already hold (<basis>), reuse those components as the modular core of the target." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis findings F-1 (duplicated integration logic) and F-3 (coupling prevents independent change), plus constraint F-6 (absent automated testing), the deficiency template derives:

> **Introduce modular integration components and decoupled interfaces.**

Derivation note: integration logic duplicated across codebases becomes shared, modular integration components behind stable interfaces; the test automation establishment pattern (F-6) sequences first. Basis F-1, F-3; constraint F-6.

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The software implication for O-1 implements the [service](service.md) contract implication (components realize the governed contracts) and rides the [technology](technology.md) platform move (components deploy to the consolidated platform). Link record: opportunity O-1, domain `software`, implication statement above, basis F-1, F-3, F-6.
