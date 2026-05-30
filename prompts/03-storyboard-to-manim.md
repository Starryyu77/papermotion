# Prompt: Storyboard To Manim Code

You are writing reliable Manim Community Edition code for a short educational animation.

Input:
- `storyboard.md`
- `examples/<demo>/enriched_scene_spec.json`
- Optional detailed files under `examples/<demo>/scene_specs/*.json`

Output file:
- `manim/<demo>_demo.py`

Requirements:
- Use one `Scene` class.
- Read timing, scene class names, objects, animation sequence, colors, and transparent-background requirements from the enriched scene spec where available.
- Use common Manim APIs only.
- Prefer simple groups, matrices, arrows, rectangles, labels, and transforms.
- Keep code renderable at low quality first.
- Do not use external assets unless they are already in the repo.
- Keep each scene segment short and repairable.

Render command:

```bash
uv run manim -ql manim/<demo>_demo.py <SceneClassName>
```

Fallback:

```bash
manim -ql manim/<demo>_demo.py <SceneClassName>
```
