# OMN-SA v0.9.0 — Deterministic Run Identity and Execution Modes

## Summary

v0.9.0 adds deterministic runtime modes after v0.8.3 separated CI from release validation.

## New CLI Surface

```text
python -m omn run --seed synthetic-toy --ci-mode --run-id omn_ci_smoke --output-dir outputs_ci --no-write-report
python -m omn validate --output-dir outputs_ci
python -m omn report-latest --output-dir outputs_ci
```

## Boundary

This release improves deterministic execution and reproducibility discipline. It does not prove empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
