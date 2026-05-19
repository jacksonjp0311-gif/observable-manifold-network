# Theory Documents

## Purpose

This folder stores source-bounded theory summaries and version bridges.

## Current Theory Stack

| Theory | File | Role |
|---|---|---|
| OMN v1.0 | `omn_v1_0_summary.md` | Observable-topology source-bounded extraction. |
| OMN v1.1 | `omn_v1_1_theory_bridge.md` | Minimal runtime bridge and adoption layer. |
| GMN source summary | `gmn_source_summary.md` | Source-method boundary and attribution. |

## Update Rule

Every theory change must update:

- root README registry section,
- `docs/DOCS_REGISTRY.md`,
- this README,
- relevant software architecture docs if runtime behavior changes,
- relevant injection docs if a governance layer changes.

## Boundary

Theory documents are not implementation proof, empirical validation, or source-paper replication.

## S — Specification

Canonical OMN theory and source-anchor documents.

## H — Hooks

Inbound hooks:

- README.md
- AGENTS.md
- README_90_SECONDS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- Local files in `docs/theory`
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

- Canonical OMN theory and source-anchor documents.

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
