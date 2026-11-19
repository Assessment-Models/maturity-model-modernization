# Solution Architecture Pack

Contextualization pack for the solution architecture domain (catalog domain id `solution`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Solution architecture covers solution scope, requirements alignment, solution design, technology choices, constraints, trade-offs, and the architecture decisions that govern a specific solution. Typical subjects: a solution or project scope, a solution cluster, the fit of proposed designs to the assessment findings.

## Domain concern catalog

| Concern | Reads | Evaluates, in solution terms |
|---------|-------|------------------------------|
| Scope and requirements alignment | D4.1, D4.6 | Whether the solution scope still matches the requirements it serves |
| Integration fit | D4.4, D5.2 | Whether proposed integration designs fit the assessed integration reality |
| Technology choice soundness | D8.3, D6.1 | Whether options were evaluated against lifecycle and exposure, not novelty |
| Constraint and trade-off discipline | D7.6, D8.5 | Whether constraints are recorded and trade-offs decided, not discovered late |
| Solution overlap | D5.4 | Several solutions covering the same need at growing cost |
| Design-reality drift | D3.3, D5.6 | Designed solution versus built and running solution |
| Solution risk | D6.3, D6.5 | Feasibility, compliance, and delivery risk concentrated in the design |
| Target solution definition | D8.1, D8.6 | Whether the target solution and its boundaries are defined and decidable |

## Vocabulary mapping

| Common term | Solution vocabulary |
|-------------|---------------------|
| Baseline (condition) | Solution scope, design, and fit as currently defined |
| Fitness | Requirements alignment of the solution under its constraints |
| Coupling | Solution integration dependencies, chosen and imposed |
| Fragmentation | Overlapping solutions for the same need |
| Drift | Designed versus implemented solution |
| Exposure | Feasibility, compliance, and delivery risk in the design |
| Readiness | Capacity to deliver the solution as designed |
| Target state | Target solution design with explicit boundaries and decisions |
| Opportunity | A solution-level move: define patterns, boundaries, and decisions |

## Evidence sources

- Solution designs and architecture overviews, decision logs
- Requirements records and traceability
- Constraint registers (business, technical, regulatory)
- Option evaluations and proof-of-concept results
- Delivery reviews and design authority records
- Solution architects and accountable delivery owners

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Solution boundary definition | Overlap and scope findings: one solution, one owner, explicit boundaries |
| Target pattern definition | Demand and target findings: standard patterns the solution must follow |
| Decision enforcement | Drift findings: recorded decisions with owners, checked at design reviews |
| Trade-off re-decision | Feasibility findings: revisit choices against assessed constraints, on record |
| Solution portfolio pruning | Fragmentation findings: merge overlapping solutions deliberately |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "Fragmented or unpatterned design (<element>) leaves each solution choosing differently; define <pattern> and hold solutions to it." |
| Exposure | "Designs carrying outside-tolerance risk (<element>) must re-decide their trade-offs against the assessed constraints before delivery." |
| Demand | "Committed demand (<basis>) becomes the reference case for target patterns: solutions design against it, not against habit." |
| Constraint | "Where constraints bind (<basis>), record them in the decision log and design the staged path around them." |
| Strength | "Soundly decided parts (<basis>) become the pattern other solutions follow." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis findings F-1 (fragmented mechanics) and F-7 (clearly defined target position), the deficiency template derives:

> **Define target integration patterns and solution boundaries.**

Derivation note: with the target position defined (F-7) but mechanics fragmented (F-1), solution design work is naming the target integration patterns and the boundaries each solution must respect; the target pattern definition and boundary definition patterns produce the implication. Basis F-1, F-7.

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The solution implication for O-1 binds the [service](service.md) contract implication into concrete, reusable solution patterns and inherits the [software](software.md) modularization implication inside each solution boundary. Link record: opportunity O-1, domain `solution`, implication statement above, basis F-1, F-7.
