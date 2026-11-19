# Systems Architecture Pack

Contextualization pack for the systems architecture domain (catalog domain id `systems`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Systems architecture covers system boundaries, composition, behavior, interfaces, dependencies, and system qualities: how individual systems are built and how they interact as systems. Typical subjects: a system, a system cluster or pair, the interaction structure of a landscape area.

## Domain concern catalog

| Concern | Reads | Evaluates, in systems terms |
|---------|-------|------------------------------|
| Boundary clarity | D3.1, D5.5 | Whether responsibilities and interfaces between systems are drawn and honored |
| Interaction structure | D4.4, D5.2 | Synchronous chains, hidden synchronous calls, emergent cycles |
| System qualities | D4.2, D4.3 | The qualities each system must hold: latency, availability, recoverability |
| Resilience and failure behavior | D6.3, D4.3 | What happens when a dependency fails: planned degradation or cascade |
| Composition integrity | D5.1, D5.3 | Whether the parts fit together coherently at tolerable complexity |
| Interface contract reality | D3.3, D5.6 | Specified versus implemented interfaces |
| Verification reach | D4.3, D7.4 | Whether interaction behavior is testable and tested |
| Target composition | D8.1, D8.6 | The target system decomposition and the path to it |

## Vocabulary mapping

| Common term | Systems vocabulary |
|-------------|--------------------|
| Baseline (condition) | System composition and interaction structure as implemented |
| Fitness | System qualities against required behavior |
| Coupling | Interface and dependency coupling between systems |
| Fragmentation | Redundant components and overlapping system responsibilities |
| Drift | Specified versus implemented interface behavior |
| Exposure | Failure propagation and resilience risk across the interaction structure |
| Readiness | System-level change capacity in the interaction structure |
| Target state | Target system decomposition with defined contracts |
| Opportunity | A systems move: re-cut boundaries, redesign interactions, harden or simplify composition |

## Evidence sources

- System and interface design documents, sequence and interaction diagrams
- Runtime dependency data: call graphs, observed traffic, failure traces
- Failure and incident records showing actual failure propagation
- Test coverage on interactions (contract, integration, end-to-end)
- Architecture records: decision logs covering boundaries and exceptions
- System owners and interaction engineers

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Boundary re-cut | Boundary and fragmentation findings: redraw responsibilities so change localizes |
| Interface contract redesign | Coupling and drift findings: explicit, versioned contracts for real interactions |
| Dependency de-cycling | Coupling findings: break emergent cycles and hidden synchronous chains |
| Resilience engineering | Exposure findings: planned degradation where dependencies fail |
| Interaction test establishment | Readiness and verification findings: interaction behavior under test before moves |
| Composition simplification | Complexity findings: fewer parts, fewer interaction kinds |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "<Unclear or fragmented system structure> means interactions are <implicit or brittle>; re-cut boundaries or redesign contracts via <pattern>." |
| Exposure | "Failure paths that propagate (<element>) need planned degradation, documented and tested, not heroics at 2am." |
| Demand | "Committed interaction demand (<basis>) exceeds current interaction structure: redesign the contracts that must carry it." |
| Constraint | "Where interaction testing is absent (<basis>), test the seams before moving anything across them." |
| Strength | "Conformance to intent holds where (<basis>): those parts survive the target decomposition intact." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis findings F-3 (coupling across mechanisms prevents independent change) and F-4 (fragile dependencies outside tolerance), the constraint and exposure templates derive:

> **Clarify system boundaries and manage integration dependencies as explicit, verifiable interfaces.**

Derivation note: multiple undocumented mechanisms mean system interaction structure is implicit; the boundary re-cut and interface contract redesign patterns produce the implication. Basis F-3, F-4.

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The systems implication for O-1 is the parent of the [service](service.md) contract implication (system contracts surface as service contracts) and constrains the [software](software.md) modularization implication (module boundaries follow system boundaries). Link record: opportunity O-1, domain `systems`, implication statement above, basis F-3, F-4.
