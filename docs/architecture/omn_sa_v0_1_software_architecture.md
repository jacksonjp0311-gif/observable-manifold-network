# OMN-SA v0.1 Software Architecture

Runtime chain:

    input
    -> observables
    -> interaction matrix
    -> typed graph
    -> generated state
    -> residuals
    -> baselines
    -> sensitivity
    -> claim gate
    -> evidence

First seeds:

- synthetic-toy
- lorenz
- artifact-graph

Core locks:

- OMN is not GMN.
- GMN authorship remains with Park et al.
- Observable topology is not truth.
- Prediction is not mechanism.
- Simulation is not proof.
- Edge confidence is not causal certainty.