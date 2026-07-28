#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import tempfile

from integrate_new_exercises import A_FOLDERS, OTHER_FOLDERS, ROOT

EXERCISES_REPO = "https://github.com/xpessoles/ExercicesCompetences.git"
EXERCISES_COMMIT = "5cb4eced77ae479b10715249c87afbba183d26e4"
DDS_REPO = "https://github.com/xpessoles/DevoirDuSoir.git"
DDS_COMMIT = "d2ac417d1bbb6e02e507e6e475bb16bb81517f34"


def clone_at(url: str, commit: str, destination: Path) -> None:
    subprocess.run(
        ["git", "clone", "--filter=blob:none", "--no-checkout", url, str(destination)],
        check=True,
    )
    subprocess.run(["git", "-C", str(destination), "checkout", commit], check=True)


def resolve_dds_source(root: Path, target_relative: str) -> Path:
    relative = Path(target_relative).relative_to("A_Integrer")
    exact = root / relative
    if exact.is_dir():
        return exact

    parent = root / relative.parent
    number = relative.name.split("_", 1)[0]
    candidates = (
        sorted(path for path in parent.glob(f"{number}_*") if path.is_dir())
        if parent.is_dir()
        else []
    )
    if len(candidates) == 1:
        return candidates[0]

    candidates = sorted({path.parent for path in root.rglob(f"{relative.name}.tex")})
    if len(candidates) == 1:
        return candidates[0]
    raise SystemExit(
        f"Source DevoirDuSoir introuvable ou ambiguë pour {target_relative}: {candidates}"
    )


def copy_exercise(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)

    expected = target / f"{target.name}.tex"
    original = target / f"{source.name}.tex"
    if not expected.exists() and original.exists():
        original.rename(expected)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="integration-85-") as temporary:
        temporary_root = Path(temporary)
        exercises = temporary_root / "ExercicesCompetences"
        dds = temporary_root / "DevoirDuSoir"
        clone_at(EXERCISES_REPO, EXERCISES_COMMIT, exercises)
        clone_at(DDS_REPO, DDS_COMMIT, dds)

        for relative in OTHER_FOLDERS:
            source = exercises / relative
            if not source.is_dir():
                raise SystemExit(f"Source publique absente : {relative}")
            copy_exercise(source, ROOT / relative)

        for relative in A_FOLDERS:
            copy_exercise(resolve_dds_source(dds, relative), ROOT / relative)

    print(f"{len(A_FOLDERS) + len(OTHER_FOLDERS)} dossiers sources matérialisés.")


if __name__ == "__main__":
    main()
