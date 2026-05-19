# OMN-SA v0.7 Evidence Drift Metrics

## Summary

- Passed: True
- Evidence packages found: 85
- Evidence packages compared: 8
- Seeds seen: artifact-graph, lorenz, synthetic-toy
- Claim statuses seen: runtime-validated
- Benchmark classes seen: S0, S1, S3
- Artifact count spread: 0
- Load errors: 0
- Overpromotion flag count: 0

## Metric Drift

| Metric | Available | Unavailable | Min | Max | Spread | Status |
|---|---:|---:|---:|---:|---:|---|
| rmse | 0 | 8 | n/a | n/a | n/a | unavailable |
| mae | 0 | 8 | n/a | n/a | n/a | unavailable |
| delta_phi_residual | 0 | 8 | n/a | n/a | n/a | unavailable |
| omega_residual_weight | 0 | 8 | n/a | n/a | n/a | unavailable |

## Compared Records

| Run ID | Seed | Claim status | Benchmark | Artifact count |
|---|---|---|---|---:|
| omn_synthetic_toy_20260519_130551 | synthetic-toy | runtime-validated | S0 | 12 |
| omn_artifact_graph_20260519_130551 | artifact-graph | runtime-validated | S3 | 12 |
| omn_synthetic_toy_20260519_130553 | synthetic-toy | runtime-validated | S0 | 12 |
| omn_lorenz_20260519_130554 | lorenz | runtime-validated | S1 | 12 |
| omn_artifact_graph_20260519_130554 | artifact-graph | runtime-validated | S3 | 12 |
| omn_synthetic_toy_20260519_130554 | synthetic-toy | runtime-validated | S0 | 12 |
| omn_synthetic_toy_20260519_130555 | synthetic-toy | runtime-validated | S0 | 12 |
| omn_artifact_graph_20260519_130555 | artifact-graph | runtime-validated | S3 | 12 |

## Failure Flags

- None

## Boundary

Evidence drift comparison checks run-to-run continuity, artifact replay status, claim-status stability, and metric availability. It does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
