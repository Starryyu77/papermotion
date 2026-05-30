# PaperMotion Examples

These examples are skill-pack test cases for the PaperMotion workflow. Each case
tests whether the skills can turn a paper, formula, or mechanism into a
schema-backed dynamic visual model and, where complete, a rendered research
explainer video.

## Validation

Validate all dynamic scene examples with:

```bash
./setup.sh --check-only
```

Validate one example with:

```bash
python3 scripts/validate_dynamic_scene_model.py examples/<demo>/dynamic_scene_model.json
```

The single-file command requires the active `python3` to have `jsonschema`
installed. The canonical post-install validation path is `./setup.sh --check-only`
because it selects an available Python runtime with the validator dependency.

## Current Examples

| Demo | Source | Mechanism focus | Current artifacts |
| --- | --- | --- | --- |
| `attention` | Scaled dot-product attention formula | Q/K/V roles, score matrix, softmax normalization, weighted value aggregation | `input.md`, `mechanism_spec.json`, `dynamic_scene_model.json`, `storyboard.md`, `enriched_scene_spec.json`, `production_manifest.json` |
| `adam-optimizer` | Adam optimizer paper, https://arxiv.org/abs/1412.6980 | Noisy gradient, first moment, second moment, adaptive update step | `input.md`, `mechanism_spec.json`, `dynamic_scene_model.json`, `storyboard.md`, `enriched_scene_spec.json`, `production_manifest.json`, `render_notes.md`, `qa_report.md` |
| `ddpm-denoising` | Denoising Diffusion Probabilistic Models, https://arxiv.org/abs/2006.11239 | Fixed forward noising, closed-form noisy state, learned iterative reverse denoising | `input.md`, `mechanism_spec.json`, `dynamic_scene_model.json`, `storyboard.md`, `enriched_scene_spec.json`, `production_manifest.json`, `render_notes.md`, `qa_report.md` |
| `nerf-volume-rendering` | NeRF, https://arxiv.org/abs/2003.08934 | Ray sampling, field query, density/color outputs, transmittance-weighted volume integration | `input.md`, `mechanism_spec.json`, `dynamic_scene_model.json`, `storyboard.md`, `enriched_scene_spec.json`, `production_manifest.json`, `render_notes.md`, `qa_report.md` |

## Rendered Videos

| Demo | Video | Poster | Renderer |
| --- | --- | --- | --- |
| `attention` | `site/public/videos/attention-demo.mp4` | `site/public/videos/attention-demo-poster.jpg` | `manim/attention_demo.py` |
| `adam-optimizer` | `site/public/videos/adam-optimizer-demo.mp4` | `site/public/videos/adam-optimizer-demo-poster.jpg` | `manim/research_video_demos.py::AdamOptimizerDemo` |
| `ddpm-denoising` | `site/public/videos/ddpm-denoising-demo.mp4` | `site/public/videos/ddpm-denoising-demo-poster.jpg` | `manim/research_video_demos.py::DDPMDenoisingDemo` |
| `nerf-volume-rendering` | `site/public/videos/nerf-volume-rendering-demo.mp4` | `site/public/videos/nerf-volume-rendering-demo-poster.jpg` | `manim/research_video_demos.py::NeRFVolumeRenderingDemo` |

Render the three non-attention demos with:

```bash
cd manim
./render_research_demos.sh all
```

## Example Status

`attention` remains the most detailed scene-layer sample because it includes
separate transparent WebM scene layers.

`adam-optimizer`, `ddpm-denoising`, and `nerf-volume-rendering` are now complete
single-file rough-pass video runs. Each includes storyboard, production
manifest, enriched scene spec, render notes, QA report, MP4 output, and poster
image. They validate that the same PaperMotion skill workflow generalizes to
optimization, probabilistic generation, and 3D neural rendering mechanisms.
