# A faster copy of sim.py (numpy). Same rules as the Arduboy code; used to tune it.
import random, sys, os
import numpy as np
from data import Q, OBJ, matrix
from pack import GROUPS, PRIMARY
M = np.array(matrix(), dtype=np.int16); N, NQ = M.shape
E = lambda k, d: int(os.environ.get(k, d))
K, MG, EA, WB, CS, MG2 = E('K', 48), E('MG', 20), E('EA', 10), E('WB', 12), E('CS', 5), E('MG2', 10); XT = E('XT', 3)
D = {'Y': np.array([int(x) for x in os.environ.get('DV', '-4,0,0,3,4').split(',')]), 'U': np.array([int(x) for x in os.environ.get('DU', '-2,-2,2,-2,-2').split(',')]), 'S': np.array([int(x) for x in os.environ.get('DS', '-5,0,3,0,-5').split(',')])}
D['N'] = D['Y'][::-1].copy()
SP = np.array([max(0, min(4, (18 - int((M[i] >= 3).sum())) // 3)) for i in range(N)])
INGRP = {c: np.array([c in GROUPS[i] for i in range(N)]) for c in 'AVMO'}
LOW = set(('green','red','yellow','orange','brown','black','white','colorful','cute','old','everyday','gift'))
QW = np.array([5 if k in LOW else 8 for k, _ in Q])
Y3, N1, S2 = (M >= 3), (M <= 1), (M == 2)
def pick(score, asked, rnd):
    top = np.argsort(-score, kind='stable')[:K]
    if XT: w = np.maximum(1, (64 * np.power(2.0, (score[top] - score[top[0]]) / XT)).astype(np.int64))   # (a leader's say halves for every XT points it trails the best: as in the Arduboy code)
    else: w = np.maximum(1, WB + score[top] - score[top[0]])
    y = w @ Y3[top]; n = w @ N1[top]; s = w @ S2[top]; tot = y + n + s
    g = (tot * tot - y * y - n * n - s * s) * QW // 8; g[asked] = -1
    o = np.argsort(-g, kind='stable')[:3]; c = [q for q in o if g[q] >= g[o[0]] * 9 // 10 and g[q] >= 0]
    return int(rnd.choice(c))
def answer(v, rnd, noise):
    if rnd.random() < noise: return rnd.choice('YN')
    if v == 4: return 'Y'
    if v == 0: return 'N'
    if v == 3: return 'Y' if rnd.random() < 0.7 else rnd.choice('SN')
    if v == 1: return 'N' if rnd.random() < 0.7 else rnd.choice('SY')
    return rnd.choice('SSSUYN')
def game(target, rnd, noise, log=None):
    cat = PRIMARY[target]
    if cat != 'A' or rnd.random() < 0.25: cat = rnd.choice(sorted(GROUPS[target]))   # (a mug is an OBJECT and MAN-MADE: either box is right)      # (people don't agree on the box)
    if rnd.random() < noise: cat = rnd.choice('AVMO')
    score = np.where(INGRP[cat], CS, -CS) - 2 * SP; asked = np.zeros(NQ, dtype=bool); qn = 1
    while qn < 25:
        o = np.argsort(-score, kind='stable')[:2]; a, b = int(o[0]), int(o[1]); m = score[a] - score[b]
        guess = (qn == 20) or (qn >= EA and m >= MG) or (qn > 21 and m >= MG2) or qn == 24
        qn += 1
        if guess:
            if a == target: return qn
            if log is not None: log.append(OBJ[a][0])
            score[a] = -30000; continue
        q = pick(score, asked, rnd); asked[q] = True
        score = score + D[answer(int(M[target, q]), rnd, noise)][M[:, q]]
    return None
if __name__ == '__main__':
    rnd = random.Random(E('SEED', 1)); noise = float(sys.argv[1]) if len(sys.argv) > 1 else 0.15; R = E('R', 2)
    res = []; fails = {}
    for t in range(N):
        for r in range(R):
            log = []; g = game(t, rnd, noise, log); res.append(g)
            if g is None: fails.setdefault(OBJ[t][0], []).extend(log)
    w20 = sum(1 for g in res if g and g <= 21); w25 = sum(1 for g in res if g)
    print('K%d MG%d EA%d WB%d CS%d: by 21: %.1f%%  by 25: %.1f%%  avg q %.1f' % (K, MG, EA, WB, CS, 100 * w20 / len(res), 100 * w25 / len(res), sum(g for g in res if g) / max(1, w25)))
    if os.environ.get('SHOW'):
        for n, l in sorted(fails.items(), key=lambda x: -len(x[1]))[:E('SHOW', 40)]: print(' ', n, '<-', l[:6])

