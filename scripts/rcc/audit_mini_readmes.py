from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[2]

MAJOR_DIRS = [
    "configs",
    "docs",
    "docs/architecture",
    "docs/architecture_changes",
    "docs/benchmarks",
    "docs/context",
    "docs/future_architecture",
    "docs/injected_theory",
    "docs/injections",
    "docs/protocols",
    "docs/public_release",
    "docs/release_notes",
    "docs/software_architecture",
    "docs/theory",
    "examples",
    "outputs",
    "rcc",
    "rcc/nexus",
    "reports",
    "reports/architecture",
    "reports/graph_engine",
    "reports/modular_runtime",
    "reports/rcc_nexus",
    "schemas",
    "schemas/omn",
    "schemas/rcc_nexus",
    "scripts",
    "scripts/rcc",
    "scripts/release",
    "scripts/validation",
    "src",
    "src/omn",
    "src/omn/core",
    "tests",
    "visuals",
    "visuals/rcc_nexus",
    "visuals/omn_sa",
]

REQUIRED_MARKERS = [
    "## S — Specification",
    "## H — Hooks",
    "## A — Artifacts",
    "## T — Theory / Basis",
    "## I — Invariants",
    "## E — Examples",
    "## RCC Nexus Echo Location",
    "Claim Boundary",
    "Non-Claim Locks",
]

NON_CLAIM_BOUNDARY = (
    "This mini README improves local navigation and agent orientation. "
    "It does not prove code correctness, patch safety, empirical validation, "
    "causality, mechanism, AI understanding, production readiness, or GMN replication."
)


def normalize_rel(path: str) -> str:
    return path.replace("\\", "/")


def purpose_for(path: str) -> str:
    path = normalize_rel(path)
    mapping = {
        "configs": "Runtime and seed configuration surface.",
        "docs": "Repository documentation, theory, architecture, benchmarks, and governance surface.",
        "docs/architecture": "Architecture-level repository context and structural contracts.",
        "docs/architecture_changes": "Versioned architecture-change records.",
        "docs/benchmarks": "Benchmark and metric reporting surface.",
        "docs/context": "RCC/RCC-N context indexes, validation surfaces, and drift records.",
        "docs/future_architecture": "Forward-looking architecture plans and staged roadmap surfaces.",
        "docs/injected_theory": "Injected theory records and governed theory-transfer surface.",
        "docs/injections": "RCC/RCC-N and governance injection records.",
        "docs/protocols": "Operating protocols, claim gates, and validation procedures.",
        "docs/public_release": "Public release summaries and publishable context surfaces.",
        "docs/release_notes": "Versioned release notes.",
        "docs/software_architecture": "OMN-SA software architecture lineage.",
        "docs/theory": "Canonical OMN theory and source-anchor documents.",
        "examples": "Runnable seed examples and usage entry points.",
        "outputs": "Generated runtime outputs, evidence, reports, logs, and ledgers.",
        "rcc": "Repository Context Canon and RCC-N support surface.",
        "rcc/nexus": "RCC-N route maps, Echo Location protocol, and agent handoff surface.",
        "reports": "Generated reports and validation records.",
        "reports/architecture": "Architecture validation reports.",
        "reports/graph_engine": "Graph-engine validation reports.",
        "reports/modular_runtime": "Modular runtime validation reports.",
        "reports/rcc_nexus": "RCC-N checker and measurement reports.",
        "schemas": "Schema definitions and validation contracts.",
        "schemas/omn": "OMN evidence and runtime schemas.",
        "schemas/rcc_nexus": "RCC-N route-map and context schemas.",
        "scripts": "Automation, validation, release, and RCC utility scripts.",
        "scripts/rcc": "RCC-N checker, mini README repair, and metrics scripts.",
        "scripts/release": "Release and verification scripts.",
        "scripts/validation": "Validation entry points for architecture and runtime surfaces.",
        "src": "Python source tree.",
        "src/omn": "OMN Python package.",
        "src/omn/core": "Executable OMN runtime core and modular graph-engine surfaces.",
        "tests": "Implementation-health validation surface.",
        "visuals": "Public chart and visual evidence surface.",
        "visuals/rcc_nexus": "RCC-N public metric charts.",
        "visuals/omn_sa": "OMN-SA public metric charts.",
    }
    return mapping.get(path, f"Local context surface for `{path}`.")


def shell_for(path: str) -> str:
    path = normalize_rel(path)
    if path.startswith("src") or path.startswith("schemas"):
        return "inner"
    if path.startswith("scripts") or path.startswith("tests") or path.startswith("configs"):
        return "middle"
    if path.startswith("outputs") or path.startswith("reports") or path.startswith("visuals"):
        return "outer"
    if path.startswith("docs") or path.startswith("rcc"):
        return "center"
    return "middle"


def meridians_for(path: str) -> str:
    path = normalize_rel(path)
    meridians = []
    if "docs" in path:
        meridians.append("documentation")
    if "rcc" in path:
        meridians.append("agent")
        meridians.append("drift")
    if "src" in path:
        meridians.append("runtime")
        meridians.append("graph")
    if "test" in path or "validation" in path:
        meridians.append("validation")
    if "outputs" in path or "reports" in path or "visuals" in path:
        meridians.append("evidence")
    if "schema" in path:
        meridians.append("schema")
    if "config" in path:
        meridians.append("configuration")
    if not meridians:
        meridians.append("documentation")
    return ", ".join(sorted(set(meridians)))


def local_block(rel: str) -> str:
    top = normalize_rel(rel).split("/")[0] if rel else "root"
    return f"""
## S — Specification

{purpose_for(rel)}

## H — Hooks

Inbound hooks:

- README.md
- AGENTS.md
- README_90_SECONDS.md
- docs/context/repository_context_index.json
- docs/context/rcc_nexus_index.json
- rcc/nexus/route_map.json

Outbound hooks:

- Local files in `{normalize_rel(rel)}`
- Validation reports when this folder participates in runtime, documentation, release, or RCC checks

## A — Artifacts

This folder may contain source files, docs, reports, schemas, scripts, visuals, generated state, or validation records depending on its role.

## T — Theory / Basis

Governed by OMN v1.1, OMN-SA, RCC-N, and the repository non-claim locks.

## I — Invariants

- Preserve source attribution.
- Preserve non-claim boundaries.
- Do not treat navigation as validation.
- Do not treat documentation as correctness.
- Do not claim GMN replication without benchmark conditions.
- Keep evidence and validation surfaces inspectable.

## E — Examples

Read this file before editing this folder.

Run relevant validation after changes:

    python scripts/rcc/check_rcc_nexus.py
    python scripts/validation/validate_architecture_contracts.py
    python -m unittest discover -s tests

## RCC Nexus Echo Location

Sphere Position:

- Shell: {shell_for(rel)}
- Meridian(s): {meridians_for(rel)}
- Sector: {top}
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-19

Local Role:

- {purpose_for(rel)}

Evidence Surface:

- reports/
- outputs/
- docs/context/drift/

Validation Surface:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

Claim Boundary:

- {NON_CLAIM_BOUNDARY}

Non-Claim Locks:

- navigation_is_not_validation
- documentation_is_not_correctness
- context_reconstruction_is_not_code_quality
- validation_remains_required
- rcc_nexus_is_not_ai_understanding
"""


def ensure_readme(rel: str) -> Dict[str, object]:
    folder = ROOT / rel
    readme = folder / "README.md"

    created = False
    repaired = False

    if not readme.exists():
        readme.write_text(f"# {rel}\n" + local_block(rel), encoding="utf-8")
        created = True
        repaired = True
    else:
        text = readme.read_text(encoding="utf-8", errors="ignore")
        additions = []

        if "## S — Specification" not in text:
            additions.append(local_block(rel))
        else:
            if "## RCC Nexus Echo Location" not in text:
                additions.append("""
## RCC Nexus Echo Location

Sphere Position:

- Shell: """ + shell_for(rel) + """
- Meridian(s): """ + meridians_for(rel) + """
- Sector: """ + (normalize_rel(rel).split("/")[0] if rel else "root") + """
- Version / TTL: RCC-N-v1.0 / 180 days
- Last Verified: 2026-05-19

Local Role:

- """ + purpose_for(rel) + """

Evidence Surface:

- reports/
- outputs/
- docs/context/drift/

Validation Surface:

    python scripts/rcc/check_rcc_nexus.py
    python -m unittest discover -s tests

Claim Boundary:

- """ + NON_CLAIM_BOUNDARY + """

Non-Claim Locks:

- navigation_is_not_validation
- documentation_is_not_correctness
- context_reconstruction_is_not_code_quality
- validation_remains_required
- rcc_nexus_is_not_ai_understanding
""")
            if "Claim Boundary" not in text:
                additions.append("\n## Claim Boundary\n\n- " + NON_CLAIM_BOUNDARY + "\n")
            if "Non-Claim Locks" not in text:
                additions.append("""
## Non-Claim Locks

- navigation_is_not_validation
- documentation_is_not_correctness
- context_reconstruction_is_not_code_quality
- validation_remains_required
- rcc_nexus_is_not_ai_understanding
""")

        if additions:
            readme.write_text(text.rstrip() + "\n\n" + "\n\n".join(additions).strip() + "\n", encoding="utf-8")
            repaired = True

    text_after = readme.read_text(encoding="utf-8", errors="ignore")
    missing = [marker for marker in REQUIRED_MARKERS if marker not in text_after]

    return {
        "path": str(readme.relative_to(ROOT)),
        "created": created,
        "repaired": repaired,
        "missing": missing,
        "complete": not missing,
    }


def audit_or_repair() -> Dict[str, object]:
    created: List[str] = []
    repaired: List[str] = []
    existing: List[str] = []
    incomplete: Dict[str, List[str]] = {}

    for rel in MAJOR_DIRS:
        folder = ROOT / rel
        if not folder.exists():
            continue

        result = ensure_readme(rel)
        if result["created"]:
            created.append(result["path"])
        else:
            existing.append(result["path"])
        if result["repaired"] and not result["created"]:
            repaired.append(result["path"])
        if not result["complete"]:
            incomplete[result["path"]] = result["missing"]

    total = len(created) + len(existing)
    complete = total - len(incomplete)
    coverage = complete / total if total else 0.0

    return {
        "schema": "RCC-N-v0.5.1-mini-readme-audit",
        "total_major_dirs_with_readmes": total,
        "created": created,
        "repaired": repaired,
        "existing": existing,
        "incomplete": incomplete,
        "complete_count": complete,
        "coverage": coverage,
        "passed": coverage >= 0.90,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }


def main() -> int:
    report = audit_or_repair()

    out_dir = ROOT / "reports" / "mini_readmes"
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "latest_mini_readme_audit.json"
    md_path = out_dir / "latest_mini_readme_audit.md"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    md_lines = [
        "# Mini README Audit",
        "",
        f"- Total major dirs with READMEs: {report['total_major_dirs_with_readmes']}",
        f"- Complete count: {report['complete_count']}",
        f"- Coverage: {report['coverage']:.3f}",
        f"- Passed: {report['passed']}",
        "",
        "## Created",
        "",
    ]

    for item in report["created"]:
        md_lines.append(f"- `{item}`")

    md_lines.extend(["", "## Repaired", ""])

    for item in report["repaired"]:
        md_lines.append(f"- `{item}`")

    md_lines.extend(["", "## Incomplete", ""])

    if report["incomplete"]:
        for item, missing in report["incomplete"].items():
            md_lines.append(f"- `{item}` missing: {', '.join(missing)}")
    else:
        md_lines.append("- None")

    md_lines.extend([
        "",
        "## Boundary",
        "",
        str(report["non_claim_boundary"]),
        "",
    ])

    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())