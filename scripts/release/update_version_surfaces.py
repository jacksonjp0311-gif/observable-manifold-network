from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
DOCS_REGISTRY = ROOT / "docs" / "DOCS_REGISTRY.md"
CI_WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"

REQUIRED_README_ZONES = [
    "### Current health snapshot",
    "### Current Versioned Documentation Stack",
    "### Current Architecture Chain",
    "## AI Version Tracking Contract",
    "### Version Update Obligation",
]

REQUIRED_VERSION_SURFACES = [
    "README current health snapshot",
    "README current versioned documentation stack",
    "README architecture chain",
    "AI version tracking contract",
    "bottom lineage section",
    "CI required markers",
    "DOCS_REGISTRY.md",
    "public metrics references",
]

VERSION_SURFACE_LAW = "No version bump without automated registry-surface verification"

NON_CLAIM_BOUNDARY = (
    "Version-surface automation checks repository documentation and release-orientation surfaces. "
    "It does not prove code correctness, empirical validation, causality, mechanism, production readiness, "
    "AI understanding, or GMN replication."
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def replace_health_snapshot(text: str, block: str) -> str:
    pattern = r"(?s)### Current health snapshot\s*\n\s*\n.*?(?=\n### What this is not)"
    new_text, count = re.subn(pattern, block, text, count=1)
    if count != 1:
        raise RuntimeError("Could not replace README current health snapshot.")
    return new_text


def check_required_zones(text: str) -> list[str]:
    return [zone for zone in REQUIRED_README_ZONES if zone not in text]


def check_current(version: str, tests: str, patch_name: str) -> list[str]:
    missing: list[str] = []
    readme = read(README)
    workflow = read(CI_WORKFLOW) if CI_WORKFLOW.exists() else ""

    for zone in check_required_zones(readme):
        missing.append(f"missing README zone: {zone}")

    required_readme_markers = [
        f"Current software layer | {version}",
        f"Latest public alignment patch | {patch_name}",
        f"Current tests | {tests} OK",
        "docs/benchmarks/current_public_metrics.md",
        "visuals/omn_sa/current_public_metrics.svg",
    ]

    for marker in required_readme_markers:
        if marker not in readme:
            missing.append(f"missing README marker: {marker}")

    for marker in [version, patch_name, f"Current tests | {tests} OK"]:
        if marker not in workflow:
            missing.append(f"missing CI marker: {marker}")

    registry = read(DOCS_REGISTRY) if DOCS_REGISTRY.exists() else ""
    if version not in registry:
        missing.append(f"missing DOCS_REGISTRY version marker: {version}")

    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="OMN-SA version-surface updater/checker")
    parser.add_argument("--check", action="store_true", help="check current README/registry/CI surfaces")
    parser.add_argument("--version", required=True, help="current OMN-SA version marker, for example 'OMN-SA v0.9.3'")
    parser.add_argument("--tests", required=True, help="current passing test count without 'OK'")
    parser.add_argument("--patch-name", required=True, help="latest public alignment patch name")
    args = parser.parse_args()

    if args.check:
        missing = check_current(args.version, args.tests, args.patch_name)
        if missing:
            print("Version surface check failed:")
            for item in missing:
                print(f"- {item}")
            print(f"Boundary: {NON_CLAIM_BOUNDARY}")
            return 1
        print("Version surface check passed.")
        print(f"Boundary: {NON_CLAIM_BOUNDARY}")
        return 0

    parser.error("Only --check mode is implemented in v0.9.3. Future versions may add controlled --apply mode.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
