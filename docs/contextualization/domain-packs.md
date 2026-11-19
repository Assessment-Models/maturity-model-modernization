# Domain Packs

Each architecture domain has a contextualization pack that turns a common finding into a domain-specific interpretation. The packs are the drill-down of the [fan-out model](fan-out-model.md), built per [ROADMAP.md](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/ROADMAP.md) slice S4 (complete).

Every pack follows the same structure, so implications across domains are comparable:

1. **Domain scope**: what the discipline covers, its typical subjects and scopes.
2. **Domain concern catalog**: the concerns the domain evaluates when interpreting a common finding, each with the dimensions it most commonly reads.
3. **Vocabulary mapping**: how common terms (baseline, fitness, coupling, fragmentation, drift, exposure, readiness, target state) translate into the domain's vocabulary.
4. **Evidence sources**: where this domain's evidence typically lives.
5. **Intervention patterns**: the characteristic modernization interventions this domain contributes, each with the findings it addresses.
6. **Implication templates**: rule-like templates that turn a finding class into a domain implication statement.
7. **Worked implication**: the domain's implication for the shared [integration example](../examples/integration-architecture.md), derived by template, with its basis findings.
8. **Cross-domain overlap**: how the implication links to other domains' implications, by relationship rather than duplication.

## The packs

| Domain | Pack | Identifying question |
|--------|------|----------------------|
| Enterprise | [Enterprise pack](domain-packs/enterprise.md) | Is investment coherent with strategy? |
| Business | [Business pack](domain-packs/business.md) | Does the value stream carry the interaction smoothly? |
| Information Systems | [Information systems pack](domain-packs/information-systems.md) | Are there too many systems doing the same thing? |
| Data | [Data pack](domain-packs/data.md) | Does the exchanged data mean the same thing everywhere? |
| Technology | [Technology pack](domain-packs/technology.md) | What do the platforms and tooling actually run? |
| Systems | [Systems pack](domain-packs/systems.md) | Are boundaries and interactions explicit and resilient? |
| Service | [Service pack](domain-packs/service.md) | Can consumers be served through governed contracts? |
| Software | [Software pack](domain-packs/software.md) | Does the code localize change behind interfaces? |
| Solution | [Solution pack](domain-packs/solution.md) | Do solution designs follow defined patterns and boundaries? |
| Implementation | [Implementation pack](domain-packs/implementation.md) | Can the change be delivered repeatably and reversibly? |

## How a finding becomes an implication

The derivation is rule-governed, matching the [interpretation logic](../methodology/interpretation-logic.md):

1. The finding arrives with its class (deficiency, exposure, demand, constraint, strength), severity, and basis results; the domain never re-scores it.
2. The pack's concern catalog determines which domain concerns the finding reads through.
3. The implication template for the finding class produces the implication statement, instantiated with the domain's vocabulary.
4. The intervention patterns name the characteristic response the domain contributes.
5. Provenance is preserved: the implication records the opportunity identifier, domain, finding basis, and template used.

## Cross-domain overlap representation

One opportunity spanning several domains is represented by linkage, not duplication (see the [fan-out model](fan-out-model.md)):

- Implications belong to exactly one pack; no pack restates another pack's implication.
- Every implication records the same opportunity identifier and its own finding basis.
- Co-occurrence links (which implications typically travel together, and why) are recorded per pack, as relationship records: opportunity, domain, statement, basis.
- The shared assessment remains the single source of truth; implications are linked interpretations.

## Validation

The done-when for the packs: the [integration example](../examples/integration-architecture.md) is re-derivable purely from the packs. Its re-derivation section maps each domain implication to the pack and template that produce it; the ten packs above are the validated source.
