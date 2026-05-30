---
name: dynamic-visual-reasoning
description: Use for PaperMotion research-video work when converting a mechanism spec, paper excerpt, formula, figure, chart, algorithm, proof sketch, model architecture, or experimental process into a renderer-neutral dynamic visual model. Produces examples/<demo>/dynamic_scene_model.json with visual objects, spatial layout, motion primitives, camera plan, exact-vs-metaphor boundaries, QA constraints, and renderer recommendations.
---

# Dynamic Visual Reasoning

Use this skill after `mechanism_spec.json` exists, or when the user asks how a technical mechanism should move, unfold, transform, or be visualized over time.

This skill does not write final renderer code. It creates the dynamic visual model that storyboard, scene-contract, Manim, Three.js, Blender, Remotion, FFmpeg, and AI-video support skills can execute.

## Inputs

Accept any subset of:

- `examples/<demo>/mechanism_spec.json`
- `examples/<demo>/paper_map.json`
- source paper excerpts, formulas, theorem/proof sketches, algorithms, method sections
- uploaded figures, charts, diagrams, tables, or screenshots
- target audience, duration, style, renderer preference, and delivery goal
- existing `storyboard.md`, `enriched_scene_spec.json`, or render notes when repairing a run

If upstream files are missing, infer a provisional model and mark unresolved source gaps in `open_questions`.

## Output

Write or propose:

```text
examples/<demo>/dynamic_scene_model.json
```

Validate against:

```text
python3 scripts/validate_dynamic_scene_model.py examples/<demo>/dynamic_scene_model.json
```

Read `docs/dynamic-scene-model.md` when you need the full field guide or research basis.

## Workflow

1. Identify the mechanism family:
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

2. Extract source-backed semantic units:
   - entities, symbols, variables, components, states, operators, relations, assumptions, invariants.

3. Define the visual ontology:
   - persistent visual objects,
   - visual encodings,
   - exactness level,
   - spatial layout,
   - object identity across beats.

4. Define the motion grammar:
   - use reusable primitives such as `split`, `compare`, `normalize`, `route`, `aggregate`, `iterate`, `converge`, and `transform`;
   - every motion must have a technical meaning.

5. Define phase-by-phase states and transitions:
   - before state,
   - operation,
   - after state,
   - invariant,
   - viewer question answered.

6. Plan camera and focus:
   - hold still during dense formulas and labels,
   - use zoom or pan only to clarify hierarchy or local detail,
   - use 3D depth only when it represents a real relationship.

7. Separate exact and metaphor layers:
   - exact formulas, labels, axes, graph topology, values, proof states, and algorithm states go to deterministic renderers;
   - AI video is optional support and must not generate readable math or claims.

8. Recommend renderers by capability:
   - Manim for exact math and deterministic diagrams,
   - Three.js for web-native spatial mechanisms,
   - Blender for polished 3D scenes,
   - Remotion for timeline, captions, overlays, and assembly,
   - FFmpeg for muxing/transcoding/export,
   - AI video providers for non-exact cinematic support only.

9. Add handoff hints:
   - storyboard beat refs,
   - scene-contract hints,
   - renderer responsibilities,
   - QA checks.

## QA Self-Check

Before finishing, verify:

- every visual object, relation, and transition traces to source material or is marked as a simplification;
- symbols have stable visual encodings;
- each animation explains a change, operation, comparison, or state transition;
- 3D is not decorative;
- exact math and metaphor layers are visibly separable;
- renderer recommendations match the task;
- open ambiguities are explicit;
- downstream storyboard and scene-contract skills can proceed without guessing the core visual mechanism.

## Fallback

If full modeling is blocked, still produce:

- `source_links`
- provisional `semantic_units`
- provisional `visual_model`
- safe `renderer_plan`
- `open_questions`
- `known_risks`

Do not silently invent unsupported mechanisms.
