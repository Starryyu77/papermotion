# DDPM Denoising Render Notes

## Output

- Video: `site/public/videos/ddpm-denoising-demo.mp4`
- Poster: `site/public/videos/ddpm-denoising-demo-poster.jpg`
- Duration: `25.733333s`
- Renderer source: `manim/research_video_demos.py`
- Manim scene class: `DDPMDenoisingDemo`

## Command

```bash
cd manim
./render_research_demos.sh ddpm -ql
```

The render script renders Manim, re-encodes to H.264 Main / `yuv420p` / 30fps
/ faststart MP4, then extracts the poster frame with FFmpeg.

## Scope

This is a complete deterministic rough-pass video. It uses schematic particles
and teaching tiles to explain the mechanism. It does not attempt photorealistic
image generation, U-Net internals, training loss, or classifier-free guidance.
