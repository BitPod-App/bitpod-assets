# Taylor Hair Edit Prompts v1

## Standard hair-color patch

Use this fragment when patching a broader Taylor prompt:

```text
Hair color target:
bright electric cyan-blue, anchored to a vivid synthetic neon blue rather than teal, turquoise, cobalt, navy, or pastel blue. High brightness, high saturation, cool-toned, clean and luminous. The hair should read immediately as electric blue in normal lighting, with only slight natural variation in strands and shadows. Avoid green drift, avoid dark blue drift, avoid purple drift.
```

## Standard image-edit prompt

Use this for mutation of existing Taylor images:

```text
EDIT the provided image. Do not generate a new person.

Keep exactly the same:
- face
- identity
- expression
- pose
- framing
- lighting realism
- skin tone and texture
- hairstyle and strand structure

Only change:
- hair color → vivid electric cyan-blue

Color requirements:
- bright, saturated, cool-toned electric blue
- closer to neon sky blue than teal
- no greenish turquoise drift
- no dark cobalt drift
- no lavender or purple shift
- maintain realistic shading and natural strand variation

Output must remain fully photorealistic.
```

## Stronger full edit prompt

Use this when the model tends to drift:

```text
Change only the hair color to a vivid electric cyan-blue anchored to a bright neon synthetic blue. Keep the exact same hairstyle, strand structure, realism, face, identity, lighting, and proportions. The blue should be cool-toned, bright, saturated, and luminous, clearly more electric-blue than teal or turquoise. Avoid dark cobalt, navy, pastel blue, or purple-blue drift. Preserve realistic hair texture and natural shadow variation.
```

## Review checklist

Approve only when all are true:

- identity preserved
- same person, not a regeneration drift
- hair shape preserved
- strand structure preserved
- color reads instantly as electric blue
- no teal drift
- no cobalt/navy drift
- no purple drift
- realism preserved

## Rejection shorthand

Use these labels during review:

- `REJECT — teal drift`
- `REJECT — too dark`
- `REJECT — too pastel`
- `REJECT — purple drift`
- `REJECT — identity drift`
- `REJECT — hair structure changed`
- `APPROVE — canon match`
```
