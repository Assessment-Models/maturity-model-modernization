# Technology Architecture Pack

Contextualization pack for the technology architecture domain (catalog domain id `technology`). It instantiates the [fan-out model](../fan-out-model.md): common findings are interpreted through this domain's concerns, vocabulary, evidence, and intervention patterns. The common assessment stays the source of truth; this pack adds interpretation, it never re-scores.

## Domain scope

Technology architecture covers infrastructure, platforms, technology stacks, hosting, networks, runtime environments, and engineering tooling. Typical subjects: a platform or runtime estate, an infrastructure segment, a toolchain, shared technology services.

## Domain concern catalog

| Concern | Reads | Evaluates, in technology terms |
|---------|-------|---------------------------------|
| Platform lifecycle position | D3.4, D6.1 | Where platforms sit on their lifecycle and what that drags with it |
| Capacity and performance | D4.2, D4.5 | Whether platforms can carry current and committed load |
| Connectivity fabric | D4.4, D5.2 | The network, transport, and connection layers everything else rides on |
| Tooling sprawl | D5.4 | Proliferation of overlapping tools and runtime variants |
| Environment reality | D3.3, D3.6 | Configured versus documented environments and runbooks |
| Operational exposure | D6.1, D6.3 | Supportability, security posture at platform level, key-person dependencies |
| Technology changeability | D7.1, D7.3 | Practical feasibility of platform moves at tolerable cost and risk |
| Platform economics | D6.4, D8.5 | Whether running costs and modernization economics are understood |

## Vocabulary mapping

| Common term | Technology vocabulary |
|-------------|----------------------|
| Baseline (condition) | Platform and infrastructure condition as running today |
| Fitness | Capacity, performance, and supportability of the technology estate |
| Coupling | Infrastructure and transport dependencies between platforms |
| Fragmentation | Tooling and platform sprawl: overlapping unmanaged variants |
| Drift | Configured versus documented environment (the real config is the one that runs) |
| Exposure | Lifecycle, security, and operational exposure at platform level |
| Readiness | Platform change capacity: skills, environments, rollout mechanics |
| Target state | Target platform and runtime architecture |
| Opportunity | A platform-level move: modernize, consolidate, rehost, retire |

## Evidence sources

- Platform and infrastructure inventories, license and support records
- Monitoring and capacity data, performance baselines
- Configuration records versus live configuration (what actually runs vs what is written)
- Network and connectivity diagrams, observed traffic
- Support and incident records per platform
- Platform and operations engineers

## Intervention patterns

| Pattern | Addresses |
|---------|-----------|
| Platform modernization | Lifecycle and fitness findings: replace or rehost end-of-life platforms |
| Runtime consolidation | Fragmentation findings: fewer runtimes, with purposes written down |
| Connectivity upgrade | Coupling and fitness findings: standardize the connection and transport layer |
| Tooling standardization | Sprawl findings: one supported tool per job, on record |
| Environment standardization | Drift and readiness findings: reproducible environments as the modernization substrate |
| Runbook and observability establishment | Exposure findings: known and watched beats fast and fragile |

## Implication templates

| Finding class | Implication template |
|---------------|----------------------|
| Deficiency | "<Fragmented or aging platform area> shows up as <sprawl, drag, or support risk at platform level>; modernize or consolidate via <pattern>." |
| Exposure | "Technology exposure outside tolerance (<element>) must be reduced before volume or dependency grows: platform risk compounds under load." |
| Demand | "Committed load that current platforms cannot carry (<basis>) is platform work now: upscale or replace, do not patch-and-pray." |
| Constraint | "Where platform change is risky (<basis>), stage it: standardize environments first, then move workloads in dependency order." |
| Strength | "Existing standardization or observability (<basis>) lowers the cost of the platform move; reuse it." |

## Worked implication: the integration example

For [O-1, Integration service standardization](../../examples/integration-architecture.md) with basis finding F-1 (multiple integration mechanisms) and constraint F-6 (absent automated testing), the deficiency template derives:

> **Modernize integration platforms, runtime, connectivity, and tooling.**

Derivation note: several integration mechanisms mean several platforms, runtimes, and toolsets in parallel; the runtime consolidation, connectivity upgrade, and tooling standardization patterns produce the implication. Basis F-1; constraint F-6 shapes the staging (environment and test tooling first).

## Cross-domain overlap

Implications across domains share the opportunity identifier and finding basis, not content. The technology implication for O-1 typically co-occurs with the [information systems](information-systems.md) redundancy implication (fewer mechanisms means fewer platform instances) and the [implementation](implementation.md) automation implication (platform moves land through pipelines). Link record: opportunity O-1, domain `technology`, implication statement above, basis F-1, F-6.
