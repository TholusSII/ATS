# Exercices de Sciences industrielles pour l'ingénieur

Ce dépôt regroupe les exercices provenant de
`xpessoles/PSI_ExercicesCompetences`, figés à la révision
`bf8b5cb7d16db996022c1647f22b2203943a922b`, correspondant au lot fourni dans
`DYN.zip`.

Le framework est synchronisé depuis `xpessoles/Style`, à la révision
`dcc5a8ac942668b246087cfd624ecadc8e17af6f`. Le fichier
`Style/exercices_compat.tex` contient uniquement les adaptations nécessaires à
la compilation d'un ouvrage global avec une version récente de TeX Live.

## Recueil global

Le document maître est :

```text
ALL_EXOS/ALL_EXOS.tex
```

`tools/generate_all_exos.py` génère automatiquement `ALL_EXOS/inputs.tex` pour
les 383 exercices :

- un chapitre par grand répertoire (`CIN`, `DYN`, `SLCI`, etc.) ;
- une section par sous-répertoire de compétence ;
- un sous-titre et une entrée de table des matières pour chaque exercice.

## Compilation locale

```bash
python3 tools/patch_exercises.py
python3 tools/generate_all_exos.py
cd ALL_EXOS
latexmk -pdf -interaction=nonstopmode -halt-on-error ALL_EXOS.tex
```

Le workflow GitHub Actions `.github/workflows/sync-and-build.yml` synchronise
les deux révisions figées, applique les correctifs minimaux, génère le fichier
maître, compile `ALL_EXOS.pdf`, publie le PDF comme artefact et enregistre le
résultat dans le dépôt.
