import registry from "../../../published/personas/avatar-id-registry.json";

function json(body, status = 200) {
  return new Response(JSON.stringify(body, null, 2), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });
}

function notFound() {
  return new Response("Not Found", { status: 404 });
}

function getAvatarRecord(publicId) {
  return registry.ids.find((entry) => entry.public_id === publicId) || null;
}

async function fetchBundledAsset(request, env, record) {
  const assetPath = record.worker_asset_path || "";
  if (!assetPath || !env.ASSETS) return null;
  const assetUrl = new URL(request.url);
  assetUrl.pathname = assetPath;
  assetUrl.search = "";
  return env.ASSETS.fetch(new Request(assetUrl.toString(), { method: "GET" }));
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "GET" && url.pathname === "/health") {
      return json({
        ok: true,
        service: "bitpod-avatar-worker",
        ids: registry.ids.length,
      });
    }

    if (request.method === "GET" && url.pathname.startsWith("/__avatars/")) {
      return notFound();
    }

    const avatarMatch = url.pathname.match(/^\/a\/([a-z0-9-]+)$/);
    if (!avatarMatch) return notFound();

    const publicId = avatarMatch[1];
    const record = getAvatarRecord(publicId);
    if (!record) return notFound();

    const bundled = await fetchBundledAsset(request, env, record);
    if (bundled && bundled.ok) {
      const headers = new Headers();
      const contentType = bundled.headers.get("content-type");
      if (contentType) headers.set("content-type", contentType);
      headers.set("cache-control", "public, max-age=300, s-maxage=300");
      return new Response(bundled.body, {
        status: 200,
        headers,
      });
    }

    return json(
      {
        ok: false,
        error: "avatar_not_wired",
        public_id: publicId,
      },
      503,
    );
  },
};
