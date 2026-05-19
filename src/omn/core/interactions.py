from __future__ import annotations

import math
from typing import Any, Dict, List


def pearson(x: List[float], y: List[float]) -> float:
    n = min(len(x), len(y))
    if n < 2:
        return 0.0

    xs = x[:n]
    ys = y[:n]
    mx = sum(xs) / n
    my = sum(ys) / n

    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den_x = math.sqrt(sum((a - mx) ** 2 for a in xs))
    den_y = math.sqrt(sum((b - my) ** 2 for b in ys))

    if den_x == 0 or den_y == 0:
        return 0.0

    return num / (den_x * den_y)


def compute_interaction_matrix(observables: List[Dict[str, Any]], method: str = "correlation") -> Dict[str, Any]:
    names = [obs["name"] for obs in observables]
    matrix: List[List[float]] = []

    for left in observables:
        row: List[float] = []
        for right in observables:
            if left["name"] == right["name"]:
                row.append(1.0)
            else:
                row.append(float(pearson(left.get("values", []), right.get("values", []))))
        matrix.append(row)

    return {
        "schema": "OMN-SA-v0.4-interaction-matrix",
        "method": method,
        "names": names,
        "matrix": matrix,
        "boundary": "Interaction weights are association scores. They do not prove causality or mechanism."
    }


def matrix_edges(interaction_matrix: Dict[str, Any], threshold: float = 0.25) -> List[Dict[str, Any]]:
    names = interaction_matrix.get("names", [])
    matrix = interaction_matrix.get("matrix", [])
    edges: List[Dict[str, Any]] = []

    for i, source in enumerate(names):
        for j, target in enumerate(names):
            if i == j:
                continue
            try:
                weight = float(matrix[i][j])
            except (IndexError, TypeError, ValueError):
                weight = 0.0

            if abs(weight) >= threshold:
                edges.append({
                    "source": source,
                    "target": target,
                    "edge_type": interaction_matrix.get("method", "correlation"),
                    "weight": weight,
                    "direction": "inferred",
                    "confidence": min(1.0, abs(weight)),
                    "status": "computed",
                    "claim_boundary": "Edge confidence is not causal certainty."
                })

    return edges