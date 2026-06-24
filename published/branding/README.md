# Published Branding

Operational branding assets that are already live or ready to be used directly.

This is separate from `brand/`, which remains the broader BitPod brand library
and source material lane.

## Runtime favicon delivery

`published/branding/manifest.json` publishes the active T01/Hermes favicon
package and records retired favicon packages for historical/source traceability.

Active package:

- `taylor01-hermes-dashboard-favicons` -> `brand/favicons/taylor01-hermes-dashboard/runtime/`

Retired package:

- `t01-access-hub-favicons` -> `brand/favicons/t01-access-hub/runtime/`

Downstream apps should copy only the listed active published runtime files into
their own same-origin web root or public asset directory during deployment. Do
not serve `brand/favicons/` directly as a CDN or general public asset root.
