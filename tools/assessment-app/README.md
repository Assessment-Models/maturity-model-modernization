# AMAF Assessment App (v1)

A self-contained, dependency-free interactive assessment instrument for the Architecture Modernization Assessment Framework. Open `index.html` directly in any browser; nothing is installed, no data leaves the browser.

## What it does (v1)

- Loads the normative criterion catalog v0.4.0 (8 dimensions, 49 modeled criteria) from the machine export `../criterion-catalog/criteria-catalog.json`, embedded as a fallback (`catalog.js`) so the app also runs from `file://` and offline.
- Supports multi-subject assessment instances: instance metadata (assessment id, organization, date, scope statement) plus an editable subject list; results are recorded per subject and never mixed across subjects.
- Captures the full criterion result per the methodology: applicability decision (yes / no / deferred; no and deferred clear the score), score (1-5), target, criticality, confidence, auto-computed gap, commentary, recommendation.
- Accepts structured evidence items per result: description, class (direct or indirect), source, date, relation (supports or conflicts).
- Suggests confidence straight from the catalog `assessment_rules` v1: high needs at least two independent items with at least one direct; medium needs one direct item or at least two indirect items from independent sources in agreement; unresolved conflicts cap at low; condition items older than 12 months downgrade one level. The suggestion is shown with reasons and can be applied with one click.
- Enforces extreme-score corroboration: scores of 1 or 5 need at least two items, one direct, from at least two independent sources, else confidence is capped at medium and the result is flagged as not eligible to be the sole basis of a finding.
- Renders dimension profiles as band profiles (counts per scale band, partitioned by assessment type), never averages: below-adequacy share and median are clearly labeled descriptive, minimum confidence is reported with the distribution, and a criticality overlay counts high or critical results at or below adequacy.
- Derives finding candidates per the catalog `interpretation_rules` v1: condition or target results at score 2 or below become deficiency candidates, exposure exposure, demand demand, changeability or readiness constraint, and results at score 4 or above with high confidence become strengths. Candidates below the findings floor (low confidence) are carried as unverified observations, not findings.
- Suggests severity per the catalog rules (severe, material, moderate, minor), overridable; findings record class, severity, statement, and basis results, with basis-level warnings (low confidence basis, uncorroborated extremes, findings without basis).
- Exports a full instance as JSON and imports JSON instances; exports CSV in the exact `../criterion-catalog/scoring-template.csv` format (validated by `selftest.js`).
- Persists per assessment instance to browser localStorage (the v0.1 store under `amaf-v01` is left untouched) and lists saved instances for open and delete.

## What it deliberately does not do

- It does not compute a composite modernization score; aggregation is band profiles only (see `docs/methodology/aggregation-mechanics.md`).
- It does not collapse condition, criticality, future demand, and changeability into one number; profiles are partitioned by assessment type.
- It does not convert maturity model results into criterion scores; readiness results may cite a maturity result as evidence per the maturity bridge rules.

## Files

| File | Role |
|------|------|
| `index.html` | Layout and tab structure |
| `app.css` | Styles |
| `logic.js` | Pure functions: gap, confidence, corroboration, profiles, candidates, severity, CSV/JSON export; no DOM or storage access |
| `ui.js` | DOM wiring, rendering, persistence |
| `catalog.js` | Embedded catalog export (generated; do not edit by hand) |
| `selftest.js` | Node smoke test: `node selftest.js` (exercises rules, formats, and the template header equality) |

## Regenerating the catalog export

After editing `../criterion-catalog/criteria-catalog.yaml`, run:

```
python3 ../criterion-catalog/export-catalog.py
```

This validates catalog invariants, rewrites `../criterion-catalog/criteria-catalog.json`, and refreshes the embedded copy in `catalog.js` in one step.
