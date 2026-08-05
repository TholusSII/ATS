from pathlib import Path

# Générateur des posters et cartes mentales des cours 01 à 05.
# Le cours 05 possède désormais un poster et une carte mentale dessinés à la
# main en TikZ. Ils ne doivent pas être remplacés par les gabarits génériques.
HANDCRAFTED = {"05"}

COURSES = [
    ("01", "Analyse fonctionnelle", "Notations_AF/Notations_AF.sty", [
        ("Besoin", "Identifier le besoin, les utilisateurs, le contexte et la finalité du système."),
        ("Exigences", "Décrire les fonctions de service, les contraintes, les critères et les niveaux attendus."),
        ("SysML", "Exploiter les diagrammes de contexte, exigences, cas d'utilisation et blocs."),
        ("Méthode", "Passer du besoin au cahier des charges puis vérifier la satisfaction des exigences.")]),
    ("02", "Modélisation des mécanismes", "TLCinematique.sty", [
        ("Solides et liaisons", "Définir les classes d'équivalence cinématique et les liaisons entre solides."),
        ("Représentations", "Construire graphe de liaisons, schéma cinématique et paramétrage géométrique."),
        ("Mobilité", "Analyser les degrés de liberté, les chaînes fermées et les mouvements possibles."),
        ("Méthode", "Isoler les solides, identifier les contacts puis choisir une modélisation adaptée.")]),
    ("03", "Lois entrée-sortie", "TLLoisEntreeSortie.sty", [
        ("Objectif", "Relier le mouvement d'entrée au mouvement de sortie d'un mécanisme."),
        ("Fermeture géométrique", "Écrire les relations vectorielles ou scalaires issues d'une chaîne fermée."),
        ("Fermeture cinématique", "Composer les torseurs cinématiques et projeter sur des directions pertinentes."),
        ("Résultat", "Obtenir une loi géométrique, cinématique ou un rapport de transmission.")]),
    ("04", "Modélisation des transmetteurs", "TLTransmetteurs.sty", [
        ("Fonction", "Adapter vitesse, couple, effort ou mouvement dans une chaîne d'énergie."),
        ("Transmetteurs", "Engrenages, poulies-courroies, chaînes, vis-écrou et trains épicycloïdaux."),
        ("Rapports", "Déterminer le rapport de transmission avec une convention de signe cohérente."),
        ("Puissance", "Relier efforts et vitesses en tenant compte du rendement et de la réversibilité.")]),
    ("05", "Systèmes asservis", "TLSystemesAsservis.sty", [
        ("Structure", "Chaîne directe, retour, comparateur, correcteur, procédé et capteur."),
        ("Modèle", "Fonctions de transfert, schémas-blocs et transformations de Laplace."),
        ("Performances", "Précision, rapidité, stabilité et sensibilité aux perturbations."),
        ("Analyse", "Étudier réponses temporelles, pôles, gain statique et comportement fréquentiel.")]),
]

POSTER = r'''\documentclass[a3paper,landscape,10pt]{article}
\usepackage[margin=10mm]{geometry}
\usepackage[french]{babel}
\usepackage{amsmath,amssymb}
\makeatletter\def\input@path{{../../../Style/}}\makeatother
\input{TLPosterCarteMentale.sty}
\IfFileExists{STYLE}{\input{STYLE}}{}
\pagestyle{empty}
\begin{document}
\TLPosterTitre{TITLE}{Fiche résumé éditable}
\begin{multicols}{2}
BLOCKS
\end{multicols}
\end{document}
'''

MIND = r'''\documentclass[a3paper,landscape,10pt]{article}
\usepackage[margin=8mm]{geometry}
\usepackage[french]{babel}
\usepackage{amsmath,amssymb}
\makeatletter\def\input@path{{../../../Style/}}\makeatother
\input{TLPosterCarteMentale.sty}
\IfFileExists{STYLE}{\input{STYLE}}{}
\pagestyle{empty}
\begin{document}
\begin{TLCarteMentale}{TITLE}
BRANCHES
\end{TLCarteMentale}
\end{document}
'''


def find_course(prefix: str) -> Path:
    matches = sorted(p for p in Path('.').glob(f'{prefix}-*') if p.is_dir())
    if len(matches) != 1:
        raise RuntimeError(f'Préfixe {prefix}: {len(matches)} dossier(s) trouvé(s): {matches}')
    return matches[0]


for prefix, title, style, blocks in COURSES:
    folder = find_course(prefix)
    poster_dir = folder / 'Cours' / 'Poster'
    mind_dir = folder / 'Cours' / 'Carte mentale'
    poster_dir.mkdir(parents=True, exist_ok=True)
    mind_dir.mkdir(parents=True, exist_ok=True)

    safe = ''.join(c if c.isalnum() else '_' for c in title)
    poster_file = poster_dir / f'Poster_{prefix}_{safe}.tex'
    mind_file = mind_dir / f'Carte_Mentale_{prefix}_{safe}.tex'

    if prefix in HANDCRAFTED and poster_file.exists() and mind_file.exists():
        print(f'Cours {prefix}: visuels spécifiques conservés.')
        continue

    pblocks = '\n\n'.join(
        f'\\begin{{TLPosterBloc}}{{{h}}}\n{b}\n\\end{{TLPosterBloc}}'
        for h, b in blocks
    )
    branches = '\n'.join(f'\\TLBranche{{{h}}}{{{b}}}' for h, b in blocks)

    poster_file.write_text(
        POSTER.replace('STYLE', style).replace('TITLE', title).replace('BLOCKS', pblocks),
        encoding='utf-8',
    )
    mind_file.write_text(
        MIND.replace('STYLE', style).replace('TITLE', title).replace('BRANCHES', branches),
        encoding='utf-8',
    )

print('Création terminée pour les cours 01 à 05.')
