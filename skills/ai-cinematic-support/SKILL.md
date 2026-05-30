---
name: ai-cinematic-support
description: Use when creating optional AI video support for a research explainer, such as metaphor clips, abstract transitions, atmospheric context, or non-symbolic motion. Produces keyframes, prompts, negative prompts, and job specs while preserving exact math in Manim.
---

# AI Cinematic Support

Use this skill only for non-exact support visuals.

## Inputs

- storyboard
- enriched scene spec
- rendered stills or generated keyframes
- target AI video provider constraints when known

## Outputs

- `examples/<demo>/keyframes/*.png`
- AI video job specs in `production_manifest.json`
- per-scene AI support fields in `enriched_scene_spec.json`

## Prompt Rules

Every prompt should specify:

- educational context
- motion intent
- duration
- no readable text
- no formulas
- no fake labels
- no unsupported paper claims

Every negative prompt should block:

- readable equations
- distorted text
- invented symbols
- misleading diagrams
- random labels
- noisy or chaotic motion

## Guardrails

- If a scene needs exact notation, return it to `manim-exact-layer`.
- AI video clips should be optional layers, not the source of scientific truth.
- Keyframes for AI video should be text-free unless the provider is explicitly used only for motion around a later Manim overlay.
