# Coverage Argument

The framework claims to be a complete, non-redundant criterion space for architecture modernization assessment: every question that matters to a modernization decision is either covered by a catalog criterion, or is deliberately out of scope. A claim of completeness needs an argument, not an assertion. This page makes that argument and names its limits.

## The claim being argued

The [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml) (v0.4.1, normative, 49 criteria) covers the decision space with 8 dimensions and 47 subdimensions: drivers (D2 external, D3 internal) in several kinds, strategic grounding (D1), subject fitness (D4), structural integrity (D5), risk exposure (D6), adaptability and readiness (D7), and target-state position (D8). The argument proceeds from the purpose of the instrument, not from counting: the dimensions are derived from what a modernization decision needs to know, and the completeness claim is that those needs form a closed set.

## The derivation: assessment kinds, not checklists

Every criterion exists to produce one of a small number of distinct assessment kinds, and the catalog's type distribution (condition 24, exposure 9, target 6, changeability 4, demand 3, readiness 2, criticality 1) reflects that structure. The kind structure, not a topic list, is what the argument rests on:

- A modernization decision must know whether a **driver exists and how strong it is**: conditions and demands in the world (D2), within the estate (D3), and against strategy (D1).
- It must know whether the driver is **material to this subject**: fitness of the subject against its required capabilities (D4).
- It must know **what the subject is structurally** such that it can or cannot meet that requirement: coherence, independence of change, fragmentation (D5).
- It must know **what could go wrong** if nothing changes: exposure against stated tolerance (D6).
- It must know **whether the organization can execute** the change: delivery and organizational capacity, transition feasibility (D7).
- And it must know **whether a decision is even possible**: defined target, objectives, evaluated alternatives, value expectation, path (D8).

Each of the 49 criteria sits in exactly one of these rows, and each row is closed by an identity test: what assessment question would fall outside every row? A question about why change (D1-D3), what change (D4-D5, D8), what risk (D6), or how to execute (D7) exhausts the decision's information needs. A candidate question outside all six is either a restatement of one of them, or a subject-specific fact recorded as evidence, or out of scope by the framework's mandate (for example practice process detail, which belongs to the maturity model's practice assessment, not to architecture subjects; this separation is the [maturity bridge](../methodology/maturity-bridge.md)).

## The mapping: decision to dimensions

| The decision needs to know | Dimension | Question at the assessment layer |
|-----------------------------|-----------|----------------------------------|
| Whether modernization is being driven, and by what | [D2 Drivers & Environmental Context](../taxonomy/d2-drivers-context.md), [D3 Architecture Baseline & Condition](../taxonomy/d3-architecture-baseline.md) | Condition, demand, exposure: which world and estate facts bear on the subject |
| Whether it matters to strategy | [D1 Strategic Alignment & Relevance](../taxonomy/d1-strategic-alignment.md) | Condition and criticality: strategic significance of the subject region |
| Whether the subject is fit for its required capabilities | [D4 Architectural Fitness & Performance](../taxonomy/d4-fitness-performance.md) | Condition and changeability: does the subject meet requirements, and what do its quality attributes permit |
| What the subject is, structurally | [D5 Structural Integrity & Complexity](../taxonomy/d5-structural-integrity.md) | Condition and changeability: coherence, independence of change, fragmentation, modularity |
| What happens if nothing changes | [D6 Exposure, Risk & Sustainability](../taxonomy/d6-exposure-risk.md) | Exposure inside or outside stated tolerance |
| Whether the organization can execute | [D7 Adaptability & Modernization Readiness](../taxonomy/d7-adaptability-readiness.md) | Readiness and changeability at the practice interface |
| Whether the decision can be made now | [D8 Target State & Modernization Value](../taxonomy/d8-target-state-value.md) | Target definition, objectives, alternatives, value, path |

## Deliberate overlaps

A few seams are intentionally readable from two dimensions. These are not redundancy; each overlap records a place where an assessor needs both readings:

| Overlap | Why both readings exist |
|---------|------------------------|
| D3.5.1 Concern coverage vs D5 structural composition | What the baseline covers is a driver-side fact; how the estate is composed is a structure fact; a consolidation decision needs both, which is why the D3.5.1 record cross-references D5 (for example in the [integration example](../examples/integration-architecture.md)) |
| D4.3 quality attributes vs D6 exposure | A quality-attribute limit is a fitness fact (D4.3.1, D4.3.2); whether it yields an outside-tolerance condition is a risk fact (D6); recording them separately prevents the fitness score from silently encoding risk tolerance |
| D2.3.1 compliance drivers vs D6.5.1 compliance and governance exposure | The obligation itself is a driver; whether the subject is exposed to it is separate; this is how a fixed regulatory deadline can drive urgency on an in-tolerance subject (the [onboarding example](../examples/customer-onboarding.md) exercises exactly this pair) |
| D1 strategic grounding vs D8 target position | A clear strategy with no defined target is common and materially different from a defined target with no strategic grounding; both must be separately answerable |
| D7 adaptability vs D4.3.2 change-supporting quality attributes | Whether the organization can change and whether the subject tolerates change are distinct limits; the [maturity bridge](../methodology/maturity-bridge.md) exists precisely because conflating practice readiness with subject changeability was a known historical failure |

## Gaps, by design

The honest content of a completeness claim is the explicit list of what is deliberately absent:

1. **Practice maturity itself**: the catalog measures architecture subjects, as evidenced, and reads practice maturity only in evidence form. The Architecture Modernization Maturity Model owns that space.
2. **Financial quantification**: value and cost appear as scale levels with recorded bases (D8.4.1 value expectation, D8.5.1 economics understood, and the [significance factors](../methodology/prioritization.md)), never as computed monetary figures; the framework records the basis for a business case, not the business case.
3. **Operations-level detail**: the framework is not an operational review; infrastructure engineering detail enters only as evidence for a catalog criterion.
4. **Sector-specific criteria**: sector regulation is handled by D2.3.1 compliance drivers, not by a per-sector criterion set; a sector overlay can never require a ninth dimension.
5. **Criticality as a directly assessed criterion** appears exactly once (D1.5.1 strategic criticality), because criticality everywhere else in the framework is an overlay attribute on results and profiles, never a score weight.

## Domain completeness is a mapping property, not a criterion property

Each criterion carries a domain applicability map over the [ten domain packs](../contextualization/domain-packs.md): all 49 criteria cite at least one pack, with information systems and solution citing all 49, data, service, and software at 48, technology and systems at 46, enterprise at 38, implementation at 27, and business at 16. The distribution is itself evidence of design: business and implementation read fewer criteria because those packs contextualize different questions (business reads what the estate means for journeys and value; implementation reads what change means for execution paths), not because they are under-served. A criterion with an empty map would be a coverage defect; none exists.

## Conclusion

No coverage argument by itself proves a taxonomy complete; what it can prove is closure under the framework's decision needs, and that every deliberately absent space is owned by another instrument or another method. Both hold: the six assessment-kind rows close the decision space, the overlaps are recorded seams rather than accidents, the by-design gaps each have a named owner, and no candidate question has been identified that requires a ninth dimension. The empirical corner checks, how the instrument behaved on real assessments across three subjects, are recorded in the [validation notes](validation-notes.md).
