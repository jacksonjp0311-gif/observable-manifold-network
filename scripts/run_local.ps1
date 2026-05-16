$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
$env:PYTHONPATH = "$Root\src"
python -m omn run --seed synthetic-toy
python -m omn run --seed lorenz
python -m omn run --seed artifact-graph
python -m omn report-latest