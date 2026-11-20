# Worked Example: Customer Onboarding Modernization

A second illustrative end-to-end pass through the framework, per the [validation slice](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/ROADMAP.md): a different organisational context from the [integration architecture example](integration-architecture.md), and a subject that spans multiple architecture domains by construction (the [fan-out model](../contextualization/fan-out-model.md) names onboarding as its overlap case).

The example runs under catalog v0.4.1 (`assessment_rules` v1, `interpretation_rules` v2) and is machine-validated: the full record lives in [`framework/examples/onboarding-instance.yaml`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/examples/onboarding-instance.yaml) and passes `python3 framework/validate.py` together with the other worked bundles.

## Scenario

A mutual insurer assesses its customer onboarding value stream: the journey front end, identity verification and KYC checks, policy issuance, and the applications and data stores supporting them, as one capability-level subject. A digital identity verification regulation lands with a fixed 2027 deadline. Unlike the integration example, every result is recorded at its criterion's nominal [assessment type](../methodology/assessment-scales.md), the assessment exercises the sustained-overshoot finding and a standby opportunity, and the [maturity model bridge](../methodology/maturity-bridge.md) supplies practice evidence in the forward direction.

## Assessment summary

| Result | Criterion | Type | Score | Target | Gap | Criticality overlay |
|--------|-----------|------|-------|--------|-----|---------------------|
| RES-01 | D2.3.1 Regulatory & Compliance Drivers | exposure | 2 | 3 | 1 | critical |
| RES-02 | D4.1.1 Functional Adequacy | condition | 2 | 3 | 1 | high |
| RES-03 | D5.4.1 Fragmentation & Duplication | condition | 1 | 4 | 3 | high |
| RES-04 | D2.4.1 Stakeholder Drivers | demand | 2 | 3 | 1 | high |
| RES-05 | D4.3.2 Quality Attributes | changeability | 2 | 4 | 2 | medium |
| RES-06 | D1.1.1 Strategic Alignment | condition | 4 | 4 | 0 | high |
| RES-07 | D7.4.1 Engineering & Delivery Readiness | readiness | 3 | 4 | 1 | medium |
| RES-08 | D6.2.1 Security & Trust | exposure | 5 | 3 | -2 | high |
| RES-09 | D8.1.1 Target State Definition | target | 4 | 4 | 0 | high |
| RES-10 | D3.5.1 Architecture Coverage | condition | 2 | 3 | 1 | low |

## Interpretation into findings

Per the [interpretation logic](../methodology/interpretation-logic.md), classes and severities are derived, never chosen:

| Finding | Class | Severity | Basis | Statement |
|---------|-------|----------|-------|-----------|
| F-1 | Exposure | Severe | RES-01 | Manual KYC checks sit outside stated compliance tolerance on a critical region, against a fixed 2027 deadline (exposure outside tolerance, critical region) |
| F-2 | Deficiency | Material | RES-02 | Journeys stall on incomplete data; straight-through processing is 31 percent against intent (score 2, high criticality) |
| F-3 | Deficiency | Severe | RES-03 | Identity and eligibility logic is fragmented and duplicated across three applications (score 1, gap 3) |
| F-4 | Demand | Material | RES-04 | Committed same-week digital onboarding demand exceeds demonstrated capacity (committed demand) |
| F-5 | Constraint | Material | RES-05 | Journey changes require coordinated tri-application releases (score 2, gap 2) |
| F-6 | Strength | (none) | RES-06 | The stream carries the growth strategy: an agreed strategic anchor |
| F-7 | Constraint | Minor | RES-08 | The fraud and trust target rationale understates the sustained assurance posture: a deliberate-excess overshoot, sustained by review, against the target rationale ([gap semantics](../methodology/aggregation-mechanics.md)) |
| F-8 | Strength | (none) | RES-09 | The target journey design is defined and agreed with compliance |
| F-9 | Deficiency | Moderate | RES-10 | Decision paths and issuance interfaces are undocumented (score 2, low criticality) |

Two mechanics deserve note. RES-08 is the framework's overshoot path executed end to end: a score of 5 against a target of 3 produces the deliberate-excess review note per the gap rules, the review sustains the excess (the committed regulatory direction consumes the headroom), and the sustained overshoot becomes a constraint finding against the target rationale, which lands in the residual **minor** severity row. F-9 is the basis of the standby opportunity below.

## Opportunity synthesis

Per the synthesis rules, F-1 through F-4 concern one subject region and one course of change (a single customer identity service with automated KYC orchestration closes the compliance exposure, the fitness gap, the fragmentation, and the capacity gap together). They form **O-1: Onboarding consolidation onto a single customer identity**. F-5 does not join the theme: it constrains the how and stages the path. F-6 and F-8 ground O-1's target position and option set.

O-1's [prioritization profile](../methodology/prioritization.md): strategic importance high, need high, exposure high (F-1 severe inside), future demand high (F-4), value potential medium (RES-09), urgency high (fixed regulatory deadline), feasibility medium (F-5), readiness medium (RES-07), dependency low. **Critical Modernization is primary; Strategic Modernization is secondary** by dominance order.

**O-2: Onboarding decision-path documentation consolidation** (basis F-9) is recorded honestly as **standby**: need medium (one moderate finding), demand low, exposure low, value low, urgency low. No profile condition is satisfied, so no profile is force-fit; the opportunity carries a review date instead. The consolidated identity service will enable O-2 (recorded as an objective dependency with its basis).

## Domain fan-out

The opportunity fans out into domain-specific implications, each derived from the [domain packs](../contextualization/domain-packs.md):

| Architecture | Modernization implication | Derived from |
|--------------|---------------------------|--------------|
| [Business](../contextualization/domain-packs/business.md) | Simplify onboarding journeys; remove manual KYC bridges from the value stream | Deficiency template, basis F-2, F-4 |
| [Data](../contextualization/domain-packs/data.md) | Standardize customer identity semantics, quality, and ownership | Deficiency template, basis F-3 |
| [Information Systems](../contextualization/domain-packs/information-systems.md) | Consolidate redundant onboarding applications and record what remains | Deficiency template, basis F-2, F-3 |
| [Service](../contextualization/domain-packs/service.md) | Expose identity and eligibility capabilities as governed contracts, with catalog and governance behind them | Deficiency template, basis F-3 |
| [Software](../contextualization/domain-packs/software.md) | Introduce modular onboarding components and decouple the three applications | Deficiency template, basis F-3; constraint F-5 stages it |
| [Technology](../contextualization/domain-packs/technology.md) | Scale identity verification and KYC execution for the committed digital load | Demand template, basis F-1, F-4; overshoot context F-7 supplies headroom |
| [Implementation](../contextualization/domain-packs/implementation.md) | Automate configuration, testing, and deployment for the staged consolidation | Constraint template, constraint F-5 against severe F-1, F-3 |

The machine bundle instantiates five of these implications (business, data, software, technology, implementation) with templates, co-occurrences, and provenance; the information systems and service rows are recorded here per the same derivation rules.

## The maturity bridge in the forward direction

EV-12 is a current Architecture Modernization Maturity Model result: practice band L2 (Systematic, canonical instance `dea:maturity-bands-v2`), scoped to the organization and dated inside the change horizon. Per the [bridge rules](../methodology/maturity-bridge.md) it enters the D7.4.1 readiness assessment as exactly one direct-class practice evidence item, never as a score (R-MB1, R-MB2). Together with corroborating delivery records from the subject's own change history it lifts RES-07's confidence to high (R-MB3), and no conversion happens in either direction. The readiness anchors O-1's readiness factor at medium and removes the need for the preparatory-initiative pattern that the integration example required: adequate, corroborated readiness yields a directly staged path, a deliberate contrast demonstrating that the instrument responds to the recorded facts rather than to the template.

## The point of the example

The domain rows are linked interpretations of one assessment basis, as in the integration example; what is new here is the span. One modernization opportunity produces simultaneous implications in seven domain vocabularies from one evidence trail, the profile space is exercised at both ends (critical-primary and standby), and the overshoot, standby, and maturity-bridge mechanics are all recorded in machine-checkable form. Two independent assessments of this subject and how their profiles compare is the subject of the [comparability study](inter-rater-comparability.md); instrument coverage across all worked examples is tabulated in the [validation notes](../validation/validation-notes.md).
