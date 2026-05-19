# CODEX ΔΦ — OBSERVABLE MANIFOLD NETWORK SOFTWARE ARCHITECTURE (OMN-SA v0.3)

## Modular Runtime Split and Contract Wrapper Layer

Author: James Paul Jackson  
X / Twitter: @unifiedenergy11  
Date: May 2026  
Status: Canonical v0.3 software architecture implementation layer

---

## Source / Author Attribution

OMN-SA v0.3 evolves the current repository implementation after:

- OMN v1.1 — Minimal Runtime Bridge and Adoption Layer
- OMN-SA v0.1 — Minimal Runtime Genesis and Evidence-Gated Observable Graph Layer
- OMN-SA v0.2 — CI, Modular Runtime, Schema Validation, and RCC-N Drift Hardening Layer
- The preserved OMN-SA v0.1 source anchor in docs/theory
- Park et al.'s Generative Manifold Networks source paper

Generative Manifold Networks remain Park et al.'s method.

OMN-SA v0.3 does not claim GMN authorship, GMN replication, empirical validation, causality, mechanism, biological equivalence, physical manifold identity, AI understanding, or production readiness.

---

## Version

v0.3 — Modular Runtime Split and Contract Wrapper Layer · Locked ·

Adds:

- modular core contracts,
- claim gate module,
- artifact audit module,
- schema contract module,
- modular runtime wrapper,
- modular runtime validation script,
- modular runtime report,
- v0.3 tests,
- v0.3 architecture and release records.

---

## Purpose

OMN-SA v0.3 begins evolving the core of the repository without rewriting blindly.

The existing runtime is left intact as the legacy executable path.

v0.3 adds a modular wrapper around it so future versions can split internals safely.

This avoids the dangerous pattern:

    rewrite runtime first
    hope behavior survives

and replaces it with:

    wrap runtime
    validate contracts
    test modules
    preserve evidence
    then split internals

---

## What This Is

- A modular core architecture layer
- A safe wrapper around the current runtime
- A contract boundary before full runtime split
- A validation layer for modular modules
- A preparation step for deeper v0.4 graph/engine refactor

---

## What This Is Not

- Not a full runtime rewrite
- Not a GMN replication
- Not empirical validation
- Not proof of causality
- Not proof of mechanism
- Not proof of AI understanding
- Not production readiness
- Not a replacement for OMN v1.1 theory
- Not permission to remove existing working runtime behavior

---

## Core Extraction

v0.3 software invariant:

    Do not split a working monolith until contracts exist around it.

Runtime evolution chain:

    current runtime
    -> modular contracts
    -> modular claim gate
    -> modular artifact audit
    -> modular schema validation
    -> modular wrapper
    -> modular validation report
    -> future internal split

---

## Canonical Lock v0.3

- Preserve existing runtime behavior.
- Add modules before replacing internals.
- Do not weaken evidence output.
- Do not weaken source attribution.
- Do not weaken RCC-N navigation.
- Do not weaken non-claim locks.
- Claim gate remains evidence-bounded.
- Artifact audit checks existence, not truth.
- Schema validation checks contracts, not correctness.
- Modular wrapper is not empirical validation.

---

## Runtime Chain v0.3

The v0.3 wrapper chain is:

    seed
    -> legacy runtime
    -> evidence package
    -> modular claim gate
    -> evidence key audit
    -> artifact path audit
    -> non-claim locks
    -> modular runtime report

This is intentionally conservative.

---

## New Modules

| Module | Role |
|---|---|
| `src/omn/core/contracts.py` | Defines observable, edge, graph, and non-claim contract helpers. |
| `src/omn/core/claim_gate.py` | Computes bounded claim status from evidence. |
| `src/omn/core/artifact_audit.py` | Audits declared artifact paths and evidence keys. |
| `src/omn/core/schema_contracts.py` | Loads lightweight schema contracts and checks required keys. |
| `src/omn/core/modular_runtime.py` | Wraps current runtime and emits modular validation report. |

---

## Validation Surface

Required commands:

    python scripts/validation/validate_modular_runtime.py
    python scripts/validation/validate_architecture_contracts.py
    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests
    python -m omn run --seed synthetic-toy
    python -m omn validate

---

## Falsification Surface

OMN-SA v0.3 is weakened if:

- it rewrites runtime behavior without preserving tests,
- it removes legacy runtime path before modular parity,
- it claims modularization proves correctness,
- it hides missing artifacts,
- it weakens non-claim locks,
- it treats schema validation as truth,
- it treats wrapper validation as empirical validation,
- it claims GMN replication.

---

## Roadmap After v0.3

v0.4 should split graph and evidence internals:

- observables.py
- interactions.py
- graph_contract.py
- residuals.py
- baselines.py
- sensitivity.py
- evidence.py
- ledger.py

v0.5 should deepen topology ensemble sensitivity.

v0.6 should deepen benchmark ladder and claim gate enforcement.

---

## Concluding Compression

OMN-SA v0.1 made OMN runnable.

OMN-SA v0.2 made OMN contract-validated.

OMN-SA v0.3 makes OMN modularization-safe.

The v0.3 law:

    Wrap before rewrite.
    Validate before split.
    Preserve evidence before refactor.
    Keep claims bounded.

The boundary:

    Modular structure is not correctness.
    Contract validation is not truth.
    Runtime success is not empirical validation.