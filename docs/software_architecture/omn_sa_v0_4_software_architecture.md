# CODEX ΔΦ — OBSERVABLE MANIFOLD NETWORK SOFTWARE ARCHITECTURE (OMN-SA v0.4)

## Graph Engine Extraction and Evidence-Preserving Runtime Split

Author: James Paul Jackson  
X / Twitter: @unifiedenergy11  
Date: May 2026  
Status: Canonical v0.4 software architecture implementation layer

---

## Source / Author Attribution

OMN-SA v0.4 evolves the repository after:

- OMN v1.1 — Minimal Runtime Bridge and Adoption Layer
- OMN-SA v0.1 — preserved source architecture anchor
- OMN-SA v0.2 — contract validation and RCC-N compatibility layer
- OMN-SA v0.3 — modular runtime wrapper layer
- Park et al.'s Generative Manifold Networks source paper

Generative Manifold Networks remain Park et al.'s method.

OMN-SA v0.4 does not claim GMN authorship, GMN replication, empirical validation, causality, mechanism, biological equivalence, physical manifold identity, AI understanding, or production readiness.

---

## Version

v0.4 — Graph Engine Extraction and Evidence-Preserving Runtime Split · Locked ·

Adds:

- observables module,
- interactions module,
- graph engine module,
- residuals module,
- evidence IO module,
- graph engine validation script,
- graph engine parity report,
- v0.4 tests,
- v0.4 architecture and release records.

---

## Purpose

OMN-SA v0.4 begins the first real runtime split.

v0.3 wrapped the working runtime.

v0.4 extracts graph-engine concepts into dedicated modules while preserving the legacy runtime path.

The target is not a rewrite.

The target is evidence-preserving extraction.

---

## v0.4 Law

    No split without parity.
    No parity without evidence.
    No evidence without validation.

---

## Runtime Split Strategy

Current path:

    legacy runtime
    -> evidence package

v0.4 path:

    observable columns
    -> observables module
    -> interaction matrix module
    -> graph engine module
    -> graph contract
    -> graph validation report

Parity path:

    legacy runtime evidence
    + modular graph state
    -> parity summary
    -> validation report

---

## New Modules

| Module | Role |
|---|---|
| `src/omn/core/observables.py` | Builds and validates observable series. |
| `src/omn/core/interactions.py` | Computes simple interaction matrices and typed edges. |
| `src/omn/core/graph_engine.py` | Builds graph engine state and graph-contract parity report. |
| `src/omn/core/residuals.py` | Computes RMSE, MAE, DeltaPhi, and Omega residuals. |
| `src/omn/core/evidence_io.py` | Loads and writes evidence/report JSON. |

---

## Validation Surface

Required commands:

    python scripts/validation/validate_graph_engine.py
    python scripts/validation/validate_modular_runtime.py
    python scripts/validation/validate_architecture_contracts.py
    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests
    python -m omn run --seed synthetic-toy
    python -m omn validate

---

## Falsification Surface

OMN-SA v0.4 is weakened if:

- it removes the legacy runtime path before parity,
- graph engine outputs do not emit graph contracts,
- edge claim boundaries are missing,
- interaction weights are described as causality,
- residuals are treated as truth,
- parity report is missing,
- validation commands fail,
- evidence emission breaks,
- source attribution weakens,
- RCC-N navigation weakens.

---

## Roadmap After v0.4

v0.5 should deepen the topology ensemble engine.

v0.6 should harden benchmark ladder enforcement.

v0.7 should move evidence writing fully into modular evidence IO.

---

## Concluding Compression

OMN-SA v0.3 made modularization safe.

OMN-SA v0.4 begins the split.

The graph can now be built outside the legacy runtime.

But the claim remains bounded:

    Graph structure is not causality.
    Residual geometry is not truth.
    Runtime parity is not empirical validation.