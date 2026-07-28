#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'ALL_EXOS'/'corriges_inputs.tex'
EXCLUDED={'.git','.github','ALL_EXOS','FULL_PDF','Style','framework','resources','scripts','tools','xx_Figures'}

def esc(s:str)->str:
    return s.replace('\\',r'\textbackslash{}').replace('_',r'\_').replace('&',r'\&').replace('%',r'\%').replace('#',r'\#')

items=[]
for c in ROOT.rglob('corrige.tex'):
    rel=c.relative_to(ROOT)
    if rel.parts[0] in EXCLUDED: continue
    src=c.with_name(c.parent.name+'.tex')
    if src.exists(): items.append((rel,src.relative_to(ROOT)))
items.sort(key=lambda x:tuple(p.casefold() for p in x[0].parts))
if len(items)!=468: raise SystemExit(f'{len(items)} corrigés trouvés au lieu de 468')
lines=['% Généré par tools/generate_all_corriges.py','% 468 corrigés classés par répertoire.','']
ch=sec=None
for corr,src in items:
    if corr.parts[0]!=ch:
        ch=corr.parts[0]; sec=None; lines += [r'\clearpage',rf'\chapter{{{esc(ch)}}}','']
    if corr.parts[1]!=sec:
        sec=corr.parts[1]; lines += [rf'\section{{{esc(sec)}}}','']
    title=esc(corr.parent.name)
    parent=corr.parent.as_posix()
    lines += [rf'\subsection{{{title}}}',rf'\graphicspath{{{{../{parent}/images/}}{{../{parent}/}}{{../Style/png/}}}}',rf'\input{{../{corr.with_suffix("").as_posix()}}}','']
OUT.write_text('\n'.join(lines),encoding='utf-8')
print(f'{OUT}: {len(items)} corrigés')
