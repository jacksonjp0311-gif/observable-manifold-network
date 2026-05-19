# OMN-SA v0.9.1 Architecture Change — Stable Evidence Index

## Change Type

Evidence selection and pointer-system hardening.

## What Changed

- Added evidence index generation.
- Added latest evidence pointer files.
- Added mode-aware latest evidence selection.
- Added `index-evidence` CLI command.
- Added `--mode ci|release` to `validate` and `report-latest`.

## Why

File modification time is not a sufficient public evidence-selection rule. v0.9.1 makes latest evidence explicit and inspectable.

## Boundary

This architecture change improves reproducibility and evidence navigation. It does not change scientific claim boundaries.
