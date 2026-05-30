# Attention Demo Input Artifact

## Demo ID

`attention`

## Source Formula

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

## Source Type

Formula and mechanism description.

## Target Audience

AI-curious students or developers who have seen the Transformer attention formula but do not yet feel how the parts produce contextual token representations.

## Learning Objective

After watching the short explainer, the viewer should be able to explain:

- why `QK^T` creates pairwise relevance scores,
- why dividing by `sqrt(d_k)` stabilizes the score scale,
- why softmax turns scores into attention weights,
- how attention weights mix `V` into a contextual output.

## Visual Scope

- Token tiles and vector roles.
- Query/key similarity comparisons.
- A small score heatmap.
- Scaling as a visual cooling or calming step.
- Softmax as normalization into proportions.
- Weighted value streams merging into one context vector.

## Out Of Scope

- Multi-head attention internals.
- Full Transformer blocks.
- Training, gradients, or loss functions.
- Claims about any specific model architecture beyond scaled dot-product attention.

## Style Constraint

Use a geometric intuition explainer style: precise, calm, symbol-stable, and just-in-time. Do not impersonate a specific creator. Manim owns all exact formulas, labels, matrices, and geometry. PixVerse may only support cinematic metaphor clips without readable formulas or fake symbols.
