#!/usr/bin/env bash
# normalize → tier → split → stats
set -euo pipefail
python -m akan_autocomplete.data.normalize
python -m akan_autocomplete.data.tiers
python -m akan_autocomplete.data.split
python -m akan_autocomplete.data.stats
