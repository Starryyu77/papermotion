# Adam Optimizer Storyboard

Demo output: `site/public/videos/adam-optimizer-demo.mp4`

This storyboard turns the validated dynamic scene model into a complete
deterministic rough-pass video. The goal is to explain Adam as a mechanism:
noisy gradients are smoothed into a first moment, scaled by a second moment,
then converted into an adaptive parameter update.

## Scene Plan

| Scene | Time | Teaching Beat | Visual Action | QA Boundary |
| --- | ---: | --- | --- | --- |
| `s00_intro` | 0.0-3.7s | The topic and Adam update formula are introduced. | A title card resolves into the adaptive update formula at the top of the frame. | Intro time is explicit so chapter timestamps do not point into the title card. |
| `s01_gradient_sample` | 3.7-8.6s | A stochastic gradient is sampled at the current parameter point. | A yellow `theta_t` point appears on a 2D teaching loss slice; several red `g_t` arrows show noisy candidate directions. | The surface is a pedagogical 2D slice, not a literal full loss landscape. |
| `s02_first_moment` | 8.6-13.2s | The first moment smooths noisy direction estimates. | Red gradient evidence blends into a stable blue `m_t` arrow and formula panel. | `m_t` must not be described as the current gradient alone. |
| `s03_second_moment` | 13.2-16.7s | The second moment tracks squared-gradient scale. | Purple scale halos expand around the parameter point while `v_t` is displayed. | `v_t` is squared-gradient scale, not Hessian curvature. |
| `s04_adaptive_update` | 16.7-26.6s | The corrected first moment is divided by scale and applied. | A green adaptive step moves the yellow point to `theta_{t+1}` and the summary holds. | The update must visibly depend on both `m_t` and `v_t`. |

## Renderer Decision

- Primary renderer: Manim exact layer.
- Optional cinematic layer: not used for this pass.
- Final video: single MP4 rendered by `manim/research_video_demos.py`.
- Poster: extracted from the MP4 with FFmpeg.

## Narration Draft

1. Adam combines noisy gradients, moment estimates, and adaptive scaling into one update rule.
2. Adam starts with the same raw material as stochastic gradient descent: a noisy gradient at the current parameter point.
3. The first moment turns those noisy observations into a steadier direction estimate.
4. The second moment tracks squared-gradient scale, so high-variance coordinates can be damped.
5. The final step divides the smoothed direction by that scale and moves the parameters.
