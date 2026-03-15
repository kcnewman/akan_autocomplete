#!/usr/bin/env bash
# Usage: ./scripts/run_experiment.sh EXP-04
set -euo pipefail
EXP_ID=${1:?Usage: run_experiment.sh EXP-XX}
python -m akan_autocomplete.modeling.experiment "$EXP_ID"
