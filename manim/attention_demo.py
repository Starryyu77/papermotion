"""
PaperMotion – Scaled Dot-Product Attention
Person A: Manim exact-layer implementation

Source contract: examples/attention/enriched_scene_spec.json
Style tokens:    global_style_tokens in the same file

Render each scene (low quality, transparent bg):
    manim -ql attention_demo.py AttentionDemo
    manim -ql --transparent attention_demo.py TokensAskForContext
    manim -ql --transparent attention_demo.py QKVRoles
    manim -ql --transparent attention_demo.py SimilarityHeatmap
    manim -ql --transparent attention_demo.py SoftmaxToWeights
    manim -ql --transparent attention_demo.py WeightedValuesBecomeContext

Render all at once:
    manim -ql --transparent attention_demo.py

Output: media/videos/attention_demo/480p15/partial_movie_files/
"""

from __future__ import annotations

import numpy as np
from manim import (
    BOLD,
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    TAU,
    UP,
    AnimationGroup,
    Arrow,
    CurvedArrow,
    DashedLine,
    FadeIn,
    FadeOut,
    Indicate,
    LaggedStart,
    MathTex,
    ManimColor,
    MovingCameraScene,
    Rectangle,
    RoundedRectangle,
    Scene,
    Square,
    Text,
    Transform,
    TransformMatchingTex,
    VGroup,
    Write,
    Create,
    Line,
)

# ============================================================
# Global Style Tokens (mirrors enriched_scene_spec.json)
# ============================================================
BG            = ManimColor("#101217")
QUERY_COLOR   = ManimColor("#7DD3FC")
KEY_COLOR     = ManimColor("#A7F3D0")
VALUE_COLOR   = ManimColor("#F9A8D4")
SCORE_COLOR   = ManimColor("#FBBF24")
SCALE_COLOR   = ManimColor("#FCA5A5")
SOFTMAX_COLOR = ManimColor("#C4B5FD")
CONTEXT_COLOR = ManimColor("#37D67A")
TEXT_COLOR    = ManimColor("#E5E7EB")
MUTED_COLOR   = ManimColor("#6B7280")


# ============================================================
# Helpers
# ============================================================

def token_tile(word: str, *, width: float = 1.4, height: float = 0.65,
               border: ManimColor = TEXT_COLOR,
               fill: ManimColor = BG) -> VGroup:
    """Rounded rectangle with a word label inside."""
    rect = RoundedRectangle(
        corner_radius=0.1,
        width=width,
        height=height,
        stroke_color=border,
        stroke_width=1.8,
        fill_color=fill,
        fill_opacity=1.0,
    )
    lbl = Text(word, color=TEXT_COLOR, font_size=22)
    lbl.move_to(rect)
    return VGroup(rect, lbl)


def role_card(letter: str, color: ManimColor,
              width: float = 0.75, height: float = 0.58) -> VGroup:
    """Small coloured card with a single letter."""
    rect = RoundedRectangle(
        corner_radius=0.08,
        width=width,
        height=height,
        stroke_color=color,
        stroke_width=2.0,
        fill_color=color,
        fill_opacity=0.22,
    )
    lbl = Text(letter, color=color, font_size=22, weight=BOLD)
    lbl.move_to(rect)
    return VGroup(rect, lbl)


def score_lerp_color(value: float,
                     lo: ManimColor = BG,
                     hi: ManimColor = SCORE_COLOR) -> ManimColor:
    """Linearly interpolate between two colours by a [0,1] score."""
    t = float(np.clip(value, 0.0, 1.0))
    r = lo.to_rgb()[0] + (hi.to_rgb()[0] - lo.to_rgb()[0]) * t
    g = lo.to_rgb()[1] + (hi.to_rgb()[1] - lo.to_rgb()[1]) * t
    b = lo.to_rgb()[2] + (hi.to_rgb()[2] - lo.to_rgb()[2]) * t
    return ManimColor.from_rgb((r, g, b))


# ============================================================
# Single-scene rough pass for the documented render command
# ============================================================
class AttentionDemo(Scene):
    """
    A compact, single-scene pass through the five Person A beats.

    The per-scene classes below remain the source for transparent exact layers.
    This wrapper exists so the MVP render command can produce one rough demo
    video without an assembly step.
    """

    def construct(self) -> None:
        self.camera.background_color = BG

        title = Text("Scaled Dot-Product Attention", color=TEXT_COLOR, font_size=36)
        formula = MathTex(
            r"\mathrm{Attention}(Q,K,V)"
            r"=\mathrm{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V",
            font_size=34,
            color=TEXT_COLOR,
        )
        formula.next_to(title, DOWN, buff=0.35)
        self.play(Write(title), Write(formula), run_time=2.0)
        self.wait(0.5)
        self.play(FadeOut(title), formula.animate.to_edge(UP, buff=0.35), run_time=1.0)

        words = ["The", "cat", "sat", "on", "mat"]
        tiles = VGroup(*[token_tile(w) for w in words]).arrange(RIGHT, buff=0.35)
        tiles.shift(UP * 1.2)
        highlight = RoundedRectangle(
            corner_radius=0.1,
            width=1.55,
            height=0.78,
            stroke_color=QUERY_COLOR,
            stroke_width=3,
            fill_color=QUERY_COLOR,
            fill_opacity=0.18,
        ).move_to(tiles[1])
        arcs = VGroup(
            *[
                CurvedArrow(
                    tiles[1].get_center(),
                    tile.get_center(),
                    angle=(-TAU / 10 if i > 1 else TAU / 10),
                    color=QUERY_COLOR,
                    stroke_width=1.5,
                    stroke_opacity=0.5,
                    tip_length=0.12,
                )
                for i, tile in enumerate(tiles)
                if i != 1
            ]
        )
        caption = Text("A token asks what matters now.", color=MUTED_COLOR, font_size=22)
        caption.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(tiles, lag_ratio=0.15), Create(highlight), Write(caption), run_time=2.0)
        self.play(LaggedStart(*[Create(arc) for arc in arcs], lag_ratio=0.2), run_time=2.0)
        self.play(FadeOut(arcs), FadeOut(highlight), FadeOut(caption), tiles.animate.shift(UP * 1.0), run_time=1.0)

        q_row = VGroup(*[role_card("Q", QUERY_COLOR) for _ in words]).arrange(RIGHT, buff=0.7)
        k_row = VGroup(*[role_card("K", KEY_COLOR) for _ in words]).arrange(RIGHT, buff=0.7)
        v_row = VGroup(*[role_card("V", VALUE_COLOR) for _ in words]).arrange(RIGHT, buff=0.7)
        q_row.next_to(tiles, DOWN, buff=0.55)
        k_row.next_to(q_row, DOWN, buff=0.35)
        v_row.next_to(k_row, DOWN, buff=0.35)
        role_label = Text("Q asks, K answers, V carries information.", color=TEXT_COLOR, font_size=22)
        role_label.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(q_row, lag_ratio=0.1), FadeIn(k_row, lag_ratio=0.1), FadeIn(v_row, lag_ratio=0.1), Write(role_label), run_time=3.0)
        self.wait(1.3)

        self.play(
            FadeOut(tiles),
            FadeOut(q_row),
            FadeOut(k_row),
            FadeOut(v_row),
            FadeOut(role_label),
            run_time=1.0,
        )

        q_cards = VGroup(*[role_card(f"q{i+1}", QUERY_COLOR) for i in range(3)]).arrange(DOWN, buff=0.25)
        k_cards = VGroup(*[role_card(f"k{i+1}", KEY_COLOR) for i in range(4)]).arrange(RIGHT, buff=0.25)
        q_cards.shift(LEFT * 3.8 + DOWN * 0.1)
        k_cards.shift(UP * 1.7 + RIGHT * 0.9)
        heat_values = [
            [0.92, 0.28, 0.10, 0.60],
            [0.18, 0.85, 0.42, 0.22],
            [0.50, 0.12, 0.88, 0.32],
        ]
        cells = VGroup()
        for i, row in enumerate(heat_values):
            for j, value in enumerate(row):
                cell = Square(
                    side_length=0.62,
                    stroke_color=MUTED_COLOR,
                    stroke_width=0.8,
                    fill_color=score_lerp_color(value),
                    fill_opacity=1,
                )
                cell.move_to([j * 0.68 - 0.1, 0.8 - i * 0.68, 0])
                cells.add(cell)
        heatmap_label = MathTex(r"QK^T", color=SCORE_COLOR, font_size=40).next_to(cells, DOWN, buff=0.35)
        scale_label = MathTex(r"\frac{QK^T}{\sqrt{d_k}}", color=SCALE_COLOR, font_size=40).move_to(heatmap_label)
        self.play(FadeIn(q_cards), FadeIn(k_cards), FadeIn(cells, lag_ratio=0.04), Write(heatmap_label), run_time=3.0)
        self.play(Indicate(cells[0], color=SCALE_COLOR), Indicate(cells[5], color=SCALE_COLOR), run_time=1.6)
        self.play(
            TransformMatchingTex(heatmap_label, scale_label),
            *[cell.animate.set_fill(score_lerp_color(value * 0.52), opacity=1) for cell, row in zip(cells, sum(heat_values, [])) for value in [row]],
            run_time=2.0,
        )
        self.wait(1.3)

        self.play(FadeOut(q_cards), FadeOut(k_cards), FadeOut(cells), FadeOut(scale_label), run_time=1.0)

        scores = np.array([3.2, 1.1, 0.4, 2.0])
        weights = np.exp(scores) / np.exp(scores).sum()
        raw_bars = VGroup()
        weight_bars = VGroup()
        for i, (score, weight) in enumerate(zip(scores, weights)):
            x = (i - 1.5) * 1.1
            raw = Rectangle(
                width=0.5,
                height=score / scores.max() * 2.4,
                stroke_color=SCORE_COLOR,
                fill_color=SCORE_COLOR,
                fill_opacity=0.7,
            )
            raw.move_to([x, -0.5 + raw.height / 2, 0])
            weight_bar = Rectangle(
                width=0.5,
                height=weight / weights.max() * 2.4,
                stroke_color=SOFTMAX_COLOR,
                fill_color=SOFTMAX_COLOR,
                fill_opacity=0.7,
            )
            weight_bar.move_to([x, -0.5 + weight_bar.height / 2, 0])
            raw_bars.add(raw)
            weight_bars.add(weight_bar)
        softmax_title = Text("softmax turns scores into weights", color=SOFTMAX_COLOR, font_size=24).to_edge(DOWN, buff=0.55)
        self.play(FadeIn(raw_bars, lag_ratio=0.12), Write(softmax_title), run_time=1.5)
        self.play(Transform(raw_bars, weight_bars), run_time=2.0)
        self.play(Write(MathTex(r"\sum_i w_i = 1", color=SOFTMAX_COLOR, font_size=36).next_to(raw_bars, UP, buff=0.45)), run_time=1.2)
        self.wait(1.3)
        self.play(FadeOut(raw_bars), FadeOut(softmax_title), run_time=1.0)

        streams = VGroup()
        arrows = VGroup()
        merge_point = [1.5, 0, 0]
        for i, weight in enumerate([0.55, 0.20, 0.08, 0.17]):
            y = (1.5 - i) * 0.75
            stream = Rectangle(
                width=0.45,
                height=max(weight * 2.8, 0.15),
                stroke_color=VALUE_COLOR,
                fill_color=VALUE_COLOR,
                fill_opacity=0.6,
            )
            stream.move_to([-3.2, y, 0])
            arrow = Arrow(
                stream.get_right(),
                merge_point,
                color=VALUE_COLOR,
                stroke_width=weight * 12 + 1,
                buff=0.0,
            )
            streams.add(stream)
            arrows.add(arrow)
        context = Rectangle(
            width=0.75,
            height=2.7,
            stroke_color=CONTEXT_COLOR,
            fill_color=CONTEXT_COLOR,
            fill_opacity=0.3,
        ).move_to([2.4, 0, 0])
        context_label = Text("context", color=CONTEXT_COLOR, font_size=22).next_to(context, UP, buff=0.25)
        payoff = Text("Weighted values become context.", color=TEXT_COLOR, font_size=24).to_edge(DOWN, buff=0.55)
        self.play(FadeIn(streams, lag_ratio=0.1), Write(payoff), run_time=1.5)
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.15), run_time=2.0)
        self.play(FadeIn(context), Write(context_label), run_time=1.5)
        self.play(Indicate(formula, color=CONTEXT_COLOR), run_time=1.0)
        self.wait(1.0)


# ============================================================
# s01 – Tokens Ask For Context          (target: 7 s)
# ============================================================
class TokensAskForContext(Scene):
    """
    Beat b01: "A token does not look at a sentence all at once.
    It asks a more local question: which other tokens matter to me right now?"

    Visual:
    1. Sentence tokens appear as tiles in a strip.
    2. One token is highlighted as the active query.
    3. Soft arcs emanate from the active token to its neighbours.
    """

    def construct(self) -> None:
        self.camera.background_color = BG

        words = ["The", "cat", "sat", "on", "mat"]
        tiles = VGroup(*[token_tile(w) for w in words])
        tiles.arrange(RIGHT, buff=0.38)
        tiles.move_to(ORIGIN)

        # 1.5 s — FadeIn all tokens
        self.play(FadeIn(tiles, lag_ratio=0.15), run_time=1.5)

        # 1.2 s — Highlight "cat" (index 1)
        active_idx = 1
        active_tile = tiles[active_idx]
        highlight = RoundedRectangle(
            corner_radius=0.1,
            width=1.55,
            height=0.78,
            stroke_color=QUERY_COLOR,
            stroke_width=3.0,
            fill_color=QUERY_COLOR,
            fill_opacity=0.18,
        )
        highlight.move_to(active_tile)
        self.play(Create(highlight), run_time=1.2)

        # 3.0 s — Draw soft arcs to every other token
        arcs = VGroup()
        for i, tile in enumerate(tiles):
            if i == active_idx:
                continue
            angle = TAU / 9 if i < active_idx else -TAU / 9
            arc = CurvedArrow(
                active_tile.get_center(),
                tile.get_center(),
                angle=angle,
                color=QUERY_COLOR,
                stroke_width=1.8,
                stroke_opacity=0.55,
                tip_length=0.15,
            )
            arcs.add(arc)

        self.play(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.25), run_time=3.0)
        self.wait(1.3)


# ============================================================
# s02 – Q K V Roles                     (target: 10 s)
# ============================================================
class QKVRoles(Scene):
    """
    Beat b02: "For each token, we create three roles: a query that asks,
    keys that can answer, and values that carry the information to mix."

    Visual:
    1. Three source-token tiles appear at top.
    2. TransformFromCopy → Q cards (blue-sky), K cards (green), V cards (pink).
    3. Role labels written alongside each column.
    """

    def construct(self) -> None:
        self.camera.background_color = BG

        source_words = ["bank", "river", "flows"]
        source_row = VGroup(*[token_tile(w) for w in source_words])
        source_row.arrange(RIGHT, buff=0.55)
        source_row.shift(UP * 2.5)

        # 1.0 s — source tiles
        self.play(FadeIn(source_row, lag_ratio=0.2), run_time=1.0)

        # Build Q/K/V card columns below each token
        spacing_y = 0.95
        q_row, k_row, v_row = VGroup(), VGroup(), VGroup()
        for tile in source_row:
            q = role_card("Q", QUERY_COLOR).next_to(tile, DOWN, buff=0.55)
            k = role_card("K", KEY_COLOR).next_to(q, DOWN, buff=spacing_y - 0.58)
            v = role_card("V", VALUE_COLOR).next_to(k, DOWN, buff=spacing_y - 0.58)
            q_row.add(q)
            k_row.add(k)
            v_row.add(v)

        # 2.0 s — Q cards from source copies
        self.play(
            *[
                FadeIn(q_row[i].copy().become(q_row[i]))
                for i in range(len(source_words))
            ],
            run_time=0.1,  # placeholder pre-add
        )
        # Use TransformFromCopy for visual flair
        self.remove(*self.mobjects[1:])  # clear placeholder
        self.play(
            LaggedStart(
                *[
                    FadeIn(q_row[i])
                    for i in range(len(source_words))
                ],
                lag_ratio=0.3,
            ),
            run_time=2.0,
        )

        # 2.0 s — K cards
        self.play(
            LaggedStart(
                *[FadeIn(k_row[i]) for i in range(len(source_words))],
                lag_ratio=0.3,
            ),
            run_time=2.0,
        )

        # 2.0 s — V cards
        self.play(
            LaggedStart(
                *[FadeIn(v_row[i]) for i in range(len(source_words))],
                lag_ratio=0.3,
            ),
            run_time=2.0,
        )

        # 2.0 s — role labels
        q_lbl = Text("Query — asks", color=QUERY_COLOR, font_size=20)
        k_lbl = Text("Key — answers", color=KEY_COLOR, font_size=20)
        v_lbl = Text("Value — carries info", color=VALUE_COLOR, font_size=20)

        q_lbl.next_to(q_row, LEFT, buff=0.5)
        k_lbl.next_to(k_row, LEFT, buff=0.5)
        v_lbl.next_to(v_row, LEFT, buff=0.5)

        self.play(Write(q_lbl), Write(k_lbl), Write(v_lbl), run_time=2.0)
        self.wait(0.9)


# ============================================================
# s03 – Similarity Heatmap              (target: 16 s)
# ============================================================
class SimilarityHeatmap(MovingCameraScene):
    """
    Beats b03–b04: QK^T as a pairwise relevance table; scaling prevents
    scores from becoming too extreme before softmax.

    Visual:
    1. Q and K vector cards + QK^T formula appear.
    2. Comparison dashes from q1 to all k cards.
    3. First heatmap row fills; then full 3×4 grid.
    4. Over-sharp cells indicated.
    5. Formula transforms to QK^T / √d_k; heatmap cools.
    """

    # Simulated raw attention scores (3 queries × 4 keys)
    RAW_SCORES: list[list[float]] = [
        [0.92, 0.28, 0.10, 0.60],
        [0.18, 0.85, 0.42, 0.22],
        [0.50, 0.12, 0.88, 0.32],
    ]
    SCALE_FACTOR: float = 0.52   # multiply scores after sqrt(d_k) division

    def construct(self) -> None:
        self.camera.background_color = BG

        n_q = len(self.RAW_SCORES)
        n_k = len(self.RAW_SCORES[0])
        cell_sz = 0.72

        # ── Formula ─────────────────────────────────────────
        formula_qkt = MathTex(
            "Q",
            "K",
            "^T",
            font_size=46,
            color=SCORE_COLOR,
        )
        formula_qkt.set_color_by_tex("Q", QUERY_COLOR)
        formula_qkt.set_color_by_tex("K", KEY_COLOR)
        formula_qkt.to_edge(UP, buff=0.45)

        # ── Query cards (left column) ────────────────────────
        q_cards = VGroup()
        for i in range(n_q):
            sq = Square(side_length=cell_sz - 0.06,
                        stroke_color=QUERY_COLOR, stroke_width=2.0,
                        fill_color=QUERY_COLOR, fill_opacity=0.22)
            lbl = Text(f"q{i+1}", color=QUERY_COLOR, font_size=18)
            lbl.move_to(sq)
            q_cards.add(VGroup(sq, lbl))
        q_cards.arrange(DOWN, buff=0.18)
        q_cards.shift(LEFT * 4.2 + DOWN * 0.3)

        # ── Key cards (top row) ──────────────────────────────
        k_cards = VGroup()
        for j in range(n_k):
            sq = Square(side_length=cell_sz - 0.06,
                        stroke_color=KEY_COLOR, stroke_width=2.0,
                        fill_color=KEY_COLOR, fill_opacity=0.22)
            lbl = Text(f"k{j+1}", color=KEY_COLOR, font_size=18)
            lbl.move_to(sq)
            k_cards.add(VGroup(sq, lbl))

        grid_x0 = q_cards.get_right()[0] + 0.80
        grid_y_top = q_cards.get_top()[1] + 0.85
        for j, kc in enumerate(k_cards):
            kc.move_to([grid_x0 + j * cell_sz, grid_y_top, 0])

        # ── Heatmap grid (3×4 cells) ─────────────────────────
        cells: list[Square] = []
        for i in range(n_q):
            for j in range(n_k):
                cell = Square(
                    side_length=cell_sz - 0.06,
                    stroke_color=MUTED_COLOR,
                    stroke_width=0.8,
                    fill_color=BG,
                    fill_opacity=1.0,
                )
                cell.move_to([
                    grid_x0 + j * cell_sz,
                    q_cards[i].get_center()[1],
                    0,
                ])
                cells.append(cell)
        heatmap = VGroup(*cells)

        def raw_cell_color(i: int, j: int) -> ManimColor:
            return score_lerp_color(self.RAW_SCORES[i][j])

        def scaled_cell_color(i: int, j: int) -> ManimColor:
            return score_lerp_color(self.RAW_SCORES[i][j] * self.SCALE_FACTOR)

        # ── Step 1 (2 s): formula + Q/K cards ───────────────
        self.play(
            Write(formula_qkt),
            FadeIn(q_cards, lag_ratio=0.2),
            FadeIn(k_cards, lag_ratio=0.2),
            run_time=2.0,
        )

        # ── Step 2 (4 s): comparison dashes + first row ──────
        dashes = VGroup()
        for j in range(n_k):
            dash = DashedLine(
                q_cards[0].get_right(),
                k_cards[j].get_bottom(),
                color=SCORE_COLOR,
                stroke_opacity=0.50,
                stroke_width=1.4,
                dash_length=0.14,
            )
            dashes.add(dash)

        first_row = VGroup(*[cells[j] for j in range(n_k)])
        first_row_anim = [
            cells[j].animate.set_fill(raw_cell_color(0, j), opacity=1.0)
            for j in range(n_k)
        ]

        self.play(LaggedStart(*[Create(d) for d in dashes], lag_ratio=0.2), run_time=2.0)
        self.play(
            FadeIn(first_row),
            AnimationGroup(*first_row_anim),
            run_time=2.0,
        )

        # ── Step 3 (2 s): fill remaining rows ────────────────
        rest = VGroup(*[cells[n_k + idx] for idx in range((n_q - 1) * n_k)])
        rest_anim = [
            cells[i * n_k + j].animate.set_fill(raw_cell_color(i, j), opacity=1.0)
            for i in range(1, n_q) for j in range(n_k)
        ]
        self.play(
            FadeIn(rest, lag_ratio=0.08),
            AnimationGroup(*rest_anim, lag_ratio=0.05),
            run_time=2.0,
        )

        # ── Step 4 (4 s): pulse over-sharp cells + caption ───
        sharp_indices = [(0, 0), (1, 1), (2, 2)]
        sharp_cells = [cells[i * n_k + j] for i, j in sharp_indices]
        caption = Text(
            "High scores can over-sharpen softmax",
            color=MUTED_COLOR, font_size=20,
        ).to_edge(DOWN, buff=0.5)

        self.play(Write(caption), run_time=1.0)
        self.play(
            LaggedStart(
                *[Indicate(c, color=SCALE_COLOR, scale_factor=1.25) for c in sharp_cells],
                lag_ratio=0.3,
            ),
            run_time=3.0,
        )

        # ── Step 5 (4 s): scale formula + cool heatmap ───────
        scale_formula = MathTex(
            r"\frac{",
            "Q",
            "K",
            r"^T}{\sqrt{d_k}}",
            font_size=46,
            color=SCALE_COLOR,
        )
        scale_formula.set_color_by_tex("Q", QUERY_COLOR)
        scale_formula.set_color_by_tex("K", KEY_COLOR)
        scale_formula.to_edge(UP, buff=0.45)

        cool_anim = [
            cells[i * n_k + j].animate.set_fill(scaled_cell_color(i, j), opacity=1.0)
            for i in range(n_q) for j in range(n_k)
        ]
        self.play(
            TransformMatchingTex(formula_qkt, scale_formula),
            AnimationGroup(*cool_anim, lag_ratio=0.04),
            FadeOut(caption),
            run_time=4.0,
        )


# ============================================================
# s04 – Softmax To Weights              (target: 10 s)
# ============================================================
class SoftmaxToWeights(Scene):
    """
    Beat b05: "Softmax turns those scores into attention weights: not just
    who is relevant, but how much each token contributes."

    Visual:
    1. Raw score bars appear.
    2. Bars transform into normalised attention-weight bars.
    3. Sum label Σ w_i = 1 appears.
    """

    RAW_SCORES = [3.2, 1.1, 0.4, 2.0]

    def construct(self) -> None:
        self.camera.background_color = BG

        scores = np.array(self.RAW_SCORES, dtype=float)
        weights = np.exp(scores) / np.exp(scores).sum()
        labels = [f"k{i+1}" for i in range(len(scores))]
        bar_width = 0.72
        x_spacing = 1.35
        max_raw_h = 2.6
        max_wt_h = 2.6

        def make_bar(h: float, color: ManimColor, val: float,
                     lbl: str, fmt: str) -> VGroup:
            bar = Rectangle(
                width=bar_width, height=max(h, 0.04),
                stroke_color=color, stroke_width=1.5,
                fill_color=color, fill_opacity=0.70,
            )
            val_lbl = Text(fmt.format(val), color=color, font_size=20)
            bot_lbl = Text(lbl, color=TEXT_COLOR, font_size=18)
            return VGroup(bar, val_lbl, bot_lbl)

        # Raw bars
        raw_bars = VGroup()
        for i, (sc, lb) in enumerate(zip(scores, labels)):
            h = sc / scores.max() * max_raw_h
            grp = make_bar(h, SCORE_COLOR, sc, lb, "{:.1f}")
            cx = (i - (len(scores) - 1) / 2) * x_spacing
            grp[0].move_to([cx, -0.6 + h / 2, 0])
            grp[1].next_to(grp[0], UP, buff=0.12)
            grp[2].next_to(grp[0], DOWN, buff=0.15)
            raw_bars.add(grp)

        raw_title = Text("Raw relevance scores", color=MUTED_COLOR, font_size=24)
        raw_title.to_edge(UP, buff=0.6)

        # 2.0 s — raw bars appear
        self.play(FadeIn(raw_bars, lag_ratio=0.18), Write(raw_title), run_time=2.0)

        # Weight bars (built at same x positions)
        wt_bars = VGroup()
        for i, (w, lb) in enumerate(zip(weights, labels)):
            h = w * max_wt_h / weights.max()
            grp = make_bar(h, SOFTMAX_COLOR, w, lb, "{:.2f}")
            cx = (i - (len(weights) - 1) / 2) * x_spacing
            grp[0].move_to([cx, -0.6 + h / 2, 0])
            grp[1].next_to(grp[0], UP, buff=0.12)
            grp[2].next_to(grp[0], DOWN, buff=0.15)
            wt_bars.add(grp)

        wt_title = Text("Attention weights (softmax)", color=SOFTMAX_COLOR, font_size=24)
        wt_title.to_edge(UP, buff=0.6)

        # 4.0 s — transform bars
        self.play(
            Transform(raw_bars, wt_bars),
            Transform(raw_title, wt_title),
            run_time=4.0,
        )

        # 2.0 s — sum label
        sum_label = MathTex(r"\sum_i\, w_i = 1", font_size=42, color=SOFTMAX_COLOR)
        sum_label.to_edge(DOWN, buff=0.8)
        self.play(Write(sum_label), run_time=2.0)
        self.wait(2.0)


# ============================================================
# s05 – Weighted Values Become Context  (target: 13 s)
# ============================================================
class WeightedValuesBecomeContext(MovingCameraScene):
    """
    Beat b06: "Finally, the weights mix the value vectors. The output is the
    same token, now carrying context from the tokens it attended to."

    Visual:
    1. Value vector streams appear (height ∝ weight).
    2. Weighted arrows flow right from each stream.
    3. Context vector emerges at the merge point.
    4. Full attention formula assembles at the bottom.
    """

    WEIGHTS = [0.55, 0.20, 0.08, 0.17]

    def construct(self) -> None:
        self.camera.background_color = BG

        weights = self.WEIGHTS
        n = len(weights)
        y_positions = [(i - (n - 1) / 2) * 1.2 for i in range(n)]

        # ── Value stream bars (left side) ────────────────────
        value_group = VGroup()
        for i, (w, y) in enumerate(zip(weights, y_positions)):
            bar_h = max(w * 3.8, 0.15)
            bar = Rectangle(
                width=0.65, height=bar_h,
                stroke_color=VALUE_COLOR, stroke_width=1.5,
                fill_color=VALUE_COLOR, fill_opacity=0.60,
            )
            bar.move_to([-4.2, y, 0])
            bar.align_to([-4.2, y - bar_h / 2, 0], DOWN)

            w_lbl = Text(f"w={w:.2f}", color=SOFTMAX_COLOR, font_size=17)
            w_lbl.next_to(bar, LEFT, buff=0.22)
            v_lbl = Text(f"v{i+1}", color=VALUE_COLOR, font_size=17)
            v_lbl.next_to(bar, RIGHT, buff=0.22)
            value_group.add(VGroup(bar, w_lbl, v_lbl))

        # 2.0 s — value streams appear
        self.play(FadeIn(value_group, lag_ratio=0.18), run_time=2.0)

        # ── Weighted arrows toward merge point ────────────────
        merge_x = 1.2
        arrows = VGroup()
        for i, (w, y) in enumerate(zip(weights, y_positions)):
            bar = value_group[i][0]
            arrow = Arrow(
                bar.get_right(),
                [merge_x, y, 0],
                color=VALUE_COLOR,
                stroke_opacity=min(w * 1.5 + 0.2, 1.0),
                stroke_width=w * 14 + 1.0,
                max_tip_length_to_length_ratio=0.18,
                buff=0.0,
            )
            arrows.add(arrow)

        # 4.0 s — weighted arrows flow in
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.2), run_time=4.0)

        # ── Context vector emerges ────────────────────────────
        ctx_rect = Rectangle(
            width=0.95, height=3.2,
            stroke_color=CONTEXT_COLOR, stroke_width=2.5,
            fill_color=CONTEXT_COLOR, fill_opacity=0.32,
        )
        ctx_rect.move_to([merge_x + 0.9, 0, 0])
        ctx_lbl = Text("context", color=CONTEXT_COLOR, font_size=22)
        ctx_lbl.next_to(ctx_rect, UP, buff=0.22)

        # 4.0 s — context vector builds up
        self.play(FadeIn(ctx_rect), Write(ctx_lbl), run_time=4.0)

        # ── Full attention formula ────────────────────────────
        full_formula = MathTex(
            r"\mathrm{Attention}(Q,K,V)"
            r"=\mathrm{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V",
            font_size=32,
            color=TEXT_COLOR,
        )
        full_formula.to_edge(DOWN, buff=0.5)

        # 3.0 s — formula writes out
        self.play(Write(full_formula), run_time=3.0)
