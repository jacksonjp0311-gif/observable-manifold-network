from __future__ import annotations

from typing import Any, Dict, List

from omn.core.graph_engine import build_graph_engine_state


def run_threshold_ensemble(columns: Dict[str, List[float]], run_id: str, thresholds: List[float]) -> Dict[str, Any]:
    graph_states = []
    edge_counts = []
    edge_frequency: Dict[str, int] = {}

    for threshold in thresholds:
        state = build_graph_engine_state(columns, f"{run_id}_t_{threshold}", threshold=threshold)
        graph_states.append({
            "threshold": threshold,
            "edge_count": state["edge_count"],
            "valid": state["graph_contract"]["valid"],
        })
        edge_counts.append(state["edge_count"])

        for edge in state["graph_contract"]["edges"]:
            key = f"{edge['source']}->{edge['target']}:{edge['edge_type']}"
            edge_frequency[key] = edge_frequency.get(key, 0) + 1

    k = len(thresholds) or 1
    edge_stability = {key: value / k for key, value in edge_frequency.items()}

    spread = max(edge_counts) - min(edge_counts) if edge_counts else 0
    classification_flip_detected = spread > 0

    return {
        "schema": "OMN-SA-v0.5-topology-ensemble",
        "run_id": run_id,
        "thresholds": thresholds,
        "graph_states": graph_states,
        "edge_stability": edge_stability,
        "edge_count_spread": spread,
        "classification_flip_detected": classification_flip_detected,
        "passed": all(item["valid"] for item in graph_states),
        "boundary": "Topology ensemble measures graph stability under policy perturbation. It does not prove causality, mechanism, empirical validation, production readiness, AI understanding, or GMN replication.",
    }