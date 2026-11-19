# Changelog — maturity-model-modernization

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
