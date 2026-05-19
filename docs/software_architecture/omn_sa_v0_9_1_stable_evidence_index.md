# CODEX ΔΦ — OMN-SA v0.9.1 Stable Evidence Index and Latest Pointer System

## Purpose

v0.9.1 replaces implicit latest-evidence selection with explicit evidence indexes and pointer files.

v0.9.0 made run identity deterministic. v0.9.1 makes evidence selection explicit.

## Added Surfaces

- `outputs/evidence/evidence_index.json`
- `outputs/evidence/latest_evidence.json`
- `outputs/evidence/latest_ci_fixture.json`
- `outputs/evidence/latest_release_evidence.json`
- `python -m omn index-evidence --output-dir outputs`
- `python -m omn report-latest --output-dir outputs --mode ci`
- `python -m omn report-latest --output-dir outputs --mode release`

## v0.9.1 Law

No latest evidence without an explicit pointer.

## Boundary

The evidence index improves evidence selection and reproducibility discipline. It does not prove empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
