#!/usr/bin/env bash
set -euo pipefail
python3 -V
pip -V || true
echo "== creating venv =="
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
echo "== sanity 1: checker --fake =="
python3 -m tools.check_submission --fake
echo "== sanity 2: make_submission =="
python3 -m tools.make_submission
echo "== sanity 3: checker on file =="
python3 -m tools.check_submission --path submission.csv
echo "ALL GOOD ✅"
