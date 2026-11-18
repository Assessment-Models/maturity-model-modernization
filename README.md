# Architecture Modernization Assessment

> One modernization assessment foundation. Multiple architectural interpretations. Coordinated realization.

This repository is the home of **architecture modernization assessment** under the Assessment-Models organisation. It carries two coordinated assets:

1. **AMAF, the Architecture Modernization Assessment Framework** (new, scaffold slice). A common, architecture-agnostic framework for assessing architecture modernization: what needs to modernize, why, how significantly, and toward what desired state, then contextualized into the specific architecture domains, capabilities, decisions, and interventions required to realize it.
2. **The Architecture Modernization Maturity Model** (`dea:maturity-modernization`, 1.0.0 stable). The governed maturity model assessing the organisation's *capability to modernise* legacy estates and platforms: strategy, sequencing, execution, and technical-debt reduction.

The two assets are deliberately distinct, and the distinction is load-bearing: AMAF assesses the **modernization need of architectures**; the maturity model assesses the **maturity of the modernization practice**. Under AMAF, maturity is an input, not the organizing principle: practice capability feeds dimension D7 (Adaptability & Modernization Readiness) and shapes the modernization path. See [`docs/realization/maturity-vs-modernization.md`](docs/realization/maturity-vs-modernization.md).

## The problem AMAF solves

Architecture modernization is usually assessed through the lens of a single architecture discipline. An enterprise architect assesses enterprise architecture, a business architect assesses business architecture, a technology team assesses infrastructure, and software teams assess applications. These perspectives are individually valid but collectively fragmented: overlapping needs, different criteria, conflicting priorities, and initiatives that trace to no common modernization objective.

AMAF's central proposition separates **the assessment of modernization** (common, consistent, comparable, evidence-based) from **the architecture of modernization** (domain-specific implications, decisions, capabilities, interventions, realization paths).

## The backbone

```
01 · Common Modernization Assessment
     Drivers · Context · Current State · Gaps · Risks · Value · Readiness · Direction
02 · Architecture Contextualization
     Findings translated into domain-specific concerns, objectives, and target states
03 · Modernization Intervention
     Architecture changes · Capabilities · Decisions · Roadmaps · Programs · Projects
04 · Outcome & Realization
     Modernized architecture · Measurable outcomes · Verified value · Sustained improvement
```

## The eight assessment dimensions

| ID | Dimension | Establishes |
|----|-----------|-------------|
| D1 | Strategic Alignment & Relevance | Why modernization matters and the strategic outcomes it should enable |
| D2 | Drivers & Environmental Context | Internal and external forces creating the need or opportunity to modernize |
| D3 | Architecture Baseline & Condition | The current architecture, its characteristics, condition, and operational reality |
| D4 | Architectural Fitness & Performance | How effectively the architecture fulfills its intended purpose |
| D5 | Structural Integrity & Complexity | Coherence, dependencies, coupling, consistency, and accumulated complexity |
| D6 | Exposure, Risk & Sustainability | Operational, strategic, technical, economic, security, and lifecycle exposure |
| D7 | Adaptability & Modernization Readiness | The ability to change the architecture and the organisation's capacity to do so |
| D8 | Target State & Modernization Value | The desired state, alternatives, expected value, and transformation direction |

## What makes it different

1. **Four independent evidence types, never collapsed into one maturity score.** Condition, criticality, future demand, and changeability are assessed separately.
2. **No composite score as the primary outcome.** Prioritization derives from independent factors and produces prioritization profiles, not a false-precision rank.
3. **Common criteria, domain relationships.** A criterion is a modeled proposition; architecture domains attach to it by relationship, not by encoding the discipline into the criterion.
4. **Assessment outputs are actionable artifacts.** Assessment profiles, findings, opportunities, architecture implication profiles, priorities, and a modernization roadmap, with traceability from criterion to evidence to finding to opportunity to initiative to outcome.

## The maturity model (established asset)

`dea:maturity-modernization` assesses the capability to modernise: five levels (L0..L4) scored against the canonical v2 bands.

| Band id | Name | Range | Width | Effort multiplier | Legacy (v1) name |
|---|---|---|---|---|---|
| `level-1-emergent` | Emergent | 0–20 | 21 | 1.0× | Ad Hoc |
| `level-2-structured` | Structured | 21–45 | 25 | 1.5× | Defined |
| `level-3-systematic` | Systematic | 46–70 | 25 | 2.5× | Managed |
| `level-4-adaptive` | Adaptive | 71–88 | 18 | 4.0× | Quantitatively Managed |
| `level-5-self-optimising` | Self-Optimising | 89–100 | 12 | 6.0× | Optimising |

Level semantics (characteristics, exit criteria, evidence) live in [`maturity/scale.yaml`](maturity/scale.yaml) and are carried verbatim from the authoritative source. Under the revamp, the model is read as the readiness instrument for AMAF's D7.

## Placement

This repository is the independent home of the `dea:maturity-modernization` maturity model. Under the Assessment-Models organisation taxonomy (CR-AM-11 §8, `.github/GOVERNANCE.md`) a maturity model is an independently versioned asset with its own releases, issues, roadmap and contributors. The maturity model for *enterprise architecture practice itself* is owned by the DEA federation (`technehub-labs`), not by this organisation.

## Status

`1.0.0` · stable — canonical v2 bands, independently released

(maturity model version, coherent with `model.yaml`, `standard.yaml` and `VERSION`; see [`CHANGELOG.md`](CHANGELOG.md). The AMAF content is a revamp scaffold: framework catalog v0.1.0, developed per [`ROADMAP.md`](ROADMAP.md).)

## Repository layout

```
maturity-model-modernization/
├── README.md                       # this file
├── MANIFESTO.md                    # the AMAF framework in full prose
├── ROADMAP.md                      # phased plan of work, slice by slice
├── CHANGELOG.md                    # versioned change history
├── CONTRIBUTING.md                 # change control and rules
├── LICENSE                         # MIT
├── model.yaml                      # CR-AM-11 §15 contract handshake (maturity model)
├── standard.yaml                   # repository-standard declaration
├── VERSION
├── mkdocs.yml                      # documentation site configuration
├── docs/                           # AMAF documentation corpus
│   ├── framework/                  # problem, conceptual model, central proposition
│   ├── taxonomy/                  # D1–D8: subdimensions, criteria, signals
│   ├── methodology/               # scales, evidence model, interpretation, prioritization
│   ├── contextualization/         # fan-out to architecture domains, domain packs
│   ├── metamodel/                 # entities, relationships, criterion model
│   ├── realization/               # outputs, maturity vs modernization, model structure
│   └── examples/                   # worked end-to-end examples
├── maturity/                       # the governed maturity model
│   ├── scale.yaml                  # model-owned scale (L0..L4)
│   └── model/modernization.yaml
├── tools/                          # AMAF instrument surface
│   ├── criterion-catalog/         # criterion catalog (YAML) and scoring template
│   ├── interview-guide/           # discovery and evidence-gathering guides
│   └── assessment-app/             # interactive assessment instrument (client-side)
├── framework/                      # AMAF formal model artifacts (scaffold, per ROADMAP S6)
├── examples/                       # worked scoring example (maturity model)
├── scripts/                        # local_validate.py (Level 1 validator)
└── .github/workflows/              # local model CI, contract conformance, docs site
```

## CI levels

1. **Level 1, local model CI** (`local-model-ci.yml`): runs `scripts/local_validate.py`, manifest contract, handshake shape, scale integrity, register-to-scale resolution, worked-example scoring math against the canonical v2 bands.
2. **Level 2, contract conformance** (`contract-conformance.yml`): reuses `Assessment-Models/assessment-ci` to resolve the §15 handshake against the published contract suite at the pinned `dea-metamodel` release.
3. **Level 3, ecosystem CI**: the registration record in `Assessment-Models/assessment-registry` is resolved by the ecosystem validator on every registry pull request.

A documentation-site workflow (`.github/workflows/docs.yml`) publishes the AMAF docs corpus via MkDocs Material.

## Quick start

1. Read the [`MANIFESTO.md`](MANIFESTO.md) for the full AMAF thesis, or [`docs/framework/02-conceptual-model.md`](docs/framework/02-conceptual-model.md) for the short version.
2. Browse the [assessment taxonomy](docs/taxonomy/overview.md) (D1 through D8).
3. Open `tools/assessment-app/index.html` in a browser to try the assessment instrument against a real or hypothetical architecture.
4. For the maturity model: `maturity/scale.yaml`, worked example in `examples/`, validated by `scripts/local_validate.py`.
5. Track what lands next in [`ROADMAP.md`](ROADMAP.md).

## Provenance

`technehub-labs/dea-metamodel` — `assessment-models/maturity/v2-beta/modernization.yaml` (the v2-beta port of the frozen v1-alpha catalog entry). The AMAF is formalized from its founding assessment document; the framework, taxonomy, criterion catalog, methodology, contextualization, metamodel and realization documentation are harvested and elaborated from it, with this repository as their working home.

## Licence

MIT, see [LICENSE](LICENSE).
