# Release Notes

## Current Version

Current repository checkpoint:

    OMN-SA v0.1 local runtime + RCC-N shell + docs registry

## Version Update Checklist

Every version update must update:

- root README registry section,
- README_90_SECONDS.md,
- docs/DOCS_REGISTRY.md,
- docs/software_architecture/README.md,
- docs/theory/README.md,
- docs/injections/README.md,
- docs/future_architecture/README.md if roadmap changes,
- docs/release_notes/README.md,
- relevant mini READMEs,
- tests if behavior changes,
- evidence contracts if outputs change,
- RCC-N indexes if paths, routes, validation commands, or claim boundaries change.

## v0.1 Registry Injection

Added persistent docs shell for:

- theory,
- software architecture,
- injections,
- future architecture,
- release notes,
- root README update obligation.

Boundary:

    docs registry != code correctness
    architecture docs != empirical validation
    runtime scaffold != full GMN replication

## S — Specification

Versioned release notes.

## H — Hooks

Inbound hooks:

- README.md
- AGENTS.md
- README_90_SECONDS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- Local files in `docs/release_notes`
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

- Shell: center
- Meridian(s): documentation
- Sector: docs
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-19

Local Role:

- Versioned release notes.

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
