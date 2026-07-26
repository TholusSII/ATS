#!/usr/bin/env python3
"""Génère ALL_EXOS/ALL_EXOS.tex à partir des exercices du dépôt.

Les vrais exercices sont reconnus par la commande historique ``\\exer{...}``.
Les documents autonomes et les fichiers d'assemblage sont volontairement exclus.
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "ALL_EXOS"
OUTPUT = OUTPUT_DIR / "ALL_EXOS.tex"
MANIFEST = OUTPUT_DIR / "MANIFEST.txt"

IGNORED_TOP_LEVEL = {
    ".git",
    ".github",
    "ALL_EXOS",
    "FULL_PDF",
    "framework",
    "scripts",
    "xx_Figures",
}

TOP_LEVEL_TITLES = {
    "SYS": "Analyse fonctionnelle et systèmes",
    "GEO": "Géométrie des mécanismes",
    "CIN": "Cinématique",
    "STAT": "Statique",
    "CHS": "Hyperstatisme et théorie des mécanismes",
    "DYN": "Dynamique",
    "TEC": "Énergétique",
    "SLCI": "Systèmes linéaires continus invariants",
    "PERF": "Performances des systèmes asservis",
    "COR": "Correction des systèmes asservis",
    "NL": "Systèmes non linéaires",
    "SEQ": "Systèmes combinatoires et séquentiels",
    "NUM": "Méthodes numériques",
    "RDM": "Résistance des matériaux",
    "ELEC": "Électricité et électromécanique",
    "PPM": "Produit, procédés et matériaux",
}


def tex_escape_title(value: str) -> str:
    """Transforme un nom de dossier en titre TeX lisible."""
    value = value.replace("_", " ")
    value = re.sub(r"(?<=[a-zà-ÿ])(?=[A-Z])", " ", value)
    value = value.replace("-", " -- ")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def is_exercise(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="latin-1")
    return "\\exer{" in text and "\\documentclass" not in text


def collect_exercises() -> dict[str, dict[str, list[Path]]]:
    grouped: dict[str, dict[str, list[Path]]] = defaultdict(lambda: defaultdict(list))
    for path in sorted(ROOT.rglob("*.tex")):
        rel = path.relative_to(ROOT)
        if not rel.parts or rel.parts[0] in IGNORED_TOP_LEVEL:
            continue
        if not is_exercise(path):
            continue

        top = rel.parts[0]
        # Le dernier dossier est généralement celui de l'exercice ; les dossiers
        # précédents constituent le thème de classement.
        parent_parts = rel.parent.parts
        if len(parent_parts) >= 3:
            group_parts = parent_parts[1:-1]
        elif len(parent_parts) == 2:
            group_parts = parent_parts[1:]
        else:
            group_parts = ("Exercices",)
        group = " / ".join(group_parts)
        grouped[top][group].append(rel)
    return grouped


def build_master(grouped: dict[str, dict[str, list[Path]]]) -> str:
    lines: list[str] = [
        "% Fichier généré automatiquement par scripts/generate_all_exos.py",
        "% Ne pas modifier manuellement : relancer le script après ajout d'exercices.",
        "\\documentclass[10pt,a4paper,twoside,openany]{book}",
        "\\usepackage{framework/SI_Exercices}",
        "\\renewcommand{\\repStyle}{framework}",
        "\\newcommand{\\discipline}{Sciences industrielles de l'ingénieur}",
        "\\newcommand{\\auteur}{Thomas Lusseau}",
        "\\title{Recueil complet d'exercices de Sciences industrielles de l'ingénieur}",
        "\\author{Thomas Lusseau}",
        "\\date{\\today}",
        "\\begin{document}",
        "\\frontmatter",
        "\\maketitle",
        "\\tableofcontents",
        "\\mainmatter",
        "\\proffalse",
        "\\livrettrue",
        "\\collefalse",
        "",
    ]

    for top in sorted(grouped):
        title = TOP_LEVEL_TITLES.get(top, tex_escape_title(top))
        lines.extend([f"\\part{{{title}}}", ""])
        for group in sorted(grouped[top]):
            chapter_title = tex_escape_title(group)
            lines.extend([f"\\chapter{{{chapter_title}}}", ""])
            for rel in sorted(grouped[top][group]):
                parent = rel.parent
                exercise_dir = parent.name
                exercise_parent = parent.parent.as_posix()
                image_path = (parent / "images").as_posix()
                input_path = rel.as_posix()
                lines.extend(
                    [
                        f"% --- {input_path}",
                        f"\\renewcommand{{\\repExo}}{{{exercise_parent}}}",
                        f"\\renewcommand{{\\td}}{{{exercise_dir}}}",
                        f"\\graphicspath{{{{{image_path}/}}{{framework/images/}}}}",
                        "\\proffalse",
                        f"\\input{{{input_path}}}",
                        "",
                    ]
                )

    lines.extend(["\\backmatter", "\\printindex", "\\end{document}", ""])
    return "\n".join(lines)


def main() -> None:
    grouped = collect_exercises()
    exercises = [p for groups in grouped.values() for paths in groups.values() for p in paths]
    if not exercises:
        raise SystemExit("Aucun exercice contenant \\exer{...} n'a été trouvé.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_master(grouped), encoding="utf-8")

    manifest_lines = [
        f"Nombre total d'exercices : {len(exercises)}",
        f"Nombre de domaines : {len(grouped)}",
        "",
    ]
    for top in sorted(grouped):
        count = sum(len(paths) for paths in grouped[top].values())
        manifest_lines.append(f"{top}: {count} exercices")
        for group in sorted(grouped[top]):
            manifest_lines.append(f"  - {group}: {len(grouped[top][group])}")
    MANIFEST.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    print(f"Généré : {OUTPUT.relative_to(ROOT)} ({len(exercises)} exercices)")


if __name__ == "__main__":
    main()
