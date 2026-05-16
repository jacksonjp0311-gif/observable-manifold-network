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