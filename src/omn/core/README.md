# Folder Purpose

## S - Specification

Executable runtime implementation for seeds, graph contracts, residuals, baselines, claim gates, and evidence emission.

## H - Hooks

Inbound hooks:

- src/omn/cli.py
- python -m omn

Outbound hooks:

- outputs/state
- outputs/evidence
- outputs/reports
- tests/test_runtime.py

## A - Artifacts

Evidence / output surfaces:

- outputs/evidence

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

- python -m omn run --seed synthetic-toy
- python -m unittest discover -s tests

## RCC Nexus Echo Location

Sphere Position:

- Shell: inner
- Meridian(s): runtime, validation, evidence, safety
- Sector: core
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Executable runtime implementation for seeds, graph contracts, residuals, baselines, claim gates, and evidence emission.

Inbound Hooks:

- src/omn/cli.py
- python -m omn

Outbound Hooks:

- outputs/state
- outputs/evidence
- outputs/reports
- tests/test_runtime.py

Evidence Surface:

- outputs/evidence

Validation Surface:

- python -m omn run --seed synthetic-toy
- python -m unittest discover -s tests

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