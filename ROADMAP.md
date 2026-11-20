# AMAF Roadmap

The founding AMAF document is strong on framing and intentionally high level in places. This roadmap is the plan of work: what has landed, and the phased slices that drill the high-level framed inputs down into enriched, elaborated, documented repo content.

Each slice states its goal, the drill-down areas (the high-level inputs that need elaboration), its deliverables, and its done-when.

## Slice status

| Slice | Name | Status |
|-------|------|--------|
| S0 | Revamp scaffold | done |
| S1 | Normative taxonomy & criterion catalog | done |
| S2 | Assessment mechanics | done |
| S3 | Interpretation & prioritization logic | done |
| S4 | Architecture domain contextualization packs | done |
| S5 | Assessment instrument v1 | done |
| S6 | Metamodel formalization | done |
| S7 | Validation & worked examples | done |
| S8 | Docs site launch | done |
| S9 | Governance & asset registration | done |

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

## S1 · Normative taxonomy & criterion catalog (done)

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

**Status: complete (catalog v0.2.0).** 49 fully modeled criteria (D4.3 and D6.2 each split into independently assessable pairs), glossary at `docs/framework/glossary.md`, taxonomy docs linking the catalog as their normative source.

## S2 · Assessment mechanics (done)

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

**Status: complete (catalog v0.3.0).** Four mechanics pages under docs/methodology; normative `assessment_rules` (version 1) in the catalog; scale semantics, confidence, sufficiency, aggregation, gap, weighting, and the D7 maturity bridge are rule-complete.

## S3 · Interpretation & prioritization logic (done)

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

**Status: complete (catalog v0.4.0).** `interpretation-logic.md` and `prioritization.md` are normative: finding derivation and severity, opportunity synthesis, nine factor anchors, explicit profile assignment conditions, dependency mapping, and the preparatory-initiative pattern are rule-complete; `interpretation_rules` (version 1) in the catalog; output templates for findings, opportunities, and priorities under `docs/realization/`; a worked example runs from scored criteria to a prioritized set.

## S4 · Architecture domain contextualization packs (done)

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

**Status: complete.** Ten domain packs under `docs/contextualization/domain-packs/` (enterprise, business, information systems, data, technology, systems, service, software, solution, implementation), each with a concern catalog, vocabulary mapping, evidence sources, intervention patterns, implication templates, and a worked implication; the domain-pack index fixes the finding-to-implication derivation rule and the overlap representation; the integration example is re-derived purely from the packs (its re-derivation table maps every implication to its pack and template).

## S5 · Assessment instrument v1 (done)

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

**Status: complete.** Assessment instrument v1 under `tools/assessment-app/`: catalog-driven loading via the machine export `tools/criterion-catalog/criteria-catalog.json` (generated by `export-catalog.py`, with an embedded fallback for offline use), multi-subject instances, structured evidence items with catalog-rule confidence suggestion and extreme-score corroboration caps, band-profile dashboards partitioned by assessment type with criticality overlays (no averages anywhere), finding candidates with suggested severity under the findings floor rule, JSON import/export and CSV export aligned to the scoring template, and local-first persistence; `selftest.js` locks the rules and formats against the catalog and template. The v0.1 average-based summary cards are gone by design.

## S6 · Metamodel formalization (done)

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

**Status: complete.** Metamodel formalized under `framework/`: the manifest (`metamodel/amaf-metamodel.yaml`) declares entity packages, identifier and versioning conventions, lifecycle stages, lineage alignment with the pinned `technehub-labs/dea-metamodel`, contract suite evaluation, and a 30-relationship registry covering all 18 documented relationships with multiplicities and OpenDEA mappings; three interconnected artifacts (framework, instance, realization models, the latter as opportunity, contextualization, and realization packages) plus seven JSON Schema files (draft 2020-12, shared common definitions) constrain every entity; `rules/amaf-rules.yaml` expresses the machine rule set (37 rules with parameters and evaluable expressions) mirroring catalog assessment_rules v1 and interpretation_rules v1; `examples/integration-instance.yaml` represents the docs worked example end to end (criterion to value realization, including a preparatory initiative, staged rollout with a re-assessment gate, observed outcome, and value realization); `validate.py` (stdlib only) validates the example against the schemas and re-derives the rules (gap arithmetic, corroboration, classes, floors, severity, parking, dominance, chain coverage). Contract evaluation: conforms now to the conformance and maturity-scale contracts; the assessment contract is the recommended S7 adoption; benchmark and scoring contracts not applicable; the modernization chain is declared AMAF-owned pending an organisation change request. `docs/metamodel/` and `docs/realization/model-structure.md` now point here.

## S7 · Validation & worked examples (done)

**Drill-down areas**

- Instrument testing against different architecture domains (at least: enterprise, data, software) and organisational contexts.
- End-to-end worked examples: the integration architecture example (in `docs/examples/`) plus at least one more (e.g., customer onboarding, spanning multiple domains).
- Completeness and consistency review: does the taxonomy cover architecture modernization holistically; do the dimensions overlap or leave gaps.
- Calibration with the maturity model: confirm the L0-L4 practice capability scores integrate cleanly as D7 evidence, in both directions.

**Deliverables**: expanded `docs/examples/`, validation notes, catalog revisions.

**Done when**: two independent assessments of the same subject produce comparable profiles, and the framework's coverage argument is documented.

**Status: complete.** The acceptance test was executed as a real inter-rater study: two independent teams assessed the same integration subject (recorded in `framework/examples/integration-instance.yaml` and `framework/examples/integration-reassessment.yaml`); 6 of 7 results agree, the single score-level divergence is preserved with its evidence basis, all finding classes match, and both assessments derive identical opportunity sets and profiles by rule. Two further machine-validated bundles extend the instrument testing: the customer onboarding example (`framework/examples/onboarding-instance.yaml`, a mutual insurer context exercising the sustained deliberate-excess overshoot constraint finding, a standby opportunity, and the maturity bridge in the forward direction) and the reassessment itself (maturity bridge calibration flag, in-record evidence conflict resolution). The consistency review surfaced and fixed four defects in the machine rules and representation: the sustained-overshoot constraint finding is now machine-expressible (catalog v0.4.1, interpretation_rules v2, rule set v2), the minor severity row is reachable, standby opportunities are representable with a profile value and review date, and the stale taxonomy overview version reference was updated. The coverage argument is documented (`docs/validation/coverage-argument.md`), with the empirical record in `docs/validation/validation-notes.md` and the studies in `docs/examples/` (comparability, customer onboarding). All three bundles pass `framework/validate.py`, and the assessment app self-test remains green with five new overshoot probes.

## S8 · Docs site launch (done)

**Drill-down areas**

- MkDocs Material site polish and navigation design.
- GitHub Pages deployment (workflow landed in S0; enable Pages and verify).
- Versioning and change policy: how the framework, catalog, and instrument version independently of the maturity model.
- Review process for framework changes.

**Deliverables**: published site, governance notes.

**Done when**: the site is live and every framework change flows through the documented process.

**Status: complete.** The site is live at https://assessment-models.github.io/maturity-model-modernization/ with GitHub Pages enabled by the repository owner (Source: GitHub Actions) and published from `main` by `.github/workflows/docs.yml` on every docs-touching push. Site polish: a landing page (`docs/index.md`) with the thesis, reading paths, and the machine layer, plus curated navigation (Home, Framework, Taxonomy, Methodology, Contextualization, Metamodel, Realization, Examples, Validation, Governance), theme features (top-of-page return, search highlighting, page edit link), site metadata, and `strict: true` in `mkdocs.yml` so local and CI builds enforce link integrity identically. The governance deliverable is `docs/governance/versioning.md`: the versioned-artifact table (catalog 0.4.1 with independent `assessment_rules`/`interpretation_rules` counters, rule set v2, metamodel 1.0.0, app v1, the untouched governed maturity model), the semver mapping with the two invariants (counters move independently of the patch level; consumers pin consciously and fail loudly on drift), the change review process as practiced since S1 (prose first, machine second, regenerated exports, records that exercise the change, the verification battery with negative tests, cross-reference sync, strict docs build), and the honest scope note that the framework battery runs locally until S9 extends CI. The README now points at the published site; its tree was completed for `docs/validation/` (missed in S7) and the new pages.

## S9 · Governance & asset registration (done)

The AMAF is currently content within this repository, versioned by its catalog (v0.1.0) and changelog notes. Its status under the organisation taxonomy must be decided explicitly.

**Drill-down areas**

- Asset classification per CR-AM-11 §8: is the AMAF a second asset type within this repository, or does it become its own independently versioned repository in the organisation?
- Registration: if and when to add an AMAF registration record to `Assessment-Models/assessment-registry`, with immutable references per the contributing rules.
- CI extension: extend the Level 1 validator (or add a sibling validator) to cover the criterion catalog (schema, ID stability, cross-reference integrity), so the AMAF gets the same machine-checking discipline as the maturity model.
- Version coherence: define which AMAF artifacts participate in version coherence checks, keeping the maturity model's `model.yaml`/`VERSION`/README status line untouched.

**Deliverables**: governance decision record, catalog validator, updated contributing rules if scope changes.

**Done when**: the AMAF's identity, versioning, and CI treatment are explicit and machine-checked to the same standard as the maturity model.

**Status: complete.** The governance decision record (`docs/governance/asset-classification.md`) decides the drill-downs explicitly: the AMAF is a second, independently versioned asset inside this repository (the repository stays a classified maturity model; `model.yaml`, `standard.yaml`, `VERSION`, `maturity/` and the README status line are untouched by framework work); graduation to a taxonomy-named `assessment-model-architecture-modernization` repository is deferred and reviewed at AMAF 1.0, with machine-readable supersession of the legacy v1-alpha instrument (`dea-assessment-modernization`, CR-AR-05) recorded if that happens; and registry registration is deferred until the first AMAF release tag, with a ready-to-submit record draft living in the decision record. The AMAF versioning scheme is formalised (the catalog version is the AMAF version; `## AMAF [x.y.z]` changelog sections tag `ama-vX.Y.Z` via the release tagging workflow, keeping the maturity model's plain `vX.Y.Z` tags separate). CI treatment now matches the maturity model's discipline: `framework/validate_catalog.py` (catalog schema, ID stability against the committed baseline `framework/ids/criteria-baseline.txt`, cross-reference integrity, version coherence, negative-tested), `framework/validate.py`, export synchronization, and the app self test run in `.github/workflows/framework-ci.yml` on every push and pull request, so the framework battery is machine-checked in CI rather than run locally. Contributing rules were updated for the formalised scheme (scope changed, so the "if scope changes" deliverable applied); the governed maturity model assets were left untouched throughout.

## Sequencing rationale

The founding document's own recommendation is honored: formalize the eight dimensions into a complete, normative assessment taxonomy (S1) before defining scoring or maturity progression (S2), establishing the conceptual foundation first and validating that the assessment covers architecture modernization holistically rather than prematurely locking into an assessment instrument.
