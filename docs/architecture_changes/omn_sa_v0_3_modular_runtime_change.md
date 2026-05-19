# OMN-SA v0.3 Modular Runtime Architecture Change

## Change Type

Core runtime architecture evolution.

## From

OMN-SA v0.2 contract validation and RCC-N drift hardening.

## To

OMN-SA v0.3 modular runtime split and contract wrapper layer.

## Why

The current runtime is working but still monolithic. v0.3 starts the core evolution by adding contract modules and a wrapper around the current runtime before any broad internal rewrite.

## Added

- `src/omn/core/contracts.py`
- `src/omn/core/claim_gate.py`
- `src/omn/core/artifact_audit.py`
- `src/omn/core/schema_contracts.py`
- `src/omn/core/modular_runtime.py`
- `scripts/validation/validate_modular_runtime.py`
- `docs/software_architecture/omn_sa_v0_3_software_architecture.md`
- `tests/test_omn_sa_v0_3_modular_core.py`

## Boundary

This change wraps the current runtime. It does not claim empirical validation, GMN replication, causality, mechanism, production readiness, or AI understanding.