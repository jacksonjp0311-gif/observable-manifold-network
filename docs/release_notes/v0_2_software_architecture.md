# OMN-SA v0.2 Software Architecture Release Note

## Status

Added as canonical software architecture iteration.

## Added

- `docs/software_architecture/omn_sa_v0_2_software_architecture.md`
- `docs/architecture_changes/omn_sa_v0_2_architecture_change.md`
- schema contracts under `schemas/`
- `scripts/validation/validate_architecture_contracts.py`
- `tests/test_omn_sa_v0_2_architecture.py`
- README and README_90_SECONDS v0.2 references
- docs registry v0.2 registration

## Validation

Required:

    python scripts/validation/validate_architecture_contracts.py
    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests
    python -m omn run --seed synthetic-toy
    python -m omn validate

## Boundary

This release note records software architecture hardening.

It does not update OMN theory and does not claim empirical validation, code correctness, AI understanding, causality, mechanism, production readiness, or GMN replication.