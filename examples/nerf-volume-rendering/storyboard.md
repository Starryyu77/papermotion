# NeRF Volume Rendering Storyboard

Demo output: `site/public/videos/nerf-volume-rendering-demo.mp4`

This storyboard turns the validated dynamic scene model into a complete
deterministic rough-pass video. The core idea: NeRF is a continuous queried
field, not a stored voxel table. A camera ray is sampled in order; each sample
queries `F_Theta(x,d)` for density and color; transmittance-weighted integration
produces one pixel.

## Scene Plan

| Scene | Time | Teaching Beat | Visual Action | QA Boundary |
| --- | ---: | --- | --- | --- |
| `s00_intro` | 0.0-3.7s | The title and rendering equation frame the video. | A title card resolves into the volume rendering equation at the top of the frame. | Intro time is explicit so chapter timestamps do not point into the title card. |
| `s01_camera_ray` | 3.7-8.2s | One highlighted camera pixel casts one ray. | A camera icon, image-plane pixel, translucent volume, and yellow `r(t)` ray appear. | One ray explains one pixel, not the whole image. |
| `s02_sample_points` | 8.2-11.8s | The ray is sampled in near-to-far order. | Blue sample beads appear along the ray with depth-order brace. | Samples must not look like a voxel grid. |
| `s03_field_query` | 11.8-16.3s | Each sample queries the continuous field. | Dashed query lines route beads to `F_Theta`; density/color chips appear. | `F_Theta` must read as a function, not lookup storage. |
| `s04_volume_integration` | 16.3-21.9s | Density and transmittance weight color contributions. | A green visibility ribbon fades with depth while color chips aggregate to `C(r)`. | Contributions are not equal-weighted. |
| `s05_many_rays` | 21.9-27.53s | Repeat over many rays to form a view. | Several faint rays sweep from the camera plane and the summary holds. | Do not introduce training loss or hierarchical sampling. |

## Renderer Decision

- Current rough-pass renderer: Manim exact layer.
- Future high-fidelity spatial renderer: Three.js or Blender for full 3D camera orbit and volume depth.
- Optional cinematic layer: not used for formulas, sample order, ray topology, or labels.
- Poster: extracted from the MP4 with FFmpeg.

## Narration Draft

1. NeRF volume rendering turns field queries along a camera ray into one pixel color.
2. One camera pixel casts one ordered ray through the scene volume.
3. NeRF samples positions along that ray from near to far.
4. The continuous neural field maps each position and view direction to density and color.
5. Transmittance decides how much later samples remain visible.
6. Repeating the process for many rays gives a rendered view.
