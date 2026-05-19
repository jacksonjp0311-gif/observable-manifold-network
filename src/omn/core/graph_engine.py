from __future__ import annotations

from typing import Any, Dict, List

from omn.core.contracts import minimal_graph_contract
from omn.core.interactions import compute_interaction_matrix, matrix_edges
from omn.core.observables import build_observable_set, validate_observables


def build_graph_engine_state(columns: Dict[str, List[float]], run_id: str, threshold: float = 0.25) -> Dict[str, Any]:
    observables = build_observable_set(columns)
    observable_validation = validate_observables(observables)
    interaction_matrix = compute_interaction_matrix(observables)
    edges = matrix_edges(interaction_matrix, threshold=threshold)

    node_records = []
    for obs in observables:
        node_records.append({
            "node_id": obs["name"],
            "observable_name": obs["name"],
            "observable_type": obs.get("observable_type", "synthetic"),
            "claim_boundary": obs.get("claim_boundary", "Observable node does not prove mechanism.")
        })

    graph_contract = minimal_graph_contract(run_id=run_id, nodes=node_records, edges=edges)

    return {
        "schema": "OMN-SA-v0.4-graph-engine-state",
        "run_id": run_id,
        "observables": observables,
        "observable_validation": observable_validation,
        "interaction_matrix": interaction_matrix,
        "graph_contract": graph_contract,
        "edge_count": len(edges),
        "boundary": "Graph engine state is an explainability scaffold. It does not prove causality, mechanism, empirical validation, or GMN replication."
    }


def graph_engine_parity_summary(legacy_evidence: Dict[str, Any], graph_state: Dict[str, Any]) -> Dict[str, Any]:
    legacy_has_graph = bool(legacy_evidence.get("artifacts", {}).get("graph_contract") or legacy_evidence.get("graph_contract"))
    modular_has_graph = bool(graph_state.get("graph_contract", {}).get("valid", False))

    return {
        "schema": "OMN-SA-v0.4-graph-engine-parity",
        "legacy_has_graph_surface": legacy_has_graph,
        "modular_graph_contract_valid": modular_has_graph,
        "edge_count": graph_state.get("edge_count", 0),
        "passed": modular_has_graph,
        "boundary": "Parity summary checks preservation of graph-contract surfaces, not scientific validity."
    }