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

## OMN-SA v0.1 Source Anchor Insertion

| Layer | File | Status | Purpose |
|---|---|---|---|
| Source Anchor | `docs/theory/omn_sa_v0_1_source_anchor.md` | active | Preserves original OMN-SA v0.1 software-architecture lineage. |
| Injection Record | `docs/injections/omn_sa_v0_1_theory_insertion.md` | active | Records Anchor -> Inject -> Retract -> Seal for v0.1 source insertion. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_1_theory_insertion_change.md` | active | Documents lineage-preservation architecture change. |
| Release Note | `docs/release_notes/v0_2_1_theory_insertion.md` | active | Records v0.2.1 theory insertion patch. |
| Validation Test | `tests/test_theory_insertion_docs.py` | active | Verifies insertion docs, locks, and registry references. |

Boundary: this insertion preserves lineage. It does not replace OMN-SA v0.2, update OMN theory, validate GMN, or prove runtime correctness.

## OMN-SA v0.3 Modular Runtime

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_3_software_architecture.md` | active | Defines modular runtime wrapper and contract split path. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_3_modular_runtime_change.md` | active | Records v0.3 core runtime architecture evolution. |
| Release Note | `docs/release_notes/v0_3_0_modular_runtime.md` | active | Records v0.3 modular runtime release. |
| Modular Contracts | `src/omn/core/contracts.py` | active | Defines contract helpers and non-claim locks. |
| Claim Gate Module | `src/omn/core/claim_gate.py` | active | Computes bounded claim status from evidence. |
| Artifact Audit Module | `src/omn/core/artifact_audit.py` | active | Audits evidence keys and declared artifact paths. |
| Schema Contract Module | `src/omn/core/schema_contracts.py` | active | Loads lightweight schema contracts. |
| Modular Runtime Wrapper | `src/omn/core/modular_runtime.py` | active | Wraps current runtime and emits modular runtime report. |
| Modular Runtime Validator | `scripts/validation/validate_modular_runtime.py` | active | Validates v0.3 module layer and runtime wrapper. |
| Tests | `tests/test_omn_sa_v0_3_modular_core.py` | active | Tests v0.3 modular core behavior. |

Boundary: v0.3 wraps and validates the current runtime before deeper refactor. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.

## OMN-SA v0.4 Graph Engine

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_4_software_architecture.md` | active | Defines graph engine extraction and evidence-preserving runtime split. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_4_graph_engine_change.md` | active | Records v0.4 graph-engine architecture change. |
| Release Note | `docs/release_notes/v0_4_0_graph_engine.md` | active | Records v0.4 graph-engine release. |
| Observables Module | `src/omn/core/observables.py` | active | Builds and validates observable series. |
| Interactions Module | `src/omn/core/interactions.py` | active | Computes association matrix and typed edges. |
| Graph Engine Module | `src/omn/core/graph_engine.py` | active | Builds modular graph engine state and parity summary. |
| Residuals Module | `src/omn/core/residuals.py` | active | Computes RMSE, MAE, DeltaPhi, and Omega. |
| Evidence IO Module | `src/omn/core/evidence_io.py` | active | Loads and writes evidence/report JSON. |
| Graph Validator | `scripts/validation/validate_graph_engine.py` | active | Validates modular graph engine and parity surface. |
| Tests | `tests/test_omn_sa_v0_4_graph_engine.py` | active | Tests v0.4 graph engine behavior. |

Boundary: v0.4 begins graph-engine extraction. It does not prove causality, mechanism, empirical validation, production readiness, AI understanding, or GMN replication.

## OMN-SA v0.4 Metrics and README Chart

| Layer | File | Status | Purpose |
|---|---|---|---|
| Metrics Snapshot | `docs/benchmarks/omn_sa_v0_4_metrics.md` | active | Records v0.4 validation metrics and boundaries. |
| README Chart | `visuals/omn_sa/omn_sa_v0_4_metrics.svg` | active | Visual summary of v0.4 validation status. |
| README Update | `README.md` | active | Current main README now reflects v0.4 metrics, graph engine, and tag. |

Boundary: these metrics summarize local validation and repository orientation. They do not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.

## OMN-SA v0.5 Topology Ensemble and RCC-N Metrics

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_5_software_architecture.md` | active | Topology ensemble and RCC-N measurement surface. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_5_topology_rcc_metrics_change.md` | active | Records v0.5 measurement architecture change. |
| Release Note | `docs/release_notes/v0_5_0_topology_rcc_metrics.md` | active | Records v0.5 release. |
| Topology Ensemble | `src/omn/core/topology_ensemble.py` | active | Tests graph stability across thresholds. |
| Topology Validator | `scripts/validation/validate_topology_ensemble.py` | active | Emits topology ensemble validation report. |
| Mini README Audit | `scripts/rcc/audit_mini_readmes.py` | active | Creates and audits mini READMEs. |
| RCC-N Metrics | `scripts/rcc/generate_rcc_n_metrics.py` | active | Measures RCC-N effectiveness and chart output. |
| RCC-N Chart | `visuals/rcc_nexus/rcc_n_effectiveness_v0_5.svg` | active | Public visual measurement of RCC-N effectiveness. |
| RCC-N Metrics Report | `docs/benchmarks/rcc_n_effectiveness_metrics_v0_5.md` | active | Human-readable metrics report. |

Boundary: v0.5 measures stability and navigation discipline. It does not prove correctness, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.

## OMN-SA v0.6 Evidence Replay and Run Ledger Integrity

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_6_software_architecture.md` | active | Evidence replay and run ledger integrity layer. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_6_evidence_replay_change.md` | active | Records v0.6 evidence continuity change. |
| Release Note | `docs/release_notes/v0_6_0_evidence_replay.md` | active | Records v0.6 release. |
| Evidence Replay | `src/omn/core/evidence_replay.py` | active | Replays evidence packages and re-audits declared artifacts. |
| Run Ledger | `src/omn/core/run_ledger.py` | active | Appends and verifies hash-chained run records. |
| Run Compare | `src/omn/core/run_compare.py` | active | Compares evidence metrics across runs. |
| Replay Validator | `scripts/validation/validate_evidence_replay.py` | active | Validates replay and ledger integrity. |
| Replay Report | `reports/evidence_replay/latest_evidence_replay_validation.json` | active | Latest replay validation report. |

Boundary: v0.6 verifies artifact continuity and local ledger integrity. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.

## OMN-SA v0.6.1 README Health Snapshot and Charts

| Layer | File | Status | Purpose |
|---|---|---|---|
| Evidence Replay Metrics | `docs/benchmarks/omn_sa_v0_6_evidence_replay_metrics.md` | active | Public benchmark report for v0.6 evidence replay and ledger integrity. |
| Evidence Replay Chart | `visuals/omn_sa/omn_sa_v0_6_evidence_replay_metrics.svg` | active | README chart for evidence replay, ledger integrity, RCC-N, and tests. |
| Lineage Chart | `visuals/omn_sa/omn_sa_lineage_v0_6.svg` | active | Visual evolution path through v0.6.1. |
| Release Note | `docs/release_notes/v0_6_1_readme_health_charts.md` | active | Records the v0.6.1 README/charts alignment patch. |

Boundary: v0.6.1 improves public benchmark visibility and orientation. It does not prove correctness, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.

## OMN-SA v0.7 Evidence Drift Comparison and Multi-Run Stability Dashboard

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_7_software_architecture.md` | active | Evidence drift comparison and multi-run stability dashboard. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_7_evidence_drift_change.md` | active | Records v0.7 evidence drift architecture change. |
| Release Note | `docs/release_notes/v0_7_0_evidence_drift_dashboard.md` | active | Records v0.7 release. |
| Evidence Drift Module | `src/omn/core/evidence_drift.py` | active | Compares evidence packages across runs. |
| Evidence Drift Validator | `scripts/validation/validate_evidence_drift.py` | active | Validates evidence drift report and dashboard output. |
| README Canonicalizer | `scripts/release/canonicalize_readme_v0_7.py` | active | Repairs public README health/registry drift. |
| Benchmark Report | `docs/benchmarks/omn_sa_v0_7_evidence_drift_metrics.md` | active | Human-readable v0.7 drift metrics. |
| Dashboard | `visuals/omn_sa/omn_sa_v0_7_evidence_drift_dashboard.svg` | active | Public v0.7 evidence drift chart. |

Boundary: v0.7 compares evidence packages across runs. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
