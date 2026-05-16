# AGENTS.md - Observable Manifold Network Agent Contract

## Entry Order

1. Read `README.md`.
2. Read `README_90_SECONDS.md`.
3. Read `docs/context/repository_context_index.json`.
4. Read `docs/context/rcc_nexus_index.json`.
5. Read `rcc/nexus/route_map.json`.
6. Read the target folder README.
7. Inspect relevant source and tests.
8. Run validation before claiming behavior changed.

## Patch Rule

Patch the smallest necessary surface.

## Validation Rule

For documentation / RCC changes:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

For runtime changes:

    python -m omn run --seed synthetic-toy
    python -m omn run --seed lorenz
    python -m omn run --seed artifact-graph
    python -m unittest discover -s tests

## Non-Claim Lock

Do not claim causality, mechanism, empirical validation, biological equivalence, physical manifold identity, production readiness, or full GMN replication.