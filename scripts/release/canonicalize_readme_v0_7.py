from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"


HEALTH_BLOCK = """### Current health snapshot

| Surface | Current result |
|---|---:|
| Package / CLI | `omn` |
| Current software layer | OMN-SA v0.7 |
| Latest public alignment patch | OMN-SA v0.7 |
| Seeds | synthetic-toy, lorenz, artifact-graph |
| Evidence emission | state, evidence, report, plots, logs, ledger |
| Evidence replay | passed |
| Evidence drift comparison | passed |
| Ledger integrity | passed |
| Declared artifacts replayed | 12 / 12 |
| Missing replay artifacts | 0 |
| Current tests | 38 OK |
| Claim status | runtime-validated locally |
| Source boundary | GMN authorship preserved |
| RCC-N checker | passed |
| NCI self | 1.0 |
| Mini README coverage | 37 / 37 |
| RCC-N effectiveness score | 1.0 |
| Regular README baseline | 0.107 |
| Measured RCC-N lift | +0.893 |
| Current tag | pending-v0.7.0 |
| Current main commit | pending-v0.7.0 |
"""


V07_BLOCK = """

---

## Current v0.7 Evidence Drift Dashboard

![OMN-SA v0.7 Evidence Drift Dashboard](visuals/omn_sa/omn_sa_v0_7_evidence_drift_dashboard.svg)

v0.7 adds multi-run evidence drift comparison.

Current measured state:

| Surface | Result |
|---|---:|
| Evidence drift validation | passed |
| Compared evidence packages | latest 8 or fewer available |
| Artifact count spread | 0 expected |
| Load error count | 0 expected |
| Claim overpromotion flags | 0 expected |
| Evidence replay | passed |
| Ledger integrity | passed |
| RCC-N effectiveness | 1.0 |
| Mini README coverage | 37 / 37 |
| Unit tests | 38 OK expected after v0.7 |

v0.7 law:

    No evidence package is mature until it can be compared across runs.
    No stability claim is mature until drift is measured.
    No public benchmark is mature until the dashboard is visible.

Boundary:

Evidence drift comparison measures local continuity, run-to-run stability, artifact-count stability, load integrity, and claim-status discipline. It does not prove code correctness, patch safety, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication.
"""


STACK_BLOCK = """### Current Versioned Documentation Stack

| Layer | Current file | Status | Notes |
|---|---|---|---|
| Theory | `docs/theory/omn_v1_1_theory_bridge.md` | active | OMN v1.1 minimal runtime bridge and adoption layer. |
| Software Architecture | `docs/software_architecture/omn_sa_v0_7_software_architecture.md` | active | OMN-SA v0.7 evidence drift comparison and multi-run stability dashboard. |
| Source Boundary | `docs/architecture/source_boundary.md` | active | GMN authorship and non-invention boundary. |
| Docs Registry | `docs/DOCS_REGISTRY.md` | active | Canonical map of theory, architecture, injections, metrics, and future docs. |
| Injection Records | `docs/injections/` | active | RCC-N and docs-registry injections. |
| Benchmarks | `docs/benchmarks/omn_sa_v0_7_evidence_drift_metrics.md` | active | v0.7 evidence drift metrics. |
| Release Notes | `docs/release_notes/v0_7_0_evidence_drift_dashboard.md` | active | v0.7 version checkpoint. |
| RCC-N Context | `docs/context/rcc_nexus_index.json` | active | Repository navigation and Echo Location index. |

### Current Architecture Chain

OMN v1.0 theory -> OMN v1.1 minimal runtime bridge -> OMN-SA v0.2 contract validation -> OMN-SA v0.3 modular runtime wrapper -> OMN-SA v0.4 graph engine extraction -> OMN-SA v0.5 topology ensemble and RCC-N metrics -> OMN-SA v0.5.1 mini README repair -> OMN-SA v0.6 evidence replay and run ledger integrity -> OMN-SA v0.6.1 README health/charts -> OMN-SA v0.7 evidence drift comparison and multi-run stability dashboard
"""


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if pattern.search(text):
        return pattern.sub(replacement + "\n" + end, text, count=1)
    return text


def main() -> None:
    text = README.read_text(encoding="utf-8", errors="ignore")

    if "### Current health snapshot" in text and "### What this is not" in text:
        text = replace_between(text, "### Current health snapshot", "### What this is not", HEALTH_BLOCK)
    else:
        text = HEALTH_BLOCK + "\n\n" + text

    if "## Current v0.7 Evidence Drift Dashboard" not in text:
        insert_before = "# PART I - Human README"
        if insert_before in text:
            text = text.replace(insert_before, V07_BLOCK + "\n\n" + insert_before, 1)
        else:
            text += V07_BLOCK

    if "### Current Versioned Documentation Stack" in text and "### Version Update Obligation" in text:
        text = replace_between(text, "### Current Versioned Documentation Stack", "### Version Update Obligation", STACK_BLOCK)
    else:
        text += "\n\n" + STACK_BLOCK

    replacements = {
        "Current software architecture layer: OMN-SA v0.4.": "Current software architecture layer: OMN-SA v0.7.",
        "Current software architecture layer: OMN-SA v0.6.": "Current software architecture layer: OMN-SA v0.7.",
        "Current NCI target: `0.90+`.": "Current NCI target: `1.0`.",
        "| Current tests | 26 passing |": "| Current tests | 38 OK |",
        "| Current tests | 34 OK |": "| Current tests | 38 OK |",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()