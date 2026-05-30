# PaperMotion Research And 3-Hour MVP Plan

## 1. Product Positioning

PaperMotion is a science-explainer workflow, not just a generic AI video generator.

The wedge should be:

> Turn one complex paper mechanism or formula into a short interactive explainer film, with visible links between the original symbols, the storyboard, the Manim render, and the final video.

The demo should prove the workflow, not a fully automated product. In three hours, the deliverable should be a polished website that shows one end-to-end example and makes the pipeline believable.

Important update: PaperMotion should be Trae Solo native. Trae Solo is the actual production workspace for the MVP; the website is the public-facing demo surface. See `docs/trae-solo-native-workflow.md`.

## 2. External Research Summary

### Manim

Manim Community is a Python library for precise programmatic mathematical animation. The official quickstart shows a `Scene` class rendered from the command line, for example `manim -pql scene.py SceneName`, and notes that Manim outputs MP4 files. Source: https://docs.manim.community/en/stable/tutorials/quickstart.html

Implication for PaperMotion:
- Use Manim for formula-accurate, deterministic animation.
- Render scene-by-scene at low quality first.
- Keep generated code small and repairable.
- Avoid asking an LLM to produce a full 3-minute video in one pass.

### PixVerse

PixVerse exposes a REST API for text-to-video, image-to-video, transition generation, effects, lip-sync, and sound. The official docs say jobs are asynchronous: submit a request, get a `video_id`, then poll status until success. Source: https://docs.platform.pixverse.ai/pixverse-api-llm-txt-2109771m0

PixVerse platform pricing depends on model, quality, duration, and whether audio is enabled. Source: https://docs.platform.pixverse.ai/pricing-796039m0

Implication for PaperMotion:
- PixVerse is a formal cinematic support stage in the workflow.
- Use PixVerse for cinematic cover shots, transitions, object/metaphor clips, and background motion.
- Preserve Manim output for exact formulas, equations, matrices, and causal mechanisms.

### Trae Solo

Trae Solo is positioned as a workspace where AI can decompose tasks, call skills/tools, and handle files in one workspace. The official Chinese Solo page explicitly lists paper reading, market research, website building, and code wiki style tasks. Source: https://www.trae.cn/solo-web

Implication for PaperMotion:
- Split the workflow into file-producing agents rather than a single vague chat request.
- Keep intermediate artifacts in the repo so both teammates can work in parallel.
- Use Trae Solo Work mode for research/storyboard artifacts and Code mode for app/render scripts.
- Treat Solo's workspace, terminal, browser preview, task visibility, and parallel execution as first-class parts of the product demo.

### Relevant AI + Manim Research

LLM2Manim argues for a human-in-the-loop pipeline using constrained prompt templates, a symbol ledger, partial regeneration of erroneous sections, and expert review before final render. Source: https://arxiv.org/abs/2604.05266

Manimator describes a pipeline that turns a paper/PDF into a structured scene description and then into executable Manim Python code. Source: https://arxiv.org/abs/2507.14306

ALGOGEN reports better reliability by separating verifiable traces from rendering, instead of relying on one end-to-end generation step. Source: https://arxiv.org/abs/2605.12159

Training and Agentic Inference Strategies for LLM-based Manim Animation Generation highlights the core difficulty: Manim generation needs spatial reasoning, temporal sequencing, and API familiarity. Source: https://arxiv.org/abs/2604.18364

Implication for PaperMotion:
- The product should be a staged compiler-like workflow:
  `paper -> intent -> prerequisite graph -> curriculum -> script -> storyboard -> scene spec -> Manim/PixVerse/audio -> website`
- The key differentiator is not "AI makes a video"; it is visible, editable, and verifiable transformations from paper concepts to scenes.

## 3. MVP Scope

### Must Have In 3 Hours

1. A website with:
   - Demo video area.
   - Workflow timeline.
   - Sample input excerpt/formula.
   - Storyboard or scene list.
   - A small "interactive movie" layer: clicking scene chapters reveals the formula/mechanism being explained.

2. One sample workflow:
   - Input formula/paper excerpt.
   - Mechanism brief.
   - Scene storyboard.
   - Manim script.
   - Rendered rough MP4.

3. Reproducibility:
   - README explains how to run the site.
   - README explains how to render the Manim demo.
   - Repo contains all prompt templates and intermediate artifacts.

### Nice To Have

- Before/after comparison: raw Manim draft vs cinematic final.
- A fake but clear upload panel on the site, labelled as workflow preview, not production upload.

### Explicit Non-Goals

- Full PDF parser backend.
- Multi-paper support.
- User accounts.
- Payment.
- Claiming the system can explain any paper without human review.

## 4. Recommended First Demo

Use the scaled dot-product attention formula:

```text
Attention(Q,K,V) = softmax(QK^T / sqrt(d_k))V
```

Why this is the best 3-hour demo:
- It contains a real formula and a mechanism.
- It maps cleanly to visual objects: tokens, query/key/value vectors, matrix multiplication, heatmap, weighted sum.
- It is recognizable to AI/ML viewers.
- It can be rendered with Manim primitives without needing complex 3D assets.

Scene plan:

1. Hook: tokens become vector cards.
2. Q/K/V split: each token emits three colored vectors.
3. Similarity: `QK^T` becomes a heatmap.
4. Scaling: divide by `sqrt(d_k)` to prevent overly sharp scores.
5. Softmax: raw scores become attention weights.
6. Weighted sum: values combine into contextualized token representation.
7. Closing: formula reassembles from visual steps.

## 5. Architecture For The Demo

```text
examples/attention/
  input.md
  production_manifest.json
  mechanism_spec.json
  storyboard.md
  scene_specs/

prompts/
  00-solo-master-orchestrator.md
  01-paper-to-mechanism.md
  02-mechanism-to-storyboard.md
  03-storyboard-to-manim.md
  04-pixverse-polish.md
  05-website-integration.md
  06-agent-coordination-production-manifest.md
  07-pixverse-asset-agent.md

solo/
  runbook.md
  task-board.md
  review-checklist.md

manim/
  attention_demo.py

site/
  React or static frontend
  public/videos/attention-demo.mp4
```

Minimum pipeline:

1. Open the repo as the Trae Solo workspace.
2. Run `prompts/00-solo-master-orchestrator.md` to create/update `solo/task-board.md`.
3. Create/update `examples/attention/production_manifest.json`.
4. MTC mode writes intent, prerequisite graph, curriculum plan, teaching script beats, rhythm map, and visual asset requests.
5. Storyboard and Scene Spec agents write scene plans and precise scene specs.
6. PixVerse Asset Agent creates PixVerse job specs and generated cinematic support assets when credentials are available.
7. Code Mode writes or repairs `manim/attention_demo.py`.
8. Voice/music/SFX agents fill the audio manifest.
9. Code Mode runs Manim low-quality render first.
10. Assembly combines Manim, PixVerse, and audio assets.
11. Website displays the video plus synchronized chapters and workflow artifacts.

## 6. Three-Hour Team Plan

### 0:00-0:15 Scope Lock

Shared:
- Confirm demo topic: scaled dot-product attention.
- Confirm output: website + one video + visible workflow.
- Create folders and starter files.
- Open repo in Trae Solo and use `solo/task-board.md` as the live task board.

Person A:
- Owns `examples/attention/`, explanation prompts, `manim/`.
- Uses MTC mode first, then Code Mode for Manim.

Person B:
- Owns PixVerse cinematic support, audio rhythm, website app, visual direction, final embed, deployment/readme.
- Uses Code Mode for site, MTC mode for copy/review/PixVerse prompts.

### 0:15-0:45 Analysis And Storyboard

Person A:
- Draft `input.md`.
- Generate intent, prerequisite graph, curriculum plan, and first script beats in `production_manifest.json`.
- Draft 5-7 scene storyboard.
- Define symbol ledger: Q, K, V, `d_k`, softmax, attention weights.

Person B:
- Create website skeleton.
- Draft PixVerse asset request slots from the early script beats.
- Draft the first rhythm map slots for slowdown/reveal moments.
- Build first screen around the video, not a marketing landing page.
- Add chapter list and workflow timeline.

Sync at 0:45:
- Freeze scene count.
- Freeze color mapping for symbols.

### 0:45-1:35 Manim Draft And Website UI

Person A:
- Generate scene specs before code.
- Generate Manim code one scene at a time.
- Render low quality with:

```bash
uv run manim -ql manim/attention_demo.py AttentionDemo
```

Fallback if `uv` is not set up:

```bash
manim -ql manim/attention_demo.py AttentionDemo
```

Person B:
- Freeze first PixVerse job spec by 1:15.
- Implement the website sections:
  - Demo player.
  - Chapter buttons.
  - Formula ledger.
  - Workflow proof.
  - Sample input/output panels.

Sync at 1:35:
- Decide whether Manim draft is good enough.
- If not, reduce scenes instead of adding complexity.

### 1:35-2:10 Render, PixVerse, Audio

Person A:
- Render final Manim MP4.
- Export 1-3 still frames/keyframes for PixVerse image-to-video.

Person B:
- Run PixVerse image-to-video for one 3-5s cinematic support clip if API key/credits are ready.
- If API execution is not ready, keep the PixVerse job spec in `production_manifest.json` and show the planned stage on the site.
- Fill the voiceover/music/SFX timing plan from `rhythm_map`.

PixVerse should handle:
- Opening cinematic shot.
- Scene transitions.
- Abstract background motion.
- Explanatory object/metaphor clips.

PixVerse should not replace:
- Formula rendering.
- Matrices.
- Symbol transformations.
- Exact educational explanation.

### 2:10-2:40 Assembly

Person A:
- Stitch Manim clips and PixVerse clips or placeholders using ffmpeg.
- Export one web-ready MP4.

Person B:
- Embed MP4.
- Wire chapter clicks to update explanatory text.
- Add reproducibility section.

### 2:40-3:00 QA And Delivery

Shared checklist:
- Website runs locally.
- Video loads on the page.
- Chapters do not overlap text.
- Formula symbols keep the same colors across site and video.
- README has run/render instructions.
- The site clearly shows the workflow, not just the final video.

## 7. Prompt Workflow For Trae Solo

Use separate prompts so each stage produces files.

1. Intent / prerequisite / curriculum:
   - Input: excerpt/formula.
   - Output: `production_manifest.json`.
   - Must include intent, prerequisite graph, curriculum order, and minimal just-in-time insertions.

2. Teaching script / storyboard:
   - Input: `production_manifest.json`.
   - Output: script beats, rhythm map, visual asset requests, storyboard scenes.
   - Must include 5-7 scenes with duration, narration, visuals, and PixVerse/Manim classification.

3. Scene specs / Manim:
   - Input: `scene_specs/*.json`.
   - Output: one Manim scene class plus render notes.
   - Must use only common Manim APIs and render at low quality first.

4. PixVerse cinematic support:
   - Input: Manim still frame or prompt.
   - Output: short cinematic support clip or formal job spec.
   - Must not alter mathematical symbols or formulas.

## 8. Risk Register

| Risk | Impact | Response |
| --- | --- | --- |
| Manim install/render fails | Demo blocked | Use a shorter Manim script, use `manim -ql`, or fall back to website animation for one scene while keeping the Manim script in repo. |
| PixVerse API/credits unavailable | Generation unavailable | Keep PixVerse job specs in the manifest, use a Manim/still placeholder, and show the stage in the website. |
| LLM generates broken Manim code | Time loss | Generate one scene at a time and repair from render errors. |
| Story gets too abstract | Weak demo | Keep the narrative tied to one formula and one learning objective. |
| Website becomes generic landing page | Demo feels fake | First viewport must show the actual video/workflow, not marketing copy. |

## 9. Suggested Website Structure

First viewport:
- Product name: PaperMotion.
- Embedded demo video.
- Chapter rail: Formula, Q/K/V, heatmap, softmax, weighted sum.
- Current scene explanation panel.

Below:
- Input excerpt/formula.
- Generated mechanism spec preview.
- Storyboard preview.
- Manim render proof.
- PixVerse cinematic support step.
- "Built in 3 hours" execution log.

Visual direction:
- Dark neutral background for cinematic feel.
- Use 2-3 stable symbol colors, not a rainbow.
- Formula cards should be compact.
- Avoid dense bullet-heavy sections.
- Website should feel like an interactive explainer tool, not a SaaS marketing page.

## 10. Immediate Next Commands After This Plan

If we start implementation, Person B can initialize the site:

```bash
npm create vite@latest site -- --template react-ts
cd site
npm install
npm run dev
```

Person A can initialize Manim after Python/uv is available:

```bash
uv venv
uv pip install manim
uv run manim -ql manim/attention_demo.py AttentionDemo
```

If dependencies are already installed, skip setup and render directly.
