---
name: research-video-orchestrator
description: Use when coordinating a Trae Solo workflow that turns a research paper, formula, proof, algorithm, or technical mechanism into a visual explainer video. Routes work across PaperMotion skills, updates repo task state, and keeps the workflow file-backed rather than website-first.
---

# Research Video Orchestrator

Use this skill when the user wants a research or math visualization video workflow in Trae Solo.

## Workflow

1. Read `memory/active/current.md`, `solo/task-board.md`, and the current demo folder under `examples/`.
2. Decide the artifact sequence:
   - source input
   - mechanism spec
   - storyboard
   - enriched scene spec
   - Manim exact layer
   - optional AI cinematic support
   - QA report
3. Update `solo/task-board.md` so current work is file-backed.
4. Update `memory/active/current.md` with durable decisions and the next executable step.
5. Keep website work optional unless the user explicitly requests a public demo surface.

## Routing

- Source understanding: use `paper-to-visual-brief`.
- Scene design: use `math-storyboard-director`.
- Exact math rendering: use `manim-exact-layer`.
- AI video support: use `ai-cinematic-support`.
- Scientific and visual review: use `research-video-qa`.

## Guardrails

- Do not leave conclusions only in chat.
- Do not skip mechanism/spec artifacts and jump directly to video.
- Do not ask AI video tools to render formulas, axes, matrices, readable labels, or citations.
- Treat every generated video as draft until QA approves source fidelity and visual clarity.
