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