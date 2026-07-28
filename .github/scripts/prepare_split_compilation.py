#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import os
import re

ROOT = Path('.').resolve()
ALL_DIR = ROOT / 'ALL_EXOS'

TITLE_PATTERN = re.compile(r'^(\s*\\exer\{[^\r\n]*?\})\\n', re.MULTILINE)
QR_PATTERN = re.compile(r'\\qrcode(?:\[[^\]]*\])?\{([^{}]+)\}')
GRAPHICS_PATTERN = re.compile(r'(\\includegraphics(?:\[[^\]]*\])?\{)([^{}]+)(\})')
BAD_RAD_PATTERN = re.compile(r'\\SI\{([+-]?(?:\d+(?:[.,]\d*)?|[.,]\d+))\s*rad\}\{s\}')
EXTENSIONS = ('', '.pdf', '.png', '.jpg', '.jpeg', '.PDF', '.PNG', '.JPG', '.JPEG')


def existing_path(base: Path, reference: str) -> Path | None:
    for parent in (base, ROOT, ALL_DIR):
        for extension in EXTENSIONS:
            candidate = (parent / (reference + extension)).resolve()
            if candidate.is_file():
                return candidate
    return None


def repair_graphic(path: Path, match: re.Match[str]) -> str:
    reference = match.group(2)
    if existing_path(path.parent, reference):
        return match.group(0)

    stem = Path(reference).name
    simple = stem[:-2] if stem.endswith('_c') else stem
    candidates: list[Path] = []
    image_dir = path.parent / 'images'
    if image_dir.is_dir():
        candidates.extend(sorted(image_dir.glob(simple + '*')))
    if not candidates:
        candidates.extend(sorted(ROOT.rglob(simple + '*')))
    candidates = [
        item for item in candidates
        if item.is_file() and item.suffix.lower() in {'.pdf', '.png', '.jpg', '.jpeg'}
    ]
    if not candidates:
        return r'\fbox{\textit{Illustration non disponible}}'

    relative = Path(os.path.relpath(candidates[0], path.parent)).as_posix()
    return match.group(1) + relative + match.group(3)


def apply_transient_compatibility() -> None:
    modified = 0
    malformed_si = 0
    for path in ROOT.rglob('*.tex'):
        if '.git' in path.parts or path.name.startswith(('PART_', 'FRONTMATTER')):
            continue
        text = path.read_text(encoding='utf-8', errors='ignore')
        updated = TITLE_PATTERN.sub(r'\1\n', text)
        updated = QR_PATTERN.sub(
            lambda match: r'\fbox{\href{' + match.group(1) + r'}{\textsf{Lien vers le formulaire}}}',
            updated,
        )
        updated, count = BAD_RAD_PATTERN.subn(
            lambda match: r'\SI{' + match.group(1) + r'}{rad.s^{-1}}',
            updated,
        )
        malformed_si += count
        updated = updated.replace(r'\proftrue', r'\proffalse')
        updated = updated.replace(r'\correctiontrue', r'\correctionfalse')
        updated = GRAPHICS_PATTERN.sub(lambda match: repair_graphic(path, match), updated)
        if updated != text:
            path.write_text(updated, encoding='utf-8')
            modified += 1

    compat = ROOT / 'Style/exercices_compat.tex'
    text = compat.read_text(encoding='utf-8')
    marker = r'\@ifundefined{c@question}{\newcounter{question}}{}'
    addition = marker + '\n' + r'\@ifundefined{c@exo}{\newcounter{exo}}{}'
    if r'\@ifundefined{c@exo}' not in text:
        compat.write_text(text.replace(marker, addition), encoding='utf-8')

    print(f'{modified} sources adaptées dans le checkout éphémère.')
    print(f'{malformed_si} écriture(s) siunitx corrigée(s).')


def tex_escape(value: str) -> str:
    replacements = {'&': r'\&', '%': r'\%', '#': r'\#', '_': r'\_'}
    return ''.join(replacements.get(char, char) for char in value)


def build_parts() -> None:
    inputs = (ALL_DIR / 'inputs.tex').read_text(encoding='utf-8')
    chapter_re = re.compile(r'(?m)^\\clearpage\s*\n\\chapter\{([^\n{}]*)\}\s*\n')
    matches = list(chapter_re.finditer(inputs))
    if not matches:
        raise SystemExit('Aucun chapitre trouvé dans ALL_EXOS/inputs.tex')

    master = (ALL_DIR / 'ALL_EXOS.tex').read_text(encoding='utf-8')
    preamble, document = master.split(r'\begin{document}', 1)
    before_input = document.split(r'\input{inputs.tex}', 1)[0]
    setup = before_input[before_input.index(r'\mainmatter'):]

    lock_modes = (
        r'\proffalse' + '\n' +
        r'\let\proftrue\proffalse' + '\n' +
        r'\ifdefined\correctionfalse' + '\n' +
        r'  \correctionfalse' + '\n' +
        r'  \let\correctiontrue\correctionfalse' + '\n' +
        r'\fi' + '\n'
    )
    reset_modes = r'\proffalse' + '\n' + r'\ifdefined\correctionfalse\correctionfalse\fi' + '\n'

    manifest: list[str] = []
    summary_rows: list[tuple[str, int]] = []
    total_exercises = 0

    for index, match in enumerate(matches, 1):
        end = matches[index].start() if index < len(matches) else len(inputs)
        block = inputs[match.start():end].rstrip() + '\n'
        block = block.replace(r'\subimport', reset_modes + r'\subimport')
        title = match.group(1)
        exercise_count = block.count(r'\subimport')
        total_exercises += exercise_count
        prefix_match = re.match(r'(\d+)', title)
        chapter_number = int(prefix_match.group(1)) if prefix_match else index
        stem = f'PART_{index:02d}'

        (ALL_DIR / f'inputs_{stem}.tex').write_text(block, encoding='utf-8')
        part = (
            r'\def\ModeCorriges{1}' + '\n' + preamble + r'\begin{document}' + '\n' +
            setup + lock_modes + f'\\setcounter{{chapter}}{{{chapter_number - 1}}}\n' +
            f'\\input{{inputs_{stem}.tex}}\n' + r'\end{document}' + '\n'
        )
        (ALL_DIR / f'{stem}.tex').write_text(part, encoding='utf-8')
        (ALL_DIR / 'gnuplot' / stem).mkdir(parents=True, exist_ok=True)
        manifest.append(f'{stem}.pdf')
        summary_rows.append((title, exercise_count))

    if total_exercises != 468:
        raise SystemExit(f'Découpage incomplet : {total_exercises} exercices au lieu de 468')

    rows = '\n'.join(f'{tex_escape(title)} & {count} exercices \\\\' for title, count in summary_rows)
    front = (
        r'\def\ModeCorriges{1}' + '\n' + preamble + r'\begin{document}' + '\n' +
        r'\frontmatter' + '\n' + r'\maketitle' + '\n' +
        r'\chapter*{Sommaire du recueil}' + '\n' +
        r'\begin{longtable}{p{0.78\linewidth}r}' + '\n' +
        r'\toprule Famille & Contenu \\ \midrule' + '\n' + rows + '\n' +
        r'\bottomrule\end{longtable}' + '\n' +
        r'\vfill\begin{center}\textbf{468 exercices avec leurs corrigés intégrés}\end{center}' + '\n' +
        r'\end{document}' + '\n'
    )
    (ALL_DIR / 'FRONTMATTER.tex').write_text(front, encoding='utf-8')
    (ALL_DIR / 'gnuplot' / 'FRONTMATTER').mkdir(parents=True, exist_ok=True)
    (ALL_DIR / 'PDF_PARTS_ORDER.txt').write_text(
        'FRONTMATTER.pdf\n' + '\n'.join(manifest) + '\n', encoding='utf-8'
    )
    print(f'{len(manifest)} familles préparées, {total_exercises} exercices.')


def main() -> None:
    (ALL_DIR / 'gnuplot').mkdir(parents=True, exist_ok=True)
    apply_transient_compatibility()
    build_parts()


if __name__ == '__main__':
    main()
