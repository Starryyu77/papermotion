# Scaled Dot-Product Attention Storyboard

Source mechanism: `examples/attention/mechanism_spec.json`

Formula:

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V
```

## Scene 1: Tokens Ask For Context

- Duration: 7 seconds
- Chapter label: Context question
- Learning point: A token asks which other tokens matter before any formula is shown.
- Narration: A token does not look at a sentence all at once. It asks a more local question: which other tokens matter to me right now?
- On-screen text: Which tokens matter right now?
- Visual action: Sentence tokens appear as tiles. One token receives a query-color highlight, then curved arcs connect it to relevant neighbors.
- Manim notes: Use `TokensAskForContext`; render token tiles, a highlighted active tile, and lagged curved arrows. PixVerse can provide only a text-free base-layer spotlight.
- Website chapter note: Clicking this chapter should show the input formula plus the pre-formula context question.

## Scene 2: Q K V Roles

- Duration: 10 seconds
- Chapter label: Q/K/V roles
- Learning point: Query, key, and value are functional roles created from each token.
- Narration: For each token, we create three roles: a query that asks, keys that can answer, and values that carry the information to mix.
- On-screen text: Q asks. K answers. V carries information.
- Visual action: Three token tiles split into rows of Q, K, and V cards using the global colors.
- Manim notes: Use `QKVRoles`; keep labels compact and exact. No PixVerse layer is needed because this scene depends on readable labels.
- Website chapter note: Highlight `Q`, `K`, and `V` in the formula ledger and show their symbol definitions.

## Scene 3: Similarity Heatmap

- Duration: 16 seconds
- Chapter label: Similarity scores
- Learning point: `QK^T` creates a table of pairwise relevance scores; scaling prevents over-sharp scores.
- Narration: The query compares itself with every key. These comparisons become a grid of relevance scores. Dividing by the square root of the key dimension keeps the scores from becoming too extreme too early.
- On-screen text: Pairwise relevance, then scaled.
- Visual action: Q cards and K cards appear around a heatmap. Comparison lines fill heatmap cells. High cells pulse, then the formula transforms to `QK^T / sqrt(d_k)` while the colors cool.
- Manim notes: Use `SimilarityHeatmap`; keep the heatmap deterministic and readable. PixVerse can be used only as an abstract transition before returning to the exact Manim heatmap.
- Website chapter note: Show `QK^T` and `sqrt(d_k)` as the active formula tokens.

## Scene 4: Softmax To Weights

- Duration: 10 seconds
- Chapter label: Normalize
- Learning point: Softmax converts raw scores into attention proportions.
- Narration: Softmax turns those scores into attention weights: not just who is relevant, but how much each token contributes.
- On-screen text: Scores become proportions.
- Visual action: Raw score bars appear, transform into normalized weight bars, and end with `sum_i w_i = 1`.
- Manim notes: Use `SoftmaxToWeights`; compute deterministic weights from fixed raw scores and label bars with compact numeric values.
- Website chapter note: Highlight `softmax` in the formula ledger and show the normalization explanation.

## Scene 5: Weighted Values Become Context

- Duration: 13 seconds
- Chapter label: Context vector
- Learning point: Attention weights scale value vectors, then the values merge into contextual output.
- Narration: Finally, the weights mix the value vectors. The output is the same token, now carrying context from the tokens it attended to.
- On-screen text: Weighted values become context.
- Visual action: Value streams appear with weight labels. Arrows flow toward a merge point, a context vector appears, and the full attention formula reassembles at the bottom.
- Manim notes: Use `WeightedValuesBecomeContext`; keep arrow thickness proportional to weights. PixVerse can provide an abstract text-free convergence clip as a base layer.
- Website chapter note: Highlight `V` and the full formula; show this scene as the conceptual payoff.
