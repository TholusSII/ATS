#!/usr/bin/env python3
"""Place les 468 exercices dans les sous-dossiers TD et crée les dossiers Cours."""
from __future__ import annotations

from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_RE = re.compile(r"^(0[1-9]|1[0-5])-")
TEXT_SUFFIXES = {'.tex', '.py', '.md', '.yml', '.yaml', '.txt', '.csv', '.json', '.sty', '.cls', '.sh'}


def categories() -> list[Path]:
    result = sorted(
        (path for path in ROOT.iterdir() if path.is_dir() and CATEGORY_RE.match(path.name)),
        key=lambda path: path.name.casefold(),
    )
    numbers = [int(path.name[:2]) for path in result]
    if numbers != list(range(1, 16)):
        raise SystemExit(f"Familles trouvées : {numbers}; attendu : 01 à 15.")
    return result


def move_contents(category: Path) -> int:
    td = category / 'TD'
    cours = category / 'Cours'
    td.mkdir(exist_ok=True)
    cours.mkdir(exist_ok=True)
    moved = 0
    for entry in list(category.iterdir()):
        if entry.name in {'TD', 'Cours', 'TD.tex'}:
            continue
        destination = td / entry.name
        if destination.exists():
            raise SystemExit(f"Collision pendant le déplacement : {destination}")
        shutil.move(str(entry), str(destination))
        moved += 1
    (cours / '.gitkeep').write_text('', encoding='utf-8')
    if not any(td.iterdir()):
        (td / '.gitkeep').write_text('', encoding='utf-8')
    return moved


def update_text_references(cats: list[Path]) -> int:
    changed = 0
    patterns = [
        (
            re.compile(re.escape(category.name) + r'/(?!TD/|Cours/|TD\.tex)'),
            category.name + '/TD/',
        )
        for category in cats
    ]
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            continue
        updated = text
        for pattern, replacement in patterns:
            updated = pattern.sub(replacement, updated)
        if updated != text:
            path.write_text(updated, encoding='utf-8')
            changed += 1
    return changed


def validate(cats: list[Path]) -> tuple[int, int, int]:
    exercises = corrections = includes = 0
    outside = []
    for category in cats:
        if not (category / 'Cours' / '.gitkeep').is_file():
            raise SystemExit(f"Cours absent dans {category.name}")
        if not (category / 'TD').is_dir() or not (category / 'TD.tex').is_file():
            raise SystemExit(f"Structure TD incomplète dans {category.name}")
        for source in category.rglob('*.tex'):
            if source.name == source.parent.name + '.tex' and (source.parent / 'corrige.tex').is_file():
                exercises += 1
                if 'TD' not in source.relative_to(category).parts:
                    outside.append(source.relative_to(ROOT).as_posix())
                text = source.read_text(encoding='utf-8', errors='ignore')
                if r'\InclureCorrige{corrige.tex}' in text:
                    includes += 1
        corrections += sum(1 for path in (category / 'TD').rglob('corrige.tex')
                           if path.with_name(path.parent.name + '.tex').is_file())
    if outside:
        raise SystemExit('Exercices restés hors TD : ' + ', '.join(outside[:10]))
    if (exercises, corrections, includes) != (468, 468, 468):
        raise SystemExit(
            f"Contrôle incorrect : {exercises} exercices, {corrections} corrigés, {includes} inclusions"
        )
    master = (ROOT / 'ALL_EXOS' / 'ALL_EXOS.tex').read_text(encoding='utf-8')
    if master.count(r'\subimport{../') < 15 or master.count('{TD.tex}') != 15:
        raise SystemExit('ALL_EXOS/ALL_EXOS.tex ne référence pas les quinze TD.tex')
    return exercises, corrections, includes


def main() -> None:
    cats = categories()
    moved = sum(move_contents(category) for category in cats)
    references = update_text_references(cats)
    subprocess.run(['python3', 'tools/generate_all_exos.py'], cwd=ROOT, check=True)
    subprocess.run(['python3', 'tools/generate_all_corriges.py'], cwd=ROOT, check=True)
    exercises, corrections, includes = validate(cats)
    report = [
        '# Structure ATS appliquée', '',
        f'- Familles structurées : **{len(cats)}**',
        f'- Entrées déplacées dans les dossiers `TD` : **{moved}**',
        f'- Fichiers texte dont les chemins ont été actualisés : **{references}**',
        f'- Contrôle : **{exercises} exercices, {corrections} corrigés, {includes} inclusions**', '',
        'Chaque famille contient désormais :', '',
        '```text',
        'NN-Nom de la famille/',
        '├── Cours/',
        '├── TD/',
        '└── TD.tex',
        '```',
    ]
    (ROOT / 'STRUCTURE_ATS.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
    print(f"Structure ATS validée : {exercises}/{corrections}/{includes}.")


if __name__ == '__main__':
    main()
