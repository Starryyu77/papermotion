"""
PaperMotion research-video demo renders.

These scenes turn three validated dynamic scene models into single-file
deterministic rough-pass videos:

    manim -ql research_video_demos.py AdamOptimizerDemo
    manim -ql research_video_demos.py DDPMDenoisingDemo
    manim -ql research_video_demos.py NeRFVolumeRenderingDemo

The videos are intentionally self-contained. They are not final narrated films,
but they are complete exact-layer explainer passes that can be posted, reviewed,
and replaced by higher-fidelity renderer implementations later.
"""

from __future__ import annotations

import math
from typing import Iterable

import numpy as np
from manim import (
    BOLD,
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UL,
    UP,
    Arrow,
    Brace,
    Circle,
    Create,
    DashedLine,
    Dot,
    Ellipse,
    FadeIn,
    FadeOut,
    GrowArrow,
    Indicate,
    LaggedStart,
    Line,
    MathTex,
    ManimColor,
    Polygon,
    Rectangle,
    ReplacementTransform,
    RoundedRectangle,
    Scene,
    Square,
    Text,
    Transform,
    VGroup,
    VMobject,
    Write,
)

BG = ManimColor("#101217")
PANEL = ManimColor("#171B22")
TEXT = ManimColor("#E5E7EB")
MUTED = ManimColor("#7A8494")
GRID = ManimColor("#2B3442")
YELLOW = ManimColor("#FBBF24")
RED = ManimColor("#F87171")
BLUE = ManimColor("#60A5FA")
CYAN = ManimColor("#7DD3FC")
GREEN = ManimColor("#37D67A")
PURPLE = ManimColor("#C4B5FD")
PINK = ManimColor("#F9A8D4")
ORANGE = ManimColor("#FB923C")
TEAL = ManimColor("#5EEAD4")


def title_block(title: str, subtitle: str) -> VGroup:
    header = Text(title, color=TEXT, font_size=34, weight=BOLD)
    sub = Text(subtitle, color=MUTED, font_size=20)
    sub.next_to(header, DOWN, buff=0.18)
    return VGroup(header, sub)


def panel(width: float, height: float, label: str | None = None) -> VGroup:
    box = RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.1,
        stroke_color=GRID,
        stroke_width=1.4,
        fill_color=PANEL,
        fill_opacity=0.92,
    )
    if not label:
        return VGroup(box)
    tag = Text(label, color=MUTED, font_size=18)
    tag.move_to(box.get_top() + DOWN * 0.22)
    return VGroup(box, tag)


def formula_card(tex: str, color: ManimColor = TEXT, font_size: int = 30) -> VGroup:
    body = MathTex(tex, color=color, font_size=font_size)
    pad = RoundedRectangle(
        width=body.width + 0.45,
        height=body.height + 0.32,
        corner_radius=0.08,
        stroke_color=color,
        stroke_width=1.2,
        fill_color=color,
        fill_opacity=0.08,
    )
    pad.move_to(body)
    return VGroup(pad, body)


def label(text: str, color: ManimColor = TEXT, size: int = 20) -> Text:
    return Text(text, color=color, font_size=size)


def vector_arrow(start: np.ndarray, end: np.ndarray, color: ManimColor, name: str) -> VGroup:
    arrow = Arrow(start, end, buff=0, color=color, stroke_width=6, tip_length=0.18)
    tag = Text(name, color=color, font_size=20, weight=BOLD)
    tag.next_to(arrow.get_end(), UP, buff=0.08)
    return VGroup(arrow, tag)


def timeline(labels: Iterable[str], width: float, color: ManimColor = MUTED) -> VGroup:
    labels = list(labels)
    line = Line(LEFT * width / 2, RIGHT * width / 2, color=color, stroke_width=2)
    group = VGroup(line)
    for i, name in enumerate(labels):
        x = -width / 2 + i * width / (len(labels) - 1)
        tick = Line([x, -0.08, 0], [x, 0.08, 0], color=color, stroke_width=2)
        dot = Dot([x, 0, 0], radius=0.055, color=color)
        txt = Text(name, color=color, font_size=16)
        txt.next_to(dot, DOWN, buff=0.12)
        group.add(tick, dot, txt)
    return group


def curved_signal(points: list[np.ndarray], color: ManimColor, stroke_width: float = 4) -> VMobject:
    curve = VMobject(stroke_color=color, stroke_width=stroke_width)
    curve.set_points_smoothly(points)
    return curve


def particle_cloud(
    center: np.ndarray,
    spread: float,
    count: int,
    color: ManimColor,
    seed: int,
    radius: float = 0.035,
) -> VGroup:
    rng = np.random.default_rng(seed)
    group = VGroup()
    for _ in range(count):
        offset = rng.normal(0, spread, size=2)
        dot = Dot(center + np.array([offset[0], offset[1], 0]), radius=radius, color=color)
        dot.set_opacity(0.72)
        group.add(dot)
    return group


class AdamOptimizerDemo(Scene):
    """Complete rough-pass video for examples/adam-optimizer."""

    def construct(self) -> None:
        self.camera.background_color = BG

        header = title_block(
            "Adam Optimizer",
            "noisy gradients -> moments -> adaptive parameter step",
        )
        formula = formula_card(
            r"\theta_t=\theta_{t-1}-\alpha\,\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}",
            GREEN,
            31,
        )
        formula.next_to(header, DOWN, buff=0.45)
        self.play(Write(header), FadeIn(formula), run_time=2.2)
        self.wait(0.5)
        self.play(FadeOut(header), formula.animate.scale(0.78).to_edge(UP, buff=0.35), run_time=1.0)

        surface = self._loss_slice()
        surface.shift(LEFT * 2.8 + DOWN * 0.15)
        state_panel = panel(3.5, 4.7, "optimizer state").shift(RIGHT * 3.15 + DOWN * 0.05)
        theta = Dot(surface[1].get_center() + np.array([0.0, 0.0, 0]), radius=0.09, color=YELLOW)
        theta_label = MathTex(r"\theta_t", color=YELLOW, font_size=28).next_to(theta, UP, buff=0.08)
        raw_arrows = VGroup(
            vector_arrow(theta.get_center(), theta.get_center() + np.array([-0.9, 0.55, 0]), RED, r"g_t^{(1)}"),
            vector_arrow(theta.get_center(), theta.get_center() + np.array([-0.55, 0.85, 0]), RED, r"g_t^{(2)}"),
            vector_arrow(theta.get_center(), theta.get_center() + np.array([-1.05, 0.25, 0]), RED, r"g_t^{(3)}"),
        )
        raw_arrows[1].shift(RIGHT * 0.06)
        beat = Text("1. Sample a noisy stochastic gradient.", color=TEXT, font_size=23)
        beat.next_to(state_panel, UP, buff=0.18)
        self.play(FadeIn(surface), FadeIn(state_panel), FadeIn(theta), Write(theta_label), Write(beat), run_time=2.0)
        self.play(LaggedStart(*[GrowArrow(a[0]) for a in raw_arrows], lag_ratio=0.2), FadeIn(raw_arrows[0][1]), FadeIn(raw_arrows[1][1]), FadeIn(raw_arrows[2][1]), run_time=2.3)
        self.wait(0.6)

        first_formula = formula_card(r"m_t=\beta_1m_{t-1}+(1-\beta_1)g_t", BLUE, 25)
        first_formula.move_to(state_panel[0].get_center() + UP * 1.15)
        smooth_arrow = vector_arrow(theta.get_center(), theta.get_center() + np.array([-0.78, 0.55, 0]), BLUE, r"m_t")
        memory_curve = curved_signal(
            [
                state_panel[0].get_center() + np.array([-1.2, -0.3, 0]),
                state_panel[0].get_center() + np.array([-0.5, 0.15, 0]),
                state_panel[0].get_center() + np.array([0.25, 0.35, 0]),
                state_panel[0].get_center() + np.array([1.1, 0.45, 0]),
            ],
            BLUE,
            5,
        )
        memory_label = Text("first moment keeps direction stable", color=BLUE, font_size=18)
        memory_label.next_to(memory_curve, DOWN, buff=0.18)
        self.play(Transform(beat, Text("2. The first moment smooths direction.", color=TEXT, font_size=23).move_to(beat)), run_time=0.5)
        self.play(FadeIn(first_formula), Transform(raw_arrows.copy(), smooth_arrow), Create(memory_curve), Write(memory_label), run_time=2.5)
        self.play(GrowArrow(smooth_arrow[0]), FadeIn(smooth_arrow[1]), run_time=1.0)
        self.wait(0.6)

        second_formula = formula_card(r"v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2", PURPLE, 25)
        second_formula.move_to(state_panel[0].get_center() + DOWN * 0.72)
        scale_field = VGroup()
        for i, scale in enumerate([0.62, 0.94, 1.28]):
            halo = Ellipse(
                width=1.35 * scale,
                height=0.42 * scale,
                stroke_color=PURPLE,
                stroke_width=2,
                fill_color=PURPLE,
                fill_opacity=0.04,
            )
            halo.rotate(0.35)
            halo.move_to(theta.get_center() + np.array([0.12 * i, -0.05 * i, 0]))
            scale_field.add(halo)
        scale_note = Text("second moment is squared-gradient scale, not curvature", color=PURPLE, font_size=18)
        scale_note.next_to(second_formula, DOWN, buff=0.16)
        self.play(Transform(beat, Text("3. The second moment estimates coordinate scale.", color=TEXT, font_size=23).move_to(beat)), run_time=0.5)
        self.play(FadeIn(second_formula), LaggedStart(*[Create(h) for h in scale_field], lag_ratio=0.18), Write(scale_note), run_time=2.4)
        self.wait(0.6)

        update_arrow = vector_arrow(theta.get_center(), theta.get_center() + np.array([-0.48, 0.37, 0]), GREEN, r"\Delta\theta")
        route_1 = Arrow(first_formula.get_left() + LEFT * 0.1, second_formula.get_left() + LEFT * 0.1, color=BLUE, stroke_width=3, buff=0.05, tip_length=0.12)
        route_2 = Arrow(second_formula.get_left() + LEFT * 0.1, update_arrow[0].get_start(), color=GREEN, stroke_width=3, buff=0.05, tip_length=0.12)
        theta_next = Dot(update_arrow[0].get_end(), radius=0.09, color=GREEN)
        theta_next_label = MathTex(r"\theta_{t+1}", color=GREEN, font_size=28).next_to(theta_next, LEFT, buff=0.08)
        self.play(Transform(beat, Text("4. Divide by scale, then move the parameters.", color=TEXT, font_size=23).move_to(beat)), run_time=0.5)
        self.play(Create(route_1), Create(route_2), GrowArrow(update_arrow[0]), FadeIn(update_arrow[1]), run_time=2.2)
        self.play(Transform(theta, theta_next), Transform(theta_label, theta_next_label), run_time=1.0)
        self.wait(0.7)

        summary = VGroup(
            Text("Adam's update is not just momentum.", color=TEXT, font_size=27, weight=BOLD),
            Text("It combines a smoothed direction with a squared-gradient scale.", color=MUTED, font_size=22),
        ).arrange(DOWN, buff=0.2)
        summary.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(summary), Indicate(update_arrow[0], color=GREEN), run_time=2.2)
        self.wait(3.2)

    def _loss_slice(self) -> VGroup:
        base = panel(5.2, 4.55, "2D teaching loss slice")
        contours = VGroup()
        for i, color in enumerate([GRID, BLUE, CYAN, GREEN]):
            ell = Ellipse(
                width=4.3 - i * 0.76,
                height=2.7 - i * 0.48,
                stroke_color=color,
                stroke_width=1.4,
                fill_opacity=0,
            )
            ell.rotate(0.45)
            ell.shift(DOWN * 0.08)
            contours.add(ell)
        minimum = Dot(RIGHT * 0.35 + DOWN * 0.35, radius=0.06, color=GREEN)
        minimum_label = Text("low loss", color=GREEN, font_size=16).next_to(minimum, DOWN, buff=0.1)
        axes = VGroup(
            Arrow(LEFT * 2.35 + DOWN * 1.75, RIGHT * 2.2 + DOWN * 1.75, buff=0, color=MUTED, stroke_width=2, tip_length=0.12),
            Arrow(LEFT * 2.35 + DOWN * 1.75, LEFT * 2.35 + UP * 1.65, buff=0, color=MUTED, stroke_width=2, tip_length=0.12),
            Text(r"theta_1", color=MUTED, font_size=15).move_to(RIGHT * 2.3 + DOWN * 1.52),
            Text(r"theta_2", color=MUTED, font_size=15).move_to(LEFT * 2.05 + UP * 1.72),
        )
        group = VGroup(base, contours, minimum, minimum_label, axes)
        return group


class DDPMDenoisingDemo(Scene):
    """Complete rough-pass video for examples/ddpm-denoising."""

    def construct(self) -> None:
        self.camera.background_color = BG

        header = title_block(
            "DDPM Denoising",
            "fixed forward corruption, learned iterative reverse steps",
        )
        formula = formula_card(
            r"q(x_t\mid x_0)=\mathcal N(\sqrt{\bar\alpha_t}x_0,\,(1-\bar\alpha_t)I)",
            CYAN,
            30,
        )
        formula.next_to(header, DOWN, buff=0.45)
        self.play(Write(header), FadeIn(formula), run_time=2.2)
        self.wait(0.5)
        self.play(FadeOut(header), formula.animate.scale(0.76).to_edge(UP, buff=0.35), run_time=1.0)

        time = timeline(["t=0", "t=100", "t=400", "t=700", "t=T"], 6.8, MUTED).shift(DOWN * 2.35)
        clean = self._sample_tile("x0", GREEN, 0.15)
        clean.shift(LEFT * 4.3 + DOWN * 0.1)
        beta_label = formula_card(r"\beta_t\ \mathrm{is\ fixed}", YELLOW, 25).shift(UP * 1.75 + RIGHT * 2.75)
        beat = Text("1. Start from structured data.", color=TEXT, font_size=23).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(time), FadeIn(clean), Write(beat), run_time=1.8)
        self.wait(0.4)

        clouds = VGroup(
            self._sample_tile("x100", TEAL, 0.45).shift(LEFT * 2.15 + DOWN * 0.1),
            self._sample_tile("x400", BLUE, 0.9).shift(ORIGIN + DOWN * 0.1),
            self._sample_tile("x700", PURPLE, 1.25).shift(RIGHT * 2.15 + DOWN * 0.1),
            particle_cloud(RIGHT * 4.3 + DOWN * 0.1, 0.72, 52, MUTED, 55, radius=0.035),
        )
        xT_label = MathTex(r"x_T", color=MUTED, font_size=28).next_to(clouds[-1], UP, buff=0.18)
        forward_arrows = VGroup(
            *[
                Arrow(
                    np.array([-3.65 + i * 2.15, -0.1, 0]),
                    np.array([-2.82 + i * 2.15, -0.1, 0]),
                    color=YELLOW,
                    stroke_width=3,
                    tip_length=0.13,
                    buff=0.1,
                )
                for i in range(4)
            ]
        )
        self.play(Transform(beat, Text("2. The forward process adds scheduled Gaussian noise.", color=TEXT, font_size=23).move_to(beat)), FadeIn(beta_label), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(c) for c in clouds], lag_ratio=0.25), LaggedStart(*[GrowArrow(a) for a in forward_arrows], lag_ratio=0.2), FadeIn(xT_label), run_time=3.3)
        self.wait(0.6)

        curve_panel = panel(4.0, 2.35, "closed-form sample").shift(LEFT * 2.75 + UP * 0.8)
        alpha_curve = curved_signal(
            [
                curve_panel[0].get_left() + np.array([0.45, -0.55, 0]),
                curve_panel[0].get_center() + np.array([-0.5, 0.1, 0]),
                curve_panel[0].get_center() + np.array([0.4, 0.45, 0]),
                curve_panel[0].get_right() + np.array([-0.45, 0.55, 0]),
            ],
            CYAN,
            4,
        )
        slider = Dot(alpha_curve.point_from_proportion(0.66), radius=0.07, color=CYAN)
        alpha_formula = formula_card(r"x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon", CYAN, 24)
        alpha_formula.next_to(curve_panel, DOWN, buff=0.18)
        self.play(Transform(beat, Text("3. A closed form jumps directly to any timestep.", color=TEXT, font_size=23).move_to(beat)), run_time=0.5)
        self.play(FadeIn(curve_panel), Create(alpha_curve), FadeIn(slider), FadeIn(alpha_formula), run_time=2.5)
        self.play(slider.animate.move_to(alpha_curve.point_from_proportion(0.92)), Indicate(clouds[2], color=CYAN), run_time=1.4)
        self.wait(0.5)

        denoiser = self._denoiser_module().shift(RIGHT * 2.9 + UP * 0.9)
        reverse_formula = formula_card(r"p_\theta(x_{t-1}\mid x_t)", PURPLE, 26).next_to(denoiser, DOWN, buff=0.2)
        reverse_arrows = VGroup(
            *[
                Arrow(
                    np.array([3.75 - i * 1.2, 1.12 - i * 0.2, 0]),
                    np.array([3.05 - i * 1.2, 0.98 - i * 0.2, 0]),
                    color=PURPLE,
                    stroke_width=3,
                    buff=0.08,
                    tip_length=0.13,
                )
                for i in range(4)
            ]
        )
        denoise_states = VGroup(
            particle_cloud(RIGHT * 3.7 + UP * 1.15, 0.52, 36, PURPLE, 91, radius=0.032),
            self._sample_tile("x600", BLUE, 0.95).scale(0.6).shift(RIGHT * 2.5 + UP * 0.95),
            self._sample_tile("x300", TEAL, 0.55).scale(0.6).shift(RIGHT * 1.3 + UP * 0.75),
            self._sample_tile("x0", GREEN, 0.12).scale(0.6).shift(RIGHT * 0.1 + UP * 0.55),
        )
        self.play(Transform(beat, Text("4. The reverse process is learned and iterative.", color=TEXT, font_size=23).move_to(beat)), FadeIn(denoiser), FadeIn(reverse_formula), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(s) for s in denoise_states], lag_ratio=0.22), LaggedStart(*[GrowArrow(a) for a in reverse_arrows], lag_ratio=0.18), run_time=3.0)
        self.wait(0.6)

        summary = VGroup(
            Text("Forward noising is fixed.", color=YELLOW, font_size=27, weight=BOLD),
            Text("Generation is many learned reverse denoising steps.", color=TEXT, font_size=24),
        ).arrange(DOWN, buff=0.18)
        summary.to_edge(DOWN, buff=0.34)
        self.play(FadeOut(beat), FadeIn(summary), Indicate(denoiser, color=PURPLE), run_time=2.2)
        self.wait(3.4)

    def _sample_tile(self, name: str, color: ManimColor, noise: float) -> VGroup:
        card = RoundedRectangle(
            width=1.25,
            height=1.25,
            corner_radius=0.12,
            stroke_color=color,
            stroke_width=1.6,
            fill_color=color,
            fill_opacity=0.07,
        )
        structure = VGroup(
            Circle(radius=0.28, stroke_color=color, stroke_width=3),
            Line(LEFT * 0.28, RIGHT * 0.28, color=color, stroke_width=3).rotate(0.7),
            Line(LEFT * 0.25, RIGHT * 0.25, color=color, stroke_width=3).rotate(-0.7),
        )
        structure.move_to(card)
        structure.set_opacity(max(0.15, 1.0 - noise))
        dots = particle_cloud(card.get_center(), 0.14 + noise * 0.18, 18, MUTED if noise > 0.8 else color, int(noise * 1000 + 7), radius=0.018 + noise * 0.006)
        dots.set_opacity(min(0.9, 0.2 + noise * 0.8))
        if name.startswith("x") and len(name) > 1:
            tex_name = rf"x_{{{name[1:]}}}"
        else:
            tex_name = name
        tag = MathTex(tex_name, color=color, font_size=22)
        tag.next_to(card, UP, buff=0.12)
        return VGroup(card, structure, dots, tag)

    def _denoiser_module(self) -> VGroup:
        box = RoundedRectangle(
            width=2.05,
            height=1.05,
            corner_radius=0.12,
            stroke_color=PURPLE,
            stroke_width=1.8,
            fill_color=PURPLE,
            fill_opacity=0.1,
        )
        txt = MathTex(r"\epsilon_\theta(x_t,t)", color=PURPLE, font_size=28).move_to(box)
        learned = Text("learned denoiser", color=MUTED, font_size=17).next_to(box, UP, buff=0.12)
        return VGroup(box, txt, learned)


class NeRFVolumeRenderingDemo(Scene):
    """Complete rough-pass video for examples/nerf-volume-rendering."""

    def construct(self) -> None:
        self.camera.background_color = BG

        header = title_block(
            "NeRF Volume Rendering",
            "ray samples -> neural field queries -> transmittance-weighted pixel",
        )
        formula = formula_card(r"C(r)=\int T(t)\,\sigma(r(t))\,c(r(t),d)\,dt", ORANGE, 31)
        formula.next_to(header, DOWN, buff=0.45)
        self.play(Write(header), FadeIn(formula), run_time=2.2)
        self.wait(0.5)
        self.play(FadeOut(header), formula.animate.scale(0.78).to_edge(UP, buff=0.35), run_time=1.0)

        camera = self._camera_icon().shift(LEFT * 4.45 + DOWN * 0.15)
        volume = self._volume_box().shift(LEFT * 0.7 + DOWN * 0.15)
        pixel = Square(side_length=0.58, stroke_color=YELLOW, fill_color=YELLOW, fill_opacity=0.18)
        pixel.move_to(camera.get_center() + RIGHT * 0.52 + UP * 0.1)
        ray = Arrow(pixel.get_center(), RIGHT * 2.85 + UP * 0.55, buff=0, color=YELLOW, stroke_width=5, tip_length=0.18)
        ray_label = MathTex(r"r(t)", color=YELLOW, font_size=28).next_to(ray, UP, buff=0.12)
        direction = Arrow(pixel.get_center() + DOWN * 0.55, pixel.get_center() + RIGHT * 0.75 + DOWN * 0.35, buff=0, color=CYAN, stroke_width=3, tip_length=0.13)
        d_label = MathTex(r"d", color=CYAN, font_size=25).next_to(direction, DOWN, buff=0.05)
        beat = Text("1. One camera pixel casts one ordered ray.", color=TEXT, font_size=23).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(camera), FadeIn(volume), FadeIn(pixel), Write(beat), run_time=1.9)
        self.play(GrowArrow(ray), FadeIn(ray_label), GrowArrow(direction), FadeIn(d_label), run_time=2.1)
        self.wait(0.5)

        sample_points = VGroup()
        sample_labels = VGroup()
        color_chips = [TEAL, GREEN, YELLOW, ORANGE, PINK]
        for i, prop in enumerate([0.23, 0.38, 0.52, 0.66, 0.81]):
            point = ray.get_start() + (ray.get_end() - ray.get_start()) * prop
            dot = Dot(point, radius=0.075, color=BLUE)
            sample_points.add(dot)
            sample_labels.add(MathTex(rf"x_{i+1}", color=BLUE, font_size=20).next_to(dot, DOWN, buff=0.09))
        brace = Brace(Line(sample_points[0].get_center(), sample_points[-1].get_center()), direction=DOWN, color=MUTED)
        brace_text = Text("near to far sample order", color=MUTED, font_size=17).next_to(brace, DOWN, buff=0.08)
        self.play(Transform(beat, Text("2. The ray is sampled from near to far.", color=TEXT, font_size=23).move_to(beat)), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(p) for p in sample_points], lag_ratio=0.18), LaggedStart(*[FadeIn(t) for t in sample_labels], lag_ratio=0.18), FadeIn(brace), Write(brace_text), run_time=2.6)
        self.wait(0.5)

        field = self._field_module().shift(RIGHT * 3.65 + UP * 0.75)
        queries = VGroup()
        outputs = VGroup()
        for i, point in enumerate(sample_points):
            q = DashedLine(point.get_center(), field.get_left() + DOWN * 0.22 + UP * (0.12 * (i - 2)), color=BLUE, stroke_width=2)
            queries.add(q)
            chip = RoundedRectangle(
                width=0.62,
                height=0.36,
                corner_radius=0.06,
                stroke_color=color_chips[i],
                fill_color=color_chips[i],
                fill_opacity=0.25 + 0.11 * i,
            )
            chip.move_to(field.get_right() + RIGHT * 0.52 + DOWN * 0.55 + UP * (0.27 * i))
            outputs.add(chip)
        output_label = MathTex(r"(\sigma_i,c_i)", color=PURPLE, font_size=24).next_to(outputs, RIGHT, buff=0.12)
        field_formula = formula_card(r"F_\Theta(x,d)\rightarrow(\sigma,c)", PURPLE, 25)
        field_formula.next_to(field, DOWN, buff=0.2)
        self.play(Transform(beat, Text("3. A continuous field is queried at each sample.", color=TEXT, font_size=23).move_to(beat)), FadeIn(field), FadeIn(field_formula), run_time=1.0)
        self.play(LaggedStart(*[Create(q) for q in queries], lag_ratio=0.12), LaggedStart(*[FadeIn(o) for o in outputs], lag_ratio=0.14), FadeIn(output_label), run_time=3.0)
        self.wait(0.5)

        transmittance = VGroup()
        widths = [0.22, 0.18, 0.13, 0.09, 0.05]
        opacities = [0.95, 0.72, 0.48, 0.28, 0.14]
        for i in range(4):
            seg = Line(sample_points[i].get_center(), sample_points[i + 1].get_center(), color=GREEN, stroke_width=12 * widths[i] / widths[0])
            seg.set_opacity(opacities[i])
            transmittance.add(seg)
        t_label = MathTex(r"T(t)\ \mathrm{fades\ with\ accumulated\ density}", color=GREEN, font_size=23)
        t_label.shift(LEFT * 0.35 + DOWN * 1.6)
        contribution_arrows = VGroup()
        rendered_pixel = Square(side_length=0.8, stroke_color=GREEN, fill_color=GREEN, fill_opacity=0.2)
        rendered_pixel.shift(RIGHT * 4.85 + DOWN * 1.45)
        rendered_label = MathTex(r"C(r)", color=GREEN, font_size=28).next_to(rendered_pixel, DOWN, buff=0.12)
        for i, chip in enumerate(outputs):
            arr = Arrow(chip.get_center(), rendered_pixel.get_center() + UP * (0.18 - i * 0.09), buff=0.08, color=color_chips[i], stroke_width=2.4, tip_length=0.11)
            arr.set_opacity(opacities[min(i, len(opacities) - 1)])
            contribution_arrows.add(arr)
        self.play(Transform(beat, Text("4. Density and visibility weight each color contribution.", color=TEXT, font_size=23).move_to(beat)), run_time=0.5)
        self.play(LaggedStart(*[Create(seg) for seg in transmittance], lag_ratio=0.12), Write(t_label), FadeIn(rendered_pixel), FadeIn(rendered_label), run_time=2.3)
        self.play(LaggedStart(*[GrowArrow(a) for a in contribution_arrows], lag_ratio=0.12), run_time=2.2)
        self.wait(0.6)

        sweep_rays = VGroup()
        for y in [-0.45, -0.15, 0.15, 0.45]:
            sweep = Arrow(camera.get_center() + RIGHT * 0.55 + UP * y, RIGHT * 2.7 + UP * (y + 0.4), buff=0, color=YELLOW, stroke_width=2, tip_length=0.1)
            sweep.set_opacity(0.35)
            sweep_rays.add(sweep)
        summary = VGroup(
            Text("One ray explains one pixel.", color=TEXT, font_size=27, weight=BOLD),
            Text("A whole image repeats this field query over many camera rays.", color=MUTED, font_size=22),
        ).arrange(DOWN, buff=0.2)
        summary.to_edge(DOWN, buff=0.32)
        self.play(FadeOut(beat), LaggedStart(*[GrowArrow(r) for r in sweep_rays], lag_ratio=0.12), FadeIn(summary), run_time=2.4)
        self.wait(3.2)

    def _camera_icon(self) -> VGroup:
        body = Polygon(
            LEFT * 0.6 + DOWN * 0.55,
            LEFT * 0.6 + UP * 0.55,
            RIGHT * 0.45 + UP * 0.35,
            RIGHT * 0.45 + DOWN * 0.35,
            color=CYAN,
            stroke_width=2,
            fill_color=CYAN,
            fill_opacity=0.08,
        )
        lens = Circle(radius=0.16, stroke_color=CYAN, fill_color=CYAN, fill_opacity=0.18)
        lens.move_to(body.get_center() + RIGHT * 0.12)
        tag = Text("camera", color=MUTED, font_size=17).next_to(body, DOWN, buff=0.14)
        return VGroup(body, lens, tag)

    def _volume_box(self) -> VGroup:
        front = Rectangle(width=3.5, height=2.55, stroke_color=GRID, fill_color=PANEL, fill_opacity=0.35)
        back = Rectangle(width=3.5, height=2.55, stroke_color=GRID, fill_opacity=0)
        back.shift(RIGHT * 0.42 + UP * 0.32)
        connectors = VGroup(
            Line(front.get_corner(UL), back.get_corner(UL), color=GRID),
            Line(front.get_corner(UL) + RIGHT * front.width, back.get_corner(UL) + RIGHT * back.width, color=GRID),
            Line(front.get_corner(UL) + DOWN * front.height, back.get_corner(UL) + DOWN * back.height, color=GRID),
            Line(front.get_corner(UL) + RIGHT * front.width + DOWN * front.height, back.get_corner(UL) + RIGHT * back.width + DOWN * back.height, color=GRID),
        )
        tag = Text("continuous 3D field", color=MUTED, font_size=18).next_to(front, UP, buff=0.15)
        wisps = VGroup()
        for i, color in enumerate([TEAL, GREEN, ORANGE, PINK]):
            blob = Circle(radius=0.18 + i * 0.04, stroke_color=color, fill_color=color, fill_opacity=0.1)
            blob.move_to(front.get_center() + np.array([-1.1 + i * 0.72, 0.45 * math.sin(i), 0]))
            wisps.add(blob)
        return VGroup(front, back, connectors, wisps, tag)

    def _field_module(self) -> VGroup:
        box = RoundedRectangle(
            width=2.1,
            height=1.2,
            corner_radius=0.12,
            stroke_color=PURPLE,
            stroke_width=1.8,
            fill_color=PURPLE,
            fill_opacity=0.1,
        )
        txt = MathTex(r"F_\Theta", color=PURPLE, font_size=36).move_to(box)
        note = Text("continuous function", color=MUTED, font_size=17).next_to(box, UP, buff=0.12)
        return VGroup(box, txt, note)
