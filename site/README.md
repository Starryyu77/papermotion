# PaperMotion Workbench Site

Focused demo website for the PaperMotion presentation branch.

This is a desktop presentation surface. It borrows old workstation / classic system UI language, but the visible product framing stays on PaperMotion rather than acting like a literal operating-system clone. Mobile layout is out of scope for this pass.

## Run

```bash
npm run dev
```

The local server defaults to:

```text
http://127.0.0.1:4173
```

## Build Check

```bash
npm run build
```

This is a zero-dependency static site check. It validates required files and parses the local JSON data.

## Data

The site reads copied demo data from:

```text
site/data/production_manifest.json
site/data/enriched_scene_spec.json
```

The source-of-truth repo files are:

```text
examples/attention/production_manifest.json
examples/attention/enriched_scene_spec.json
```

## PixVerse API Boundary

The frontend calls:

```text
POST /api/pixverse/generate
GET /api/pixverse/status/:video_id
```

The current local server uses mock responses only. It does not expose or require a PixVerse API key.
