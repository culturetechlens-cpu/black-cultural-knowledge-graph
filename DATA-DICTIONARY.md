# CULTURETECHLENS
## "Culture, Clearly Seen." · Black Cultural Intelligence

# Data Dictionary — Black Cultural Knowledge Graph, Dataset v2.0

Cite as: CultureTechLens, "Data Dictionary — Black Cultural Knowledge Graph, Dataset v2.0," October 28, 2026.
Source: CultureTechLens.

## entities.csv / entities.json

| Column | Meaning |
|---|---|
| `union_id` | The dataset's own ID (U-NNNNN). The only ID that is safe to cite across versions. |
| `name` | The entity's headline name in the union. Where stores used different name forms, the master's form governs and the divergence is in `conflicts.csv`. |
| `type` | Entity type under the governing (master) typing. One of 22: Person, Work, Event, Institution, Outlet, Organization, Place, Business, Practice, Topic, School, Locality, Publication, Venue, Address, Church, Archive, List, Neighborhood, RadioStation, Technology, Policy. |
| `aliases` | Alternate names, semicolon-separated. |
| `description` | Curated description. Its source store is recorded in the underlying release artifact. |
| `grade_master` | The canonical master's grade: VERIFIED, STRONG EVIDENCE, or UNVERIFIED. Blank = the master holds no record of this entity. |
| `grade_build` | The build graph's grade under CTL-GOV-006 (see grade scales). Blank = the build graph holds no record. |
| `in_master` / `in_build` | Y/N store membership. 615 entities are in both; 3,496 master-only; 3,419 build-only. |
| `master_ids` / `build_ids` | Each store's own identifiers for this entity. **Not interchangeable** — the same CTL-E- string can name different entities in the two stores (221 known collisions). |
| `conflict_count` | How many preserved disagreements attach to this record (full text in the JSON and in `conflicts.csv`). |
| `has_photo` / `photo_asset_id` | Whether a rights-documented photograph is attached, and its asset ID where one has been minted. |

## relationships.csv / relationships.json

| Column | Meaning |
|---|---|
| `from_id` / `to_id` | `union_id`s of the connected entities; `from_name` / `to_name` repeat the names for readability. |
| `type` | Relationship type — 83 in use, e.g. `related_to`, `affiliated_with`, `located_in`, `honored_by`, `authored_by`, `founded_by`. |
| `evidenced_by` | Which store(s) attest the edge: `master`, `build`, or `master+build` (43 edges). The JSON form also carries evidence text where the source record has it. |

## conflicts.csv

| Column | Meaning |
|---|---|
| `class` | Grade divergence · Type conflict · Name-form divergence · Duplicate cluster (certain) · Duplicate cluster (probable) · Split-record pair · Fold · Date conflict. |
| `note` | The disagreement stated in full, both sides attributed to their store. Conflicts are disclosed, never resolved silently. |

## photos.csv

The per-image record CTL-PHOTO-001 requires: `asset_id`, `title`, `creator`, `date`, `collection`, `source_url`, `license` (short form), `rights` (the full rights statement from the source), and `credit` (the credit line that must travel with the image).

## The two grade scales — read this before using grades

- **Master scale:** VERIFIED / STRONG EVIDENCE / UNVERIFIED, assigned in the flagship research program.
- **Build scale (CTL-GOV-006):** Verified = at least two independent sources, at least one authoritative; anything less caps at Provisional, however good the single source is.
- A **grade divergence** (273 records) is one entity graded differently by the two stores. Both grades ship. There is no combined grade, by design, until the founder's grade-harmonization ruling lands.
