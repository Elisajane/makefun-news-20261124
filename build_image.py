#!/usr/bin/env python3
"""Build entry.png for make.fun bounty news-image-20261124.

Renders a clean newspaper-style summary of world news for Tuesday,
24 November 2026, as a single 1024x1024 PNG. All text is drawn with
PIL using DejaVu fonts, so the output is deterministic: same input,
same pixels, no network, no randomness.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Wrap text to fit max_width pixels, returning a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    ("INDONESIA  •  DISASTER", "Factory fire in Indonesia",
     "A major fire at an industrial facility leaves several workers "
     "missing as rescue teams search the site."),
    ("UKRAINE  •  WAR", "Fresh Russian strikes hit Kyiv",
     "Ukraine reports new drone and missile strikes in the Kyiv region; "
     "rescue workers assess the damage."),
    ("IRAN  •  U.S.  •  TENSIONS", "Iran warns over U.S. naval blockade",
     "Tehran warns of countermeasures as tensions rise over a U.S. "
     "naval blockade."),
    ("GULF OF FINLAND  •  SEA", "Russian cargo ship catches fire",
     "A Russian cargo vessel catches fire after a drone incident; "
     "all 16 crew are evacuated safely."),
    ("SOUTH KOREA  •  SECURITY", "Seoul scrambles jets after Russian breach",
     "South Korea issues an air-raid alert and mobilises fighter jets "
     "after a Russian air-zone violation."),
    ("BANGLADESH  •  HEALTH", "50 million children in typhoid drive",
     "Bangladesh begins a month-long campaign to vaccinate 50 million "
     "children against drug-resistant typhoid."),
]

NAVY = (15, 42, 68)
GOLD = (255, 196, 0)
WHITE = (255, 255, 255)
INK = (20, 24, 28)
MUTED = (80, 88, 96)
CARD = (242, 244, 247)
ACCENTS = [(198, 40, 40), (21, 101, 192), (123, 31, 162),
           (0, 121, 107), (230, 124, 0), (46, 125, 50)]


def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # --- Header ---
    d.rectangle([0, 0, W, 178], fill=NAVY)
    d.rectangle([0, 178, W, 184], fill=GOLD)
    title_f = font(SERIF_BOLD, 62)
    d.text((48, 26), "WORLD NEWS", font=title_f, fill=WHITE)
    date_f = font(SANS_BOLD, 30)
    d.text((48, 106), "TUESDAY, 24 NOVEMBER 2026", font=date_f, fill=GOLD)
    sub_f = font(SANS, 22)
    d.text((48, 148), "Six stories that defined the day — in one image",
           font=sub_f, fill=(205, 216, 228))

    # --- Story cards: 2 columns x 3 rows ---
    margin, gap = 32, 20
    card_w = (W - 2 * margin - gap) // 2
    card_h = 246
    top = 208
    tag_f = font(SANS_BOLD, 17)
    head_f = font(SANS_BOLD, 26)
    body_f = font(SANS, 20)

    for i, (tag, headline, body) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = margin + col * (card_w + gap)
        y = top + row * (card_h + gap)
        d.rounded_rectangle([x, y, x + card_w, y + card_h],
                            radius=14, fill=CARD)
        d.rectangle([x, y + 14, x + 8, y + card_h - 14],
                    fill=ACCENTS[i])
        tx = x + 28
        d.text((tx, y + 20), tag, font=tag_f, fill=ACCENTS[i])
        lines = wrap(d, headline, head_f, card_w - 56)
        ly = y + 52
        for line in lines[:2]:
            d.text((tx, ly), line, font=head_f, fill=INK)
            ly += 34
        blines = wrap(d, body, body_f, card_w - 56)
        by = ly + 8
        for line in blines[:3]:
            d.text((tx, by), line, font=body_f, fill=MUTED)
            by += 27

    # --- Footer ---
    foot_f = font(SANS, 18)
    d.text((48, 984),
           "Reports first published 24 November 2026  •  @elisajane / make.fun",
           font=foot_f, fill=MUTED)

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} {W}x{H}")


if __name__ == "__main__":
    main()
