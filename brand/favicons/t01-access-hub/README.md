# T01 Access Hub Favicons

Canonical favicon assets for the Taylor01 T01 Access Hub.

These assets live under `brand/favicons/` because they are presentation/identity
assets for an app surface, not public persona media and not Cloudflare worker
inputs. A consuming app may generate or copy deployment files from this package
when it needs same-origin favicon files.

## Source

- Imported on 2026-04-30 from `favicon_assets_T01_access_hub.zip`.
- `source/` preserves the two files exactly as supplied in that ZIP.
- `source/favicon-vectorized.svg` currently contains PNG image data despite the `.svg` extension.

## Runtime Exports

`runtime/` contains normalized browser/runtime exports:

- `favicon.ico`
- `favicon.svg`
- `favicon-32.png`
- `favicon.png`
- `apple-touch-icon.png`
- `icon-192.png`
- `icon-512.png`

`runtime/utility-panel/` mirrors the same asset set for the Access Hub favicon tester candidate.
