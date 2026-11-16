import json
rows=json.load(open('coded/emotions.json',encoding='utf-8'))
out=["# Evidence table","","What each document contains that bears on the question, with the quotation (from coded/emotions.json after the check).",""]
for d in ["I10","I38"]:
    out+=[f"## {d}","","| valence | emotion | subject | link | quotation |","|---|---|---|---|---|"]
    for r in rows:
        if r["document"]==d:
            out.append("| "+" | ".join(str(r[k]).replace("|","/") for k in ["valence","emotion","subject","link","quote"])+" |")
    out.append("")
open('work/evidence-table.md','w',encoding='utf-8').write("\n".join(out))
print(len(rows))
