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
