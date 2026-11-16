import json, sys
a=json.load(open('coded/emotions.json')); b=json.load(open('recode/coded/emotions.json'))
def ov(x,y):
    x,y=x['quote'],y['quote']; return x in y or y in x or len(set(x.split())&set(y.split()))>=max(4,min(len(x.split()),len(y.split()))//2)
out=['# Passage-level comparison of first and second coding','']
for name,src,oth in (('first only',a,b),('second only',b,a)):
    out.append(f'## Passages coded by the {name} coder'); out.append('')
    for r in src:
        if not any(r['document']==o['document'] and ov(r,o) for o in oth):
            out.append(f"- {r['document']} | {r['valence']} | {r['emotion']} | \"{r['quote']}\"")
    out.append('')
out.append('## Same passage, different valence'); out.append('')
for r in a:
    for o in b:
        if r['document']==o['document'] and ov(r,o) and r['valence']!=o['valence']:
            out.append(f"- {r['document']}: first {r['valence']} \"{r['quote']}\" / second {o['valence']} \"{o['quote']}\"")
print('\n'.join(out))
