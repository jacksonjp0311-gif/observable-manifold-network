import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from omn.core.runtime import run, validate_evidence


class TestOMNRuntime(unittest.TestCase):
    def test_synthetic_toy_run_emits_evidence(self):
        evidence = run("synthetic-toy", str(ROOT))
        self.assertIn(evidence["schema"], ["OMN-SA-v0.1-evidence-package", "OMN-SA-v0.8-evidence-package", "OMN-SA-v0.9-evidence-package"])
        self.assertTrue(Path(evidence["artifacts"]["state"]).exists())
        self.assertTrue(Path(evidence["artifacts"]["graph_contract"]).exists())
        self.assertTrue(Path(evidence["artifacts"]["generated_state"]).exists())
        self.assertTrue(Path(evidence["artifacts"]["validation_residuals"]).exists())
        self.assertTrue(Path(ROOT / "outputs" / "evidence" / f'{evidence["run_id"]}_evidence_package.json').exists())
        self.assertTrue(evidence["audit"]["passed"])

    def test_lorenz_run_has_non_claim_locks(self):
        evidence = run("lorenz", str(ROOT))
        locks = evidence["non_claim_locks"]
        self.assertTrue(locks["simulation_is_not_proof"])
        self.assertTrue(locks["prediction_is_not_mechanism"])
        self.assertTrue(locks["observable_topology_is_not_truth"])

    def test_validate_evidence_paths(self):
        evidence = run("artifact-graph", str(ROOT))
        evidence_path = ROOT / "outputs" / "evidence" / f'{evidence["run_id"]}_evidence_package.json'
        result = validate_evidence(evidence_path)
        self.assertTrue(result["valid"], result)


if __name__ == "__main__":
    unittest.main()