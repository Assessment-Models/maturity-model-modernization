# Asset classification & registration decision

Status: **accepted** (ROADMAP slice S9). This page is the governance decision
record for the AMAF's identity under the Assessment-Models organisation
taxonomy. It records what was decided, the evidence the decision rests on,
and what each decision makes mandatory. The versioning mechanics live in the
[versioning and change policy](versioning.md); this page decides *who the
AMAF is and where it lives*, not how it changes.

## Context

The organisation taxonomy (CR-AM-11 §8, extended by CR-AM-ORG-RES-000,
carried in the organisation's `.github/GOVERNANCE.md`) classifies
repositories into classes: maturity models (`maturity-model-<domain>`),
assessment models (`assessment-model-<domain>`), assessment tools, reusable
components, and org-governed infrastructure. Classification precedes
restructuring, the repository standard applies only to maturity-model
repositories, and "assets are identified by registration id, not repository
name" ([assessment-registry](https://github.com/Assessment-Models/assessment-registry)
is the identity spine).

This repository is classified and standardized as a **maturity model**
(`standard.yaml`, AM-MODEL-REPOSITORY-STANDARD v1.0.1, conformance level
`structural`; identity `maturity-model-modernization` v1.1.0). The AMAF was
built inside it through roadmap slices S0 to S8 as a criterion catalog, a
machine rule set, a metamodel with JSON Schemas, an instrument, worked
bundles, and a documentation site, versioned independently by its
[catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml)
(currently 0.4.1) rather than by the repository's `VERSION`.

The taxonomy question is therefore explicit: is the AMAF content in this
repository a second asset type inside a maturity-model repository, or does it
become its own independently versioned repository in the organisation? And,
either way, when does it get a registration record in the
[assessment registry](https://github.com/Assessment-Models/assessment-registry),
whose records demand immutable references (a release tag, a 40-character
commit SHA, or a content digest; `main` and `latest` are rejected)?

One fact grounds the decision: the organisation already hosts the legacy
v1-alpha instrument for the same domain,
[`dea-assessment-modernization`](https://github.com/Assessment-Models/dea-assessment-modernization)
(registered, active, deliberately scoring against the frozen v1-alpha
maturity scheme). The AMAF is, in substance, its v2-successor under
development; the taxonomy's migration rule explicitly reserves repository
graduation for the point where a v1-alpha instrument ports to v2-canonical
content, with machine-readable supersession (CR-AR-05) recorded at that
moment.

## Decisions

### D1. The AMAF is a second asset inside this repository

The AMAF remains **a second, independently versioned asset within
`maturity-model-modernization`** for the whole of its incubation. The
repository stays classified as a maturity model; the AMAF does not change
`model.yaml`, `standard.yaml`, `VERSION` or the README status line, and those
governed assets are untouched by framework changes (the existing CI keeps
checking them independently). The two-asset regime is already the
[documented boundary](../realization/maturity-vs-modernization.md): one
repository, two change regimes, one load-bearing distinction between what
the maturity model measures and what the framework measures.

Rationale:

- The AMAF has no release yet; the taxonomy's own lifecycle convention is
  that model repositories are "independently versioned, released, tested,
  documented and governed", and the AMAF does not yet meet the "released"
  part of that bar on its own standing.
- The framework and its site, examples, validator and battery were built
  here; a move now would churn references for no semantic gain, exactly the
  argument the taxonomy uses to forbid unnecessary renames.
- The maturity model is the readiness instrument for AMAF dimension D7;
  co-location keeps that bridge short while the bridge itself is evolving.

### D2. Graduation is a standing option, reviewed at AMAF 1.0

The AMAF graduating to its own taxonomy-named repository
(`assessment-model-architecture-modernization` per the §8 naming rule) is
**deferred, not dismissed**. It is reviewed when the catalog reaches 1.0,
with these criteria:

1. the catalog version has left the 0.x incubation line (semver: public
   commitment to stability);
2. the instrument is stable and the framework battery is green in CI over
   an extended period;
3. ecosystem consumers actually need the registry to resolve the AMAF
   (registration pulls, compatibility declarations, cross-asset
   dependencies).

If graduation happens, the taxonomy's pipeline applies: content moves per
the IDENTIFY to CLASSIFY to EXTRACT to NORMALIZE to VALIDATE to REGISTER to
RELEASE pipeline (CR-AM-11 §27), the new repository uses the taxonomy name,
the registration id `ama-framework` travels with the asset (registry id, not
repository name, is the identity), and
[`dea-assessment-modernization`](https://github.com/Assessment-Models/dea-assessment-modernization)
(the v1-alpha instrument for the same domain) is registered with
machine-readable supersession (CR-AR-05) at that point, not before. Nothing
in the current repository state precommits content to that move.

### D3. Registration deferred until the first AMAF release tag

A registration record for the AMAF is **not added now**. The registry is the
organisation's identity spine and registration is a Level 3 contract: record
metadata plus immutable references (CR-AM-11 §11-12), resolved by the
registry's ecosystem validator on every pull request. Registering an asset
with no release would anchor identity to a moving commit.

The trigger is the first AMAF release tag (see the
[versioning policy](versioning.md): the catalog version is the AMAF version;
an AMAF release is a `## AMAF [x.y.z]` section in the project changelog,
tagged `ama-vX.Y.Z` at the introducing commit by the release tagging
workflow). At that point the record below is submitted to
`Assessment-Models/assessment-registry/registry/assessment-models/`, with the
tag as `release.reference`.

The draft record (informative, kept here so the "when" stays a submission,
not a design exercise):

```yaml
# Registration record for the AMAF, submitted at first AMAF release tag.
# Draft lives in this repository (docs/governance/); submission updates
# release.version / release.reference to the actual tag.
id: ama-framework
asset_class: assessment
type: assessment-model
name: Architecture Modernization Assessment Framework
description: >-
  Architecture-agnostic assessment framework for architecture modernization:
  49 modeled criteria across 8 dimensions and 47 subdimensions, machine
  assessment and interpretation rules, domain contextualization packs, and a
  client-side instrument. Versioned by its criterion catalog.
source:
  organization: Assessment-Models
  repository: maturity-model-modernization
release:
  version: 0.5.0            # placeholder: the released catalog version
  reference: ama-v0.5.0     # placeholder: the ama- release tag
conformsTo:
  contract:
    id: opendea-assessment-contract-suite
    version: "1.0.0"
status: active
dependencies:
  - maturity-model-modernization
notes: >-
  Second asset inside the maturity-model-modernization repository per the
  asset classification decision (docs/governance/asset-classification.md).
  The AMAF bridge scores dimension D7 readiness against the registered
  maturity model. Graduation to a taxonomy-named repository is reviewed at
  AMAF 1.0 with supersession of dea-assessment-modernization (CR-AR-05)
  recorded if it happens.
```

The `dependencies` entry reflects the D7 bridge: the framework's maturity
bridge is a conscious consumption of the registered maturity model, so the
record declares it rather than leaving the relationship implicit. Whether
`maturity-model-modernization` and the other registry records resolve the
`opendea-assessment-contract-suite` id is checked by the registry's own
validator at submission time; the draft follows the shape of the contract
handshake the AMAF metamodel already pins.

### D4. The AMAF gets the same machine-checking discipline

Classification without enforcement is assertion. The AMAF's battery moves
from "runs locally before push" to CI: the workflow
[`framework-ci.yml`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/.github/workflows/framework-ci.yml)
runs on every push and pull request and checks:

1. **Catalog validation** ([`framework/validate_catalog.py`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/validate_catalog.py)):
   catalog schema (16 modeled fields per criterion, types, enums), ID
   stability against the committed baseline
   ([`framework/ids/criteria-baseline.txt`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/ids/criteria-baseline.txt),
   both directions: nothing disappears, nothing appears unregistered, no
   names drift), cross-reference integrity (every `related_criteria` and
   `domain_applicability` entry resolves), and version coherence (the YAML
   source, the JSON export, the app embed, and the rule-set `catalog_version`
   pin all agree, and the `assessment_rules` / `interpretation_rules`
   counters agree between source and export).
2. **Framework model validation** ([`framework/validate.py`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/framework/validate.py)):
   schemas over all three worked bundles and semantic re-derivation of the
   machine rules.
3. **Export synchronization**: the committed exports must be exactly what
   the exporter regenerates (hand edits and drift fail the build).
4. **Instrument self test** ([`tools/assessment-app/selftest.js`](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/assessment-app/selftest.js)).

The baseline file is the deliberate-change mechanism: criterion IDs are
stable, so an ID change must update the baseline in the same change-set, and
the review process reads that edit as the visible record of the identity
change. A validator that cannot fail is not a rule; the battery was
negative-tested (renamed IDs, dangling cross-references, rule-set pin drift,
broken structural edits, rogue status changes) before this page was
committed.

## Scope notes

- This record binds framework work in this repository. It does not amend
  the organisation taxonomy, the repository standard, or the registry's
  rules; those change through their own change requests
  (`CR-AR-01`-style processes in their home repositories).
- Nothing here releases anything: the catalog stays at 0.4.1 until the
  review process decides otherwise, and no registry record exists yet.
- The governed maturity model participates in this record only as a
  neighbor and an eventual dependency declaration; none of its artifacts,
  versions or CI levels are touched.
