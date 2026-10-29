# CULTURETECHLENS
## "Culture, Clearly Seen." · Black Cultural Intelligence

# CultureTechLens Black Cultural Knowledge Graph — Dataset v2.0

**7,530 entities · 7,998 relationships · 832 rights-documented photographs · 576 preserved conflict notes.**

**One DOI:** 10.5281/zenodo.23403147 — the concept DOI for this dataset. It always resolves to the current version. Cite it.
**Version:** 2.0 (2026-10-28), built from *CultureTechLens Combined Graph, Release 2026-10-28*.
**Creators:** William Maxey (ORCID 0009-0004-2837-8037) · CultureTechLens NFP.
**License:** CC BY 4.0 (dataset). Photographs remain under their own licenses — see `photos.csv`.

Cite as: CultureTechLens, "CultureTechLens Black Cultural Knowledge Graph" (Dataset v2.0), October 28, 2026. https://doi.org/10.5281/zenodo.23403147
Source: CultureTechLens.

## What this is

One record per person, place, work, institution, event, and practice in Black culture — Chicago first — drawn from CultureTechLens's two research stores and published as a single downloadable dataset. Every entity carries its type, a curated description, the grade each store assigned it, and both stores' identifiers. Grades are carried per store and **never merged**; where the two stores disagree, the disagreement ships in `conflicts.csv`, labeled and explained — nothing is blended, averaged, or silently picked.

The canonical public counts on culturetechlens.com remain the master store's (4,111 entities / 2,527 relationships). This dataset is the union view — the diligence and research instrument — designated in *Combined Graph — Release 2026-10-28*.

## Files

| File | Contents |
|---|---|
| `entities.csv` / `entities.json` | One row/object per entity (7,530): name, type, aliases, description, per-store grades, per-store IDs, conflict count, photo flag. JSON adds the full conflict notes and photo records. |
| `relationships.csv` / `relationships.json` | One row/object per relationship (7,998), with the store(s) attesting each edge; JSON adds evidence text where the source record carries it. |
| `conflicts.csv` | All 576 preserved disagreements: 273 grade divergences · 172 type conflicts · 93 name-form divergences · 20 duplicate-cluster notes · 13 fold notes · 4 split-record notes · 1 date conflict. |
| `photos.csv` | The per-image evidence record for each attached photograph (832): creator, source, license, credit line. By license: 527 public domain / CC0 / no known restrictions · 181 CC BY-SA · 124 CC BY. |
| `schema.json` | Machine-readable schema: file definitions, entity-type counts, grade-scale definitions. |
| `DATA-DICTIONARY.md` | Every column defined, both grade scales explained. |
| `CHANGELOG.md` | Version history. **Read the v2.0 entry before comparing counts with v1.x** — the source changed. |
| `CITATION.cff` | Machine-readable citation metadata. |

## Terms

The dataset is published CC BY 4.0: use it, build on it, credit CultureTechLens and the DOI. The photographs are **not** covered by the dataset license — each carries its own license and credit line in `photos.csv`, and downstream use follows those terms. Living-person records rest on published, public sources; correction and takedown requests go to info@culturetechlens.com and are answered against the evidence record.

## Provenance

Built 2026-10-28 by a deterministic export from `combined-graph.json` (23,990,016 bytes; SHA-256 307f3e125226b230f43c49b6cd1519fa2215ffee1f3e28ddb4b27c3c34f33797), the Release 2026-10-28 artifact — the union of the canonical master and the build graph, matched only through the certified 2026-10-20 crosswalk, with the cleared photo layer folded in (including the 2026-10-27 archive fold-in). Identifiers: `union_id` (U-NNNNN) is the dataset ID. The two stores' own ID strings are **not** interchangeable (221 known collisions) — cite the union_id.

## Citation forms (per CTL-CITE-001; Chicago is CTL's primary style)

- **Chicago:** Maxey, William, and CultureTechLens. *CultureTechLens Black Cultural Knowledge Graph*. Version 2.0. Chicago: CultureTechLens NFP, 2026. https://doi.org/10.5281/zenodo.23403147.
- **APA:** Maxey, W., & CultureTechLens NFP. (2026). *CultureTechLens Black Cultural Knowledge Graph* (Version 2.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23403147
- **MLA:** Maxey, William, and CultureTechLens NFP. *CultureTechLens Black Cultural Knowledge Graph*. Version 2.0, Zenodo, 2026. doi:10.5281/zenodo.23403147.
