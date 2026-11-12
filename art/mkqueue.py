# Builds the training-survey queue: for every thing, the questions Zandor actually asks when you think of it
# (found by playing pretend games), most-asked first. Written as ../../zsurvey/queue.json for the survey page.
import random, json, sys, collections
import numpy as np, fastsim as F
from data import Q, OBJ
rnd = random.Random(7); cnt = [collections.Counter() for _ in range(F.N)]
def game(target):
    cat = OBJ[target][1].replace('M', 'O'); score = np.where(F.INGRP[cat], F.CS, -F.CS) - 2 * F.SP; asked = np.zeros(F.NQ, dtype=bool)
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
json.dump({'things': [o[0] for o in OBJ], 'questions': [[k, t] for k, t in Q], 'queue': queue}, open(sys.argv[1], 'w'), separators=(',', ':'))
print(len(queue), 'cards')
