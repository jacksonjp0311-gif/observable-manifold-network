from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, Iterable, List, Sequence


@dataclass(frozen=True)
class ObservableSeries:
    name: str
    values: List[float]
    observable_type: str = "synthetic"
    claim_boundary: str = "Observable series does not prove mechanism."

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def coerce_numeric_series(name: str, values: Iterable[Any], observable_type: str = "synthetic") -> ObservableSeries:
    coerced: List[float] = []
    for value in values:
        try:
            coerced.append(float(value))
        except (TypeError, ValueError):
            continue
    return ObservableSeries(name=name, values=coerced, observable_type=observable_type)


def build_observable_set(columns: Dict[str, Sequence[Any]], observable_type: str = "synthetic") -> List[Dict[str, Any]]:
    observables: List[Dict[str, Any]] = []
    for name, values in columns.items():
        series = coerce_numeric_series(name, values, observable_type=observable_type)
        if series.values:
            observables.append(series.to_dict())
    return observables


def validate_observables(observables: List[Dict[str, Any]]) -> Dict[str, Any]:
    failures: List[str] = []
    names = set()

    for obs in observables:
        name = obs.get("name")
        values = obs.get("values", [])
        if not name:
            failures.append("observable_missing_name")
        if name in names:
            failures.append(f"duplicate_observable:{name}")
        names.add(name)
        if not values:
            failures.append(f"observable_missing_values:{name}")
        if not obs.get("claim_boundary"):
            failures.append(f"observable_missing_claim_boundary:{name}")

    return {
        "schema": "OMN-SA-v0.4-observable-validation",
        "passed": not failures,
        "count": len(observables),
        "failure_flags": failures,
        "boundary": "Observable validation checks declared series structure, not truth or mechanism."
    }