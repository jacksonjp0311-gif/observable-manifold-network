# Injected Theory

## Purpose

This folder stores theory that has been intentionally inserted into the project through a declared source-boundary or injection process.

This is separate from:

- `docs/theory/` — canonical theory summaries and source-bound theory bridge
- `docs/software_architecture/` — executable software architecture
- `docs/injections/` — governance/module injection records
- `docs/architecture_changes/` — versioned structural changes

## Why this exists

Some theory enters a repository as a deliberate addition rather than as original local implementation.

When that happens, the theory needs a clear boundary:

- what source it came from,
- what was extracted,
- what was adapted,
- what claims are allowed,
- what claims are forbidden,
- whether it affects runtime behavior,
- whether it requires new validation.

## Current Status

No separate injected-theory payload is canonical yet beyond the existing OMN theory bridge.

Current canonical theory remains:

- `docs/theory/omn_v1_1_theory_bridge.md`

Current canonical architecture remains:

- `docs/software_architecture/omn_sa_v0_1_software_architecture.md`

Current injection records remain:

- `docs/injections/`

## Admission Rule

Injected theory must include:

1. source attribution,
2. extraction boundary,
3. adaptation boundary,
4. affected files,
5. affected claims,
6. affected validation commands,
7. non-claim locks,
8. rollback/downgrade rule.

## RCC Nexus Echo Location

Sphere Position:

- Shell: outer
- Meridian(s): source, documentation, safety, release
- Sector: source
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Stores source-bounded theory inserted into the repo by declared process.

Inbound Hooks:

- README.md
- docs/DOCS_REGISTRY.md
- docs/theory/
- docs/injections/

Outbound Hooks:

- docs/software_architecture/
- docs/architecture_changes/
- docs/release_notes/

Evidence Surface:

- docs/injected_theory/
- reports/rcc_nexus/latest_rcc_nexus_check.md

Validation Surface:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

Claim Boundary:

- Injected theory is not implementation proof.
- Injected theory is not empirical validation.
- Injected theory may not weaken source attribution or non-claim locks.

Non-Claim Locks:

- theory_is_not_runtime
- source_extraction_is_not_authorship
- documentation_is_not_validation
- validation_remains_required

Agent Route:

- Read README.md, docs/DOCS_REGISTRY.md, docs/theory/README.md, docs/injections/README.md, then this README before editing injected theory.

Update Obligation:

- Update this folder when new source-bounded theory is injected into the project.