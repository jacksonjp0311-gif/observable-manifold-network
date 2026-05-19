from __future__ import annotations

import re
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


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if pattern.search(text):
        return pattern.sub(replacement + "\n" + end, text, count=1)
    return text


def main() -> None:
    text = README.read_text(encoding="utf-8", errors="ignore")

    health = """### Current health snapshot

| Surface | Current result |
|---|---:|
| Package / CLI | `omn` |
| Current software layer | OMN-SA v0.8 |
| Latest public alignment patch | OMN-SA v0.8 |
| Seeds | synthetic-toy, lorenz, artifact-graph |
| Evidence emission | state, evidence, report, plots, logs, ledger |
| Evidence replay | passed |
| Evidence drift comparison | passed |
| Metric availability | passed |
| Ledger integrity | passed |
| Declared artifacts replayed | 12 / 12 |
| Missing replay artifacts | 0 |
| Current tests | pending-v0.8 |
| Claim status | runtime-validated locally |
| Source boundary | GMN authorship preserved |
| RCC-N checker | passed |
| RCC-N v1.7 profile checker | passed |
| RCC-N selected profile | Full |
| RCC-N governance need | 0.5375 |
| GEN boundary | GEN-R, not full GEN v1.0 |
| NCI self | 1.0 |
| Mini README coverage | 37 / 37 |
| RCC-N effectiveness score | 0.9822222222 |
| Regular README baseline | 0.107 |
| Measured RCC-N lift | +0.8752222222 |
| Current tag | pending-v0.8.0 |
| Current main commit | pending-v0.8.0 |
"""

    if "### Current health snapshot" in text and "### What this is not" in text:
        text = replace_between(text, "### Current health snapshot", "### What this is not", health)
    else:
        text = health + "\n\n" + text

    if "## Current v0.8 Metric Availability and Residual Field Hardening" not in text:
        insert_before = "# PART I - Human README"
        if insert_before in text:
            text = text.replace(insert_before, V08_BLOCK + "\n\n" + insert_before, 1)
        else:
            text += V08_BLOCK

    if "OMN-SA v0.8 metric availability and residual field hardening" not in text:
        text += "\n\nCurrent architecture chain extension: OMN-SA v0.8 metric availability and residual field hardening.\n"

    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()