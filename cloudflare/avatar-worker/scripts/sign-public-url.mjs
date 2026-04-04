#!/usr/bin/env node

import crypto from "node:crypto";
import process from "node:process";

function usage() {
  console.error(
    "Usage: AVATAR_URL_SIGNING_SECRET=... node scripts/sign-public-url.mjs <public_id> [domain] [ttl_seconds]",
  );
  process.exit(1);
}

const [, , publicId, domainArg, ttlArg] = process.argv;
if (!publicId) usage();

const secret = process.env.AVATAR_URL_SIGNING_SECRET;
if (!secret) {
  console.error("Missing AVATAR_URL_SIGNING_SECRET");
  process.exit(1);
}

const domain = domainArg || "https://bitpod.com";
const ttlSeconds = Number.parseInt(ttlArg || "86400", 10);
if (!Number.isFinite(ttlSeconds) || ttlSeconds <= 0) {
  console.error("ttl_seconds must be a positive integer");
  process.exit(1);
}

const expiry = Math.floor(Date.now() / 1000) + ttlSeconds;
const payload = `${publicId}:${expiry}`;
const signature = crypto.createHmac("sha256", secret).update(payload).digest("hex");
const url = new URL(`/a/${publicId}`, domain);
url.searchParams.set("exp", String(expiry));
url.searchParams.set("h", signature);

console.log(url.toString());
