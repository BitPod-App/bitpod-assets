import registry from "../../../assets/agents/avatar-id-registry.json";

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

function getNowSeconds() {
  return Math.floor(Date.now() / 1000);
}

function timingSafeEqual(a, b) {
  if (!(a instanceof Uint8Array) || !(b instanceof Uint8Array)) return false;
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i += 1) diff |= a[i] ^ b[i];
  return diff === 0;
}

function hexToBytes(hex) {
  if (!/^[0-9a-f]+$/i.test(hex) || hex.length % 2 !== 0) return null;
  const out = new Uint8Array(hex.length / 2);
  for (let i = 0; i < hex.length; i += 2) {
    out[i / 2] = Number.parseInt(hex.slice(i, i + 2), 16);
  }
  return out;
}

async function signMessage(secret, message) {
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(message));
  return new Uint8Array(sig);
}

function parseExpiry(expiry) {
  if (!/^\d+$/.test(expiry || "")) return null;
  const parsed = Number.parseInt(expiry, 10);
  return Number.isFinite(parsed) ? parsed : null;
}

async function verifyPublicUrlSignature(secret, publicId, expiry, signature) {
  if (!secret || !publicId || !expiry || !signature) return false;
  const provided = hexToBytes(signature);
  if (!provided) return false;
  const expected = await signMessage(secret, `${publicId}:${expiry}`);
  return timingSafeEqual(provided, expected);
}

function cloudflareImageUrl(env, imageId) {
  const accountHash = env.CLOUDFLARE_IMAGES_ACCOUNT_HASH;
  const variant = env.CLOUDFLARE_IMAGES_VARIANT || "public";
  if (!accountHash || !imageId) return null;
  return `https://imagedelivery.net/${accountHash}/${imageId}/${variant}`;
}

async function signCloudflareImageUrl(url, signingKey, expirySeconds) {
  const expiry = getNowSeconds() + expirySeconds;
  url.searchParams.set("exp", String(expiry));

  const stringToSign = `${url.pathname}?${url.searchParams.toString()}`;
  const signature = await signMessage(signingKey, stringToSign);
  const hexSignature = [...signature]
    .map((value) => value.toString(16).padStart(2, "0"))
    .join("");

  url.searchParams.set("sig", hexSignature);
  return url;
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

    const avatarMatch = url.pathname.match(/^\/a\/([a-z0-9-]+)$/);
    if (!avatarMatch) return notFound();

    const publicId = avatarMatch[1];
    const record = getAvatarRecord(publicId);
    if (!record) return notFound();

    const expiry = parseExpiry(url.searchParams.get("exp") || "");
    if (!expiry) {
      return json({ ok: false, error: "missing_or_invalid_expiry", public_id: publicId }, 400);
    }

    if (expiry <= getNowSeconds()) {
      return json({ ok: false, error: "expired_url", public_id: publicId }, 403);
    }

    const maxTtl = Number.parseInt(env.MAX_PUBLIC_URL_TTL_SECONDS || "86400", 10);
    if (expiry - getNowSeconds() > maxTtl) {
      return json({ ok: false, error: "expiry_too_far_in_future", public_id: publicId }, 403);
    }

    const signature = url.searchParams.get("h") || "";
    const ok = await verifyPublicUrlSignature(
      env.AVATAR_URL_SIGNING_SECRET,
      publicId,
      String(expiry),
      signature,
    );
    if (!ok) {
      return new Response("Forbidden", { status: 403 });
    }

    if (!record.cloudflare_image_id) {
      return json(
        {
          ok: false,
          error: "avatar_not_wired",
          public_id: publicId,
        },
        503,
      );
    }

    const imageUrl = cloudflareImageUrl(env, record.cloudflare_image_id);
    if (!imageUrl) {
      return json(
        {
          ok: false,
          error: "cloudflare_images_not_configured",
          public_id: publicId,
        },
        500,
      );
    }

    if (!env.IMAGES_SIGNING_KEY) {
      return json(
        {
          ok: false,
          error: "images_signing_key_not_configured",
          public_id: publicId,
        },
        500,
      );
    }

    const signedCloudflareUrl = await signCloudflareImageUrl(
      new URL(imageUrl),
      env.IMAGES_SIGNING_KEY,
      maxTtl,
    );

    const upstream = await fetch(signedCloudflareUrl, {
      cf: { cacheEverything: true, cacheTtl: 300 },
    });

    if (!upstream.ok) {
      return json(
        {
          ok: false,
          error: "upstream_fetch_failed",
          public_id: publicId,
          status: upstream.status,
        },
        502,
      );
    }

    const headers = new Headers();
    const contentType = upstream.headers.get("content-type");
    if (contentType) headers.set("content-type", contentType);
    headers.set("cache-control", "public, max-age=300, s-maxage=300");

    return new Response(upstream.body, {
      status: 200,
      headers,
    });
  },
};
