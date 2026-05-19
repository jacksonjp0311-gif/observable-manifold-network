# OMN-SA v0.7 Evidence Drift Architecture Change

## Change Type

Multi-run evidence comparison and public stability dashboard.

## Added

- `src/omn/core/evidence_drift.py`
- `scripts/validation/validate_evidence_drift.py`
- `scripts/release/canonicalize_readme_v0_7.py`
- `docs/software_architecture/omn_sa_v0_7_software_architecture.md`
- `docs/benchmarks/omn_sa_v0_7_evidence_drift_metrics.md`
- `reports/evidence_drift/latest_evidence_drift_report.json`
- `visuals/omn_sa/omn_sa_v0_7_evidence_drift_dashboard.svg`
- `tests/test_omn_sa_v0_7_evidence_drift.py`

## Boundary

This change compares evidence packages across runs. It does not prove correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.