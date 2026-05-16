import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_PATHS = [
    "docs/software_architecture/omn_sa_v0_2_software_architecture.md",
    "docs/architecture_changes/omn_sa_v0_2_architecture_change.md",
    "schemas/omn/evidence_package.schema.json",
    "schemas/omn/graph_contract.schema.json",
    "schemas/rcc_nexus/route_map.schema.json",
    "schemas/rcc_nexus/rcc_nexus_index.schema.json",
    "docs/DOCS_REGISTRY.md",
    "README.md",
    "README_90_SECONDS.md",
    "docs/injections/README.md",
    "docs/architecture_changes/README.md",
    "docs/injected_theory/README.md",
    "visuals/rcc_nexus/rcc_nexus_echo_chart.svg",
]

DOC_LANES = [
    "docs/theory/",
    "docs/software_architecture/",
    "docs/architecture_changes/",
    "docs/injections/",
    "docs/injected_theory/",
    "docs/future_architecture/",
    "docs/release_notes/",
]

SCHEMA_FILES = [
    "schemas/omn/evidence_package.schema.json",
    "schemas/omn/graph_contract.schema.json",
    "schemas/rcc_nexus/route_map.schema.json",
    "schemas/rcc_nexus/rcc_nexus_index.schema.json",
]

def read_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def main() -> int:
    missing = [p for p in REQUIRED_PATHS if not (ROOT / p).exists()]

    readme = (ROOT / "README.md").read_text(encoding="utf-8", errors="replace")
    registry = (ROOT / "docs" / "DOCS_REGISTRY.md").read_text(encoding="utf-8", errors="replace")
    public_release = (ROOT / "docs" / "public_release" / "ai_orientable_repositories_rcc_n.md").read_text(encoding="utf-8", errors="replace")

    missing_lanes = [lane for lane in DOC_LANES if lane not in registry]
    missing_readme_markers = []
    for marker in [
        "Theory / Software Architecture / Injections Registry",
        "Documentation Separation Rule",
        "RCC-N Echo Chart",
        "OMN-SA v0.2 Engineering Hardening",
    ]:
        if marker not in readme:
            missing_readme_markers.append(marker)

    missing_public_boundaries = []
    for marker in [
        "It does not make AI conscious",
        "It is repository-level orientation",
        "RCC-N does not prove the code is correct",
    ]:
        if marker not in public_release:
            missing_public_boundaries.append(marker)

    schema_failures = []
    for rel in SCHEMA_FILES:
        path = ROOT / rel
        try:
            data = read_json(path)
        except Exception as exc:
            schema_failures.append({"path": rel, "error": str(exc)})
            continue
        for key in ["schema_id", "required_keys", "boundary", "validation_command", "non_claim_lock"]:
            if key not in data:
                schema_failures.append({"path": rel, "missing_key": key})

    # Validate actual RCC route map and Nexus index against lightweight contracts.
    route_map_path = ROOT / "rcc" / "nexus" / "route_map.json"
    route_contract = read_json(ROOT / "schemas" / "rcc_nexus" / "route_map.schema.json")
    route_map_failures = []
    if route_map_path.exists():
        route_map = read_json(route_map_path)
        for key in route_contract["required_keys"]:
            if key not in route_map:
                route_map_failures.append(f"missing route_map key: {key}")
        actual_types = {r.get("task_type") for r in route_map.get("routes", [])}
        for required in route_contract["required_route_task_types"]:
            if required not in actual_types:
                route_map_failures.append(f"missing route task type: {required}")
    else:
        route_map_failures.append("missing rcc/nexus/route_map.json")

    nexus_index_path = ROOT / "docs" / "context" / "rcc_nexus_index.json"
    nexus_contract = read_json(ROOT / "schemas" / "rcc_nexus" / "rcc_nexus_index.schema.json")
    nexus_failures = []
    if nexus_index_path.exists():
        nexus_index = read_json(nexus_index_path)
        for key in nexus_contract["required_keys"]:
            if key not in nexus_index:
                nexus_failures.append(f"missing rcc_nexus_index key: {key}")
    else:
        nexus_failures.append("missing docs/context/rcc_nexus_index.json")

    report = {
        "schema": "OMN-SA-v0.2-architecture-contract-validation",
        "passed": not any([
            missing,
            missing_lanes,
            missing_readme_markers,
            missing_public_boundaries,
            schema_failures,
            route_map_failures,
            nexus_failures,
        ]),
        "missing_required_paths": missing,
        "missing_doc_lanes": missing_lanes,
        "missing_readme_markers": missing_readme_markers,
        "missing_public_boundaries": missing_public_boundaries,
        "schema_failures": schema_failures,
        "route_map_failures": route_map_failures,
        "nexus_index_failures": nexus_failures,
        "non_claim_boundary": "Architecture validation checks repository contracts, not code correctness, empirical validation, causality, mechanism, AI understanding, production readiness, or GMN replication."
    }

    out_dir = ROOT / "reports" / "architecture"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "latest_omn_sa_v0_2_architecture_validation.json").write_text(
        json.dumps(report, indent=2),
        encoding="utf-8"
    )

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())