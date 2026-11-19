# Business Architecture Pack

Contextualization pack for the business architecture domain (catalog domain id `business`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Business architecture covers value streams, business processes, business services, and the organization that delivers them. Typical subjects: a value stream, a business capability in operation, a customer or partner journey, an operating unit and its services.

## Domain concern catalog

| Concern | Reads | Evaluates, in business terms |
|---------|-------|------------------------------|
| Value stream performance | D1.3, D4.5 | Whether the stream delivers value smoothly or through friction and manual work |
| Process adequacy | D4.1, D4.6 | Whether processes meet the business needs they exist for |
| Cross-business interaction | D4.4, D5.2 | How units, partners, and channels reach each other: directly, or through manual bridges |
| Journey friction | D4.4, D2.4 | Where onboarding and service journeys stall, for customers and partners alike |
| Duplicated business function | D5.4 | Several units performing overlapping business functions |
| Process drift | D3.3 | Designed process versus the process actually executed |
| Business continuity exposure | D6.3, D6.6 | Operational and viability risk carried by the business operation |
| Change capacity | D7.5 | Whether the organization can absorb operating model change |

## Vocabulary mapping

| Common term | Business vocabulary |
|-------------|---------------------|
| Baseline (condition) | Value stream and process condition as delivered today |
| Fitness | Process and service adequacy toward business outcomes |
| Coupling | Cross-process dependency and handoff structure |
| Fragmentation | Duplicated business functions and overlapping responsibilities |
| Drift | Designed versus executed process (the real process is the one that runs) |
| Exposure | Operational business risk carried by the value stream |
| Readiness | Organizational capacity to absorb operating change |
| Target state | Target business capability and journey design |
| Opportunity | A business-level modernization move with defined outcome |

## Evidence sources

- Value stream and process maps, journey maps, service catalogs
- Process telemetry: throughput, cycle times, handoff counts, rework rates
- Playbooks, procedures, and the actual working instructions people follow
- Organizational charts and responsibility assignment records
- Business reviews, incident and complaint records
- Business owner and operations stakeholder interviews

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Value stream redesign | Fitness and friction findings: remove non-value steps and manual bridges |
| Process simplification | Deficiency findings: collapse duplicated or overly complex process branches |
| Business service consolidation | Fragmentation findings: one service, one owner, one face to the customer or partner |
| Journey redesign | Demand and stakeholder findings: reshape onboarding and interaction journeys |
| Operating model adjustment | Readiness findings: clarify who owns what before the technology changes |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "<Fragmented or weak process area> shows up to the business as <friction, delay, duplicated effort>; simplify or consolidate it via <pattern>, re-anchoring the value stream." |
| Exposure | "Where <element> carries outside-tolerance risk, the business impact of failure is <consequence>; make the continuity expectation explicit before choosing the fix." |
| Demand | "Committed demand on <journey or interaction> cannot be met by the current flow; redesign <journey> to carry it." |
| Constraint | "If change capacity is short, sequence <pattern> as a pilot in one stream, then scale after re-assessment." |
| Strength | "What already works well (<basis>) is the anchor to build the new flow around." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis findings F-1 (fragmented integration logic) and F-5 (partner growth demand exceeding capacity), the deficiency and demand templates derive:

> **Simplify partner onboarding and cross-business interaction.**

Derivation note: fragmented integration read through the value stream concern becomes onboarding friction across business boundaries; the journey redesign and process simplification patterns produce the implication. Basis F-1, F-5.

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The business implication for O-1 typically co-occurs with the [service](service.md) contract implication (journeys are delivered through service contracts) and the [data](data.md) exchange implication (partner interaction depends on shared semantics). Link record: opportunity O-1, domain `business`, implication statement above, basis F-1, F-5.
