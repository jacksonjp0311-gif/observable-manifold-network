# CODEX ΔΦ — OMN-SA v0.8.3 CI / Release Boundary Separation

## Purpose

OMN-SA v0.8.3 separates CI smoke validation from local release validation.

The failure pattern discovered during v0.8.1/v0.8.2 was not a Git failure. Commits were landing. The red-X cycle came from asking GitHub Actions to run artifact-emitting validators that write timestamps, evidence counts, run IDs, replay ledgers, dashboards, and latest reports.

## Core Finding

Artifact-emitting validation is a release operation, not a CI smoke operation.

CI must verify committed state without refreshing evidence. Release validation may refresh evidence and then intentionally commit those refreshed artifacts.

## v0.8.3 Law

CI verifies committed state.

Release validation refreshes evidence state.

Do not let CI create release artifacts.

Do not treat generated report drift as a commit failure.

## Boundary

v0.8.3 improves repository operation, CI reliability, and release discipline. It does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.