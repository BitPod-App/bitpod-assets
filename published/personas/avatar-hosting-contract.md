# Published Persona Avatar Hosting Contract

Status: Active
Owner: BitPod published persona surfaces
Class: CANONICAL_STABLE

## Purpose

Define the minimum stable contract for serving public persona avatars through a
Cloudflare-controlled URL without exposing repo internals or raw storage
details.

## Public URL contract

Stable public avatar URLs should use this shape:

- `https://bitpod-avatar-worker.cjarguello.workers.dev/a/<public_id>`

Preferred future custom-domain shape:

- `https://bitpod.com/a/<public_id>`

## What the public surface must not expose

- local filesystem paths
- repo-relative asset paths
- raw working filenames beyond the stable public ID
- origin storage details

## Current canonical Taylor01 public ID

- `taylor01-hq`

Current source asset:

- `published/personas/taylor01/avatars/taylor01-hq-headset-avatar-square-v2.png`

Current published brand mark ID:

- `bitpod-mark`

## Scope rule

This hosting contract applies only to a small promoted subset of public persona
avatars.

It does not apply to:

- `bitgals/refs`
- `bitgals/approved`
- `bitgals/conditional`
- `bitgals/rejected`
- raw working media
- general internal-only persona assets
