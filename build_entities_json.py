#!/usr/bin/env python3
"""Rebuild the single-file entities.json (as deposited on Zenodo,
DOI 10.5281/zenodo.23753474) from this repo's data/entities-*.json shards."""
import json, glob
records = []
for path in sorted(glob.glob('data/entities-*.json')):
    records.extend(json.load(open(path)))
assert len(records) == 7530, f"expected 7530 records, got {len(records)}"
with open('entities.json', 'w') as f:
    json.dump(records, f, ensure_ascii=False, indent=1)
print(f"entities.json rebuilt: {len(records)} records")
