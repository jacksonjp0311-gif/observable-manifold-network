# Architecture Changes

## Purpose

This folder stores versioned architecture changes for Observable Manifold Network.

Architecture changes are separate from:

- `docs/theory/` — source-bounded theory and theory bridge documents
- `docs/software_architecture/` — current canonical software architecture
- `docs/injections/` — governance or module injections
- `docs/injected_theory/` — theory inserted into the project through a declared source/injection process

## Current Architecture Change Records

| Version | Record | Status |
|---|---|---|
| OMN-SA v0.1 | `docs/software_architecture/omn_sa_v0_1_software_architecture.md` | canonical baseline |
| RCC-N docs registry patch | root README registry + docs registry | active |
| RCC-N benchmark/public release patch | benchmark docs + chart + public release essay | active |

## Update Rule

Add a record here whenever project structure, runtime architecture, evidence schema, validation route, CLI surface, or docs registry structure changes.

Do not store governance injections here. Governance injections belong in `docs/injections/`.

Do not store primary theory here. Theory belongs in `docs/theory/` or `docs/injected_theory/`.

## RCC Nexus Echo Location

Sphere Position:

- Shell: outer
- Meridian(s): documentation, release, runtime, safety
- Sector: release
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Stores architecture-change records and versioned structural evolution notes.

Inbound Hooks:

- README.md
- docs/DOCS_REGISTRY.md
- docs/software_architecture/

Outbound Hooks:

- docs/release_notes/
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Evidence Surface:

- reports/rcc_nexus/latest_rcc_nexus_check.md
- docs/context/drift/latest_rcc_nexus_report.md

Validation Surface:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

Claim Boundary:

- Architecture-change records document structural evolution.
- They do not prove code correctness, empirical validation, patch safety, causality, mechanism, production readiness, or GMN replication.

Non-Claim Locks:

- architecture_is_not_correctness
- documentation_is_not_validation
- navigation_is_not_validation
- validation_remains_required

Agent Route:

- Read README.md, docs/DOCS_REGISTRY.md, this README, then relevant architecture files before changing architecture records.

Update Obligation:

- Update this folder when architecture, runtime structure, CLI routes, evidence schemas, or validation routes change.

## S — Specification

Versioned architecture-change records.

## H — Hooks

Inbound hooks:

- README.md
- AGENTS.md
- README_90_SECONDS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- Local files in `docs/architecture_changes`
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

- Versioned architecture-change records.

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
