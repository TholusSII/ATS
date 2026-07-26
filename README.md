# Exercices de Sciences industrielles pour l'ingénieur

Ce dépôt regroupe les exercices provenant de
`xpessoles/PSI_ExercicesCompetences`, figés à la révision
`bf8b5cb7d16db996022c1647f22b2203943a922b`.

## Recueil global

Le document maître est :

```text
ALL_EXOS/ALL_EXOS.tex
```

`tools/generate_all_exos.py` génère automatiquement `ALL_EXOS/inputs.tex` :

- un chapitre par grand répertoire (`CIN`, `DYN`, `SLCI`, etc.) ;
- une section par sous-répertoire de compétence ;
- un sous-titre pour chaque exercice, repris de sa commande `\exer{...}`.

Le framework historique fourni dans `Style` est conservé. Le fichier
`Style/exercices_compat.tex` contient uniquement les adaptations nécessaires à
la compilation d'un ouvrage global avec une version récente de TeX Live.

## Compilation locale

```bash
python3 tools/patch_exercises.py
python3 tools/generate_all_exos.py
cd ALL_EXOS
latexmk -pdf -interaction=nonstopmode -halt-on-error ALL_EXOS.tex
```

Le workflow GitHub Actions `.github/workflows/import-and-build.yml` importe la
révision source figée, restaure le framework, génère la liste des exercices,
compile le PDF puis enregistre le résultat dans le dépôt.
