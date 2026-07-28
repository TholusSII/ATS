#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import reclassify_exercises as base


def contains(text: str, *phrases: str) -> bool:
    for phrase in phrases:
        probe = base.norm(phrase)
        if not probe:
            continue
        if " " not in probe and len(probe) <= 4:
            if re.search(rf"\b{re.escape(probe)}\b", text):
                return True
        elif probe in text:
            return True
    return False


def forced_category(relative: Path) -> int | None | str:
    rel = relative.as_posix()
    root = relative.parts[0]

    if root in base.CATEGORY_ROOTS:
        for cat, name in base.CATEGORIES.items():
            if root == name:
                return cat

    # Représentation 2D / lecture de plans : aucun dossier demandé ne correspond exactement.
    if root == "PPM":
        return "unresolved"

    direct = {
        "SYS": 1,
        "GEO": 2,
        "RDM": 12,
        "SEQ": 14,
        "NUM": 15,
        "COR": 6,
        "DYN": 11,
        "STAT": 11,
        "TEC": 11,
    }
    if root in direct:
        return direct[root]

    if root == "CIN":
        if len(relative.parts) > 1 and "CIN-01" in relative.parts[1]:
            return 2
        if len(relative.parts) > 1 and "CIN-02" in relative.parts[1]:
            return 4
        if len(relative.parts) > 1 and "CIN-03" in relative.parts[1]:
            return 3

    if root == "SLCI":
        reln = base.norm(rel)
        if any(word in reln for word in ("correct", "precision", "marge", "performance")):
            return 6
        return 5

    if root == "PERF":
        return 6

    if root == "ELEC":
        reln = base.norm(rel)
        if contains(reln, "hacheur", "onduleur", "redresseur", "electronique de puissance", "pont en h"):
            return 10
        if contains(reln, "mcc", "moteur a courant continu", "machine a courant continu"):
            return 9
        if contains(
            reln,
            "mas",
            "machine asynchrone",
            "moteur asynchrone",
            "ms",
            "machine synchrone",
            "moteur synchrone",
        ):
            return 13
        if contains(reln, "electromecanique", "actionneur", "convertisseur electromecanique"):
            return 8
        return 7

    if root == "A_Integrer":
        name = base.norm(relative.parent.name)
        if name == "011 is":
            return "unresolved"
        if contains(
            name,
            "produit vectoriel",
            "derivation vectorielle",
            "geometrie",
            "schema cinematique",
            "cinematique schema",
            "modelisation geometrie",
            "qcm liaisons",
            "chs leq",
        ):
            return 2
        if contains(name, "cinematique"):
            return 4
        if contains(
            name,
            "pfs",
            "statique",
            "statiques am",
            "pfd",
            "inertie",
            "torseurs dyn",
            "tec",
            "hyperstatisme",
        ):
            return 11
        if contains(name, "correcteur", "marges graphiques", "slci pi", "slci p"):
            return 6
        if contains(
            name,
            "ftbo",
            "ftbf",
            "bode",
            "slci",
            "valeur finale",
            "identification temporelle",
            "calcul complexes",
            "modelisation schema blocs",
        ):
            return 5

    if root == "B2_ProposerModele":
        reln = base.norm(rel)
        if contains(reln, "hyperstatisme", "liaison", "schema cinematique", "parametrage", "geometrie"):
            return 2

    if root == "C2_MettreEnOeuvreDemarche":
        reln = base.norm(rel)
        if contains(reln, "pfs", "statique", "pfd", "dynamique", "tec"):
            return 11

    return None


original_classify = base.classify


def classify(source: Path) -> base.Proposal:
    relative = source.relative_to(base.ROOT)
    forced = forced_category(relative)
    if forced == "unresolved":
        return base.Proposal(
            source,
            source.parent,
            None,
            0,
            0,
            ["arbitrage pédagogique requis"],
            [(1, 0), (2, 0), (3, 0)],
        )
    if isinstance(forced, int):
        return base.Proposal(
            source,
            source.parent,
            forced,
            1000,
            1000,
            ["règle de classement explicite"],
            [(forced, 1000)],
        )
    return original_classify(source)


base.contains = contains
base.classify = classify

if __name__ == "__main__":
    base.main()
