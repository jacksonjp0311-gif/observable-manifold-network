# OMN-SA v0.8.3 Architecture Change — CI / Release Boundary Separation

## Change Type

Operational architecture repair.

## What Changed

- CI is confirmed as a non-release smoke gate.
- Artifact-emitting validation is moved into a local release checkpoint script.
- A test verifies that GitHub Actions does not call artifact-refresh validators.
- Documentation records the discovered failure mode.

## Why

The repo entered a self-refresh loop:

validation -> report mutation -> commit -> CI -> report mutation -> red X

v0.8.3 breaks that loop by separating smoke validation from release artifact refresh.

## Boundary

This change improves operational stability. It does not change OMN runtime claims, scientific claims, or source-paper boundaries.