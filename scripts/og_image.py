#!/usr/bin/env python3
"""
OG 이미지(1200x630) 생성기 — pikaworks blog
브랜드 컬러 타이틀 카드 자동 생성. 한/영/일 모두 Noto Sans CJK로 렌더링.

사용:
  python3 scripts/og_image.py --title "글 제목" --out assets/og/slug-ko.png [--category 경제]
"""
import argparse
import re
from PIL import Image, ImageDraw, ImageFont

# 이모지·기호 제거(폰트 미지원으로 두부 방지)
EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF"
    "\U00002190-\U000021FF\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F\U00002B50]",
    flags=re.UNICODE,
)


def clean(s):
    s = EMOJI_RE.sub("", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip(" -–—·")

BG = (28, 28, 30)        # #1c1c1e
GRAD_TO = (62, 62, 70)   # 밝은 차콜 (대각선 그라디언트 끝색, 블랙 톤)
BRAND = (101, 38, 217)   # #6526d9
WHITE = (255, 255, 255)
MUTED = (185, 183, 200)
W, H = 1200, 630
MARGIN = 90


def diagonal_bg(w, h, c1, c2, scale=12):
    """좌상단 c1 → 우하단 c2 대각선 그라디언트."""
    sw, sh = max(2, w // scale), max(2, h // scale)
    mask = Image.new("L", (sw, sh))
    px = mask.load()
    for y in range(sh):
        for x in range(sw):
            px[x, y] = int(255 * ((x / (sw - 1) + y / (sh - 1)) / 2))
    mask = mask.resize((w, h), Image.BILINEAR)
    base = Image.new("RGB", (w, h), c1)
    top = Image.new("RGB", (w, h), c2)
    base.paste(top, (0, 0), mask)
    return base

FONT_CANDIDATES_BOLD = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]
FONT_CANDIDATES_REG = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
]


def load_font(size, bold=True):
    paths = FONT_CANDIDATES_BOLD if bold else FONT_CANDIDATES_REG
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


def wrap(draw, text, font, max_w):
    """문자 단위 줄바꿈(CJK 대응) + 공백 우선."""
    lines, cur = [], ""
    for ch in text:
        test = cur + ch
        if draw.textlength(test, font=font) <= max_w or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = ch
        if ch == "\n":
            lines.append(cur.rstrip("\n"))
            cur = ""
    if cur:
        lines.append(cur)
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--category", default="")
    ap.add_argument("--site", default="blog.pikaworks.kr")
    args = ap.parse_args()

    img = diagonal_bg(W, H, BG, GRAD_TO)
    d = ImageDraw.Draw(img)

    # 상단 브랜드 바
    d.rectangle([0, 0, W, 12], fill=BRAND)

    y = MARGIN
    # 카테고리 칩
    if args.category:
        cfont = load_font(30, bold=True)
        ctext = args.category
        tw = d.textlength(ctext, font=cfont)
        pad = 22
        d.rounded_rectangle([MARGIN, y, MARGIN + tw + pad * 2, y + 54],
                            radius=27, fill=BRAND)
        d.text((MARGIN + pad, y + 8), ctext, font=cfont, fill=WHITE)
        y += 92

    # 제목 (길이에 따라 폰트 크기 자동 조절)
    title = clean(args.title)
    max_w = W - MARGIN * 2
    size = 70
    while size >= 44:
        tfont = load_font(size, bold=True)
        lines = wrap(d, title, tfont, max_w)
        line_h = int(size * 1.32)
        if len(lines) * line_h <= (H - y - 130):
            break
        size -= 6
    for ln in lines[:6]:
        d.text((MARGIN, y), ln, font=tfont, fill=WHITE)
        y += line_h

    # 하단: 브랜드 점 + 사이트명
    sfont = load_font(34, bold=True)
    dot_r = 11
    by = H - MARGIN + 6
    d.ellipse([MARGIN, by, MARGIN + dot_r * 2, by + dot_r * 2], fill=BRAND)
    d.text((MARGIN + dot_r * 2 + 16, by - 8), args.site, font=sfont, fill=MUTED)

    import os
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    img.save(args.out, "PNG")
    print("saved:", args.out)


if __name__ == "__main__":
    main()
