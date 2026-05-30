# Archive: Website And Attention Demo Direction

Archived on: 2026-05-30

## What This Captures

This archive preserves the previous PaperMotion exploration:

- a 3-hour public demo website direction,
- a Person A / Person B split,
- a scaled dot-product attention sample,
- Manim exact-layer renders,
- PixVerse cinematic support planning,
- a desktop workbench-style website prototype.

These artifacts are useful as examples, but they are no longer the default product direction.

## Why It Is Archived

The project direction has shifted from a website-first demo to a Trae Solo skill workflow for researchers and science communicators.

The main user value should be:

> help researchers turn formulas, mechanisms, paper sections, proof sketches, and algorithms into accurate visual explainer videos inside Trae Solo.

The website may still be useful later as an optional presentation or public demo surface, but it should not drive the core workflow.

## Archived Artifact Groups

### Website Demo

- `site/`
- `docs/person-b-presentation-website-design.md`
- `docs/website-builder-handoff.md`
- `handoff/website-builder/`

Status: useful as optional delivery-surface reference, not mainline product.

### Attention Demo

- `examples/attention/`
- `manim/attention_demo.py`
- `manim/render.sh`
- `site/public/videos/`

Status: useful sample workflow and render proof. It should be reframed as one example of the research-video workflow.

### Previous Planning

- `docs/research-and-mvp-plan.md`
- `docs/project-plan-fusion.md`
- `docs/trae-solo-native-workflow.md`
- `docs/agent-coordination-and-pixverse.md`
- `prompts/`

Status: keep as source material, but future edits should update wording from website-first MVP to research-video skill workflow.

## New Mainline

Use `docs/papermotion-mainline.md` as the current orientation document.
