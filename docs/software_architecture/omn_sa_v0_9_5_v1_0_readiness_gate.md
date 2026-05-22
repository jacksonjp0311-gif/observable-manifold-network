# CODEX ΔΦ — OMN-SA v0.9.5 v1.0 Readiness Gate

## Purpose

v0.9.5 adds a readiness classifier before the v1.0.0 public runtime checkpoint.

v0.9.4 introduced the machine-readable release manifest. v0.9.5 checks whether the repo is ready to be promoted toward v1.0.

## Added Surfaces

- `scripts/release/check_v1_0_readiness.py`
- `reports/readiness/latest_v1_0_readiness_report.json`
- `reports/readiness/latest_v1_0_readiness_report.md`

## v0.9.5 Law

No v1.0 without a readiness classifier.

## Boundary

The readiness gate checks local release-readiness surfaces. It does not prove empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
