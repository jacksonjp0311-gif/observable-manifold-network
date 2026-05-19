# CODEX ΔΦ — OMN-SA v0.9.0 Deterministic Run Identity and Execution Modes

## Purpose

v0.9.0 makes OMN-SA runtime execution mode-aware.

v0.8.3 separated CI smoke validation from artifact-emitting release validation. v0.9.0 pushes that boundary into the runtime by adding deterministic run identity and explicit execution modes.

## Added Runtime Controls

- `--run-id <id>`
- `--ci-mode`
- `--release-mode`
- `--no-write-report`
- `--output-dir <path>`

## v0.9.0 Law

No timestamp-driven instability without explicit release mode.

CI mode should be deterministic.

Release mode may emit timestamped evidence.

## Boundary

v0.9.0 improves runtime determinism and operational reproducibility. It does not prove empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
