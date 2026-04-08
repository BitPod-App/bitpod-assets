#!/usr/bin/env node

const [, , publicId, domainArg] = process.argv;

if (!publicId) {
  console.error("Usage: node scripts/print-public-url.mjs <public_id> [domain]");
  process.exit(1);
}

const domain = domainArg || "https://bitpod-avatar-worker.cjarguello.workers.dev";
const url = new URL(`/a/${publicId}`, domain);
console.log(url.toString());
