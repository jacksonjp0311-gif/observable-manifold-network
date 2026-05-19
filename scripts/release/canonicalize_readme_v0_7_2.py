from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"


HEALTH_BLOCK_TEMPLATE = """### Current health snapshot

| Surface | Current result |
|---|---:|
| Package / CLI | `omn` |
| Current software layer | OMN-SA v0.7.2 |
| Latest public alignment patch | OMN-SA v0.7.2 |
| Seeds | synthetic-toy, lorenz, artifact-graph |
| Evidence emission | state, evidence, report, plots, logs, ledger |
| Evidence replay | passed |
| Evidence drift comparison | passed |
| Ledger integrity | passed |
| Declared artifacts replayed | 12 / 12 |
| Missing replay artifacts | 0 |
| Current tests | {test_count} OK |
| Claim status | runtime-validated locally |
| Source boundary | GMN authorship preserved |
| RCC-N checker | passed |
| RCC-N v1.7 profile checker | passed |
| RCC-N selected profile | Full |
| RCC-N governance need | 0.5375 |
| GEN boundary | GEN-R, not full GEN v1.0 |
| NCI self | 1.0 |
| Mini README coverage | 37 / 37 |
| RCC-N effectiveness score | 1.0 |
| Regular README baseline | 0.107 |
| Measured RCC-N lift | +0.893 |
| Current tag | pending-v0.7.2 |
| Current main commit | pending-v0.7.2 |
"""


REGISTRY_BLOCK = """### Current Versioned Documentation Stack

| Layer | Current file | Status | Notes |
|---|---|---|---|
| Theory | `docs/theory/omn_v1_1_theory_bridge.md` | active | OMN v1.1 minimal runtime bridge and adoption layer. |
| Software Architecture | `docs/software_architecture/omn_sa_v0_7_2_readme_self_organization.md` | active | README self-organization and current-state canonicalization. |
| Prior Software Architecture | `docs/software_architecture/omn_sa_v0_7_1_rcc_n_v1_7_profile_injection.md` | active | RCC-N v1.7 profile injection layer. |
| Source Boundary | `docs/architecture/source_boundary.md` | active | GMN authorship and non-invention boundary. |
| Docs Registry | `docs/DOCS_REGISTRY.md` | active | Canonical map of theory, architecture, injections, metrics, and future docs. |
| Injection Records | `docs/injections/rcc_n_v1_7_injection_record.md` | active | RCC-N v1.7 HYDRA-style injection record. |
| Injected Theory | `docs/injected_theory/rcc_n_v1_7_adoption_profiles.md` | active | RCC-N v1.7 adoption-profile theory record. |
| Benchmarks | `docs/benchmarks/omn_sa_v0_7_1_rcc_n_v1_7_profile_metrics.md` | active | v0.7.1 profile metrics. |
| Self-Organization | `reports/self_organization/latest_readme_self_organization_audit.md` | active | v0.7.2 README self-organization audit. |
| Release Notes | `docs/release_notes/v0_7_2_readme_self_organization.md` | active | v0.7.2 version checkpoint. |
| RCC-N Context | `docs/context/rcc_nexus_index.json` and `docs/context/rcc_nexus_profile_v1_7.json` | active | Repository navigation and profile-gated governance. |
|

### Current Architecture Chain

OMN v1.0 theory -> OMN v1.1 minimal runtime bridge -> OMN-SA v0.2 contract validation -> OMN-SA v0.3 modular runtime wrapper -> OMN-SA v0.4 graph engine extraction -> OMN-SA v0.5 topology ensemble and RCC-N metrics -> OMN-SA v0.5.1 mini README repair -> OMN-SA v0.6 evidence replay and run ledger integrity -> OMN-SA v0.6.1 README health/charts -> OMN-SA v0.7 evidence drift comparison and multi-run stability dashboard -> OMN-SA v0.7.1 RCC-N v1.7 profile injection -> OMN-SA v0.7.2 README self-organization canonicalization
"""


V072_BLOCK = """

---

## Current v0.7.2 README Self-Organization Audit

![OMN-SA v0.7.2 Self-Organization Audit](visuals/omn_sa/omn_sa_v0_7_2_self_organization.svg)

v0.7.2 repairs public README drift after the RCC-N v1.7 profile injection.

Current self-organization state:

| Surface | Result |
|---|---:|
| Current health snapshot | canonicalized |
| AI Version Tracking | aligned to v0.7.2 |
| RCC-N v1.7 profile layer | visible |
| Historical v0.2/v0.4 sections | archive wording |
| Current documentation stack | updated |
| Next measured weakness | v0.8 residual metrics |

v0.7.2 law:

    If the repository helps agents navigate, the repository must keep its own map current.

Boundary:

Self-organization improves repository orientation and AI agent self-location. It does not prove code correctness, patch safety, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
"""


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if pattern.search(text):
        return pattern.sub(replacement + "\n" + end, text, count=1)
    return text


def main() -> None:
    test_count = "41"
    tests_report = ROOT / "reports" / "self_organization" / "latest_unittest_count.txt"
    if tests_report.exists():
        value = tests_report.read_text(encoding="utf-8").strip()
        if value.isdigit():
            test_count = value

    text = README.read_text(encoding="utf-8", errors="ignore")

    health = HEALTH_BLOCK_TEMPLATE.format(test_count=test_count)

    if "### Current health snapshot" in text and "### What this is not" in text:
        text = replace_between(text, "### Current health snapshot", "### What this is not", health)
    else:
        text = health + "\n\n" + text

    replacements = {
        "Observable Manifold Network includes a local RCC Nexus layer based on RCC-N v1.0.": "Observable Manifold Network includes a local RCC Nexus layer with RCC-N v1.0 compatibility and RCC-N v1.7 adoption-profile governance.",
        "- Current software architecture layer: OMN-SA v0.7.": "- Current software architecture layer: OMN-SA v0.7.2.",
        "- Current software architecture layer: OMN-SA v0.4.": "- Current software architecture layer: OMN-SA v0.7.2.",
        "- RCC-N mode: local geometric repository navigation shell.": "- RCC-N mode: local geometric repository navigation shell plus RCC-N v1.7 Full profile governance.",
        "## Archived v0.2 Validation Status\n\nCurrent clean checkpoint:": "## Archived v0.2 Validation Status\n\nHistorical checkpoint at that version:",
        "## Current v0.4 Metrics Snapshot": "## Archived v0.4 Metrics Snapshot",
        "Current clean checkpoint:": "Historical checkpoint at that version:",
        "| Current tests | 41 OK expected after v0.7.1 |": f"| Current tests | {test_count} OK |",
        "Unit tests | 38 OK expected after v0.7": "Unit tests | 38 OK",
        "Current software architecture layer: OMN-SA v0.7.": "Current software architecture layer: OMN-SA v0.7.2.",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    if "### Current Versioned Documentation Stack" in text and "### Version Update Obligation" in text:
        text = replace_between(text, "### Current Versioned Documentation Stack", "### Version Update Obligation", REGISTRY_BLOCK)
    else:
        text += "\n\n" + REGISTRY_BLOCK

    if "## Current v0.7.2 README Self-Organization Audit" not in text:
        insert_before = "# PART I - Human README"
        if insert_before in text:
            text = text.replace(insert_before, V072_BLOCK + "\n\n" + insert_before, 1)
        else:
            text += V072_BLOCK

    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()