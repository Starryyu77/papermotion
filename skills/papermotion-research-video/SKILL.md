---
name: papermotion-research-video
description: Use as the root PaperMotion skill pack for Trae Solo research-video work. Installs or coordinates PaperMotion skills that turn papers, formulas, algorithms, proofs, model mechanisms, and figures into file-backed dynamic scientific explainer video workflows.
---

# PaperMotion Research Video

Use this as the root skill when a user installs PaperMotion from GitHub or asks to generate a research explainer video from technical material.

PaperMotion is a skill pack, not a website template. Its job is to coordinate repo-backed skills that produce research-video artifacts.

## Install Or Bootstrap

When installing from GitHub:

1. Clone the repository.
2. Read `papermotion.sku.json`.
3. Treat `papermotion.sku.json.skills[]` as the authoritative skill list.
4. For each listed `SKILL.md`, read frontmatter `name` and `description`.
5. Import, register, or load exactly those skills through Trae's skill mechanism.
6. Mark installation complete when the listed skills are registered or loadable and this root skill is available.
7. Run `./setup.sh --check-only` as post-install validation.
8. Run full `./setup.sh` only when a local validation environment must be created or refreshed.
9. Report installed skills, registration metadata, validation status, and discovered examples.

If Trae does not expose a native skill registry, keep the repo as the skill workspace and load the `SKILL.md` files listed in `papermotion.sku.json.skills[]` directly when each stage triggers.

## Child Skill Routing

| Intent | Child skill path | Frontmatter name |
| --- | --- | --- |
| Coordinate an end-to-end research-video run and update repo task state. | `skills/research-video-orchestrator/SKILL.md` | `research-video-orchestrator` |
| Convert source material into `input.md` and `mechanism_spec.json`. | `skills/paper-to-visual-brief/SKILL.md` | `paper-to-visual-brief` |
| Turn a mechanism into `dynamic_scene_model.json`. | `skills/dynamic-visual-reasoning/SKILL.md` | `dynamic-visual-reasoning` |
| Produce storyboard and scene-level teaching beats. | `skills/math-storyboard-director/SKILL.md` | `math-storyboard-director` |
| Implement deterministic formulas, matrices, diagrams, and exact animation layers. | `skills/manim-exact-layer/SKILL.md` | `manim-exact-layer` |
| Create optional non-exact cinematic support specs and provider prompts. | `skills/ai-cinematic-support/SKILL.md` | `ai-cinematic-support` |
| Review source fidelity, visual clarity, pacing, and claim boundaries. | `skills/research-video-qa/SKILL.md` | `research-video-qa` |

## Default Workflow

1. Intake source material and target audience.
2. Decompose paper/formula/figure into video-ready structure.
3. Build or repair `mechanism_spec.json`.
4. Use `dynamic-visual-reasoning` to create `dynamic_scene_model.json`.
5. Write storyboard and scene contracts.
6. Route exact layers to deterministic renderers.
7. Route optional cinematic support to AI video providers with strict guardrails.
8. Assemble and QA the research-video draft.

## Required Contracts

For dynamic-scene skill tests:

- `examples/<demo>/input.md`
- `examples/<demo>/mechanism_spec.json`
- `examples/<demo>/dynamic_scene_model.json`

For full video production runs, add:

- `examples/<demo>/storyboard.md`
- `examples/<demo>/enriched_scene_spec.json`
- `examples/<demo>/qa_report.md`

Validate dynamic scene models with:

```bash
./setup.sh --check-only
```

For a single file, use `python3 scripts/validate_dynamic_scene_model.py examples/<demo>/dynamic_scene_model.json` only when that Python runtime can import `jsonschema`.

## Guardrails

- Do not make website work the default path.
- Do not treat paper summary as enough.
- Do not use 3D as decoration.
- Do not delegate exact formulas, labels, axes, matrix dimensions, proof states, graph topology, or quantitative claims to AI video providers.
- Keep all decisions file-backed.
