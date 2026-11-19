# Domain Packs (Scaffold)

Each architecture domain gets a contextualization pack that turns a common finding into a domain-specific interpretation. The packs are the drill-down of the [fan-out model](fan-out-model.md) and are built per [ROADMAP.md](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/ROADMAP.md) slice S4.

## Pack structure (template)

Every domain pack follows the same structure:

1. **Domain scope and vocabulary**: what this architecture discipline covers, and how common terms (condition, fitness, coupling, exposure, readiness) translate into domain vocabulary.
2. **Domain concern catalog**: the specific concerns this domain evaluates when interpreting a common finding.
3. **Evidence sources**: where this domain's evidence typically lives (models, repositories, registries, operational records, governance artifacts).
4. **Intervention patterns**: the characteristic modernization interventions this domain contributes (e.g., boundary restructuring for software architecture, contract standardization for service architecture).
5. **Implication templates**: how a generic finding becomes a domain-specific implication statement.
6. **Cross-domain links**: which findings typically co-occur with other domains' implications, so overlap is represented by relationship rather than duplication.

## Planned packs

- [ ] Enterprise Architecture
- [ ] Business Architecture
- [ ] Information Systems Architecture
- [ ] Data Architecture
- [ ] Technology Architecture
- [ ] Systems Architecture
- [ ] Service-Oriented Architecture
- [ ] Software Architecture
- [ ] Solution Architecture
- [ ] Implementation Architecture

## Drill-down questions per pack

- What are the domain's recurring modernization concerns, in the domain's own vocabulary?
- Which common criteria most often require domain-specific interpretation here?
- What evidence does this domain uniquely hold, and what does it commonly lack?
- Which intervention patterns does this domain own end-to-end, and which does it only contribute to?
- How do this domain's implications typically depend on or enable other domains' implications?

Done-when: the integration example (see [`docs/examples/integration-architecture.md`](../examples/integration-architecture.md)) can be re-derived purely from the domain packs.
