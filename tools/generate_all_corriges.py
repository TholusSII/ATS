#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'ALL_EXOS' / 'corriges_inputs.tex'
CATEGORY_RE = re.compile(r'^(0[1-9]|1[0-5])-')


def esc(s: str) -> str:
    return (s.replace('\\', r'\textbackslash{}').replace('_', r'\_')
             .replace('&', r'\&').replace('%', r'\%').replace('#', r'\#'))


categories = sorted(
    (p for p in ROOT.iterdir() if p.is_dir() and CATEGORY_RE.match(p.name)),
    key=lambda p: p.name.casefold(),
)
items = []
for category in categories:
    td = category / 'TD'
    if not td.is_dir():
        continue
    for corrige in td.rglob('corrige.tex'):
        source = corrige.with_name(corrige.parent.name + '.tex')
        if source.exists():
            items.append((corrige.relative_to(ROOT), source.relative_to(ROOT), category))
items.sort(key=lambda x: tuple(p.casefold() for p in x[0].parts))
if len(items) != 468:
    raise SystemExit(f'{len(items)} corrigés trouvés au lieu de 468')

lines = ['% Généré par tools/generate_all_corriges.py', '% 468 corrigés classés par répertoire.', '']
chapter = section = None
for corrige, source, category in items:
    if category.name != chapter:
        chapter = category.name
        section = None
        lines += [r'\clearpage', rf'\chapter{{{esc(chapter)}}}', '']
    relative_parent = (ROOT / corrige).parent.relative_to(category / 'TD')
    new_section = relative_parent.parts[0] if len(relative_parent.parts) > 1 else 'TD'
    if new_section != section:
        section = new_section
        lines += [rf'\section{{{esc(section)}}}', '']
    title = esc((ROOT / corrige).parent.name)
    parent = (ROOT / corrige).parent.relative_to(ROOT).as_posix()
    lines += [
        rf'\subsection{{{title}}}',
        rf'\graphicspath{{{{../{parent}/images/}}{{../{parent}/}}{{../Style/png/}}}}',
        rf'\input{{../{corrige.with_suffix("").as_posix()}}}',
        '',
    ]
OUT.write_text('\n'.join(lines), encoding='utf-8')
print(f'{OUT}: {len(items)} corrigés')
