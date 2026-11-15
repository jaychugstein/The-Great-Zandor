# Folds the training survey's answers (a folder of one JSON file per thing, as pulled from the survey's database) into learned.json.
# python3 survey_apply.py <folder>
import json,glob,sys,os
sys.path.insert(0,'.')
import data,more4
NEW=set(m[0] for m in more4.MORE4)
names=set(o[0] for o in data.OBJ); qk=set(q[0] for q in data.Q)
SIZE=('$small','$small2','$pound','$duck','$heavy','$light','$microwave','$pickup','pocket')
L={};n=used=0;unk=set();badq=set()
for f in glob.glob(os.path.join(sys.argv[1] if len(sys.argv) > 1 else 'survey_pull', '*.json')):
    d=json.load(open(f));d=d.get('data',d);nm=d.get('name')
    for k,v in d.get('a',{}).items():
        n+=1
        if k in('paint','burn'):continue
        if k=='burnL': k='burn'   # (the lighter wording)
        if v<0: continue   # (DON'T KNOW: no answer, so the rules decide; in the game it's a skip now)
        if nm not in names: unk.add(nm);continue
        if k not in qk: badq.add(k);continue
        if (nm in data.DISPLAY or nm in data.MASS) and k in SIZE:continue
        sh=data.DISPLAY.get(nm,'').split(' of ')[0]
        if k in('$hard','soft') and sh in('a bag','a bowl','a plate','a glass','a cup','a mug','a bottle','a jar','a can','a tub','a jug','a tube','a pack'):continue
        if k=='$hold' and nm not in NEW:continue
        L.setdefault(nm,{})[k]=v;used+=1
print('answers',n,'applied',used,'things',len(L));print('unknown things',len(unk),sorted(unk)[:15]);print('unknown q',badq)
json.dump(L,open('learned.json','w'),indent=0,sort_keys=True)
