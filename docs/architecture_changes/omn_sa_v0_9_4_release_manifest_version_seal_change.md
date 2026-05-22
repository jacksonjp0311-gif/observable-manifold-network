# OMN-SA v0.9.4 Architecture Change — Release Manifest / Version Seal

## Change Type

Release-readiness and version-seal hardening.

## What Changed

- Added machine-readable release manifest.
- Added human-readable release manifest.
- Added tests for manifest presence and non-claim boundaries.
- Updated README, DOCS_REGISTRY, CI markers, and current public metrics.
- Updated version-surface checker expectations.

## Why

The repository now has deterministic execution, explicit evidence pointers, public metrics, and version-surface checking. v0.9.4 binds those surfaces into one release object.

## Boundary

This change improves release traceability. It does not change scientific claim boundaries.
