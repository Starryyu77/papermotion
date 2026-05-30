# PaperMotion Trae Solo Runbook

## Workspace Setup

Open this folder in Trae Solo Desktop:

```text
/Users/starryyu/Downloads/trae/papermotion
```

Use this repo as the only source of truth. Every Solo task should create or update files here.

## Recommended Mode Split

MTC mode:
- Paper/formula understanding.
- Mechanism spec.
- Prerequisite graph.
- Curriculum ordering.
- Storyboard.
- Narration.
- PixVerse prompt writing.
- Music and SFX planning.
- Educational review.

Code Mode:
- Manim code.
- Render/debug loop.
- Manim still/keyframe export for PixVerse.
- PixVerse API/job execution if credentials are available.
- Website implementation.
- Local dev server.
- Browser QA.
- Final repo cleanup.

## Three-Hour Run Order

1. Run `prompts/00-solo-master-orchestrator.md`.
2. Create/update `examples/attention/production_manifest.json` and `examples/attention/enriched_scene_spec.json`.
3. Run Intent, Prerequisite Graph, and Curriculum stages through `prompts/06-agent-coordination-production-manifest.md`.
4. Run the Teaching Script and Storyboard stages through `prompts/06-agent-coordination-production-manifest.md`.
5. In parallel, run `prompts/05-website-integration.md`.
6. Run Scene Spec and Manim stages through `prompts/03-storyboard-to-manim.md`; scene-level execution details should land in `enriched_scene_spec.json`.
7. Run `prompts/07-pixverse-asset-agent.md` to create PixVerse job specs and generate clips if credentials are available.
8. Run voiceover/music/SFX planning through `prompts/06-agent-coordination-production-manifest.md`.
9. Render Manim low quality first, then final.
10. Assemble Manim + PixVerse + audio assets.
11. Embed the final MP4 and workflow artifacts in the website.

## Handoff Between Two Teammates

Person A owns the explanation film pipeline:
- `examples/attention/input.md`
- `examples/attention/production_manifest.json`
- `examples/attention/enriched_scene_spec.json`
- `examples/attention/mechanism_spec.json`
- `examples/attention/storyboard.md`
- `examples/attention/scene_specs/*.json`
- `manim/attention_demo.py`
- Rendered MP4

Person B owns the PixVerse/audio/website surface:
- PixVerse job specs and generated clips
- Voiceover/music/SFX manifests
- `site/`
- Video embed
- Chapter rail
- Workflow timeline
- README run instructions

Sync files:
- `solo/task-board.md`
- `memory/active/current.md`
- `examples/attention/production_manifest.json`
- `examples/attention/enriched_scene_spec.json`
- `examples/attention/render_notes.md`

## Stop Conditions

Do not let PixVerse overwrite exact math:
- If a PixVerse clip changes formulas or symbols, reject it and keep the Manim layer.
- If PixVerse key is missing, still keep the PixVerse job specs in the manifest and show the stage on the website.
- If PixVerse queue is slow, assemble a Manim-first version and replace the PixVerse slot later.

Reduce scope if:
- Manim render fails after two repair attempts.
- The storyboard exceeds seven scenes.
- The website first viewport does not yet show the actual demo.
