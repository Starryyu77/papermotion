# PixVerse Keyframe Slots

Person A exports these text-free PNG keyframes after Manim render validation:

- `s01_attention_spotlight.png`: text-free token tiles with one query-color spotlight.
- `s03_heatmap_cooling.png`: text-free abstract heatmap cooling frame, with no readable formulas.
- `s05_value_streams.png`: text-free converging value streams, with no labels or symbols.

These files are inputs for `image_to_video` jobs in `examples/attention/production_manifest.json` and `examples/attention/enriched_scene_spec.json`.

Regenerate them with:

```bash
.venv/bin/python examples/attention/keyframes/generate_keyframes.py
```
