from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List


NON_CLAIM_LOCKS = {
    "simulation_is_not_proof": True,
    "prediction_is_not_mechanism": True,
    "observable_topology_is_not_truth": True,
    "edge_confidence_is_not_causal_certainty": True,
    "schema_validation_is_not_truth": True,
    "ci_passing_is_not_correctness": True,
    "rcc_nexus_is_not_ai_understanding": True,
    "gmn_authorship_preserved": True,
}


@dataclass(frozen=True)
class ObservableNodeContract:
    node_id: str
    observable_name: str
    observable_type: str
    claim_boundary: str = "Observable node does not prove mechanism."

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class TypedEdgeContract:
    source: str
    target: str
    edge_type: str
    weight: float = 0.0
    direction: str = "inferred"
    confidence: float = 0.0
    status: str = "unvalidated"
    claim_boundary: str = "Edge confidence is not causal certainty."

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class GraphContractEnvelope:
    schema: str
    run_id: str
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]
    valid: bool
    failure_flags: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def non_claim_locks() -> Dict[str, bool]:
    return dict(NON_CLAIM_LOCKS)


def minimal_graph_contract(run_id: str, nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]]) -> Dict[str, Any]:
    failure_flags: List[str] = []

    if not nodes:
        failure_flags.append("missing_nodes")

    for node in nodes:
        if not node.get("node_id"):
            failure_flags.append("node_missing_id")
        if not node.get("claim_boundary"):
            failure_flags.append("node_missing_claim_boundary")

    for edge in edges:
        if not edge.get("source") or not edge.get("target"):
            failure_flags.append("edge_missing_endpoint")
        if not edge.get("edge_type"):
            failure_flags.append("edge_missing_type")
        if not edge.get("claim_boundary"):
            failure_flags.append("edge_missing_claim_boundary")

    return GraphContractEnvelope(
        schema="OMN-SA-v0.3-graph-contract-envelope",
        run_id=run_id,
        nodes=nodes,
        edges=edges,
        valid=not failure_flags,
        failure_flags=failure_flags,
    ).to_dict()