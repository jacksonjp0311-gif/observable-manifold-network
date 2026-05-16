# Observable Manifold Network

Repository: observable-manifold-network  
Package / CLI: omn  
Architecture: OMN-SA v0.1  
Status: Minimal local runtime scaffold.

## What this is

Observable Manifold Network is a minimal Python runtime for observable-topology dynamical modeling.

It can:

- declare observable nodes
- compute an interaction matrix
- build typed graph contracts
- run simple node-local generators
- generate future state
- validate residuals
- compare baselines
- test topology sensitivity
- attribute residuals
- gate claims
- emit evidence JSON, reports, plots, logs, and ledger records

## Source boundary

This repository is aligned with OMN-SA v0.1, derived from OMN v1.0 and OMN v1.1, which are source-bounded extractions from Park et al.'s Generative Manifold Networks paper.

GMN remains Park et al.'s method. OMN is a Codex runtime architecture that preserves the observable-topology spine while adding governance, evidence, and claim-gating layers.

## What this is not

This is not:

- a claim to have invented GMN
- a full GMN replication
- empirical validation
- proof of causality
- proof of mechanism
- proof of biological equivalence
- proof that observable topology is truth
- proof that OMN outperforms GMN or any baseline

## Quick start

From the repository root:

    $env:PYTHONPATH = "$PWD\src"
    python -m omn --help
    python -m omn run --seed synthetic-toy
    python -m omn run --seed lorenz
    python -m omn run --seed artifact-graph
    python -m unittest discover -s tests

## Output locations

- outputs/state
- outputs/evidence
- outputs/reports
- outputs/plots
- outputs/logs
- outputs/ledger

## AI operating contract

Before modifying this repo, read:

1. README.md
2. README_90_SECONDS.md
3. docs/architecture/rcc_context_map.md
4. the relevant tests

Do not weaken source attribution, non-claim locks, evidence gates, graph contracts, or residual validation requirements.