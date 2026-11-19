# Assessment Taxonomy

The common assessment organizes modernization opportunity into eight dimensions that collectively establish a complete view of why modernization is necessary, what is being modernized, how significant the need is, and what the organization should do about it.

The taxonomy is a model that can be instantiated for enterprise, business, information, data, technology, systems, software, service, implementation, or solution architecture. Dimensions are architecture-agnostic in intent; subdimensions and criteria provide the specificity that makes the assessment meaningful.

## Structure

Each dimension carries:

- An **assessment objective**.
- **Subdimensions**, each with assessment criteria.
- **Modernization signals**: observable conditions that indicate modernization relevance.
- **Interpretation notes** where the dimension requires careful reading.

## The dimensions

| ID | Dimension | Establishes | Doc |
|----|-----------|-------------|-----|
| D1 | Strategic Alignment & Relevance | Why modernization matters and the strategic outcomes it should enable | [d1-strategic-alignment.md](d1-strategic-alignment.md) |
| D2 | Drivers & Environmental Context | Internal and external forces creating the need or opportunity to modernize | [d2-drivers-context.md](d2-drivers-context.md) |
| D3 | Architecture Baseline & Condition | The current architecture, its characteristics, condition, and operational reality | [d3-architecture-baseline.md](d3-architecture-baseline.md) |
| D4 | Architectural Fitness & Performance | How effectively the architecture fulfills its intended purpose and requirements | [d4-fitness-performance.md](d4-fitness-performance.md) |
| D5 | Structural Integrity & Complexity | Coherence, dependencies, coupling, consistency, and accumulated complexity | [d5-structural-integrity.md](d5-structural-integrity.md) |
| D6 | Exposure, Risk & Sustainability | Operational, strategic, technical, economic, security, and lifecycle exposure | [d6-exposure-risk.md](d6-exposure-risk.md) |
| D7 | Adaptability & Modernization Readiness | The ability to change the architecture and the capacity to execute and sustain change | [d7-adaptability-readiness.md](d7-adaptability-readiness.md) |
| D8 | Target State & Modernization Value | The desired state, alternatives, expected value, and transformation direction | [d8-target-state-value.md](d8-target-state-value.md) |

## Identifier conventions

- Dimensions: `D1`-`D8`.
- Subdimensions: `D<n>.<m>` (e.g., `D5.2` Coupling & Dependencies).
- Criteria: stable IDs assigned in the [criterion catalog](../../tools/criterion-catalog/criteria-catalog.yaml); architecture disciplines are never encoded into criterion identifiers or definitions. Domain applicability is a separate relationship.

## Status

The taxonomy is complete and normative. Every criterion is fully modeled in the [criterion catalog](../../tools/criterion-catalog/criteria-catalog.yaml) (v0.2.0, status: normative): definition, assessment intent, assessment question, assessment type, applicability rule, assessment method, evidence requirements, interpretation guidance, modernization relevance, and domain applicability. The catalog is the normative source for all criteria; these taxonomy docs carry the narrative context around it. Terminology follows the [glossary](../framework/glossary.md).
