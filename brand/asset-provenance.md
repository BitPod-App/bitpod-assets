# BitPod Brand Asset Provenance

This registry tracks source, owner, usage rights status, and lifecycle status for current brand assets.

Status vocabulary used in this file:

- `placeholder`
- `working`
- `final`
- `superseded`

## Current Phase 1 working set

| asset_set | paths | source | owner | usage_rights_status | status | note |
|---|---|---|---|---|---|---|
| corrected logo SVG wrappers | `brand/logo/svg/*.svg` | `bitpod_brand_starter_fixed.zip` | BitPod App | pending formal policy | working | visually faithful to approved logo; not canonical vector master |
| corrected logo PNG exports | `brand/logo/png/*.png` | `bitpod_brand_starter_fixed.zip` | BitPod App | pending formal policy | working | practical delivery assets for Phase 1 |
| repo social preview cards | `brand/social/repo-previews/bitpod-tools-preview.png`, `brand/social/repo-previews/sector-feeds-preview.png` | local working file imports | BitPod App | pending formal policy | placeholder | operational org/profile previews |

## Superseded assets/source

| asset_set | paths | source | owner | usage_rights_status | status | note |
|---|---|---|---|---|---|---|
| legacy starter source package | `bitpod_brand_starter.zip` and folder variant `bitpod_brand_starter` | earlier starter generation | BitPod App | pending formal policy | superseded | drifted from approved/current logo |
| legacy mismatched logo variants retained for traceability | `brand/superseded/bitpod_brand_starter_legacy/logo/svg/bitpod-logo-mark-color.svg`, `brand/superseded/bitpod_brand_starter_legacy/logo/svg/bitpod-logo-mark-negative.svg` | earlier starter generation | BitPod App | pending formal policy | superseded | retained only for audit/traceability; do not use as source of truth |

## Canonicality note

No asset in this Phase 1 working set should be interpreted as final canonical vector master.
Canonical vector master work is explicitly deferred under BIT-57.
