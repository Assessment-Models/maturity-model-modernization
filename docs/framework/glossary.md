# Glossary

Normalized terminology for the AMAF assessment. These terms mean one thing across all dimensions, docs, and tools. The intention of each term, as used in the catalog's `definition`, `assessment_intent`, and `interpretation_guidance` attributes, follows the definitions below.

Where a term is also a modeled entity, its authoritative structural description lives in the [metamodel](../metamodel/entities.md); this glossary normalizes meaning.

## Assessment structure

**Assessment** — The application of the criterion catalog to a subject at a scope, producing findings per criterion.

**Subject** — The architectural thing being assessed: an architecture, an element of one, or a set of elements treated as a unit. The subject is the referent of every criterion: propositions read as statements about the subject.

**Scope** — The boundary declaration of an assessment instance: which subject, which concerns, which time constraint, and which change demand the results apply to.

**Dimension** — One of the eight top-level lenses of the taxonomy (`D1`-`D8`) that collectively establish why modernization matters, what exists and how fit it is, what could go wrong, and what should be done about it.

**Subdimension** — A named subdivision of a dimension (`D<n>.<m>`), collecting criteria that share a concern (coupling, operational risk, and so on).

**Criterion** — A stable, independently assessable unit in the [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml), identified as `D<n>.<m>.<k>`. Each criterion is a modeled proposition with a full attribute set: definition, assessment intent, assessment question, assessment type, applicability rule, assessment method, scale reference, evidence requirements, interpretation guidance, modernization relevance, domain applicability, and related criteria.

**Proposition** — The affirmative statement a criterion makes about the subject. A criterion score expresses how true the proposition holds for the subject, on the five-point scale.

## Evidence types and assessment types

**Condition** — The state of the subject as it stands today: whether the proposition holds now. Assessed on current evidence.

**Demand** — The expected duties on the subject: whether the proposition will hold against the anticipated future the organization has actually stated. Always assessed against recorded anticipated demand, never against speculation.

**Exposure** — The subject's known vulnerabilities and liabilities, and whether the resulting risk is within tolerance. Exposure is scored as knowledge plus tolerance alignment, not as raw risk level. Backed by the `criticality_scale` and tolerance record.

**Criticality** — The importance of the subject: how much strategic-execution and business-continuity weight it carries. The criterion scores whether criticality is established and accepted, not how high it is.

**Readiness** — The organization's capacity to execute and sustain change on the subject, independent of the subject's own merits.

**Changeability** — The subject's practical capacity to undergo change at appropriate ease, speed, cost, and risk. Changeability is always judged against a realistic change portfolio, and never collapsed into a single condition score.

**Target** — The desired future state of the subject and the modernization opportunity around it. Target criteria assess the quality of the target position itself (clarity, viability, objectives, options, economics, path), not its implementation.

## Assessment judgment

**Finding** — A criterion-level assessment result: a judgment on the proposition, with its evidence basis, confidence, and a dated interpretation. Findings are the atomic output of assessment.

**Evidence** — The artifacts, metrics, records, and interview testimony that support a finding, per the criterion's evidence requirements. What counts as sufficient evidence follows the [evidence model](../methodology/evidence-model.md).

**Confidence** — How well-supported a finding is on its evidence, on the three-level confidence scale (low: assertion-level evidence, medium: some direct evidence with incomplete coverage, high: direct, sufficient, corroborated evidence).

**Evidence item** — The unit of evidence: a single, dated, identifiable artifact or testimony, with a class (direct or indirect), a source, and a mapping to the criterion's evidence requirements. Counting, corroboration, and confidence assignment follow the [evidence mechanics](../methodology/evidence-mechanics.md).

**Band profile** — The distribution of criterion results over the scale, reported per subdimension or dimension and partitioned by assessment type. It is the only aggregate the framework produces; composite scores do not exist above the dimension level.

**Overshoot** — A negative gap: the current finding sits above the target score. An overshoot of two or more triggers a deliberate-excess review, and is never reported as headroom to spend.

**Practice maturity** — The organization's modernization practice band (L0-L4, canonical v2), assessed by the governed maturity model, not by the catalog. Practice maturity results enter D7 assessment as evidence under the [maturity model bridge](../methodology/maturity-bridge.md), never as converted scores.

**Applicability** — Whether and under what scope conditions a criterion is assessed for the subject. Non-assessment is a recorded decision with a reason (inapplicable, deferred, or out of scope), never a silent omission.

**Interpretation guidance** — The catalog's normative guidance for how to judge a criterion's evidence, including its score guards, common failure modes, and what not to penalize.

**Baseline** — The established representation and reality of the subject before change: today's subject, its condition and its context. Referenced with the reliability expectations of D3.6.

**Drift** — Divergence between a declared state and the realized state (D3.3), or between realized architecture and architectural intent (D5.6). Known and dated drift is a finding; unknown drift is a failure state.

**Gap** — The distance between a criterion's current finding and its target score, stored in the scoring record and used by prioritization to size opportunity.

**Target score** — The level the organization sets as intended for a criterion, within the assessment's time constraint. May equal the current score (no gap, no action).

**Opportunity** — A modernization course of action inferred from findings, with a target-score gap it intends to close and an option set it recommends.

**Priority** — The rank-weighted ordering of opportunities per the [prioritization logic](../methodology/prioritization.md), which combines criticality, gap, exposure, readiness, and changeability evidence.

**Severity** — The rule-derived import of a finding on the ordered scale minor, moderate, material, severe. Severity is derived from score band, gap, criticality overlay, and tolerance per the [interpretation logic](../methodology/interpretation-logic.md), never from intuition, and never averaged across results.

**Preparatory initiative** — A staged initiative ahead of a critical but difficult opportunity that builds readiness, mitigates risk, or cleans the baseline, closing the constraint findings that limit it. It changes the path, never the priority.

**Dependency edge** — The recorded relationship between two opportunities: enables (closing one materially reduces the cost, risk, or scope of the other) or blocks (one cannot proceed until the other is resolved). Edges cite their basis; the dependency map is acyclic, and a cycle is a recorded sequencing conflict.

**Profile** — The assessed pattern across dimensions: which regions of the taxonomy carry findings, qualifying-in or qualifying-out modernization moves.

## Context

**Architecture domain** — One of the ten disciplines the subject may instantiate: enterprise, business, information-systems, data, technology, systems, service, software, solution, implementation architecture. Domain applicability is a relationship of a criterion, never part of its identity.

**Domain applicability** — The catalog-recorded relationship of which architecture domains a criterion's proposition commonly applies to, used to instantiate the assessment for a domain (see the [fan-out model](../contextualization/fan-out-model.md)).

**Driver** — A force creating pressure on or through the subject (business, technology, compliance, stakeholder, environmental). Identified and understood in D2, drivers feed the modernization case and target-state selection in D8.

**Trigger** — The specific event, constraint, threshold, initiative, failure, opportunity, or decision that converts background pressure into committed modernization consideration, characterized with its time horizon (D2.6).

**Contextualization** — The instantiation of the framework for a specific architecture domain, scope, or organization pattern, via domain packs and scope declarations.

**Domain pack** — The contextualization asset for one architecture domain: a concern catalog, vocabulary mapping, evidence sources, intervention patterns, and implication templates that turn common findings into domain implications without re-scoring. See the [domain pack index](../contextualization/domain-packs.md).
