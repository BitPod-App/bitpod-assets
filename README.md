# BitPod Assets

Public asset host for BitPod org/profile and design starter materials.

## Canonical structure

- `assets/brand/logo/svg/` — logo marks + lockups
- `assets/brand/guidelines/` — brand guidance docs
- `assets/brand/figma/` — Figma handoff docs
- `assets/brand/social/repo-previews/` — repo social preview images
- `assets/agents/` — agent avatar assets, registry, and hosting contract
- `assets/brand/brand-asset-manifest.txt` — starter package manifest
- `assets/brand/asset-provenance.md` — ownership/source/status metadata
- `assets/brand/BRAND_FREEZE_PHASE1.md` — no-redesign freeze note for phase 1

## Agent avatar lane

Current agent/avatar canon now lives under:

- `assets/agents/`

Current stable-contract files:

- `assets/agents/avatar-id-registry.md`
- `assets/agents/avatar-id-registry.json`
- `assets/agents/avatar-hosting-contract.md`

Current edge scaffold for hosted avatar delivery:

- `cloudflare/avatar-worker/`

## Import source and parity

Current Phase 1 working source imported from:

- `$WORKSPACE/local-workspace/local-working-files/bitpod_brand_starter_fixed.zip`

Superseded source (not canonical):

- `bitpod_brand_starter.zip` / folder variant `bitpod_brand_starter`

Intentional repo additions beyond package import:

- `assets/brand/README.md`
- `assets/brand/social/repo-previews/bitpod-tools-preview.png`
- `assets/brand/social/repo-previews/sector-feeds-preview.png`
- `assets/brand/asset-provenance.md`
- `assets/brand/BRAND_FREEZE_PHASE1.md`

## Priority previews

- `assets/brand/social/repo-previews/bitpod-tools-preview.png`
- `assets/brand/social/repo-previews/sector-feeds-preview.png`

## Update policy

- Phase 1: install/import starter assets with minimal modification.
- Phase 2+: normalize names/exports only with explicit decision records.
- Keep originals editable and avoid destructive overwrites.

## Phase 1 freeze

- Placeholder identity is intentional for Phase 1.
- No logo/visual redesign in this phase.
- Redesign and normalization work is deferred to [BIT-57](https://linear.app/bitpod-app/issue/BIT-57/brand-assets-phase-2-naming-normalization-export-workflow-figma-import).
