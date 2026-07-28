# Reprise de l’intégration des 85 exercices

## Relance du 28 juillet 2026

La source publique du bloc `A_Integrer` a été identifiée : `xpessoles/DevoirDuSoir`.
Le workflow ne reconstruit plus d’archive Base64 : il copie directement les 76 dossiers `DDS_*` depuis ce dépôt et les 9 autres exercices depuis `xpessoles/ExercicesCompetences`.

La branche reste en brouillon jusqu’à validation des contrôles suivants :

- 468 exercices ;
- 468 fichiers `corrige.tex` ;
- 468 inclusions `\InclureCorrige{corrige.tex}` ;
- aucun marqueur `\CorrigeACompleter` ;
- recueils maîtres régénérés pour 468 exercices et 468 corrigés.
