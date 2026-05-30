# NeRF Volume Rendering

Source paper: [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934)

Project/code reference: [bmild/nerf](https://github.com/bmild/nerf)

Core formulas:

```text
F_Theta: (x, d) -> (c, sigma)
C(r) = integral_{t_n}^{t_f} T(t) sigma(r(t)) c(r(t), d) dt
T(t) = exp(- integral_{t_n}^{t} sigma(r(s)) ds)
```

Target audience: researchers who understand neural networks and want a spatial intuition for neural radiance fields and differentiable volume rendering.

Learning objective: show NeRF as a continuous 5D scene function sampled along camera rays, where density and color accumulate into a rendered pixel.

Visual scope:

- Camera ray through 3D volume.
- Sample points along the ray.
- Neural field query at each sample.
- Density controls opacity/transmittance.
- Color accumulation produces a pixel.
- Camera orbit reveals novel view synthesis.

Out of scope:

- Positional encoding details.
- Hierarchical sampling details.
- Training loss derivation.
