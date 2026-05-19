# OMN-SA v0.4 Graph Engine Architecture Change

## Change Type

Core graph-engine extraction.

## From

OMN-SA v0.3 modular runtime wrapper.

## To

OMN-SA v0.4 graph engine extraction and evidence-preserving runtime split.

## Added

- `src/omn/core/observables.py`
- `src/omn/core/interactions.py`
- `src/omn/core/graph_engine.py`
- `src/omn/core/residuals.py`
- `src/omn/core/evidence_io.py`
- `scripts/validation/validate_graph_engine.py`
- `docs/software_architecture/omn_sa_v0_4_software_architecture.md`
- `tests/test_omn_sa_v0_4_graph_engine.py`

## Boundary

This change begins graph-engine extraction. It does not prove causality, mechanism, empirical validation, production readiness, AI understanding, or GMN replication.