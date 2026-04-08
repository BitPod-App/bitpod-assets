# GPT Handoff: BitPod Assets Structure Resolution

Use this as the current repo-grounded structure decision.

## Resolved root model

The canonical repo root is now:

- `brand/`
- `published/`
- `bitgals/`
- `cloudflare/`
- `scripts/`

Do not reintroduce an extra `assets/` wrapper.

The old `assets/...` root was caused by shorthand confusion about the repo name
and is no longer canonical.

## Purpose split

There are two distinct media systems in this repo.

### 1. `published/`

This is the live/hostable/use-now machine.

Use it for:

- assets already wrapped by Cloudflare
- assets already in live use
- assets that are ready to be used operationally at any time

This is not the BitGals identity-canon workflow.

Current intended top-level buckets:

- `published/branding/`
- `published/personas/`

### 2. `bitgals/`

This is the reviewed BitGal identity-canon workflow.

Use it for:

- persona continuity
- anti-drift references
- reviewed intake
- approved vs conditional vs rejected organization
- avatars vs stills vs video separation
- sidecar metadata

This is not the hosting/publishing lane.

## Relationship between the two

An asset may be:

- in `published/` without having gone through the full BitGals canon pipeline
- in `bitgals/` without being published or hostable
- in both, if it is both canonically useful and operationally live

Do not force those systems to be the same machine.

## Cloudflare rule

Cloudflare signed/hashed avatar URLs should apply only to a small promoted
subset of published public persona avatars.

They should not be the front door for the entire BitGals library.

## What to preserve from the newer design

Keep:

- the `bitgals/` persona folder system
- `refs`, `approved`, `conditional`, `rejected`, `avatars`, `videos`
- sidecar metadata next to assets
- `scripts/bitgals_scaffold.py`
- `scripts/bitgals_intake.py`
- `scripts/bitgals_validate.py`
- human review as the real pass/fail gate

## What to keep narrow

Keep narrow:

- avatar registry
- public avatar IDs
- Cloudflare avatar worker

That is a downstream published-avatar surface, not the whole repo architecture.
