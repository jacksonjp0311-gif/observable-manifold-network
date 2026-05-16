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

## Documentation Lane Separation

| Lane | Path | Rule |
|---|---|---|
| Theory | `docs/theory/` | Stores canonical source-bounded theory summaries and theory bridge records. |
| Software Architecture | `docs/software_architecture/` | Stores current executable software architecture. |
| Architecture Changes | `docs/architecture_changes/` | Stores versioned structure/runtime/docs architecture changes. |
| Injections | `docs/injections/` | Stores governance/module/documentation injections and HYDRA-style records. |
| Injected Theory | `docs/injected_theory/` | Stores source-bounded theory inserted through declared admission. |
| Future Architecture | `docs/future_architecture/` | Stores planned architecture tracks before promotion. |
| Release Notes | `docs/release_notes/` | Stores version continuity and release records. |

Boundary rule: injection records are not architecture docs, architecture changes are not theory, and injected theory is not implementation proof.
## Added Documentation Lanes

| Layer | File | Status | Purpose |
|---|---|---|---|
| Architecture Changes | `docs/architecture_changes/README.md` | active | Separates architecture-change records from injections and theory. |
| Injected Theory | `docs/injected_theory/README.md` | reserved | Separates source-bounded injected theory from architecture and governance injections. |
## OMN-SA v0.2 Engineering Hardening

| Artifact | Path | Status | Purpose |
|---|---|---|---|
| CI Workflow | `.github/workflows/ci.yml` | active | Runs RCC-N checker, unit tests, seed run, and evidence validation on GitHub. |
| Local All Checks | `scripts/run_all_checks.ps1` | active | Runs full local validation surface. |
| Fresh Clone Verify | `scripts/release/fresh_clone_verify.ps1` | active | Verifies remote repo from a clean clone. |
| v0.2 Plan | `docs/future_architecture/omn_sa_v0_2_plan.md` | active | Defines next engineering hardening targets. |
| v0.2 Patch Notes | `docs/release_notes/v0_2_engineering_patch.md` | active | Records this engineering patch seed. |
| Graph Contract Tests | `tests/test_graph_contracts.py` | active | Tests typed edges, baselines, topology sensitivity, and claim gate boundaries. |
| RCC-N Integrity Tests | `tests/test_rcc_nexus_integrity.py` | active | Tests chart embedding, docs lanes, route map, and public-release boundary. |

## OMN-SA v0.2 Software Architecture

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_2_software_architecture.md` | active | CI, modular runtime target, schema validation, and RCC-N drift hardening architecture. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_2_architecture_change.md` | active | Records the v0.1 -> v0.2 architecture transition. |
| Evidence Schema | `schemas/omn/evidence_package.schema.json` | active | Lightweight evidence package contract. |
| Graph Schema | `schemas/omn/graph_contract.schema.json` | active | Lightweight graph contract. |
| Route Map Schema | `schemas/rcc_nexus/route_map.schema.json` | active | Lightweight RCC-N route map contract. |
| RCC-N Index Schema | `schemas/rcc_nexus/rcc_nexus_index.schema.json` | active | Lightweight RCC-N index contract. |
| Architecture Validator | `scripts/validation/validate_architecture_contracts.py` | active | Validates v0.2 architecture contracts. |
| Architecture Test | `tests/test_omn_sa_v0_2_architecture.py` | active | Unit tests for v0.2 architecture contract. |

Boundary: OMN-SA v0.2 is software architecture hardening. It does not update OMN theory, prove code correctness, prove empirical validation, or replicate GMN.
