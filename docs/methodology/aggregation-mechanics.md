# Aggregation, Gap, and Weighting Mechanics

*The framework rejects composite scores as primary outcomes ([prioritization logic](prioritization.md)); this page fixes what aggregation is allowed, how gaps are computed, and where weighting may appear. The machine-readable form is the `assessment_rules` section of the [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml).*

## The only aggregate: the band profile

Aggregation never produces a number. It produces a **band profile**: the distribution of criterion results over the scale, reported at a subdimension or dimension level.

| Aggregate | Built from |
|-----------|------------|
| Subdimension profile | The criterion results of one subdimension, as counts per scale band and per applicable type partition |
| Dimension profile | The subdimension profiles of one dimension, summed by band |

A profile may carry two descriptive companions:

- the **below-adequacy share**: the proportion of applicable results at score 2 or lower;
- the **median**, labeled as descriptive metadata.

Neither companion may be quoted as the finding, and neither may be arithmetically combined across dimensions.

**Type partitioning.** Profiles partition by assessment type. Results of different types never enter the same aggregate: condition results aggregate with condition results, demand with demand, and so on. Collapsing types in aggregation destroys the same information that [the evidence model](evidence-model.md) forbids collapsing in scoring.

**Provenance rule.** Every aggregate references the criterion result identifiers it draws from. Anonymous totals, unexplained removals of applicable results, and averages without itemization all fail review.

## What is forbidden

- **Cross-dimension composite scores.** No score exists above the dimension level, and none is computed across dimensions.
- **Arithmetic means as findings**, at any level and on any grouping.
- **Averaging across assessment types**, across subjects, or across assessment scopes.
- **Averaging condition with target scores**; current and target results are separate recorded values (see [assessment scales](assessment-scales.md)).
- **Averaging confidence levels**; an aggregate reports its confidence as the minimum confidence among its results, plus the confidence distribution.

## Gap semantics

For each applicable criterion where a target score is set, the gap is the signed integer:

```
gap = target score - current score
```

- **Positive gap: a shortfall.** The target is above the current score; positive gaps need closing and size the opportunity.
- **Zero: no gap.** The subject already sits at its intended level; no action is implied, and none is invented.
- **Negative gap: an overshoot.** The subject sits above its intended level; an overshoot of 2 or more is not headroom to spend. It triggers a deliberate-excess review: the assessor records why the target sits below reality, and target-state criteria (D8) check whether the excess is economic.

Gaps are computed per criterion only. There is no gap arithmetic on aggregates: gap reporting is itself a profile (the distribution of positive, zero, and negative gaps per subdimension and dimension), plus per-criterion gaps in the scoring record. The worked example in [realization outputs](../realization/outputs.md) uses the same convention: score 2, target 4, gap 2.

## Weighting guidance

Weighting is the exception, not the default:

1. **Default: unweighted profiles.** Criterion results and profiles carry no weights.
2. **Criticality is an overlay, never a weight.** Criticality qualifies which results justify attention (the criticality overlay on a profile is the count of high and critical results at or below adequacy). It never multiplies a score.
3. **Weighted views are for prioritization only.** Weighting may appear in prioritization profiles (slice S3) as decision logic on top of profiles, never to manufacture a composite score, and never inside scoring, aggregation, or gap computation.
4. **Disclosure rule.** Any weighted view must state its weights, their rationale, and the unweighted comparison. A weighting that changes the ordering of opportunities relative to the unweighted comparison must be called out explicitly, with the consequence accepted by the assessment owner.
