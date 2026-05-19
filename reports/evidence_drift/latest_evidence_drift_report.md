# OMN-SA v0.7 Evidence Drift Metrics

## Summary

- Passed: True
- Evidence packages found: 178
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
| rmse | 8 | 0 | 0.251442 | 14.061 | 13.8096 | computed |
| mae | 8 | 0 | 0.200144 | 11.8146 | 11.6145 | computed |
| delta_phi_residual | 8 | 0 | 0.200144 | 11.8146 | 11.6145 | computed |
| omega_residual_weight | 8 | 0 | 0.0780357 | 0.833234 | 0.755198 | computed |

## Compared Records

| Run ID | Seed | Claim status | Benchmark | Artifact count |
|---|---|---|---|---:|
| omn_artifact_graph_20260519_134928 | artifact-graph | runtime-validated | S3 | 12 |
| omn_lorenz_20260519_135044 | lorenz | runtime-validated | S1 | 12 |
| omn_artifact_graph_20260519_135044 | artifact-graph | runtime-validated | S3 | 12 |
| omn_synthetic_toy_20260519_135044 | synthetic-toy | runtime-validated | S0 | 12 |
| omn_synthetic_toy_20260519_135045 | synthetic-toy | runtime-validated | S0 | 12 |
| omn_synthetic_toy_20260519_135046 | synthetic-toy | runtime-validated | S0 | 12 |
| omn_lorenz_20260519_135046 | lorenz | runtime-validated | S1 | 12 |
| omn_artifact_graph_20260519_135046 | artifact-graph | runtime-validated | S3 | 12 |

## Failure Flags

- None

## Boundary

Evidence drift comparison checks run-to-run continuity, artifact replay status, claim-status stability, and metric availability. It does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
