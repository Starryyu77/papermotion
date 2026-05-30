# PaperMotion Solo Task Board

## Now

| Task | Owner | Mode | Input | Output | Acceptance |
| --- | --- | --- | --- | --- | --- |
| Create attention input artifact | Person A | MTC | `docs/research-and-mvp-plan.md` | `examples/attention/input.md` | Contains formula, target audience, and learning objective. |
| Create production manifest | Person A | MTC | `contracts/production_manifest.schema.json` | `examples/attention/production_manifest.json` | Contains project registry, intent, prerequisite graph, curriculum plan, script slots, PixVerse job slots, and pointer to enriched scene spec. |
| Generate intent/prereq/curriculum | Person A | MTC | `examples/attention/input.md` | `production_manifest` sections | Uses minimal just-in-time prerequisite policy. |
| Generate PixVerse asset plan | Person B | MTC | `production_manifest.script.beats` | `production_manifest.visual_asset_requests` | Marks which assets are PixVerse, Manim, static, or website-only. |
| Finalize focused presentation site | Person B | Code | `site/` + `examples/attention/enriched_scene_spec.json` | committed `site/` branch state | Desktop first viewport centers one film workbench, with formula overlay, chapter rail, compact workflow strip, hidden inspector drawer, and PixVerse server-side mock/proxy boundary. |

## Done

| Task | Owner | Output | Acceptance |
| --- | --- | --- | --- |
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
| Generate storyboard | Person A | MTC | `mechanism_spec.json` | `examples/attention/storyboard.md` | 5-7 scenes with narration and Manim notes. |
| Generate scene specs | Person A | MTC/Code | `production_manifest.storyboard` | `examples/attention/enriched_scene_spec.json` + optional `examples/attention/scene_specs/*.json` | Each scene has timing, narration, Manim, TTS, Music, PixVerse, Assembly, and QA fields. |
| Generate Manim script | Person A | Code | `examples/attention/enriched_scene_spec.json` + optional `scene_specs/*.json` | `manim/attention_demo.py` | Renders at low quality. |
| Configure PixVerse API proxy | Person B | Code | PixVerse API credentials | backend API route + `.env.local` convention | API key remains server-side; generate and polling routes are defined. |
| Run PixVerse jobs | Person B | Code/MTC | `production_manifest.pixverse_jobs` + `enriched_scene_spec.scenes[*].pixverse` | generated clips or job status | Uses PixVerse for cinematic support, not exact math. |
| Integrate rendered video | Person B | Code | `attention-demo.mp4` | Website video player | Video plays and chapter rail updates text. |
| Audio rhythm plan | Person B | MTC | `enriched_scene_spec.scenes[*].tts` + `music_cue` | `audio_manifest` | Voice/music/SFX align with scene timing, slowdown, and reveal beats. |

## Blocked

| Task | Blocker | Decision Needed |
| --- | --- | --- |
| None | - | - |
