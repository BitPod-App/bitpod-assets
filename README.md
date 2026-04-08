# BitPod Assets

Public asset repo for BitPod brand assets, published/live media, and BitGals
identity canon.

## Canonical structure

- `brand/` — BitPod brand assets, guidelines, Figma handoff, and previews
- `published/` — operational assets that are live, hostable, or ready to ship
- `bitgals/` — reviewed BitGal identity/media canon and intake workflow
- `cloudflare/` — delivery adapters such as the avatar worker
- `scripts/` — repo-local asset workflow scripts

## Purpose split

There are two different media machines in this repo:

- `published/` answers: what can we serve or use right now?
- `bitgals/` answers: what should future persona media learn from?

Do not collapse those into one approval system.

`brand/` stays separate from both because org/brand assets are not persona
media.

## Import source and parity

Current Phase 1 working source imported into `brand/` from:

- `$WORKSPACE/local-workspace/local-working-files/bitpod_brand_starter_fixed.zip`

Superseded source (not canonical):

- `bitpod_brand_starter.zip` / folder variant `bitpod_brand_starter`

Intentional repo additions beyond package import:

- `brand/README.md`
- `brand/social/repo-previews/bitpod-tools-preview.png`
- `brand/social/repo-previews/sector-feeds-preview.png`
- `brand/asset-provenance.md`
- `brand/BRAND_FREEZE_PHASE1.md`

## Priority previews

- `brand/social/repo-previews/bitpod-tools-preview.png`
- `brand/social/repo-previews/sector-feeds-preview.png`

## Update policy

- Phase 1: install/import starter assets with minimal modification.
- Phase 2+: normalize names/exports only with explicit decision records.
- Keep originals editable and avoid destructive overwrites.

## Phase 1 freeze

- Placeholder identity is intentional for Phase 1.
- No logo/visual redesign in this phase.
- Redesign and normalization work is deferred to [BIT-57](https://linear.app/bitpod-app/issue/BIT-57/brand-assets-phase-2-naming-normalization-export-workflow-figma-import).
