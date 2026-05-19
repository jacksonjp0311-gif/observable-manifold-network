# OMN-SA v0.1 Theory Insertion Architecture Change

## Change Type

Documentation architecture and lineage preservation.

## Summary

Inserted the original OMN-SA v0.1 source architecture into `docs/theory/` as a preserved source anchor.

## Why This Was Needed

The repository is now at OMN-SA v0.2, but the original v0.1 software-architecture theory should remain accessible inside the docs shell.

This prevents the software architecture lineage from becoming detached from the initial runtime contract.

## Files Added

- `docs/theory/omn_sa_v0_1_source_anchor.md`
- `docs/injections/omn_sa_v0_1_theory_insertion.md`
- `docs/architecture_changes/omn_sa_v0_1_theory_insertion_change.md`
- `docs/release_notes/v0_2_1_theory_insertion.md`
- `tests/test_theory_insertion_docs.py`

## Boundary

This change does not alter runtime behavior.

This change does not update OMN theory.

This change does not replace OMN-SA v0.2.

It preserves OMN-SA v0.1 as the lineage anchor.

## Validation

    python scripts/validation/validate_architecture_contracts.py
    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests
    python -m omn run --seed synthetic-toy
    python -m omn validate