# Tools

The framing and tooling surface of AMAF. Tools implement the methodology documented in `docs/`; where a tool and a doc disagree, the doc wins and the tool gets a fix.

| Tool | Purpose | Status |
|------|---------|--------|
| [criterion-catalog/](criterion-catalog/criteria-catalog.yaml) | The normative criterion catalog: dimensions, subdimensions, criteria as modeled propositions, and the assessment mechanics rules (scoring anchors per type, confidence, sufficiency, aggregation, gap, weighting, maturity bridge) | Normative v0.3.0 (49 fully modeled criteria across D1-D8; `assessment_rules` v1) |
| [scoring-template.csv](criterion-catalog/scoring-template.csv) | Assessment result recording format: score, criticality, confidence, target, gap, evidence, commentary | Usable now |
| [interview-guide/](interview-guide/discovery-guide.md) | Discovery and evidence-gathering question bank per dimension | Usable now |
| [assessment-app/](assessment-app/index.html) | Interactive assessment instrument: score, capture evidence, view profiles, export | v0.1 (self-contained, no dependencies) |

## Intended trajectory

Per [ROADMAP.md](../ROADMAP.md) slice S5, the instrument grows toward: catalog-driven loading from the YAML criterion catalog, multi-subject assessment instances, structured evidence records, profile dashboards with criticality overlays, and JSON/CSV import/export aligned to the scoring template.
