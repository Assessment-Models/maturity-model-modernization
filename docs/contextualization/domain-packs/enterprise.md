# Enterprise Architecture Pack

Contextualization pack for the enterprise architecture domain (catalog domain id `enterprise`). It instantiates the [fan-out model](../fan-out-model.md): common findings from the criterion catalog are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Enterprise architecture covers the organization's structure as a whole: the operating model, business capability map, technology-business alignment, and the coherence of investment across the estate. Typical subjects: the enterprise landscape, a capability area, a cross-cutting platform or program scope.

## Domain concern catalog

The concerns this domain evaluates when interpreting a common finding, and the dimensions each most commonly reads:

| Concern | Reads | Evaluates, in enterprise terms |
|---------|-------|--------------------------------|
| Investment coherence | D1.3, D8.5 | Whether money and attention concentrate on the same things across units, or scatter over overlapping efforts |
| Strategic alignment of change | D1.1, D1.4, D8.1 | Whether planned moves serve stated strategy and the future business |
| Ecosystem posture | D2.1, D8.1 | How the organization intends to interoperate with partners and the outside world |
| Capability overlap | D5.4 | Duplicated capabilities and overlapping mandates across the landscape |
| Enterprise dependency structure | D5.1, D5.2 | Cross-capability and cross-system dependencies that gate any sequenced change |
| Enterprise risk position | D6.3, D6.6 | Aggregate operational exposure and long-term viability at the estate level |
| Transformation readiness | D7.3, D7.5 | Organizational capacity to run cross-cutting programs, not single projects |
| Governance architecture | D3.6, D6.5 | Whether decision rights and records are reliable enough to steer a program |

## Vocabulary mapping

Common terms translate as follows when findings are stated in this domain:

| Common term | Enterprise vocabulary |
|-------------|------------------------|
| Baseline (condition) | Capability and operating model health as invested today |
| Fitness | Business-technology alignment |
| Coupling | Cross-capability dependency |
| Fragmentation | Duplicated capability investment and overlapping mandates |
| Drift | Strategy-to-execution divergence in the portfolio |
| Exposure | Enterprise coherence and continuity risk |
| Readiness | Transformation capacity across programs |
| Target state | Future operating model and capability target |
| Opportunity | An investment-level modernization move on the roadmap |

## Evidence sources

- Strategy documents, business capability maps, operating model definitions
- Investment and portfolio records, program charters, budget lines
- Governance records: architecture board minutes, decision logs, exceptions registers
- Enterprise inventories and dependency maps
- Value realization records and post-implementation reviews
- Leadership and strategy stakeholder interviews (context and strategic demand)

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Capability rationalization | Fragmentation findings: consolidate duplicated capabilities under one mandate |
| Portfolio alignment | Alignment and value findings: point investment at the stated strategy |
| Governance redesign | Constraint and governance findings: fix decision rights, records, and escalation |
| Ecosystem strategy definition | Demand and target findings: set the partner interoperability posture |
| Roadmap sequencing | Constraint and dependency findings: order cross-cutting moves by dependency, not by appetite |
| Value tracking establishment | Value findings: tie each move to a recorded value expectation |

## Implication templates

A common finding becomes an enterprise implication by these templates:

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "A fragmented or inadequate <element> reads at enterprise level as <incoherent investment or misalignment>; consolidate or align it via <pattern>, under one decision point." |
| Exposure | "An outside-tolerance risk on <element> becomes an enterprise risk posture item: register it, set the governing decision, and assign ownership at estate level." |
| Demand | "Committed future demand on <element> sets a capability target; align investment and sequencing to meet it, not to admire it." |
| Constraint | "Path constraints stage the move: <preparatory pattern> first, then the main <pattern>, re-assessing at each gate." |
| Strength | "Assets such as <basis> anchor the target operating model; reuse them rather than rebuilding." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis findings F-1 (severe fragmentation of integration mechanisms) and F-5 (committed ecosystem demand), the deficiency and demand templates derive:

> **Align ecosystem integration strategy and investment.**

Derivation note: fragmentation of a strategically demanded capability (F-1, F-5) reads at enterprise level as incoherent investment against a committed ecosystem posture; the portfolio alignment and ecosystem strategy definition patterns produce the implication.

## Cross-domain overlap

Overlap is a link, never a duplication: implications across domains share the opportunity identifier and the finding basis, not each other's content. Enterprise implications for O-1 typically co-occur with the [information systems](information-systems.md) redundancy implication (portfolio-level vs landscape-level rationalization) and the [data](data.md) ownership implication (who owns exchange semantics is an enterprise decision). The link is recorded as: opportunity O-1, domain `enterprise`, implication statement above, basis F-1, F-5.
