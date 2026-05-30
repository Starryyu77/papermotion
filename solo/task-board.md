# PaperMotion Solo Task Board

## Now

| Task | Owner | Mode | Input | Output | Acceptance |
| --- | --- | --- | --- | --- | --- |
| Create attention input artifact | Person A | MTC | `docs/research-and-mvp-plan.md` | `examples/attention/input.md` | Contains formula, target audience, and learning objective. |
| Create production manifest | Person A | MTC | `contracts/production_manifest.schema.json` | `examples/attention/production_manifest.json` | Contains intent, prerequisite graph, curriculum plan, script slots, rhythm map, PixVerse job slots. |
| Generate intent/prereq/curriculum | Person A | MTC | `examples/attention/input.md` | `production_manifest` sections | Uses minimal just-in-time prerequisite policy. |
| Generate PixVerse asset plan | Person B | MTC | `production_manifest.script.beats` | `production_manifest.visual_asset_requests` | Marks which assets are PixVerse, Manim, static, or website-only. |
| Build website skeleton | Person B | Code | `docs/trae-solo-native-workflow.md` | `site/` | First viewport has video area, chapters, and workflow timeline. |

## Next

| Task | Owner | Mode | Input | Output | Acceptance |
| --- | --- | --- | --- | --- | --- |
| Generate storyboard | Person A | MTC | `mechanism_spec.json` | `examples/attention/storyboard.md` | 5-7 scenes with narration and Manim notes. |
| Generate scene specs | Person A | MTC/Code | `production_manifest.storyboard` | `examples/attention/scene_specs/*.json` | Each scene has coordinates, objects, actions, timing, render layer. |
| Generate Manim script | Person A | Code | `scene_specs/*.json` | `manim/attention_demo.py` | Renders at low quality. |
| Run PixVerse jobs | Person B | Code/MTC | `production_manifest.pixverse_jobs` | generated clips or job status | Uses PixVerse for cinematic support, not exact math. |
| Integrate rendered video | Person B | Code | `attention-demo.mp4` | Website video player | Video plays and chapter rail updates text. |
| Audio rhythm plan | Person B | MTC | `production_manifest.rhythm_map` | `audio_manifest` | Voice/music/SFX align with slowdown/reveal beats. |

## Blocked

| Task | Blocker | Decision Needed |
| --- | --- | --- |
| PixVerse clip generation | API key/credits/time may be unavailable | If unavailable by 1:35, keep job specs and fill slot with Manim/still placeholder. |
