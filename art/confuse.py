# Mix-ups (Nov 15): plays pretend games and notes which wrong thing Zandor guesses for each real one, then picks the
# questions that should tell each pair apart but don't yet: the two answers are close (or one is blank), and at least
# one of the two hasn't been answered in the survey. Both things get asked that question, so your answers split them.
import json, os, random, collections, numpy as np
import fastsim as F
from data import OBJ, Q
def pairs(rounds=6, noise=0.10, seed=3):
    rnd = random.Random(seed); c = collections.Counter(); idx = {o[0]: i for i, o in enumerate(OBJ)}
    for t in range(F.N):
        for r in range(rounds):
            log = []; F.game(t, rnd, noise, log)
            for w in log: c[(t, idx[w])] += 1
    return c
def cards(max_pairs=400, per_pair=3):
    L = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'learned.json')))
    keys = [k for k, _ in Q]; out = []; seen = set()
    for (t, w), n in pairs().most_common(max_pairs):
        lt, lw = L.get(OBJ[t][0], {}), L.get(OBJ[w][0], {})
        cand = []
        for q in range(F.NQ):
            k = keys[q]; a, b = int(F.M[t, q]), int(F.M[w, q])
            if abs(a - b) >= 3 or (k in lt and k in lw): continue           # (already tells them apart, or you've answered both)
            if max(a, b) < 2: continue                                     # (both a clear no: not much to learn)
            if a == b and a != 2: continue                                 # (both a clear yes: they really are the same there)
            cand.append((-F.QW[q] - 3 * (a == 2 or b == 2) - 2 * (abs(a - b) == 2), q))   # (an unsure answer, or a near-miss, is where the mix-up hides)
        for _, q in sorted(cand)[:per_pair]:
            for i in (t, w):
                if (i, q) not in seen and keys[q] not in L.get(OBJ[i][0], {}): seen.add((i, q)); out.append([int(i), int(q), int(F.M[i, q])])
    return out
if __name__ == '__main__':
    from data import DISPLAY
    c = pairs(); keys = dict(Q)
    for (t, w), n in c.most_common(15): print(n, DISPLAY.get(OBJ[t][0], OBJ[t][0]), '-> guessed', DISPLAY.get(OBJ[w][0], OBJ[w][0]))
    print(len(cards()), 'cards')
