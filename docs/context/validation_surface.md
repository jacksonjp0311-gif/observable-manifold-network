# Validation Surface

## Documentation / RCC-N validation

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

## Runtime validation

    python -m omn --help
    python -m omn run --seed synthetic-toy
    python -m omn run --seed lorenz
    python -m omn run --seed artifact-graph
    python -m omn validate

## Evidence boundary

Validation commands prove only local scaffold health for the current implementation. They do not prove causality, mechanism, empirical validity, production readiness, or GMN replication.