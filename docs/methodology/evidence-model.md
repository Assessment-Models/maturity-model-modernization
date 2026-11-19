# The Evidence Model: Four Independent Assessment Types

The most important modeling decision in AMAF is that not every criterion is a maturity question. Four different types of assessment evidence must be captured, and they are **not interchangeable**.

## The four assessment types

| Type | Question | Example |
|------|----------|---------|
| 1. Condition | How good, adequate, healthy, effective, or deficient is the current architecture? | Integration architecture is highly fragmented |
| 2. Criticality | How consequential is the architecture or criterion to the organization? | The integration architecture is business-critical |
| 3. Future Demand | How significantly will future needs, requirements, or ambitions differ from current capacity? | Integration must support real-time ecosystem orchestration |
| 4. Changeability | How readily can the architecture be changed, and how difficult is modernization likely to be? | High coupling makes modernization difficult |

## Why independence matters

Because the types are captured separately, meaningful conclusions emerge from their **relationships**:

| Combination | Conclusion |
|-------------|------------|
| Good condition, low future fitness | Healthy today, strategically stranded tomorrow |
| Poor condition, low business criticality | Deficient but immaterial; modernization optional |
| High criticality, poor condition | Urgent modernization |
| High modernization need, low readiness | Transformation risk; needs preparation, not just priority |
| Strong fitness, excessive cost | Economic modernization attractive |

Collapsing these into one number destroys exactly the information modernization decisions need.

## Where the types live in the taxonomy

- **Condition** is the primary type for D3 (Baseline), D4 (Fitness), and D5 (Structure).
- **Criticality** attaches to every criterion as an attribute and is established in D1.5 (Priority & Criticality).
- **Future demand** is established in D1.4 (Future Alignment), D2 (Drivers), and anticipated-condition criteria in D4.
- **Changeability** is established in D7 (Adaptability & Readiness) and is strongly predicted by D5 (Structure).
- **Target** criteria in D8 (Target State & Modernization Value) carry target condition and value expectations.

Evidence confidence and sufficiency rules are being formalized per [ROADMAP.md](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/ROADMAP.md) slice S2.
