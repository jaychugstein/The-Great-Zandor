# Which things does Zandor miss most? Plays every thing several times and lists the worst, by kind.
import random, sys, os, collections
import numpy as np, fastsim as F
from data import Q, OBJ
KEY = {k: i for i, (k, _) in enumerate(Q)}
rnd = random.Random(3); R = int(os.environ.get('R', 6)); noise = 0.10
res = {}
for t in range(F.N):
    w20 = w25 = 0
    for r in range(R):
        g = F.game(t, rnd, noise)
        if g and g <= 21: w20 += 1
        if g: w25 += 1
    res[t] = (w20, w25)
def kind(t):
    g = lambda k: F.M[t, KEY[k]]
    n, c, size, _ = OBJ[t]
    if g('person') >= 3: return 'person'
    if size == 'x': return 'idea'
    if g('place') >= 3: return 'place'
    if g('body') >= 3: return 'body'
    if g('eat') >= 3 or g('drink') >= 3: return 'food'
    if c == 'A': return 'animal'
    if g('plant') >= 3: return 'plant'
    if g('pretend') >= 3: return 'pretend'
    if g('weather') >= 3 or g('sky') >= 3: return 'sky'
    return 'thing'
by = collections.defaultdict(list)
for t in range(F.N): by[kind(t)].append(t)
print('all: by 20 %.1f%%  by 25 %.1f%%' % (100 * sum(v[0] for v in res.values()) / (R * F.N), 100 * sum(v[1] for v in res.values()) / (R * F.N)))
for k, ts in sorted(by.items(), key=lambda x: -len(x[1])):
    print('%-8s %4d things  by20 %3.0f%%  by25 %3.0f%%' % (k, len(ts), 100 * sum(res[t][0] for t in ts) / (R * len(ts)), 100 * sum(res[t][1] for t in ts) / (R * len(ts))))
if os.environ.get('LIST'):
    for k in os.environ['LIST'].split(','):
        print(k, ':', ', '.join('%s %d/%d' % (OBJ[t][0], res[t][1], R) for t in sorted(by[k], key=lambda t: res[t][1])))
