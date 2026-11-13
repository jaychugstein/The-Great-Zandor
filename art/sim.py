# Plays thousands of pretend games against the engine (same rules as the Arduboy code) to tune it.
import random, sys, os
from data import Q, OBJ, matrix
M = matrix(); N = len(OBJ); NQ = len(Q)
CATS = 'AVMO'
DV = os.environ.get('DV','-4,0,0,3,4'); _d=[int(x) for x in DV.split(',')]
_n=[int(x) for x in os.environ.get('DN',','.join(str(v) for v in _d[::-1])).split(',')]
D = {'Y': _d, 'N': _n, 'U': [-2, -2, 2, -2, -2], 'S': [-5, 0, 3, 0, -5]}   # (as in the Arduboy code)
import os
K, MARGIN, EARLY = int(os.environ.get('K',48)), int(os.environ.get('MG',20)), int(os.environ.get('EA',10))
WB = int(os.environ.get('WB',12))
from pack import GROUPS, PRIMARY
SPARSE = [max(0, min(4, (18 - sum(1 for v in M[i] if v >= 3)) // 3)) for i in range(N)]

def pick(score, asked, rnd):
    top = sorted(range(N), key=lambda i: -score[i])[:K]; t = score[top[0]]
    w = {i: max(1, WB + score[i] - t) for i in top}
    best = []
    for q in range(NQ):
        if asked[q]: continue
        y = n = s = 0
        for i in top:
            v = M[i][q]
            if v >= 3: y += w[i]
            elif v <= 1: n += w[i]
            else: s += w[i]
        tot = y + n + s; g = tot * tot - y * y - n * n - s * s
        g = g * (5 if Q[q][0] in ('green','red','yellow','orange','brown','black','white','colorful','cute','old','everyday','gift') else 8) // 8
        best.append((g, q))
    best.sort(reverse=True)
    lim = best[0][0] * 9 // 10
    c = [q for g, q in best[:3] if g >= lim]
    return rnd.choice(c)

def answer(v, rnd, noise):
    if rnd.random() < noise: return rnd.choice('YN')
    if v == 4: return 'Y'
    if v == 0: return 'N'
    if v == 3: return 'Y' if rnd.random() < 0.7 else rnd.choice('SN')
    if v == 1: return 'N' if rnd.random() < 0.7 else rnd.choice('SY')
    return rnd.choice('SSSUYN')

def game(target, rnd, noise=0.05):
    score = [0] * N; asked = [False] * NQ; banned = set()
    cat = PRIMARY[target]
    if cat != 'A' or rnd.random() < 0.25: cat = rnd.choice(sorted(GROUPS[target]))   # (a mug is an OBJECT and MAN-MADE: either box is right)     # (people don't agree on the box)
    if rnd.random() < noise: cat = rnd.choice('AVMO')
    CS = int(os.environ.get('CS', 5))
    for i in range(N): score[i] = (CS if cat in GROUPS[i] else -CS) - 2 * SPARSE[i]
    qn = 1
    while qn < 25:
        order = sorted(range(N), key=lambda i: -score[i]); a, b = order[0], order[1]
        guess = (qn == 20) or (qn >= EARLY and score[a] - score[b] >= MARGIN) or (qn > 21 and score[a] - score[b] >= MARGIN // 2) or qn == 24
        qn += 1
        if guess:
            if a == target: return qn
            score[a] -= 1000; continue
        q = pick(score, asked, rnd); asked[q] = True
        ans = answer(M[target][q], rnd, noise)
        for i in range(N): score[i] += D[ans][M[i][q]]
    return None

if __name__ == '__main__':
    rnd = random.Random(1); noise = float(sys.argv[1]) if len(sys.argv) > 1 else 0.05
    res = []; fails = []
    for t in range(N):
        for r in range(int(os.environ.get('R',4))):
            g = game(t, rnd, noise); res.append(g)
            if g is None: fails.append(OBJ[t][0])
    w20 = sum(1 for g in res if g and g <= 21); w25 = sum(1 for g in res if g)
    print('noise %.2f: won by 21: %.0f%%, by 25: %.0f%%, avg question %.1f' % (noise, 100 * w20 / len(res), 100 * w25 / len(res), sum(g for g in res if g) / max(1, w25)))
    from collections import Counter
    print('hardest:', Counter(fails).most_common(15))
