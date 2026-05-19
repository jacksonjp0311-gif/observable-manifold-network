# Folder Purpose

## S - Specification

Runtime and seed configuration.

## H - Hooks

Inbound hooks:

- README.md
- src/omn/core/runtime.py

Outbound hooks:

- configs/seeds

## A - Artifacts

Evidence / output surfaces:

- configs

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

## RCC Nexus Echo Location

Sphere Position:

- Shell: inner
- Meridian(s): runtime, source
- Sector: runtime
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Runtime and seed configuration.

Inbound Hooks:

- README.md
- src/omn/core/runtime.py

Outbound Hooks:

- configs/seeds

Evidence Surface:

- configs

Validation Surface:

- python -m omn run --seed synthetic-toy

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

## S — Specification

Runtime and seed configuration surface.

## H — Hooks

Inbound hooks:

- README.md
- AGENTS.md
- README_90_SECONDS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- Local files in `configs`
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

- Shell: middle
- Meridian(s): configuration
- Sector: configs
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-19

Local Role:

- Runtime and seed configuration surface.

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
