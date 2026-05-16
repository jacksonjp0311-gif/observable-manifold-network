# Folder Purpose

## S - Specification

Seed metadata for synthetic, Lorenz, and artifact-graph runs.

## H - Hooks

Inbound hooks:

- configs/omn_default.json

Outbound hooks:

- examples
- src/omn/core/runtime.py

## A - Artifacts

Evidence / output surfaces:

- configs/seeds

## T - Theory / Basis

Governed by OMN-SA v0.1 and RCC-N v1.0.

OMN-SA basis:

    observables -> interaction matrix -> typed graph -> generated state -> residuals -> evidence

RCC-N basis:

    Human README -> RCC Nexus README -> AI Agent README -> route map -> Echo Location -> validation

## I - Invariants

- Preserve GMN source attribution.
- Preserve non-claim locks.
- Preserve evidence-bound claims.
- Do not claim causality, mechanism, biological equivalence, physical manifold identity, empirical validation, or full GMN replication.
- Navigation is not validation.
- Context is not correctness.

## E - Examples

Validation examples:

- python -m omn run --seed lorenz

## RCC Nexus Echo Location

Sphere Position:

- Shell: inner
- Meridian(s): runtime, source
- Sector: examples
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Seed metadata for synthetic, Lorenz, and artifact-graph runs.

Inbound Hooks:

- configs/omn_default.json

Outbound Hooks:

- examples
- src/omn/core/runtime.py

Evidence Surface:

- configs/seeds

Validation Surface:

- python -m omn run --seed lorenz

Claim Boundary:

- This folder improves implementation, evidence, documentation, or navigation only within its declared scope.
- It does not prove code correctness, patch safety, empirical validation, causality, mechanism, or GMN replication.

Non-Claim Locks:

- geometry_is_not_ai_internal_proof
- nci_is_not_code_quality_proof
- navigation_is_not_validation
- context_reconstruction_is_not_correctness_proof
- validation_remains_required
- observable_topology_is_not_truth
- prediction_is_not_mechanism
- simulation_is_not_proof

Agent Route:

- Read root README, docs/context indexes, route map, then this README before editing.

Update Obligation:

- Update this README and RCC/Nexus records if folder purpose, hooks, evidence surfaces, validation commands, or claim boundaries change.