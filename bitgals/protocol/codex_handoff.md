# Codex Handoff — BitGals v2 bridge (with v1 compatibility)

Implement a minimal ingestion system for `bitgals/` with active v2 personas and v1 compatibility preserved only for legacy aliases.

## Goal
Do not build a giant platform.
Build a small helper system that:
1. scaffolds persona folders
2. validates filenames
3. creates metadata sidecars
4. routes assets into `avatars/`, `approved/`, `conditional/`, `rejected/`, or `videos/`
5. supports a manual human score and decision flow

Validation rules for v2 (with v1 compatibility):
- `refs/` accepts still-image reference assets of type `image` and `avatar`
- `refs/` does not accept `video`
- metadata sidecars live next to each asset by default
- `metadata/` folders stay in the scaffold but are not a default intake destination
- `kati` is accepted only as a v1 legacy alias for existing legacy assets

## Required folders
For each active persona (`taylor`, `ember`, `kate`, `shiva`, `vera`) create:
- `refs/`
- `approved/`
- `conditional/`
- `rejected/`
- `avatars/`
- `videos/`
- `metadata/`

Compatibility bridge:
- `kati` is a legacy alias for `kate`.
- New intake should use `kate` and target the `kate` folder.
- Legacy scripts may accept `kati` inputs and normalize to `kate` for existing v1 assets only.

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
