# OMN-SA v0.9.1 — Stable Evidence Index and Latest Pointer System

## Summary

v0.9.1 adds stable evidence indexes and pointer files so "latest evidence" is selected explicitly rather than inferred from filesystem ordering.

## New CLI Surface

```text
python -m omn index-evidence --output-dir outputs
python -m omn report-latest --output-dir outputs_ci --mode ci
python -m omn validate --output-dir outputs_ci --mode ci
```

## Boundary

This release improves evidence-selection determinism. It does not prove empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
