# NeRF Volume Rendering Render Notes

## Output

- Video: `site/public/videos/nerf-volume-rendering-demo.mp4`
- Poster: `site/public/videos/nerf-volume-rendering-demo-poster.jpg`
- Duration: `27.533008s`
- Renderer source: `manim/research_video_demos.py`
- Manim scene class: `NeRFVolumeRenderingDemo`

## Command

```bash
cd manim
./render_research_demos.sh nerf -ql
```

The render script renders Manim, re-encodes to H.264 Main / `yuv420p` / 30fps
/ faststart MP4, then extracts the poster frame with FFmpeg.

## Scope

This is a complete deterministic rough-pass video. It uses a 2.5D Manim view to
keep formulas, ray order, field queries, and labels exact and reviewable. A
future high-fidelity version can replace the base layer with Three.js or Blender
while preserving the same `production_manifest.json` and
`enriched_scene_spec.json` contract.
