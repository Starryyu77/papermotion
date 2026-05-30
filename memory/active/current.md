# PaperMotion Current Memory

## Current Goal
Reframe PaperMotion as a Trae Solo skill workflow for research-video production: helping researchers turn formulas, paper sections, algorithms, proof sketches, and mechanisms into accurate dynamic visual explainer videos.

## Current Repo State
- Repo: `Starryyu77/papermotion`
- Branch: `person-a-production-workflow`
- Local path: `/Users/starryyu/Downloads/trae/papermotion`
- Starting state: only `README.md` existed after cloning.

## Product Decision
PaperMotion should not be website-first. It should be a Trae Solo native skill suite for researcher productivity and science communication.

PaperMotion should not duplicate Trae Solo's base abilities such as reading papers, inspecting images, writing code, operating files, and coordinating agents. It should add the missing research-video layer: paper decomposition, dynamic visual reasoning, and video generation through renderer/video-library skills.

Trae Solo is the production cockpit:
- MTC mode handles paper/formula understanding, mechanism specs, storyboards, narration, and review.
- Code Mode handles Manim, website implementation, terminal renders, and browser QA.
- Repo files are the handoff contract between stages.

The MVP should be one reusable research-video workflow plus one reproducible sample run:

1. Input: one paper excerpt or formula.
2. Paper decomposition: paper map, formula inventory, figure-to-claim map, and visualizable units.
3. Mechanism modeling: symbol ledger, causal steps, assumptions, and claim boundaries.
4. Dynamic visual reasoning: visual objects, 3D/spatial layout, motion primitives, camera plan, exact-vs-metaphor boundary, and renderer recommendation.
5. Learning path, teaching script, storyboard, and scene contract.
6. Render: deterministic layers for exact formulas, diagrams, transformations, and 3D mechanism scenes.
7. Optional AI support: cinematic clips, explanatory objects, transitions, voice/audio, and assembly aids that do not require exact math.
8. QA/delivery: draft video, artifact bundle, source-fidelity review, and optional presentation surface.

## Recommended Demo Topic
Use scaled dot-product attention as the first demo:

`Attention(Q,K,V) = softmax(QK^T / sqrt(d_k))V`

Reason: it is recognizable, formula-heavy enough to show value, and simple enough to render in Manim within three hours using matrices, token dots, attention heatmaps, and weighted value aggregation.

## Historical Split
The old Person A / Person B split is now archived as reference.

- Person A produced the first attention mechanism artifacts and Manim pipeline.
- Person B produced the website/presentation prototype direction.

The current planning frame is no longer Person A versus Person B. It is the research-video skill workflow: intake, paper decomposition, mechanism modeling, dynamic visual reasoning, learning path, science script, storyboard, scene contract, exact animation, cinematic support, voice/audio, and assembly/QA.

## Active Workstream
Current work is packaging PaperMotion as a Trae Solo skill pack / SKU and validating
that the dynamic visual reasoning skill generalizes beyond the attention demo.

The prior website and attention demo work is archived as reference. The new execution summary is documented in `docs/execution-summary.md`, the mainline is documented in `docs/papermotion-mainline.md`, and the target skill suite is documented in `docs/research-video-skill-suite.md`.

The current install path is skill-first:
- `papermotion.sku.json` is the SKU manifest.
- `papermotion.sku.json.skills[]` is the authoritative skill list.
- Trae should read each listed `SKILL.md` frontmatter `name` and `description` and
  register or load those skills.
- `skills/papermotion-research-video/SKILL.md` is the root skill.
- `prompts/trae-install-sku.md` is the GitHub-link install prompt.
- `./setup.sh --check-only` is post-install validation, not the product install.
- Full `./setup.sh` is only for creating or refreshing the local validation backend.

Updated project-plan fusion is captured in `docs/project-plan-fusion.md`. The fused architecture uses a two-level contract: `production_manifest.json` remains the project-level registry and website navigation source, while `enriched_scene_spec.json` is the executable scene-level single source of truth for Manim, TTS, Music/SFX, PixVerse, Assembly, and QA.

Website-builder handoff and site prototype files are now optional delivery-surface references, not the core product direction.

Current website direction when explicitly requested:
- Build the website as a simulated formula/paper-to-video flow, not as a real generation backend and not as a dense OS-style inspector-first workbench.
- The user inputs a formula, excerpt, or one-line request; the page runs a preset staged pipeline; the final state reveals the pre-generated attention demo video.
- The UI should clearly label this as a workflow preview and avoid implying full backend generation is complete.
- Keep the attention preset grounded in `site/data/production_manifest.json`, `site/data/enriched_scene_spec.json`, and `site/public/videos/attention-demo.mp4`.

## Trae Solo Integration
- Open this repo as the Solo Desktop workspace.
- Install from `papermotion.sku.json` as a skill pack; do not treat `./setup.sh`
  as the product installation.
- Use `prompts/trae-install-sku.md` when installing from a GitHub repo URL.
- Use `solo/runbook.md` as the operating guide.
- Use `solo/task-board.md` as the live task board.
- Use `docs/execution-summary.md` as the execution summary for near-term work.
- Use `docs/papermotion-mainline.md` as the current source of truth for product direction.
- Use `docs/dynamic-scene-model.md` and `contracts/dynamic_scene_model.schema.json` as the source of truth for mechanism-to-dynamic-scene modeling.
- Use `docs/research-video-skill-suite.md` as the current skill-suite design anchor.
- Treat website-specific docs as archived/optional delivery-surface references.
- Use `prompts/00-solo-master-orchestrator.md` before starting parallel tasks.
- Treat `docs/trae-solo-native-workflow.md` as the source of truth for integration decisions.
- Treat `docs/agent-coordination-and-pixverse.md` as the source of truth for multi-agent coordination and PixVerse integration.
- Use `examples/<demo>/production_manifest.json` as the project-level coordination registry.
- Use `examples/<demo>/enriched_scene_spec.json` as the executable scene-level coordination contract.
- Use `examples/README.md` as the current example catalogue.

## Skill Pack Artifact State
- `papermotion.sku.json` declares `artifact_type: trae_skill_pack`, the root skill,
  the skill registry authority, entry docs, contracts, validation commands, and example roots.
- `skills/papermotion-research-video/SKILL.md` now includes a child-skill routing table
  for orchestration, visual brief, dynamic visual reasoning, storyboard, deterministic render,
  cinematic support, and QA.
- `docs/install.md` and `prompts/trae-install-sku.md` define the one-link Trae install flow:
  clone, read SKU, register/load listed skills by frontmatter, then optionally run validation.
- `setup.sh`, `scripts/setup.sh`, and `scripts/validate_dynamic_scene_model.py` are executable.
- `scripts/setup.sh --check-only` selects a Python runtime that can import `jsonschema`;
  it no longer fails on a stale `.venv` that lacks the dependency when system Python can validate.

## Dynamic Scene Model Example State
- `examples/attention/dynamic_scene_model.json` validates and remains the most complete sample run.
- `examples/adam-optimizer/dynamic_scene_model.json` validates and tests optimizer visualization:
  noisy gradient, first moment, second moment, and adaptive update on a 3D teaching loss slice.
- `examples/ddpm-denoising/dynamic_scene_model.json` validates and tests probabilistic generation:
  fixed forward noising, closed-form noisy state, learned iterative reverse denoising.
- `examples/nerf-volume-rendering/dynamic_scene_model.json` validates and tests 3D neural rendering:
  camera ray, sample points, field query, density/color outputs, and transmittance-weighted integration.
- `./setup.sh --check-only` currently validates all four dynamic scene models.

## Hard Rules For MVP
- AI cinematic support is optional and subordinate to exact math rendering.
- Static plotting is not sufficient; the hard problem is mechanism-to-dynamic-scene reasoning.
- Manim, Three.js, Blender, Remotion, and FFmpeg are renderer/video-library execution tools, not the product definition.
- Manim owns exact formulas, matrices, graphs, and deterministic transformations.
- AI video providers own cinematic support assets, explanatory objects, metaphor shots, and transitions.
- If a video provider is unavailable in a specific run environment, still produce provider-neutral job specs and continue with deterministic renders.
- Website integration is optional delivery-surface work, not the default product path.
- Coordination happens through repo files, not chat-only decisions. Project status lives in `production_manifest.json`; executable scene details live in `enriched_scene_spec.json`; QA should be captured in `qa_report.md`.

## Person A Artifact State
- `examples/attention/input.md` defines the formula, audience, learning objective, visual scope, and out-of-scope boundaries.
- `examples/attention/mechanism_spec.json` defines the symbol ledger, causal steps, and misconception guardrails.
- `examples/attention/storyboard.md` defines the five clickable scenes.
- `examples/attention/enriched_scene_spec.json` remains the scene-level source of truth and now has declared Manim object IDs for all animation targets.
- `examples/attention/scene_specs/*.json` exists for all five scenes.
- `manim/attention_demo.py` contains one `AttentionDemo` rough pass plus five per-scene exact-layer classes.
- `manim/render.sh` renders scene layers and copies WebM outputs into `site/public/videos/scenes/`.
- All five low-quality transparent WebM scene layers have been rendered and copied to the website contract path.
- A single-file low-quality rough pass exists at `site/public/videos/attention-demo.mp4`.
- Text-free PixVerse keyframe PNGs exist under `examples/attention/keyframes/`.

## Next Step
Next production step:
- Add remaining schema-backed contracts for paper decomposition, storyboard, render manifest, provider-neutral video jobs, delivery, and QA.
- Reframe `examples/attention/` as a sample run under the new workflow.
- Pick one non-attention example, likely Adam or NeRF, and push it from validated
  `dynamic_scene_model.json` into storyboard, scene contract, renderer prototype, and QA report.
