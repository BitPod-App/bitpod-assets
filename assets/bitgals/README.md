# BitGals

Minimal canon system for BitPod character assets.

## Purpose
This folder is the source of truth for BitGal media organization.

The goal is simple:
- keep one shared base woman across all personas
- prevent persona drift
- standardize naming, placement, and review
- make future ingestion easy for Codex

## Personas
- `taylor` — chief of staff, symmetry, white HQ, cobalt hair
- `orange` — performer/creator, motion, orange hair, stage energy
- `kati` — sound engineer/DJ/repair, texture, green-turquoise hair, purple eyes, gold-heavy styling
- `shiva` — dark narrator, lighting, short purple hair, silver styling
- `vera` — QA engineer, structure, brunette, glasses, tech-office scenes

## Canon files
- `protocol/bitgal_canon_minimal_v1.yaml` — machine-readable canon and thresholds
- `protocol/metadata_template.json` — sidecar metadata shape
- `protocol/review_checklist.md` — fast human review
- `protocol/naming_rules.md` — naming and filing rules
- `protocol/codex_handoff.md` — implementation brief for Codex

## Folder intent
- `shared_base/` — anchor images of the base woman
- `{persona}/refs/` — strong canonical references
- `{persona}/approved/` — official images
- `{persona}/conditional/` — near-misses worth keeping
- `{persona}/rejected/` — failed outputs
- `{persona}/avatars/` — square avatar-ready stills
- `{persona}/videos/` — approved video files
- `{persona}/metadata/` — JSON sidecars if not stored next to file

## Review policy
- Official pass: total >= 90
- Conditional review: 85–89
- Reject: < 85
- Hard fail if it is the wrong persona, not the same base woman, missing a required anchor, or reads like generic AI portrait slop.

## Note
This is intentionally small. Start manual. Automate later.
