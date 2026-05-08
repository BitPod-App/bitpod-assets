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
