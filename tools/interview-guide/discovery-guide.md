# Interview and Discovery Guide

A starter question bank for gathering assessment evidence per dimension. Questions are prompts for inquiry, not the assessment itself: the assessment unit is the criterion proposition (see the [criterion catalog](../criterion-catalog/criteria-catalog.yaml)), and interview answers are recorded as evidence against criteria.

## General discovery (before dimension work)

- What is the assessment subject: enterprise, portfolio, domain, system, or component?
- Who owns this architecture, and who depends on it?
- What documentation, models, and inventories exist, and how current are they?
- Is there a declared architecture, and do practitioners believe the implemented one differs? (D3.3 leads here.)

## D1 · Strategic Alignment & Relevance

- Which strategic objectives does this architecture directly enable? Where is that traceable?
- Where does the architecture currently constrain what the business wants to do?
- What value does the business attribute to this architecture? Would the business notice if it degraded?
- What strategic direction is anticipated, and can this architecture support it?

## D2 · Drivers & Environmental Context

- What business changes (growth, expansion, operating model change) are pressuring this architecture?
- What technology shifts or end-of-life events touch it?
- What regulatory, audit, or standards changes apply within the planning horizon?
- What do customers, partners, and the workforce expect that it does not deliver?
- What event or decision, if any, triggered this assessment?

## D3 · Architecture Baseline & Condition

- Is there a complete, current inventory of the architectural elements in scope?
- How accurate are the models and documentation? When were they last validated?
- Where does the declared architecture differ from what is actually implemented and deployed?
- Which elements are obsolete, unsupported, or near end-of-life?
- Who owns the baseline, and can it be traced to evidence?

## D4 · Architectural Fitness & Performance

- Does the architecture fulfill its intended functions? Where are the functional gaps?
- Does performance (throughput, responsiveness, capacity) meet requirements today? Under forecast demand?
- Which quality attributes (reliability, scalability, maintainability) are deficient?
- Where is integration costly, fragile, or unreliable?
- How effectively does it support day-to-day operations and service delivery?

## D5 · Structural Integrity & Complexity

- Can components be changed independently, or does change propagate?
- Are architectural boundaries clear, and are they respected?
- Is complexity growing faster than the organization's capacity to absorb it?
- Where do duplicate capabilities, systems, or components exist?
- Does the realized architecture conform to its stated principles and standards?

## D6 · Exposure, Risk & Sustainability

- What is the technology lifecycle exposure (obsolescence, vendor dependency, skills scarcity)?
- What security, privacy, or trust weaknesses exist?
- What are the operational failure scenarios, and how recoverable are they?
- What does it cost to own and maintain, and is that economically sustainable?
- What compliance or governance exposure exists?
- Is the architecture viable over the long term, environmentally and operationally?

## D7 · Adaptability & Modernization Readiness

- How long and how expensive is a typical change?
- Can new capabilities be added without structural rework?
- Can modernization be executed incrementally, or does it demand a big-bang transition?
- Do the teams have the engineering and delivery capacity (automation, testing, deployment) to execute?
- Does the organization have the skills, governance, sponsorship, and funding to sustain it?
- What constraints (contracts, dependencies, policy, legacy) limit transition options?

## D8 · Target State & Modernization Value

- Is a target state defined? How clear and viable is it?
- What measurable outcomes is modernization intended to achieve?
- Which alternatives were considered, and how were they evaluated?
- What value (business, operational, technical, stakeholder) is expected?
- What investment is required, and what are the trade-offs?
- Is there a sequenced path from current to target state?

## Evidence capture conventions

- Record every answer as evidence linked to a criterion ID, with source and date.
- Distinguish observation (what was seen) from interpretation (what it means); findings are interpreted later, at assessment synthesis.
- Where evidence is missing, capture that too: missing evidence bounds confidence, and low confidence in D3 bounds confidence everywhere else.
