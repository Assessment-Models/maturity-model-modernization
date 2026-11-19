# Data Architecture Pack

Contextualization pack for the data architecture domain (catalog domain id `data`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Data architecture covers data domains, models, quality, ownership, lineage, platforms, and the exchange of data between systems. Typical subjects: a data domain or product, a set of exchange flows, the data estate behind a capability or journey.

## Domain concern catalog

| Concern | Reads | Evaluates, in data terms |
|---------|-------|---------------------------|
| Data asset condition | D3.2, D4.1 | Whether the data (quality, completeness, structure) can carry its load |
| Exchange semantics | D4.4, D5.1 | Whether exchanged data agrees in meaning across producers and consumers |
| Data copy sprawl | D5.4 | Duplicated stores and copies made outside any design decision |
| Ownership and accountability | D3.5, D6.5 | Whether owners, stewards, and decision rights for data exist and act |
| Lineage and provenance | D3.2, D3.3 | Whether anyone can trace data from origin to use, on record |
| Data risk and trust | D6.2, D6.3 | Security, privacy, and trust exposure riding on the data flows |
| Data readiness | D7.2 | How much data change (models, stores, flows) the organization absorbs |
| Target data position | D8.1, D8.2 | Whether the target data architecture and outcomes are defined |

## Vocabulary mapping

| Common term | Data vocabulary |
|-------------|-----------------|
| Baseline (condition) | Data estate condition: models, quality, flows as they run |
| Fitness | Data adequacy for the uses it must serve |
| Coupling | Semantic and store-level dependency: consuming another system's data model |
| Fragmentation | Copy sprawl and duplicated data holdings |
| Drift | Declared versus actual schema and semantics |
| Exposure | Data security, privacy, and trust exposure on the flows |
| Readiness | Capacity to absorb model and flow change |
| Target state | Target data architecture: domains, ownership, exchange design |
| Opportunity | A data-level move: standardize semantics, consolidate copies, establish ownership |

## Evidence sources

- Data models, schema repositories, data catalogs
- Data quality measurements and issue registers
- Lineage records and actual flow inventories (what really moves where)
- Ownership and stewardship records, governance decisions
- Security and privacy assessments on data in flight and at rest
- Data owners, stewards, and platform engineers

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Semantic standardization | Exchange and coupling findings: canonical exchange models agreed and versioned |
| Ownership establishment | Ownership and governance findings: one named domain owner per dataset |
| Copy rationalization | Fragmentation findings: reduce copies to designed ones, on record |
| Exchange redesign | Fitness and demand findings: replace hidden database-level exchange with designed flows |
| Lineage establishment | Inventory and drift findings: traceable paths before further change |
| Data platform consolidation | Fragmentation at platform level: fewer stores with designed purposes |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "<Fragmented or undocumented data area> turns into integration as <ungoverned copies or hidden couplings>; standardize via <pattern> and put an owner on the result." |
| Exposure | "Data flows carrying outside-tolerance risk (<element>) must be redesigned on contract before volume or partners increase." |
| Demand | "Committed exchange demand (<basis>) defines canonical semantics work now: agree what the exchanged data means before scaling it." |
| Constraint | "Where model change is hard to absorb (<basis>), stage semantics: versioned contracts first, physical consolidation later." |
| Strength | "Existing quality or lineage assets (<basis>) anchor the new exchange design; build on recorded truth." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis findings F-1 (fragmented integration logic) and F-2 (unreliable representation), the deficiency template derives:

> **Standardize data exchange, semantics, and ownership.**

Derivation note: duplicated integration mechanisms have each imposed their own exchange semantics with no owner; the semantic standardization and ownership establishment patterns produce the implication. Basis F-1, F-2.

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The data implication for O-1 typically co-occurs with the [service](service.md) contract implication (contracts carry the semantics) and the [enterprise](enterprise.md) ownership implication (who owns enterprise exchange is an estate decision). Link record: opportunity O-1, domain `data`, implication statement above, basis F-1, F-2.
