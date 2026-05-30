# PaperMotion Current Memory

## Current Goal
Build a 3-hour MVP plan for PaperMotion: a Trae Solo native workflow and website that demonstrate how to turn complex formulas and paper mechanisms into interactive AI visualization short films.

## Current Repo State
- Repo: `Starryyu77/papermotion`
- Branch: `main`
- Local path: `/Users/starryyu/Downloads/trae/papermotion`
- Starting state: only `README.md` existed after cloning.

## Product Decision
PaperMotion should not start as a fully automated paper-to-video SaaS. It should be built as a Trae Solo native workspace workflow plus a credible demo website.

Trae Solo is the production cockpit:
- MTC mode handles paper/formula understanding, mechanism specs, storyboards, narration, and review.
- Code Mode handles Manim, website implementation, terminal renders, and browser QA.
- Repo files are the handoff contract between stages.

The 3-hour MVP should be a credible demo website plus one reproducible sample workflow:

1. Input: one paper excerpt or formula.
2. Analysis: concept/mechanism brief with a symbol ledger.
3. Storyboard: 5-7 short scenes.
4. Render: deterministic Manim draft video.
5. PixVerse: cinematic support clips / explanatory objects / transitions that do not require exact math.
6. Website: demo video, synchronized scene/formula notes, and workflow proof.

## Recommended Demo Topic
Use scaled dot-product attention as the first demo:

`Attention(Q,K,V) = softmax(QK^T / sqrt(d_k))V`

Reason: it is recognizable, formula-heavy enough to show value, and simple enough to render in Manim within three hours using matrices, token dots, attention heatmaps, and weighted value aggregation.

## Team Split
- Person A: Trae Solo MTC/Code track for paper/formula analysis, scene spec, Manim code, rough video export.
- Person B: Trae Solo Code/MTC track for PixVerse cinematic support, audio rhythm, website, workflow UI, final embed/QA.

## Trae Solo Integration
- Open this repo as the Solo Desktop workspace.
- Use `solo/runbook.md` as the operating guide.
- Use `solo/task-board.md` as the live task board.
- Use `prompts/00-solo-master-orchestrator.md` before starting parallel tasks.
- Treat `docs/trae-solo-native-workflow.md` as the source of truth for integration decisions.
- Treat `docs/agent-coordination-and-pixverse.md` as the source of truth for multi-agent coordination and PixVerse integration.
- Use `examples/<demo>/production_manifest.json` as the shared coordination contract.

## Hard Rules For MVP
- PixVerse is a formal workflow stage, not an afterthought.
- Manim owns exact formulas, matrices, graphs, and deterministic transformations.
- PixVerse owns cinematic support assets, explanatory objects, metaphor shots, and transitions.
- If PixVerse API access is not ready, still produce `pixverse_jobs` specs and show the planned PixVerse stage on the website.
- Coordination happens through `production_manifest.json`, not chat-only decisions.

## Next Step
Create the site skeleton and a sample workflow artifact set:
- `examples/attention/input.md`
- `examples/attention/production_manifest.json`
- `examples/attention/mechanism_spec.json`
- `examples/attention/storyboard.md`
- `examples/attention/scene_specs/*.json`
- `manim/attention_demo.py`
- `site/` or Vite root app
