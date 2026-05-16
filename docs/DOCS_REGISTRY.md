# Observable Manifold Network Docs Registry

## Purpose

This registry is the canonical documentation shell for Observable Manifold Network.

It tracks:

- theory documents,
- software architecture documents,
- injection records,
- RCC / RCC-N context layers,
- future architecture plans,
- versioned release notes,
- validation and evidence boundaries.

## Current Canonical Stack

| Layer | File | Status | Purpose |
|---|---|---|---|
| Theory | `docs/theory/omn_v1_1_theory_bridge.md` | canonical summary | Preserves OMN v1.1 as theory/runtime bridge. |
| Software Architecture | `docs/software_architecture/omn_sa_v0_1_software_architecture.md` | canonical summary | Defines current OMN-SA v0.1 runtime architecture. |
| Injection | `docs/injections/rcc_nexus_injection.md` | active | Records RCC/RCC-N repository-navigation injection. |
| Context | `docs/context/repository_context_index.json` | active | Machine-readable repository context index. |
| Nexus | `docs/context/rcc_nexus_index.json` | active | RCC-N repository navigation index. |
| Future Architecture | `docs/future_architecture/README.md` | reserved | Stores future architecture proposals and version bridges. |
| Release Notes | `docs/release_notes/README.md` | active | Stores versioned changes and update obligations. |

## Version Update Rule

Every time the repository version evolves, the maintainer must update:

1. `README.md`
2. `README_90_SECONDS.md`
3. `docs/DOCS_REGISTRY.md`
4. `docs/software_architecture/README.md`
5. `docs/theory/README.md`
6. `docs/injections/README.md`
7. `docs/release_notes/README.md`
8. relevant folder mini READMEs
9. RCC-N indexes if paths, claims, validation commands, or architecture layers change

## Non-Claim Boundary

Documentation quality is not code correctness.

Architecture clarity is not empirical validation.

RCC/Nexus navigation is not proof of AI understanding, patch safety, causality, mechanism, biological equivalence, physical manifold identity, or GMN replication.
## Benchmark and Public Release Artifacts

| Layer | File | Status | Purpose |
|---|---|---|---|
| RCC-N Benchmark | `docs/benchmarks/rcc_nexus_echo_benchmark.md` | active | Compares RCC-N repository navigation against a regular README baseline. |
| Benchmark Metrics | `docs/benchmarks/rcc_nexus_echo_benchmark_metrics.csv` | active | Stores benchmark category scores. |
| Public Release Essay | `docs/public_release/ai_orientable_repositories_rcc_n.md` | active | Public explanation of AI-orientable repositories. |
| Echo Chart | `visuals/rcc_nexus/rcc_nexus_echo_chart.svg` | active | Visual comparison chart for RCC-N vs regular README. |

Update rule: if RCC-N checker logic, benchmark categories, NCI scoring, route maps, or public claims change, update these artifacts and the root README registry.
