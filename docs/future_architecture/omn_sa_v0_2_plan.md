# OMN-SA v0.2 Plan

## Name

OMN-SA v0.2 — CI, Modular Runtime, Schema Validation, and RCC-N Drift Hardening

## Purpose

OMN-SA v0.2 moves the repository from a working v0.1 scaffold into a stronger engineering baseline.

v0.1 proved:

- OMN runtime scaffold can run.
- RCC-N shell can orient agents.
- Evidence packages can be emitted.
- README trisection works.
- Echo Location coverage can be checked.
- Docs registry and lane separation can be maintained.

v0.2 should harden:

- CI,
- modular runtime,
- schema validation,
- evidence validation,
- graph contract tests,
- claim-gate tests,
- RCC-N drift checks,
- release verification.

## v0.2 Software Targets

1. Split `src/omn/core/runtime.py` into modules:

   - observables.py
   - interactions.py
   - graph_contract.py
   - generators.py
   - residuals.py
   - baselines.py
   - sensitivity.py
   - claim_gate.py
   - evidence.py
   - ledger.py

2. Add JSON schema validation for:

   - state artifact,
   - graph contract,
   - evidence package,
   - RCC-N index,
   - route map.

3. Expand test suite toward 20+ tests.

4. Harden RCC-N checker:

   - broken path checks,
   - stale TTL checks,
   - docs registry completeness,
   - chart reference existence,
   - separated docs-lane enforcement.

5. Add CI validation on every push.

## Boundary

v0.2 is engineering hardening.

It does not claim empirical validation, GMN replication, causality, mechanism, biological equivalence, physical manifold identity, production readiness, or AI understanding.