// gta6-meme-x-01 entry — "5-Star Wanted / In Leonida" (Node 22, standard library only).
//
// The entry is the X post itself: the house reads the post from X (its first
// picture, then its text) and hands that to the judge. This program does the
// one thing the harness asks of it: it copies POST.json, which names the post,
// from the repository root into the output directory, so the gate can read it.
//
// Nothing this program writes about the post is judged. It needs no network,
// no wall clock, and no files outside the repository, and two runs of it write
// the same bytes.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

// The grader mounts the repository at /bot and expects output at /output.
// Outside the grader, the two env vars below stand in for those paths.
const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const sourcePath = join(botDir, "POST.json");
const targetPath = join(outputDir, "POST.json");

// Read first so a malformed POST.json fails loudly instead of silently
// copying garbage into the output directory.
const post = JSON.parse(readFileSync(sourcePath, "utf8"));
if (typeof post !== "object" || post === null || typeof post.url !== "string") {
  console.error("POST.json must be a JSON object with a string \"url\" field");
  process.exit(1);
}
// The gate only accepts an X post address, id digits only, so refuse anything
// else here instead of letting a bad placeholder through to grading.
if (!/^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/[^/]+\/status\/\d+/.test(post.url)) {
  console.error(`POST.json url is not an X post address: ${post.url}`);
  process.exit(1);
}

mkdirSync(outputDir, { recursive: true });
copyFileSync(sourcePath, targetPath);
