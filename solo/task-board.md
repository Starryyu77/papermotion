# PaperMotion Solo Task Board

## Now

| Task | Owner | Mode | Input | Output | Acceptance |
| --- | --- | --- | --- | --- | --- |
| Refine research-video skill suite | Shared | MTC/Code | `docs/execution-summary.md` + `skills/` | bounded Trae Solo skills | Skills map cleanly to paper decomposition, mechanism modeling, dynamic visual reasoning, scene contracts, renderer execution, and QA. |
| Add skill output schemas | Shared | Code | `docs/execution-summary.md` | `contracts/*schema.json` | Contracts cover run metadata, paper map, mechanism spec, dynamic scene model, storyboard, render manifest, AI video jobs, delivery manifest, and QA report. |
| Reframe attention demo as sample run | Shared | MTC/Code | `examples/attention/` | sample under new workflow | Attention artifacts use `examples/attention/outputs/` as default output root; website remains optional mirror. |

## Done

| Task | Owner | Output | Acceptance |
| --- | --- | --- | --- |
| Create attention input artifact | Person A | `examples/attention/input.md` | Contains formula, target audience, learning objective, visual scope, and out-of-scope boundaries. |
| Archive old website and attention direction | Shared | `docs/archive/2026-05-30-website-and-attention-demo.md` | Previous 3-hour website, Person A/B split, and attention demo are preserved as reference rather than active product direction. |
| Rebuild PaperMotion mainline | Shared | `docs/papermotion-mainline.md`, `README.md`, `memory/active/current.md` | Current repo direction is research-video production through Trae Solo skills, not website-first work. |
| Align skill-suite design doc | Shared | `docs/research-video-skill-suite.md` | Target suite now includes paper decomposition, mechanism modeling, and dynamic visual reasoning as first-class stages. |
| Capture execution summary | Shared | `docs/execution-summary.md` | Defines Trae Solo base abilities, PaperMotion's missing layers, dynamic 3D visual reasoning, video-library boundaries, phases, and immediate next work. |
| Design dynamic scene model | Shared | `docs/dynamic-scene-model.md`, `contracts/dynamic_scene_model.schema.json`, `skills/dynamic-visual-reasoning/SKILL.md`, `examples/attention/dynamic_scene_model.json` | Defines renderer-neutral visual IR, validates the attention sample against schema, and exposes it as a Trae Solo skill. |
| Package PaperMotion as skill pack SKU | Shared | `papermotion.sku.json`, `skills/papermotion-research-video/SKILL.md`, `prompts/trae-install-sku.md`, `docs/install.md`, `setup.sh` | Trae installs from the SKU skill list, registers each `SKILL.md` by frontmatter, treats `./setup.sh --check-only` as post-install validation, and does not default to website work. |
| Validate dynamic scene model generalization | Shared | `examples/adam-optimizer/dynamic_scene_model.json`, `examples/ddpm-denoising/dynamic_scene_model.json`, `examples/nerf-volume-rendering/dynamic_scene_model.json`, `examples/README.md` | Four examples now validate: attention, Adam optimizer, DDPM denoising, and NeRF volume rendering. |
| Create mechanism spec | Person A | `examples/attention/mechanism_spec.json` | Defines symbol ledger, causal steps, and misconception guardrails. |
| Create production manifest | Person A | `examples/attention/production_manifest.json` | Contains project registry, intent, prerequisite graph, curriculum plan, script slots, PixVerse job slots, scene spec pointer, asset manifest, and edit decision list. |
| Generate intent/prereq/curriculum | Person A | `examples/attention/production_manifest.json` | Uses minimal just-in-time prerequisite policy. |
| Generate storyboard | Person A | `examples/attention/storyboard.md` | 5 scenes with narration, on-screen text, visual action, Manim notes, and website chapter notes. |
| Generate scene specs | Person A | `examples/attention/enriched_scene_spec.json` + `examples/attention/scene_specs/*.json` | All five scenes have timing, narration, Manim, TTS, Music, PixVerse, Assembly, and QA fields; contract object IDs are reconciled. |
| Generate Manim script and scene layers | Person A | `manim/attention_demo.py`, `manim/render.sh`, `site/public/videos/scenes/*.webm` | Includes one `AttentionDemo` rough pass and five scene-layer classes; all five low-quality transparent WebM layers render successfully. |
| Export PixVerse keyframes | Person A | `examples/attention/keyframes/*.png` | Provides text-free PNG inputs for the three image-to-video PixVerse jobs. |
| Create Person B website design spec | Person B | `docs/person-b-presentation-website-design.md` | Covers functions, visual direction, PixVerse API flow, and interaction motion. |
| Package website-builder handoff | Person B | `docs/website-builder-handoff.md` | Standalone brief that can be given to a dedicated website-building tool. |
| Fuse updated project plan | Shared | `docs/project-plan-fusion.md` | Reconciles Formula2Video plan with PaperMotion/Solo/website direction. |
| Add enriched scene spec contract | Shared | `contracts/enriched_scene_spec.schema.json` | Defines scene-level SSOT fields for Manim, TTS, Music, PixVerse, Assembly, and QA. |
| Add attention enriched scene spec seed | Shared | `examples/attention/enriched_scene_spec.json` | Gives the website and downstream agents a concrete scene-level contract to read. |
| Build focused website skeleton | Person B | `site/` | Zero-dependency local desktop website loads manifest/spec data and supports scene navigation, formula token jumps, hidden inspector panels, and mock PixVerse generate/status flow. |
| Clarify first-viewport product story | Person B | `site/index.html`, `site/styles/main.css` | First viewport now states formula-to-film promise, shows input/output conversion, and exposes Formula -> Mechanism -> Scene Spec -> Render Layers -> Explainer Film. |

## Next

| Task | Owner | Mode | Input | Output | Acceptance |
| --- | --- | --- | --- | --- | --- |
| Update prompt set | Shared | MTC | `prompts/` | research-video prompt sequence | `website-integration` is optional delivery-surface work, not default sequence. |
| Add QA report for attention sample | Shared | MTC | `examples/attention/` | `examples/attention/qa_report.md` | Checks source fidelity, symbol consistency, readability, pacing, output existence, and claim boundaries. |
| Decide first real researcher use case | Shared | MTC | user-selected paper/formula | new `examples/<demo>/` run | Demo targets a research productivity scenario, not a public landing page. |
| Turn one validated DSM into a second rendered sample | Shared | MTC/Code | `examples/adam-optimizer/`, `examples/ddpm-denoising/`, or `examples/nerf-volume-rendering/` | storyboard, scene contract, renderer prototype, QA report | Proves the skill pack can move beyond DSM into video production for a non-attention paper. |

## Blocked

| Task | Blocker | Decision Needed |
| --- | --- | --- |
| None | - | - |
