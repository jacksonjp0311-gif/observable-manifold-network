# Software Architecture

## Purpose

This folder stores canonical and future software architecture documents for Observable Manifold Network.

## Current Canonical Architecture

- `omn_sa_v0_1_software_architecture.md`

## Current Architecture Summary

OMN-SA v0.1 turns OMN v1.1 into a minimal executable runtime:

    input
    -> observable registry
    -> interaction matrix
    -> typed graph contract
    -> delay/history embeddings
    -> local manifold state
    -> node-local generators
    -> closed-loop generated state
    -> validation residuals
    -> DeltaPhi / Omega residual geometry
    -> baseline comparison
    -> ablation report
    -> topology ensemble sensitivity
    -> residual attribution
    -> claim gate
    -> state artifacts
    -> evidence JSON
    -> markdown report
    -> RCC context surfaces

## Update Rule

Every architecture change must update:

- this README,
- `docs/DOCS_REGISTRY.md`,
- root `README.md` section named “Theory / Software Architecture / Injections Registry”,
- `README_90_SECONDS.md` if public behavior changes,
- relevant mini READMEs,
- validation commands if needed.

## Boundary

This architecture documents the runtime scaffold. It does not prove empirical validity, code correctness, causality, mechanism, biological equivalence, physical manifold identity, production readiness, or full GMN replication.

## RCC Nexus Echo Location

Sphere Position:

- Shell: outer
- Meridian(s): documentation, runtime, source, safety
- Sector: release
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Stores canonical and future software architecture records.

Validation Surface:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

Claim Boundary:

- Architecture is not correctness.
- Design is not validation.
- Runtime scaffold is not full GMN replication.

## S — Specification

OMN-SA software architecture lineage.

## H — Hooks

Inbound hooks:

- README.md
- AGENTS.md
- README_90_SECONDS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- Local files in `docs/software_architecture`
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

- OMN-SA software architecture lineage.

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
