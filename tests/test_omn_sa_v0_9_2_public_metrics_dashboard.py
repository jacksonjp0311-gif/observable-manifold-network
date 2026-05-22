import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestOMNSAV092PublicMetricsDashboard(unittest.TestCase):
    def test_public_metrics_dashboard_exists_and_has_boundaries(self):
        dashboard = ROOT / "docs" / "benchmarks" / "current_public_metrics.md"
        chart = ROOT / "visuals" / "omn_sa" / "current_public_metrics.svg"

        self.assertTrue(dashboard.exists())
        self.assertTrue(chart.exists())

        text = dashboard.read_text(encoding="utf-8")
        self.assertIn("OMN-SA v0.9.2 Current Public Metrics Dashboard", text)
        self.assertIn("Unit tests | 63 OK", text)
        self.assertIn("Mini README coverage | 37 / 37", text)
        self.assertIn("RCC-N effectiveness score | 0.9822222222", text)
        self.assertIn("Measured RCC-N lift | +0.8752222222", text)
        self.assertIn("Stable evidence index | passed", text)
        self.assertIn("does not prove empirical validation", text)

    def test_readme_links_current_public_metrics(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertTrue("Current software layer | OMN-SA v0.9.2" in readme or "Current software layer | OMN-SA v0.9.3" in readme)
        self.assertIn("docs/benchmarks/current_public_metrics.md", readme)
        self.assertIn("visuals/omn_sa/current_public_metrics.svg", readme)


if __name__ == "__main__":
    unittest.main()
