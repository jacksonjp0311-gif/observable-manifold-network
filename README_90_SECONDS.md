# OMN in 90 Seconds

Observable Manifold Network is a local-first observable-topology runtime.

It preserves the GMN-style spine:

    observables
    -> interaction matrix
    -> typed graph
    -> generated state

It adds Codex governance:

    residuals
    -> baselines
    -> topology sensitivity
    -> claim gate
    -> evidence package

It now uses the AERMA/RCC-N README shell:

    PART I - Human README
    PART II - RCC Nexus README
    PART III - AI Agent README

Run:

    $env:PYTHONPATH = "$PWD\src"
    python -m omn run --seed synthetic-toy
    python -m unittest discover -s tests
    python scripts/rcc/check_rcc_nexus.py

Core rule:

    No graph contract, no topology claim.
    No residuals, no evidence.
    No claim gate, no strong claim.
    No route map, no agent-safe patch.