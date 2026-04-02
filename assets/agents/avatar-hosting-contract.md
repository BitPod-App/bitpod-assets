# Avatar Hosting Contract

Status: Active
Owner: BitPod brand and agent surfaces
Class: CANONICAL_STABLE

## Purpose

Define the minimum stable contract for serving BitPod agent avatars from
`bitpod.com` without exposing local repo paths, raw working filenames, or
Cloudflare internal IDs.

This file is the public-hosting companion to:

- `assets/agents/avatar-id-registry.md`
- `assets/agents/avatar-id-registry.json`

## External URL Contract

Hosted avatar URLs should use this shape:

- `https://bitpod.com/a/<public_id>?exp=<unix_seconds>&h=<signature>`

Where:

- `<public_id>` is the stable avatar ID from the registry
- `exp=<unix_seconds>` is the public URL expiry
- `h=<signature>` is a short-lived signature generated server-side over
  `<public_id>:<exp>`

The external URL must not expose:

- local filesystem paths
- repo-relative asset paths
- raw source filenames
- Cloudflare internal image IDs, if avoidable

## Current Canonical ID For Taylor01

Current preferred public ID for Taylor01's main UI avatar:

- `taylor01-hq`

Current source asset:

- `assets/agents/taylor01/png/taylor01-hq-gal-avatar-square-v1.png`

## Cloudflare Design

Preferred hosting design:

1. store the image in Cloudflare Images as a private image
2. keep a server-side map from `public_id` -> `cloudflare_image_id`
3. serve through `bitpod.com`
4. validate the signature server-side
5. sign the private Cloudflare Images URL server-side
6. proxy the image bytes instead of redirecting, so Cloudflare image IDs stay
   hidden from the public surface

## Stable ID Rule

Public ID stability matters more than repo filename stability.

This means:

- repo files may be replaced later
- Cloudflare image IDs may be replaced later
- the public ID should remain stable when the user-facing identity is the same

## Classification Rule

Identity classification must follow the registry rule:

- if the avatar does not have blue hair, she is not `Taylor01`
- non-blue-hair variants should default to `BitGal` unless explicitly
  contracted otherwise

## Implementation Minimum

Any future worker or edge adapter should:

1. accept only registered `public_id` values
2. reject unknown IDs with `404`
3. verify `h`
4. resolve `public_id` using the machine-readable registry
5. never expose local repo paths in the response surface

## Deferred

This contract intentionally does not decide yet:

- the exact default TTL beyond "short-lived"
- whether the path should later rename from `/a/` to another short surface

Those choices can be made later without changing the core public ID contract.
