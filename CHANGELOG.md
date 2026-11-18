# CULTURETECHLENS
## "Culture, Clearly Seen." · Black Cultural Intelligence

# Changelog — Black Cultural Knowledge Graph (Dataset)

Concept DOI: 10.5281/zenodo.23403147 (all versions). Cite as: CultureTechLens, "Changelog — Black Cultural Knowledge Graph (Dataset)," 2026. Source: CultureTechLens.

## v2.2 — 2026-11-18
**New source, same standard.** Built from *Combined Graph Release 2026-11-15* — the first union snapshot carrying the wired build graph (762-edge relationship merge landed; build graph at 4,812 entities / 6,740 relationships) — and filtered under Phase 0 Amendment A1 exactly as v2.1 was. No row was relabeled, merged, or edited to pass.
- 3,488 entities (unchanged from v2.1 — the canonical master has not moved, so published membership is the same 3,488 rows) · 2,628 relationships (from 2,595; +33 wiring-merge edges between published entities) · 205 photographs (from 197) · 491 conflict notes (from 493; the union's note total fell 576 → 574 in the November dedupe).
- Union before the filter: 8,296 entities · 9,086 relationships · 1,150 photographs · 574 conflict notes. Withheld: 4,808 entities (623 master-graded "UNVERIFIED (no verification object)" + 4,185 build-only rows with no master grade) · 6,458 relationships · 945 photographs · 83 conflict notes.
- Published on the GitHub mirror (culturetechlens-cpu/black-cultural-knowledge-graph) at build. Zenodo deposit pending the founder's token sitting; on deposit the concept DOI 10.5281/zenodo.23403147 resolves to this version and v2.1 (10.5281/zenodo.23822179) remains the dated historical version.

## v2.1 — 2026-10-30
**Publication-standard change — read before comparing counts.** The underlying graph did not shrink. On 2026-10-30 the founder extended CTL Phase 0 to dataset releases (Amendment A1): a dataset published under a CTL DOI may contain only rows graded **VERIFIED** or **STRONG EVIDENCE** as stored (`grade_master`). Version 2.1 is v2.0 filtered by that rule — no row was relabeled, merged, or edited to pass.
- 3,488 entities (from 7,530) · 2,595 relationships (from 7,998) · 197 photographs (from 832) · 493 conflict notes (from 576).
- Withheld entities: 4,042 — 623 graded "UNVERIFIED (no verification object)" by the master, and 3,419 build-only rows carrying no master grade. Relationships publish only when both endpoints publish (5,403 withheld); photographs and conflict notes publish with their entities (635 photographs, 83 conflict notes withheld).
- The eligibility grade is `grade_master`, the only column carrying the ruling's labels. Build-scale grades (`grade_build`: Verified / Provisional under CTL-GOV-006) are a different scale, are carried as stored for published rows, and were not mapped onto the ruling's labels. The full census — every grade value in both columns, with counts and dispositions — is in `BUILD-REPORT.md` in the release package.
- v2.0 (DOI 10.5281/zenodo.23753474) remains published as the dated, unfiltered combined-graph instrument; v2.1 supersedes it as the current citable release under the concept DOI.

## v2.0 — 2026-10-28
**Source change — read before comparing counts.** Versions 1.0–1.2 published the build graph alone. Version 2.0 is built from *CultureTechLens Combined Graph, Release 2026-10-28*: the union of the canonical CSV master (4,111 entities / 2,527 relationships) and the build graph (4,048 / 5,646), matched only through the certified 2026-10-20 crosswalk. The count jump (3,118 → 7,530 entities) is the wider source, not overnight growth.
- 7,530 entities · 7,998 relationships · 832 rights-documented photographs.
- New files: `conflicts.csv` (576 preserved disagreements, labeled — the stores' conflicts are disclosed, never blended), `photos.csv` (the per-image evidence records), and `CITATION.cff`.
- Grades carried per store (`grade_master`, `grade_build`); no combined grade exists.
- The public headline counts on culturetechlens.com remain the canonical master's 4,111 / 2,527; this dataset is the union view.
- Assembly note, stated for the record: two unpublished v2.0 builds were prepared on 2026-10-24 (a dataset export on Release 2026-10-22, and an artifact package). Both were superseded before publication by this single final build, which carries the Game Changers merge and the 2026-10-27 archive photo fold-in. Nothing from either earlier build was published.
- v1.3 (built 2026-10-16 from the build graph at 3,201 / 4,714) was staged as a draft and **never published**; v2.0 supersedes it.

## v1.2 — 2026-10-15 · DOI 10.5281/zenodo.23406848
Build graph: 3,118 entities · 4,698 relationships · 2,383 Verified / 735 Provisional · 8,174 source citations.

## v1.1 — 2026-10-15 · DOI 10.5281/zenodo.23405689
Build graph: 3,051 entities · 4,634 relationships.

## v1.0 — 2026-10-15 · DOI 10.5281/zenodo.23403148
First release under this concept DOI: build graph, 3,044 entities · 4,627 relationships.

*An earlier public edition (2026-10-06, 2,822 entities) was published under a separate record (DOI 10.5281/zenodo.23253532) before this lineage was established. This record — concept DOI 10.5281/zenodo.23403147 — is the dataset's single citable home.*
