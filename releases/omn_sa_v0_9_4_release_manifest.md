# OMN-SA v0.9.4 Release Manifest / Version Seal

Generated: 2026-05-22T08:42:28.896687+00:00

## Release Identity

| Surface | Value |
|---|---|
| Version | OMN-SA v0.9.4 |
| Release reference | v0.9.4-release-manifest-version-seal |
| Source base commit | `b834d5d` |
| Expected tests | 67 OK |
| Release readiness | local-release-sealed |

## Validation Commands

```powershell
python -m unittest discover -s tests
python scripts/release/update_version_surfaces.py --check --version "OMN-SA v0.9.4" --tests 67 --patch-name "OMN-SA v0.9.4 release manifest / version seal"
python -m omn run --seed synthetic-toy --ci-mode --run-id omn_ci_smoke --output-dir outputs_ci --no-write-report
python -m omn index-evidence --output-dir outputs_ci
python -m omn report-latest --output-dir outputs_ci --mode ci
python -m omn validate --output-dir outputs_ci --mode ci
python -m omn --help
```

## Required Surfaces

| Surface | Path |
|---|---|
| README | `README.md` |
| Docs registry | `docs/DOCS_REGISTRY.md` |
| Version-surface checker | `scripts/release/update_version_surfaces.py` |
| Public metrics dashboard | `docs/benchmarks/current_public_metrics.md` |
| Public metrics chart | `visuals/omn_sa/current_public_metrics.svg` |
| Release manifest JSON | `releases/omn_sa_v0_9_4_release_manifest.json` |
| Release manifest MD | `releases/omn_sa_v0_9_4_release_manifest.md` |

## v0.9.4 Law

    No release without a machine-readable version seal.

## Boundary

The release manifest records local release-readiness surfaces and validation commands. It does not prove code correctness, empirical validation, causality, mechanism, production readiness, AI understanding, or GMN replication.
