# OMN-SA v0.8 Metric Availability Architecture Change

## Change Type

Evidence schema and validation hardening.

## Purpose

Repair the v0.7 evidence drift weakness where residual metrics were computed but unavailable to the multi-run comparator.

## Repairs

- Runtime evidence now exposes canonical nested metric fields.
- Evidence drift reader supports canonical v0.8 fields and legacy v0.1/v0.7 fields.
- Metric availability validator checks latest evidence packages.
- README receives v0.8 metric availability dashboard.
- Public chart shows metric availability improvement.

## Boundary

This improves metric availability and evidence schema consistency. It does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.