---
name: math-storyboard-director
description: Use when turning a visual mechanism spec into a concise research explainer video storyboard. Produces storyboard.md and scene plans with narration, visual action, Manim notes, pacing, and chapter-level teaching goals.
---

# Math Storyboard Director

Use this skill after `mechanism_spec.json` exists.

## Inputs

- `examples/<demo>/mechanism_spec.json`
- Existing manifest or scene spec if continuing work.

## Outputs

Write:

- `examples/<demo>/storyboard.md`
- storyboard sections in `examples/<demo>/production_manifest.json` when present

## Scene Requirements

Each scene should include:

- duration
- chapter label
- learning point
- narration
- on-screen text
- visual action
- Manim implementation notes
- exact-vs-metaphor boundary
- QA risk

## Defaults

- 5-9 scenes.
- 45-120 seconds unless the user asks otherwise.
- One core idea per scene.
- Slow down at notation changes, proof pivots, algorithm state changes, and graph/geometry reveals.

## Guardrails

- Do not add decorative scenes that do not teach the mechanism.
- Do not introduce new symbols late without explanation.
- Do not use AI cinematic scenes as substitutes for exact visual reasoning.
