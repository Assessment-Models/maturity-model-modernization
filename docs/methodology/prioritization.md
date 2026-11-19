# Prioritization and Decision Logic

## No composite score as the primary outcome

The framework supports prioritization but avoids producing a single composite modernization score as its primary outcome. An average can conceal critical weaknesses and create false precision. Prioritization derives from multiple independent factors and produces **prioritization profiles** rather than relying solely on a numerical rank. What a profile is, and what ordering is allowed, is fixed below and in the `interpretation_rules` section of the [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml).

## Modernization priority factors

For every opportunity, each of the nine factors is assessed on the anchored three-level scale (low, medium, high) per the [interpretation logic](interpretation-logic.md) that produced the opportunity:

| Factor | What it determines | Derived from |
|--------|--------------------|--------------|
| Strategic Importance | How important the architecture is to strategic execution | D1 results and the criticality overlay |
| Modernization Need | Severity of current deficiencies and inadequacy | The severity of deficiency, demand, and exposure findings |
| Future Demand | Magnitude of the gap between current fitness and future requirements | Demand results against recorded anticipated demand, and D2 drivers/triggers |
| Exposure | Risk, economic burden, operational vulnerability, and sustainability | Exposure findings and stated tolerances (D6) |
| Value Potential | Expected benefit or value from modernization | D8 value criteria (expectations, economics) |
| Urgency | How soon modernization is necessary | The trigger characterization and time horizon (D2.6) |
| Feasibility | Practical ability to execute modernization | Changeability results and the option set |
| Readiness | Organizational, technical, and delivery preparedness | D7 results, with practice maturity as evidence per the [maturity bridge](maturity-bridge.md) |
| Dependency | Whether modernization enables or blocks other modernization opportunities | The dependency map (below) |

### Qualitative anchors per factor

Each factor level is anchored so two assessors with the same evidence assign the same level. Levels cite their basis: a factor level with no finding, result, or record behind it is an opinion, not a rating.

**Strategic Importance** (low) the subject is peripheral to strategic execution and carries low criticality; (medium) the subject supports strategic execution, criticality established at medium or high; (high) the subject carries strategic execution or business continuity, criticality overlay high or critical with D1 support.

**Modernization Need** (low) no below-adequacy findings on the opportunity's subject region; (medium) only moderate-severity findings; (high) at least one material or severe finding.

**Future Demand** (low) no recorded anticipated demand beyond current capacity; (medium) recorded anticipated demand exists, and demand results show capacity stretched; (high) recorded, committed demand materially exceeds demonstrated capacity (demand results at score 2 or below).

**Exposure** (low) risks known and within stated tolerance; (medium) risks known with tolerance pressure, or knowledge gaps on non-critical regions; (high) risk outside stated tolerance, or unknown, on a high or critical region.

**Value Potential** (low) the value case is undocumented or speculative; (medium) a credible, stated value case without quantified benefit expectations (D8 value criteria at adequate); (high) documented value expectations and understood economics (D8.4, D8.5 at adequate or above).

**Urgency** (low) no trigger within the planning horizon; (medium) a characterized trigger expected within the horizon, not yet committed; (high) a committed trigger with a fixed date, threshold, or constraint.

**Feasibility** (low) no viable option inside current constraints; (medium) viable options exist with material constraints (changeability results at 2 or below); (high) a viable option at tolerable effort, speed, cost, and risk.

**Readiness** (low) readiness results at 2 or below, or a high-readiness claim without corroboration under the maturity bridge calibration flags; (medium) mixed readiness results; (high) readiness results at 4 or above, corroborated.

**Dependency** (low) the opportunity enables nothing and blocks nothing; (medium) it enables or unblocks one other opportunity; (high) it is an enabler of multiple opportunities, or it resolves a blocking node.

## Prioritization profiles

| Profile | Characterized by |
|---------|------------------|
| Critical Modernization | High need · high importance · material exposure |
| Strategic Modernization | Future demand · strategic value · capability advancement |
| Risk-Driven Modernization | Lifecycle exposure · sustainability · operational risk |
| Opportunity-Driven Modernization | Efficiency · innovation · value enhancement · simplification |

### Assignment conditions (explicit)

Profile assignment is by condition, not by narrative. The conditions, evaluated on the factor levels above:

- **Critical Modernization**: need is high, strategic importance is high, and at least one material or severe exposure finding exists within the opportunity.
- **Strategic Modernization**: future demand is high, value potential is medium or higher, and a defined target position exists (target results at score 3 or above).
- **Risk-Driven Modernization**: exposure is high, need is medium or higher, and the driver is lifecycle, viability, or operational risk rather than demand.
- **Opportunity-Driven Modernization**: value potential is high, feasibility is medium or higher, and no severe exposure finding exists within the opportunity.

Ordering rules for assignment:

1. **Dominance order.** An opportunity may satisfy several conditions. The primary profile is the first satisfied in the order: Critical, then Strategic, then Risk-Driven, then Opportunity-Driven. Criticality of need dominates; efficiency never outranks a critical modernization.
2. **Secondary profiles are recorded, not merged.** Satisfied secondary profiles are listed with the rationale; there is no blended profile and no averaging of conditions.
3. **No forced fit.** An opportunity satisfying no condition is reported as **standby**, with a recorded review date. It is not pushed into a profile to make the set look cohesive.
4. **Conditions are auditable.** Each assigned profile cites the factor levels and, through them, the findings and results that ground the condition.

## Dependency mapping

Opportunities are related explicitly. A dependency edge is recorded when one opportunity changes what another costs, risks, or requires:

| Kind | Semantics |
|------|-----------|
| `enables` | Closing the source opportunity's gap materially reduces the cost, risk, or scope of the target opportunity, or makes it possible at all |
| `blocks` | The target opportunity cannot proceed until the source opportunity is resolved; they alter the same elements or capabilities |

Rules:

- Every edge cites its basis: the finding, result, or shared element that grounds it. An edge without a recorded basis is deleted in review.
- The dependency map must be **acyclic**. A cycle is a sequencing conflict: it is recorded as such and resolved by re-scoping or decomposition, not by ignoring it.
- Dependency feeds sequencing: within a priority band, enablers precede their dependents.
- The Dependency factor level is read off the map (anchors above); the map, not a hunch about "strategic fit", is the single source of the factor.

## Readiness is separate from priority

A modernization opportunity may be highly critical but difficult to execute. Such an opportunity is not deprioritized. It may require:

- Preparatory initiatives.
- Risk mitigation.
- Capability development.
- Staged modernization.

Readiness shapes the **path** (preparation, staging, sequencing), while priority factors establish the **need**.

### The preparatory-initiative pattern

When an opportunity is Critical profile (or of material or severe severity) while readiness or feasibility is low, the following pattern is mandatory:

1. **Record the shortfall.** The readiness or feasibility gap is captured as constraint findings (they already exist in the worked example: F-6).
2. **Define a preparatory initiative.** It carries its own target, scope, and success criterion: capability development, risk mitigation, or baseline cleanup that closes the constraint findings. It is scheduled ahead of, or as the first stage of, the main opportunity.
3. **Stage the opportunity.** The main opportunity is decomposed into increments whose first stage fits current readiness; later stages raise their ambition as readiness results improve.
4. **Set a re-assessment gate.** Readiness and feasibility are re-scored before each subsequent increment commits. The gate result is recorded; a failed gate re-opens staging rather than cancelling priority.

The opportunity keeps its priority and profile; only the path changes. A preparatory initiative is never reported as a substitute for the modernization it prepares.

## The ordered set

Priority is an ordering of opportunities, not a score:

1. **Primary profile first**: Critical before Strategic before Risk-Driven before Opportunity-Driven; standby entries are listed last with review dates.
2. **Severity within profile**: primary opportunities ordered by their highest-severity finding basis (severe, material, moderate, minor).
3. **Dependency within severity**: enablers before dependents, per the acyclic map.
4. **Ties remain ties.** Where the three keys do not separate two opportunities, they are reported as tied, with any further ordering decision made by the assessment owner and recorded as such.

Weighted views may be attached as decision logic on top of the ordering, under the weighting guidance of the [aggregation mechanics](aggregation-mechanics.md): unweighted default, disclosure rule, and no composite scores. Arithmetic ranking positions, letter grades, and numeric "priority scores" are not produced.

Recording follows the [output templates](../realization/output-templates.md).

## Worked example: prioritizing O-1

Continuing from [interpretation logic](interpretation-logic.md): O-1, Integration service standardization, with basis findings F-1 (severe), F-4 (severe), F-2 (severe), F-3 (material), F-5 (material), constraint F-6 (moderate), asset F-7.

Factor levels for O-1, each with basis:

| Factor | Level | Basis |
|--------|-------|-------|
| Strategic importance | High | Criticality overlay high across the subject region; D1 support for ecosystem expansion |
| Modernization need | High | F-1, F-2, F-4 severe; F-3, F-5 material |
| Future demand | High | F-5: committed partner and real-time demand exceeds capacity |
| Exposure | High | F-4: outside stated tolerance on a high-criticality region |
| Value potential | Medium | D8 value expectations credible, economics partially understood |
| Urgency | Medium | Ecosystem expansion trigger characterized, not yet date-committed |
| Feasibility | Medium | F-3 constrains effort; a viable staged option exists |
| Readiness | Low | F-6: delivery capacity limited, chiefly automated testing |
| Dependency | High | O-1 enables O-2 (partner onboarding simplification): shared service contracts and discoverability |

Profile assignment: need high, importance high, material-or-severe exposure finding present (F-4), so **Critical Modernization** is satisfied and, by dominance order, primary (Strategic's conditions are also met: future demand high, target defined via RES-07, recorded as secondary with rationale).

Readiness treatment: low readiness with severe severity triggers the preparatory-initiative pattern: P-1 "Automated integration testing capability" (closes F-6, own target), then staged standardization with a re-assessment gate before each stage commits. O-1 keeps the Critical profile; its path gains P-1 and the gate.

The ordered set excerpt:

```yaml
order:
  - opportunity: O-1
    primary_profile: critical
    severity_basis: severe
    dependencies:
      - { kind: enables, to: O-2, basis: shared service contracts and discoverability }
    path:
      preparatory: [P-1]
      gate: readiness re-scored before each stage commit
  - opportunity: O-2
    primary_profile: strategic
    severity_basis: material
```

O-2's assignment and path follow the same rules; nothing about O-1's difficulty lowered either opportunity's need: readiness moved the path, never the profile.
