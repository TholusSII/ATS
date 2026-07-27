# Reprise de l’intégration des 85 exercices

## État sauvegardé — 27 juillet 2026

- Dépôt : `TholusSII/Exercices`
- Branche de travail : `agent/materialiser-85-exercices-final`
- Pull request : `#8` — **brouillon, ouverte, ne pas fusionner en l’état**
- Branche cible : `main`
- État actuel de `main` : **383 exercices / 383 corrigés**
- Objectif : **468 exercices / 468 corrigés**

## Travail déjà préparé

- Liste des 85 exercices absents déterminée :
  - 76 exercices du bloc `A_Integrer` provenant du ZIP fourni ;
  - 9 exercices récupérables depuis la banque publique `xpessoles/ExercicesCompetences`.
- Workflow de restauration des ressources préparé.
- Générateurs de corrigés et des recueils maîtres déjà adaptés pour viser 468 exercices.
- Branche et pull request de matérialisation créées.

## Blocage actuel

Le workflow échoue avant l’extraction des 76 exercices `A_Integrer`, lors de la reconstruction de l’archive Base64/XZ. Les fragments transférés par l’API GitHub ont été redécoupés plusieurs fois et présentent un problème de jonction ou de duplication. Aucun contrôle `468/468` n’a donc encore réussi.

Les 85 dossiers ne doivent pas être considérés comme intégrés tant que les assertions ci-dessous ne passent pas.

## Reprise recommandée

Ne pas poursuivre le transfert fragment par fragment. Repartir du ZIP original dans une session disposant du fichier, puis :

1. extraire directement les 76 dossiers `A_Integrer` absents ;
2. copier les 9 dossiers complets depuis la révision publique prévue ;
3. ajouter ou conserver `corrige.tex` et `\\InclureCorrige{corrige.tex}` dans chaque exercice ;
4. exécuter :
   - `python3 tools/generate_corrections.py`
   - `python3 tools/generate_all_exos.py`
   - `python3 tools/generate_all_corriges.py`
5. vérifier impérativement :
   - `find . -type f -name corrige.tex | wc -l` → `468` ;
   - 468 sources contenant `\\InclureCorrige{corrige.tex}` ;
   - aucune occurrence de `\\CorrigeACompleter` ;
   - `CORRECTIONS_REPORT.md` indiquant 468 exercices et 0 corrigé partiel ;
   - `ALL_EXOS/inputs.tex` indiquant 468 exercices ;
   - `ALL_EXOS/corriges_inputs.tex` indiquant 468 corrigés ;
6. pousser l’arborescence matérialisée sur `agent/materialiser-85-exercices-final` ;
7. seulement après validation, passer la PR #8 hors brouillon et la fusionner.

## Important

Le travail validé antérieur — les 383 exercices et leurs corrigés — reste présent sur `main`. La PR #8 est volontairement laissée ouverte en brouillon pour conserver le point de reprise sans compromettre le dépôt principal.
