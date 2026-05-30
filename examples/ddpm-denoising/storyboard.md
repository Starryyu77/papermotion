# DDPM Denoising Storyboard

Demo output: `site/public/videos/ddpm-denoising-demo.mp4`

This storyboard turns the validated dynamic scene model into a complete
deterministic rough-pass video. The main idea is the DDPM split: the forward
process is a fixed noising chain, while generation is a learned iterative
reverse denoising chain.

## Scene Plan

| Scene | Time | Teaching Beat | Visual Action | QA Boundary |
| --- | ---: | --- | --- | --- |
| `s00_intro` | 0.0-3.7s | The title and closed-form formula frame the video. | A title card resolves into `q(x_t | x_0)` at the top of the frame. | Intro time is explicit so chapter timestamps do not point into the title card. |
| `s01_clean_state` | 3.7-5.9s | Start from a structured sample `x_0`. | A clean tile appears next to a timestep rail. | The tile is a teaching abstraction, not a real training image. |
| `s02_forward_noise` | 5.9-10.6s | Fixed `beta_t` adds scheduled Gaussian noise. | The sample diffuses from `x_0` toward `x_T` along the timeline. | The forward process must be labeled fixed, not learned. |
| `s03_closed_form` | 10.6-15.5s | `alpha_bar_t` lets us sample `x_t` directly from `x_0`. | A signal-retention curve and slider point to a matching noisy state. | The curve is schematic unless a toy schedule is specified. |
| `s04_reverse_denoise` | 15.5-25.73s | `epsilon_theta` guides repeated reverse steps. | A learned denoiser module routes noisy states back toward structure and the summary holds. | The reverse process must be iterative, not a one-step jump. |

## Renderer Decision

- Primary renderer: Manim exact layer.
- Optional cinematic layer: not used for this pass.
- Final video: single MP4 rendered by `manim/research_video_demos.py`.
- Poster: extracted from the MP4 with FFmpeg.

## Narration Draft

1. DDPMs separate fixed forward corruption from learned iterative reverse denoising.
2. DDPM starts with a clean structured sample, `x_0`.
3. The forward chain is fixed: each step injects scheduled Gaussian noise.
4. The closed-form expression uses cumulative signal retention to sample `x_t` directly.
5. Generation runs the learned reverse process over many denoising steps.
