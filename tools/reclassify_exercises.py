#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "RECLASSEMENT_PROPOSITIONS.md"
EXPECTED = 468

CATEGORIES = {
    1: "1-Ingénierie système",
    2: "2-Modélisation des mécanismes",
    3: "3-Lois entrée sortie",
    4: "4-Cinématique",
    5: "5-Modélisation Systèmes Asservis",
    6: "6-Correction des Systèmes asservis",
    7: "7-Électronique",
    8: "8-Électromécanique",
    9: "9-MCC",
    10: "10-Électronique de Puissance",
    11: "11-Actions Mécaniques",
    12: "12-RDM",
    13: "13-MAS-MS",
    14: "14-Logique",
    15: "15-Outils numériques",
}
CATEGORY_ROOTS = set(CATEGORIES.values())
INFRA_ROOTS = {
    ".git", ".github", "ALL_EXOS", "FULL_PDF", "Style", "framework",
    "resources", "scripts", "tools", "xx_Figures",
}
OLD_EXERCISE_ROOTS = {
    "A_Integrer", "B2_ProposerModele", "C2_MettreEnOeuvreDemarche",
    "CIN", "COR", "DYN", "ELEC", "GEO", "NUM", "PERF", "PPM",
    "RDM", "SEQ", "SLCI", "STAT", "SYS", "TEC",
}
BEGIN_MARKER = "% BEGIN AUTO CORRIGE INCLUDE"
END_MARKER = "% END AUTO CORRIGE INCLUDE"


@dataclass
class Proposal:
    source: Path
    folder: Path
    category: int | None
    score: int
    gap: int
    reasons: list[str]
    alternatives: list[tuple[int, int]]


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = text.casefold().replace("œ", "oe")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def inspect_exercise(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if not relative.parts or relative.parts[0] in INFRA_ROOTS:
        return False
    if path.name == "corrige.tex" or path.name.endswith("_old.tex") or "_Colle_" in path.name:
        return False
    content = path.read_text(encoding="utf-8", errors="ignore")
    if r"\documentclass" in content:
        return False
    return r"\exer" in content or r"\subsection*" in content


def exercise_sources() -> list[Path]:
    sources = sorted(
        (path for path in ROOT.rglob("*.tex") if inspect_exercise(path)),
        key=lambda p: tuple(part.casefold() for part in p.relative_to(ROOT).parts),
    )
    if len(sources) != EXPECTED:
        raise SystemExit(f"Nombre d'exercices inattendu : {len(sources)} (attendu : {EXPECTED}).")
    return sources


def add(scores: dict[int, int], reasons: dict[int, list[str]], cat: int, points: int, why: str) -> None:
    scores[cat] += points
    reasons[cat].append(f"+{points} {why}")


def contains(text: str, *phrases: str) -> bool:
    return any(norm(phrase) in text for phrase in phrases)


def classify(source: Path) -> Proposal:
    relative = source.relative_to(ROOT)
    root = relative.parts[0]
    raw = source.read_text(encoding="utf-8", errors="ignore")
    sample = norm(relative.as_posix() + "\n" + raw[:24000])
    scores = {cat: 0 for cat in CATEGORIES}
    reasons = {cat: [] for cat in CATEGORIES}

    root_defaults = {
        "SYS": (1, 120), "GEO": (2, 120), "RDM": (12, 120),
        "SEQ": (14, 120), "NUM": (15, 120), "COR": (6, 115),
        "DYN": (11, 115), "STAT": (11, 115), "PERF": (6, 100),
        "SLCI": (5, 65), "CIN": (4, 60), "ELEC": (7, 45),
        "TEC": (3, 15),
    }
    if root in root_defaults:
        cat, points = root_defaults[root]
        add(scores, reasons, cat, points, f"racine historique {root}")

    rules: list[tuple[int, int, tuple[str, ...], str]] = [
        (1, 95, ("analyse fonctionnelle", "ingenierie systeme", "chaine fonctionnelle", "chaines fonctionnelles", "sysml", "diagramme des exigences", "diagramme de contexte", "cas d utilisation", "bdd", "ibd", "sadt", "fast", "pieuvre"), "ingénierie système"),
        (1, 60, ("exigence", "fonction principale", "matiere d oeuvre", "chaine d energie", "chaine d information"), "fonctions/exigences"),
        (2, 100, ("schema cinematique", "schemas cinematiques", "graphe de liaisons", "torseur cinematique", "fermeture geometrique", "parametrage", "hyperstatisme"), "modélisation mécanique forte"),
        (2, 70, ("liaison", "geometrie", "mobilite", "isostatique", "modele cinematique", "produit vectoriel"), "liaisons/géométrie"),
        (3, 105, ("loi entree sortie", "loi e s", "rapport de transmission", "rapport de reduction", "train epicycloidal", "roue et vis", "vis ecrou"), "loi entrée-sortie/transmission"),
        (3, 75, ("engrenage", "transmetteur", "poulie courroie", "poulie", "courroie", "reducteur", "transmission"), "transmetteur mécanique"),
        (4, 95, ("cinematique", "composition des vitesses", "torseur distributeur des vitesses", "rsg", "roulement sans glissement", "trapeze des vitesses"), "cinématique"),
        (4, 55, ("vitesse", "acceleration", "trajectoire", "loi horaire"), "vitesse/accélération"),
        (5, 90, ("schema bloc", "schema blocs", "fonction de transfert", "ftbo", "ftbf", "slci", "transformee de laplace", "identification temporelle"), "modélisation asservie"),
        (5, 70, ("bode", "premier ordre", "second ordre", "stabilite", "valeur finale"), "analyse des systèmes asservis"),
        (6, 125, ("correcteur", "correction des systemes", "correcteur pi", "correcteur pid", "correcteur p"), "correcteur"),
        (6, 95, ("marge de phase", "marge de gain", "marges graphiques", "precision", "erreur statique", "ecart statique"), "marges/précision"),
        (6, 65, ("rapidite", "temps de reponse", "depassement", "performances slci", "performances des systemes"), "performances asservies"),
        (7, 90, ("electronique", "amplificateur operationnel", "transistor", "diode", "filtre analogique", "circuit rlc", "circuit rc"), "électronique"),
        (7, 55, ("resistance", "condensateur", "loi des noeuds", "loi des mailles"), "circuit électrique"),
        (8, 100, ("electromecanique", "convertisseur electromecanique", "actionneur electromecanique"), "électromécanique"),
        (8, 60, ("couple moteur", "actionneur", "moteur electrique", "force contre electromotrice"), "actionneur électromécanique"),
        (9, 145, ("mcc", "moteur a courant continu", "machine a courant continu"), "MCC"),
        (10, 150, ("hacheur", "electronique de puissance", "onduleur", "redresseur", "pont en h", "convertisseur statique", "thyristor", "mli"), "électronique de puissance"),
        (11, 115, ("pfs", "principe fondamental de la statique", "actions mecaniques", "torseur statique", "pfd", "principe fondamental de la dynamique", "torseur dynamique", "theoreme de l energie cinetique"), "actions mécaniques"),
        (11, 75, ("statique", "dynamique", "energie cinetique", "moment cinetique", "inertie", "equilibre"), "statique/dynamique"),
        (11, 65, (" tec ", " tec"), "TEC"),
        (12, 140, ("rdm", "resistance des materiaux", "traction compression", "torsion", "flexion", "contrainte normale", "contrainte tangentielle"), "RDM"),
        (13, 155, ("machine asynchrone", "moteur asynchrone", "mas ", " mas"), "MAS"),
        (13, 150, ("machine synchrone", "moteur synchrone", "alternateur", " ms ", " ms"), "MS"),
        (14, 120, ("logique combinatoire", "logique sequentielle", "grafcet", "reseau de petri", "automate", "table de verite", "chronogramme"), "logique"),
        (14, 70, ("combinatoire", "sequentiel", "sequentielle", "reseau", "bascule", "compteur"), "séquentiel/réseaux"),
        (15, 135, ("methode d euler", "schema d euler", "integration numerique", "outils numeriques", "resolution numerique"), "outil numérique"),
        (15, 80, ("algorithme", "python", "dichotomie", "newton raphson", "interpolation", "equation differentielle", "discretisation"), "algorithme numérique"),
    ]
    for cat, points, phrases, why in rules:
        if contains(sample, *phrases):
            add(scores, reasons, cat, points, why)

    if contains(sample, "schema cinematique", "torseur cinematique", "parametrage"):
        scores[4] -= 35
    if contains(sample, "hyperstatisme"):
        scores[11] -= 35
    if contains(sample, "hacheur", "onduleur", "redresseur"):
        scores[7] -= 30
        scores[9] -= 20
    if contains(sample, "moteur a courant continu", "mcc"):
        scores[8] -= 20
        scores[7] -= 20
    if contains(sample, "machine asynchrone", "machine synchrone"):
        scores[8] -= 20
        scores[7] -= 20
    if contains(sample, "correcteur", "marge de phase", "marge de gain", "precision"):
        scores[5] -= 25

    ranking = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
    best_cat, best_score = ranking[0]
    second_score = ranking[1][1]
    gap = best_score - second_score

    direct_roots = {"SYS", "GEO", "RDM", "SEQ", "NUM", "COR", "DYN", "STAT"}
    threshold = 45
    min_gap = 8 if root in direct_roots else 15
    category = best_cat if best_score >= threshold and gap >= min_gap else None

    return Proposal(
        source=source,
        folder=source.parent,
        category=category,
        score=best_score,
        gap=gap,
        reasons=reasons[best_cat],
        alternatives=ranking[:3],
    )


def destination_for(proposal: Proposal) -> Path:
    assert proposal.category is not None
    relative_folder = proposal.folder.relative_to(ROOT)
    if relative_folder.parts[0] in CATEGORY_ROOTS:
        tail = Path(*relative_folder.parts[1:])
    else:
        tail = relative_folder
    return ROOT / CATEGORIES[proposal.category] / tail


def write_report(proposals: list[Proposal], applied: bool = False) -> None:
    counts = {cat: 0 for cat in CATEGORIES}
    unresolved = []
    for proposal in proposals:
        if proposal.category is None:
            unresolved.append(proposal)
        else:
            counts[proposal.category] += 1

    lines = [
        "# Proposition de reclassement des exercices",
        "",
        f"- Exercices analysés : **{len(proposals)}**",
        f"- Exercices classés automatiquement : **{len(proposals) - len(unresolved)}**",
        f"- Exercices à arbitrer : **{len(unresolved)}**",
        f"- Déplacements appliqués : **{'oui' if applied else 'non (classement à blanc)'}**",
        "",
        "## Répartition proposée",
        "",
    ]
    for cat, name in CATEGORIES.items():
        lines.append(f"- `{name}` : **{counts[cat]}** exercices")

    lines += ["", "## Exercices à arbitrer", ""]
    if not unresolved:
        lines.append("Aucun.")
    else:
        for proposal in unresolved:
            alternatives = ", ".join(
                f"{CATEGORIES[cat]} ({score})" for cat, score in proposal.alternatives
            )
            lines.append(
                f"- `{proposal.folder.relative_to(ROOT).as_posix()}` — propositions : {alternatives}"
            )

    lines += ["", "## Détail des classements automatiques", ""]
    for proposal in proposals:
        if proposal.category is None:
            continue
        destination = destination_for(proposal).relative_to(ROOT).as_posix()
        why = "; ".join(proposal.reasons[:4]) or "score lexical"
        lines.append(
            f"- `{proposal.folder.relative_to(ROOT).as_posix()}` → `{destination}` "
            f"(score {proposal.score}, écart {proposal.gap}; {why})"
        )
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def resolve_existing_path(old_parent: Path, raw_path: str) -> tuple[Path, bool] | None:
    if not raw_path or any(token in raw_path for token in ("\\", "#", "{", "}", "http://", "https://")):
        return None
    raw_path = raw_path.strip()
    candidate = (old_parent / raw_path).resolve()
    if candidate.exists():
        return candidate, False
    if Path(raw_path).suffix:
        return None
    for suffix in (".tex", ".png", ".jpg", ".jpeg", ".pdf", ".eps", ".svg"):
        extended = Path(str(candidate) + suffix)
        if extended.exists():
            return extended, True
    return None


def mapped_path(path: Path, directory_map: dict[Path, Path]) -> Path:
    for old_folder in sorted(directory_map, key=lambda p: len(p.parts), reverse=True):
        try:
            tail = path.relative_to(old_folder)
        except ValueError:
            continue
        return directory_map[old_folder] / tail
    return path


def rewrite_command_paths(text: str, old_file: Path, new_file: Path, directory_map: dict[Path, Path]) -> str:
    old_parent = old_file.parent
    new_parent = new_file.parent

    pattern = re.compile(r"(\\(?:includegraphics|input|include)(?:\[[^\]]*\])?\{)([^{}]+)(\})")

    def repl(match: re.Match[str]) -> str:
        raw = match.group(2)
        resolved = resolve_existing_path(old_parent, raw)
        if not resolved:
            return match.group(0)
        target, extension_was_added = resolved
        new_target = mapped_path(target, directory_map)
        replacement = os.path.relpath(new_target, new_parent).replace(os.sep, "/")
        if extension_was_added:
            replacement = str(Path(replacement).with_suffix(""))
        return match.group(1) + replacement + match.group(3)

    text = pattern.sub(repl, text)

    gpattern = re.compile(r"\\graphicspath\{((?:\{[^{}]*\})+)\}")

    def grepl(match: re.Match[str]) -> str:
        entries = re.findall(r"\{([^{}]*)\}", match.group(1))
        rewritten = []
        for raw in entries:
            resolved = resolve_existing_path(old_parent, raw.rstrip("/"))
            if resolved:
                target, _ = resolved
                new_target = mapped_path(target, directory_map)
                value = os.path.relpath(new_target, new_parent).replace(os.sep, "/") + "/"
            else:
                value = raw
            rewritten.append("{" + value + "}")
        return r"\graphicspath{" + "".join(rewritten) + "}"

    text = gpattern.sub(grepl, text)

    old_rel = old_file.relative_to(ROOT).as_posix()
    new_rel = new_file.relative_to(ROOT).as_posix()
    text = text.replace(f"% Source : {old_rel}", f"% Source : {new_rel}")
    return text


def apply_moves(proposals: list[Proposal]) -> None:
    unresolved = [proposal for proposal in proposals if proposal.category is None]
    if unresolved:
        raise SystemExit(
            f"{len(unresolved)} exercices restent à arbitrer. Le déplacement n'est pas appliqué."
        )

    directory_map = {proposal.folder.resolve(): destination_for(proposal).resolve() for proposal in proposals}
    destinations = list(directory_map.values())
    if len(set(destinations)) != len(destinations):
        raise SystemExit("Collision de destinations détectée.")
    for old, new in directory_map.items():
        if new.exists() and new != old:
            raise SystemExit(f"Destination déjà existante : {new.relative_to(ROOT)}")

    for old_folder, new_folder in directory_map.items():
        for old_file in old_folder.rglob("*"):
            if not old_file.is_file() or old_file.suffix.lower() not in {".tex", ".sty", ".cls", ".md"}:
                continue
            new_file = new_folder / old_file.relative_to(old_folder)
            text = old_file.read_text(encoding="utf-8", errors="ignore")
            rewritten = rewrite_command_paths(text, old_file, new_file, directory_map)
            if rewritten != text:
                old_file.write_text(rewritten, encoding="utf-8")

    for old_folder, new_folder in sorted(directory_map.items(), key=lambda item: len(item[0].parts), reverse=True):
        if old_folder == new_folder:
            continue
        new_folder.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old_folder), str(new_folder))

    for root_name in OLD_EXERCISE_ROOTS:
        root = ROOT / root_name
        if not root.exists():
            continue
        for directory in sorted((p for p in root.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
            try:
                directory.rmdir()
            except OSError:
                pass
        try:
            root.rmdir()
        except OSError:
            pass

    subprocess.run(["python3", str(ROOT / "tools/generate_all_exos.py")], cwd=ROOT, check=True)
    subprocess.run(["python3", str(ROOT / "tools/generate_all_corriges.py")], cwd=ROOT, check=True)

    sources = exercise_sources()
    corrections = [path for path in ROOT.rglob("corrige.tex") if path.relative_to(ROOT).parts[0] not in INFRA_ROOTS]
    if len(corrections) != EXPECTED:
        raise SystemExit(f"{len(corrections)} corrigés trouvés au lieu de {EXPECTED}.")
    inclusions = 0
    for source in sources:
        if r"\InclureCorrige{corrige.tex}" in source.read_text(encoding="utf-8", errors="ignore"):
            inclusions += 1
    if inclusions != EXPECTED:
        raise SystemExit(f"{inclusions} inclusions de corrigé au lieu de {EXPECTED}.")

    remaining_old = [name for name in OLD_EXERCISE_ROOTS if (ROOT / name).exists()]
    if remaining_old:
        raise SystemExit(f"Anciennes racines encore présentes : {remaining_old}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    proposals = [classify(source) for source in exercise_sources()]
    write_report(proposals, applied=False)
    if args.apply:
        apply_moves(proposals)
        final_proposals = [classify(source) for source in exercise_sources()]
        write_report(final_proposals, applied=True)
        print("Reclassement appliqué : 468 exercices, 468 corrigés, 15 racines pédagogiques.")
    else:
        unresolved = sum(proposal.category is None for proposal in proposals)
        print(f"Classement à blanc : {len(proposals) - unresolved} classés, {unresolved} à arbitrer.")


if __name__ == "__main__":
    main()
