# DDPM Reverse Diffusion

Source paper: [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)

Core formulas:

```text
q(x_t | x_{t-1}) = N(sqrt(1 - beta_t) x_{t-1}, beta_t I)
q(x_t | x_0) = N(sqrt(alpha_bar_t) x_0, (1 - alpha_bar_t) I)
```

Target audience: ML researchers and graduate students who know generative modeling but want a visual explanation of forward noising and learned reverse denoising.

Learning objective: show diffusion as a time-indexed probabilistic chain where data is gradually corrupted into noise, then sampled backward by learned denoising steps.

Visual scope:

- Clean sample point or image patch.
- Forward trajectory into a noise cloud.
- Noise schedule over time.
- Reverse denoising trajectory.
- Distribution cloud narrowing toward the data manifold.

Out of scope:

- Full variational lower bound derivation.
- U-Net architecture internals.
- Classifier-free guidance.
