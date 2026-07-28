#!/usr/bin/env python3
"""Génère ALL_EXOS/inputs.tex à partir de l'arborescence des exercices."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "ALL_EXOS" / "inputs.tex"
EXPECTED_EXERCISES = 468
EXCLUDED_TOP_LEVEL = {
    ".git", ".github", "ALL_EXOS", "FULL_PDF", "Style", "framework",
    "resources", "scripts", "tools", "xx_Figures",
}


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}", "_": r"\_", "&": r"\&", "%": r"\%",
        "#": r"\#", "$": r"\$", "{": r"\{", "}": r"\}",
    }
    return "".join(replacements.get(char, char) for char in text)


def inspect_exercise(path: Path) -> bool | None:
    relative = path.relative_to(ROOT)
    if len(relative.parts) < 4 or relative.parts[0] in EXCLUDED_TOP_LEVEL:
        return None
    if path.name.endswith("_old.tex") or "_Colle_" in path.name or path.name == "corrige.tex":
        return None
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    if r"\documentclass" in content:
        return None
    if r"\exer" not in content and r"\subsection*" not in content:
        return None
    return r"\exer" in content


def sort_key(path: Path) -> tuple[str, ...]:
    return tuple(part.casefold() for part in path.relative_to(ROOT).parts)


def main() -> None:
    exercises: list[tuple[Path, bool]] = []
    for path in ROOT.rglob("*.tex"):
        has_exer = inspect_exercise(path)
        if has_exer is not None:
            exercises.append((path, has_exer))
    exercises.sort(key=lambda item: sort_key(item[0]))

    if len(exercises) != EXPECTED_EXERCISES:
        raise SystemExit(
            f"Nombre d'exercices inattendu : {len(exercises)} "
            f"(attendu : {EXPECTED_EXERCISES})."
        )

    lines = [
        "% Fichier généré automatiquement : ne pas modifier à la main.",
        f"% {len(exercises)} exercices classés par répertoire.",
        "",
    ]
    current_chapter: str | None = None
    current_section: str | None = None

    for source, has_exer in exercises:
        relative = source.relative_to(ROOT)
        chapter, section = relative.parts[0], relative.parts[1]

        if chapter != current_chapter:
            lines.extend([r"\clearpage", rf"\chapter{{{tex_escape(chapter)}}}", ""])
            current_chapter = chapter
            current_section = None

        if section != current_section:
            lines.extend([rf"\section{{{tex_escape(section)}}}", ""])
            current_section = section

        parent = relative.parent.as_posix()
        fallback_title = tex_escape(relative.parent.name)
        lines.extend(
            [
                r"\refstepcounter{exerciseentry}",
                r"\setcounter{question}{0}",
                r"\phantomsection",
                rf"\addcontentsline{{toc}}{{subsection}}{{\protect\numberline{{\theexerciseentry}}{fallback_title}}}",
                rf"\graphicspath{{{{../{parent}/images/}}{{../{parent}/}}{{../Style/png/}}}}",
            ]
        )
        if not has_exer:
            lines.append(rf"\ExerciseTitle{{{fallback_title}}}")
        lines.extend([rf"\subimport{{../{parent}/}}{{{relative.name}}}", ""])

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"{OUTPUT.relative_to(ROOT)} généré avec {len(exercises)} exercices.")


if __name__ == "__main__":
    main()
