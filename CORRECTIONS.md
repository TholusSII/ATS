# Corrigés des exercices

Chaque répertoire d’exercice contient un fichier `corrige.tex`. Le fichier principal de l’exercice appelle ce corrigé avec :

```tex
\InclureCorrige{corrige.tex}
```

L’affichage est piloté par une seule commande du framework `Style/exercices_compat.tex` :

```tex
\AfficherCorriges   % affiche les corrigés dans une box verte
\MasquerCorriges    % masque tous les corrigés
```

Deux fichiers maîtres sont disponibles :

- `ALL_EXOS/ALL_EXOS.tex` compile les énoncés seuls ;
- `ALL_EXOS/ALL_EXOS_CORRIGE.tex` compile les énoncés suivis des corrigés.

Le script `tools/generate_corrections.py` :

1. extrait les réponses déjà présentes dans les branches professeur ou correction ;
2. consolide uniquement les réponses de questions identiques appartenant à un exercice homonyme ;
3. crée un fichier `corrige.tex` pour chacun des 383 exercices ;
4. signale explicitement les réponses absentes ou partielles dans `CORRECTIONS_REPORT.md`.

Les fichiers marqués **Corrigé à rédiger** sont volontairement identifiés comme non validés : aucun résultat n’est inventé automatiquement.
