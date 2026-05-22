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

## OMN-SA v0.7.1 RCC-N v1.7 Adoption Profile Injection

| Layer | File | Status | Purpose |
|---|---|---|---|
| Injected Theory | `docs/injected_theory/rcc_n_v1_7_adoption_profiles.md` | active | RCC-N v1.7 adoption-profile and utility-evidence theory record. |
| Injection Record | `docs/injections/rcc_n_v1_7_injection_record.md` | active | HYDRA-style injection record for RCC-N v1.7. |
| Software Architecture | `docs/software_architecture/omn_sa_v0_7_1_rcc_n_v1_7_profile_injection.md` | active | OMN-SA v0.7.1 profile injection architecture. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_7_1_rcc_n_profile_injection_change.md` | active | Records v0.7.1 governance profile injection. |
| Release Note | `docs/release_notes/v0_7_1_rcc_n_v1_7_profile_injection.md` | active | Records the v0.7.1 release. |
| Profile Config | `docs/context/rcc_nexus_profile_v1_7.json` | active | Machine-readable RCC-N v1.7 profile declaration. |
| Profile Checker | `scripts/rcc/check_rcc_nexus_v1_7_profile.py` | active | Validates adoption profile, minimal viable RCC-N, utility locks, and GEN boundary. |
| Profile Report | `reports/rcc_nexus/latest_rcc_nexus_v1_7_profile_check.json` | active | Latest RCC-N v1.7 profile check report. |
| Profile Chart | `visuals/omn_sa/omn_sa_v0_7_1_rcc_n_v1_7_profile.svg` | active | Public profile governance chart. |
| Benchmark Report | `docs/benchmarks/omn_sa_v0_7_1_rcc_n_v1_7_profile_metrics.md` | active | Public profile metrics report. |

Boundary: v0.7.1 adds profile-aware governance. It does not prove correctness, empirical validation, causality, mechanism, AI understanding, production readiness, GMN replication, or full GEN v1.0.

## OMN-SA v0.7.3 README v0.7 Lineage Completion

| Layer | File | Status | Purpose |
|---|---|---|---|
| Architecture Change | `docs/architecture_changes/omn_sa_v0_7_3_readme_lineage_completion_change.md` | active | Records README lineage completion patch. |
| Release Note | `docs/release_notes/v0_7_3_readme_lineage_completion.md` | active | Records v0.7.3 checkpoint. |
| Lineage Audit Script | `scripts/release/audit_readme_v0_7_lineage.py` | active | Validates archived v0.7 bottom section and README typo repair. |
| Lineage Audit Report | `reports/self_organization/latest_readme_v0_7_lineage_audit.md` | active | Human-readable audit report. |

Boundary: v0.7.3 repairs README lineage continuity. It does not change runtime behavior or prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.

## OMN-SA v0.8 Metric Availability and Residual Field Hardening

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_8_metric_availability_residual_hardening.md` | active | Canonical v0.8 metric availability architecture. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_8_metric_availability_change.md` | active | Records v0.8 schema and residual hardening. |
| Release Note | `docs/release_notes/v0_8_0_metric_availability_residual_hardening.md` | active | Records v0.8 release. |
| Runtime Patch | `src/omn/core/runtime.py` | active | Emits canonical metrics.validation and metrics.baseline blocks. |
| Drift Patch | `src/omn/core/evidence_drift.py` | active | Reads v0.8 canonical metrics with legacy fallback. |
| Validator | `scripts/validation/validate_metric_availability.py` | active | Checks residual metric availability across latest evidence packages. |
| README Audit | `scripts/release/audit_readme_v0_8_metric_availability.py` | active | Validates public README v0.8 metric availability surface. |
| Benchmark Report | `docs/benchmarks/omn_sa_v0_8_metric_availability_metrics.md` | active | Public metric availability benchmark. |
| Chart | `visuals/omn_sa/omn_sa_v0_8_metric_availability.svg` | active | Public v0.8 metric availability chart. |
| Tests | `tests/test_omn_sa_v0_8_metric_availability.py` | active | Validates runtime evidence schema and metric availability. |

Boundary: v0.8 makes residual metrics available for comparison. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.

## OMN-SA v0.8.1 Validation Compatibility and Lineage Audit Repair

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_8_1_validation_compatibility_repair.md` | active | Repairs v0.8 validation compatibility and lineage audits. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_8_1_validation_compatibility_repair_change.md` | active | Records post-v0.8 validation repair. |
| Release Note | `docs/release_notes/v0_8_1_validation_compatibility_repair.md` | active | Records v0.8.1 checkpoint. |
| README Self-Organization Audit | `scripts/release/audit_readme_self_organization.py` | active | Version-aware self-organization audit. |
| v0.7 Lineage Audit | `scripts/release/audit_readme_v0_7_lineage.py` | active | Historical lineage audit decoupled from old current test count. |
| Runtime Test | `tests/test_runtime.py` | active | Accepts v0.8 evidence schema and checks canonical metrics. |

Boundary: v0.8.1 repairs validation compatibility. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.

## OMN-SA v0.8.2 README Lineage and AI Update Policy

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_8_2_readme_lineage_policy.md` | active | Defines README lineage and AI update-policy repair. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_8_2_readme_lineage_policy_change.md` | active | Records README lineage-policy repair. |
| Release Note | `docs/release_notes/v0_8_2_readme_lineage_policy.md` | active | Records v0.8.2 checkpoint. |
| Audit Script | `scripts/release/audit_readme_lineage_policy.py` | active | Validates README current-state, registry-state, AI policy, and bottom lineage. |
| Audit Report | `reports/readme_policy/latest_readme_lineage_policy_audit.md` | active | Human-readable v0.8.2 README lineage-policy audit. |
| Tests | `tests/test_omn_sa_v0_8_2_readme_lineage_policy.py` | active | Verifies AI policy and v0.8/v0.8.1/v0.8.2 bottom lineage sections. |

Boundary: v0.8.2 improves README maintenance and AI orientation. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.

## OMN-SA v0.8.3 CI / Release Boundary Separation

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_8_3_ci_release_boundary_separation.md` | active | Defines CI / release mode separation. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_8_3_ci_release_boundary_change.md` | active | Records operational architecture repair. |
| Release Note | `docs/release_notes/v0_8_3_ci_release_boundary.md` | active | Records the v0.8.3 checkpoint. |
| Local Release Script | `scripts/release/run_release_validation.ps1` | active | Runs full artifact-emitting release validation locally. |
| Test | `tests/test_omn_sa_v0_8_3_ci_release_boundary.py` | active | Verifies CI smoke gate stays non-mutating. |

Boundary: v0.8.3 improves operational release discipline and CI reliability. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.



## OMN-SA v0.9.0 Deterministic Run Identity and Execution Modes

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_9_0_deterministic_run_identity.md` | active | Defines deterministic run identity and execution modes. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_9_0_deterministic_run_identity_change.md` | active | Records runtime determinism hardening. |
| Release Note | `docs/release_notes/v0_9_0_deterministic_run_identity.md` | active | Records the v0.9.0 checkpoint. |
| Test | `tests/test_omn_sa_v0_9_0_deterministic_modes.py` | active | Verifies fixed run IDs and execution-mode metadata. |

Boundary: v0.9.0 improves deterministic execution and release discipline. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.



## OMN-SA v0.9.1 Stable Evidence Index and Latest Pointer System

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_9_1_stable_evidence_index.md` | active | Defines stable evidence index and latest pointer surfaces. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_9_1_stable_evidence_index_change.md` | active | Records evidence-selection hardening. |
| Release Note | `docs/release_notes/v0_9_1_stable_evidence_index.md` | active | Records the v0.9.1 checkpoint. |
| Test | `tests/test_omn_sa_v0_9_1_stable_evidence_index.py` | active | Verifies evidence index and latest CI fixture pointer. |

Boundary: v0.9.1 improves evidence selection and reproducibility discipline. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.



## OMN-SA v0.9.2 Public Metrics Dashboard Hardening

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_9_2_public_metrics_dashboard.md` | active | Defines public metrics dashboard hardening. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_9_2_public_metrics_dashboard_change.md` | active | Records public metric-surface hardening. |
| Release Note | `docs/release_notes/v0_9_2_public_metrics_dashboard.md` | active | Records the v0.9.2 checkpoint. |
| Dashboard | `docs/benchmarks/current_public_metrics.md` | active | Current public benchmark surface. |
| Chart | `visuals/omn_sa/current_public_metrics.svg` | active | README-visible metrics chart. |
| Test | `tests/test_omn_sa_v0_9_2_public_metrics_dashboard.py` | active | Verifies dashboard/chart presence and boundaries. |

Boundary: v0.9.2 improves public interpretability and benchmark visibility. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.



## OMN-SA v0.9.3 README / Registry Autopatcher

| Layer | File | Status | Purpose |
|---|---|---|---|
| Software Architecture | `docs/software_architecture/omn_sa_v0_9_3_readme_registry_autopatcher.md` | active | Defines README / registry autopatcher discipline. |
| Architecture Change | `docs/architecture_changes/omn_sa_v0_9_3_readme_registry_autopatcher_change.md` | active | Records version-surface hardening. |
| Release Note | `docs/release_notes/v0_9_3_readme_registry_autopatcher.md` | active | Records the v0.9.3 checkpoint. |
| Version Surface Checker | `scripts/release/update_version_surfaces.py` | active | Checks README, CI, and DOCS_REGISTRY alignment. |
| Test | `tests/test_omn_sa_v0_9_3_readme_registry_autopatcher.py` | active | Verifies checker presence and current surface alignment. |

Boundary: v0.9.3 improves release hygiene and repository orientation. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
