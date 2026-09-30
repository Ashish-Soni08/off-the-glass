"""Overlay a compact city banner flush to the bottom-left corner of a court image.

The court artwork is Hy Image output; this script only adds the title banner,
because a script places it at the same size and position on every image.

Usage:
    python add_city_banner.py court.png "MOHALI" "INDIA · STAGE 1" out.jpg
"""
import sys

from PIL import Image, ImageDraw, ImageFont

NAVY = (14, 22, 48, 235)
TEAL = (0, 214, 200, 255)
# Windows font paths; swap for any heavy / bold sans on your system.
TITLE = ImageFont.truetype("C:/Windows/Fonts/seguibl.ttf", 78)
SUB = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)
PAD_X, PAD_TOP, GAP, PAD_BOTTOM, SLANT, EDGE = 44, 22, 4, 26, 48, 6


def add_banner(src, title, sub, out):
    im = Image.open(src).convert("RGBA")
    W, H = im.size
    measure = ImageDraw.Draw(im)
    tb = measure.textbbox((0, 0), title, font=TITLE)
    sb = measure.textbbox((0, 0), sub, font=SUB)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    sw, sh = sb[2] - sb[0], sb[3] - sb[1]
    bw = PAD_X + max(tw, sw) + PAD_X + SLANT
    bh = PAD_TOP + th + GAP + sh + PAD_BOTTOM
    top = H - bh

    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # Teal edge: the same slanted shape, EDGE px larger on the top and the slanted side.
    d.polygon([(0, top - EDGE), (bw + EDGE, top - EDGE), (bw + EDGE - SLANT, H), (0, H)], fill=TEAL)
    d.polygon([(0, top), (bw, top), (bw - SLANT, H), (0, H)], fill=NAVY)
    d.text((PAD_X, top + PAD_TOP - tb[1]), title, font=TITLE, fill=(255, 255, 255, 255))
    d.text((PAD_X + 2, top + PAD_TOP + th + GAP - sb[1] + 6), sub, font=SUB, fill=TEAL)
    Image.alpha_composite(im, layer).convert("RGB").save(out, quality=92)


if __name__ == "__main__":
    add_banner(*sys.argv[1:5])
