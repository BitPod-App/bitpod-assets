# Published Branding

Operational branding assets that are already live or ready to be used directly.

This is separate from `brand/`, which remains the broader BitPod brand library
and source material lane.

## Runtime favicon delivery

`published/branding/manifest.json` publishes two T01 favicon packages for
runtime apps to consume from the repo:

- `t01-access-hub-favicons` -> `brand/favicons/t01-access-hub/runtime/`
- `taylor01-hermes-dashboard-favicons` -> `brand/favicons/taylor01-hermes-dashboard/runtime/`

Downstream apps should copy the listed runtime files into their own same-origin
web root or public asset directory during deployment. Do not serve
`brand/favicons/` directly as a CDN or general public asset root.
