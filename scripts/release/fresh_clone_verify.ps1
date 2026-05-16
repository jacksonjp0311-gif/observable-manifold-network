$ErrorActionPreference = "Stop"

$RemoteUrl = "https://github.com/jacksonjp0311-gif/observable-manifold-network.git"
$Desktop = Join-Path $env:USERPROFILE "OneDrive\Desktop"
if (!(Test-Path $Desktop)) {
    $Desktop = Join-Path $env:USERPROFILE "Desktop"
}

$CloneRoot = Join-Path $Desktop "OMN-FRESH-CHECK"

if (Test-Path $CloneRoot) {
    Remove-Item -Recurse -Force $CloneRoot
}

git clone $RemoteUrl $CloneRoot
Set-Location $CloneRoot

$env:PYTHONPATH = "$CloneRoot\src"

python scripts/rcc/check_rcc_nexus.py
python -m unittest discover -s tests
python -m omn run --seed synthetic-toy
python -m omn validate

Write-Host ""
Write-Host "Fresh clone verification completed." -ForegroundColor Green
Write-Host "Clone: $CloneRoot" -ForegroundColor Green