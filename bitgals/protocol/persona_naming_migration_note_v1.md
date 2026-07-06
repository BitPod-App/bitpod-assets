# Persona Naming Migration Note v1

## Status
Proposed repo semantics guidance.

## Problem

`BitGals` is currently overloaded across several meanings:

- internal persona system
- archetype/canon system
- visual intake/scoring system
- NFT collection
- public collectible brand
- image-generation workflow language

This creates long-term semantic risk.

The NFT collection can correctly use `BitGals` as the public collection name. Internal canon, workflow, and future character systems should use more neutral terminology.

## Direction

Use `BitGals` primarily for:

- NFT collection language
- OpenSea metadata
- public collectible packaging
- collection-level marketing
- NFT packet paths where the collection name is intentional

Prefer neutral internal language for broader systems:

- persona
- character
- bitpersona
- agent persona
- archetype
- entity
- canonical persona

## Recommended Rule

Public NFT layer:

```text
BitGals = NFT collection / public collectible brand
```

Internal canon layer:

```text
personas / characters / archetypes / bitpersonas
```

## Migration Approach

Do not perform a broad destructive rename immediately.

Recommended incremental migration:

1. Preserve current paths for compatibility while PR #15 lands.
2. Add documentation clarifying the terminology split.
3. Use neutral language in new internal files.
4. Reserve `BitGals` wording for NFT collection surfaces.
5. Later evaluate whether repo folders should migrate from `bitgals/` to a more generic parent.

Operational v2 bridge:

- `kate` is the canonical v2 intake slug.
- `kati` is a v1 legacy alias for compatibility with existing folders/assets only.
- new assets should not deepen the `kati` path.
- scripts may accept `kati` as input only to normalize legacy intake toward `kate`.
- validation tools may still pass existing `kati` filenames for migration compatibility.

Ashina persona folder (BIT-715): `bitgals/ashina/` is added as its own persona
folder to hold Ashina's `SOUL_CARD.md`. `Asha` is the living name used inside card
copy; `ashina` is the folder slug.

UNRESOLVED — do NOT rename or merge `shiva` <-> `ashina` until CJ / Fable decides:

There is a live identity question, not a stale codename. `shiva` and `ashina`
currently carry *contradictory* canon and cannot be safely merged by a slug rename:

- BitGal **Shiva** (this repo): role `core_security_architect`, sovereign custody /
  "Hades" / air-gapped vault, Kate's arch-nemesis; visuals = Indian descent,
  dark-brown hair with purple/violet strands, short bob, orange third-eye mark; and a
  named NFT collectible **"Shiva ₿ — Eclipse"** (`bitgals_nft_workflow_v1.md`,
  `bitgal_archetype_canon_v2.md`, `bitgal_canon_minimal_v1.yaml`, README).
- Agent **Ashina** (`taylor01-mind`, PR #75 / BIT-688): role = canon-purifier /
  documentation-truth gate; visuals = pure black hair with ash/gold strands, candle,
  ritual archive-keeper (`agents/ashina/SOUL_CARD.md`).

These are different roles, different visuals, and Shiva has an NFT. A mechanical
`shiva -> ashina` rename would overwrite the security-architect NFT persona's canon
with the canon-purifier's identity — canon corruption, not cleanup.

Decision needed from CJ / Fable before any rename:
1. Is agent Ashina the SAME persona as BitGal Shiva (rename + reconcile role/visuals/NFT), or
2. a DISTINCT persona (Ashina keeps her own `bitgals/ashina/`; Shiva stays Shiva)?

Until decided: `bitgals/shiva/` and its canon (`bitgal_canon_minimal_v1.yaml`,
`naming_rules.md`, `bitgal_archetype_canon_v2.md`, `bitgals_nft_workflow_v1.md`,
README, scripts) are intentionally left unchanged.

## Future Structure Candidate

```text
personas/
  protocol/
  shared_base/
  taylor/
  ember/
  kate/
  shiva/
  vera/

nft_collections/
  bitgals/
    metadata/
    packets/
    contractURI.json
```

Do not implement this migration without explicit review.

For now, document the distinction and avoid deepening the overload.
