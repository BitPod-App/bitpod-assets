# Taylor01 Hermes Dashboard Favicons

Canonical favicon package for the Taylor01 / T01 Hermes Dashboard and related Hermes operator pages.

These assets live under `brand/favicons/` because they are app presentation
assets for the Hermes operator surface, not persona media and not Cloudflare
worker inputs. Runtime services may copy or serve these files same-origin so
browsers and installed app shortcuts resolve the Taylor01 favicon consistently.

## Active package

- Published on 2026-06-05 from `taylor01_svg_gradient_canonical_favicon_pack.zip`.
- `source/taylor01-hermes-dashboard-favicon-pack.zip` preserves the supplied favicon pack under a repo-normalized filename.
- `runtime/` preserves the extracted browser/runtime favicon package and keeps standard web favicon filenames.
- This SVG-gradient package supersedes the earlier T01 Access Hub favicon publication surface.

## Runtime exports

`runtime/` contains:

- `favicon.svg`
- `favicon.ico`
- `favicon-16x16.png`
- `favicon-32x32.png`
- `favicon-48x48.png`
- `favicon-64x64.png`
- `favicon-96x96.png`
- `favicon-128x128.png`
- `favicon-256x256.png`
- `apple-touch-icon.png`
- `android-chrome-192x192.png`
- `android-chrome-512x512.png`
- `site.webmanifest`
- `html-head-snippet.txt`
