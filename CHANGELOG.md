# Changelog — maturity-model-modernization

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- CR-AM-13 Phase 2: increment the draft touchpoint manifest to v0.1.1 and declare `touchpoints.yaml` through the model's typed manifest path. Preserve the shared `operations-modernization` component boundary and existing peer mapping; practice-area-to-criterion resolution remains an explicit granularity limitation, not a validated criterion-level mirror.

### Changed

- CR-AM-14: define EAV as marginal score-point contributions across canonical v2 bands divided by their respective effort multipliers; EAV is supplementary and does not determine maturity level.
- Update the scoring utility, local validator and both worked examples to use the unrounded aggregate and marginal-band EAV; resolve continuous scores without gaps between integer-labelled bands.


### Changed — BREAKING

- **Scale level renumbering adopted (dea-metamodel #214): `L-0 Not Assessed` + `L-1..L-5`.** Release 2.0.0 — blocked on upstream ratification of dea-metamodel #214; do not merge before the renumbered canonical scale instance is released and CI pins are bumped.
  - Mapping: old L0→new L-1 … old L4→new L-5; new L-0 is the Not Assessed sentinel (0 points, not a capability level, carries no practice anchors).
  - Unchanged: level definitions/names, band instance `dea:maturity-bands-v2` v1.0.0 (ids, ranges, effort multipliers), band ids `level-1-emergent`…`level-5-self-optimising`, criterion content and weights, scoring mechanics.
  - Comparability: historical index values and bands remain valid; only per-criterion level labels shift (+1).
  - Lockstep consuming-side changes: VERSION/model.yaml/standard.yaml declare 2.0.0; scripts/local_validate.py validates the six-level scale with the Not-Assessed first-entry rule and capability-level anchor coverage; criterion-catalog exports regenerated; README/docs/app strings present the aligned numbering.

### Added

- Repository revamp around the Architecture Modernization Assessment
  Framework (AMAF): landing README reworked to present the assessment
  framework and the maturity model as two coordinated assets, with the
  maturity model positioned as the readiness instrument for AMAF dimension
  D7 (Adaptability & Modernization Readiness).
- `MANIFESTO.md`: the AMAF framework in full prose, harvested from the
  founding assessment document.
- `ROADMAP.md`: the phased plan of work (slices S1–S9) to drill the
  high-level framed inputs into enriched, documented repo content:
  normative taxonomy and criterion catalog, assessment mechanics,
  interpretation and prioritization logic, architecture domain
  contextualization packs, assessment instrument v1, metamodel
  formalization, validation, site launch, and governance alignment.
- AMAF documentation corpus under `docs/`: framework (problem, conceptual
  model, central proposition), taxonomy (D1–D8 with subdimensions,
  criteria, and modernization signals), methodology (scales, evidence
  model, interpretation logic, prioritization), contextualization
  (fan-out model, domain-pack scaffold), metamodel (entities,
  relationships, criterion model), realization (outputs, maturity vs
  modernization, model structure and formalization sequence), and the
  integration architecture worked example.
- AMAF tooling surface under `tools/`: criterion catalog seed
  (`criteria-catalog.yaml`, 47 starter criteria plus one fully modeled
  exemplar, D5.2.1), scoring template (`scoring-template.csv`), dimension
  discovery guide, and the interactive assessment app v0.1
  (self-contained, dependency-free).
- `framework/`: scaffold for AMAF formal model artifacts (OpenDEA /
  metamodel), to be populated per ROADMAP slice S6.
- Documentation site configuration (`mkdocs.yml`) and a docs deployment
  workflow (`.github/workflows/docs.yml`, MkDocs Material to GitHub Pages).

### Notes

- The maturity model assets are unchanged by this revamp: `model.yaml`,
  `standard.yaml`, `VERSION`, `maturity/`, `examples/`, `scripts/` and the
  Level 1/Level 2 CI workflows are untouched; version coherence
  (1.0.0 · stable) is preserved.
- The AMAF is versioned independently of the maturity model during its
  build-out (catalog v0.1.0); asset registration per the organisation
  taxonomy is a roadmap decision (ROADMAP slice S9).

### Added (S1: normative criterion catalog)

- Normative criterion catalog v0.2.0 (`tools/criterion-catalog/criteria-catalog.yaml`,
  status: normative): all 49 criteria across D1-D8 fully modeled with definition,
  assessment intent, assessment question, assessment type, applicability rule,
  assessment method, evidence requirements, interpretation guidance, modernization
  relevance, domain applicability, and related criteria.
- Principled criterion splits where a subdimension held two independently assessable
  propositions: D4.3 split into D4.3.1 Service quality attributes and D4.3.2
  Change-supporting quality attributes (changeability); D6.2 split into D6.2.1
  Security exposure and D6.2.2 Privacy and trust exposure.
- `docs/framework/glossary.md`: normalized assessment terminology (subject, scope,
  criterion, proposition, condition, demand, exposure, criticality, readiness,
  changeability, target, finding, evidence, confidence, applicability, baseline,
  drift, gap, target score, opportunity, priority, profile, architecture domain,
  driver, trigger, contextualization), added to the docs site navigation.

### Changed (S1)

- Criterion catalog: `version: 0.2.0`, `status: normative` (was `seed`, v0.1.0);
  every seed criterion proposition preserved verbatim on its stable ID.
- Taxonomy docs (overview + D1-D8) now link the criterion catalog as their
  normative source; D4 and D6 docs document the new criterion splits; the
  overview status states the taxonomy is complete and normative.
- `mkdocs.yml`: corrected the markdown extension `admonition` (was `admonitions`),
  which aborted `mkdocs build --strict` and blocked the GitHub Pages deployment.
- Docs pages: 24 relative links that escaped the docs directory (13 to
  `ROADMAP.md`, 11 to the criterion catalog) replaced with absolute GitHub
  URLs, clearing the `mkdocs build --strict` link warnings that also blocked
  the Pages deployment.
- `mkdocs.yml`: nav entries corrected to docs-dir-relative paths (they carried
  a redundant `docs/` prefix that `mkdocs build --strict` rejects), the true
  blocker behind the never-passing docs deployment.
- `tools/README.md`: criterion-catalog status row updated to normative v0.2.0.

### Added (S2: assessment mechanics)

- Assessment mechanics documentation under `docs/methodology/`, normative and
  added to the docs site navigation:
  - `scoring-mechanics.md`: scale semantics per assessment type (the shared
    1-5 scale read differently for condition, demand, exposure, criticality,
    readiness, changeability, and target criteria), the uniform direction rule,
    the four-step anchoring procedure, and the reproducibility guards.
  - `evidence-mechanics.md`: the evidence item (direct/indirect classes,
    independence rule), rule-based confidence assignment (high/medium/low), the
    currency and conflict rules, and sufficiency rules (minimum to record,
    corroboration for extreme scores 1 and 5, findings floor at medium
    confidence).
  - `aggregation-mechanics.md`: band profiles as the only aggregate
    (subdimension and dimension, partitioned by assessment type), forbidden
    aggregates (cross-dimension composites, arithmetic means, type mixing),
    provenance rule, gap semantics (target minus current; shortfalls,
    no-action zeros, overshoot reviews), and weighting guidance (unweighted
    default, criticality as overlay, disclosure rule).
  - `maturity-bridge.md`: the relationship between the criterion catalog and
    the governed maturity model's L0-L4 practice bands: evidence not scores,
    no conversion, confidence applies, two-direction calibration flags, and
    separation preserved.
- `assessment_rules` (version 1) in the criterion catalog: the machine-readable
  form of all mechanics (scoring anchors per type, confidence assignment and
  downgrade rules, sufficiency thresholds, aggregation and gap rules,
  weighting disclosure, maturity bridge calibration flags).
- Glossary entries: evidence item, band profile, overshoot, practice maturity.

### Changed (S2)

- Criterion catalog version 0.2.0 to 0.3.0 (additive: `assessment_rules`
  section; all 49 criteria and their attributes unchanged verbatim).
- `docs/methodology/assessment-scales.md` and `evidence-model.md`: the
  placeholders stating that scale semantics, confidence, and aggregation were
  "being formalized" now point to the new mechanics pages.
- `tools/README.md`: criterion-catalog status row updated to normative v0.3.0
  with the assessment rules.

### Added (S3: interpretation and prioritization logic)

- Interpretation and prioritization logic expanded to normative status under
  `docs/methodology/`:
  - `interpretation-logic.md`: finding derivation rules (basis and provenance,
    medium-confidence findings floor, five finding classes: deficiency,
    exposure, demand, constraint, strength; corroboration carry-over,
    non-findings, overshoot handling), finding severity semantics (minor,
    moderate, material, severe, derived by rule from score band, gap,
    criticality overlay, and tolerance; never averaged), opportunity
    synthesis rules (combination test, no dimensional convenience, required
    content, strengths inform but never found, no finding parked silently),
    and a worked example from scored criteria through findings to one
    opportunity.
  - `prioritization.md`: qualitative anchors for all nine priority factors
    (each level cites its basis), explicit profile assignment conditions for
    the Critical, Strategic, Risk-Driven, and Opportunity-Driven profiles with
    a dominance order, recorded secondary profiles, standby instead of
    forced fit, dependency mapping (enables/blocks edges with cited basis,
    acyclic map), the mandatory preparatory-initiative pattern for
    critical-but-difficult opportunities, and ordered-set keys (profile,
    severity, dependency; ties remain ties; no composite rank).
  - `docs/realization/output-templates.md`: recording templates (YAML) for
    findings, opportunities, and priorities, with the worked example filling
    all three.
- `interpretation_rules` (version 1) in the criterion catalog: the
  machine-readable form of all interpretation mechanics (finding classes and
  severity derivation, opportunity synthesis, factor levels and profiles,
  assignment and ordering, dependency kinds, preparatory pattern).
- Glossary entries: severity, preparatory initiative, dependency edge.

### Changed (S3)

- Criterion catalog version 0.3.0 to 0.4.0 (additive: `interpretation_rules`
  section; all 49 criteria and their attributes unchanged verbatim).
- `docs/realization/outputs.md`: links to the output templates and the two
  normative methodology pages.
- Docs site navigation: Output Templates entry under Realization.
- `tools/README.md`: criterion-catalog status row updated to normative v0.4.0
  with assessment rules and interpretation rules.

### Added (S4: architecture domain contextualization packs)

- Ten domain packs under `docs/contextualization/domain-packs/`, one per
  architecture domain (enterprise, business, information systems, data,
  technology, systems, service, software, solution, implementation). Each
  pack carries the same structure: domain scope, a concern catalog with the
  dimensions each concern reads, vocabulary mapping of common terms into
  domain vocabulary, domain evidence sources, intervention patterns mapped
  to the finding classes they address, implication templates per finding
  class, a worked implication for the integration example with its basis
  findings, and cross-domain overlap links recorded as relationships.
- The implication derivation rule in the domain-pack index: a finding reaches
  a domain with its class, severity, and basis; the concern catalog positions
  it, the class template produces the statement, and provenance (opportunity,
  domain, basis, template) is preserved. The pack never re-scores.
- Cross-domain overlap representation: implications belong to exactly one
  pack, share the opportunity identifier and their own finding basis, and
  record co-occurrence links rather than duplicating each other's statements.

### Changed (S4)

- `docs/contextualization/domain-packs.md`: scaffold replaced by the pack
  index with the ten packs, the derivation rule, and overlap representation.
- `docs/examples/integration-architecture.md`: the fan-out table now covers
  all ten domains (Systems Architecture row added), and a re-derivation
  section maps every implication to the pack and template that produce it;
  the done-when for the packs (re-derivation purely from the packs) is met.
- `docs/contextualization/fan-out-model.md`: the packs-complete pointer
  updated.
- Docs site navigation: ten pack entries under Contextualization.
- Glossary: domain pack entry.

### Added (S5: assessment instrument v1)

- Assessment instrument v1 under `tools/assessment-app/` (self-contained,
  dependency-free): catalog-driven multi-subject assessment instances with
  structured evidence capture, rule-based confidence suggestion and
  extreme-score corroboration caps, band-profile dashboards partitioned by
  assessment type with criticality overlays, finding candidates with
  suggested severity under the findings floor rule, JSON import/export and
  CSV export aligned to the scoring template, and local-first persistence.
- Machine export of the criterion catalog
  (`tools/criterion-catalog/criteria-catalog.json`) plus
  `export-catalog.py` (stdlib only): validates catalog invariants and
  regenerates the JSON export and the app's embedded copy in one step.
- `tools/assessment-app/selftest.js`: node smoke test locking the rules and
  formats against the catalog and the scoring template (gap semantics,
  confidence assignment, corroboration, band profiles, finding classes and
  severity, CSV header equality, JSON round trip).

### Changed (S5)

- `tools/assessment-app/index.html`: rebuilt from the v0.1 single file into
  the v1 multi-file app; average-based dimension summary cards removed
  (arithmetic means are never findings, per the aggregation rules).
- `tools/README.md`: assessment app row now v1; catalog JSON export and
  exporter documented; trajectory section updated to delivered.
- Root README quick start: points the instrument step at v1 capabilities.
- ROADMAP slice status: S5 done, S6 (metamodel formalization) next.

### Added (S6: metamodel formalization)

- `framework/` populated (ROADMAP S6): metamodel manifest
  (`metamodel/amaf-metamodel.yaml`) with entity packages, identifier and
  versioning conventions, lifecycle stages, lineage alignment with the
  pinned `technehub-labs/dea-metamodel`, contract suite evaluation, and a
  30-relationship registry covering all 18 documented relationships with
  multiplicities and OpenDEA mappings.
- Three interconnected model artifacts: assessment framework model,
  assessment instance model, and modernization realization model (the
  realization side split into opportunity, contextualization, and
  realization packages), all under `framework/metamodel/`.
- Seven JSON Schema files (draft 2020-12, shared common definitions with
  identifier/version/modelReference alignment) under `framework/schemas/`:
  instance, framework, opportunity, contextualization, realization, and
  relationship shapes.
- `framework/rules/amaf-rules.yaml`: the machine rule set v1 (37 rules with
  kind, target, parameters, and evaluable expressions, each tied to its
  normative catalog source), mirroring assessment_rules v1 and
  interpretation_rules v1.
- `framework/examples/integration-instance.yaml`: the docs worked example
  formalized end to end, criterion to value realization, including the
  staged rollout with the P-1 preparatory initiative and the re-assessment
  gate, an observed outcome, and an evidenced value realization.
- `framework/validate.py`: stdlib-only validator; validates the example
  against all package schemas and re-derives the machine rules over it
  (gap arithmetic, corroboration and staleness, finding classes and floors,
  severity derivation, parking, profile dominance ordering, chain
  coverage). Validator behavior is locked by negative tests run during
  development: each rule violation class produces the expected error.

### Changed (S6)

- `docs/metamodel/entities.md` and `docs/metamodel/relationships.md`:
  the S6 "in formalization" notes now point at the landed artifacts in
  `framework/`.
- `docs/realization/model-structure.md`: pointers to the formal artifacts
  (the five substructures now exist as packages, models, and schemas).
- `docs/methodology/interpretation-logic.md` and
  `docs/methodology/prioritization.md`: worked example severity of F-6
  corrected to material (its basis result is score 2 with a positive gap
  of 2 on a below-adequacy result, satisfying the Material row of the
  severity derivation table; the machine rule re-derivation surfaced the
  mismatch), and RES-07 confidence corrected to high (its evidence meets
  the high-confidence assignment criteria, which the strength finding F-7
  requires).
- Root README and ROADMAP slice status: S6 done, S7 (validation and worked
  examples) next; framework README rewritten from scaffold to populated.

### Added (S7: validation and worked examples)

- `framework/examples/onboarding-instance.yaml`: second machine-validated
  worked bundle, a customer onboarding value stream assessed at capability
  level in a mutual insurer context: 10 results, 17 evidence items, 9
  findings, 2 opportunities, 5 domain implications, 3 realization stages.
  Exercises the sustained deliberate-excess overshoot constraint finding
  (RES-08 score 5 against target 3, deliberate-excess review sustained,
  finding F-7 minor), a standby opportunity (O-2, review date required,
  no profile force-fit), and the maturity model bridge in the forward
  direction (current L2 practice result as direct practice evidence for
  D7.4.1).
- `framework/examples/integration-reassessment.yaml`: third bundle, the
  inter-rater comparability study executed for real: an independent team
  B assessment of the integration subject (7 results, 13 evidence, 7
  findings, 2 opportunities) with its own evidence base, an in-record
  evidence conflict resolution, one preserved score-level divergence
  (D3.2.1 score 1 versus 2), the maturity bridge calibration flag
  (readiness 2 against practice L2 with the required subject-specific
  explanation), and opportunity profiles identical to the first
  assessment by rule.
- `docs/examples/customer-onboarding.md`: documentation of the onboarding
  worked example (results, derived findings, critical-primary and standby
  opportunities, seven-domain fan-out with derivation from the domain
  packs, maturity bridge forward direction).
- `docs/examples/inter-rater-comparability.md`: the comparability study:
  result-level, finding-level, and profile comparisons, the single
  divergence localized to its evidence basis, and what the rules force
  versus permit.
- `docs/validation/validation-notes.md`: instrument testing matrix
  (three bundles, 14 criteria, 6 of 7 assessment types, 8 of 10 domain
  packs, full profile space), consistency review findings with
  dispositions, maturity model calibration in both exercised directions,
  negative testing record (nine caught mutations), and verification
  commands.
- `docs/validation/coverage-argument.md`: the completeness coverage
  argument: the derivation from assessment kinds, the decision-to-dimension
  mapping, deliberate overlaps, gaps by design with named owners, and
  domain pack coverage as a mapping property.
- `mkdocs.yml`: navigation for the new example and validation pages.

### Changed (S7)

- `tools/criterion-catalog/criteria-catalog.yaml`: catalog v0.4.1
  (additive): `interpretation_rules` v2 extends the constraint class row to
  the sustained deliberate-excess overshoot (gap of -2 or less with the
  review sustained, against the target rationale), matching the catalog's
  existing findings.overshoot prose, and rewords the minor severity row to
  its canonical reachable case (the sustained-overshoot constraint
  finding); the previous minor row was machine-unreachable. Exported JSON
  and the assessment app embed regenerated; app scoring logic extended
  (findingClass carries the overshoot gap; deliberate-excess constraint
  candidates) with five new self-test probes.
- `framework/rules/amaf-rules.yaml`: rule set v2 against catalog v0.4.1:
  R-FND-4 parameters extended for the overshoot branch, R-SEV-4 rewritten
  against the v0.4.1 normative source.
- `framework/schemas/common.schema.json`: `standby` added to the profile
  name enum; standby opportunities are machine-representable (primary
  profile standby, status standby, review date required, no profile
  condition satisfied).
- `framework/validate.py`: multi-bundle validation (all three example
  bundles, per-bundle coverage reporting), the sustained-overshoot
  constraint-from-overshoot branch, and standby opportunity checks;
  negative-test battery re-run, all nine injected violations caught.
- `docs/methodology/interpretation-logic.md`: synced with interpretation
  rules v2 (constraint class row, minor severity row, catalog version
  pin in the header note).
- `docs/methodology/prioritization.md`: standby now documented as
  machine-representable.
- `docs/taxonomy/overview.md`: stale catalog version reference corrected
  to v0.4.1.
- `docs/examples/integration-architecture.md`: pointer to the machine
  bundle and the follow-on examples and validation pages.
- `framework/README.md`: updated for the three bundles, rule set v2, and
  multi-bundle validation output.
- Root README and ROADMAP slice status: S7 done, S8 (docs site launch)
  next.

### Added (S8: docs site launch)

- `docs/index.md`: site landing page: the AMAF thesis and tagline, the two
  assessment concerns, where-to-start reading paths keyed to intent, the
  machine-checked overview (catalog, rule set, validator, self-testing
  instrument, three worked bundles), a machine-layer diagram, and the slice
  status.
- `docs/governance/versioning.md`: governance notes, the S8 deliverable:
  versioned-artifact table with owners (catalog v0.4.1 with independent
  `assessment_rules` v1 / `interpretation_rules` v2 counters, rule set v2
  pinned to the catalog, metamodel 1.0.0, assessment app v1, docs and
  bundles unversioned or informative, the governed maturity model untouched
  by framework changes); the semver mapping and its two invariants; the
  framework change review process as practiced since S1 (prose first,
  machine second, exports regenerated by the version-locked exporter,
  changes proven by records, verification battery with negative tests,
  cross-reference sync, strict docs build); and the honest CI scope note
  (the framework battery runs locally until S9 extends machine checking).
- `mkdocs.yml`: site polish and navigation design: Home and Governance nav
  sections, `site_url`, `site_author`, `strict: true` (local builds behave
  like the CI strict build), theme features (back-to-top, URL tracking,
  search highlighting and suggestions, page edit link into `docs/` on
  `main`), and a repository social link.

### Changed (S8)

- Root README: published-site link
  (`https://assessment-models.github.io/maturity-model-modernization/`),
  governance pointer, and a completed docs tree, including the `docs/`
  validation pages missed in the S7 tree update.
- ROADMAP slice status: S8 done, S9 (governance and asset registration)
  next; the site live and deploy-verified conditions recorded in the S8
  status paragraph.

### Added (S9: governance & asset registration)

- Governance decision record (`docs/governance/asset-classification.md`):
  the AMAF is formally a second, independently versioned asset inside this
  repository (the repository stays a classified maturity model; the governed
  assets are untouched); graduation to a taxonomy-named
  `assessment-model-architecture-modernization` repository is deferred and
  reviewed at AMAF 1.0, with supersession of the legacy v1-alpha instrument
  (`dea-assessment-modernization`, CR-AR-05) recorded if it happens; and
  registry registration in `Assessment-Models/assessment-registry` is
  deferred until the first AMAF release tag, with a ready-to-submit record
  draft kept in the decision record.
- `framework/validate_catalog.py`: catalog validator, the sibling of the
  maturity model's Level 1 validator: catalog schema (the 16 modeled
  fields per criterion, types, enums, structure, counts), ID stability
  against the committed baseline, cross-reference integrity (every
  `related_criteria` and `domain_applicability` reference resolves), and
  version coherence (YAML source, JSON export, app embed, and rule-set
  `catalog_version` pin agree; rule counters agree between source and
  export). Negative-tested (renamed IDs, rogue records, pin drift,
  dangling references, status edits break it).
- `framework/ids/criteria-baseline.txt`: the machine-checked identity
  baseline for the 8 dimensions, 47 subdimensions, and 49 criteria
  (ids and names), established at catalog version 0.4.1; an ID change
  updates the baseline in the same change-set.
- `.github/workflows/framework-ci.yml`: the AMAF framework battery moves
  from local execution to CI: catalog validation, framework model
  validation over the worked bundles, export synchronization (committed
  exports must match the exporter's regeneration), and the assessment app
  self test, on every push and pull request.

### Changed (S9)

- `release-tagging.yml`: two release namespaces: maturity model sections
  `## [x.y.z]` tag `vX.Y.Z` as before, AMAF sections `## AMAF [x.y.z]` tag
  `ama-vX.Y.Z` (the formalised AMAF versioning scheme: the catalog version
  is the AMAF version). Existing behavior unchanged; extraction logic
  tested against both namespaces.
- `CONTRIBUTING.md`: the AMAF versioning scheme replaces the
  "until formalised" placeholder; new rules for the CI framework battery
  and the ID baseline.
- `docs/governance/versioning.md`: the honest scope note is retired (the
  framework battery now runs in CI) and the versioning-scheme paragraph now
  states the release mechanics and the registration trigger.
- `README.md` and `mkdocs.yml`: tree, CI description, and navigation updated
  for the new artifacts and the governance decision record.

### Added (repository operations)

- `.github/workflows/release-tagging.yml`: idempotent workflow that tags released
  versions (sections `## [x.y.z]` in `CHANGELOG.md`) at the commit that introduced
  each release note, closing the missing v1.1.0 tag.
- Fix in `release-tagging.yml`: the sed pattern extracting released versions from
  `CHANGELOG.md` built an empty character class on GNU sed and matched nothing,
  so the workflow always exited without tagging; extraction now uses grep/tr.
- `docs.yml`: the docs build step surfaces mkdocs error output as check-run
  annotations for remote visibility, and the workflow re-runs when its own
  definition changes.
- `docs.yml`: added `actions/configure-pages@v5` with `enablement: true`, so
  the workflow enables the GitHub Pages site itself instead of failing with a
  404 at deployment time.
- `release-tagging.yml`: pushing a tag at a historical commit whose workflow
  files differ from `main` is refused for the job token (`workflows`
  permission is never granted to `GITHUB_TOKEN`); the tagger now detects this
  rejection, prints the exact manual tagging command, and continues, so the
  workflow stays green for current and future releases. `v1.1.0` still needs a
  manual `git tag v1.1.0 fed38e2 && git push origin v1.1.0` from a local clone.

## [1.1.0] — 2026-11-18

### Added

- Criteria catalog (`maturity/model/criteria.yaml`): the model decomposed into
  15 independently assessable criteria across 4 practice areas (Strategy &
  Direction, Sequencing & Migration Patterns, Execution & Operations,
  Technical Debt & Outcomes, weights 30/30/20/20). Each criterion carries a
  definition, assessment question, evidence expectations, weight, and
  observable level anchors L0-L4 restated from the scale's characteristics,
  expected practices and evidence expectations at criterion granularity.
- Scoring model (`maturity/model/scoring.yaml`): weighted-mean aggregation on
  the native 0-100 criterion scale with per-practice-area sub-scores, a
  `not_applicable` rule with weight renormalisation and a minimum-coverage
  floor, band resolution as a machine-checked mirror of the canonical v2
  bands (`dea:maturity-bands-v2` v1.0.0), and the effort-adjusted value.
- Scoring CLI (`scripts/score_assessment.py`): validates an assessment against
  the catalog and prints per-area results, the aggregate, resolved band and
  scale level, effort multiplier and effort-adjusted value; `--json` output.
- Second worked example (`examples/payments-platform-2026.yaml`, Structured
  entry profile) and `examples/modernization-2026.yaml` rewritten with real
  catalog criterion scores, practice-area profile notes, and the explicit
  weighted-mean arithmetic.

### Changed

- Level 1 validator (`scripts/local_validate.py`) extended: criteria catalog
  checks (identity, uniqueness, fully formed criteria, weight total),
  scoring-model checks (aggregation contract, band mirror equality with the
  canonical constants), validation of every `examples/*.yaml` (criterion
  resolution, weighted-mean math, band and level resolution, effort-adjusted
  value), and register-manifest version coherence.
- Version bumped 1.0.0 to 1.1.0 coherently across `model.yaml`,
  `standard.yaml`, `VERSION`, the README status line and the model register.
  MINOR per the contribution rules: new criteria, additive; no level, band or
  scale semantics changed.

### Notes

- Level semantics in `maturity/scale.yaml` are unchanged (rule 1: no change
  request). Band widths and effort multipliers remain canonical upstream; the
  scoring model's band table is a declared, machine-checked mirror that fails
  CI on drift (rule 2).
- AMAF assets (docs, tools, roadmap slices) are unchanged by this release; the
  only AMAF-side edit is a maturity-model track note (milestone M1) added to
  ROADMAP.md.

## [1.0.0] — 2026-11-13

### Added

- Initial release of the `dea:maturity-modernization` maturity model as an
  independently versioned asset, per the Assessment-Models organisation
  taxonomy (CR-AM-11 §8).
- Model-owned scale conforming to the published `maturity-scale.schema.json`:
  five levels, ordinals 0–4, `ordering: ascending`, linear topology with
  exponential progression, scored against the canonical v2 band instance
  (`dea:maturity-bands-v2` v1.0.0) — non-linear widths 20/25/25/18/12 and
  per-level effort multipliers 1.0 → 6.0.
- CR-AM-11 §15 contract handshake (`model.yaml`) declaring conformance to
  `maturity-scale-contract`, `maturity-model-contract` and
  `conformance-contract` against `technehub-labs/dea-metamodel`.
- Level 1 local model CI and Level 2 contract conformance workflows.
- Worked scoring example demonstrating canonical v2 band resolution and the
  effort-adjusted value.

### Notes

- Level semantics are carried verbatim from the authoritative source; only the
  scoring fields differ between the frozen v1-alpha lineage and the canonical
  v2 scheme.
