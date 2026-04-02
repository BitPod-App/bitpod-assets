# BitPod Avatar Worker

Cloudflare Worker scaffold for serving BitPod-controlled avatar URLs from
`bitpod.com` using stable public avatar IDs.

Canonical inputs:

- [avatar-id-registry.md](/Users/cjarguello/BitPod-App/bitpod-assets/assets/agents/avatar-id-registry.md)
- [avatar-id-registry.json](/Users/cjarguello/BitPod-App/bitpod-assets/assets/agents/avatar-id-registry.json)
- [avatar-hosting-contract.md](/Users/cjarguello/BitPod-App/bitpod-assets/assets/agents/avatar-hosting-contract.md)

## Public URL shape

- `https://bitpod.com/a/<public_id>?exp=<unix_seconds>&h=<signature>`

## Current behavior

- validates `public_id` against the registry
- validates `h` as an HMAC-SHA256 signature of `<public_id>:<exp>`
- rejects expired or over-long public URLs
- signs the private Cloudflare Images delivery URL internally
- proxies the image bytes instead of redirecting to Cloudflare Images
- returns `503` when the avatar is registered but not yet wired to Cloudflare

## Required secrets/config

- `AVATAR_URL_SIGNING_SECRET`
- `IMAGES_SIGNING_KEY`
- `CLOUDFLARE_IMAGES_ACCOUNT_HASH`
- optional:
  - `CLOUDFLARE_IMAGES_VARIANT`
  - `MAX_PUBLIC_URL_TTL_SECONDS`

## Current status

This is a scaffold only.

It does not deploy anything by itself and does not yet populate
`cloudflare_image_id` values in the registry.

## Local helper

Generate a signed public BitPod avatar URL:

```bash
AVATAR_URL_SIGNING_SECRET=... node scripts/sign-public-url.mjs taylor01-hq
```
