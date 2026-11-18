# AMAF Roadmap

The founding AMAF document is strong on framing and intentionally high level in places. This roadmap is the plan of work: what has landed, and the phased slices that drill the high-level framed inputs down into enriched, elaborated, documented repo content.

Each slice states its goal, the drill-down areas (the high-level inputs that need elaboration), its deliverables, and its done-when.

## Slice status

| Slice | Name | Status |
|-------|------|--------|
| S0 | Revamp scaffold | done |
| S1 | Normative taxonomy & criterion catalog | next |
| S2 | Assessment mechanics | planned |
| S3 | Interpretation & prioritization logic | planned |
| S4 | Architecture domain contextualization packs | planned |
| S5 | Assessment instrument v1 | planned |
| S6 | Metamodel formalization | planned |
| S7 | Validation & worked examples | planned |
| S8 | Docs site launch | planned |
| S9 | Governance & asset registration | planned |

## Maturity model track

The slices above track the AMAF build-out. The maturity model advances on its
own release track under the change-control rules in CONTRIBUTING.md:

| Milestone | Scope | Status |
|-----------|-------|--------|
| M1 | Full-fledged model (v1.1.0): criteria catalog, scoring model, worked examples, scoring CLI | done |

M1 notes: the model moved from scale-plus-example to a full assessment
instrument. The catalog's `readiness_assessment` criterion and the AMAF's D7
dimension are the integration point: practice maturity feeds AMAF readiness
evidence in both directions (slice S7 calibrates this).

## S0 · Revamp scaffold (done)

Landing README (assessment framework + maturity model as coordinated assets), manifesto, full docs corpus (framework, taxonomy, methodology, contextualization, metamodel, realization, examples), starter tools (criterion catalog seed, scoring template, discovery guide, interactive assessment app v0.1), docs site configuration, roadmap. The maturity model assets, contracts, and CI levels are unchanged.

## S1 · Normative taxonomy & criterion catalog (next)

The eight dimensions currently carry subdimensions, criteria names, and modernization signals. To become normative, every criterion must be modeled as a full proposition.

**Drill-down areas**

- Full criterion propositions for all subdimensions: definition, assessment intent, assessment question, assessment type (condition, demand, exposure, readiness, target), interpretation guidance, modernization relevance.
- Applicability rules: under what scope conditions each criterion is assessed or skipped.
- Evidence requirements per criterion: expected artifacts, metrics, records, and interview sources, and what counts as sufficient evidence.
- Domain applicability relationships per criterion (which of the domains each criterion commonly applies to).
- Terminology normalization: a glossary so terms like condition, fitness, capability, and intervention mean one thing across dimensions.
- Splitting of seed criteria where a subdimension contains more than one independently assessable proposition (target: 45-60 fully modeled criteria).

**Deliverables**: `tools/criterion-catalog/criteria-catalog.yaml` complete for D1-D8; glossary in `docs/framework/`.

**Done when**: every criterion in the catalog carries definition, intent, type, applicability, evidence requirements, interpretation guidance, and domain applicability, and the taxonomy docs link to the catalog as their normative source.

## S2 · Assessment mechanics

Scales and attributes are defined; the mechanics of using them are not yet fully specified.

**Drill-down areas**

- Scale semantics per assessment type: how the 1-5 scale reads differently for condition vs future demand vs readiness vs target criteria.
- Evidence confidence model: levels, how confidence is assigned, minimum confidence before a result informs a finding.
- Evidence sufficiency rules: how many and what kinds of evidence constitute a defensible result.
- Aggregation rules: what may be aggregated (subdimension to dimension profiles) and what must not be (cross-dimension composite scores), plus gap semantics between current and target scores.
- Weighting guidance: when weighting is appropriate and how criticality interacts with weights.
- Relationship to the maturity model's canonical v2 band scheme: where the 1-5 criterion scale and the L0-L4 practice levels meet (D7), without collapsing one into the other.

**Deliverables**: `docs/methodology/` mechanics pages, machine-readable rules in the catalog (`assessment_rules` section).

**Done when**: two assessors with the same evidence would produce the same scores and confidence, by documented rule.

## S3 · Interpretation & prioritization logic

The flow from results to findings to opportunities to priorities is framed conceptually; the derivation rules need elaboration.

**Drill-down areas**

- Finding derivation rules: which result and evidence combinations constitute a finding, and finding severity semantics.
- Opportunity synthesis: how multiple findings combine into one modernization opportunity, and how opportunity significance is characterized.
- Priority factor definitions: qualitative anchors for the nine factors (strategic importance, need, future demand, exposure, value potential, urgency, feasibility, readiness, dependency) so profiles are assigned consistently.
- Prioritization profile logic: explicit conditions for critical, strategic, risk-driven, and opportunity-driven profiles.
- Dependency mapping: representing enabler/blocker relationships between opportunities.
- Readiness treatment: the preparatory-initiative pattern for critical-but-hard opportunities.

**Deliverables**: `docs/methodology/interpretation-logic.md` and `docs/methodology/prioritization.md` expanded to normative status; output templates for findings, opportunities, and priorities.

**Done when**: an assessment can move from scored criteria to a prioritized opportunity set by documented rule, with a worked example.

## S4 · Architecture domain contextualization packs

Each of the ten-plus architecture domains currently has a contextualization focus row. Each needs a full pack.

**Drill-down areas**

- Domain concern catalogs: the specific concerns each domain evaluates when interpreting a common finding.
- Vocabulary mapping: how common terms (condition, fitness, coupling, exposure) translate into domain vocabulary.
- Domain evidence sources: where each domain's evidence typically lives.
- Intervention patterns: the characteristic modernization interventions each domain contributes.
- Worked implication templates: how a generic finding becomes a domain-specific implication statement.
- Cross-domain overlap representation: how one opportunity spanning several domains is linked, not duplicated.

**Deliverables**: `docs/contextualization/domain-packs/<domain>.md` for enterprise, business, information systems, data, technology, systems, service, software, solution, and implementation architecture.

**Done when**: the integration example can be re-derived purely from the domain packs.

## S5 · Assessment instrument v1

The interactive app exists as a self-contained v0.1 with an embedded seed catalog.

**Drill-down areas**

- Catalog-driven loading: read the criterion catalog (via JSON export) instead of embedded data.
- Multi-subject assessments: score multiple architectures in one assessment instance.
- Evidence capture: structured evidence records per result, with confidence.
- Profile dashboards: dimension profiles, gap views, and criticality overlays.
- Export: JSON and CSV export aligned to the scoring template; optional findings capture.
- Persistence and portability: local-first storage with import/export of assessment instances.

**Deliverables**: `tools/assessment-app/` v1.

**Done when**: an end-to-end assessment (define scope, score, capture evidence, derive profile, export) completes in the tool without manual format wrangling.

## S6 · Metamodel formalization

Entity and relationship lists exist; the formal model needs artifacts.

**Drill-down areas**

- Entity schemas: attributes, identifiers, and lifecycle for every entity in `docs/metamodel/entities.md`.
- Relationship cardinalities formalized (the 18 documented relationships).
- Criterion ID conventions and versioning of the framework and catalog.
- Model artifacts suitable for modeling in OpenDEA, aligned with the organisation's metamodel lineage (`technehub-labs/dea-metamodel`): the assessment framework model, assessment instance model, and modernization realization model as distinct but interconnected artifacts.
- Assessment rule representation: how applicability, aggregation, and interpretation rules are expressed in the model, not in prose only.
- Contract evaluation: which (if any) existing or new contracts the AMAF assets should conform to, per the organisation's contract suite.

**Deliverables**: `framework/` populated with model artifacts and schemas.

**Done when**: an assessment instance can be represented end-to-end (criterion to value realization) in the model without free-text workarounds.

## S7 · Validation & worked examples

**Drill-down areas**

- Instrument testing against different architecture domains (at least: enterprise, data, software) and organisational contexts.
- End-to-end worked examples: the integration architecture example (in `docs/examples/`) plus at least one more (e.g., customer onboarding, spanning multiple domains).
- Completeness and consistency review: does the taxonomy cover architecture modernization holistically; do the dimensions overlap or leave gaps.
- Calibration with the maturity model: confirm the L0-L4 practice capability scores integrate cleanly as D7 evidence, in both directions.

**Deliverables**: expanded `docs/examples/`, validation notes, catalog revisions.

**Done when**: two independent assessments of the same subject produce comparable profiles, and the framework's coverage argument is documented.

## S8 · Docs site launch

**Drill-down areas**

- MkDocs Material site polish and navigation design.
- GitHub Pages deployment (workflow landed in S0; enable Pages and verify).
- Versioning and change policy: how the framework, catalog, and instrument version independently of the maturity model.
- Review process for framework changes.

**Deliverables**: published site, governance notes.

**Done when**: the site is live and every framework change flows through the documented process.

## S9 · Governance & asset registration

The AMAF is currently content within this repository, versioned by its catalog (v0.1.0) and changelog notes. Its status under the organisation taxonomy must be decided explicitly.

**Drill-down areas**

- Asset classification per CR-AM-11 §8: is the AMAF a second asset type within this repository, or does it become its own independently versioned repository in the organisation?
- Registration: if and when to add an AMAF registration record to `Assessment-Models/assessment-registry`, with immutable references per the contributing rules.
- CI extension: extend the Level 1 validator (or add a sibling validator) to cover the criterion catalog (schema, ID stability, cross-reference integrity), so the AMAF gets the same machine-checking discipline as the maturity model.
- Version coherence: define which AMAF artifacts participate in version coherence checks, keeping the maturity model's `model.yaml`/`VERSION`/README status line untouched.

**Deliverables**: governance decision record, catalog validator, updated contributing rules if scope changes.

**Done when**: the AMAF's identity, versioning, and CI treatment are explicit and machine-checked to the same standard as the maturity model.

## Sequencing rationale

The founding document's own recommendation is honored: formalize the eight dimensions into a complete, normative assessment taxonomy (S1) before defining scoring or maturity progression (S2), establishing the conceptual foundation first and validating that the assessment covers architecture modernization holistically rather than prematurely locking into an assessment instrument.
