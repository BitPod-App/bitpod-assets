# Published Asset Promotion Policy

Status: Active

## Purpose

Define how assets become part of the `published/` inventory.

## Principle

`published/` is the operational inventory, not the identity-canon workflow.

That means an asset may be promoted into `published/` because it is:

- already live
- already referenced by product surfaces
- already wrapped by Cloudflare
- approved for immediate use

It does **not** have to come from the full BitGals canon process first.

## Current buckets

- `published/branding/`
- `published/personas/`
- `published/bitgals/`

## Typical promotion paths

### From BitGals canon

If an asset in `bitgals/` becomes operationally useful, copy or export it into
the correct `published/` location.

### From legacy or ad hoc use

If an asset is already live or needed immediately, it may be promoted directly
into `published/` without first being stored in `bitgals/`.

## Rule

Do not confuse:

- `bitgals/` = identity continuity and anti-drift review
- `published/` = live, hostable, use-now inventory
