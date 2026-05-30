# PaperMotion Research Video Skill Suite

## Direction

PaperMotion should shift from a website-first demo into a Trae Solo skill suite for researchers and science communicators.

Primary job:

> Turn a paper section, formula, proof sketch, algorithm, or experimental mechanism into a scientifically cautious visual explainer video workflow.

The website is no longer the main product surface. The main surface is Trae Solo: skills, repo artifacts, terminal renders, review checklists, and reusable contracts.

## Target Users

- Researchers preparing talks, lab updates, paper explainers, and teaching material.
- Graduate students trying to build intuition for mathematical mechanisms.
- Science communicators who need accurate visual explanations rather than generic AI video.
- Technical teams who need short internal videos explaining a method, formula, or experiment.

## Product Principles

- Exact math stays deterministic: formulas, matrices, diagrams, axes, and symbolic transformations belong in Manim or equivalent code-rendered layers.
- AI video is supportive: cinematic clips, metaphors, transitions, and texture may use PixVerse or other video models, but they must not invent formulas or labels.
- Every claim needs a source link: source excerpt, symbol ledger, mechanism brief, storyboard, render, and QA should be file-backed.
- The workflow should improve research productivity, not only produce a public landing page.
- Use human-in-the-loop checkpoints before rendering and before claiming scientific correctness.

## Target Skill Suite

| Skill | Purpose | Input | Output |
| --- | --- | --- | --- |
| `research-intake` | Normalize source material, user goal, audience, target use, and run metadata. | User goal, paper/formula/algorithm/proof sketch, repo state | `input.md`, run metadata, task-memory update |
| `paper-decomposition` | Split paper/formula/figure into video-ready structure. | `input.md`, source excerpts, figures | paper map, formula inventory, figure-to-claim map |
| `mechanism-modeling` | Extract the technical mechanism without overclaiming. | paper map, source excerpts | `mechanism_spec.json`, symbol ledger, assumptions, claim boundaries |
| `dynamic-visual-reasoning` | Convert the mechanism into a 3D/time-based visual model. | `mechanism_spec.json`, figures, target audience | `dynamic_scene_model.json`, visual objects, motion grammar, camera plan |
| `learning-path` | Decide the concept order needed for comprehension. | `mechanism_spec.json`, audience profile | prerequisite map, learning objectives, misconception risks |
| `science-script` | Write narration beats that teach the mechanism. | mechanism spec, learning path | script beats, voice intent, on-screen text draft |
| `storyboard` | Convert teaching beats into visual scenes. | script beats, mechanism spec | `storyboard.md`, scene list, visual intent |
| `scene-contract` | Freeze timing, layers, ownership, asset requirements, and output paths. | storyboard, technical constraints | `enriched_scene_spec.json`, `scene_specs/*.json`, render manifest |
| `exact-animation` | Implement deterministic math/diagram/3D mechanism visuals. | scene contracts | Manim/Three.js/Blender code, rendered exact layers, render notes |
| `cinematic-support` | Generate optional non-exact AI video prompts/keyframes/clips. | scene contracts, rendered stills | keyframes, AI video job specs, negative prompts |
| `voice-audio` | Align narration, pauses, music, and SFX to scene timing. | script beats, scene contracts, render timing | audio manifest, voiceover notes |
| `assembly-qa` | Assemble the draft and review scientific/readability quality. | all manifests, renders, audio | final draft, `qa_report.md`, blocking issue list |

The current `skills/` directory contains a coarse prototype split:

- `research-video-orchestrator`
- `paper-to-visual-brief`
- `dynamic-visual-reasoning`
- `math-storyboard-director`
- `manim-exact-layer`
- `ai-cinematic-support`
- `research-video-qa`

Keep those as transitional artifacts until the repo is ready to rename or split them into the target suite above.

`dynamic-visual-reasoning` is the first refined skill added under the new direction. It writes `examples/<demo>/dynamic_scene_model.json` and validates with `python3 scripts/validate_dynamic_scene_model.py examples/<demo>/dynamic_scene_model.json`.

## Default Workflow

1. `research-intake` creates or refreshes the project task board and memory.
2. `paper-decomposition` turns source material into video-ready structure.
3. `mechanism-modeling` extracts the symbol ledger, causal mechanism, assumptions, and claim boundaries.
4. `dynamic-visual-reasoning` decides visual objects, spatial layout, motion grammar, camera plan, and exact-vs-metaphor boundaries.
5. `learning-path` orders prerequisites and flags misconception risks.
6. `science-script` creates teachable narration beats.
7. `storyboard` creates 4-8 scenes with narration, screen text, visual action, and chapter notes.
8. `scene-contract` freezes timing, layer ownership, output paths, renderer choice, and asset requirements.
9. `exact-animation` generates or repairs deterministic rendered layers.
10. `cinematic-support` creates optional keyframes/prompts only for non-exact visual support.
11. `voice-audio` aligns voiceover and audio cues to scene timing.
12. `assembly-qa` assembles the draft and reviews source fidelity, symbol consistency, pacing, render readability, and overclaiming.

## Repo Contracts

Use this file layout for each demo or paper mechanism:

```text
examples/<demo>/
  input.md
  paper_map.json
  mechanism_spec.json
  dynamic_scene_model.json
  storyboard.md
  production_manifest.json
  enriched_scene_spec.json
  scene_specs/
  keyframes/
  render_notes.md
  qa_report.md

manim/
  <demo>_demo.py

site/
  optional; not part of the default workflow
```

`production_manifest.json` remains the project-level registry. `enriched_scene_spec.json` remains the scene-level execution contract. Website data mirrors are optional and should not drive the workflow.

## Non-Goals

- Do not build a website unless the user explicitly asks for a public demo surface.
- Do not claim fully automatic paper understanding.
- Do not let AI video generate readable math, labels, or unsupported research claims.
- Do not skip QA just because the render succeeds.
