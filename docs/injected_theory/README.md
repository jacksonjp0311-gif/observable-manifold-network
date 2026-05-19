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

## S — Specification

Injected theory records and governed theory-transfer surface.

## H — Hooks

Inbound hooks:

- README.md
- AGENTS.md
- README_90_SECONDS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- Local files in `docs/injected_theory`
- Validation reports when this folder participates in runtime, documentation, release, or RCC checks

## A — Artifacts

This folder may contain source files, docs, reports, schemas, scripts, visuals, generated state, or validation records depending on its role.

## T — Theory / Basis

Governed by OMN v1.1, OMN-SA, RCC-N, and the repository non-claim locks.

## I — Invariants

- Preserve source attribution.
- Preserve non-claim boundaries.
- Do not treat navigation as validation.
- Do not treat documentation as correctness.
- Do not claim GMN replication without benchmark conditions.
- Keep evidence and validation surfaces inspectable.

## E — Examples

Read this file before editing this folder.

Run relevant validation after changes:

    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python -m unittest discover -s tests

## RCC Nexus Echo Location

Sphere Position:

- Shell: center
- Meridian(s): documentation
- Sector: docs
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-19

Local Role:

- Injected theory records and governed theory-transfer surface.

Evidence Surface:

- reports/
- outputs/
- docs/context/drift/

Validation Surface:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

Claim Boundary:

- This mini README improves local navigation and agent orientation. It does not prove code correctness, patch safety, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.

Non-Claim Locks:

- navigation_is_not_validation
- documentation_is_not_correctness
- context_reconstruction_is_not_code_quality
- validation_remains_required
- rcc_nexus_is_not_ai_understanding
