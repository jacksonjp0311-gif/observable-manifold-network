# OMN v1.1 Theory Bridge

## Identity

OMN v1.1 is the Minimal Runtime Bridge and Adoption Layer after OMN v1.0.

It preserves the OMN v1.0 source-bounded extraction from Park et al.'s Generative Manifold Networks and adds the runtime bridge needed to implement a minimal package.

## Runtime Spine

    observables
    -> interaction matrix
    -> typed graph
    -> local manifolds
    -> generators
    -> generated state
    -> residuals
    -> baselines
    -> sensitivity
    -> evidence JSON

## Adoption Spine

    canonical theory
    -> 90-second README
    -> minimal runtime
    -> evidence package
    -> claim gate

## Additive Refinements

OMN v1.1 adds:

- 90-second adoption layer,
- minimal runtime seed contract,
- benchmark ladder,
- graph contract,
- edge confidence and edge status,
- topology ensemble sensitivity,
- residual attribution,
- evidence JSON hardening,
- README / one-page compression,
- implementation-readiness transition R2 to R4.

## Benchmark Ladder

| Class | Meaning |
|---|---|
| S0 | synthetic toy graph |
| S1 | Lorenz-style low-dimensional chaotic seed |
| S2 | paper-inspired benchmark using public data or reproduced setup |
| S3 | artifact/repository graph seed |
| S4 | external dataset benchmark |
| S5 | source-paper replication attempt |

## Claim Boundary

Minimal runtime success proves implementability, not empirical validity.

Edge confidence is not causal certainty.

Simulation is not proof.

Prediction is not mechanism.

Observable topology is not truth.

GMN is not renamed as a Codex invention.

## Update Obligation

If this theory bridge changes, update:

- root README registry section,
- `docs/DOCS_REGISTRY.md`,
- `docs/software_architecture/omn_sa_v0_1_software_architecture.md` if runtime contracts change,
- RCC-N route/index files if navigation changes.