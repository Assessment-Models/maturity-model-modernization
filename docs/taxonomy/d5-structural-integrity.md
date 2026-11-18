# D5 · Structural Integrity & Complexity

**Assessment objective**: evaluate the internal composition, coherence, relationships, dependencies, and structural characteristics of the architecture.

## Subdimensions and assessment criteria

| Subdimension | Assessment criteria |
|--------------|---------------------|
| D5.1 Architectural Coherence | Consistency of architecture elements, principles, patterns, and structures |
| D5.2 Coupling & Dependencies | Degree of interdependence, dependency concentration, and dependency management |
| D5.3 Complexity | Structural, conceptual, technical, operational, and cognitive complexity |
| D5.4 Fragmentation & Duplication | Redundancy, overlap, inconsistency, proliferation, and fragmentation |
| D5.5 Modularity & Separation | Boundaries, encapsulation, cohesion, separation of concerns, and composability |
| D5.6 Architectural Integrity | Conformance to architectural intent, standards, patterns, and constraints |

## Modernization signals

- Excessive coupling prevents independent change.
- Architectural boundaries are unclear or violated.
- Complexity is increasing faster than organizational capacity.
- Duplicate capabilities, systems, or components proliferate.
- Architectural inconsistency makes integration or governance difficult.

## Interpretation notes

D5 is the strongest predictor of **modernization difficulty** (see [changeability in the evidence model](../methodology/evidence-model.md)). Structural findings often convert directly into sequencing constraints: high coupling (D5.2) does not merely indicate a deficiency, it constrains how any modernization can be staged. The worked criterion example for this dimension is [D5.2 Coupling & Dependencies](../metamodel/criterion-model.md), modeled as a full proposition in the criterion catalog.

Because complexity is both a cause and an effect, D5.3 findings should record whether complexity originates in the architecture itself, in the organization around it, or in their interaction. The intervention differs in each case.
