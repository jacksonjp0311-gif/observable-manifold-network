from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

NON_CLAIM_BOUNDARY = (
    "The v1.0 readiness gate checks local release-readiness surfaces. "
    "It does not prove code correctness, empirical validation, causality, mechanism, production readiness, "
    "AI understanding, or GMN replication."
)

REQUIRED_FILES = [
    "README.md",
    "docs/DOCS_REGISTRY.md",
    ".github/workflows/ci.yml",
    "scripts/release/update_version_surfaces.py",
    "docs/benchmarks/current_public_metrics.md",
    "visuals/omn_sa/current_public_metrics.svg",
    "releases/omn_sa_v0_9_4_release_manifest.json",
    "releases/omn_sa_v0_9_4_release_manifest.md",
]

REQUIRED_NON_CLAIMS = [
    "code correctness",
    "empirical validation",
    "causality",
    "production readiness",
    "GMN replication",
]

def run_cmd(args: list[str]) -> tuple[int, str]:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    return result.returncode, (result.stdout + result.stderr)

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8", errors="ignore")

def check_file_presence() -> tuple[bool, list[str]]:
    missing = [p for p in REQUIRED_FILES if not (ROOT / p).exists()]
    return len(missing) == 0, missing

def check_readme(version: str, tests: str, patch_name: str) -> tuple[bool, list[str]]:
    text = read("README.md")
    markers = [
        f"Current software layer | {version}",
        f"Latest public alignment patch | {patch_name}",
        f"Current tests | {tests} OK",
        "No v1.0 without a readiness classifier",
    ]
    missing = [m for m in markers + REQUIRED_NON_CLAIMS if m not in text]
    return len(missing) == 0, missing

def check_registry(version: str) -> tuple[bool, list[str]]:
    text = read("docs/DOCS_REGISTRY.md")
    lower_text = text.lower()
    checks = [
        (version, version in text),
        ("v1.0 readiness gate", "v1.0 readiness gate" in lower_text),
        ("scripts/release/check_v1_0_readiness.py", "scripts/release/check_v1_0_readiness.py" in text),
    ]
    missing = [name for name, ok in checks if not ok]
    return len(missing) == 0, missing


def check_release_manifest() -> tuple[bool, list[str]]:
    path = ROOT / "releases" / "omn_sa_v0_9_4_release_manifest.json"
    if not path.exists():
        return False, ["release manifest missing"]
    data = json.loads(path.read_text(encoding="utf-8"))
    required = [
        ("schema", "OMN-SA-v0.9.4-release-manifest"),
        ("release_readiness", "local-release-sealed"),
    ]
    missing = []
    for key, value in required:
        if data.get(key) != value:
            missing.append(f"{key} != {value}")
    if "non_claim_boundary" not in data:
        missing.append("non_claim_boundary missing")
    return len(missing) == 0, missing

def check_git_clean() -> tuple[bool, list[str]]:
    code, out = run_cmd(["git", "status", "--short"])
    if code != 0:
        return False, ["git status failed"]
    lines = [line for line in out.splitlines() if line.strip()]
    return len(lines) == 0, lines

def build_report(version: str, tests: str, patch_name: str, require_clean: bool) -> dict:
    checks = {}

    ok, missing = check_file_presence()
    checks["required_files"] = {"passed": ok, "missing": missing}

    ok, missing = check_readme(version, tests, patch_name)
    checks["readme_alignment"] = {"passed": ok, "missing": missing}

    ok, missing = check_registry(version)
    checks["docs_registry_alignment"] = {"passed": ok, "missing": missing}

    ok, missing = check_release_manifest()
    checks["release_manifest_present"] = {"passed": ok, "missing": missing}

    code, out = run_cmd([
        "python",
        "scripts/release/update_version_surfaces.py",
        "--check",
        "--version",
        version,
        "--tests",
        tests,
        "--patch-name",
        patch_name,
    ])
    checks["version_surface_checker"] = {
        "passed": code == 0,
        "details": out.strip().splitlines()[-5:],
    }

    if require_clean:
        ok, missing = check_git_clean()
        checks["working_tree_clean"] = {"passed": ok, "missing": missing}
    else:
        checks["working_tree_clean"] = {"passed": True, "missing": [], "skipped": True}

    passed = all(item.get("passed") for item in checks.values())

    return {
        "schema": "OMN-SA-v0.9.5-v1.0-readiness-report",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "version": version,
        "target": "OMN-SA v1.0.0",
        "readiness_classification": "v1.0-ready-candidate" if passed else "not-ready",
        "passed": passed,
        "checks": checks,
        "non_claim_boundary": NON_CLAIM_BOUNDARY,
    }

def main() -> int:
    parser = argparse.ArgumentParser(description="OMN-SA v1.0 readiness gate")
    parser.add_argument("--version", default="OMN-SA v0.9.5")
    parser.add_argument("--tests", default="73")
    parser.add_argument("--patch-name", default="OMN-SA v0.9.5 v1.0 readiness gate")
    parser.add_argument("--require-clean", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()

    report = build_report(args.version, args.tests, args.patch_name, args.require_clean)

    if args.write_report:
        out_dir = ROOT / "reports" / "readiness"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "latest_v1_0_readiness_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        lines = [
            "# OMN-SA v1.0 Readiness Report",
            "",
            f"- Version: {report['version']}",
            f"- Target: {report['target']}",
            f"- Passed: {report['passed']}",
            f"- Classification: {report['readiness_classification']}",
            "",
            "## Checks",
            "",
            "| Check | Passed |",
            "|---|---:|",
        ]
        for key, value in report["checks"].items():
            lines.append(f"| {key} | {value.get('passed')} |")
        lines.extend(["", "## Boundary", "", report["non_claim_boundary"], ""])
        (out_dir / "latest_v1_0_readiness_report.md").write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
