# BitPod Avatar Worker

Cloudflare Worker for serving stable public persona avatar routes.

Canonical inputs:

- `/Users/taylor01/BitPod-App/bitpod-assets/published/personas/avatar-id-registry.md`
- `/Users/taylor01/BitPod-App/bitpod-assets/published/personas/avatar-id-registry.json`
- `/Users/taylor01/BitPod-App/bitpod-assets/published/personas/avatar-hosting-contract.md`

## Public URL shape

- `https://bitpod-avatar-worker.cjarguello.workers.dev/a/<public_id>`

Preferred future custom-domain shape:

- `https://bitpod.com/a/<public_id>`

## Current behavior

- validates `public_id` against the registry
- serves a bundled Worker asset when `worker_asset_path` is present, including
  explicitly promoted still or animated avatar assets
- returns `404` for unknown IDs
- returns `503` when an ID exists but has no bundled worker asset

## Design note

This Worker intentionally serves a tiny stable subset of published persona
avatars.

It is not the front door to the full BitGals library.

Animated avatar previews are allowed only when they are listed in
`published/personas/avatar-id-registry.json` and copied into `public/__avatars/`.

## Local validation

```bash
PATH="/opt/homebrew/opt/node@20/bin:$PATH" npx wrangler deploy --dry-run
PATH="/opt/homebrew/opt/node@20/bin:$PATH" npx wrangler dev
```
