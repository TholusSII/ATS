#!/usr/bin/env python3
from __future__ import annotations

import base64
import csv
import lzma
import re
import shutil
import subprocess
from collections import Counter
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "RECLASSEMENT_EXERCICES.csv"
PACKED_CSV = ROOT / "tools/vendor/reclassement_exercices.csv.xz.b64"
STAGING = ROOT / ".reclassement_staging"
EXPECTED = 468
EXCLUDED_TOP_LEVEL = {
    ".git", ".github", "ALL_EXOS", "FULL_PDF", "Style", "framework",
    "resources", "scripts", "tools", "xx_Figures",
}


def git(*args: str) -> None:
    subprocess.run(["git", *args], cwd=ROOT, check=True)


def normalize(raw: str, field: str, line: int) -> str:
    value = raw.strip().replace("\\", "/")
    path = PurePosixPath(value)
    if not value or value.startswith("/") or ".." in path.parts or "." in path.parts:
        raise SystemExit(f"Ligne {line}: {field} invalide: {raw!r}")
    if any(not part.strip() for part in path.parts):
        raise SystemExit(f"Ligne {line}: segment vide dans {field}: {raw!r}")
    return path.as_posix().rstrip("/")


def load_rows() -> list[tuple[int, str, str]]:
    if not CSV_PATH.exists():
        if not PACKED_CSV.is_file():
            raise SystemExit("Fichier de reclassement absent")
        packed = base64.b64decode("".join(PACKED_CSV.read_text(encoding="ascii").split()))
        CSV_PATH.write_bytes(lzma.decompress(packed))
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        if reader.fieldnames != ["chemin_actuel", "nouveau_chemin"]:
            raise SystemExit(f"En-têtes CSV inattendus: {reader.fieldnames}")
        rows = [
            (
                line,
                normalize(row.get("chemin_actuel", ""), "chemin_actuel", line),
                normalize(row.get("nouveau_chemin", ""), "nouveau_chemin", line),
            )
            for line, row in enumerate(reader, start=2)
        ]
    if len(rows) != EXPECTED:
        raise SystemExit(f"{len(rows)} lignes trouvées au lieu de {EXPECTED}")
    old_counts = Counter(old for _, old, _ in rows)
    new_counts = Counter(new for _, _, new in rows)
    duplicate_old = [path for path, count in old_counts.items() if count > 1]
    duplicate_new = [path for path, count in new_counts.items() if count > 1]
    if duplicate_old:
        raise SystemExit(f"Chemins actuels dupliqués: {duplicate_old}")
    if duplicate_new:
        raise SystemExit(f"Destinations dupliquées: {duplicate_new}")
    return rows


def detect_source(folder: Path, expected_name: str) -> Path:
    expected = folder / f"{expected_name}.tex"
    if expected.is_file():
        return expected
    candidates: list[Path] = []
    for path in folder.glob("*.tex"):
        if path.name == "corrige.tex" or path.name.endswith("_old.tex") or "_Colle_" in path.name:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if r"\documentclass" not in text and (r"\exer" in text or r"\subsection*" in text):
            candidates.append(path)
    if len(candidates) != 1:
        raise SystemExit(f"Source principale ambiguë dans {folder.relative_to(ROOT)}: {candidates}")
    return candidates[0]


def validate_sources(rows: list[tuple[int, str, str]]) -> None:
    old_set = {old for _, old, _ in rows}
    for line, old, new in rows:
        source = ROOT / old
        if not source.is_dir():
            raise SystemExit(f"Ligne {line}: dossier source absent: {old}")
        detect_source(source, source.name)
        if not (source / "corrige.tex").is_file():
            raise SystemExit(f"Ligne {line}: corrige.tex absent: {old}")
        destination = ROOT / new
        if old != new and destination.exists() and new not in old_set:
            raise SystemExit(f"Ligne {line}: destination déjà existante: {new}")


def stage_and_move(rows: list[tuple[int, str, str]]) -> int:
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir()
    changed = [(index, old, new) for index, (_, old, new) in enumerate(rows, start=1) if old != new]

    for index, old, _new in changed:
        stage = STAGING / f"{index:04d}"
        git("mv", "--", old, stage.relative_to(ROOT).as_posix())

    for index, old, new in changed:
        stage = STAGING / f"{index:04d}"
        destination = ROOT / new
        destination.parent.mkdir(parents=True, exist_ok=True)
        git("mv", "--", stage.relative_to(ROOT).as_posix(), destination.relative_to(ROOT).as_posix())

        old_name = PurePosixPath(old).name
        new_name = PurePosixPath(new).name
        main_source = detect_source(destination, old_name)
        target_source = destination / f"{new_name}.tex"
        if main_source != target_source:
            if target_source.exists():
                raise SystemExit(f"Fichier cible déjà présent: {target_source.relative_to(ROOT)}")
            git("mv", "--", main_source.relative_to(ROOT).as_posix(), target_source.relative_to(ROOT).as_posix())

        for item in sorted(destination.iterdir()):
            if not item.is_file() or item == target_source or item.name == "corrige.tex":
                continue
            if item.stem == old_name:
                renamed = item.with_name(new_name + item.suffix)
                if renamed.exists():
                    raise SystemExit(f"Collision lors du renommage: {renamed.relative_to(ROOT)}")
                git("mv", "--", item.relative_to(ROOT).as_posix(), renamed.relative_to(ROOT).as_posix())

    shutil.rmtree(STAGING)
    return len(changed)


def tracked_text_files() -> list[Path]:
    raw = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    ).stdout
    return [ROOT / item.decode("utf-8") for item in raw.split(b"\0") if item]


def update_references(rows: list[tuple[int, str, str]]) -> int:
    replacements = [(old, new) for _, old, new in rows if old != new]
    replacements.sort(key=lambda pair: len(pair[0]), reverse=True)
    changed = 0
    for path in tracked_text_files():
        if not path.is_file() or path == CSV_PATH:
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
        updated = text
        for old, new in replacements:
            updated = updated.replace(old, new)
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
        if len(relative.parts) < 2 or path.name == "corrige.tex":
            continue
        if path.name.endswith("_old.tex") or "_Colle_" in path.name:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if r"\documentclass" in text:
            continue
        if r"\exer" in text or r"\subsection*" in text:
            sources.append(path)
    return sorted(sources)


def validate_final(rows: list[tuple[int, str, str]]) -> tuple[int, int, int]:
    for line, old, new in rows:
        destination = ROOT / new
        if not destination.is_dir():
            raise SystemExit(f"Ligne {line}: destination absente après déplacement: {new}")
        expected_source = destination / f"{destination.name}.tex"
        if not expected_source.is_file():
            raise SystemExit(f"Ligne {line}: source renommée absente: {expected_source.relative_to(ROOT)}")
        if not (destination / "corrige.tex").is_file():
            raise SystemExit(f"Ligne {line}: corrigé absent après déplacement: {new}")
        if old != new and (ROOT / old).exists():
            raise SystemExit(f"Ligne {line}: ancien chemin encore présent: {old}")

    sources = exercise_sources()
    corrections = [
        path for path in ROOT.rglob("corrige.tex")
        if path.relative_to(ROOT).parts[0] not in EXCLUDED_TOP_LEVEL
    ]
    inclusions = sum(
        r"\InclureCorrige{corrige.tex}" in path.read_text(encoding="utf-8", errors="ignore")
        for path in sources
    )
    counts = (len(sources), len(corrections), inclusions)
    if counts != (EXPECTED, EXPECTED, EXPECTED):
        raise SystemExit(
            f"Validation incomplète: {counts[0]} exercices, {counts[1]} corrigés, {counts[2]} inclusions"
        )
    return counts


def write_report(rows: list[tuple[int, str, str]], moved: int, updated_files: int) -> None:
    distribution = Counter(new.split("/", 1)[0] for _, _, new in rows)
    lines = [
        "# Reclassement CSV appliqué",
        "",
        f"- Lignes traitées : **{len(rows)}**",
        f"- Dossiers déplacés ou renommés : **{moved}**",
        f"- Dossiers inchangés : **{len(rows) - moved}**",
        f"- Fichiers texte dont les références ont été actualisées : **{updated_files}**",
        "- Contrôle final : **468 exercices, 468 corrigés, 468 inclusions**",
        "",
        "## Répartition finale",
        "",
    ]
    lines.extend(f"- `{root}` : **{count}**" for root, count in sorted(distribution.items()))
    lines.extend([
        "",
        "## Collision résolue",
        "",
        "Le second exercice `PPM-02/1000_Dessin2D` est classé sous le nom "
        "`02-Modélisation des mécanismes/TD/Dessin2D/1000_Dessin2D_PPM02` afin de préserver les deux dossiers.",
        "",
    ])
    (ROOT / "RECLASSEMENT_APPLIQUE.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    rows = load_rows()
    validate_sources(rows)
    moved = stage_and_move(rows)
    updated_files = update_references(rows)
    subprocess.run(["python3", "tools/generate_all_exos.py"], cwd=ROOT, check=True)
    subprocess.run(["python3", "tools/generate_all_corriges.py"], cwd=ROOT, check=True)
    validate_final(rows)
    write_report(rows, moved, updated_files)
    print(f"Reclassement validé: {moved} déplacements, 468 exercices et corrigés.")


if __name__ == "__main__":
    main()
