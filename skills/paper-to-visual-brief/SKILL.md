---
name: paper-to-visual-brief
description: Use when converting a paper excerpt, formula, proof sketch, algorithm, or experimental mechanism into a visual mechanism brief for a research explainer video. Produces input.md and mechanism_spec.json with symbol ledger, prerequisites, causal steps, and misconception guardrails.
---

# Paper To Visual Brief

Use this skill before storyboard or rendering work.

## Inputs

- User-provided paper excerpt, formula, algorithm, theorem, proof sketch, or method section.
- Target audience and desired video use when available.
- Existing `examples/<demo>/input.md` or `mechanism_spec.json` when continuing work.

## Outputs

Write:

- `examples/<demo>/input.md`
- `examples/<demo>/mechanism_spec.json`

## Mechanism Spec Shape

Include:

- `title`
- `learning_objective`
- `source_excerpt`
- `symbol_ledger`
- `prerequisite_policy`
- `causal_steps`
- `visual_metaphors`
- `misconceptions`
- `claim_boundaries`

## Rules

- Preserve source meaning. If the source does not support a claim, mark it as unknown or out of scope.
- Define symbols before using them in scenes.
- Keep prerequisites just-in-time; do not turn the video into a textbook chapter.
- Separate exact math elements from metaphor elements.
- Prefer visual mechanisms over generic narration summaries.
