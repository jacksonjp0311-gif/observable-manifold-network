# OMN-SA v0.9.3 Architecture Change — README / Registry Autopatcher

## Change Type

Version-surface governance and release-orientation hardening.

## What Changed

- Added a reusable version-surface checker.
- Added tests for required README/registry/CI zones.
- Updated README current state, documentation stack, architecture chain, and CI markers.
- Added a release note and architecture document for v0.9.3.

## Why

The repository repeatedly learned that version drift occurs when one current-state surface updates while another stays stale. v0.9.3 turns that lesson into an explicit release check.

## Boundary

This change improves release hygiene. It does not change scientific claim boundaries.
