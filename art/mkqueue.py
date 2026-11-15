# Builds the training-survey queue: for every thing, the questions Zandor actually asks when you think of it
# (found by playing pretend games), most-asked first. Written as ../../zsurvey/queue.json for the survey page.
import random, json, sys, collections, os
import numpy as np, fastsim as F
from data import Q, OBJ
rnd = random.Random(7); cnt = [collections.Counter() for _ in range(F.N)]
def game(target):
    cat = F.PRIMARY[target]; score = np.where(F.INGRP[cat], F.CS, -F.CS) - 2 * F.SP; asked = np.zeros(F.NQ, dtype=bool)
    for step in range(23):
        q = F.pick(score, asked, rnd); asked[q] = True; cnt[target][q] += 1
        score = score + F.D[F.answer(int(F.M[target, q]), rnd, 0.08)][F.M[:, q]]
for t in range(F.N):
    for r in range(4): game(t)
order = list(range(F.N)); queue = []
for rnd_no in range(10):
    random.Random(rnd_no).shuffle(order)
    for t in order:
        qs = [q for q, _ in cnt[t].most_common()]
        if rnd_no < len(qs): queue.append([t, qs[rnd_no], int(F.M[t, qs[rnd_no]])])
# the newest things (more4.py) go to the front of the line: they have had no answers from real players yet
from more4 import MORE4, HOTEL
_new = set(m[0] for m in MORE4); _hot = set(m[0] for m in HOTEL)
import json as _j, os as _o
_L = _j.load(open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'learned.json')))
_thin = set(o[0] for o in OBJ if len(_L.get(o[0], {})) <= 1)          # (things with no answers yet, or just one: they come next)
queue = ([c for c in queue if OBJ[c[0]][0] in _hot] + [c for c in queue if OBJ[c[0]][0] in _thin - _hot]
         + [c for c in queue if OBJ[c[0]][0] in _new - _hot - _thin] + [c for c in queue if OBJ[c[0]][0] not in _new | _hot | _thin])
from data import DISPLAY, boxy
queue = [c for c in queue if not (Q[c[1]][0] == 'box' and boxy(OBJ[c[0]][0]))]
_BODYQ = ('$pickup', '$heavy', 'pocket', '$hold', '$movable', '$duck', '$microwave', '$light', 'shoebox', '$outdoors', '$indoors', 'rolls', 'float', 'envelope', '$steal')
queue = [c for c in queue if not (Q[c[1]][0] in _BODYQ and F.M[c[0], [k for k, _ in Q].index('body')] >= 3)]   # (no pocket questions about your back)   # (never ask whether a box comes in a box)
# The question of the round (Nov 14): one important question, asked about every thing in a row, made things first.
# Chosen as the question Zandor asks most that has the fewest real answers behind it.
SWEEP = os.environ.get('SWEEP', 'burn')
if SWEEP:
    _qi = [k for k, _ in Q].index(SWEEP)
    _done = set(o[0] for o in OBJ if SWEEP in _L.get(o[0], {}))
    _order = sorted(range(len(OBJ)), key=lambda t: ('MVOA'.index(OBJ[t][1]) if OBJ[t][1] in 'MVOA' else 9, __import__('fixes')._bare(OBJ[t][0])))
    _k = [k for k, _ in Q]; _col = lambda t, k: int(F.M[t, _k.index(k)])
    def _fits(t):                                            # (only things the question makes sense for: never a body part, a place, the sky)
        if _col(t, 'body') >= 3 or _col(t, 'place') >= 3 or _col(t, '$touch') < 3: return False
        if SWEEP in ('inhand', 'parts'): return _col(t, '$made') >= 3 and max(_col(t, 'alive'), _col(t, 'building'), _col(t, 'eat'), _col(t, 'drink'), _col(t, 'wear') if SWEEP == 'inhand' else 0) < 3
        if SWEEP == 'burn': return _col(t, 'alive') < 3 or _col(t, 'plant') >= 3
        if SWEEP == '$household': return _col(t, '$made') >= 3 and _col(t, 'alive') < 3 and _col(t, 'building') < 3
        return True
    _sweep = [[t, _qi, int(F.M[t, _qi])] for t in _order if OBJ[t][0] not in _done and _fits(t)]
    queue = _sweep + [c for c in queue if c[1] != _qi]
if os.environ.get('SHUFFLE', '1') == '1':                    # (completely shuffled: every card in random order)
    random.Random().shuffle(queue)
json.dump({'things': [o[0] for o in OBJ], 'show': [DISPLAY.get(o[0], o[0]) for o in OBJ], 'questions': [['burnL' if k == 'burn' else k, t] for k, t in Q],   # (burnL: answers to the lighter wording, kept apart from old match ones)
           'queue': queue}, open(sys.argv[1], 'w'), separators=(',', ':'))
print(len(queue), 'cards')
