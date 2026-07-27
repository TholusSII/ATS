#!/usr/bin/env python3
"""Restaure les ressources graphiques des exercices A_Integrer depuis la banque existante."""
from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
UPSTREAM = Path('/tmp/ExercicesCompetences')
MAPPING = REPO / 'tools' / 'a_integrer_candidate_map.json'
EXTENSIONS = ('.png', '.jpg', '.jpeg', '.pdf', '.eps', '.ps')
GRAPHICS = re.compile(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}')


def resource_files(root: Path):
    for path in root.rglob('*'):
        if path.is_file() and path.suffix.lower() not in {'.tex', '.aux', '.log'}:
            yield path


def main() -> None:
    mapping = json.loads(MAPPING.read_text(encoding='utf-8'))
    by_name: dict[str, list[Path]] = defaultdict(list)
    by_stem: dict[str, list[Path]] = defaultdict(list)
    for root in (REPO, UPSTREAM):
        for path in resource_files(root):
            if '.git' in path.parts or 'tools/vendor' in path.as_posix():
                continue
            by_name[path.name.lower()].append(path)
            by_stem[path.stem.lower()].append(path)

    resolved: list[tuple[str, str, str]] = []
    unresolved: list[tuple[str, str]] = []

    def score(path: Path, source: Path, preferred: Path | None) -> tuple[int, int, int]:
        source_tokens = set(re.findall(r'[a-z0-9]+', source.parent.as_posix().lower()))
        path_tokens = set(re.findall(r'[a-z0-9]+', path.as_posix().lower()))
        overlap = len(source_tokens & path_tokens)
        preferred_bonus = 0
        if preferred is not None:
            try:
                path.relative_to(preferred)
                preferred_bonus = 100
            except ValueError:
                pass
        repo_bonus = 5 if REPO in path.parents else 0
        return preferred_bonus, overlap, repo_bonus

    for source_rel, candidate_rel in mapping.items():
        source = REPO / source_rel
        if not source.exists():
            raise FileNotFoundError(source)
        candidate_dir = (REPO / candidate_rel).parent
        target_dir = source.parent

        if candidate_dir.exists():
            for item in resource_files(candidate_dir):
                rel = item.relative_to(candidate_dir)
                destination = target_dir / rel
                destination.parent.mkdir(parents=True, exist_ok=True)
                if not destination.exists():
                    shutil.copy2(item, destination)
                flat = target_dir / item.name
                if not flat.exists():
                    shutil.copy2(item, flat)

        text = source.read_text(encoding='utf-8', errors='ignore')
        for raw_ref in GRAPHICS.findall(text):
            ref = raw_ref.strip().replace('\\detokenize{', '').rstrip('}')
            if not ref or any(char in ref for char in ('#', '\\', '$')):
                continue
            requested = target_dir / ref
            existing = [requested] if requested.suffix else [requested.with_suffix(ext) for ext in EXTENSIONS]
            if any(path.exists() for path in existing):
                continue

            key_name = Path(ref).name.lower()
            key_stem = Path(ref).stem.lower()
            candidates = list(by_name.get(key_name, []))
            if not candidates:
                candidates = [p for p in by_stem.get(key_stem, []) if p.suffix.lower() in EXTENSIONS]
            if not candidates:
                unresolved.append((source_rel, ref))
                continue

            selected = max(candidates, key=lambda p: score(p, source, candidate_dir if candidate_dir.exists() else None))
            destination = requested if requested.suffix else requested.with_suffix(selected.suffix.lower())
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(selected, destination)
            selected_rel = selected.relative_to(REPO) if REPO in selected.parents else selected.relative_to(UPSTREAM)
            resolved.append((source_rel, ref, str(selected_rel)))

    report = [
        '# Restauration des illustrations', '',
        f'- Références restaurées automatiquement : **{len(resolved)}**',
        f'- Références restant sans ressource : **{len(unresolved)}**', ''
    ]
    if unresolved:
        report.extend(['## Références non résolues', ''])
        report.extend(f'- `{source}` : `{ref}`' for source, ref in unresolved)
    else:
        report.append('Toutes les références graphiques détectées disposent d’un fichier exploitable.')
    (REPO / 'IMAGE_RESOLUTION_REPORT.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
    print('\n'.join(report[:5]))


if __name__ == '__main__':
    main()
