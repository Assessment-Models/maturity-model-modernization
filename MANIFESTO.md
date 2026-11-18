# The AMAF Manifesto

The Architecture Modernization Assessment Framework (AMAF), in full prose. This document is the source of the framework's reasoning; the docs tree operationalizes it.

## 1. The fundamental problem: architecture modernization is fragmented

Architecture modernization is often approached through the lens of a specific architecture discipline. An enterprise architect may assess enterprise architecture, a business architect may assess business architecture, a technology team may assess infrastructure, and software teams may assess applications and software architecture.

The problem is that these perspectives are individually valid but collectively fragmented. They may identify overlapping modernization needs, use different assessment criteria, recommend conflicting priorities, and produce initiatives that are not traceable to a common modernization objective.

Modernization is not inherently an enterprise architecture, technology architecture, software architecture, or systems architecture initiative. It is an organizational change opportunity that manifests across one or more architecture domains, depending on what needs to change, why it needs to change, and what outcomes the change is expected to achieve.

The central proposition is therefore:

> Architecture modernization should be assessed through a common, architecture-agnostic framework that establishes the nature, urgency, scope, value, and direction of modernization, and subsequently contextualizes the assessment into the specific architectural domains, capabilities, decisions, and interventions required to realize it.

This establishes two distinct but connected assessment concerns:

- **Common modernization assessment**: what needs to modernize, why, how significantly, and toward what desired state?
- **Architecture-specific contextualization**: what does that modernization opportunity mean for each affected architecture, and what changes, capabilities, decisions, and interventions are required?

This separation makes it possible to compare modernization opportunities consistently without erasing the technical and contextual differences between architectural disciplines.

## 2. The conceptual model: common assessment, architectural realization

The framework should not attempt to unify every architecture discipline into a single architecture. Instead, it should unify the assessment of modernization while preserving the distinct concerns of each architecture.

The backbone:

1. **Common Modernization Assessment** - drivers, context, current state, gaps, risks, value, readiness, direction.
2. **Architecture Contextualization** - translate modernization findings into architecture-specific concerns, objectives, and target states.
3. **Modernization Intervention** - architecture changes, capabilities, decisions, roadmaps, programs, projects.
4. **Outcome & Realization** - modernized architecture, measurable outcomes, verified value, sustained improvement.

The assessment dimensions are architecture-agnostic in their intent, but their findings must be capable of being interpreted within a specific architectural context.

## 3. The eight assessment dimensions

The common assessment organizes modernization opportunity into eight dimensions:

- **D1. Strategic Alignment & Relevance** - why modernization matters and the strategic outcomes it should enable.
- **D2. Drivers & Environmental Context** - internal and external forces creating the need or opportunity to modernize.
- **D3. Architecture Baseline & Condition** - the current architecture, its characteristics, condition, and operational reality.
- **D4. Architectural Fitness & Performance** - how effectively the architecture fulfills its intended purpose and requirements.
- **D5. Structural Integrity & Complexity** - coherence, dependencies, coupling, consistency, and accumulated complexity.
- **D6. Exposure, Risk & Sustainability** - operational, strategic, technical, economic, security, and lifecycle exposure.
- **D7. Adaptability & Modernization Readiness** - the ability to change the architecture and the organization's capacity to execute and sustain change.
- **D8. Target State & Modernization Value** - the desired state, modernization alternatives, expected value, and transformation direction.

These dimensions should be sufficiently universal to assess different architecture types, while their subdimensions and criteria provide the specificity necessary to make the assessment meaningful.

## 4. Condition, importance, and direction are distinct

One of the most important modeling decisions is not to treat every assessment criterion as a simple maturity question. Architecture modernization requires understanding at least four different types of assessment evidence:

1. **Condition** - how good, adequate, healthy, effective, or deficient is the current architecture?
2. **Criticality** - how consequential is the architecture or criterion to the organization?
3. **Future demand** - how significantly will future needs, requirements, or ambitions differ from current capacity?
4. **Changeability** - how readily can the architecture be changed, and how difficult is modernization likely to be?

These are not interchangeable. An architecture can have good condition but low future fitness, poor condition but low business criticality, high criticality and poor condition (creating urgent modernization), high modernization need but low readiness (creating transformation risk), or strong fitness but excessive cost (making economic modernization attractive). The assessment model captures these independently, allowing meaningful conclusions to emerge from their relationships.

## 5. A common assessment scale

The core assessment uses a consistent five-point criterion scale, supplemented by applicability, evidence confidence, and criticality:

1. **Inadequate** - material deficiency; fails expectations or creates significant exposure.
2. **Weak** - partially adequate; significant limitations, weaknesses, or improvement needs exist.
3. **Adequate** - generally satisfies current expectations, with identified deficiencies or opportunities.
4. **Strong** - performs well; limited weaknesses and well-managed improvement needs.
5. **Leading** - highly effective, optimized, or strategically advanced relative to defined expectations.

Every criterion result carries additional attributes: applicability, criticality, evidence, confidence, target score, gap, commentary, recommendation, and assessed scope.

A low assessment score should not automatically imply a modernization requirement. A criterion must be interpreted in the context of criticality, strategic relevance, future demand, risk, target condition, and evidence. An obsolete component may score poorly but be immaterial to the organization, while a seemingly healthy architecture may warrant substantial modernization because it cannot support a critical strategic direction.

## 6. Architecture-specific contextualization

The common framework establishes a modernization assessment independent of architecture type. Architecture-specific contextualization is where the assessment becomes actionable: the assessment fans out into distinct architecture domains (enterprise, business, information systems, data, technology, systems, service, software, solution, implementation), with each domain interpreting the common assessment through its own vocabulary, scope, concepts, concerns, criteria, capabilities, and intervention patterns.

The domains are not mutually exclusive. One modernization opportunity may span several domains, and the framework explicitly represents that overlap rather than force a finding into one architecture category. The common assessment is the source of truth for the modernization opportunity; architecture-specific assessments are linked interpretations and elaborations of that opportunity, not independently competing assessments.

## 7. The assessment metamodel

The framework is modeled as a taxonomy and assessment metamodel rather than maintained as a static assessment spreadsheet. Distinct entities are not collapsed into one object: framework, dimension, subdimension, criterion, scale, domain, domain concern, method, rule, assessment instance, subject, result, evidence, finding, opportunity, objective, target architecture, intervention, capability implication, decision, initiative, outcome, and value realization.

This structure preserves traceability from the assessment criterion through evidence, findings, modernization objectives, architecture decisions, initiatives, and outcomes.

A criterion is the most important unit of assessment: a structured proposition that describes a condition capable of being evaluated against a defined context and evidence, with modeled attributes covering its definition, assessment intent and method, applicability, scale, evidence requirements, interpretation guidance, modernization relevance, domain applicability, weighting, and related criteria. The architecture discipline is not encoded into the criterion identifier; domain applicability is a separate relationship.

## 8. From assessment to modernization need

The framework does not simply produce an assessment score. It produces a reasoned modernization interpretation. A modernization opportunity emerges through the combination of assessment results, evidence, context, strategic demand, criticality, risk, and target-state expectations, and then fans out into domain-specific modernization implications.

## 9. Prioritization without false precision

Prioritization is supported, but a single composite modernization score is avoided as the primary outcome; an average can conceal critical weaknesses and create false precision. Prioritization derives from multiple independent factors: strategic importance, modernization need, future demand, exposure, value potential, urgency, feasibility, readiness, and dependency. These generate prioritization profiles: **critical modernization**, **strategic modernization**, **risk-driven modernization**, and **opportunity-driven modernization**.

Readiness is considered separately from priority. A highly critical but difficult-to-execute opportunity may require preparatory initiatives, risk mitigation, capability development, or staged modernization, rather than simply being deprioritized.

## 10. The framework produces more than a report

Defined outputs: the Modernization Assessment Profile, Modernization Findings, Modernization Opportunities, Architecture Implication Profiles, Modernization Priorities, and the Modernization Roadmap. Ultimately the assessment answers: where modernization is needed, why, what is driving it, how significant the need is, the consequence of inaction, the value it could produce, which architecture domains are affected, which capabilities change, which decisions are required, the target state, what should be modernized first, how it should be realized, and whether modernization delivered its intended value.

## 11. A modernization assessment, not a maturity model

There is a meaningful distinction between an architecture maturity assessment and an architecture modernization assessment. Maturity evaluates progression of an architecture or practice; modernization assessment evaluates change, fitness, value, risk, and future demand, and produces modernization objectives, interventions, and architectural change. Maturity may be a useful input where architectural governance, engineering, organizational, or delivery capability constrains modernization, but maturity should not become the organizing principle of the modernization assessment.

## 12. The central architectural proposition

The most consequential part of this framework is that it separates the assessment of modernization from the architecture of modernization. The former provides a common, consistent, comparable, evidence-based way to determine modernization need. The latter determines how that need translates into specific architectural implications, decisions, capabilities, interventions, and realization paths.

This allows an organization to assess modernization at an enterprise level, a portfolio level, a domain level, a system level, or an individual architectural component level, without inventing a new assessment methodology for each architecture discipline.

**The unifying principle: one modernization assessment foundation, multiple architectural interpretations, coordinated realization.**
