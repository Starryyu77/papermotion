# Prompt: Website Integration In Trae Solo

You are building the PaperMotion website inside Trae Solo Code Mode.

Goal:
- Build the public demo surface for the Trae Solo workflow.
- The first screen should show the actual explainer experience, not a generic landing page.

Input files:
- `docs/research-and-mvp-plan.md`
- `docs/trae-solo-native-workflow.md`
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
- Workflow timeline: input -> intent -> prerequisite graph -> curriculum -> script -> storyboard -> scene specs -> Manim exact layer + PixVerse cinematic layer -> audio -> website.
- Artifact preview cards for input, mechanism spec, storyboard, and render notes.
- A clear note that Trae Solo is the workspace where the workflow runs.

Design direction:
- Dense, polished, cinematic technical tool.
- Avoid a generic marketing hero.
- Use the demo content in the first viewport.
- No oversized empty cards.
- Keep text compact and readable.

Acceptance checks:
- Site runs locally.
- First viewport shows the demo player and chapter rail.
- No text overlaps at desktop or mobile widths.
- The workflow visibly references file-backed artifacts.
- The video path can be swapped without code changes if possible.
