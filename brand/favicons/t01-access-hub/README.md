# T01 Access Hub Favicons

Canonical favicon assets for the Taylor01 T01 Access Hub.

These assets live under `brand/favicons/` because they are presentation/identity
assets for an app surface, not public persona media and not Cloudflare worker
inputs. A consuming app may generate or copy deployment files from this package
when it needs same-origin favicon files.

## Source

- Imported on 2026-04-30 from `favicon_assets_T01_access_hub.zip`.
- `source/favicon.ico` preserves the ICO supplied in that ZIP.
- The ZIP also supplied a file named `favicon-vectorized.svg`, but its bytes are
  PNG image data, not SVG vector markup. It is kept as
  `source/favicon-original-raster.png` so the file extension matches the actual
  format while preserving the original raster source bytes.
- There is no true vector source in this package today. Do not use `source/` as a
  runtime input unless you intentionally need the original imported files.

## Runtime Exports

`runtime/` contains normalized browser/runtime exports for T01/Hermes consumers:

- `favicon.ico` — safest default for broad browser/tab support.
- `favicon.svg` — compatibility SVG wrapper that embeds the original 64×64 PNG;
  it is not a vector drawing and should not be treated as an editable vector
  source.
- `favicon-32.png`
- `favicon.png`
- `apple-touch-icon.png`
- `icon-192.png`
- `icon-512.png`

Recommended app references when copying these files to a same-origin web root:

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

If a consumer needs an actual vector favicon, create one explicitly from brand
artwork instead of reusing `runtime/favicon.svg` or the original imported raster.

`runtime/utility-panel/` mirrors the same asset set for the Access Hub favicon
tester candidate.
