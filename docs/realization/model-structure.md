# Model Structure and Formalization Sequence

## Position within OpenDEA

AMAF is treated as a distinct assessment model within OpenDEA, structured along these lines:

```
Architecture Modernization Assessment Model
│
├── Assessment Framework
│   ├── Assessment Dimensions
│   │   └── Assessment Subdimensions
│   │       └── Assessment Criteria
│   ├── Assessment Scales
│   ├── Assessment Methods
│   ├── Assessment Rules
│   ├── Assessment Profiles
│   └── Architecture Domain Applicability
│
├── Assessment Instance
│   ├── Assessment Context
│   ├── Assessment Scope
│   ├── Assessment Subjects
│   ├── Criterion Results
│   ├── Evidence
│   └── Findings
│
├── Modernization Opportunity
│   ├── Modernization Drivers
│   ├── Modernization Objectives
│   ├── Value Hypothesis
│   ├── Priority
│   └── Target State
│
├── Architecture Contextualization
│   ├── Enterprise Architecture Implications
│   ├── Business Architecture Implications
│   ├── Data Architecture Implications
│   ├── Information Systems Implications
│   ├── Technology Architecture Implications
│   ├── Systems Architecture Implications
│   ├── Service Architecture Implications
│   ├── Software Architecture Implications
│   ├── Solution Architecture Implications
│   └── Implementation Architecture Implications
│
└── Modernization Realization
    ├── Architecture Decisions
    ├── Capability Changes
    ├── Modernization Interventions
    ├── Initiatives
    ├── Roadmaps
    ├── Outcomes
    └── Value Realization
```

The separation permits the framework to evolve independently from individual assessment instances, assessed architectures, modernization initiatives, and execution plans.

## Formalization sequence

The foundation is formalized in this order:

1. **Assessment Framework Foundation**: purpose, scope, principles, terminology, assessment architecture, normative model boundaries.
2. **Assessment Taxonomy**: formalize the eight dimensions, subdimensions, definitions, and domain applicability.
3. **Criterion Catalog**: define the assessment criteria, propositions, applicability rules, evidence, and interpretation.
4. **Assessment Mechanics**: define scales, assessment methods, scoring, confidence, evidence sufficiency, weighting, and aggregation rules.
5. **Modernization Interpretation**: define how findings, context, risk, value, and target expectations generate modernization opportunities and priorities.
6. **Architecture Domain Contextualization**: formalize how the common framework fans out to architecture-specific implications, concerns, and interventions.
7. **Modernization Realization Model**: connect modernization objectives to architecture decisions, capabilities, initiatives, transition plans, outcomes, and value.
8. **Assessment Instrument & Validation**: develop the instrument, test against different architecture domains and organizational contexts, and validate the model for completeness and consistency.

The next most valuable step is step 2-3: formalizing the eight dimensions into a complete, normative assessment taxonomy, including the full subdimension structure and criterion catalog, before defining scoring or maturity progression. This establishes the conceptual foundation and validates that the assessment covers architecture modernization holistically rather than prematurely locking into an assessment instrument. This is tracked as [ROADMAP.md](../../ROADMAP.md) slice S1.
