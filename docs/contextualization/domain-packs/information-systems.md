# Information Systems Architecture Pack

Contextualization pack for the information systems architecture domain (catalog domain id `information-systems`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Information systems architecture covers the application and system landscape: what each system does, where its responsibilities begin and end, what depends on what, and which systems should exist at all. Typical subjects: an application portfolio or segment, a system cluster, the landscape serving a business area.

## Domain concern catalog

| Concern | Reads | Evaluates, in information systems terms |
|---------|-------|------------------------------------------|
| Landscape responsibility map | D3.1, D3.5 | Whether responsibilities over the landscape are known and complete |
| Application redundancy | D5.4 | Overlapping systems doing the same job at different costs |
| System dependency burden | D4.4, D5.2 | The fan-in and fan-out of dependencies each system carries |
| Inventory and interface reality | D3.2, D3.3 | Declared versus implemented interfaces, connections, and inventory entries |
| Lifecycle position | D3.4, D6.1 | Which systems sit at end-of-life and drag the landscape |
| Portfolio risk | D6.3, D6.6 | Operational and viability risk concentrated at the portfolio level |
| Portfolio changeability | D7.1, D7.3 | How much independent change the landscape tolerates |
| Target landscape definition | D8.1, D8.3 | Whether a defensible target landscape and alternatives exist |

## Vocabulary mapping

| Common term | Information systems vocabulary |
|-------------|-------------------------------|
| Baseline (condition) | Application and system landscape condition as running today |
| Fitness | Functional and interaction adequacy of the systems portfolio |
| Coupling | System-to-system dependency, direct and via shared datastores |
| Fragmentation | Application redundancy: same function, several systems |
| Drift | Declared versus implemented interfaces and inventory records |
| Exposure | Portfolio-level risk: single points of failure at estate scale |
| Readiness | Ability to absorb system replacements and interface change |
| Target state | Target application landscape with explicit boundaries |
| Opportunity | A landscape-level move: retire, replace, consolidate, re-cut |

## Evidence sources

- Application portfolios, system registers, CMDB records
- Interface inventories and actual connection data (network records, API gateways)
- Lifecycle and support records: versions, vendor dates, run-cost
- Dependency data: dependency graphs, integrations observed in production
- Project post-mortems and retirement decisions already made
- Application owners and landscape architects

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Application rationalization | Fragmentation findings: reduce overlapping systems with a stated rule (cost, capability, lifecycle) |
| System retirement | Lifecycle and risk findings: turn end-of-life positions into sequenced exits |
| Boundary re-cut | Coupling and dependency findings: redraw system responsibilities so change localizes |
| Dependency pruning | Risk findings: remove hidden dependencies (direct database access, file drops) before anything moves |
| Interface consolidation | Redundancy of mechanics: fewer integration mechanisms, written down per interface |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "Fragmentation or drift at the landscape level (<element>) means <redundant systems or undocumented connections>; consolidate via <pattern> and record what remains." |
| Exposure | "A system or cluster carrying outside-tolerance risk (<element>) should not be extended: stabilize it, ring-fence it, or exit it, per the risk record." |
| Demand | "Committed demand that the current systems cannot absorb (<basis>) must land as landscape work now: allocate it openly, or lose it to shadow systems." |
| Constraint | "Where changeability is low (<basis>), sequence the safe patterns first: no direct-to-target jumps where dependencies are unpruned." |
| Strength | "Dependency and inventory records that already exist (<basis>) reduce the integration effort for the new architecture." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis finding F-1 (severe fragmentation: multiple integration mechanisms, duplicated logic), the deficiency template derives:

> **Reduce integration redundancy and system dependency.**

Derivation note: duplicated integration logic across mechanisms is application redundancy read at landscape scale; the interface consolidation and dependency pruning patterns produce the implication. Basis F-1, F-2.

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The information systems implication for O-1 typically co-occurs with the [technology](technology.md) platform implication (mechanisms run on platforms) and the [service](service.md) contract implication (each retained interface becomes a governed contract). Link record: opportunity O-1, domain `information-systems`, implication statement above, basis F-1, F-2.
