# OMN-SA v0.6 Evidence Replay Architecture Change

## Change Type

Evidence continuity and run-ledger integrity.

## Added

- `src/omn/core/evidence_replay.py`
- `src/omn/core/run_ledger.py`
- `src/omn/core/run_compare.py`
- `scripts/validation/validate_evidence_replay.py`
- `docs/software_architecture/omn_sa_v0_6_software_architecture.md`
- `reports/evidence_replay/latest_evidence_replay_validation.json`
- `reports/ledger_integrity/`
- `tests/test_omn_sa_v0_6_evidence_replay.py`

## Boundary

This change verifies artifact continuity and local ledger integrity. It does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.