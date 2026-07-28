#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORY_RE = re.compile(r"^(?:0[1-9]|1[0-5])-")
EXPECTED = 468
MD_OUTPUT = ROOT / "ARBORESCENCE_EXERCICES.md"
CSV_OUTPUT = ROOT / "RECLASSEMENT_EXERCICES.csv"


def exercise_directories() -> list[Path]:
    directories: list[Path] = []
    for correction in ROOT.rglob("corrige.tex"):
        relative = correction.relative_to(ROOT)
        if not relative.parts or not CATEGORY_RE.match(relative.parts[0]):
            continue
        folder = correction.parent
        source = folder / f"{folder.name}.tex"
        if source.exists():
            directories.append(folder.relative_to(ROOT))
    directories = sorted(set(directories), key=lambda p: tuple(x.casefold() for x in p.parts))
    if len(directories) != EXPECTED:
        raise SystemExit(f"{len(directories)} exercices trouvés au lieu de {EXPECTED}")
    return directories


def build_tree(paths: list[Path]) -> dict:
    root: dict = {}
    for path in paths:
        node = root
        for part in path.parts:
            node = node.setdefault(part, {})
    return root


def render_tree(node: dict, prefix: str = "") -> list[str]:
    lines: list[str] = []
    items = list(node.items())
    for index, (name, children) in enumerate(items):
        last = index == len(items) - 1
        connector = "└── " if last else "├── "
        lines.append(prefix + connector + name)
        if children:
            extension = "    " if last else "│   "
            lines.extend(render_tree(children, prefix + extension))
    return lines


def write_markdown(paths: list[Path]) -> None:
    tree = build_tree(paths)
    lines = [
        "# Arborescence des 468 exercices",
        "",
        "Ce document liste uniquement les dossiers d'exercices, sans détailler les images, le fichier source et le corrigé contenus dans chaque dossier.",
        "",
        "## Comment m'indiquer les modifications",
        "",
        "Tu peux me renvoyer une ou plusieurs lignes sous cette forme :",
        "",
        "```text",
        '"02-Modélisation des mécanismes/CIN/CIN-01/.../NomExercice" -> "03-Lois entrée sortie/Transmetteurs/NomExercice"',
        "```",
        "",
        "Cette syntaxe permet à la fois de déplacer et de renommer un dossier. Le chemin à droite est toujours le chemin final souhaité.",
        "",
        "Pour déplacer plusieurs exercices dans le même dossier, indique une ligne par exercice. Pour déplacer un dossier intermédiaire complet, indique le chemin de ce dossier : tous ses sous-dossiers suivront.",
        "",
        "Tu peux aussi remplir la colonne `nouveau_chemin` du fichier `RECLASSEMENT_EXERCICES.csv` et me renvoyer seulement les lignes modifiées.",
        "",
        "## Arborescence actuelle",
        "",
        "```text",
        *render_tree(tree),
        "```",
        "",
    ]
    MD_OUTPUT.write_text("\n".join(lines), encoding="utf-8")


def write_csv(paths: list[Path]) -> None:
    with CSV_OUTPUT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream, delimiter=";")
        writer.writerow(["chemin_actuel", "nouveau_chemin"])
        for path in paths:
            writer.writerow([path.as_posix(), ""])


def main() -> None:
    paths = exercise_directories()
    write_markdown(paths)
    write_csv(paths)
    print(f"Arborescence générée pour {len(paths)} exercices.")


if __name__ == "__main__":
    main()
