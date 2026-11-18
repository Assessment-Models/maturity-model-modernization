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
