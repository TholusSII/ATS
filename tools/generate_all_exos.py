#!/usr/bin/env python3
"""Génère les quinze fichiers TD.tex et le recueil ALL_EXOS."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ALL_EXOS = ROOT / "ALL_EXOS" / "ALL_EXOS.tex"
INPUTS = ROOT / "ALL_EXOS" / "inputs.tex"
EXPECTED_EXERCISES = 468
CATEGORY_RE = re.compile(r"^(0[1-9]|1[0-5])-")
BEGIN = "% BEGIN AUTO TD INCLUDES"
END = "% END AUTO TD INCLUDES"


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}", "_": r"\_", "&": r"\&", "%": r"\%",
        "#": r"\#", "$": r"\$", "{": r"\{", "}": r"\}",
    }
    return "".join(replacements.get(char, char) for char in text)


def categories() -> list[Path]:
    result = sorted(
        (path for path in ROOT.iterdir() if path.is_dir() and CATEGORY_RE.match(path.name)),
        key=lambda path: path.name.casefold(),
    )
    numbers = [int(path.name[:2]) for path in result]
    if numbers != list(range(1, 16)):
        raise SystemExit(f"Familles trouvées : {numbers}; attendu : 01 à 15.")
    return result


def inspect_source(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if r"\documentclass" in text:
        return False
    return r"\exer" in text or r"\subsection*" in text


def exercise_sources(category: Path) -> list[tuple[Path, bool]]:
    td = category / "TD"
    result: list[tuple[Path, bool]] = []
    if not td.is_dir():
        return result
    for source in td.rglob("*.tex"):
        if source.name in {"corrige.tex", "TD.tex"} or source.name.endswith("_old.tex"):
            continue
        if source.name != source.parent.name + ".tex":
            continue
        if not (source.parent / "corrige.tex").is_file():
            continue
        result.append((source, inspect_source(source)))
    result.sort(key=lambda item: tuple(part.casefold() for part in item[0].relative_to(td).parts))
    return result


def section_name(category: Path, source: Path) -> str:
    relative_parent = source.parent.relative_to(category / "TD")
    return relative_parent.parts[0] if len(relative_parent.parts) > 1 else "TD"


def write_category_td(category: Path, exercises: list[tuple[Path, bool]]) -> None:
    lines = [
        "% Fichier généré automatiquement : ne pas modifier à la main.",
        f"% {len(exercises)} TD dans {category.name}.",
        r"\clearpage",
        rf"\chapter{{{tex_escape(category.name)}}}",
        "",
    ]
    current_section: str | None = None
    for source, has_exer in exercises:
        section = section_name(category, source)
        if section != current_section:
            lines.extend([rf"\section{{{tex_escape(section)}}}", ""])
            current_section = section
        relative = source.relative_to(ROOT)
        parent = relative.parent.as_posix()
        title = tex_escape(source.parent.name)
        lines.extend([
            r"\refstepcounter{exerciseentry}",
            r"\setcounter{question}{0}",
            r"\phantomsection",
            rf"\addcontentsline{{toc}}{{subsection}}{{\protect\numberline{{\theexerciseentry}}{title}}}",
            rf"\graphicspath{{{{../{parent}/images/}}{{../{parent}/}}{{../Style/png/}}}}",
        ])
        if not has_exer:
            lines.append(rf"\ExerciseTitle{{{title}}}")
        lines.extend([rf"\subimport{{../{parent}/}}{{{relative.name}}}", ""])
    if not exercises:
        lines.append("% Aucun TD dans cette famille pour le moment.")
    (category / "TD.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_master(cats: list[Path], total: int) -> None:
    includes = [rf"\subimport{{../{category.name}/}}{{TD.tex}}" for category in cats]
    INPUTS.parent.mkdir(parents=True, exist_ok=True)
    INPUTS.write_text(
        "% Fichier généré automatiquement : ne pas modifier à la main.\n"
        f"% {total} exercices répartis dans 15 fichiers TD.tex.\n\n"
        + "\n".join(includes) + "\n",
        encoding="utf-8",
    )

    text = ALL_EXOS.read_text(encoding="utf-8")
    block = BEGIN + "\n" + "\n".join(includes) + "\n" + END
    if BEGIN in text and END in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), block, text, flags=re.S)
    elif r"\input{inputs.tex}" in text:
        text = text.replace(r"\input{inputs.tex}", block)
    else:
        raise SystemExit("Point d'insertion introuvable dans ALL_EXOS/ALL_EXOS.tex")
    ALL_EXOS.write_text(text, encoding="utf-8")


def main() -> None:
    cats = categories()
    all_exercises: list[tuple[Path, bool]] = []
    for category in cats:
        exercises = exercise_sources(category)
        write_category_td(category, exercises)
        all_exercises.extend(exercises)
    if len(all_exercises) != EXPECTED_EXERCISES:
        raise SystemExit(
            f"Nombre d'exercices inattendu : {len(all_exercises)} "
            f"(attendu : {EXPECTED_EXERCISES})."
        )
    update_master(cats, len(all_exercises))
    print(f"15 fichiers TD.tex et ALL_EXOS générés avec {len(all_exercises)} exercices.")


if __name__ == "__main__":
    main()
