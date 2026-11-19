# Evidence Mechanics: Confidence and Sufficiency

*The evidence model ([The Evidence Model](evidence-model.md)) defines what is captured; this page fixes how evidence items are counted, how confidence is assigned, and what makes a result defensible. Terminology follows the [glossary](../framework/glossary.md); the machine-readable form of these rules is the `assessment_rules` section of the [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml).*

## The evidence item

The unit of evidence is the **evidence item**: a single, dated, identifiable artifact or testimony. Each carries an identifier, a class, a source, and a mapping to the assessed criterion's evidence requirements.

| Class | What it is | Examples |
|-------|------------|----------|
| Direct | Produced by the subject's operation or its authoritative artifacts | Measured metrics and telemetry, system and code artifacts, dependency and architecture models, operational records, validated architecture documents |
| Indirect | Asserted about the subject by people or derived sources | Interviews, self-reported claims, unvalidated documents, third-party assertions |

**Independence rule.** Two items are independent only if they originate from different people, artifacts, or systems and neither derives from the other. An interview and the document the interviewee cites count once unless the document originates independently. The same artifact quoted twice never counts twice.

## Confidence assignment

Confidence is computed from the evidence items, never asserted from feel. The scale is `low · medium · high` (see [assessment scales](assessment-scales.md)):

| Confidence | Assigned when |
|------------|---------------|
| High | At least two independent evidence items, at least one direct, with no unresolved material conflict, all dated current for the assessed time constraint |
| Medium | At least one direct item, or at least two indirect items from independent sources in agreement |
| Low | Assertion-level evidence only (a single indirect item), or material conflict that was resolved by judgment |

**Currency rule.** An item is current if it is new enough for the subject's change rate and the assessment's time constraint. As a normative default: the newest supporting item older than 12 months for condition criteria, or older than the recorded anticipated-demand window for demand criteria, downgrades confidence by one level.

**Conflict rule.** Material conflict between items must be recorded in the commentary with its resolution. Unresolved material conflict caps confidence at low.

Confidence qualifies the result's trustworthiness; it never adjusts the score. Two assessors with the same items compute the same confidence because the assignment is a rule over the items' classes, independence, recency, and agreement.

## Sufficiency rules

**Rule 0 (applicability first).** Only applicable criteria are scored; non-assessment is a recorded decision per the [glossary](../framework/glossary.md).

**Rule 1 (minimum to record).** A result requires at least one evidence item explicitly mapped to the criterion's evidence requirements. Without it, the criterion is deferred, not scored.

**Rule 2 (independent corroboration for extreme scores).** Scores of 1 and 5 carry the decision weight, so they require corroboration: at least two items from at least two independent sources, at least one direct. An extreme score without corroboration is recorded but its confidence is capped at medium, and it may not be the sole basis of a finding.

**Rule 3 (findings floor).** A finding builds on at least one criterion result at medium confidence or better. Low-confidence results are recorded and marked provisional; they enter interpretation only when corroborated, and never as the sole support of a finding. (Finding derivation itself is slice S3.)

## How score and confidence interact

| Situation | Score | Confidence | Consequence |
|-----------|-------|------------|-------------|
| Two direct items from independent sources agree | The anchored score | High | Can inform findings |
| One direct item | The anchored score | Medium | Can inform findings |
| One indirect item (interview claim) | The anchored score | Low | Provisional; needs corroboration |
| Direct and indirect items materially conflict | The resolvable score, with the conflict recorded | Low | Provisional; resolution documented in commentary |
| Score 5 on a single direct item | The anchored score | Medium | Extreme score uncorroborated; not sole basis of a finding |

## Worked micro-example

For a D5 coupling criterion, an assessor holds: (a) a dependency map from the CMDB, dated two months ago; (b) a change impact analysis report, dated this quarter; (c) an interview asserting "coupling is manageable." The dependency map and impact analysis are direct, independent, current, and in agreement: confidence is high and the score follows the anchors under [scoring mechanics](scoring-mechanics.md). Had only the interview existed, the result would be recorded at low confidence, marked provisional, and excluded as sole support for any finding.
