# Build-time safety checks (Nov 15): stop the build if a correction could silently wipe out another one.
# 1. A dict literal that lists the same name twice: Python keeps only the last, and the earlier entry is lost without a word.
# 2. A thin.py line for a name that is listed again: those are merged (not replaced), so this only reports them.
import ast, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def dup_keys(path):
    tree = ast.parse(open(path).read()); bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            seen = {}
            for k in node.keys:
                if isinstance(k, ast.Constant):
                    if k.value in seen: bad.append((os.path.basename(path), k.lineno, k.value, seen[k.value]))
                    seen[k.value] = k.lineno
    return bad
def run():
    bad = []
    for f in sorted(os.listdir(HERE)):
        if f.endswith('.py') and f != 'checks.py': bad += dup_keys(os.path.join(HERE, f))
    if bad:
        for f, l, k, l0 in bad: print('CHECK FAILED: %s line %d lists %r again (first at line %d); the earlier one would be lost' % (f, l, k, l0))
        sys.exit(1)
if __name__ == '__main__': run(); print('checks ok')
