# Output Templates

Recording templates for the three interpretation outputs: findings, opportunities, and priorities. The templates implement the derivation rules of the [interpretation logic](../methodology/interpretation-logic.md) and the [prioritization logic](../methodology/prioritization.md); the machine-readable rules live in the `interpretation_rules` section of the [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml).

The traceability requirement of [assessment outputs](outputs.md) applies to every field: every statement traces back through findings, results, and evidence, and identifiers are stable within an assessment instance. Templates are YAML; any equivalent serialization (JSON, CSV rows) is acceptable as long as fields and semantics are preserved.

## Findings template

One record per assessment finding. `class` and `severity` are derived per the interpretation rules, never free text; `confidence` is the minimum among basis results (never averaged); `severity` is `null` for strength findings.

```yaml
assessment: <assessment instance id>
subject: <subject id>
findings:
  - id: F-1                      # stable within the assessment instance
    class: deficiency            # deficiency | exposure | demand | constraint | strength
    statement: >-                # the interpreted observation, faithful to its basis
      ...
    result_ids: [D5.4.1]         # criterion results this finding draws on
    evidence_ids: [E-3, E-7]     # evidence items behind those results
    confidence: medium           # minimum among basis results
    severity: severe             # minor | moderate | material | severe; null for strengths
    criticality_overlay: high    # of the subject region the finding sits on
    date: 2026-04-01
    interpretation_note: >-      # optional: the reading of the basis, for review
      ...
    status: open                 # open | drawn-into-opportunity | parked
    park_reason: null            # required when status is parked
```

## Opportunities template

One record per synthesized modernization opportunity. Synthesis follows the combination test: a single course of change closing the target gaps together.

```yaml
assessment: <assessment instance id>
opportunities:
  - id: O-1
    theme: Integration service standardization
    statement: >-
      ...
    finding_ids: [F-1, F-2, F-3, F-4, F-5]   # must include every severe/material finding drawn in
    asset_findings: [F-7]                    # strength findings informing design
    constraint_findings: [F-6]               # path constraints, feed the preparatory pattern
    dimensions: [D2, D3, D4, D5, D6, D8]     # dimensions drawn on
    closes_gap_profile:                      # per-criterion targets it intends to close
      - { result: D5.4.1, target: 4 }
    target_position: >-                      # from target-state results (D8)
      ...
    option_set: [...]                        # options considered, including rejected
    significance:                            # nine factors, per the anchors; levels with basis
      strategic_importance: { level: high, basis: [criticality overlay, D1 results] }
      modernization_need: { level: high, basis: [F-1, F-2, F-4] }
      future_demand: { level: high, basis: [F-5] }
      exposure: { level: high, basis: [F-4] }
      value_potential: { level: medium, basis: [D8.4.1, D8.5.1] }
      urgency: { level: medium, basis: [D2.6.1] }
      feasibility: { level: medium, basis: [F-3, option set] }
      readiness: { level: low, basis: [F-6] }
      dependency: { level: high, basis: [dependency map edges] }
    profile:
      primary: critical        # first satisfied in dominance order
      secondary: [strategic]  # also satisfied, with rationale
      rationale: >-
        ...
    status: active            # active | standby | deferred-pending-evidence
    review_date: null         # required for standby
```

## Priorities template

The ordered set, with dependency edges and paths. Ordering follows the ordered-set keys: primary profile, then severity basis, then dependency order; ties remain ties with the owner decision recorded.

```yaml
assessment: <assessment instance id>
order:
  - opportunity: O-1
    primary_profile: critical
    severity_basis: severe                 # highest-severity finding basis
    dependencies:                          # edges where O-1 is the source
      - { kind: enables, to: O-2, basis: shared service contracts }   # enables | blocks
    path:
      preparatory: [P-1]                   # preparatory initiatives ahead or as stage one
      stages: [...]                        # increments; first fits current readiness
      gate: readiness re-scored before each stage commit
    note: >-
      ...
ties:
  - opportunities: [O-3, O-4]              # reported as tied when keys do not separate
    owner_decision: O-3 first, accepted delivery-risk ordering
date: 2026-04-02
```

Preparatory initiatives (the [readiness pattern](../methodology/prioritization.md)) carry their own record wherever initiatives are tracked; in the priorities template it suffices to reference them from `path.preparatory` with the finding they close.

## Filled example

The integration architecture worked example fills all three templates: results and findings in [interpretation logic](../methodology/interpretation-logic.md), factor assignments and the ordered set in [prioritization logic](../methodology/prioritization.md). The example is deliberately small: the templates do not reward verbosity, they reward traceable basis fields.
