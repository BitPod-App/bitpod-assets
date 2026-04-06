# Published Persona Avatar ID Registry

Status: Active
Owner: BitPod published persona surfaces
Class: CANONICAL_STABLE

## Purpose

Define the stable public avatar IDs used by public persona avatar URLs.

This registry is intentionally narrow. It is for the tiny subset of persona
avatars that are actually published or ready to be published.

It is not the BitGals review/canon system.

## Public ID rule

Public avatar URLs use stable IDs, not raw filenames.

Format:

- `<persona>-<variant>`

Examples:

- `taylor01-hq`

## Current registry

| public_id | class | current_repo_asset |
| --- | --- | --- |
| `taylor01-hq` | Taylor01 canonical public square avatar | `published/personas/taylor01/avatars/taylor01-hq-headset-avatar-square-v2.png` |
| `bitpod-mark` | BitPod published square mark | `published/branding/marks/bitpod-app-logo-square-v1.png` |

## Hosting rule

The stable public route shape is:

- `https://bitpod-avatar-worker.cjarguello.workers.dev/a/<public_id>`

Later, this can move behind `bitpod.com` without changing the public ID.

## Classification note

This registry should remain small and operational.

If an image is useful for identity continuity or generation guidance but is not
actually published, it belongs in `bitgals/`, not here.
