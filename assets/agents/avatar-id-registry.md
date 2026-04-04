# Avatar ID Registry

Status: Active
Owner: BitPod brand and agent surfaces
Class: CANONICAL_STABLE

## Purpose

Define the stable public avatar IDs used by hosted avatar URLs and agent UI
surfaces.

This file is the canonical contract for:

- stable public avatar IDs
- semantic classification of agent avatars
- internal asset mapping to current repo files

## Core Rule

Public avatar URLs must use stable avatar IDs, not raw repo filenames.

Do not expose:

- local filesystem paths
- messy working filenames
- source image filenames from local working folders

## Identity Rule

Rule of thumb:

- if the image/avatar does not have blue hair, she is not `Taylor01`
- if the image/avatar does not have blue hair, classify her as a `BitGal`
  unless explicitly contracted otherwise

This rule is used for avatar naming, registry assignment, and hosted avatar URL
design.

## Public ID Scheme

Format:

- `<persona>-<variant>`

Examples:

- `taylor01-hq`
- `taylor01-main`
- `taylor01-runtime`
- `bitgal-orange-headset`
- `bitpod-mark`

Rules:

- lowercase only
- use hyphens, not underscores
- keep IDs short and stable
- IDs describe semantic identity, not local filenames
- do not append repo file extensions to the public ID
- do not rename an existing public ID casually once it is in use

## Current Registry

### Taylor01

These qualify as `Taylor01` avatars because they retain the blue-hair identity
contract.

| public_id | class | current_repo_asset |
| --- | --- | --- |
| `taylor01-hq` | Taylor01 canonical square avatar | `assets/agents/taylor01/png/taylor01-hq-gal-avatar-square-v1.png` |
| `taylor01-main` | Taylor01 personal square avatar | `assets/agents/taylor01/jpeg/taylor01-main-blue-avatar-square-v1.jpeg` |
| `taylor01-runtime` | Taylor01 runtime square avatar | `assets/agents/taylor01/jpeg/taylor01-runtime-avatar-square-v1.jpeg` |
| `taylor01-bitpod-headset` | Taylor01 square avatar with BitPod headset branding | `assets/agents/taylor01/png/taylor01-blue-headset-bitpod-square-v1.png` |
| `taylor01-genesis` | Taylor01 genesis/NFT square avatar | `assets/agents/taylor01/png/taylor01-genesis-nft-square-v1.png` |

### BitGals

These do not qualify as `Taylor01` under the blue-hair rule and should remain
in the `BitGal` lane.

| public_id | class | current_repo_asset |
| --- | --- | --- |
| `bitgal-orange-headset` | BitGal square avatar with orange hair/headset | `assets/agents/taylor01/png/taylor01-orange-bitpod-avatar-square-v1.png` |

### Brand Marks

These are not personae and should never be confused with Taylor01 or BitGal
identity.

| public_id | class | current_repo_asset |
| --- | --- | --- |
| `bitpod-mark` | BitPod square logo mark | `assets/agents/taylor01/png/bitpod-app-logo-square-v1.png` |

## Hosting Rule

Hosted avatar URLs should use the public ID from this registry and resolve
internally to the current repo asset or Cloudflare-managed asset ID.

Preferred external shape:

- `https://bitpod.com/a/<public_id>?exp=<unix_seconds>&h=<signature>`

The hosted surface should expose:

- stable public ID
- short-lived expiry
- short-lived hash/signature

The hosted surface should not expose:

- repo file path
- local working filename
- Cloudflare internal image ID if avoidable

## Update Rule

When a new avatar is added:

1. classify it as `Taylor01`, `BitGal`, or `Brand Mark`
2. assign a stable public ID
3. map that ID here to the current repo asset
4. only then wire the hosted URL layer

Do not mint hosted avatar URLs for unregistered images.
