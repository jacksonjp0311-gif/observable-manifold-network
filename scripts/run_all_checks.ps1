$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

Write-Host ""
Write-Host "OMN-SA all checks" -ForegroundColor Cyan
Write-Host "Root: $Root" -ForegroundColor Green

$env:PYTHONPATH = "$Root\src"

Write-Host ""
Write-Host "1. RCC-N checker" -ForegroundColor Cyan
python scripts/rcc/check_rcc_nexus.py

Write-Host ""
Write-Host "2. Unit tests" -ForegroundColor Cyan
python -m unittest discover -s tests

Write-Host ""
Write-Host "3. Runtime seeds" -ForegroundColor Cyan
python -m omn run --seed synthetic-toy
python -m omn run --seed lorenz
python -m omn run --seed artifact-graph

Write-Host ""
Write-Host "4. Evidence validation" -ForegroundColor Cyan
python -m omn validate

Write-Host ""
Write-Host "All checks completed." -ForegroundColor Green