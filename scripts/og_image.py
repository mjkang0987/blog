#!/usr/bin/env python3
"""
OG 이미지(1200x630) 생성기 — pikaworks blog
브랜드 컬러 타이틀 카드 자동 생성. 한/영/일 모두 Noto Sans CJK로 렌더링.

사용:
  python3 scripts/og_image.py --title "글 제목" --out assets/og/slug-ko.png [--category 경제] [--theme dark|yellow]
"""
import argparse
import re
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
MARGIN = 90

# 테마 팔레트
THEMES = {
    # 블랙 톤 그라디언트 + 브랜드 보라 포인트
    "dark": {
        "bg": (28, 28, 30), "grad": (62, 62, 70),
        "bar": (101, 38, 217), "chip_bg": (101, 38, 217), "chip_fg": (255, 255, 255),
        "title": (255, 255, 255), "site": (185, 183, 200), "dot": (101, 38, 217),
        "bolt": (255, 214, 10),
    },
    # 피카츄 옐로우 ⚡
    "yellow": {
        "bg": (255, 228, 84), "grad": (255, 198, 0),
        "bar": (28, 28, 30), "chip_bg": (28, 28, 30), "chip_fg": (255, 214, 10),
        "title": (24, 24, 26), "site": (90, 78, 20), "dot": (28, 28, 30),
        "bolt": (28, 28, 30),
    },
}

EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF"
    "\U00002190-\U000021FF\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F\U00002B50]",
    flags=re.UNICODE,
)

FONT_BOLD = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]


def clean(s):
    s = EMOJI_RE.sub("", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip(" -–—·")


def load_font(size):
    for p in FONT_BOLD:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


def diagonal_bg(w, h, c1, c2, scale=12):
    sw, sh = max(2, w // scale), max(2, h // scale)
    mask = Image.new("L", (sw, sh))
    px = mask.load()
    for y in range(sh):
        for x in range(sw):
            px[x, y] = int(255 * ((x / (sw - 1) + y / (sh - 1)) / 2))
    mask = mask.resize((w, h), Image.BILINEAR)
    base = Image.new("RGB", (w, h), c1)
    base.paste(Image.new("RGB", (w, h), c2), (0, 0), mask)
    return base


def wrap(draw, text, font, max_w):
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=font) <= max_w or not cur:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def draw_bolt(d, ox, oy, sc, color):
    """64-단위 좌표의 번개(+양옆 지지직 스파크)를 (ox,oy) 기준 sc 배율로 그림."""
    pts = [(37, 7), (17, 35), (29, 35), (26, 57), (48, 28), (35, 28), (40, 7)]
    d.polygon([(ox + px * sc, oy + py * sc) for px, py in pts], fill=color)
    sw = max(2, int(round(2.6 * sc)))
    for seg in [[(12, 20), (16, 24), (13, 25), (17, 30)],
                [(56, 34), (52, 39), (55, 40), (51, 45)]]:
        d.line([(ox + px * sc, oy + py * sc) for px, py in seg],
               fill=color, width=sw, joint="curve")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--category", default="")
    ap.add_argument("--site", default="blog.pikaworks.kr")
    ap.add_argument("--theme", default="dark", choices=list(THEMES.keys()))
    ap.add_argument("--chip-bolt", action="store_true",
                    help="칩(chip) 안 텍스트 앞에 브랜드 번개 마크를 그린다")
    ap.add_argument("--logo", default="",
                    help="상단에 칩 대신 넣을 로고 이미지(PNG) 경로")
    ap.add_argument("--logo-h", type=int, default=78,
                    help="로고 높이(px)")
    args = ap.parse_args()
    c = THEMES[args.theme]

    img = diagonal_bg(W, H, c["bg"], c["grad"])
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 12], fill=c["bar"])

    y = MARGIN
    if args.logo and os.path.exists(args.logo):
        logo = Image.open(args.logo).convert("RGBA")
        lh = args.logo_h
        lw = max(1, int(logo.width * lh / logo.height))
        logo = logo.resize((lw, lh), Image.LANCZOS)
        img.paste(logo, (MARGIN, y), logo)
        y += lh + 40
    elif args.category:
        cfont = load_font(30)
        tw = d.textlength(args.category, font=cfont)
        pad = 22
        bsc = 0.62 if args.chip_bolt else 0          # 칩 안 번개 마크 배율
        bolt_w = int(48 * bsc)                        # 번개가 차지하는 가로폭(약 30px)
        gap = 16 if args.chip_bolt else 0             # 번개와 텍스트 사이 간격
        chip_w = pad + bolt_w + gap + tw + pad
        d.rounded_rectangle([MARGIN, y, MARGIN + chip_w, y + 54], radius=27, fill=c["chip_bg"])
        if args.chip_bolt:
            # 번개 64-그리드 기준 x≈8~56, y≈7~57 → 칩 높이 54 중앙에 배치
            draw_bolt(d, MARGIN + pad - 8 * bsc, y + 8, bsc, c["bolt"])
        d.text((MARGIN + pad + bolt_w + gap, y + 8), args.category, font=cfont, fill=c["chip_fg"])
        y += 92

    title = clean(args.title)
    max_w = W - MARGIN * 2
    size = 70
    while size >= 44:
        tfont = load_font(size)
        lines = wrap(d, title, tfont, max_w)
        line_h = int(size * 1.32)
        if len(lines) * line_h <= (H - y - 130):
            break
        size -= 6
    for ln in lines[:6]:
        d.text((MARGIN, y), ln, font=tfont, fill=c["title"])
        y += line_h

    sfont = load_font(34)
    by = H - MARGIN + 6
    sc = 0.96  # 번개 마크 배율(높이 약 48px)
    draw_bolt(d, MARGIN - 12 * sc, by + 11 - 32 * sc, sc, c["bolt"])
    d.text((MARGIN + int(44 * sc) + 18, by - 8), args.site, font=sfont, fill=c["site"])

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    img.save(args.out, "PNG")
    print("saved:", args.out)


if __name__ == "__main__":
    main()
