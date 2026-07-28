#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import reclassify_exercises_v3 as v3

base = v3.v2.base
ROOT = base.ROOT


def main() -> None:
    source = ROOT / "PPM"
    destination = ROOT / "02-Modélisation des mécanismes" / "PPM"

    if source.exists():
        if destination.exists():
            raise SystemExit(f"Destination déjà présente : {destination.relative_to(ROOT)}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(destination))
    elif not destination.exists():
        raise SystemExit("Le dossier PPM est introuvable à la source comme à la destination.")

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
        in exercise.read_text(encoding="utf-8", errors="ignore")
        for exercise in sources
    )

    if len(sources) != 468 or len(corrections) != 468 or inclusions != 468:
        raise SystemExit(
            f"Validation incomplète : {len(sources)} exercices, "
            f"{len(corrections)} corrigés, {inclusions} inclusions."
        )

    remaining = sorted(name for name in base.OLD_EXERCISE_ROOTS if (ROOT / name).exists())
    if remaining:
        raise SystemExit(f"Anciennes racines encore présentes : {remaining}")

    proposals = [base.classify(exercise) for exercise in sources]
    unresolved = [proposal for proposal in proposals if proposal.category is None]
    if unresolved:
        raise SystemExit(f"Exercices encore non classés : {len(unresolved)}")
    base.write_report(proposals, applied=True)

    diagnostic = ROOT / "RECLASSEMENT_EXECUTION.txt"
    if diagnostic.exists():
        diagnostic.unlink()

    print(
        "Reclassement complet validé : les 30 exercices PPM ont été déplacés dans "
        "02-Modélisation des mécanismes ; 468 exercices, 468 corrigés et 468 inclusions contrôlés."
    )


if __name__ == "__main__":
    main()
