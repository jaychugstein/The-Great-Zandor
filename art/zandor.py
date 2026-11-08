# The fortune teller's picture (1-bit, 48 x 64): a turbaned seer with hollow glowing eyes, hands spread over a crystal ball.
# Drawn big with bold shapes, then shrunk, so it reads at Arduboy size. Writes zandor.png (+ zandor_check.png to look at).
from PIL import Image, ImageDraw
W, H, S = 48, 64, 6
def P(*pts): return [(x * S, y * S) for x, y in pts]
def portrait(glow=True):
    im = Image.new('L', (W * S, H * S), 0); d = ImageDraw.Draw(im)
    cx = 24
    # robe: dark, with a bright collar edge
    d.polygon(P((cx - 10, 38), (cx - 23, 50), (cx - 23, 64), (cx + 23, 64), (cx + 23, 50), (cx + 10, 38)), fill=0, outline=255, width=2 * S // 2)
    # face: pale, long, tapering down into a pointed beard
    d.polygon(P((cx - 11, 18), (cx + 11, 18), (cx + 11, 30), (cx + 7, 38), (cx + 2, 46), (cx, 48), (cx - 2, 46), (cx - 7, 38), (cx - 11, 30)), fill=255)
    # turban: big dome, wrap folds, jewel
    d.ellipse(P((cx - 17, 0), (cx + 17, 24)), fill=255); d.rectangle(P((cx - 17, 12), (cx + 17, 20)), fill=255)
    for y in (9, 15):
        d.arc(P((cx - 20, y - 5), (cx + 20, y + 8)), 205, 335, fill=0, width=S)
    d.polygon(P((cx, 7), (cx - 4, 12), (cx, 17), (cx + 4, 12)), fill=0); d.ellipse(P((cx - 1.5, 10.5), (cx + 1.5, 13.5)), fill=255)
    d.line(P((cx - 17, 21), (cx + 17, 21)), fill=0, width=S)  # turban's lower edge
    # eyes: hollow black sockets under sharp brows, small bright pupils
    d.line(P((cx - 10, 22), (cx - 3, 25)), fill=0, width=2 * S); d.line(P((cx + 10, 22), (cx + 3, 25)), fill=0, width=2 * S)
    for ex in (cx - 6, cx + 6):
        d.ellipse(P((ex - 3.5, 25), (ex + 3.5, 30)), fill=0)
        if glow: d.ellipse(P((ex - 1, 26.5), (ex + 1, 28.5)), fill=255)
    # nose shadow, moustache curling up, thin mouth, beard split
    d.line(P((cx + 1, 28), (cx + 1, 33)), fill=0, width=S)
    d.line(P((cx - 7, 36), (cx, 34.5), (cx + 7, 36)), fill=0, width=2 * S, joint='curve')
    d.line(P((cx - 7, 36), (cx - 9, 33)), fill=0, width=S); d.line(P((cx + 7, 36), (cx + 9, 33)), fill=0, width=S)
    d.line(P((cx, 39), (cx, 46)), fill=0, width=S)
    # crystal ball, glowing, on a little stand
    d.ellipse(P((cx - 11, 44), (cx + 11, 63)), fill=0, outline=255, width=2 * S)
    d.arc(P((cx - 7, 47), (cx + 3, 57)), 190, 280, fill=255, width=S)
    d.ellipse(P((cx + 3, 55), (cx + 5, 57)), fill=255)
    # hands: long pale fingers spread on each side of the ball
    for sd in (-1, 1):
        for f in range(4):
            y = 47 + f * 3.2
            d.line(P((cx + sd * 20, y + 3), (cx + sd * 11.5, y)), fill=255, width=int(1.6 * S))
        d.polygon(P((cx + sd * 23, 47), (cx + sd * 18, 47), (cx + sd * 18, 60), (cx + sd * 23, 62)), fill=255)
    small = im.resize((W, H), Image.BOX).point(lambda v: 255 if v >= 128 else 0).convert('1')
    return small
p = portrait(); p.save('zandor.png')
big = Image.new('L', (W * 2 + 8, H), 40); big.paste(p.convert('L'), (0, 0)); big.paste(portrait(False).convert('L'), (W + 8, 0))
big.resize(((W * 2 + 8) * 5, H * 5), Image.NEAREST).save('zandor_check.png')
