# PaperMotion Current Memory

## Current Goal
Build a 3-hour MVP plan for PaperMotion: a Trae Solo native workflow and website that demonstrate how to turn complex formulas and paper mechanisms into interactive AI visualization short films.

## Current Repo State
- Repo: `Starryyu77/papermotion`
- Branch: `person-b-presentation`
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

## Active Workstream
Current branch is for Person B: presentation-facing work around the website, demo flow, PixVerse support specs, audio rhythm, final embed, and QA.

Person B website direction is `PaperMotion Workbench`: a desktop-only retro workstation presentation surface that borrows from early Mac OS X Aqua / classic desktop UI and Windows 98 control density without copying real Apple or Microsoft assets or framing the product as a literal OS clone. The current implementation uses one primary film workbench as the visual focus, with formula overlay, chapter rail, compact workflow strip, and a hidden context inspector drawer. Mobile layout is out of scope for this pass.

PixVerse API access is available. Website implementation should include a server-side PixVerse proxy/generate flow instead of only showing planned jobs.

Updated project-plan fusion is captured in `docs/project-plan-fusion.md`. The fused architecture uses a two-level contract: `production_manifest.json` remains the project-level registry and website navigation source, while `enriched_scene_spec.json` is the executable scene-level single source of truth for Manim, TTS, Music/SFX, PixVerse, Assembly, and QA.

Website-builder handoff package is captured in `docs/website-builder-handoff.md`. It is now secondary to the repo-local `site/` implementation because Person B is building the website directly.

## Trae Solo Integration
- Open this repo as the Solo Desktop workspace.
- Use `solo/runbook.md` as the operating guide.
- Use `solo/task-board.md` as the live task board.
- Use `docs/person-b-presentation-website-design.md` as the source of truth for Person B website design, functions, PixVerse API interactions, and motion behavior.
- Use `docs/project-plan-fusion.md` as the source of truth for the merged Formula2Video/PaperMotion architecture.
- Use `docs/website-builder-handoff.md` as the direct implementation brief for a dedicated website-building tool.
- Use `prompts/00-solo-master-orchestrator.md` before starting parallel tasks.
- Treat `docs/trae-solo-native-workflow.md` as the source of truth for integration decisions.
- Treat `docs/agent-coordination-and-pixverse.md` as the source of truth for multi-agent coordination and PixVerse integration.
- Use `examples/<demo>/production_manifest.json` as the project-level coordination registry.
- Use `examples/<demo>/enriched_scene_spec.json` as the executable scene-level coordination contract.

## Hard Rules For MVP
- PixVerse is a formal workflow stage, not an afterthought.
- Manim owns exact formulas, matrices, graphs, and deterministic transformations.
- PixVerse owns cinematic support assets, explanatory objects, metaphor shots, and transitions.
- If PixVerse API access is unavailable in a specific run environment, still produce `pixverse_jobs` specs and show the planned PixVerse stage on the website.
- Since PixVerse API access is available, keep the API key server-side and expose generation through website backend routes.
- Coordination happens through repo files, not chat-only decisions. Project status lives in `production_manifest.json`; executable scene details live in `enriched_scene_spec.json`.

## Next Step
Finalize the Person B presentation site:
- Keep the first viewport focused on the film workbench rather than multiple competing desktop widgets.
- Use `site/` as the zero-dependency desktop demo website.
- Keep PixVerse API credentials server-side; the current local server exposes mock generate/status routes ready for a real proxy.
- Run build/browser QA, then commit and push the focused website branch.
