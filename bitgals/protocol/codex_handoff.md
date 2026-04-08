# Codex Handoff — BitGals v1

Implement a minimal ingestion system for `bitgals/`.

## Goal
Do not build a giant platform.
Build a small helper system that:
1. scaffolds persona folders
2. validates filenames
3. creates metadata sidecars
4. routes assets into `avatars/`, `approved/`, `conditional/`, `rejected/`, or `videos/`
5. supports a manual human score and decision flow

Validation rules for v1:
- `refs/` accepts still-image reference assets of type `image` and `avatar`
- `refs/` does not accept `video`
- metadata sidecars live next to each asset by default
- `metadata/` folders stay in the scaffold but are not a default intake destination

## Required folders
For each persona (`taylor`, `ember`, `kati`, `shiva`, `vera`) create:
- `refs/`
- `approved/`
- `conditional/`
- `rejected/`
- `avatars/`
- `videos/`
- `metadata/`

Also create:
- `bitgals/shared_base/`
- `bitgals/protocol/`

## Minimal CLI ideas
### 1. scaffold
Creates missing folders.

### 2. intake
Inputs:
- file path
- persona
- asset type
- scene
- look
- decision
- scores

Outputs:
- normalized filename
- copied/moved asset into correct folder
- metadata sidecar JSON

### 3. validate
Checks:
- extension allowed for type
- persona valid
- filename valid
- destination folder valid

## Decision logic
- Approved if total >= 90 and no hard-fail
- Conditional if 85-89 and no hard-fail
- Rejected otherwise
- Hard fail if:
  - wrong persona read
  - not same base woman
  - missing required anchor
  - generic AI portrait slop

## Important
This is a human-in-the-loop system.
Do not pretend to fully automate visual judgment yet.
The tool should support manual scoring first.

## Suggested first files
- `scripts/bitgals_scaffold.py`
- `scripts/bitgals_intake.py`
- `scripts/bitgals_validate.py`
