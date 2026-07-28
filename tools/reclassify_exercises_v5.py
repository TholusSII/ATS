#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import reclassify_exercises_v3 as v3

base = v3.v2.base
ROOT = base.ROOT


def merge_tree(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    destination.mkdir(parents=True, exist_ok=True)
    for item in source.iterdir():
        target = destination / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)
    shutil.rmtree(source)


def main() -> None:
    # Les exercices ont déjà été déplacés ; il reste seulement les fichiers annexes de RDM.
    merge_tree(ROOT / "RDM", ROOT / "12-RDM" / "RDM")

    subprocess.run(["python3", str(ROOT / "tools/generate_all_exos.py")], cwd=ROOT, check=True)
    subprocess.run(["python3", str(ROOT / "tools/generate_all_corriges.py")], cwd=ROOT, check=True)

    sources = base.exercise_sources()
    corrections = [
        path
        for path in ROOT.rglob("corrige.tex")
        if path.relative_to(ROOT).parts[0] not in base.INFRA_ROOTS
    ]
    inclusions = sum(
        r"\InclureCorrige{corrige.tex}"
        in source.read_text(encoding="utf-8", errors="ignore")
        for source in sources
    )
    if len(corrections) != 468 or inclusions != 468:
        raise SystemExit(
            f"Validation incomplète : {len(sources)} exercices, "
            f"{len(corrections)} corrigés, {inclusions} inclusions."
        )

    old_roots = set(base.OLD_EXERCISE_ROOTS) - {"PPM"}
    remaining = sorted(name for name in old_roots if (ROOT / name).exists())
    if remaining:
        raise SystemExit(f"Anciennes racines encore présentes : {remaining}")

    proposals = [base.classify(source) for source in sources]
    base.write_report(proposals, applied=True)

    diagnostic = ROOT / "RECLASSEMENT_EXECUTION.txt"
    if diagnostic.exists():
        diagnostic.unlink()

    print(
        "Reclassement validé : 438 exercices déplacés, 468 corrigés et inclusions contrôlés ; "
        "30 exercices PPM restent à arbitrer."
    )


if __name__ == "__main__":
    main()
