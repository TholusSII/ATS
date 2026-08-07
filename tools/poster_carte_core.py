from pathlib import Path

POSTER_TEMPLATE = r'''\documentclass[10pt,a3paper]{article}
\usepackage[margin=10mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[french]{babel}
\usepackage{lmodern}
\usepackage{microtype}
\makeatletter\def\input@path{{../../../Style/}}\makeatother
\input{TLPosterCarteMentale.sty}
\pagestyle{empty}
\renewcommand{\familydefault}{\sfdefault}
\begin{document}
\TLPosterCourseHeader{@@CHAPTER@@}{@@TITLE@@}{@@SUBTITLE@@}
\vspace{2mm}
\begin{minipage}[t]{0.61\linewidth}
\begin{TLPosterSavoirs}
\begin{itemize}
@@SAVOIRS@@
\end{itemize}
\end{TLPosterSavoirs}
\end{minipage}\hfill
\begin{minipage}[t]{0.36\linewidth}
\TLPosterKey{@@KEYTITLE@@}{@@KEY@@}
\end{minipage}
\vfill
\begin{minipage}[t]{0.49\linewidth}
@@BLOCK1@@
@@BLOCK3@@
\end{minipage}\hfill
\begin{minipage}[t]{0.49\linewidth}
@@BLOCK2@@
@@BLOCK4@@
\end{minipage}
\vfill
\begin{TLPosterMethode}
\begin{enumerate}
@@METHOD@@
\end{enumerate}
\end{TLPosterMethode}
\vfill
\TLPosterRetenir{@@RETENIR@@}
\end{document}
'''

MIND_TEMPLATE = r'''\documentclass[10pt,a3paper,landscape]{article}
\usepackage[margin=6mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[french]{babel}
\usepackage{lmodern}
\usepackage{microtype}
\makeatletter\def\input@path{{../../../Style/}}\makeatother
\input{TLPosterCarteMentale.sty}
\pagestyle{empty}
\renewcommand{\familydefault}{\sfdefault}
\begin{document}
\begin{tikzpicture}
\TLMapBase{@@TITLE@@}{@@KEY@@}
\TLMapBranchTL{Savoirs}{@@MAPSAVOIRS@@}
\TLMapBranchTR{@@MAPLABEL1@@}{@@MAPCONTENT1@@}
\TLMapBranchML{@@MAPLABEL2@@}{@@MAPCONTENT2@@}
\TLMapBranchMR{@@MAPLABEL3@@}{@@MAPCONTENT3@@}
\TLMapBranchBL{@@MAPLABEL4@@}{@@MAPCONTENT4@@}
\TLMapBranchBR{Méthode}{@@MAPMETHOD@@}
\TLMapRibbon{@@MAPFLOW@@}
\end{tikzpicture}
\end{document}
'''

COLORS = ["TLPosterBlue", "TLPosterGreen", "TLPosterPurple", "TLPosterTeal"]


def _items(items):
    return "\n".join(r"  \item " + x for x in items)


def _map_items(items, numbered=False, limit=6):
    out = []
    for i, item in enumerate(items[:limit], 1):
        prefix = f"{i}. " if numbered else r"\textbullet\ "
        out.append(prefix + item)
    return r"\\[1.2mm]".join(out)


def _block(title, body, color):
    return "\\begin{TLPosterBloc}[" + title + "]{" + color + "}\n" + body + "\n\\end{TLPosterBloc}"


def _safe(title):
    return ''.join(c if c.isalnum() else '_' for c in title)


def _render(template, values):
    for key, value in values.items():
        template = template.replace(f"@@{key}@@", str(value))
    return template


def generate(data, root=Path('.')):
    written = []
    for prefix, d in data.items():
        course = root / d['folder'] / 'Cours'
        poster_dir = course / 'Poster'
        mind_dir = course / 'Carte mentale'
        poster_dir.mkdir(parents=True, exist_ok=True)
        mind_dir.mkdir(parents=True, exist_ok=True)

        # Une seule source canonique par support : on supprime les anciens
        # gabarits génériques ou les titres devenus obsolètes.
        for old in poster_dir.glob('*.tex'):
            old.unlink()
        for old in mind_dir.glob('*.tex'):
            old.unlink()

        blocks = [_block(h, b, COLORS[i]) for i, (h, b) in enumerate(d['blocks'])]
        poster = _render(POSTER_TEMPLATE, {
            'CHAPTER': int(prefix), 'TITLE': d['title'], 'SUBTITLE': d['subtitle'],
            'SAVOIRS': _items(d['savoirs']), 'KEYTITLE': d['key_title'], 'KEY': d['key'],
            'BLOCK1': blocks[0], 'BLOCK2': blocks[1], 'BLOCK3': blocks[2], 'BLOCK4': blocks[3],
            'METHOD': _items(d['method']), 'RETENIR': d['retenir'],
        })

        map_values = {
            'TITLE': d['title'], 'KEY': d['map_key'],
            'MAPSAVOIRS': _map_items(d['savoirs'], limit=5),
            'MAPMETHOD': _map_items(d['method'], numbered=True, limit=5),
            'MAPFLOW': d['map_flow'],
        }
        for i, (label, items) in enumerate(d['map'], 1):
            map_values[f'MAPLABEL{i}'] = label
            map_values[f'MAPCONTENT{i}'] = _map_items(items, limit=5)
        mind = _render(MIND_TEMPLATE, map_values)

        safe = f"{prefix}_{_safe(d['title'])}"
        poster_path = poster_dir / f"Poster_{safe}.tex"
        mind_path = mind_dir / f"Carte_Mentale_{safe}.tex"
        poster_path.write_text(poster, encoding='utf-8')
        mind_path.write_text(mind, encoding='utf-8')
        written += [poster_path, mind_path]
    return written
