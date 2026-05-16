# Injection Records

## Purpose

This folder records governance, module, documentation, and repository-context injections into Observable Manifold Network.

An injection is not the same as an architecture change.

An injection is a declared addition that modifies how the repository is governed, navigated, interpreted, validated, or extended.

## Separation Rule

Use these folders distinctly:

| Folder | Purpose |
|---|---|
| `docs/injections/` | Governance/module/documentation injections and their Anchor -> Inject -> Retract -> Seal records. |
| `docs/software_architecture/` | Current canonical software architecture. |
| `docs/architecture_changes/` | Versioned changes to architecture or repo structure. |
| `docs/theory/` | Canonical theory and theory bridge summaries. |
| `docs/injected_theory/` | Source-bounded theory inserted through a declared injection/admission process. |

## Active Injections

| Injection | File | Status | Purpose |
|---|---|---|---|
| RCC-N shell | `rcc_nexus_injection.md` | active | Adds AERMA-style README trisection, route maps, Echo Location records, and repository navigation. |
| Docs registry shell | `docs_registry_injection.md` | active | Adds theory / software architecture / injections registry and update obligation. |

## Injection Record Requirements

Every future injection must include:

1. host surface,
2. injected layer,
3. operator,
4. anchor,
5. inject step,
6. retract step,
7. seal step,
8. classification,
9. validation surface,
10. non-claim boundary,
11. affected architecture files if any,
12. affected theory files if any,
13. rollback or downgrade rule.

## Boundary

Injection records document governance and architecture additions.

They do not prove code correctness, empirical validation, patch safety, causality, mechanism, biological equivalence, physical manifold identity, production readiness, or GMN replication.

## RCC Nexus Echo Location

Sphere Position:

- Shell: outer
- Meridian(s): documentation, agent, safety, drift
- Sector: rcc
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Stores governance injection records for RCC-N, docs registry, and future governance modules.

Inbound Hooks:

- README.md
- docs/DOCS_REGISTRY.md
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound Hooks:

- docs/injections/rcc_nexus_injection.md
- docs/injections/docs_registry_injection.md
- docs/software_architecture/
- docs/architecture_changes/
- docs/injected_theory/
- docs/theory/
- docs/future_architecture/
- docs/release_notes/

Evidence Surface:

- reports/rcc_nexus/latest_rcc_nexus_check.md
- reports/rcc_nexus/latest_rcc_nexus_check.json
- docs/context/drift/latest_rcc_nexus_report.md

Validation Surface:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

Claim Boundary:

- Injection records improve governance traceability and repository navigation.
- Injection records do not prove runtime correctness, empirical validation, patch safety, causality, mechanism, biological equivalence, physical manifold identity, production readiness, or GMN replication.

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

- Read README.md, docs/DOCS_REGISTRY.md, docs/context/repository_context_index.json, docs/context/rcc_nexus_index.json, rcc/nexus/route_map.json, then this README before editing injection records.

Update Obligation:

- Update this README, docs/DOCS_REGISTRY.md, root README registry section, and RCC-N indexes whenever injection records, governance modules, software architecture layers, architecture-change records, injected-theory tracks, future architecture tracks, claim boundaries, or validation commands change.