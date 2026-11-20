# Tools

The framing and tooling surface of AMAF. Tools implement the methodology documented in `docs/`; where a tool and a doc disagree, the doc wins and the tool gets a fix.

| Tool | Purpose | Status |
|------|---------|--------|
| [criterion-catalog/](criterion-catalog/criteria-catalog.yaml) | The normative criterion catalog: dimensions, subdimensions, criteria as modeled propositions, the assessment mechanics rules (scoring anchors per type, confidence, sufficiency, aggregation, gap, weighting, maturity bridge), and the interpretation rules (finding classes and severity, opportunity synthesis, prioritization factors and profiles, dependency and readiness treatment) | Normative v0.4.1 (49 fully modeled criteria across D1-D8; `assessment_rules` v1, `interpretation_rules` v2) |
| [criteria-catalog.json](criterion-catalog/criteria-catalog.json) | Machine export of the catalog for tools and scripts; regenerated with `export-catalog.py` (stdlib only), which also refreshes the app embed and validates catalog invariants | Derived; do not edit by hand |
| [scoring-template.csv](criterion-catalog/scoring-template.csv) | Assessment result recording format: score, criticality, confidence, target, gap, evidence, commentary | Usable now |
| [interview-guide/](interview-guide/discovery-guide.md) | Discovery and evidence-gathering question bank per dimension | Usable now |
| [assessment-app/](assessment-app/index.html) | Interactive assessment instrument: catalog-driven multi-subject scoring, structured evidence with confidence suggestion, rule-based band profiles and finding candidates, JSON/CSV import and export; self tests via `node selftest.js` | v1 (self-contained, no dependencies) |

## Delivered and next

Slice S5 delivered the assessment instrument v1: catalog-driven loading via the JSON export, multi-subject instances, structured evidence records with confidence suggestion and corroboration caps, band-profile dashboards with criticality overlays, finding candidates with suggested severity, and JSON/CSV import and export aligned to the scoring template. The next intended step is [ROADMAP.md](../ROADMAP.md) slice S6 (metamodel formalization), which tooling will consume as it lands.
