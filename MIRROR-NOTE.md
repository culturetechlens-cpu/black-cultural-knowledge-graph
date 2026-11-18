# GitHub Mirror Note — entities.json layout

CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

This repository carries the CultureTechLens Black Cultural Knowledge Graph
dataset, **v2.2 (2026-11-18)**, built from Combined Graph Release 2026-11-15
and filtered under Phase 0 Amendment A1 (verified rows only). Its Zenodo
deposit is pending the founder's token sitting; the concept DOI
**10.5281/zenodo.23403147** always resolves to the latest deposited version
(currently v2.1, DOI 10.5281/zenodo.23822179) and will resolve to v2.2 on
deposit. The Zenodo record is the canonical, citable source.

Ten of the eleven deposit files are mirrored byte-identical at the repo root:
README.md, CHANGELOG.md, DATA-DICTIONARY.md, CITATION.cff, schema.json,
entities.csv, relationships.csv, relationships.json, conflicts.csv,
photos.csv.

**One exception, for a transport limit only:** the single-file `entities.json`
exceeds the per-push payload limit of the channel used to build this mirror,
so on GitHub it ships as 27 shards — `data/entities-A.json` …
`data/entities-Z.json` plus `data/entities-0-9.json` — split by the first
letter of each record's name, preserving record order. Rebuild the exact
deposit file with:

    python3 build_entities_json.py

which concatenates the shards into `entities.json` (3,488 records) and
verifies the count. Nothing else about the dataset differs from the deposit.

Cite as: CultureTechLens, "CultureTechLens Black Cultural Knowledge Graph"
(Dataset v2.2), November 18, 2026. https://doi.org/10.5281/zenodo.23403147
Source: CultureTechLens.
