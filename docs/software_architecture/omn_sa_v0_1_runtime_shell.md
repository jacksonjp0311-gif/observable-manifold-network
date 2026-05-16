# OMN-SA v0.1 Runtime Shell

## Runtime chain

    observables
    -> interaction matrix
    -> typed graph
    -> generated state
    -> residuals
    -> baselines
    -> topology sensitivity
    -> claim gate
    -> evidence package

## Current package

    src/omn/

## Current CLI

    python -m omn --help
    python -m omn run --seed synthetic-toy
    python -m omn run --seed lorenz
    python -m omn run --seed artifact-graph
    python -m omn validate

## Architecture boundary

This is a minimal runtime scaffold. It is not full GMN replication or empirical validation.