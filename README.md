# PaperMotion

PaperMotion is an MVP workflow for turning complex formulas and paper mechanisms into short interactive AI visualization films.

Current focus: a 3-hour demo website that shows one end-to-end workflow:

```text
paper/formula -> intent -> prerequisite graph -> curriculum -> teaching script -> storyboard -> scene specs -> Manim exact layer + PixVerse cinematic layer -> audio -> website demo
```

## Start Here

- Planning and research: [docs/research-and-mvp-plan.md](docs/research-and-mvp-plan.md)
- Trae Solo native workflow: [docs/trae-solo-native-workflow.md](docs/trae-solo-native-workflow.md)
- Agent coordination and PixVerse: [docs/agent-coordination-and-pixverse.md](docs/agent-coordination-and-pixverse.md)
- Production manifest schema: [contracts/production_manifest.schema.json](contracts/production_manifest.schema.json)
- Trae Solo runbook: [solo/runbook.md](solo/runbook.md)
- Live task board: [solo/task-board.md](solo/task-board.md)
- Current project memory: [memory/active/current.md](memory/active/current.md)
- Trae Solo prompt templates: [prompts/](prompts/)

## Trae Solo First

Open this repo as the Trae Solo workspace. Use MTC mode for paper/formula understanding, mechanism specs, storyboards, narration, and review. Use Code Mode for Manim, website implementation, terminal rendering, browser preview, and QA.

## MVP Rule

The minimum viable demo is a working website plus one Manim-rendered exact-math explainer layer and one PixVerse cinematic support stage. Manim owns formulas and deterministic transformations; PixVerse owns cinematic support objects, atmosphere, and transitions.
