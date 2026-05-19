# v0.3.0 Modular Runtime Release Note

## Status

Core software architecture evolution.

## Added

- Modular contracts
- Claim gate module
- Artifact audit module
- Schema contract module
- Modular runtime wrapper
- Modular runtime validation report
- Modular runtime validation script
- v0.3 tests
- v0.3 architecture document

## Validation

Required:

    python scripts/validation/validate_modular_runtime.py
    python scripts/validation/validate_architecture_contracts.py
    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests
    python -m omn run --seed synthetic-toy
    python -m omn validate

## Boundary

v0.3 is modularization-safe architecture. It does not prove empirical validation, GMN replication, causality, mechanism, production readiness, or AI understanding.