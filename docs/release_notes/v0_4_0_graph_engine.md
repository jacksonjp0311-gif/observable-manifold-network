# v0.4.0 Graph Engine Release Note

## Status

Core graph-engine extraction.

## Added

- Observables module
- Interactions module
- Graph engine module
- Residuals module
- Evidence IO module
- Graph engine validation script
- Graph engine validation report
- v0.4 architecture document
- v0.4 tests

## Validation

Required:

    python scripts/validation/validate_graph_engine.py
    python scripts/validation/validate_modular_runtime.py
    python scripts/validation/validate_architecture_contracts.py
    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests
    python -m omn run --seed synthetic-toy
    python -m omn validate

## Boundary

v0.4 extracts graph-engine surfaces. It does not prove causality, mechanism, empirical validation, production readiness, AI understanding, or GMN replication.