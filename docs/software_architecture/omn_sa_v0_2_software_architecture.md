# CODEX ΔΦ — OBSERVABLE MANIFOLD NETWORK SOFTWARE ARCHITECTURE (OMN-SA v0.2)

## CI, Modular Runtime, Schema Validation, and RCC-N Drift Hardening Layer

**Author:** James Paul Jackson  
**X / Twitter:** @unifiedenergy11  
**Date:** May 2026  
**Status:** Canonical v0.2 Software Architecture Hardening Layer

---

## Source / Author Attribution

This document is a Codex-format software architecture evolution derived from and aligned with:

- OMN v1.0 — Observable Manifold Network Theory
- OMN v1.1 — Minimal Runtime Bridge and Adoption Layer
- OMN-SA v0.1 — Minimal Runtime Genesis and Evidence-Gated Observable Graph Layer
- Park et al., “Explainable prediction and simulation of complex system dynamics through networks of manifolds,” bioRxiv preprint, posted May 14, 2026.
- RCC-N repository navigation shell
- Current observable-manifold-network runtime implementation and validation results

Generative Manifold Networks remain Park et al.'s method.

OMN-SA v0.2 does not claim authorship over GMN, Takens embedding, generalized Takens embedding, convergent cross mapping, simplex projection, mutual information, nonlinear cross mapping, reservoir computing, Crossformer comparison, universal approximation proof, Drosophila analysis, Rattus norvegicus analysis, or any empirical result reported by Park et al.

OMN-SA v0.2 is an engineering-hardening architecture, not a new scientific validation claim.

---

## Version

v0.2 — CI, Modular Runtime, Schema Validation, and RCC-N Drift Hardening Layer · Locked ·

Adds:

- CI-backed validation surface
- local all-check script contract
- fresh-clone verification contract
- schema registry
- evidence package schema validation
- graph contract schema validation
- route map schema validation
- RCC-N index schema validation
- documentation-lane separation enforcement
- stronger graph/evidence/RCC tests
- modular runtime target
- release-hardening path
- no-overpromotion locks preserved

---

## Purpose

OMN-SA v0.2 hardens the v0.1 runtime scaffold into a stronger engineering baseline.

v0.1 proved that the repository can:

- run a minimal OMN runtime,
- emit evidence packages,
- validate evidence,
- expose RCC-N navigation,
- pass RCC-N self-checks,
- preserve non-claim locks,
- publish benchmark and public-release docs,
- maintain docs-lane separation.

v0.2 asks the next software question:

How do we make the runtime harder to break, easier to validate, easier to modularize, and safer for AI agents to modify?

---

## What This Is

- A software architecture evolution after OMN-SA v0.1
- A CI and release-validation layer
- A schema-validation layer
- A modular runtime target
- An RCC-N drift-hardening layer
- A stronger docs-lane enforcement layer
- A test expansion layer
- A release-readiness bridge toward v0.3 modularization

---

## What This Is Not

- Not a new OMN theory version
- Not OMN v1.2
- Not a GMN replication
- Not empirical validation
- Not proof of causality
- Not proof of mechanism
- Not proof of biological equivalence
- Not proof of physical manifold identity
- Not proof of production readiness
- Not proof that AI understands the repository
- Not proof that RCC-N navigation equals correctness
- Not permission to weaken source attribution or claim boundaries

---

## Core Extraction

OMN-SA v0.2 extracts the software invariant:

A runtime architecture becomes trustworthy only when its artifacts, schemas, routes, docs lanes, validation commands, and claim gates are themselves testable.

v0.1 law:

    No graph contract, no topology claim.
    No residuals, no evidence.
    No claim gate, no strong claim.

v0.2 adds:

    No schema, no stable contract.
    No CI, no remote validation surface.
    No docs-lane enforcement, no reliable agent navigation.
    No fresh-clone check, no release confidence.

---

## Canonical Lock v0.2

- OMN-SA v0.2 implements OMN v1.1; it does not replace OMN v1.1.
- OMN theory remains locked until software iteration teaches a reusable principle.
- GMN authorship remains with Park et al.
- GMN is not renamed as Codex invention.
- RCC-N improves navigation, not correctness.
- CI passing is not empirical validation.
- Schema validation is not truth.
- Evidence validation is not mechanism.
- Claim gates remain evidence-bounded.
- Topology sensitivity remains required for strong graph claims.
- Baselines must be allowed to win.
- Docs lanes must remain separated:
  - theory
  - software architecture
  - architecture changes
  - injections
  - injected theory
  - future architecture
  - release notes
- AI agents must read context before editing.
- No broad rewrite without route and validation surface.
- Evolutions must remain additive.

---

## Runtime Chain v0.2

The v0.1 runtime chain remains:

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

v0.2 wraps the runtime chain with validation infrastructure:

    source boundary
    -> docs registry
    -> RCC-N route map
    -> schema registry
    -> runtime run
    -> evidence package
    -> schema validation
    -> RCC-N checker
    -> unit tests
    -> fresh-clone verification
    -> release tag

---

## v0.2 System Definition

OMN-SA v0.2 is:

    OMN-SA_v0.2 =
    {
      Runtime,
      Schemas,
      ValidationScripts,
      CI,
      RCCNChecker,
      DocsLaneEnforcer,
      EvidenceValidator,
      Tests,
      ReleaseVerifier
    }

where:

- Runtime is the existing OMN runtime scaffold.
- Schemas define stable object contracts.
- ValidationScripts provide local and CI validation.
- CI gives remote validation surface.
- RCCNChecker validates repository navigation integrity.
- DocsLaneEnforcer preserves documentation ontology.
- EvidenceValidator checks artifact completeness.
- Tests preserve implementation health.
- ReleaseVerifier verifies the repo from a fresh clone.

---

## Required Schema Families

OMN-SA v0.2 requires schema files for:

1. evidence package
2. graph contract
3. route map
4. RCC-N index
5. docs registry
6. claim gate
7. state artifact

Minimal schema contract:

    schema_id
    required_keys
    boundary
    validation_command
    non_claim_lock

Schemas in v0.2 may be lightweight JSON contracts before full JSON Schema Draft compliance. The important requirement is that they are machine-readable and tested.

---

## Modular Runtime Target

OMN-SA v0.2 begins the transition away from a single compact runtime file.

Target modules:

    src/omn/core/runtime.py
    src/omn/core/contracts.py
    src/omn/core/claim_gate.py
    src/omn/core/evidence.py
    src/omn/core/schemas.py
    src/omn/core/validation.py
    src/omn/core/ledger.py

Future v0.3 modules:

    observables.py
    interactions.py
    graph_contract.py
    generators.py
    residuals.py
    baselines.py
    sensitivity.py
    attribution.py

v0.2 does not need to complete the split. It must prepare the contract and tests so v0.3 can split safely.

---

## CI Validation Surface

GitHub Actions must run:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests
    python -m omn run --seed synthetic-toy
    python -m omn validate
    python scripts/validation/validate_architecture_contracts.py

Passing CI means:

- repository navigation is internally consistent,
- tests pass,
- runtime emits evidence,
- latest evidence validates,
- architecture contract files exist.

Passing CI does not mean:

- code is correct in all cases,
- system is production-ready,
- OMN is empirically validated,
- GMN has been replicated,
- causality or mechanism has been proven.

---

## RCC-N Drift Hardening

v0.2 expands RCC-N drift checks conceptually from “presence” to “alignment.”

v0.1 checker validates:

- required files exist,
- README markers exist,
- non-claim locks exist,
- Echo Location blocks exist,
- index exists,
- route map exists.

v0.2 hardening target adds:

- docs lanes exist,
- chart file exists if README embeds it,
- benchmark docs exist if README links them,
- release notes exist,
- architecture docs are registered,
- injection docs are separated from architecture changes,
- injected theory has its own lane,
- route map contains required task types,
- public release boundary is present.

---

## Docs-Lane Contract

OMN-SA v0.2 preserves the lane separation:

| Lane | Path | Role |
|---|---|---|
| Theory | docs/theory/ | Canonical source-bounded theory and theory bridge summaries. |
| Software Architecture | docs/software_architecture/ | Current executable software architecture. |
| Architecture Changes | docs/architecture_changes/ | Versioned structural and runtime architecture changes. |
| Injections | docs/injections/ | Governance/module/documentation injections and HYDRA-style records. |
| Injected Theory | docs/injected_theory/ | Source-bounded theory admitted through declared process. |
| Future Architecture | docs/future_architecture/ | Planned architecture tracks before promotion. |
| Release Notes | docs/release_notes/ | Version continuity and release records. |

Boundary:

- Architecture changes are structural.
- Injections are governance/admission records.
- Injected theory is source-bounded conceptual material.
- Software architecture is current executable design.
- Theory is the canonical conceptual spine.

---

## Evidence Package Hardening

A valid evidence package must include:

- source boundary
- run ID
- seed
- benchmark class
- claim status
- metrics
- artifacts
- baselines
- topology sensitivity
- audit block
- non-claim locks
- failure flags

v0.2 adds schema validation:

    EvidencePackage -> SchemaContract -> RequiredKeys -> Pass/Fail

Invalid evidence package conditions:

- missing claim status,
- missing source boundary,
- missing artifact paths,
- missing non-claim locks,
- missing audit block,
- missing metrics,
- missing baseline/topology fields when claimed.

---

## Release Validation Surface

A release candidate must pass:

    powershell -ExecutionPolicy Bypass -File scripts/run_all_checks.ps1
    powershell -ExecutionPolicy Bypass -File scripts/release/fresh_clone_verify.ps1
    python scripts/validation/validate_architecture_contracts.py

Release readiness is blocked if:

- RCC-N checker fails,
- tests fail,
- evidence validation fails,
- schema contract validation fails,
- fresh clone fails,
- README registry is stale,
- docs lanes are missing,
- non-claim locks are missing.

---

## Tests Required in v0.2

v0.2 requires tests for:

- graph contract typed edges,
- edge claim boundary,
- baseline reporting,
- topology sensitivity reporting,
- claim gate overpromotion blocking,
- README chart embedding,
- docs lane separation,
- route map task types,
- public-release boundary,
- architecture contract presence,
- schema contract presence,
- evidence package schema keys,
- RCC-N index schema keys.

---

## Falsification Surface v0.2

OMN-SA v0.2 is weakened or rejected if:

- it claims to update OMN theory without software evidence,
- it claims CI passing proves correctness,
- it claims schema validation proves truth,
- it hides baseline-equivalent outcomes,
- it weakens source attribution,
- it blends injections with architecture changes,
- it blends injected theory with software architecture,
- it removes non-claim locks,
- it emits evidence without required keys,
- it changes README routes without updating RCC-N index,
- it changes architecture docs without updating docs registry,
- it claims AI understanding from RCC-N orientation.

Compact invalidation rule:

    CI_PASS != correctness
    SCHEMA_PASS != truth
    RCCN_PASS != AI understanding
    EVIDENCE_PASS != empirical validation

---

## Implementation Roadmap

### v0.2.0 — Engineering Hardening

- CI workflow
- all-check script
- fresh-clone verification
- architecture contract validator
- schema contracts
- stronger tests
- docs-lane enforcement
- v0.2 architecture document

### v0.2.1 — Schema Hardening

- full JSON schema validation
- schema test fixtures
- invalid evidence package tests
- route map schema checks

### v0.3.0 — Modular Runtime

- split runtime into modules
- maintain backward-compatible CLI
- preserve evidence output
- add module-level READMEs

### v0.4.0 — Topology Ensemble Engine

- real threshold sweep
- driver count sweep
- edge stability matrix
- topology spread report

### v0.5.0 — Benchmark Ladder Engine

- S0-S5 runner
- benchmark class enforcement
- claim gate tied to benchmark class

### v1.0.0 — Stable AI-Orientable Runtime

- CI
- schemas
- modular runtime
- evidence packages
- docs registry
- RCC-N navigation
- release tags
- public-safe framing

---

## Public Framing

OMN-SA v0.2 is an engineering-hardening layer for an AI-orientable observable-topology runtime.

It makes the repository:

- easier to validate,
- easier to navigate,
- easier to release,
- easier to patch safely,
- harder to overclaim.

It does not prove:

- causality,
- mechanism,
- GMN replication,
- empirical validity,
- AI understanding,
- code correctness,
- production readiness.

Short description:

    Validate the contracts.
    Harden the routes.
    Check the schemas.
    Preserve the locks.
    Then evolve the runtime.

---

## Concluding Compression

OMN-SA v0.1 made OMN runnable.

OMN-SA v0.2 makes OMN harder to break.

The v0.2 software law is:

    No schema, no stable contract.
    No CI, no remote validation surface.
    No docs-lane enforcement, no reliable AI orientation.
    No fresh-clone check, no release confidence.

The v0.2 boundary law is:

    CI is not correctness.
    Schema validation is not truth.
    RCC-N is not AI understanding.
    Evidence validation is not empirical proof.

Therefore OMN-SA v0.2 is the correct next software architecture layer before deeper runtime modularization or OMN theory evolution.