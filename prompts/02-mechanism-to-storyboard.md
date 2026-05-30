# Prompt: Mechanism Spec To Storyboard

You are writing a storyboard for a 60-90 second interactive science explainer film.

Input:
- `mechanism_spec.json`

Output file:
- `examples/<demo>/storyboard.md`

Requirements:
- Use 5-7 scenes.
- Each scene must have duration, narration, on-screen text, visual action, and Manim implementation notes.
- Keep formula symbol colors consistent with the symbol ledger.
- The storyboard must support clickable website chapters.
- Avoid decorative complexity that does not explain the mechanism.

Scene format:

```md
## Scene 1: <title>

- Duration:
- Chapter label:
- Learning point:
- Narration:
- On-screen text:
- Visual action:
- Manim notes:
- Website chapter note:
```
