# PowerShell sanity script
$ErrorActionPreference = "Stop"
python -V
pip -V
Write-Host "== creating venv =="
py -m venv .venv
. .\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
Write-Host "== sanity 1: checker --fake =="
py -m tools.check_submission --fake
Write-Host "== sanity 2: make_submission =="
py -m tools.make_submission
Write-Host "== sanity 3: checker on file =="
py -m tools.check_submission --path submission.csv
Write-Host "ALL GOOD ✅"
