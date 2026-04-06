# BitPod Assets Repo Structure Resolution

Status: Active
Date: 2026-04-05

## Decision

The repo root is now intentionally flat:

- `brand/`
- `published/`
- `bitgals/`
- `cloudflare/`
- `scripts/`

The old `assets/` root was removed because it was redundant inside the
`bitpod-assets` repo and made navigation unnecessarily confusing.

## Meaning

### `brand/`

BitPod brand/logo/guideline assets.

### `published/`

Operational assets that are live, wrapped by Cloudflare, or ready to be used at
any time.

This is not the identity-canon workflow.

### `bitgals/`

Reviewed BitGal identity/media canon.

This is the intake, review, organization, and anti-drift workflow for persona
media.

This is not the hosting/publishing lane.

### `cloudflare/`

Delivery adapters only.

Cloudflare hashed/signed avatar URLs should apply only to a small promoted
subset of published public persona avatars.

## Resolution rule

An asset may be:

- in `published/` without having gone through the full BitGals canon flow
- in `bitgals/` without being published or hostable
- in both, if it is both canonically useful and operationally live

Do not force those systems to be the same machine.

## Immediate implication

Future recovery of the avatar worker and avatar registry should target
`published/`, not the BitGals intake tree.
