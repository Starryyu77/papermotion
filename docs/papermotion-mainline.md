# PaperMotion Mainline

## Current Repository

- GitHub: `https://github.com/Starryyu77/papermotion.git`
- Default branch: `main`
- Current local branch: `person-a-production-workflow`
- Remote branches visible locally: `origin/main`, `origin/person-b-presentation`
- Open GitHub issues: none
- Open GitHub pull requests: none

## Main Product Direction

PaperMotion is a Trae Solo skill workflow for research-video production.

It helps researchers and science communicators turn technical material into accurate visual explainer videos:

- paper sections,
- mathematical formulas,
- proof sketches,
- algorithms,
- model mechanisms,
- experimental workflows.

The default product surface is not a website. The default product surface is the Trae Solo workspace: skills, file-backed artifacts, deterministic renders, review reports, and reusable contracts.

## Core User

Primary users:

- researchers preparing talks, lab updates, and paper walkthroughs,
- graduate students trying to build intuition for mathematical mechanisms,
- science communicators producing accurate technical explainers,
- technical teams documenting a method or experiment.

## Core Promise

PaperMotion should make it faster to produce a scientifically cautious explainer video while preserving traceability from source material to visuals.

The workflow should answer:

1. What source claim or mechanism is being explained?
2. Which symbols and assumptions matter?
3. What is the minimal learning path?
4. What scenes teach the mechanism?
5. Which visual elements must be exact?
6. Which cinematic elements may be AI-generated?
7. What QA evidence supports final use?

## Main Workflow

```text
source material
  -> intake
  -> paper decomposition
  -> mechanism modeling
  -> dynamic visual reasoning
  -> learning path
  -> teaching script
  -> storyboard
  -> scene contract
  -> exact animation
  -> optional cinematic support
  -> voice/audio
  -> assembly
  -> research-video QA
```

## Recommended Skill Set

The project should evolve toward these Trae Solo skills:

| Skill | Responsibility | Default Outputs |
| --- | --- | --- |
| `research-intake` | Normalize source, audience, target use, and run metadata. | `input.md`, run metadata |
| `paper-decomposition` | Split paper/formula/figure into video-ready structure. | paper map, formula inventory, figure-to-claim map |
| `mechanism-modeling` | Extract symbols, prerequisites, causal steps, assumptions, and claim boundaries. | `mechanism_spec.json` |
| `dynamic-visual-reasoning` | Convert mechanism into a 3D/time-based visual model. | `dynamic_scene_model.json` |
| `learning-path` | Decide just-in-time concept order for understanding. | curriculum/prerequisite fields |
| `science-script` | Write narration beats and teaching intent. | script beats |
| `storyboard` | Convert beats into 4-8 visual scenes. | `storyboard.md` |
| `scene-contract` | Freeze timing, layer ownership, output paths, and asset requirements. | `enriched_scene_spec.json`, `scene_specs/*.json` |
| `exact-animation` | Implement deterministic formulas, graphs, matrices, diagrams, 3D mechanisms, and proof states. | Manim/Three.js/Blender code and rendered exact layers |
| `cinematic-support` | Produce optional non-exact AI video prompts/keyframes/clips. | AI video job specs and clips |
| `voice-audio` | Align voice, pauses, music, and SFX with scene timing. | audio manifest |
| `assembly-qa` | Assemble draft video and validate scientific/readability quality. | final draft, `qa_report.md` |

The current `skills/` folder contains an initial coarse version of this suite. It should be refined into the above smaller boundaries, with special attention to `dynamic-visual-reasoning`.

The field guide for this core layer is `docs/dynamic-scene-model.md`, and the schema is `contracts/dynamic_scene_model.schema.json`.

## File Contracts

For each research video run:

```text
examples/<demo>/
  input.md
  paper_map.json
  mechanism_spec.json
  dynamic_scene_model.json
  production_manifest.json
  storyboard.md
  enriched_scene_spec.json
  scene_specs/
  keyframes/
  outputs/
  render_notes.md
  qa_report.md

manim/
  <demo>_demo.py

skills/
  <skill-name>/SKILL.md
```

`production_manifest.json` is the project-level registry.

`enriched_scene_spec.json` is the scene-level execution contract.

`dynamic_scene_model.json` is the renderer-neutral visual reasoning contract. It decides semantic units, visual objects, spatial layout, motion grammar, camera plan, exactness policy, renderer candidates, and QA checks before scene execution fields are frozen.

`site/` is optional and should only mirror or present outputs. It should not be a required stage.

## Technical Boundaries

Manim owns:

- exact formulas,
- labels,
- axes,
- graphs,
- matrices,
- symbolic transformations,
- algorithm state,
- proof-state visuals.

AI video tools own only optional support:

- abstract transitions,
- cinematic background motion,
- metaphors,
- texture,
- non-symbolic illustrative clips.

AI video must not generate readable equations, labels, citations, or unsupported scientific claims.

## Current Repo State

`main` currently represents the original planning state for a website-backed 3-hour MVP.

`person-b-presentation` contains the website prototype direction.

`person-a-pipeline` contains an earlier Person A Manim pipeline commit.

`person-a-production-workflow` currently has uncommitted work from the attention demo and initial skill-suite pivot. Treat this branch as an exploration branch until the new mainline is cleaned and committed.

## Recommended Next Steps

1. Keep the archived website direction as reference only.
2. Rename/refine `skills/` into the execution suite above.
3. Add schema-backed contracts for:
   - run metadata,
   - paper map,
   - mechanism spec,
   - dynamic scene model,
   - storyboard,
   - render manifest,
   - provider-neutral AI video jobs,
   - delivery manifest,
   - QA report.
4. Move future outputs from `site/public/videos/...` to `examples/<demo>/outputs/...`.
5. Update prompts and docs so “website integration” becomes optional delivery-surface work.
6. Use the attention demo as the first sample run for the new skill workflow, not as the product itself.
