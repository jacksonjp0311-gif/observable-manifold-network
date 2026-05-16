# OMN-SA v0.1 Software Architecture

## Identity

Name: Observable Manifold Network Software Architecture  
Short name: OMN-SA v0.1  
Repository: observable-manifold-network  
Package / CLI: omn  
Status: canonical v0.1 software architecture genesis layer

## Source Alignment

OMN-SA v0.1 is derived from and aligned with:

- OMN v1.0: source-bounded Observable Manifold Network Theory
- OMN v1.1: Minimal Runtime Bridge and Adoption Layer
- Park et al.'s Generative Manifold Networks source paper

GMN remains Park et al.'s method. OMN-SA does not claim authorship over GMN, Takens embedding, generalized Takens embedding, convergent cross mapping, simplex projection, mutual information, nonlinear cross mapping, reservoir computing, Crossformer comparison, universal approximation proof, Drosophila analysis, Rattus norvegicus analysis, or source-paper empirical results.

## Core Software Invariant

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

## Runtime Chain

    input time series or artifact graph
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

## Current First Runtime

Current target runtime:

    OMN v0.1 Minimal Runtime

Current seeds:

- synthetic-toy
- lorenz
- artifact-graph

Current residual:

    DeltaPhi_OMN = || W(S_validation - S_generated) ||

Current stability function:

    Omega_OMN = 1 / (1 + |DeltaPhi_OMN|)

## Object Contracts

### ObservableNode

    node_id
    observable_name
    observable_type
    data_path
    column
    role
    claim_boundary

### TypedEdge

    source
    target
    edge_type
    weight
    direction
    threshold_policy
    confidence
    status
    claim_boundary

### GraphContract

    schema
    run_id
    target_node
    cycle_policy
    driver_count_policy
    nodes
    edges
    valid
    failure_flags

### LocalManifold

    node_id
    drivers
    embedding_policy
    E
    tau
    manifold_state_path
    generator

## Required Evidence Outputs

A complete v0.1 run should emit:

- observables JSON,
- interaction matrix CSV,
- graph contract JSON,
- generated state CSV,
- validation residuals CSV,
- residual attribution JSON,
- state JSON,
- evidence JSON,
- markdown report,
- SVG plots,
- runtime log,
- JSONL ledger.

## Claim Gate

Supported claim statuses:

- blocked
- demo-only
- runtime-validated
- benchmark-supported
- replication-attempted
- externally-validated

Current v0.1 strongest local status:

    runtime-validated

Boundary:

    runtime-validated != empirical validation
    runtime-validated != full GMN replication
    runtime-validated != proof of causality
    runtime-validated != proof of mechanism

## Canonical Locks

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
- DeltaPhi / Omega are residual metrics, not truth.
- Baselines must be allowed to win.
- Topology sensitivity must be reported.
- Edge confidence is not causal certainty.
- Claim status must be computed from evidence, not tone.
- README compression may not weaken locks.
- Tests are implementation health truth.
- Evidence packages are run truth.
- Ledgers are continuity truth.

## Software Non-Claim Lock

OMN-SA measures and emits observable-topology runtime artifacts.

It does not prove:

- intelligence,
- consciousness,
- truth,
- scientific validity,
- code correctness,
- causal mechanism,
- physical manifold identity,
- biological equivalence,
- universal applicability,
- full GMN replication,
- superiority over GMN, ESN, EDM, Crossformer, transformers, or any baseline.

## Version Update Obligation

When OMN-SA evolves, update:

- root README registry section,
- this architecture file,
- docs registry,
- release notes,
- relevant mini READMEs,
- RCC-N route/index files if paths or validation commands change.