from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"

V08_BLOCK = """

---

## Current v0.8 Metric Availability and Residual Field Hardening

![OMN-SA v0.8 Metric Availability](visuals/omn_sa/omn_sa_v0_8_metric_availability.svg)

v0.8 repairs the metric availability weakness exposed by v0.7 evidence drift.

Current metric availability target:

| Metric | Required path |
|---|---|
| rmse | metrics.validation.rmse |
| mae | metrics.validation.mae |
| delta_phi_residual | metrics.validation.delta_phi_residual |
| omega_residual_weight | metrics.validation.omega_residual_weight |

v0.8 law:

    A metric is not available until the evidence package exposes it where validators expect it.
    A residual is not mature until it is named consistently across runtime, evidence, drift, and report surfaces.

Boundary:

Metric availability means residual fields are exposed for comparison. It does not prove code correctness, patch safety, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
"""

def main() -> None:
    text = README.read_text(encoding="utf-8", errors="ignore")

    if "## Current v0.8 Metric Availability and Residual Field Hardening" not in text:
        insert_before = "# PART I - Human README"
        if insert_before in text:
            text = text.replace(insert_before, V08_BLOCK + "\n\n" + insert_before, 1)
        else:
            text += V08_BLOCK

    if "OMN-SA v0.8 metric availability and residual field hardening" not in text:
        text += "\n\nOMN-SA v0.8 metric availability and residual field hardening.\n"

    README.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()