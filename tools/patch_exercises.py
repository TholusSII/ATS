#!/usr/bin/env python3
"""Applique les deux corrections minimales requises par les sources d'origine."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch_missing_rdm_image() -> None:
    path = ROOT / "RDM/RDM-05-Deformation/541_RdM/541_RdM.tex"
    text = path.read_text(encoding="utf-8")
    old = r"\includegraphics[width=.8\linewidth]{540}"
    new = r"\includegraphics[width=.8\linewidth]{541_RdM}"
    if old in text:
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        print(f"Corrigé : {path.relative_to(ROOT)} (nom de l'image).")
    elif new not in text:
        raise SystemExit(f"Motif d'image inattendu dans {path.relative_to(ROOT)}")


def patch_unclosed_professional_mode() -> None:
    path = ROOT / "SLCI/SLCI-03-SchemaBlocs/96_Stabilisateur/96_Stabilisateur.tex"
    text = path.read_text(encoding="utf-8")
    opened = text.count(r"\ifprof") + text.count(r"\ifcorrection")
    closed = text.count(r"\fi")
    if opened == closed + 1:
        path.write_text(text.rstrip() + "\n\\fi\n", encoding="utf-8")
        print(f"Corrigé : {path.relative_to(ROOT)} (condition fermée).")
    elif opened != closed:
        raise SystemExit(
            f"Structure conditionnelle inattendue dans {path.relative_to(ROOT)} : "
            f"{opened} ouvertures, {closed} fermetures."
        )


def main() -> None:
    patch_missing_rdm_image()
    patch_unclosed_professional_mode()


if __name__ == "__main__":
    main()
