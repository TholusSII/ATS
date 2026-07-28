#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

TITLES = {
    1: "Ingénierie système",
    2: "Modélisation des mécanismes",
    3: "Lois entrée sortie",
    4: "Cinématique",
    5: "Modélisation Systèmes Asservis",
    6: "Correction des Systèmes asservis",
    7: "Électronique",
    8: "Électromécanique",
    9: "MCC",
}
MAPPING = {f"{number}-{title}": f"{number:02d}-{title}" for number, title in TITLES.items()}
EXCLUDED_TOP_LEVEL = {
    ".git", ".github", "ALL_EXOS", "FULL_PDF", "Style", "framework",
    "resources", "scripts", "tools", "xx_Figures",
}


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, check=True, text=True, capture_output=True)


def tracked_files() -> list[Path]:
    data = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    ).stdout
    return [ROOT / raw.decode("utf-8") for raw in data.split(b"\0") if raw]


def rename_roots() -> None:
    for old, new in MAPPING.items():
        old_path = ROOT / old
        new_path = ROOT / new
        if old_path.exists() and new_path.exists():
            raise SystemExit(f"Les deux dossiers existent déjà : {old} et {new}")
        if old_path.exists():
            subprocess.run(["git", "mv", old, new], cwd=ROOT, check=True)
        elif not new_path.exists():
            raise SystemExit(f"Dossier attendu absent : {old}")


def replace_category_names(text: str) -> str:
    updated = text
    for old, new in MAPPING.items():
        updated = re.sub(rf"(?<!\d){re.escape(old)}", new, updated)
    return updated


def update_text_references() -> int:
    changed = 0
    for path in tracked_files():
        if not path.is_file():
            continue
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        if b"\0" in raw:
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        updated = replace_category_names(text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def exercise_sources() -> list[Path]:
    sources: list[Path] = []
    for path in ROOT.rglob("*.tex"):
        relative = path.relative_to(ROOT)
        if not relative.parts or relative.parts[0] in EXCLUDED_TOP_LEVEL:
            continue
        if len(relative.parts) < 4 or path.name == "corrige.tex":
            continue
        if path.name.endswith("_old.tex") or "_Colle_" in path.name:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if r"\documentclass" in text:
            continue
        if r"\exer" in text or r"\subsection*" in text:
            sources.append(path)
    return sorted(sources)


def validate() -> None:
    for old, new in MAPPING.items():
        if (ROOT / old).exists():
            raise SystemExit(f"Ancien dossier encore présent : {old}")
        if not (ROOT / new).is_dir():
            raise SystemExit(f"Nouveau dossier absent : {new}")

    sources = exercise_sources()
    corrections = [
        path for path in ROOT.rglob("corrige.tex")
        if path.relative_to(ROOT).parts[0] not in EXCLUDED_TOP_LEVEL
    ]
    inclusions = sum(
        r"\InclureCorrige{corrige.tex}" in source.read_text(encoding="utf-8", errors="ignore")
        for source in sources
    )
    if (len(sources), len(corrections), inclusions) != (468, 468, 468):
        raise SystemExit(
            f"Validation incomplète : {len(sources)} exercices, "
            f"{len(corrections)} corrigés, {inclusions} inclusions."
        )

    for generated in (ROOT / "ALL_EXOS/inputs.tex", ROOT / "ALL_EXOS/corriges_inputs.tex"):
        text = generated.read_text(encoding="utf-8")
        for old in MAPPING:
            forbidden = (f"../{old}/", rf"\chapter{{{old}}}")
            if any(token in text for token in forbidden):
                raise SystemExit(f"Ancienne référence dans {generated.relative_to(ROOT)} : {old}")
        for new in MAPPING.values():
            required = (f"../{new}/", rf"\chapter{{{new}}}")
            if not all(token in text for token in required):
                raise SystemExit(f"Nouvelle référence absente de {generated.relative_to(ROOT)} : {new}")


def main() -> None:
    rename_roots()
    changed = update_text_references()
    run("python3", "tools/generate_all_exos.py")
    run("python3", "tools/generate_all_corriges.py")
    validate()
    diagnostic = ROOT / "PREFIX_RENAME_EXECUTION.txt"
    if diagnostic.exists():
        diagnostic.unlink()
    print(
        "Renommage validé : 01 à 09, 468 exercices, 468 corrigés, "
        f"468 inclusions ; {changed} fichiers texte mis à jour."
    )


if __name__ == "__main__":
    main()
