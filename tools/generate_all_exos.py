#!/usr/bin/env python3
"""Génère ALL_EXOS/inputs.tex à partir de l'arborescence des exercices."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "ALL_EXOS" / "inputs.tex"
EXPECTED_EXERCISES = 383
EXCLUDED_TOP_LEVEL = {
    ".git",
    ".github",
    "ALL_EXOS",
    "FULL_PDF",
    "Style",
    "framework",
    "resources",
    "scripts",
    "tools",
    "xx_Figures",
}


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "_": r"\_",
        "&": r"\&",
        "%": r"\%",
        "#": r"\#",
        "$": r"\$",
        "{": r"\{",
        "}": r"\}",
    }
    return "".join(replacements.get(char, char) for char in text)


def is_exercise_fragment(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if len(relative.parts) < 4:
        return False
    if relative.parts[0] in EXCLUDED_TOP_LEVEL:
        return False
    if path.name.endswith("_old.tex") or "_Colle_" in path.name:
        return False
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return (
        r"\documentclass" not in content
        and (r"\exer" in content or r"\subsection*" in content)
    )


def sort_key(path: Path) -> tuple[str, ...]:
    return tuple(part.casefold() for part in path.relative_to(ROOT).parts)


def main() -> None:
    exercises = sorted(
        (path for path in ROOT.rglob("*.tex") if is_exercise_fragment(path)),
        key=sort_key,
    )
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

    for source in exercises:
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
        source_path = relative.with_suffix("").as_posix()
        lines.extend(
            [
                rf"\graphicspath{{{{../{parent}/images/}}{{../{parent}/}}{{../Style/png/}}}}",
                rf"\input{{../{source_path}}}",
                "",
            ]
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"{OUTPUT.relative_to(ROOT)} généré avec {len(exercises)} exercices.")


if __name__ == "__main__":
    main()
