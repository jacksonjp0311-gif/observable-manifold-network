# Folder Purpose

## S - Specification

Repository context indexes, Nexus index, validation surface, and drift report surface.

## H - Hooks

Inbound hooks:

- README.md
- rcc/nexus

Outbound hooks:

- repository_context_index.json
- rcc_nexus_index.json
- validation_surface.md

## A - Artifacts

Evidence / output surfaces:

- docs/context/drift

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

- python scripts/rcc/check_rcc_nexus.py

## RCC Nexus Echo Location

Sphere Position:

- Shell: outer
- Meridian(s): documentation, drift, evidence, agent
- Sector: rcc
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Repository context indexes, Nexus index, validation surface, and drift report surface.

Inbound Hooks:

- README.md
- rcc/nexus

Outbound Hooks:

- repository_context_index.json
- rcc_nexus_index.json
- validation_surface.md

Evidence Surface:

- docs/context/drift

Validation Surface:

- python scripts/rcc/check_rcc_nexus.py

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