# AMAF Assessment App

A self-contained, dependency-free interactive assessment instrument for the Architecture Modernization Assessment Framework. Open `index.html` directly in any browser; nothing is installed, no data leaves the browser.

## What it does (v0.1)

- Presents the seed criterion catalog (8 dimensions, 47 starter criteria) embedded from `../criterion-catalog/criteria-catalog.yaml`.
- Captures the full criterion result per the methodology: applicability, score (1-5), criticality, confidence, target, computed gap, evidence, commentary, recommendation.
- Renders a dimension profile (average score, average gap, weak-criterion counts) as the Modernization Assessment Profile preview.
- Persists to browser localStorage; exports assessment instances as JSON or CSV (aligned to `../criterion-catalog/scoring-template.csv`).

## What it deliberately does not do

- It does not compute a composite modernization score; prioritization is profile-based (see `docs/methodology/prioritization.md`).
- It does not collapse condition, criticality, future demand, and changeability into one number.

## Roadmap

Catalog-driven loading from the YAML (via JSON export), multi-subject assessment instances, structured evidence records, richer profile dashboards with criticality overlays, and import are planned in [ROADMAP.md](../../ROADMAP.md) slice S5.
