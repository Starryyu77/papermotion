# Dynamic Scene Model

## Purpose

`dynamic_scene_model.json` is PaperMotion's renderer-neutral visual IR.

It sits between `mechanism_spec.json` and downstream storyboard / scene contracts:

```text
paper_map.json
  -> mechanism_spec.json
  -> dynamic_scene_model.json
  -> learning_path.json / science script
  -> storyboard.md
  -> enriched_scene_spec.json
  -> renderer-specific code and assets
```

The model answers one question:

> How should a source-backed research mechanism become space, time, motion, camera, exact layers, and optional metaphor layers?

It should not contain Manim, Three.js, Blender, Remotion, FFmpeg, or AI-video provider API details. It should describe what must be shown and why; renderer bindings decide how to implement it.

## Research Basis

The design borrows from several established ideas:

- Data-state pipelines separate raw data, analytical abstraction, visual abstraction, and final view. This informs `source_links`, `semantic_units`, `visual_model`, and `camera_model`. Source: Ed Chi, [A Taxonomy of Visualization Techniques Using the Data State Reference Model](https://research.google/pubs/a-taxonomy-of-visualization-techniques-using-the-data-state-reference-model/).
- Declarative visualization grammars separate marks, encodings, layers, and selections. This informs `visual_model.objects`, `visual_model.encodings`, and renderer-neutral handoff. Source: [Vega-Lite](https://vis.mit.edu/pubs/vega-lite/).
- Staged animated transitions preserve object constancy across views. This informs `dynamic_model.states`, `dynamic_model.transitions`, and `object_correspondence`. Source: Heer and Robertson, [Animated Transitions in Statistical Data Graphics](https://idl.uw.edu/papers/animated-transitions).
- Animation grammars such as Gemini describe transition steps and composition rules. This informs `motion_primitives`, `composition`, and perceptual cost notes. Source: Kim and Heer, [Gemini](https://arxiv.org/abs/2009.01429).
- Data animation tools use enter, exit, merge, split, staging, staggering, and hierarchical keyframes. This informs `motion_primitives`, `stagger`, and `object_lifecycle`. Sources: [Data Animator](https://hdi.cs.umd.edu/papers/DataAnimator_CHI21.pdf), [Canis](https://diglib.eg.org/items/2f489f52-f081-4d03-a175-dc388880a952).
- Narrative visualization separates author guidance, reveal order, and viewer comprehension. This informs `dynamic_model.beats`, `visual_thesis`, and `handoff.storyboard_beat_refs`. Source: Segel and Heer, [Narrative Visualization](https://homes.cs.washington.edu/~jheer/files/narrative.pdf).
- Scientific storytelling treats visual elements as actors whose relationships and evolution create the story. This informs `semantic_units.entities`, `semantic_units.relations`, and `evolution_over_time`. Source: [Scientific Storytelling using Visualization](https://vis.cs.ucdavis.edu/papers/Scientific_Storytelling_CGA.pdf).
- Cinematic scientific visualization emphasizes camera, abstraction, attention guidance, and complexity control. This informs `camera_model`, `exactness_policy`, and `qa_contract`. Source: [Cinematic Scientific Visualization](https://experts.illinois.edu/en/publications/cinematic-scientific-visualization-the-art-of-communicating-scien).

## Core Principle

Do not make a scene because it looks good. Make a scene because spatial layout, motion, or camera movement encodes a source-backed relationship.

The schema separates four layers:

1. **Source and semantics**: claims, formulas, symbols, entities, operators, states, relations.
2. **Visual abstraction**: spaces, objects, encodings, layout constraints.
3. **Dynamic grammar**: beats, states, transitions, motion primitives, camera plan.
4. **Execution policy**: exactness, renderer plan, QA contract, handoff hints.

## Top-Level Shape

```json
{
  "contract_version": "dynamic-scene-model/v0.1",
  "demo_id": "attention",
  "source_links": {},
  "content_profile": {},
  "semantic_units": {},
  "visual_model": {},
  "dynamic_model": {},
  "camera_model": {},
  "exactness_policy": {},
  "renderer_plan": {},
  "handoff": {},
  "qa_contract": {},
  "open_questions": [],
  "known_risks": []
}
```

## Required Design Decisions

### Content Family

Every model should identify which families it covers:

- `formula_derivation`
- `algorithm_execution`
- `proof_sketch`
- `model_architecture`
- `data_pipeline`
- `causal_mechanism`
- `optimization_process`
- `statistical_result`
- `geometry_topology`
- `physical_simulation`
- `experimental_workflow`

This prevents the schema from becoming attention-specific. Q/K/V and softmax are only instances of entities, operators, states, relations, and transitions.

### Visual Objects

A visual object is a persistent entity that can be tracked across states and scenes. It may be exact, schematic, or metaphorical.

Common object types:

- `symbol`
- `equation`
- `matrix`
- `tensor`
- `scalar`
- `vector`
- `graph_node`
- `graph_edge`
- `layer`
- `plane`
- `surface`
- `volume`
- `field`
- `particle`
- `axis_plot`
- `distribution`
- `state_machine`
- `timeline`
- `image_patch`

Each visual object should trace back to source-backed semantic units through `entity_refs` and `source_refs`.

### Motion Primitives

Motion is the grammar of the explanation. Use stable primitives so downstream renderers can compile them consistently:

- `appear`
- `highlight`
- `trace`
- `transform`
- `split`
- `merge`
- `aggregate`
- `filter`
- `normalize`
- `project`
- `route`
- `rotate`
- `extrude`
- `sample`
- `select`
- `measure`
- `fit`
- `solve`
- `propagate`
- `diffuse`
- `iterate`
- `loop`
- `branch`
- `converge`
- `collapse`
- `expand`
- `reveal`
- `compare`
- `align`
- `disappear`
- `exit`
- `copy`
- `group`
- `sweep`

Every primitive needs a `technical_meaning`. If a movement has no technical meaning, it belongs in an optional cinematic layer, not the core dynamic model.

### Exactness Levels

Use exactness to protect scientific meaning:

- `symbolic_exact`: formula, label, theorem/proof state, symbolic transform.
- `numeric_exact`: quantitative chart, score, probability, loss value, dimension.
- `topology_exact`: source-defined graph, architecture, dependency, or connectivity.
- `qualitative`: accurate high-level trend without exact values.
- `pedagogical_simplification`: explicitly simplified for teaching.
- `metaphor`: visual analogy that is not a claim.
- `forbidden`: should not appear.

### Renderer Planning

Renderer recommendation is capability-based:

- `manim`: exact formulas, matrices, axes, diagrams, proof states, deterministic transitions.
- `threejs`: interactive or web-native spatial mechanisms, networks, fields, layers.
- `blender`: polished 3D scenes, camera movement, materials, complex object animation.
- `remotion`: timeline composition, captions, voiceover alignment, overlays.
- `ffmpeg`: stitching, muxing, transcoding, overlays, delivery export.
- `ai_video_provider`: optional non-exact cinematic support only.

AI video providers must not generate readable equations, labels, citations, exact values, or unsupported scientific claims.

## Handoff Rules

- Storyboard scenes should reference `dynamic_model.beats[*].id`.
- Scene contracts should reference visual object IDs and motion primitive IDs instead of inventing new names.
- Renderer-specific fields should live in `enriched_scene_spec.json`, renderer bindings, or provider job specs, not in `dynamic_scene_model.json`.
- Every simplification should state what was simplified, why it is acceptable, and how it should be disclosed or guarded in QA.
- Validate both JSON Schema shape and semantic references with `python3 scripts/validate_dynamic_scene_model.py examples/<demo>/dynamic_scene_model.json`.

## QA Rules

Before downstream production, check:

- Every visual object, relation, and state transition traces to source material or is marked as a simplification.
- Symbols have stable encodings.
- Motion represents a technical operation, state change, comparison, or relationship.
- 3D space is used only when depth clarifies a mechanism.
- Camera movement does not hide formulas, labels, or quantitative evidence.
- Exact and metaphor layers are visibly separable.
- Renderer choices match the visual need and fallback path.
- The model would still work for a different paper family, not only the current sample.
