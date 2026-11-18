# CULTURETECHLENS
## "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — Black Cultural Knowledge Graph, Dataset v2.2

Cite as: CultureTechLens, "Data Dictionary — Black Cultural Knowledge Graph, Dataset v2.2," November 18, 2026.
Source: CultureTechLens.

## Scope note (new in v2.1, carried in v2.2)

Dataset v2.2 is a **verified-only** release, published under CTL Phase 0 as amended by Amendment A1 (2026-10-30). An entity row appears here only when its `grade_master`, as stored, is VERIFIED or STRONG EVIDENCE. Rows graded UNVERIFIED and rows carrying no master grade are withheld — not deleted, and not relabeled; they remain in the internal stores and in the dated v2.0 record (DOI 10.5281/zenodo.23753474). Relationships appear only when both endpoint entities appear; photographs and conflict notes appear with the entities they document. `grade_build` values are carried exactly as stored for the rows that publish — the build scale is a separate scale (see below) and was not used to determine eligibility.

## entities.csv / entities.json

| Column | Meaning |
|---|---|
| `union_id` | The dataset's own ID (U-NNNNN). The only ID that is safe to cite across versions. |
| `name` | The entity's headline name in the union. Where stores used different name forms, the master's form governs and the divergence is in `conflicts.csv`. |
| `type` | Entity type under the governing (master) typing. Eight types appear in v2.2: Person, Work, Event, Institution, Outlet, Place, Topic, List. (The v2.0 union carried 22 types; the remaining 14 types appear only on withheld rows.) |
| `aliases` | Alternate names, semicolon-separated. |
| `description` | Curated description. Its source store is recorded in the underlying release artifact. |
| `grade_master` | The canonical master's grade: VERIFIED, STRONG EVIDENCE, or UNVERIFIED. In v2.1 only VERIFIED (2,005) and STRONG EVIDENCE (1,483) rows appear. |
| `grade_build` | The build graph's grade under CTL-GOV-006 (see grade scales). Blank = the build graph holds no record. |
| `in_master` / `in_build` | Y/N store membership. In v2.1: 573 entities are in both stores; 2,915 master-only; 0 build-only (build-only rows carry no master grade and are withheld under Amendment A1). |
| `master_ids` / `build_ids` | Each store's own identifiers for this entity. **Not interchangeable** — the same CTL-E- string can name different entities in the two stores (221 known collisions). |
| `conflict_count` | How many preserved disagreements attach to this record (full text in the JSON and in `conflicts.csv`). |
| `has_photo` / `photo_asset_id` | Whether a rights-documented photograph is attached, and its asset ID where one has been minted. |

## relationships.csv / relationships.json

| Column | Meaning |
|---|---|
| `from_id` / `to_id` | `union_id`s of the connected entities; `from_name` / `to_name` repeat the names for readability. |
| `type` | Relationship type — 37 of the union's 83 types survive the endpoint filter in v2.1, e.g. `related_to`, `affiliated_with`, `located_in`, `honored_by`, `authored_by`, `founded_by`. |
| `evidenced_by` | Which store(s) attest the edge: `master`, `build`, or `build+master` (41 edges in v2.1). The JSON form also carries evidence text where the source record has it. |

## conflicts.csv

| Column | Meaning |
|---|---|
| `class` | Grade divergence · Type conflict · Name-form divergence · Duplicate cluster (certain) · Duplicate cluster (probable) · Split-record pair · Fold · Date conflict. |
| `note` | The disagreement stated in full, both sides attributed to their store. Conflicts are disclosed, never resolved silently. |

## photos.csv

The per-image record CTL-PHOTO-001 requires: `asset_id`, `title`, `creator`, `date`, `collection`, `source_url`, `license` (short form), `rights` (the full rights statement from the source), and `credit` (the credit line that must travel with the image).

## The two grade scales — read this before using grades

- **Master scale:** VERIFIED / STRONG EVIDENCE / UNVERIFIED, assigned in the flagship research program. This is the scale Phase 0 Amendment A1 names, and the scale v2.1 eligibility was read from.
- **Build scale (CTL-GOV-006):** Verified = at least two independent sources, at least one authoritative; anything less caps at Provisional, however good the single source is. Build grades are carried as stored; they are **not** mapped onto the master scale.
- A **grade divergence** (236 records in v2.1) is one entity graded differently by the two stores. Both grades ship. There is no combined grade, by design, until the founder's grade-harmonization ruling lands.
