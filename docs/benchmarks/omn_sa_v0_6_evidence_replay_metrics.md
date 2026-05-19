# OMN-SA v0.6 Evidence Replay Metrics

## Checkpoint

Target public checkpoint: `v0.6.1-omn-sa-readme-health-charts`

## Current Validation Metrics

| Surface | Result |
|---|---:|
| Evidence replay | passed |
| Ledger integrity | passed |
| Declared artifacts replayed | 12 / 12 |
| Missing artifacts | 0 |
| Mini README coverage | 37 / 37 |
| RCC-N effectiveness score | 1.000 |
| Regular README baseline | 0.107 |
| Lift over regular README | +0.893 |
| Topology ensemble | passed |
| Edge count spread | 0 |
| Classification flip detected | false |
| Graph engine validation | passed |
| Modular runtime validation | passed |
| Architecture validation | passed |
| RCC-N checker | passed |
| NCI self | 1.000 |
| Unit tests | 34 OK |
| Evidence validation | valid |

## Interpretation

OMN-SA v0.6 changes the system from evidence-emitting to evidence-replayable.

The repository can now:

1. emit evidence,
2. reload latest evidence,
3. verify declared artifacts exist,
4. preserve claim boundaries,
5. append a run ledger record,
6. verify ledger hash-chain integrity,
7. keep RCC-N coverage at 1.0,
8. preserve mini README coverage at 1.0.

## Boundary

These metrics demonstrate local artifact continuity, repository orientation, and replay discipline.

They do not prove code correctness, patch safety, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.