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

`shiva` is LEGACY — the retired former name of this same persona (CJ, 2026-07-06):

`ashina` is canonical. `shiva` is the old identity that was renamed to Ashina
elsewhere (agent side: `taylor01-mind` PR #75 / BIT-688). Mentions of `shiva` were
already scrubbed across most surfaces; `bitpod-assets` was simply overlooked because
few people look here and it holds little logic (mostly a few Cloudflare-published
public image URLs — logo / avatar / emoticon). They are the SAME persona, not rivals.

Intentionally retained as legacy for now (do NOT delete):

- the NFT collectible **"Shiva ₿ — Eclipse"** (`bitgals_nft_workflow_v1.md`) and the
  old security-architect / "Hades" archetype lore (`bitgal_archetype_canon_v2.md`).
  That NFT project is not expected to be touched for ~1 year; it will eventually be
  replaced by an **"Asha ₿ — Ink of the Sun"** once Asha has enough lore and visuals.
  Ashina's doctrine keeps legacy as history, not active law.

Deferred low-priority legacy scrub (fine for someone else to do later, per CJ):

- rename `bitgals/shiva/` (empty `.gitkeep` scaffold) to `bitgals/ashina/`, and update
  the remaining operational `shiva` references (`bitgal_canon_minimal_v1.yaml`,
  `naming_rules.md`, `codex_handoff.md`, `review_checklist.md`, README persona line,
  and the `scripts/bitgals_*.py` PERSONAS/regex) to canonical `ashina`, keeping `shiva`
  only as a legacy-accepted alias where old assets/NFT surfaces still need it.

This PR does NOT do that scrub — it only ADDS `bitgals/ashina/SOUL_CARD.md`. The
scrub is left untouched here so this change stays additive and low-risk.

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
