import { access, readFile } from "node:fs/promises";

const requiredFiles = [
  "index.html",
  "styles/main.css",
  "scripts/app.js",
  "server.mjs",
  "data/production_manifest.json",
  "data/enriched_scene_spec.json"
];

for (const file of requiredFiles) {
  await access(new URL(`../${file}`, import.meta.url));
}

const manifest = JSON.parse(await readFile(new URL("../data/production_manifest.json", import.meta.url), "utf8"));
const spec = JSON.parse(await readFile(new URL("../data/enriched_scene_spec.json", import.meta.url), "utf8"));

if (!manifest.project?.title) {
  throw new Error("production_manifest.json is missing project.title");
}

if (!Array.isArray(spec.scenes) || spec.scenes.length === 0) {
  throw new Error("enriched_scene_spec.json is missing scenes");
}

const sceneIds = new Set(spec.scenes.map((scene) => scene.scene_id));
for (const manifestScene of manifest.scenes || []) {
  if (!sceneIds.has(manifestScene.scene_id)) {
    throw new Error(`Manifest scene ${manifestScene.scene_id} is missing from enriched scene spec`);
  }
}

console.log(`PaperMotion Workbench build check ok: ${spec.scenes.length} scenes`);
