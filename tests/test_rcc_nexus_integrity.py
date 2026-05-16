import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestRCCNexusIntegrity(unittest.TestCase):
    def test_readme_embeds_echo_chart(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("visuals/rcc_nexus/rcc_nexus_echo_chart.svg", readme)
        self.assertIn("Documentation Separation Rule", readme)

    def test_docs_registry_declares_separated_lanes(self):
        registry = (ROOT / "docs" / "DOCS_REGISTRY.md").read_text(encoding="utf-8")
        for lane in [
            "docs/theory/",
            "docs/software_architecture/",
            "docs/architecture_changes/",
            "docs/injections/",
            "docs/injected_theory/",
            "docs/future_architecture/",
            "docs/release_notes/",
        ]:
            self.assertIn(lane, registry)

    def test_route_map_has_required_task_types(self):
        route = json.loads((ROOT / "rcc" / "nexus" / "route_map.json").read_text(encoding="utf-8"))
        task_types = {item["task_type"] for item in route["routes"]}
        for required in ["docs", "runtime", "evidence", "rcc"]:
            self.assertIn(required, task_types)

    def test_public_release_boundary_present(self):
        public = (ROOT / "docs" / "public_release" / "ai_orientable_repositories_rcc_n.md").read_text(encoding="utf-8")
        self.assertIn("It does not make AI conscious", public)
        self.assertIn("It is repository-level orientation", public)


if __name__ == "__main__":
    unittest.main()