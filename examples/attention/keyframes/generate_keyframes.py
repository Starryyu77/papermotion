from __future__ import annotations

from math import sin
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parent
W, H = 854, 480
BG = (16, 18, 23)
QUERY = (125, 211, 252)
KEY = (167, 243, 208)
VALUE = (249, 168, 212)
SCORE = (251, 191, 36)
CONTEXT = (55, 214, 122)


def glow_layer() -> Image.Image:
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def save_frame(name: str, layer: Image.Image) -> None:
    base = Image.new("RGB", (W, H), BG)
    base.paste(layer, (0, 0), layer)
    base.save(ROOT / name)


def draw_token_spotlight() -> None:
    layer = glow_layer()
    glow = glow_layer()
    gd = ImageDraw.Draw(glow)
    gd.ellipse((155, 86, 545, 386), fill=(*QUERY, 38))
    glow = glow.filter(ImageFilter.GaussianBlur(28))
    layer.alpha_composite(glow)

    d = ImageDraw.Draw(layer)
    x0, y = 172, 214
    active = 1
    for i in range(5):
        x = x0 + i * 98
        fill = (*QUERY, 70) if i == active else (230, 235, 245, 26)
        outline = QUERY if i == active else (229, 231, 235)
        d.rounded_rectangle((x, y, x + 72, y + 42), radius=8, fill=fill, outline=outline, width=2)

    active_center = (x0 + active * 98 + 36, y + 21)
    for i in [0, 2, 3, 4]:
        target = (x0 + i * 98 + 36, y + 21)
        d.line((active_center, target), fill=(*QUERY, 110), width=3)

    save_frame("s01_attention_spotlight.png", layer)


def draw_heatmap_cooling() -> None:
    layer = glow_layer()
    glow = glow_layer()
    gd = ImageDraw.Draw(glow)
    gd.rounded_rectangle((225, 106, 620, 358), radius=22, fill=(*SCORE, 24))
    glow = glow.filter(ImageFilter.GaussianBlur(20))
    layer.alpha_composite(glow)

    d = ImageDraw.Draw(layer)
    rows, cols = 3, 4
    cell, gap = 52, 8
    left = (W - cols * cell - (cols - 1) * gap) // 2
    top = 154
    values = [
        [0.72, 0.34, 0.18, 0.50],
        [0.22, 0.64, 0.42, 0.28],
        [0.48, 0.20, 0.70, 0.36],
    ]
    for r in range(rows):
        for c in range(cols):
            v = values[r][c]
            color = (
                int(34 + SCORE[0] * v * 0.75),
                int(41 + SCORE[1] * v * 0.55),
                int(52 + SCORE[2] * v * 0.25),
                220,
            )
            x = left + c * (cell + gap)
            y = top + r * (cell + gap)
            d.rounded_rectangle((x, y, x + cell, y + cell), radius=5, fill=color, outline=(90, 96, 112, 130), width=1)

    for i in range(10):
        y = 122 + i * 20
        alpha = 80 - i * 5
        d.arc((170 + i * 8, y, 680 - i * 8, y + 110), start=200, end=340, fill=(*QUERY, alpha), width=2)

    save_frame("s03_heatmap_cooling.png", layer)


def draw_value_streams() -> None:
    layer = glow_layer()
    glow = glow_layer()
    gd = ImageDraw.Draw(glow)
    gd.ellipse((410, 108, 720, 370), fill=(*CONTEXT, 32))
    glow = glow.filter(ImageFilter.GaussianBlur(24))
    layer.alpha_composite(glow)

    d = ImageDraw.Draw(layer)
    origins = [(140, 150), (140, 210), (140, 270), (140, 330)]
    widths = [12, 7, 4, 6]
    for idx, ((x, y), width) in enumerate(zip(origins, widths)):
        points = []
        for step in range(45):
            t = step / 44
            px = x + 470 * t
            py = y * (1 - t) + 240 * t + sin(t * 3.14 + idx) * 18 * (1 - t)
            points.append((px, py))
        d.line(points, fill=(*VALUE, 150), width=width)
        d.ellipse((x - 10, y - 10, x + 10, y + 10), fill=(*VALUE, 130))

    d.rounded_rectangle((605, 170, 654, 310), radius=12, fill=(*CONTEXT, 95), outline=CONTEXT, width=2)
    save_frame("s05_value_streams.png", layer)


if __name__ == "__main__":
    draw_token_spotlight()
    draw_heatmap_cooling()
    draw_value_streams()
