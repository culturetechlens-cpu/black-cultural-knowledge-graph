# CULTURETECHLENS
## "Culture, Clearly Seen." · Black Cultural Intelligence

# CultureTechLens Black Cultural Knowledge Graph — Dataset v2.2

**3,488 entities · 2,628 relationships · 205 rights-documented photographs · 491 preserved conflict notes.**

**One DOI:** 10.5281/zenodo.23403147 — the concept DOI for this dataset. It always resolves to the current version. Cite it.
**Version:** 2.2 (2026-11-18), built from *CultureTechLens Combined Graph, Release 2026-11-15*, filtered under Phase 0 as amended (Amendment A1, 2026-10-30).
**Creators:** William Maxey (ORCID 0009-0004-2837-8037) · CultureTechLens NFP.
**License:** CC BY 4.0 (dataset). Photographs remain under their own licenses — see `photos.csv`.

Cite as: CultureTechLens, "CultureTechLens Black Cultural Knowledge Graph" (Dataset v2.2), November 18, 2026. https://doi.org/10.5281/zenodo.23403147
Source: CultureTechLens.

## Scope — verified rows only (Phase 0, as amended 2026-10-30)

This release contains **verified rows only**. Under CTL Phase 0 as amended by Amendment A1 (2026-10-30), a dataset published under a CultureTechLens DOI may contain only rows that carry a verification grade of **VERIFIED** or **STRONG EVIDENCE** as stored (the `grade_master` column). Rows graded UNVERIFIED, and rows carrying no verification object, stay internal until stamped. Relationships publish only when both endpoint entities publish; photographs and conflict notes publish with the entities they document.

Applied to Combined Graph Release 2026-11-15, that standard withholds **4,808 of the 8,296 union entities**: 623 rows the master grades "UNVERIFIED (no verification object)" and 4,185 build-only rows that carry no master grade. Also withheld by the endpoint rule: 6,458 relationships, 945 photographs, and 83 conflict notes attached to withheld entities. Nothing was relabeled to pass the filter — grades are carried exactly as stored, per store, and never merged.

What changed since v2.1 (2026-10-30): the underlying union grew — the November build carried the 762-edge relationship wiring merge and the build graph's growth to 4,812 entities — so this release adds **33 relationships, 8 photographs, and 2 fewer conflict notes** on the same 3,488 published entities (the canonical master has not moved; published-entity membership is unchanged). Version 2.1 (DOI 10.5281/zenodo.23822179) remains published as the dated historical version; versions are never silently rewritten. This v2.2 build is published to the GitHub mirror; its Zenodo deposit is pending the founder's token sitting, after which the concept DOI resolves to it.

## What this is

One record per person, place, work, institution, event, and practice in Black culture — Chicago first — drawn from CultureTechLens's two research stores and published as a single downloadable dataset. Every entity carries its type, a curated description, the grade each store assigned it, and both stores' identifiers. Grades are carried per store and **never merged**; where the two stores disagree, the disagreement ships in `conflicts.csv`, labeled and explained — nothing is blended, averaged, or silently picked.

The canonical public counts on culturetechlens.com remain the master store's (4,111 entities / 2,527 relationships). This dataset is the union view, restricted to verified rows — the diligence and research instrument — designated in *Combined Graph — Release 2026-11-15* and filtered under Phase 0 Amendment A1 (2026-10-30).

## Files

| File | Contents |
|---|---|
| `entities.csv` / `entities.json` | One row/object per entity (3,488): name, type, aliases, description, per-store grades, per-store IDs, conflict count, photo flag. JSON adds the full conflict notes and photo records. |
| `relationships.csv` / `relationships.json` | One row/object per relationship (2,628): with the store(s) attesting each edge; JSON adds evidence text where the source record carries it. |
| `conflicts.csv` | All 491 preserved disagreements attached to published entities: 236 grade divergences · 136 type conflicts · 83 name-form divergences · 16 duplicate-cluster notes (certain) · 12 fold notes · 4 duplicate-cluster notes (probable) · 4 split-record notes. |
| `photos.csv` | The per-image evidence record for each attached photograph (205): creator, source, license, credit line. By license: 111 public domain / CC0 / no known restrictions · 55 CC BY-SA · 39 CC BY. |
| `schema.json` | Machine-readable schema: file definitions, entity-type counts, grade-scale definitions. |
| `DATA-DICTIONARY.md` | Every column defined, both grade scales explained. |
| `CHANGELOG.md` | Version history. **Read the v2.1 entry before comparing counts across the v2.0 line** — the publication standard changed there, not the underlying graph. |
| `CITATION.cff` | Machine-readable citation metadata. |

## Terms

The dataset is published CC BY 4.0: use it, build on it, credit CultureTechLens and the DOI. The photographs are **not** covered by the dataset license — each carries its own license and credit line in `photos.csv`, and downstream use follows those terms. Living-person records rest on published, public sources; correction and takedown requests go to info@culturetechlens.com and are answered against the evidence record.

## Provenance

Built 2026-11-18 by a deterministic export of `combined-graph.json` (30,050,530 bytes; SHA-256 db942902a6546552c9208c424ce42fac26f53d1c5dedf809f0d24ffad903bcdf), the Release 2026-11-15 artifact — the union of the canonical master (4,111 / 2,527) and the build graph (4,812 / 6,740), matched only through the certified 2026-10-20 crosswalk, with the cleared photo layer folded in — filtered under Phase 0 Amendment A1 by the method of v2.1. The filter rule, the full grade census, and validation results are recorded in `BUILD-REPORT.md` in the release package. Identifiers: `union_id` (U-NNNNN) is the dataset ID. The two stores' own ID strings are **not** interchangeable (221 known collisions) — cite the union_id.

## Citation forms (per CTL-CITE-001; Chicago is CTL's primary style)

- **Chicago:** Maxey, William, and CultureTechLens. *CultureTechLens Black Cultural Knowledge Graph*. Version 2.2. Chicago: CultureTechLens NFP, 2026. https://doi.org/10.5281/zenodo.23403147.
- **APA:** Maxey, W., & CultureTechLens NFP. (2026). *CultureTechLens Black Cultural Knowledge Graph* (Version 2.2) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23403147
- **MLA:** Maxey, William, and CultureTechLens NFP. *CultureTechLens Black Cultural Knowledge Graph*. Version 2.2, Zenodo, 2026. doi:10.5281/zenodo.23403147.
