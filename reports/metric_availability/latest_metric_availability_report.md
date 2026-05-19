# OMN-SA v0.8 Metric Availability Report

- Passed: True
- Compared evidence packages: 8

## Metric Availability

| Metric | Available | Unavailable | Availability | Status | Min | Max | Spread |
|---|---:|---:|---:|---|---:|---:|---:|
| rmse | 8 | 0 | 1.000 | available | 0.251442 | 14.061 | 13.8096 |
| mae | 8 | 0 | 1.000 | available | 0.200144 | 11.8146 | 11.6145 |
| delta_phi_residual | 8 | 0 | 1.000 | available | 0.200144 | 11.8146 | 11.6145 |
| omega_residual_weight | 8 | 0 | 1.000 | available | 0.0780357 | 0.833234 | 0.755198 |

## Interpretation

v0.8 passes when all required residual fields are available in the compared evidence packages.

## Boundary

Metric availability validation checks whether evidence packages expose residual fields for comparison. It does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
