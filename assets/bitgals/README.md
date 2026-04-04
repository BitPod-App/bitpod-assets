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
- `ember` — performer/creator, motion, orange hair, stage energy
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
- `{persona}/refs/` — strong canonical still-image references (`image` or `avatar`, not `video`)
- `{persona}/approved/` — official images
- `{persona}/conditional/` — near-misses worth keeping
- `{persona}/rejected/` — failed outputs
- `{persona}/avatars/` — square avatar-ready stills
- `{persona}/videos/` — approved video files
- `{persona}/metadata/` — reserved for future use; sidecar JSON lives next to each asset by default in v1

## Review policy
- Official pass: total >= 90
- Conditional review: 85–89
- Reject: < 85
- Hard fail if it is the wrong persona, not the same base woman, missing a required anchor, or reads like generic AI portrait slop.

## Note
This is intentionally small. Start manual. Automate later.

## Script usage
Scaffold the folder tree:

```bash
python3 scripts/bitgals_scaffold.py
```

Intake an asset:

```bash
python3 scripts/bitgals_intake.py /path/to/source.png \
  --persona ember \
  --type image \
  --scene stage \
  --look singing \
  --decision approved \
  --base-identity 94 \
  --persona-score 92 \
  --confusion-score 4 \
  --total-score 93 \
  --notes "Strong performer read"
```

Preview intake without copying:

```bash
python3 scripts/bitgals_intake.py /path/to/source.mp4 \
  --persona ember \
  --type video \
  --scene stage \
  --look performance \
  --decision approved \
  --total-score 91 \
  --dry-run
```

Validate a BitGals filename or asset path:

```bash
python3 scripts/bitgals_validate.py assets/bitgals/ember/approved/ember_image_stage_singing_v01.png
python3 scripts/bitgals_validate.py assets/bitgals/taylor/avatars/taylor_avatar_hq_black-suit_v01.png
```
