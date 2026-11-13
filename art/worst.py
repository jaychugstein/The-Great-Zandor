# The things Zandor misses most, with what he guesses instead and how thinly they are filled in.
import random, os, collections
import numpy as np, fastsim as F
from data import OBJ
rnd = random.Random(5); R = int(os.environ.get('R', 10)); rows = []
for t in range(F.N):
    w = 0; conf = collections.Counter()
    for r in range(R):
        log = []; g = F.game(t, rnd, 0.10, log)
        if g and g <= 21: w += 1
        else: conf.update(log[-3:])
    rows.append((w, t, conf))
rows.sort(key=lambda x: x[0])
for w, t, conf in rows[:int(os.environ.get('TOP', 70))]:
    print('%d/%d %-22s yes:%2d  <- %s' % (w, R, OBJ[t][0], int((F.M[t] >= 3).sum()), ', '.join(n for n, _ in conf.most_common(4))))
print('won %.1f%%; things under 70%%: %d' % (100 * sum(r[0] for r in rows) / (R * F.N), sum(1 for r in rows if r[0] < 0.7 * R)))
