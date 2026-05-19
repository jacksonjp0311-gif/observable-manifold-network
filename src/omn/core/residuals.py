from __future__ import annotations

import math
from typing import Dict, List


def rmse(observed: List[float], generated: List[float]) -> float:
    n = min(len(observed), len(generated))
    if n == 0:
        return 0.0
    return math.sqrt(sum((observed[i] - generated[i]) ** 2 for i in range(n)) / n)


def mae(observed: List[float], generated: List[float]) -> float:
    n = min(len(observed), len(generated))
    if n == 0:
        return 0.0
    return sum(abs(observed[i] - generated[i]) for i in range(n)) / n


def delta_phi_mean_abs(observed: List[float], generated: List[float]) -> float:
    return mae(observed, generated)


def omega_from_delta_phi(delta_phi: float) -> float:
    return 1.0 / (1.0 + abs(float(delta_phi)))


def residual_record(observed: List[float], generated: List[float]) -> Dict[str, float]:
    dphi = delta_phi_mean_abs(observed, generated)
    return {
        "rmse": rmse(observed, generated),
        "mae": mae(observed, generated),
        "delta_phi": dphi,
        "omega": omega_from_delta_phi(dphi)
    }