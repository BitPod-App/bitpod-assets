# BitGal Naming Rules

## File pattern
`{persona}_{type}_{scene}_{look}_vNN.{ext}`

## Allowed persona values
- `taylor`
- `ember`
- `kati`
- `shiva`
- `vera`

## Allowed type values
- `avatar`
- `image`
- `video`

## Examples
- `taylor_avatar_hq_black-suit_v01.png`
- `ember_video_stage_singing_v02.mp4`
- `kati_image_studio_gold-heavy_v03.jpg`
- `shiva_avatar_night_gloss-black_v01.webp`
- `vera_image_serverroom_glasses_v01.png`

## Folder rules
- square still intended for profile use -> `avatars/`
- still image not specifically avatar -> `approved/` or `conditional/`
- moving media -> `videos/`
- still-image reference material (`image` or `avatar`, never `video`) -> `refs/`
- failed output -> `rejected/`

## Metadata rule
Use a sidecar JSON with the same filename plus `.json` next to the asset by default.
Leave `metadata/` folders unused in v1 unless a later workflow explicitly requests them.

Example:
- `kati_avatar_studio_gold-heavy_v01.png`
- `kati_avatar_studio_gold-heavy_v01.png.json`
