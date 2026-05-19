# OMN-SA v0.1 Source Anchor

## Title

CODEX ΔΦ — Observable Manifold Network Software Architecture (OMN-SA v0.1)

## Role

This file anchors the original OMN-SA v0.1 software-architecture theory inside the repository documentation shell.

It is not replacing OMN-SA v0.2.

It preserves the v0.1 source-bound architecture as lineage context so later software versions can be compared against the original runtime contract.

## Source-Bound Attribution

This anchor is derived from the original Codex-format OMN-SA v0.1 document authored by James Paul Jackson.

It is aligned with:

- OMN v1.0 — Observable Manifold Network Theory
- OMN v1.1 — Minimal Runtime Bridge and Adoption Layer
- Park et al., “Explainable prediction and simulation of complex system dynamics through networks of manifolds,” bioRxiv preprint, posted May 14, 2026

Generative Manifold Networks remain Park et al.'s method.

This repository does not claim authorship over GMN, Takens embedding, generalized Takens embedding, convergent cross mapping, simplex projection, mutual information, nonlinear cross mapping, reservoir computing, Crossformer comparison, universal approximation proof, or empirical results reported by Park et al.

## Core v0.1 Software Invariant

A runnable observable-topology system must:

1. declare observables,
2. compute or load interactions,
3. emit a typed graph contract,
4. build local delay/history manifolds,
5. run node-local generators,
6. generate state,
7. validate residuals,
8. compare baselines,
9. test topology sensitivity,
10. attribute residuals,
11. compute claim status,
12. write evidence artifacts.

Compact invariant:

    Observable topology becomes useful only when it becomes executable,
    auditable, residual-bearing, baseline-aware, topology-sensitive,
    and claim-gated.

## Original Runtime Chain

    input
    -> observables
    -> interaction matrix
    -> typed graph
    -> embeddings
    -> manifolds
    -> generators
    -> generated state
    -> residuals
    -> baselines
    -> sensitivity
    -> claim gate
    -> evidence

## Original Target Runtime

    OMN v0.1 Minimal Runtime

Original target seeds:

- synthetic-toy
- lorenz
- artifact-graph

Original residual:

    DeltaPhi_OMN = || W(S_validation - S_generated) ||

Original stability function:

    Omega_OMN = 1 / (1 + |DeltaPhi_OMN|)

## Original v0.1 Software Law

    No graph contract, no topology claim.
    No residuals, no evidence.
    No claim gate, no strong claim.

## Preserved Locks

- OMN-SA implements OMN v1.1; it does not replace OMN v1.1.
- GMN authorship remains with Park et al.
- GMN is not renamed as a Codex invention.
- Source algorithm is preserved as source-attributed kernel.
- Observable nodes must be declared.
- Edges must be typed.
- Interaction matrix must be emitted or declared.
- Graph contract must be emitted.
- Delay/history policy must be recorded.
- Node generators must be declared.
- Generated state must be validated.
- Residuals must be preserved.
- DeltaPhi/Omega are residual metrics, not truth.
- Baselines must be allowed to win.
- Topology sensitivity must be reported.
- Edge confidence is not causal certainty.
- Claim status must be computed from evidence, not tone.
- README compression may not weaken locks.
- Tests are implementation health truth.
- Evidence packages are run truth.
- Ledgers are continuity truth.

## Relation to Current OMN-SA v0.2

OMN-SA v0.2 is the current software architecture layer.

OMN-SA v0.1 is preserved here as the source anchor.

v0.2 adds:

- schema contracts,
- architecture contract validation,
- RCC-N drift hardening,
- CI/release validation expectations,
- docs-lane enforcement,
- modular runtime target.

v0.2 does not erase v0.1. It hardens it.

## Boundary

This source anchor is documentation and lineage preservation.

It does not prove:

- code correctness,
- empirical validation,
- GMN replication,
- causality,
- mechanism,
- biological equivalence,
- physical manifold identity,
- production readiness,
- AI understanding,
- or source-paper correctness.

## Update Rule

If OMN-SA v0.3 or later changes the runtime architecture, update this file only by adding comparison notes. Do not rewrite the v0.1 invariant.

## RCC Nexus Echo Location

Sphere Position:

- Shell: outer
- Meridian(s): source, documentation, safety, runtime
- Sector: source
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-16

Local Role:

- Preserves original OMN-SA v0.1 software-architecture lineage.

Inbound Hooks:

- README.md
- docs/DOCS_REGISTRY.md
- docs/software_architecture/omn_sa_v0_2_software_architecture.md
- docs/injections/omn_sa_v0_1_theory_insertion.md

Outbound Hooks:

- docs/architecture_changes/omn_sa_v0_1_theory_insertion_change.md
- docs/release_notes/v0_2_1_theory_insertion.md
- tests/test_theory_insertion_docs.py

Evidence Surface:

- reports/theory/
- reports/architecture/
- reports/rcc_nexus/

Validation Surface:

    python scripts/validation/validate_architecture_contracts.py
    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

Claim Boundary:

- This source anchor improves lineage traceability.
- It does not prove implementation correctness, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.

Non-Claim Locks:

- source_anchor_is_not_runtime
- lineage_is_not_validation
- documentation_is_not_correctness
- gmn_authorship_preserved
- observable_topology_is_not_truth
- prediction_is_not_mechanism
- simulation_is_not_proof