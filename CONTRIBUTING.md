# Contributing to `maturity-model-modernization`

## Change control

Changes go through a pull request with a rationale and a `CHANGELOG.md`
entry. Semver applies:

- **MAJOR** — level or band definition change
- **MINOR** — new dimension or criterion
- **PATCH** — clarifications, corrections, additional evidence examples

## Rules

1. **Do not alter level semantics without a change request.** Characteristics,
   exit criteria and evidence are the model's substantive content; changing
   them changes what the instrument measures.
2. **Band definitions are canonical upstream.** Band widths and effort
   multipliers are owned by `dea:maturity-bands-v2` in
   `technehub-labs/dea-metamodel`. Do not copy or restate them as local
   truth — reference them.
3. **References are immutable.** Every external reference (component, scale,
   dependency) must be a tag `vX.Y.Z`, a 40-character commit SHA, or a
   sha256 digest. `main`, `master` and `latest` are rejected by CI.
4. **Level 1, Level 2 and the repository-standard gate must be green** before
   merge. Level 2 resolves the handshake against the pinned
   `dea-metamodel` release.
5. **Model identity is the registration id.** The `id` in `model.yaml` must
   match the `repo_id` in the model register and the id in
   `Assessment-Models/assessment-registry`. The repository name is a
   location, not an identity.
6. **Version coherence is machine-checked.** `model.yaml`, `VERSION`, the
   README `## Status` line and `standard.yaml` must always agree — the
   repository-standard conformance workflow fails the build on drift.

## Contributing to the AMAF

The Architecture Modernization Assessment Framework (docs corpus, criterion
catalog, methodology, and instrument) evolves under the same discipline, with
its own conventions:

1. Check `ROADMAP.md` for the current slice and its drill-down areas.
2. Criteria are modeled propositions, not questions: definition, intent,
   assessment type, applicability, evidence requirements, interpretation
   guidance, and domain applicability. Criterion IDs are stable and never
   encode architecture disciplines; domain applicability is a relationship.
3. Do not introduce composite modernization scores as primary outputs, and
   do not collapse condition, criticality, future demand, and changeability
   into one measure.
4. Keep the taxonomy docs and the criterion catalog synchronized: they
   describe the same model.
5. The maturity model assets (`model.yaml`, `standard.yaml`, `VERSION`,
   `maturity/`, `examples/`, `scripts/`) are governed by the rules above;
   AMAF work must not disturb their contracts or version coherence.
6. The assessment app is intentionally dependency-free and client-side; keep
   it runnable by opening `index.html` directly.
7. The framework's machine checking runs in CI on every push and pull
   request (`.github/workflows/framework-ci.yml`):
   `framework/validate_catalog.py` (catalog schema, ID stability, cross
   references, version coherence), `framework/validate.py` (schemas and rule
   re-derivation over the worked bundles), the export regeneration (the
   committed JSON export and app embed must match the exporter's output
   byte for byte), and the app self test. A framework change is complete
   only when that workflow is green.

AMAF framework and catalog changes are recorded in `CHANGELOG.md` under
`[Unreleased]` until an AMAF release is cut. The versioning scheme is
formalised (ROADMAP slice S9): the catalog version is the AMAF version; an
AMAF release is a `## AMAF [x.y.z]` changelog section, which the release
tagging workflow tags `ama-vX.Y.Z` (the repository's plain `vX.Y.Z` tags
remain the maturity model's releases). Criterion IDs are machine-checked
against `framework/ids/criteria-baseline.txt`: an ID change updates the
baseline in the same change-set, and that edit is the visible record of the
identity change. Registry registration is deferred until the first AMAF
release tag, per the asset classification decision
(`docs/governance/asset-classification.md`), which also governs when the
framework graduates to its own repository.

## Registering a release

After a release is tagged, add or update the registration record under
`Assessment-Models/assessment-registry/registry/` with the immutable tag
reference. A record must not point at a repository or reference that does
not resolve — the ecosystem validator checks this.

## Licence

By contributing you agree that your contributions are licensed under the MIT
licence of this repository.
