# Finds answers that are blank (so the game assumes "no") where the most similar things say "yes": the likely gaps.
# Used by mkqueue.py to put them first in the training survey.
import json, os, numpy as np
from data import OBJ, answers, Q
def find(k_near=10, need=0.5):
    L = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'learned.json')))
    keys = [k for k, _ in Q]; A = [answers(*o) for o in OBJ]
    M = np.array([[a.get(k, 0) for k in keys] for a in A], np.float32); has = np.array([[k in a for k in keys] for a in A])
    for i, o in enumerate(OBJ):
        for k in L.get(o[0], {}):
            if k in keys: has[i, keys.index(k)] = True
    Y = (M >= 3).astype(np.float32); n = Y / np.maximum(1, np.linalg.norm(Y, axis=1, keepdims=True)); S = n @ n.T; np.fill_diagonal(S, -1)
    out = []
    for i in range(len(OBJ)):
        nb = np.argsort(-S[i])[:k_near]
        frac = Y[nb].mean(0)
        for j in np.where((~has[i]) & (frac >= need))[0]: out.append((i, j, float(frac[j])))
    return sorted(out, key=lambda r: -r[2])
if __name__ == '__main__':
    r = find(); qt = dict(Q); keys = [k for k, _ in Q]
    print(len(r), 'blank answers where similar things say yes')
    for i, j, f in r[:40]: print(OBJ[i][0], '|', qt[keys[j]], round(f, 2))
