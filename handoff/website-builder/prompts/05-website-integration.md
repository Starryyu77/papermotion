# Prompt: Website Integration In Trae Solo

You are building the PaperMotion website inside Trae Solo Code Mode.

Goal:
- Build the public demo surface for the Trae Solo workflow.
- The first screen should show the actual explainer experience, not a generic landing page.

Input files:
- `docs/research-and-mvp-plan.md`
- `docs/project-plan-fusion.md`
- `docs/person-b-presentation-website-design.md`
- `docs/trae-solo-native-workflow.md`
- `examples/attention/production_manifest.json`
- `examples/attention/enriched_scene_spec.json`
- `examples/attention/mechanism_spec.json`
- `examples/attention/storyboard.md`
- `site/public/videos/attention-demo.mp4` if available

If the video is not available yet:
- Use a clearly marked placeholder panel.
- Build the player and chapter UI so the MP4 can be dropped in later.

Required UI:
- Demo video player or placeholder.
- Clickable chapter rail.
- Current scene explanation.
- Formula ledger with stable symbol colors.
- Workflow timeline: input -> intent -> prerequisite graph -> curriculum -> script -> storyboard -> enriched scene spec -> Manim/TTS/Music/PixVerse -> assembly -> website.
- Scene Spec Inspector showing timing, visual type, Manim, TTS, music cue, PixVerse cue, assembly, and QA checks for the active scene.
- Assembly Monitor showing layer readiness across scenes.
- Artifact preview cards for input, mechanism spec, storyboard, and render notes.
- A clear note that Trae Solo is the workspace where the workflow runs.

Design direction:
- Retro desktop-inspired `PaperMotionOS` workbench with early desktop UI references, without copying Apple or Microsoft assets.
- Avoid a generic marketing hero.
- Use the demo content in the first viewport.
- No oversized empty cards.
- Keep text compact and readable.

Acceptance checks:
- Site runs locally.
- First viewport shows the demo player and chapter rail.
- First viewport shows or can focus Film, Formula, PixVerse, Workflow, Scene Spec, and Assembly windows.
- No text overlaps at desktop or mobile widths.
- The workflow visibly references file-backed artifacts.
- The video path can be swapped without code changes if possible.
