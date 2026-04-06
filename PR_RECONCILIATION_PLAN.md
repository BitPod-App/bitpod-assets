# BitPod Assets PR Reconciliation Plan

Status: Active
Date: 2026-04-05

## Goal

Reconcile the two open PR lanes in `bitpod-assets` without reintroducing path
confusion or collapsing distinct systems together.

Relevant PRs:

- PR #5 — [BIT-237] Add avatar registry and Cloudflare avatar worker scaffold
- PR #6 — [codex] Add minimal BitGals ingestion workflow

## Executive conclusion

- PR #6 is the correct base for the BitGals identity-canon workflow and should
  be treated as the active internal media system.
- PR #5 should **not** be merged as-is.
- Only a narrow subset of PR #5 should be salvaged:
  - avatar public ID registry concept
  - avatar hosting contract concept
  - Cloudflare avatar worker scaffold
  - signed public URL helper
- Those salvaged pieces must be retargeted to the new root layout and to the
  `published/` lane, not the BitGals canon tree.

## Current implementation status

Part of that reconciliation is now implemented locally:

- repo root flattened to `brand/`, `published/`, `bitgals/`, `cloudflare/`,
  `scripts/`
- `published/` exists as the operational asset lane
- the avatar worker has been restored against `published/`
- the first stable public route is live for `taylor01-hq`

## Why PR #6 stays

PR #6 is the reviewed BitGals media system:

- persona-separated folders
- review buckets
- avatar/image/video separation
- standardized naming
- sidecar metadata
- scaffold/intake/validate scripts
- human-in-the-loop workflow

That system is useful now and matches the intended purpose of BitGals canon:

- preserve identity continuity
- reduce drift
- organize reviewed media
- support future generation/reference work

## Why PR #5 cannot be merged directly

PR #5 was cut from an older branch base.

When compared against current `main`, it does all of these at once:

- adds avatar registry/worker files
- adds `assets/agents/...`
- deletes the BitGals intake tree
- deletes the BitGals scripts

That means PR #5 is not a safe “merge the worker” PR anymore.
It is a stale branch carrying both useful work and destructive history.

## Canonical system split

The repo now has three distinct media lanes:

### `brand/`

BitPod brand assets and supporting docs.

### `bitgals/`

Identity-canon and reviewed persona media organization.

This answers:

- what is canonically useful
- what should future media learn from
- what passed review as reference/approved/conditional/rejected

### `published/`

Operational asset inventory.

This answers:

- what is live
- what is hostable
- what is Cloudflare-wrapped
- what can be used right now

## Promotion rule

Promotion into `published/` is a separate decision from BitGals review.

An asset may be:

- in `bitgals/` only
- in `published/` only
- in both

Do not force the BitGals review system to be the acceptance gate for all live
assets.

## What to salvage from PR #5

Keep the following ideas and files, but port them to the corrected repo model.

### Concepts to keep

- stable public avatar IDs
- machine-readable avatar registry
- short-lived signed public URLs
- thin Cloudflare Worker for serving public avatar bytes
- worker can serve bundled local assets first
- Cloudflare Images remains optional later

### Files to salvage conceptually

- `cloudflare/avatar-worker/README.md`
- `cloudflare/avatar-worker/src/index.js`
- `cloudflare/avatar-worker/scripts/sign-public-url.mjs`
- `cloudflare/avatar-worker/wrangler.toml`
- avatar registry and contract docs
- one canonical public avatar asset for first-path testing

## What not to salvage from PR #5

Do not revive these as the canonical shape:

- `assets/agents/...`
- any repo path rooted under `assets/...`
- the idea that the avatar worker is the front door to all persona media
- the branch’s deletions of `bitgals/` and `scripts/`

## Target landing shape after reconciliation

### BitGals canon stays here

- `bitgals/`

### Public/live persona assets land here

- `published/personas/<persona>/avatars/`
- `published/personas/<persona>/images/`
- `published/personas/<persona>/video/`

### Public/live branding assets can land here

- `published/branding/`

### Worker remains here

- `cloudflare/avatar-worker/`

## Narrow first implementation

The first hosted/public avatar lane should be tiny.

Recommended first live item:

- `published/personas/taylor01/avatars/taylor01-hq-headset-avatar-square-v2.png`

Recommended first public ID:

- `taylor01-hq`

## Required retargeting for salvaged worker files

Any registry/contract/worker code taken from PR #5 must be rewritten to point
at `published/`, not `assets/agents/`.

Examples:

- old: `assets/agents/taylor01/png/taylor01-hq-headset-avatar-square-v2.png`
- new: `published/personas/taylor01/avatars/taylor01-hq-headset-avatar-square-v2.png`

## Recommended execution order

1. Keep current `bitgals/` and scripts as the active internal media system.
2. Create `published/personas/taylor01/` structure.
3. Port the narrow worker/registry files from PR #5.
4. Retarget them to `published/`.
5. Start with one canonical public avatar only.
6. Verify signed URL generation and Worker serving.
7. Only later expand to more avatars or more personas.

## Decision summary

- Merge/adopt PR #6 behaviorally.
- Do not merge PR #5 mechanically.
- Rebuild PR #5’s useful subset on top of the corrected root layout.
