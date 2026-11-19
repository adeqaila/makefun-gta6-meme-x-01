#!/usr/bin/env python3
"""Compose grind variants for gta6-meme-x-01: background + make.fun ghost + captions.

Same deterministic pipeline as ../entry/compose.py (PIL, fixed layout, no
timestamps), plus an optional GTA-style 5-star wanted overlay (top-right)
for the wanted-level variant. Backgrounds may be WebP or PNG.
"""
import math
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SIZE = 1200
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def fit_font(draw, lines, max_width, start_size):
    size = start_size
    while size > 20:
        font = ImageFont.truetype(FONT_PATH, size)
        if all(draw.textlength(line, font=font) <= max_width for line in lines):
            return font
        size -= 4
    return ImageFont.truetype(FONT_PATH, size)


def draw_caption(draw, lines, y_top, max_width, start_size=110):
    font = fit_font(draw, lines, max_width, start_size)
    y = y_top
    for line in lines:
        w = draw.textlength(line, font=font)
        x = (SIZE - w) / 2
        draw.text((x, y), line, font=font, fill="white",
                  stroke_width=max(4, font.size // 14), stroke_fill="black")
        y += font.size + 8
    return y


def shade_band(img, y0, y1, alpha=150):
    band = Image.new("RGBA", (SIZE, y1 - y0), (0, 0, 0, alpha))
    img.alpha_composite(band, (0, y0))


def star_points(cx, cy, r_outer, r_inner, rotation=-90):
    pts = []
    for i in range(10):
        r = r_outer if i % 2 == 0 else r_inner
        a = math.radians(rotation + i * 36)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def draw_wanted_stars(img, y_top):
    """Five gold GTA-style wanted stars, top-right, just below the top band."""
    draw = ImageDraw.Draw(img)
    r = 34
    gap = 12
    total_w = 5 * 2 * r + 4 * gap
    x0 = SIZE - total_w - 40
    y = y_top
    for i in range(5):
        cx = x0 + i * (2 * r + gap) + r
        draw.polygon(star_points(cx, y + r, r, r * 0.42),
                     fill=(255, 215, 0, 255), outline=(0, 0, 0, 255), width=4)


def main(bg_path, ghost_path, top_text, bottom_text, out_path,
         ghost_size=430, wanted=False):
    bg = Image.open(bg_path).convert("RGBA")
    w, h = bg.size
    side = min(w, h)
    bg = bg.crop(((w - side) // 2, (h - side) // 2,
                  (w - side) // 2 + side, (h - side) // 2 + side))
    bg = bg.resize((SIZE, SIZE), Image.LANCZOS)

    draw = ImageDraw.Draw(bg)
    top_lines = top_text.split("\n")
    bottom_lines = bottom_text.split("\n")

    tmp = ImageDraw.Draw(Image.new("RGBA", (SIZE, SIZE)))
    top_font = fit_font(tmp, top_lines, SIZE - 80, 110)
    top_h = len(top_lines) * (top_font.size + 8)
    bot_font = fit_font(tmp, bottom_lines, SIZE - 80, 100)
    bot_h = len(bottom_lines) * (bot_font.size + 8)

    shade_band(bg, 0, top_h + 70)
    shade_band(bg, SIZE - bot_h - 70, SIZE)

    draw = ImageDraw.Draw(bg)
    draw_caption(draw, top_lines, 35, SIZE - 80, 110)
    if wanted:
        draw_wanted_stars(bg, top_h + 90)

    ghost = Image.open(ghost_path).convert("RGBA")
    ghost = ghost.resize((ghost_size, ghost_size), Image.LANCZOS)
    gx = (SIZE - ghost_size) // 2
    gy = (SIZE - ghost_size) // 2 + 40
    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse([gx + 60, gy + ghost_size - 30, gx + ghost_size - 60,
                gy + ghost_size + 30], fill=(0, 0, 0, 110))
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    bg.alpha_composite(shadow)
    bg.alpha_composite(ghost, (gx, gy))

    draw = ImageDraw.Draw(bg)
    draw_caption(draw, bottom_lines, SIZE - bot_h - 35, SIZE - 80, 100)

    bg.convert("RGB").save(out_path, "PNG")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    # argv: bg ghost top bottom out [--wanted]
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5],
         wanted="--wanted" in sys.argv[6:])
