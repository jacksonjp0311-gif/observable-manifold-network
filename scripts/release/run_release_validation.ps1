$ErrorActionPreference = "Stop"

function Run-Check {
    param(
        [Parameter(Mandatory=$true)][string]$Command,
        [Parameter(ValueFromRemainingArguments=$true)][string[]]$Args
    )
    & $Command @Args
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code ${LASTEXITCODE}: $Command $($Args -join ' ')"
    }
}

$Root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $Root
$env:PYTHONPATH = "$Root\src"

Write-Host "OMN-SA release validation checkpoint"
Write-Host "Mode: artifact-emitting release validation"

Run-Check python scripts/rcc/check_rcc_nexus_v1_7_profile.py
Run-Check python scripts/release/audit_readme_self_organization.py
Run-Check python scripts/release/audit_readme_v0_7_lineage.py
Run-Check python scripts/release/audit_readme_v0_8_metric_availability.py
Run-Check python scripts/release/audit_readme_lineage_policy.py
Run-Check python scripts/validation/validate_evidence_drift.py
Run-Check python scripts/validation/validate_metric_availability.py
Run-Check python scripts/validation/validate_evidence_replay.py
Run-Check python scripts/rcc/audit_mini_readmes.py
Run-Check python scripts/rcc/generate_rcc_n_metrics.py
Run-Check python scripts/validation/validate_topology_ensemble.py
Run-Check python scripts/validation/validate_graph_engine.py
Run-Check python scripts/validation/validate_modular_runtime.py
Run-Check python scripts/validation/validate_architecture_contracts.py
Run-Check python scripts/rcc/check_rcc_nexus.py
Run-Check python -m unittest discover -s tests
Run-Check python -m omn validate

git status --short

Write-Host "Release validation completed. Review and commit refreshed artifacts if intended."
Write-Host "Do not copy this artifact-emitting stack into GitHub Actions CI."