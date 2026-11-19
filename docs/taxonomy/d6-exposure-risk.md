# D6 · Exposure, Risk & Sustainability

**Assessment objective**: determine the vulnerabilities, liabilities, risks, and future sustainability implications of maintaining or evolving the architecture.

*Normative source: the fully modeled criteria for this dimension (definitions, assessment questions, applicability rules, evidence requirements, interpretation guidance, and domain applicability) live in the [criterion catalog](https://github.com/Assessment-Models/maturity-model-modernization/blob/main/tools/criterion-catalog/criteria-catalog.yaml).*

## Subdimensions and assessment criteria

| Subdimension | Assessment criteria |
|--------------|---------------------|
| D6.1 Technology & Lifecycle Risk | Obsolescence, end-of-life exposure, vendor dependency, skills scarcity, and support limitations |
| D6.2 Security & Trust | Two independently assessable criteria: D6.2.1 Security exposure (security weaknesses, access control, integrity) and D6.2.2 Privacy and trust exposure (privacy obligations, data protection duties, trustworthiness expectations) |
| D6.3 Operational Risk | Failure exposure, continuity, recoverability, operational dependencies, and service disruption |
| D6.4 Economic Exposure | Cost of ownership, maintenance burden, cost inefficiency, licensing, and investment sustainability |
| D6.5 Compliance & Governance Risk | Regulatory exposure, governance failures, standards deviations, and auditability |
| D6.6 Sustainability | Long-term viability, environmental impact, maintainability, and lifecycle sustainability |

## Modernization signals

- Increasing maintenance cost or technical debt.
- Unacceptable security or compliance exposure.
- Vendor or technology dependency risk.
- Loss of critical skills or support.
- The architecture becoming economically or operationally unsustainable.

## Interpretation notes

D6 establishes the **consequence of not modernizing**. Exposure findings weight both urgency and the risk side of the value equation, and they are the primary input to the risk-driven prioritization profile (see [prioritization](../methodology/prioritization.md)).

Distinguish **inherent exposure** (the architecture would be risky in any context) from **contextual exposure** (the risk arises from this organization's dependency on it). Only contextual exposure interacts with criticality: an inherent risk carried by a business-critical architecture demands a different response than the same risk carried by an immaterial one.

D6.2 is assessed as two criteria because security posture and privacy/trust obligations carry different duties, different evidence, and different remediation paths: D6.2.1 scores the classical security exposure, while D6.2.2 scores exposure against privacy, data protection, and trustworthiness expectations.
