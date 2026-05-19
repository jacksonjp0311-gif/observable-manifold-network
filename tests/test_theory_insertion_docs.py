import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestTheoryInsertionDocs(unittest.TestCase):
    def test_omn_sa_v0_1_source_anchor_exists_and_preserves_locks(self):
        path = ROOT / "docs" / "theory" / "omn_sa_v0_1_source_anchor.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("OMN-SA v0.1 Source Anchor", text)
        self.assertIn("GMN authorship remains with Park et al.", text)
        self.assertIn("OMN-SA v0.2 is the current software architecture layer", text)
        self.assertIn("No graph contract, no topology claim", text)
        self.assertIn("Observable topology becomes useful only when it becomes executable", text)
        self.assertIn("documentation_is_not_correctness", text)

    def test_injection_record_exists_and_has_hydra_sequence(self):
        path = ROOT / "docs" / "injections" / "omn_sa_v0_1_theory_insertion.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("Anchor -> Inject -> Retract -> Seal", text)
        self.assertIn("Retract", text)
        self.assertIn("Seal", text)
        self.assertIn("injection_is_not_validation", text)

    def test_registry_and_readme_reference_source_anchor(self):
        registry = (ROOT / "docs" / "DOCS_REGISTRY.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/theory/omn_sa_v0_1_source_anchor.md", registry)
        self.assertIn("docs/injections/omn_sa_v0_1_theory_insertion.md", registry)
        self.assertIn("docs/theory/omn_sa_v0_1_source_anchor.md", readme)
        self.assertIn("OMN-SA v0.1 = preserved source anchor", readme)


if __name__ == "__main__":
    unittest.main()