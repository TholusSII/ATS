from pathlib import Path

COURSES = [
    ("06-Correction des Systèmes asservis", "Correction des systèmes asservis", "TLCorrectionSystemesAsservis.sty", [
        ("Objectifs", "Précision, rapidité, stabilité et rejet des perturbations."),
        ("Correcteurs", "P : gain ; PI : annulation de l'erreur statique ; PD : anticipation ; PID : compromis global."),
        ("Méthode", "Identifier le besoin, choisir la structure, régler les paramètres, vérifier les marges et les performances."),
        ("Points clés", "Effet du gain, pôles dominants, marges de gain et de phase, saturation et robustesse.")]),
    ("07-Électronique", "Électronique", "TLElectronique.sty", [
        ("Grandeurs", "Tension, courant, puissance et énergie dans les dipôles."),
        ("Composants", "Résistance, condensateur, inductance, diode et transistor."),
        ("Méthodes", "Lois de Kirchhoff, équivalents de Thévenin/Norton et analyse temporelle."),
        ("Points clés", "Régimes transitoires, filtrage, adaptation et commande des composants.")]),
    ("08-Électromécanique", "Électromécanique", "TLElectromecanique.sty", [
        ("Conversion", "Transformation réversible entre énergie électrique et énergie mécanique."),
        ("Grandeurs", "Couple, vitesse, puissance, rendement et pertes."),
        ("Machines", "Actionneur, génératrice, chaîne d'énergie et quadrants de fonctionnement."),
        ("Méthode", "Établir le bilan des puissances puis relier les variables électriques et mécaniques.")]),
    ("09-MCC", "Machine à courant continu", "TLMCC.sty", [
        ("Modèle", "u = Ri + L di/dt + e, avec e = K_e omega."),
        ("Couple", "C_em = K_t i ; à flux constant K_e = K_t en unités SI."),
        ("Bilan", "Puissance électrique, pertes Joule, puissance électromagnétique et puissance utile."),
        ("Commande", "Variation de vitesse par la tension d'induit et fonctionnement dans les quatre quadrants.")]),
    ("10-Électronique de Puissance", "Électronique de puissance", "TLElectroniquePuissance.sty", [
        ("Convertisseurs", "DC-DC, AC-DC, DC-AC et AC-AC."),
        ("Interrupteurs", "Diode, MOSFET, IGBT et thyristor ; états passant et bloqué."),
        ("Hacheurs", "Buck, Boost, deux quadrants et quatre quadrants."),
        ("Méthode", "Identifier les séquences, tracer les grandeurs puis calculer valeurs moyennes et ondulations.")]),
    ("11-Actions Mécaniques", "Actions mécaniques", "TLActionsMecaniques.sty", [
        ("Modélisation", "Une action mécanique est représentée par un torseur."),
        ("Statique", "Isoler, dresser le BAME puis appliquer le principe fondamental de la statique."),
        ("Dynamique", "Utiliser le PFD ou le théorème de l'énergie cinétique selon le problème."),
        ("Points clés", "Frottement, moment d'une force, centre d'inertie et opérateur d'inertie.")]),
    ("12-RDM", "Résistance des matériaux", "TLRDM.sty", [
        ("Hypothèses", "Poutres droites, petites déformations, Saint-Venant et Navier-Bernoulli."),
        ("Cohésion", "La coupure fait apparaître le torseur des efforts intérieurs."),
        ("Traction", "sigma = N/S et allongement gouverné par la loi de Hooke."),
        ("Flexion", "sigma = -M_f y/I et courbure liée à M_f/(EI).")]),
    ("13-MAS-MS", "Machines asynchrones et synchrones", "TLMachinesAlternatives.sty", [
        ("Triphasé", "Tensions simples et composées, couplages étoile/triangle et puissances."),
        ("MAS", "Glissement, schéma équivalent, bilan de puissance et commande V/f constante."),
        ("MS", "Vitesse synchrone, diagramme de Behn-Eschenburg et couple électromagnétique."),
        ("Commande", "Onduleur triphasé et autopilotage des moteurs brushless.")]),
    ("14-Logique", "Logique et systèmes séquentiels", "TLLogiqueSED.sty", [
        ("Combinatoire", "Tables de vérité, algèbre de Boole et simplification des équations."),
        ("Séquentiel", "États, transitions, événements, gardes et effets."),
        ("SysML", "Diagrammes d'états et de séquence pour décrire le comportement."),
        ("Communication", "Codeurs, réseaux, modèle OSI, multiplexage et protocoles.")]),
    ("15-Outils numériques", "Outils numériques", "TLOutilsNumeriques.sty", [
        ("Discrétisation", "t_k = t_0 + kh et approximation numérique des dérivées."),
        ("Euler explicite", "y_{k+1} = y_k + h f(t_k,y_k)."),
        ("Ordre deux", "Transformer l'équation en système de deux équations du premier ordre."),
        ("Validation", "Étudier convergence, stabilité, influence du pas et cohérence physique.")]),
]

POSTER_TEMPLATE = r'''\documentclass[a3paper,landscape,10pt]{article}
\usepackage[margin=10mm]{geometry}
\usepackage[french]{babel}
\usepackage{amsmath,amssymb}
\makeatletter
\def\input@path{{../../../Style/}}
\makeatother
\input{TLPosterCarteMentale.sty}
\IfFileExists{{STYLE}}{{\input{{STYLE}}}}{{}}
\pagestyle{empty}
\begin{document}
\TLPosterTitre{{TITLE}}{{Fiche résumé éditable}}
\begin{multicols}{2}
BLOCKS
\end{multicols}
\end{document}
'''

MINDMAP_TEMPLATE = r'''\documentclass[a3paper,landscape,10pt]{article}
\usepackage[margin=8mm]{geometry}
\usepackage[french]{babel}
\usepackage{amsmath,amssymb}
\makeatletter
\def\input@path{{../../../Style/}}
\makeatother
\input{TLPosterCarteMentale.sty}
\IfFileExists{{STYLE}}{{\input{{STYLE}}}}{{}}
\pagestyle{empty}
\begin{document}
\begin{TLCarteMentale}{{TITLE}}
BRANCHES
\end{TLCarteMentale}
\end{document}
'''

for folder, title, style, blocks in COURSES:
    course = Path(folder) / "Cours"
    poster_dir = course / "Poster"
    mind_dir = course / "Carte mentale"
    poster_dir.mkdir(parents=True, exist_ok=True)
    mind_dir.mkdir(parents=True, exist_ok=True)

    poster_blocks = []
    branches = []
    for heading, body in blocks:
        poster_blocks.append(f"\\begin{{TLPosterBloc}}{{{heading}}}\n{body}\n\\end{{TLPosterBloc}}")
        branches.append(f"\\TLBranche{{{heading}}}{{{body}}}")

    safe = folder.split('-', 1)[0] + '_' + ''.join(c if c.isalnum() else '_' for c in title)
    poster = POSTER_TEMPLATE.replace('STYLE', style).replace('TITLE', title).replace('BLOCKS', '\n\n'.join(poster_blocks))
    mind = MINDMAP_TEMPLATE.replace('STYLE', style).replace('TITLE', title).replace('BRANCHES', '\n'.join(branches))

    (poster_dir / f"Poster_{safe}.tex").write_text(poster, encoding="utf-8")
    (mind_dir / f"Carte_Mentale_{safe}.tex").write_text(mind, encoding="utf-8")

print(f"Création terminée pour {len(COURSES)} cours.")
