# CODEX ΔΦ — OBSERVABLE MANIFOLD NETWORK SOFTWARE ARCHITECTURE (OMN-SA v0.8)

## Metric Availability and Residual Field Hardening

Author: James Paul Jackson  
X / Twitter: @unifiedenergy11  
Date: May 2026  
Status: Canonical v0.8 software architecture implementation layer

---

## Purpose

OMN-SA v0.8 repairs the measured weakness exposed by v0.7 evidence drift comparison:

- rmse unavailable across compared evidence packages,
- mae unavailable across compared evidence packages,
- delta_phi_residual unavailable across compared evidence packages,
- omega_residual_weight unavailable across compared evidence packages.

The metrics were already computed in runtime, but the evidence packages did not expose the canonical nested metric fields expected by the evidence drift comparator.

## v0.8 Law

A metric is not available until the evidence package exposes it where validators expect it.

A residual is not mature until it is named consistently across runtime, evidence, drift, and report surfaces.

## Adds

- canonical nested evidence metric schema,
- backward-compatible evidence drift metric extraction,
- residual-field availability validator,
- metric availability report,
- public v0.8 chart,
- README v0.8 dashboard section,
- tests proving new evidence packages expose residual fields.

## Canonical Metric Schema

Example structure:

    {
      "metrics": {
        "validation": {
          "rmse": 0.0,
          "mae": 0.0,
          "correlation": 0.0,
          "delta_phi_residual": 0.0,
          "omega_residual_weight": 1.0
        },
        "baseline": {
          "rmse": 0.0,
          "mae": 0.0,
          "correlation": 0.0,
          "delta_phi_residual": 0.0,
          "omega_residual_weight": 1.0,
          "baseline_equivalent": false
        },
        "legacy": {
          "rmse": 0.0,
          "mae": 0.0,
          "correlation": 0.0,
          "delta_phi_omn": 0.0,
          "omega_omn": 1.0
        }
      }
    }

## What This Is

- Evidence schema hardening.
- Residual metric availability repair.
- Backward-compatible drift extraction.
- Public metric availability dashboard.

## What This Is Not

- Not empirical validation.
- Not GMN replication.
- Not proof of causality.
- Not proof of mechanism.
- Not code correctness proof.
- Not production readiness.
- Not proof of AI understanding.

## Boundary

Metric availability means the evidence package exposes computable residual fields. It does not prove that the model is correct, useful, externally validated, causal, mechanistic, or superior to baselines.