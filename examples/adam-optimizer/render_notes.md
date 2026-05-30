# Adam Optimizer Render Notes

## Output

- Video: `site/public/videos/adam-optimizer-demo.mp4`
- Poster: `site/public/videos/adam-optimizer-demo-poster.jpg`
- Duration: `26.600000s`
- Renderer source: `manim/research_video_demos.py`
- Manim scene class: `AdamOptimizerDemo`

## Command

```bash
cd manim
./render_research_demos.sh adam -ql
```

The render script performs three steps:

1. Render the Manim scene.
2. Re-encode the output as H.264 Main, `yuv420p`, 30fps, faststart MP4.
3. Extract a poster frame with FFmpeg.

## Scope

This is a complete deterministic rough-pass video. It intentionally avoids AI
video for formulas and labels. The visual surface is pedagogical: the 2D loss
slice, gradients, and step sizes are teaching abstractions rather than measured
optimizer traces.
