# Service Architecture Pack

Contextualization pack for the service architecture domain (catalog domain id `service`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Service architecture covers service contracts, discoverability, composition, interoperability, and service governance: exposing capabilities as services others can consume with confidence. Typical subjects: a service landscape or catalog, a service family, the consumer-provider structure behind a capability.

## Domain concern catalog

| Concern | Reads | Evaluates, in service terms |
|---------|-------|------------------------------|
| Contract clarity | D3.5, D5.5 | Whether services declare what they do, in versioned, consumable contracts |
| Discoverability | D3.1, D3.2 | Whether consumers can find and understand services without folklore |
| Consumer-provider structure | D4.4, D5.2 | Who consumes what, through which modes, with what coupling |
| Service reuse and overlap | D5.4 | Overlapping services for the same capability, or none at all (point-to-point) |
| Contract-implementation drift | D3.3, D5.6 | Contract versus what the service really does |
| Service-level exposure | D6.3, D6.5 | Ownership, security, and governance risk on exposed services |
| Service changeability | D7.1, D7.2 | Whether providers can evolve safely with consumers attached |
| Target service position | D8.1, D8.6 | The target service landscape and migration path |

## Vocabulary mapping

| Common term | Service vocabulary |
|-------------|-------------------|
| Baseline (condition) | Service landscape condition as consumed today |
| Fitness | Whether existing services meet consumer needs at acceptable quality |
| Coupling | Consumer-provider coupling and composition depth |
| Fragmentation | Overlapping services, or the absence of services where they belong |
| Drift | Contract versus implementation (the contract is the promise; the code is the delivery) |
| Exposure | Governance and security exposure on the service surface |
| Readiness | Ability to version and evolve services with consumers attached |
| Target state | Target service catalog with governed contracts |
| Opportunity | A service move: define contracts and governance, expose or retire services |

## Evidence sources

- Service catalogs, contract definitions (API specifications, interface documents)
- Gateway and registry records; actual consumer lists per service
- Usage telemetry: volumes, error rates, key consumers
- Governance records: versioning decisions, deprecation notices, exceptions
- Contract-implementation conformance checks
- Service owners, consumers, and platform engineers

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Contract standardization | Deficiency and drift findings: consistent contract design rules, versioned |
| Catalog and discoverability establishment | Baseline and fitness findings: findable, documented, owned services |
| Governance establishment | Exposure and ownership findings: versioning, deprecation, and approval on record |
| Service modular exposure | Fragmentation of mechanics: expose capabilities as services instead of point-to-point links |
| Consumer decoupling | Coupling findings: consumer-driven contracts, safe provider evolution |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "<Missing or inconsistent service layer> means consumers integrate ad hoc; establish <pattern>: contracts first, catalog and governance behind them." |
| Exposure | "Ungoverned service exposure (<element>) must be brought under versioning and ownership before new partners attach." |
| Demand | "Committed consumer demand (<basis>) defines the service portfolio now: expose the capabilities partners will consume, with contracts." |
| Constraint | "Where provider evolution is risky (<basis>), version contracts and stage consumer migration before changing implementations." |
| Strength | "Where contracts already hold (<basis>), extend the same governance to the new standardized services." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis findings F-1 (fragmented integration mechanics) and F-2 (undocumented interfaces), the deficiency template derives:

> **Establish consistent service contracts, discoverability, and governance.**

Derivation note: undocumented point-to-point mechanisms are a missing service layer; the contract standardization, discoverability establishment, and governance establishment patterns produce the implication. Basis F-1, F-2.

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The service implication for O-1 concretizes the [systems](systems.md) contract implication (service contracts are the governed form of system contracts) and carries the [data](data.md) semantics (semantics ride in the contract payloads). Link record: opportunity O-1, domain `service`, implication statement above, basis F-1, F-2.
