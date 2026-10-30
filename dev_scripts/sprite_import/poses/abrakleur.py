#!/usr/bin/env python3
"""Recomposes the Abrakleur artworks into a quadruped posture (head held high, a long back on a
branch, short rear legs) so the sprite reads wider and heavier than the original standing pose.

Pieces are cut out of the Dofus artworks, widened, and reassembled. Writes
<src>/abrakleur_quadrupede.png and <src>/abrakleur_quadrupede_back.png, which overrides.json
points abrakleur at ("source"), then: ../run.sh --src <src> abrakleur && ../run.sh --apply abrakleur

Usage: python3 abrakleur.py [--src ~/Dev/perso/imgToGBASprite/source]
"""
import argparse
import math
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import import_sprites  # noqa: E402

W = 1.25  # limb widening
GROUND = 1250
NECK = 140  # how far above the shoulders the back joins the neck


def piece(src, poly):
    m = Image.new("L", src.size, 0)
    ImageDraw.Draw(m).polygon(poly, fill=255)
    p = src.copy()
    p.putalpha(ImageChops.multiply(src.getchannel("A"), m))
    return p.crop(p.getbbox())


def xf(p, sx=1.0, sy=1.0, rot=0, dark=1.0, flip=False):
    p = p.resize((max(1, round(p.width * sx)), max(1, round(p.height * sy))), Image.LANCZOS)
    if flip:
        p = ImageOps.mirror(p)
    if rot:
        p = p.rotate(rot, Image.BICUBIC, expand=True)
    if dark != 1.0:
        a = p.getchannel("A")
        p = ImageEnhance.Brightness(p.convert("RGB")).enhance(dark).convert("RGBA")
        p.putalpha(a)
    return p


class Canvas:
    def __init__(self):
        self.im = Image.new("RGBA", (1600, 1300), (0, 0, 0, 0))

    def put(self, p, x, y_bottom=None, y_top=None):
        y = y_top if y_top is not None else y_bottom - p.height
        self.im.alpha_composite(p, (round(x), round(y)))

    def save(self, path):
        self.im.crop(self.im.getbbox()).save(path)


def front_pieces(front):
    return {
        "head": piece(front, [(295, 70), (462, 70), (470, 180), (455, 300), (440, 360), (425, 445), (295, 445)]),
        "leg_l": piece(front, [(300, 395), (476, 398), (480, 470), (456, 560), (448, 888), (300, 888)]),
        "leg_m": piece(front, [(445, 440), (566, 440), (561, 560), (546, 600), (546, 948), (445, 948)]),
        "leg_r": piece(front, [(546, 455), (602, 455), (602, 560), (628, 568), (628, 868), (546, 868)]),
        # shoulder knot and the straight branch that becomes the back
        "knot": piece(front, [(445, 255), (470, 212), (510, 202), (560, 212), (572, 250), (565, 300),
                              (510, 308), (470, 322), (445, 300)]),
        "beam": piece(front, [(500, 292), (562, 292), (580, 400), (586, 495), (528, 495), (514, 400)]),
        "sprout1": piece(front, [(478, 140), (565, 140), (560, 212), (530, 222), (510, 212), (478, 180)]),
        "sprout2": piece(front, [(568, 222), (625, 222), (625, 322), (568, 322)]),
    }


def compose_front(f):
    """Head high on the left, back running right."""
    c = Canvas()
    front_near = xf(f["leg_l"], W, 0.86)
    fx, rx = 200, 650
    top = GROUND - front_near.height  # shoulder
    c.put(xf(f["leg_r"], W * 1.3, 0.66, dark=0.72), rx + 85, GROUND - 22)
    c.put(xf(f["leg_m"], W, 0.86, dark=0.78), fx + 150, GROUND - 20)
    # the back starts up at the neck and slopes down to the rear legs
    neck = NECK
    drop = 132 + neck
    rot = 90 - math.degrees(math.atan2(drop, 445))
    c.put(xf(f["beam"], 1.6, math.hypot(drop, 445) / 203, rot=rot), fx + 110, y_top=top - 95 - neck)
    rear_near = xf(f["leg_m"], W * 1.05, 0.68)
    c.put(rear_near, rx, GROUND)
    c.put(xf(f["sprout2"], 1.1, 1.1), rx + 55, y_bottom=GROUND - rear_near.height + 15)
    c.put(front_near, fx, GROUND)
    c.put(xf(f["sprout1"], 1.1, 1.1), fx + 210, y_bottom=top - 90 - neck // 2)
    c.put(xf(f["knot"], 1.15, 1.0), fx + 120, y_top=top - 110)
    head = xf(f["head"], 1.15, 1.0)
    c.put(head, fx + 5, y_top=top - head.height + 55)
    return c


def compose_back(back, f):
    """Mirror of the front layout: head high on the right, back running left. Head and legs come
    from the back artwork, the back branch and knot from the front one."""
    head = xf(piece(back, [(545, 50), (710, 50), (710, 422), (585, 422), (575, 330), (555, 250), (540, 150)]), 1.15)
    leg_near = piece(back, [(548, 375), (710, 375), (710, 975), (555, 975)])
    leg_mid = piece(back, [(438, 395), (556, 395), (560, 600), (552, 975), (470, 975), (470, 640), (438, 600)])
    leg_left = piece(back, [(380, 500), (436, 500), (442, 618), (476, 640), (472, 975), (360, 975), (360, 640),
                            (376, 618)])
    sprout = piece(back, [(365, 70), (530, 70), (520, 160), (470, 200), (440, 280), (365, 280)])

    c = Canvas()
    front_near = xf(leg_near, W, 0.8)
    knot = xf(f["knot"], 1.15, 1.0, flip=True)
    beam = xf(f["beam"], 1.6, 2.1, rot=-72, flip=True)
    fx = 900
    rx = fx - 430
    top = GROUND - front_near.height
    c.put(xf(leg_mid, W * 1.05, 0.62, dark=0.72), rx - 25, GROUND - 22)
    c.put(xf(leg_mid, W, 0.8, dark=0.78), fx - 120, GROUND - 20)
    c.put(beam, fx - beam.width + 60, y_top=top - 95)
    rear_near = xf(leg_left, W * 1.1, 0.72)
    c.put(rear_near, rx, GROUND)
    c.put(xf(sprout, 0.9, 0.9), rx - 20, y_bottom=GROUND - rear_near.height + 30)
    c.put(front_near, fx, GROUND)
    c.put(knot, fx - knot.width + 40, y_top=top - 150)
    c.put(head, fx + 5, y_top=top - head.height + 55)
    return c


def segment_back(path):
    """The back artwork has a plain white background: flood it away, then drop the white enclosed
    between the legs (which the flood can't reach) and pull the alpha in over the white fringe."""
    defaults, monsters = import_sprites.load_overrides()
    back = import_sprites.flood_segment(path, import_sprites.config_for("abrakleur", defaults, monsters))
    white = back.convert("L").point(lambda v: 0 if v > 205 else 255)
    back.putalpha(ImageChops.multiply(back.getchannel("A"), white).filter(ImageFilter.MinFilter(5)))
    return back


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--src", type=Path, default=Path("~/Dev/perso/imgToGBASprite/source"))
    src = p.parse_args().src.expanduser()
    f = front_pieces(Image.open(src / "abrakleur.png").convert("RGBA"))
    compose_front(f).save(src / "abrakleur_quadrupede.png")
    compose_back(segment_back(src / "abrakleur_back.png"), f).save(src / "abrakleur_quadrupede_back.png")
    print(f"écrit {src}/abrakleur_quadrupede.png et abrakleur_quadrupede_back.png")


if __name__ == "__main__":
    main()
