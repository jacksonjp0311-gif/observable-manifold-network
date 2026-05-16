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
## v0.2 Patch-Safety Rules

Before committing:

1. Inspect the git diff.
2. Do not perform broad rewrites unless the route map explicitly permits it.
3. Do not mix runtime changes with theory, injection, or documentation-lane changes unless the commit message declares the combined boundary.
4. If a change touches README, RCC-N, docs registry, route map, evidence schema, or validation commands, run:

       python scripts/rcc/check_rcc_nexus.py
       python -m unittest discover -s tests

5. If a change touches runtime behavior, run:

       python -m omn run --seed synthetic-toy
       python -m omn run --seed lorenz
       python -m omn run --seed artifact-graph
       python -m omn validate

6. If preparing release, run:

       powershell -ExecutionPolicy Bypass -File scripts/run_all_checks.ps1
       powershell -ExecutionPolicy Bypass -File scripts/release/fresh_clone_verify.ps1

Boundary:

Passing these checks does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication. It proves only the declared local validation surface.
