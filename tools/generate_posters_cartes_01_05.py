from pathlib import Path
from poster_carte_core import generate

DATA = {
"01": dict(
 folder="01-Ingénierie système", title="Ingénierie système",
 subtitle="Besoin, exigences, SysML et architecture fonctionnelle",
 key_title="Fil conducteur", key=r"Besoin $\rightarrow$ Exigences $\rightarrow$ Architecture $\rightarrow$ Vérification $\rightarrow$ Validation",
 map_key=r"Besoin $\rightarrow$ Exigences $\rightarrow$ Architecture $\rightarrow$ Validation",
 savoirs=[
  "définir un système, sa frontière, son environnement et ses interactions",
  "identifier le besoin, les fonctions de service, contraintes, critères et niveaux",
  "distinguer système souhaité, simulé et réel et situer le cycle de vie",
  "connaître parties prenantes, cycle en V, exigences, traçabilité, vérification et validation",
  "exploiter les principaux diagrammes SysML et les chaînes fonctionnelles"],
 blocks=[
  ("Système et besoin", "Un système naturel ou artificiel réalise une finalité. Sa frontière le sépare de l'environnement. Les échanges concernent matière, énergie et information. Le besoin conduit aux fonctions de service puis aux solutions."),
  ("Cycle de vie et ingénierie système", "Conception, industrialisation, utilisation, maintenance et fin de vie doivent rester cohérentes. La démarche descendante décompose le besoin ; la démarche ascendante intègre et vérifie les sous-systèmes."),
  ("Exigences et preuves", "Une exigence doit être claire, nécessaire, mesurable, vérifiable et traçable. Vérifier consiste à montrer que la conception répond aux exigences ; valider à montrer que le système répond au besoin."),
  ("SysML et architecture", "Contexte, exigences, BDD/IBD, séquence, activités et états décrivent des points de vue complémentaires. L'architecture fonctionnelle relie fonctions, chaîne d'information, chaîne d'énergie et solutions.")],
 method=[
  "Identifier le besoin, le contexte et les parties prenantes.",
  "Formuler les fonctions et des exigences mesurables.",
  "Décomposer le système et choisir les diagrammes SysML utiles.",
  "Construire l'architecture fonctionnelle et les interfaces.",
  "Définir les moyens de vérification associés aux exigences.",
  "Valider le système vis-à-vis du besoin initial."],
 retenir="partir du besoin, tracer les exigences jusqu'aux solutions, puis vérifier et valider.",
 map=[
  ("Besoin et cycle de vie", ["besoin utilisateur", "fonctions de service", "contraintes et critères", "souhaité / simulé / réel"]),
  ("Exigences", ["cahier des charges", "attributs", "traçabilité", "vérification / validation"]),
  ("SysML", ["contexte", "exigences", "BDD / IBD", "séquence / états"]),
  ("Architecture", ["parties prenantes", "cycle en V", "chaîne d'information", "chaîne d'énergie"])],
 map_flow=r"Analyser $\rightarrow$ Exprimer le besoin $\rightarrow$ Décomposer $\rightarrow$ Modéliser $\rightarrow$ Vérifier $\rightarrow$ Valider"),

"02": dict(
 folder="02-Modélisation des mécanismes", title="Modélisation des mécanismes",
 subtitle="Solides, liaisons, schéma cinématique et paramétrage",
 key_title="Objectif", key="Construire un modèle cinématique simple, pertinent et exploitable.",
 map_key=r"Solides $\rightarrow$ Liaisons $\rightarrow$ Graphe $\rightarrow$ Schéma $\rightarrow$ Paramétrage",
 savoirs=[
  "définir les classes d'équivalence cinématique et la notion de solide indéformable",
  "connaître les liaisons usuelles, leurs surfaces de contact et degrés de liberté",
  "construire un graphe des liaisons et un schéma cinématique",
  "définir repères, paramètres géométriques et coordonnées d'entrée et de sortie",
  "analyser la mobilité et déterminer une liaison équivalente"],
 blocks=[
  ("Solides et liaisons", "Une classe d'équivalence regroupe les pièces sans mouvement relatif. Une liaison modélise les mouvements autorisés entre deux solides : pivot, glissière, pivot glissant, hélicoïdale, rotule, appui plan, liaisons linéaires et ponctuelle."),
  ("Représentations", "Le graphe des liaisons montre les solides et leurs connexions. Le schéma cinématique remplace le réel par des symboles normalisés en conservant axes, directions et géométries utiles."),
  ("Paramétrage et mobilité", "On associe un repère à chaque solide puis on définit longueurs, distances et angles. Les coordonnées articulaires décrivent les mobilités ; les coordonnées opérationnelles décrivent la réponse."),
  ("Liaison équivalente", "Des liaisons en série ou en parallèle peuvent être remplacées par une liaison équivalente lorsqu'elle autorise le même mouvement relatif global.")],
 method=[
  "Identifier le bâti et les classes d'équivalence cinématique.",
  "Repérer les contacts et choisir les liaisons normalisées.",
  "Construire le graphe des liaisons.",
  "Établir le schéma cinématique en respectant axes et directions.",
  "Paramétrer solides, liaisons et variables utiles.",
  "Vérifier que le modèle conserve les mobilités nécessaires."],
 retenir="un bon modèle conserve l'essentiel du comportement mécanique sans recopier inutilement le réel.",
 map=[
  ("Solides et liaisons", ["classes d'équivalence", "pivot / glissière", "rotule / hélicoïdale", "ddl et contacts"]),
  ("Représentations", ["graphe des liaisons", "schéma cinématique", "symboles normalisés"]),
  ("Paramétrage", ["repères", "paramètres géométriques", "entrée / sortie"]),
  ("Exploitation", ["mobilité", "liaison équivalente", "préparation des lois de mouvement"])],
 map_flow=r"Identifier $\rightarrow$ Simplifier $\rightarrow$ Modéliser $\rightarrow$ Paramétrer $\rightarrow$ Vérifier"),

"03": dict(
 folder="03-Lois entrée sortie", title="Lois entrée-sortie et transmetteurs",
 subtitle="Fermetures géométriques, lois en vitesse et rapports de transmission",
 key_title="Relations clés", key=r"$\displaystyle \sum \overrightarrow{A_iA_{i+1}}=\vec 0$\qquad $i=\dfrac{\omega_s}{\omega_e}$",
 map_key=r"Boucles $\rightarrow$ Loi en position $\rightarrow$ Loi en vitesse $\rightarrow$ Transmission",
 savoirs=[
  "distinguer structures cinématiques ouvertes et fermées",
  "définir coordonnées articulaires et coordonnées opérationnelles",
  "établir une fermeture géométrique et une loi entrée-sortie en position",
  "établir une fermeture cinématique, dériver et projeter les relations",
  "connaître transmetteurs, rapports, rendement, couple, puissance et formule de Willis"],
 blocks=[
  ("Fermeture géométrique", "Dans une chaîne fermée, une boucle vectorielle traduit la géométrie. Projections, normes, orthogonalité ou loi des cosinus permettent d'obtenir les équations scalaires reliant entrée et sortie."),
  ("Loi en vitesse", "La dérivation de la loi géométrique ou la fermeture des torseurs cinématiques donne la relation entre vitesses. Les projections judicieuses éliminent les inconnues inutiles."),
  ("Transmetteurs", "Roues de friction, poulies--courroies, chaînes, engrenages, pignon--crémaillère, vis--écrou, roue et vis sans fin et trains épicycloïdaux transmettent ou transforment le mouvement."),
  ("Rapports et énergie", "Le signe du rapport traduit le sens relatif des mouvements. Le rendement relie les puissances d'entrée et de sortie. La formule de Willis relie les vitesses des éléments d'un train épicycloïdal.")],
 method=[
  "Choisir les paramètres d'entrée et de sortie et poser les repères.",
  "Écrire une fermeture géométrique ou une contrainte adaptée.",
  "Projeter et résoudre la loi en position.",
  "Dériver ou composer les torseurs pour obtenir la loi en vitesse.",
  "Établir le rapport de transmission avec la convention de signe.",
  "Vérifier sens, rendement, puissances et cohérence physique."],
 retenir="relier l'entrée à la sortie en choisissant la représentation et la relation les plus efficaces.",
 map=[
  ("Structures", ["ouverte / fermée", "coordonnées articulaires", "coordonnées opérationnelles"]),
  ("Fermeture géométrique", ["boucle vectorielle", "projection", "loi en position"]),
  ("Vitesse", ["dérivation", "torseurs", "loi en vitesse"]),
  ("Transmetteurs et rapports", ["friction / courroies / chaînes", "engrenages / vis--écrou", "Willis / rendement / puissance"])],
 map_flow=r"Modéliser $\rightarrow$ Écrire $\rightarrow$ Projeter $\rightarrow$ Résoudre $\rightarrow$ Dériver $\rightarrow$ Interpréter"),

"04": dict(
 folder="04-Cinématique", title="Cinématique", subtitle="Détermination des lois de mouvement",
 key_title="Transport des vitesses", key=r"$\vec V_Q=\vec V_P+\vec\Omega\wedge\overrightarrow{PQ}$",
 map_key=r"Position $\rightarrow$ Vitesse $\rightarrow$ Accélération",
 savoirs=[
  "maîtriser produit vectoriel, produit mixte et repérage spatial",
  "définir un torseur cinématique et effectuer un changement de point",
  "caractériser translation, rotation, mouvement plan et trajectoires",
  "relier position, vitesse, accélération et dérivation vectorielle",
  "composer les mouvements et traiter contact, roulement sans glissement et profil trapézoïdal"],
 blocks=[
  ("Outils vectoriels", "Le produit vectoriel décrit directions normales et moments ; le produit mixte facilite certaines projections. Un paramétrage cohérent fixe points, bases et sens positifs."),
  ("Torseur et mouvements", "Le torseur cinématique regroupe vecteur rotation et vitesse d'un point. Translation, rotation autour d'un axe et mouvement plan conduisent à des champs de vitesses caractéristiques."),
  ("Dérivation et composition", "Position, vitesse et accélération sont liées par dérivation. Dans un repère mobile, la dérivation vectorielle ajoute le terme de transport. Vitesses et rotations se composent entre repères."),
  ("Contact et lois de mouvement", "Le roulement sans glissement impose une vitesse relative nulle au point de contact. Une loi de vitesse trapézoïdale enchaîne accélération, vitesse constante et décélération.")],
 method=[
  "Choisir solides, repères, points et paramètres adaptés.",
  "Écrire les vecteurs position et les relations géométriques utiles.",
  "Dériver dans le bon repère pour obtenir vitesse puis accélération.",
  "Transporter les vitesses au point pertinent et composer les mouvements.",
  "Appliquer les conditions de contact ou de roulement sans glissement.",
  "Contrôler dimensions, signes et cohérence avec le mouvement réel."],
 retenir="position, vitesse et accélération se déduisent d'un modèle cinématique cohérent et d'un repérage maîtrisé.",
 map=[
  ("Outils", ["produit vectoriel", "produit mixte", "repères"]),
  ("Torseur cinématique", ["rotation", "vitesse en un point", "changement de point"]),
  ("Grandeurs", ["position", "vitesse", "accélération", "dérivation vectorielle"]),
  ("Applications", ["composition", "roulement sans glissement", "loi trapézoïdale"])],
 map_flow=r"Repérer $\rightarrow$ Exprimer $\rightarrow$ Dériver $\rightarrow$ Composer $\rightarrow$ Interpréter"),

"05": dict(
 folder="05-Modélisation Systèmes Asservis", title="Systèmes asservis",
 subtitle="Boucles, performances, modèles temporels et fréquentiels",
 key_title="Relation fondamentale", key=r"$e(t)=r(t)-m(t)$\\[1mm] erreur = consigne $-$ mesure",
 map_key=r"$e(t)=r(t)-m(t)$",
 savoirs=[
  "distinguer boucle ouverte, boucle fermée, asservissement et régulation",
  "identifier consigne, erreur, sortie, mesure et perturbation",
  "caractériser stabilité, rapidité, précision, dépassement et robustesse",
  "utiliser transformée de Laplace, SLCI et fonctions de transfert",
  "connaître premier et second ordre, FTBO, FTBF, schémas-blocs et diagrammes de Bode"],
 blocks=[
  ("Structure", "Le comparateur forme l'erreur entre consigne et mesure. Le correcteur élabore la commande, le procédé agit sur la sortie et le capteur referme la boucle. Une perturbation peut agir sur le procédé."),
  ("Modèles", r"La transformée de Laplace conduit à la fonction de transfert $H(p)=S(p)/E(p)$. Les modèles du premier ordre $K/(1+\tau p)$ et du second ordre décrivent de nombreux comportements."),
  ("Performances", "Stabilité, rapidité et précision sont les critères fondamentaux ; dépassement et robustesse complètent l'analyse. Toute correction recherche un compromis entre ces performances."),
  ("Représentations", "Schémas-blocs, réponses temporelles, pôles et zéros et diagrammes de Bode donnent des points de vue complémentaires. FTBO et FTBF relient structure et comportement.")],
 method=[
  "Identifier consigne, sortie, mesure et perturbations.",
  "Construire le schéma-bloc et identifier les fonctions de transfert.",
  "Réduire le schéma et déterminer FTBO puis FTBF.",
  "Reconnaître ou identifier le modèle dominant.",
  "Étudier les réponses temporelle et fréquentielle.",
  "Conclure sur stabilité, précision, rapidité, dépassement et robustesse."],
 retenir="comparer, corriger, agir et mesurer pour atteindre la consigne avec le meilleur compromis de performances.",
 map=[
  ("Structure et grandeurs", ["boucle ouverte / fermée", "comparateur / capteur", "consigne / erreur / mesure", "perturbation"]),
  ("Modélisation", ["SLCI", "Laplace", "fonction de transfert", "1er / 2e ordre"]),
  ("Performances", ["stabilité", "précision", "rapidité", "dépassement / robustesse"]),
  ("Représentations", ["schéma-bloc", "réponse temporelle", "Bode", "pôles et zéros"])],
 map_flow=r"Identifier $\rightarrow$ Modéliser $\rightarrow$ Réduire $\rightarrow$ Calculer $\rightarrow$ Analyser $\rightarrow$ Conclure"),
}

files = generate(DATA, Path('.'))
print(f"{len(files)} fichiers TeX mis à jour pour les cours 01 à 05.")
