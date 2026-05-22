# OMN-SA v0.9.5 Architecture Change — v1.0 Readiness Gate

## Change Type

Release promotion and readiness-classification hardening.

## What Changed

- Added v1.0 readiness checker.
- Added readiness report JSON/MD.
- Added tests for readiness classification and boundaries.
- Updated README, DOCS_REGISTRY, CI markers, and public metrics.

## Why

The repository now has deterministic execution, explicit evidence pointers, public metrics, version-surface checking, and a release seal. v0.9.5 determines whether those surfaces are sufficient to prepare for v1.0.0.

## Boundary

This change improves release promotion discipline. It does not change scientific claim boundaries.
