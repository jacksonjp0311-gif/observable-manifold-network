# OMN-SA v0.9.0 Architecture Change — Deterministic Run Identity

## Change Type

Runtime determinism and execution-mode hardening.

## What Changed

- Added explicit run identity.
- Added CI mode.
- Added release mode.
- Added output directory routing.
- Added report/ledger suppression control.
- Added execution-mode metadata to state and evidence packages.

## Why

The repo learned that CI/release separation must exist not only in GitHub Actions but also inside runtime artifact generation.

## Boundary

This architecture change improves reproducibility discipline. It does not change scientific claim boundaries.
