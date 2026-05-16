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