# BitGals NFT Workflow v1

## Status
Active workflow protocol.

This document defines the operating model for turning BitGals canon into NFT-ready assets and metadata without allowing metadata, prompts, or downstream tools to become competing sources of canon.

---

# Core Principle

NFTs are manifestations of the canon.
They are not the canon itself.

Canon defines:
- who each BitGal is
- what Bitcoin quality she represents
- mythology and archetype
- emotional read
- visual identity
- failure modes
- anti-drift constraints

NFT metadata packages a specific approved manifestation of that canon into collector-readable form.

---

# Source of Truth

GitHub is authoritative.

Active canon lives under:

```text
bitgals/protocol/
```

Current active files:

```text
bitgal_canon_minimal_v1.yaml
bitgal_archetype_canon_v2.md
persona_naming_migration_note_v1.md
bitgals_nft_workflow_v1.md
```

Planned NFT packet and metadata files should also live under `bitgals/protocol/`
until a future structure migration is explicitly approved. Expected future files
may include:

```text
bitgal_canon_v2.machine.json
opensea_metadata_template.bitgals.v1.json
opensea_metadata_template.bitgals.v2.json
trait_schema.bitgals.v1.json
variant_names.bitgals.v1.md
variant_rules.bitgals.v1.md
contractURI.bitgals.v1.json
```

Legacy Grok material lives under:

```text
bitgals/legacy/grok/
```

Legacy files are preserved for reference only. They are not active canon.

---

# Roles

## CJ

CJ owns:
- creative direction
- MoodAI base woman generation
- base identity approval
- canonical image approval
- final repo approval
- final NFT mint decisions

CJ controls the base identity and final acceptance.

## GPT / OpenAI

GPT/OpenAI-assisted work supports:
- canon organization
- anti-drift governance
- canonical image conversion from approved base images
- visual identity enforcement
- archetype and emotional-read evaluation
- repo structure updates
- workflow/protocol documentation

OpenAI image generation is used to convert approved MoodAI base images into one of the five canonical BitGals.

## Grok / SuperGrok

Grok/SuperGrok is the downstream NFT packaging assistant after canonical images are approved.

Grok may produce:
- OpenSea JSON
- contract metadata drafts
- NFT packet folders
- trait schemas
- variant name suggestions
- concise collector-facing copy
- optional lore/copy suggestions

Grok must not:
- override GitHub canon
- invent new BitGals
- revive the old 21-women structure
- redefine archetypes, mythology, or Bitcoin qualities
- treat draft copy as canon
- convert MoodAI base images into canonical BitGals unless explicitly asked

All Grok lore/copy suggestions must be marked:

```text
DRAFT — GROK PROPOSED / NOT CANON
```

Canon only becomes real after CJ approval and GitHub merge.

---

# Image Workflow

## 1. MoodAI Base Woman

CJ generates/provides high-quality base woman / identity-continuity candidates via MoodAI.

These are identity foundations, not final NFTs.

## 2. Base Approval

CJ and GPT evaluate the base image for identity continuity potential.

The approved base becomes the transformation anchor.

## 3. Canonical BitGal Conversion

OpenAI image generation converts the approved base into one canonical BitGal at a time:

- Taylor ₿
- Ember ₿
- Kate ₿
- Shiva ₿
- Vera ₿

Canonical image generation should happen one-by-one.

Do not batch-generate all personas or many variants before each Canonical A image is approved.

## 4. Canonical Review

Each candidate is reviewed for:
- same base woman
- required visual anchors
- archetype read
- emotional read
- scene fit
- failure-mode avoidance
- canon coherence

## 5. Canonical A Lock

Create one perfect Canonical A image per BitGal before producing variants.

Canonical A images are identity anchors for all future variants.

## 6. Grok Packaging

Only after CJ approves canonical images, Grok receives:
- approved image filename/path/CID
- persona
- variant name
- trait constraints
- metadata rules

Grok then creates NFT-ready metadata and packets.

---

# NFT Metadata Rules

Public metadata must stay lean.

Use OpenSea-compatible JSON fields:
- name
- description
- image
- external_url
- attributes

Recommended public traits:
- BitGal
- Variant
- Role
- Bitcoin Quality
- Mythology
- Archetype
- Hair
- Scene

Avoid:
- lore dumps
- rarity farming
- gaming rarity language
- random trait soup
- speculative marketplace psychology
- deep internal operational lore

Optimize for archetype fidelity.

Every NFT should feel like a valid state of the BitGal.

---

# Token Architecture

Current direction:
- ERC-721
- ERC-7572 contract-level metadata
- IPFS for images and token metadata JSON

ERC-721 is preferred because BitGals is a small, high-prestige, identity-driven collection.

ERC-7572 is preferred because contract-level metadata enables professional collection presentation, including collection description, banner, external links, and royalty information.

---

# Public Naming

Public NFT naming format:

```text
Name ₿ — Variant
```

Examples:

```text
Taylor ₿ — Signal
Ember ₿ — Fireblazer
Kate ₿ — Relay
Shiva ₿ — Eclipse
Vera ₿ — Proof
```

File naming uses lowercase snake_case and no special symbols:

```text
taylor_signal.json
ember_fireblazer.json
kate_relay.json
shiva_eclipse.json
vera_proof.json
```

---

# Final Operating Rule

Do not move to mass generation until the five Canonical A images are approved.

The next major phase after this PR is merged is:

1. Generate/approve Taylor Canonical A.
2. Generate/approve Ember Canonical A.
3. Generate/approve Kate Canonical A.
4. Generate/approve Shiva Canonical A.
5. Generate/approve Vera Canonical A.
6. Only then create variants and NFT packets.
