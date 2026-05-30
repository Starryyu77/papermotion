# Adam Optimizer Landscape

Source paper: [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)

Core formulas:

```text
m_t = beta_1 m_{t-1} + (1 - beta_1) g_t
v_t = beta_2 v_{t-1} + (1 - beta_2) g_t^2
theta_t = theta_{t-1} - alpha * m_hat_t / (sqrt(v_hat_t) + epsilon)
```

Target audience: graduate students and researchers who know gradient descent but have not internalized Adam's adaptive moment logic.

Learning objective: show Adam as an iterative optimizer that smooths gradients with a first moment, estimates per-direction scale with a second moment, and turns both into an adaptive parameter step.

Visual scope:

- 2D loss surface or contour field.
- Parameter point moving over time.
- Raw gradient arrows.
- First-moment smoothing arrow.
- Second-moment uncertainty or scale field.
- Adaptive step arrow.

Out of scope:

- Full convergence proof.
- Hyperparameter tuning details.
- Bias-correction derivation beyond showing corrected moment estimates.
