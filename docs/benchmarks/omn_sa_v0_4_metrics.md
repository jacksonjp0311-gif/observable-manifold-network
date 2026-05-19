# OMN-SA v0.4 Metrics Snapshot

## Checkpoint

`v0.4.0-omn-sa-graph-engine`

## Current Validation Metrics

| Surface | Result |
|---|---:|
| Graph engine validation | passed |
| Modular runtime validation | passed |
| Architecture validation | passed |
| RCC-N checker | passed |
| NCI self | 1.0 |
| Unit tests | 26 passing |
| Runtime seed | synthetic-toy runtime-validated |
| Evidence validation | valid |
| Graph observables | 3 |
| Graph edges | 6 |
| Graph parity | passed |
| Current commit | 08c781e |
| Current tag | v0.4.0-omn-sa-graph-engine |

## v0.4 Interpretation

OMN-SA v0.4 is the first extracted runtime subsystem. It moves graph-related behavior into dedicated modules while preserving the legacy evidence path.

## v0.4 Law

    No split without parity.
    No parity without evidence.
    No evidence without validation.

## Boundary

These metrics demonstrate local validation, graph-contract extraction, and repository orientation discipline.

They do not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.