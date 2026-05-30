# PaperMotion Execution Summary

Updated on: 2026-05-30

## Decision

PaperMotion will be built as a Trae Solo skill workflow for research video generation.

It will not duplicate Trae Solo's base agent abilities. Trae Solo can already read files, inspect PDFs/images, write code, coordinate agents, and operate a workspace. PaperMotion adds the missing research-video layer:

1. paper decomposition for video-ready understanding,
2. dynamic visual reasoning for 3D/time-based explanation,
3. video generation through renderer and video-library skills.

The central product problem is not static scientific plotting. It is turning a technical mechanism into a scientifically defensible dynamic visual model.

```text
paper / formula / figure / algorithm
  -> video-ready decomposition
  -> mechanism model
  -> dynamic 3D visual abstraction
  -> scene contract
  -> renderer / video library execution
  -> assembled research explainer
  -> scientific visual QA
```

## What Trae Solo Already Provides

PaperMotion should assume these base abilities exist:

- read papers, PDFs, images, figures, and local project files,
- summarize and reason over source material,
- write and modify code,
- run terminal commands and render pipelines,
- coordinate multiple agents or modes,
- maintain repo files as working memory.

PaperMotion should not spend its main effort rebuilding these abilities.

## What PaperMotion Must Add

### 1. Paper Decomposition

Trae Solo can read a paper, but PaperMotion needs a more structured decomposition step.

This step turns a paper or formula into video-production inputs:

- research question,
- source claims,
- section map,
- formula inventory,
- symbol ledger,
- figure-to-claim map,
- method components,
- causal or computational mechanism,
- assumptions and claim boundaries,
- parts that are visualizable,
- parts that should not be visually overinterpreted.

Output should be file-backed, not chat-only.

### 2. Dynamic Visual Reasoning

This is the core research challenge.

PaperMotion is not only drawing scientific charts. It must decide how an abstract mechanism should become a 3D or time-based explanatory scene.

The system needs to answer:

- What are the visual objects?
- Which objects are nodes, layers, planes, paths, fields, particles, volumes, graphs, matrices, or surfaces?
- What moves, transforms, flows, appears, disappears, merges, splits, or rotates?
- Which relationships require time sequencing?
- Which relationships require 3D space?
- What camera motion improves understanding rather than decoration?
- What must stay exact and deterministic?
- What can be metaphorical or cinematic?

This layer should produce `examples/<demo>/dynamic_scene_model.json` before storyboard and rendering.

The current field guide is `docs/dynamic-scene-model.md`, the machine-readable contract is `contracts/dynamic_scene_model.schema.json`, and semantic validation runs through `scripts/validate_dynamic_scene_model.py`.

### 3. Video Generation Through Libraries

Trae Solo does not natively generate final videos. PaperMotion should use skills to call appropriate video libraries and renderers.

Default renderer boundaries:

- Manim: exact formulas, matrices, geometry, derivations, axes, and proof-state animation.
- Three.js / WebGL: spatial mechanisms, interactive 3D prototypes, network/layer/field scenes.
- Blender: high-quality 3D scenes, camera movement, materials, and complex 3D object animation.
- Remotion: timeline composition, captions, voiceover alignment, UI-like overlays, final video assembly.
- FFmpeg: stitching, transcoding, muxing, compression, and delivery export.
- AI video providers: optional cinematic support, backgrounds, metaphors, transitions, and non-exact visual material.

AI video providers must not generate readable equations, labels, citations, or unsupported scientific claims.

## Target Skill Suite

The execution suite should evolve toward these skills:

| Skill | Role | Main Output |
| --- | --- | --- |
| `research-intake` | Normalize source, goal, audience, and run metadata. | `input.md`, run metadata |
| `paper-decomposition` | Split paper/formula/figure into video-ready structure. | paper map, formula inventory, figure-to-claim map |
| `mechanism-modeling` | Build symbol ledger, causal steps, method graph, and boundaries. | `mechanism_spec.json` |
| `dynamic-visual-reasoning` | Convert mechanism into 3D/time-based visual model. | `dynamic_scene_model.json` |
| `learning-path` | Decide concept order and prerequisite path. | learning path fields |
| `science-script` | Write narration beats and teaching intent. | script beats |
| `storyboard` | Convert script and visual model into scene sequence. | `storyboard.md` |
| `scene-contract` | Freeze timing, camera, layers, renderer choice, assets, and paths. | `enriched_scene_spec.json`, `scene_specs/*.json` |
| `exact-animation` | Render deterministic math/mechanism layers. | Manim/Three.js/Blender code and exact renders |
| `cinematic-support` | Produce optional non-exact support assets. | provider-neutral AI video jobs, keyframes |
| `voice-audio` | Generate or align narration, subtitles, pauses, music, and SFX. | audio manifest |
| `assembly-qa` | Assemble video and review scientific/readability quality. | draft video, `qa_report.md` |

## Required File Contracts

Each run should use this layout:

```text
examples/<demo>/
  input.md
  paper_map.json
  mechanism_spec.json
  dynamic_scene_model.json
  learning_path.json
  storyboard.md
  enriched_scene_spec.json
  scene_specs/
  keyframes/
  outputs/
  render_notes.md
  qa_report.md
```

Renderer code should live in renderer-specific folders:

```text
manim/
three/
blender/
remotion/
```

The website, if present, remains optional presentation infrastructure.

## Execution Phases

### Phase 0: Freeze Direction

Goal: make the repo point consistently at the research-video workflow.

Tasks:

- archive website-first and Person A/B framing,
- update README and task board,
- keep `docs/execution-summary.md` as the operating summary,
- keep `docs/papermotion-mainline.md` as the broader orientation document.

Done when new work can start without relying on previous website assumptions.

### Phase 1: Define Contracts

Goal: make skill outputs interoperable.

Tasks:

- define schemas for `paper_map.json`,
- define schemas for `mechanism_spec.json`,
- define schemas for `dynamic_scene_model.json`,
- define schemas for `enriched_scene_spec.json`,
- define provider-neutral video job specs,
- define `qa_report.md` rubric.

Done when agents can hand off through files without needing hidden context.

### Phase 2: Research Dynamic Visual Reasoning

Goal: solve the key conversion problem: mechanism to dynamic 3D scene.

Tasks:

- build a visual grammar for scientific mechanisms,
- define visual object types,
- define motion primitives,
- define camera primitives,
- define exact-vs-metaphor boundaries,
- test the grammar on scaled dot-product attention,
- test the grammar on one more paper mechanism.

Done when `dynamic_scene_model.json` can guide both storyboard and renderer selection.

### Phase 3: Build Renderer Skills

Goal: make video generation executable from scene contracts.

Tasks:

- implement or refine Manim exact animation skill,
- evaluate Three.js for spatial mechanism scenes,
- evaluate Blender for higher-quality 3D scenes,
- use Remotion for timeline/caption/assembly work,
- use FFmpeg for final export,
- keep AI video support provider-neutral.

Done when a scene contract can produce draft video assets without manual redesign.

### Phase 4: Produce Sample Runs

Goal: prove the pipeline on real examples.

Tasks:

- reframe the current attention demo as sample run 1,
- create `dynamic_scene_model.json` for attention,
- move outputs toward `examples/attention/outputs/`,
- add `qa_report.md`,
- choose a second real paper or formula with stronger 3D needs.

Done when the repo contains at least one end-to-end research-video sample with QA.

## Non-Negotiable Rules

- Do not make website work the default product path.
- Do not treat paper summarization as enough.
- Do not treat static plotting as enough.
- Do not use 3D as decoration; it must explain a relationship, mechanism, or transformation.
- Do not let AI video generate exact math, labels, citations, or unsupported claims.
- Keep every important stage file-backed.
- QA must check scientific meaning, not just render success.

## Immediate Next Work

1. Add contract schemas for paper decomposition and dynamic scene modeling.
2. Split or rename current prototype skills into the target skill suite.
3. Validate `dynamic_scene_model.json` on a second non-attention paper mechanism.
4. Update prompt templates to make dynamic visual reasoning a required stage.
5. Decide the second demo that truly requires 3D dynamic explanation.
