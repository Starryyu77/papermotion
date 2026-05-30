---
name: manim-exact-layer
description: Use when implementing or repairing deterministic math/research visuals for a PaperMotion explainer video. Produces Manim code, low-quality renders, render notes, and exact scene layers from storyboard and enriched scene specs.
---

# Manim Exact Layer

Use this skill for formulas, diagrams, graphs, matrices, algorithms, proof states, axes, and other exact visuals.

## Inputs

- `examples/<demo>/storyboard.md`
- `examples/<demo>/enriched_scene_spec.json`
- optional `examples/<demo>/scene_specs/*.json`

## Outputs

- `manim/<demo>_demo.py`
- `examples/<demo>/render_notes.md`
- rendered draft layers under a project-approved path

## Implementation Rules

- Render low quality first.
- Prefer simple Manim primitives: `Text`, `MathTex`, `VGroup`, `Rectangle`, `Square`, `Line`, `Arrow`, `Axes`, `Matrix`, transforms, and lagged starts.
- Keep code repairable; split helpers for repeated visual grammar.
- Use stable colors from the symbol ledger.
- Avoid external assets unless they already exist in the repo.
- Copy or document outputs so downstream assembly can find them.

## Validation

Run:

```bash
python3 -m py_compile manim/<demo>_demo.py
```

Then render at least one representative scene. If local Manim is unavailable, write the exact command and failure in `render_notes.md`.

## Guardrails

- Manim owns exact math; do not outsource formulas or labels to AI video.
- Do not call a render complete until the video file exists and has a plausible duration.
- Do not silently accept unreadable labels, overlapping text, or off-screen equations.
