# Attention Manim Render Notes

## Current State

- `manim/attention_demo.py` contains five renderable scene classes matching `examples/attention/enriched_scene_spec.json`.
- `manim/render.sh` provides low-quality render aliases for all scenes and for `s01` through `s05`.
- Low-quality transparent WebM render has been verified for all five scene layers.
- A single-file low-quality `AttentionDemo` rough pass has been rendered to `site/public/videos/attention-demo.mp4`.
- Text-free PixVerse keyframe PNGs have been generated under `examples/attention/keyframes/`.

## Commands

Render all scenes at low quality:

```bash
cd manim
./render.sh
```

Render a single stitched rough demo:

```bash
cd manim
./render.sh demo
```

Render one scene:

```bash
cd manim
./render.sh s03
```

Fallback without the helper:

```bash
manim -ql --transparent manim/attention_demo.py SimilarityHeatmap
```

## Expected Outputs

Manim writes to its default `manim/media/videos/attention_demo/` directory. The helper also copies transparent scene layers into the site contract path:

```text
site/public/videos/scenes/
```

The assembled MP4 slots remain expected under `site/public/videos/assembled/` after audio/PixVerse assembly.

Verified scene-layer durations from `ffprobe`:

| Scene | Target | Rendered |
| --- | ---: | ---: |
| s01 | 7.0s | 7.000s |
| s02 | 10.0s | 10.000s |
| s03 | 16.0s | 15.999s |
| s04 | 10.0s | 9.999s |
| s05 | 13.0s | 12.999s |

## Verification Boundary

The script should be treated as code-ready only after:

- Python syntax compile passes.
- Manim imports are available in the project `.venv`.
- All five low-quality scene renders pass.
- Scene output paths are copied into the website contract path.
- PixVerse keyframe PNGs exist before image-to-video jobs are submitted.
