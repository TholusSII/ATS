from pathlib import Path
from poster_carte_core import generate

DATA = {
"06": dict(
 folder="06-Correction des Systèmes asservis", title="Correction des systèmes asservis",
 subtitle="Régler la commande pour satisfaire le cahier des charges",
 key_title="Principe", key=r"Corriger la boucle sans dégrader le compromis stabilité--rapidité--précision",
 map_key=r"Erreur $\rightarrow$ Correcteur $\rightarrow$ Boucle corrigée $\rightarrow$ Validation",
 savoirs=[
  "relier précision, rapidité, stabilité, dépassement et robustesse au cahier des charges",
  "connaître l'effet du gain proportionnel et des actions intégrale et dérivée",
  "utiliser correcteurs P, PI, PD et PID",
  "comprendre retard de phase, avance de phase et pôles dominants",
  "exploiter diagrammes de Bode, marges de gain et de phase, saturation et rejet des perturbations"],
 blocks=[
  ("Effet du gain", "Augmenter le gain réduit souvent l'erreur et accélère la réponse, mais diminue les marges de stabilité et peut accroître le dépassement ou provoquer la saturation."),
  ("Correcteurs usuels", "L'action P règle le gain, I améliore la précision statique, D anticipe les variations. PI, PD et PID combinent ces effets pour satisfaire plusieurs critères simultanément."),
  ("Correction fréquentielle", "Un retard de phase peut améliorer la précision aux basses fréquences ; une avance de phase augmente la marge de phase et la rapidité. Le choix dépend de la FTBO initiale."),
  ("Validation", "Le réglage final se contrôle sur les réponses temporelle et fréquentielle : erreur, temps de réponse, dépassement, marges, robustesse, effort de commande et saturation.")],
 method=[
  "Traduire le cahier des charges en critères mesurables.",
  "Analyser la FTBO non corrigée et repérer ses pôles dominants.",
  "Choisir la structure du correcteur adaptée au défaut principal.",
  "Régler les paramètres à partir des critères temporels et fréquentiels.",
  "Vérifier marges de stabilité, saturation et rejet des perturbations.",
  "Valider le compromis global sur la FTBF."],
 retenir="un correcteur se choisit et se règle à partir d'un défaut identifié, puis se valide sur l'ensemble des performances.",
 map=[
  ("Performances", ["stabilité", "rapidité", "précision", "dépassement / robustesse"]),
  ("Correcteurs", ["P", "I / PI", "PD", "PID"]),
  ("Correction fréquentielle", ["retard de phase", "avance de phase", "pôles dominants"]),
  ("Validation", ["Bode", "marges gain / phase", "réponse temporelle", "saturation"])],
 map_flow=r"Diagnostiquer $\rightarrow$ Choisir $\rightarrow$ Régler $\rightarrow$ Vérifier $\rightarrow$ Ajuster $\rightarrow$ Valider"),

"07": dict(
 folder="07-Électronique", title="Acquisition et traitement du signal",
 subtitle="Capteurs, conditionnement, filtrage, échantillonnage et numérisation",
 key_title="Chaîne d'acquisition", key=r"Grandeur physique $\rightarrow$ Capteur $\rightarrow$ Conditionnement $\rightarrow$ CAN $\rightarrow$ Traitement",
 map_key=r"Mesurer $\rightarrow$ Conditionner $\rightarrow$ Filtrer $\rightarrow$ Échantillonner $\rightarrow$ Numériser",
 savoirs=[
  "décrire une chaîne d'acquisition et les caractéristiques d'un capteur : sensibilité, étendue, précision, résolution",
  "utiliser lois d'électrocinétique, impédances complexes et montages à amplificateur opérationnel",
  "caractériser filtres passe-bas, passe-haut, gain, phase, bande passante et fréquence de coupure",
  "interpréter spectres temporels et fréquentiels et appliquer Shannon--Nyquist",
  "comprendre anti-repliement, échantillonnage, CAN/CNA, quantification et codage binaire"],
 blocks=[
  ("Capteurs et conditionnement", "Le capteur convertit une grandeur physique en signal exploitable. Sensibilité, étendue de mesure, justesse, précision et résolution caractérisent la mesure. Le conditionnement adapte amplitude, offset et impédance."),
  ("Électrocinétique et AOP", "Les lois de Kirchhoff et les impédances de R, L et C permettent d'établir les fonctions de transfert. L'AOP idéal sert à amplifier, sommer, soustraire ou filtrer un signal."),
  ("Filtrage", "Un filtre sélectionne des bandes de fréquences. Le diagramme de Bode donne gain et phase ; fréquence de coupure et pente asymptotique caractérisent les filtres du premier ou second ordre."),
  ("Échantillonnage et conversion", "Pour éviter le repliement spectral, la fréquence d'échantillonnage respecte le critère de Shannon et un filtre anti-repliement limite le spectre. Le CAN quantifie et code ; le CNA réalise l'opération inverse.")],
 method=[
  "Identifier la grandeur à mesurer et choisir le capteur adapté.",
  "Établir le schéma de conditionnement et sa fonction de transfert.",
  "Analyser le spectre utile et définir le filtrage nécessaire.",
  "Choisir la fréquence d'échantillonnage avec une marge suffisante.",
  "Déterminer résolution, pas de quantification et plage du convertisseur.",
  "Vérifier que la chaîne complète respecte précision, dynamique et bande passante."],
 retenir="une mesure fiable exige une chaîne cohérente du capteur jusqu'au traitement numérique, sans saturation ni repliement spectral.",
 map=[
  ("Capteurs", ["sensibilité", "étendue", "précision", "résolution"]),
  ("Conditionnement", ["électrocinétique", "impédances", "AOP", "adaptation"]),
  ("Filtrage", ["spectre", "passe-bas / passe-haut", "Bode", "fréquence de coupure"]),
  ("Numérisation", ["Shannon", "anti-repliement", "CAN / CNA", "codage binaire"])],
 map_flow=r"Mesurer $\rightarrow$ Adapter $\rightarrow$ Filtrer $\rightarrow$ Échantillonner $\rightarrow$ Convertir $\rightarrow$ Vérifier"),

"08": dict(
 folder="08-Électromécanique", title="Conversion électromécanique",
 subtitle="Machines électriques, caractéristiques machine--charge et essais",
 key_title="Bilan de puissance", key=r"$P_{\rm elec}\leftrightarrow P_{\rm em}\leftrightarrow P_{\rm mec}$ avec pertes et rendement",
 map_key=r"Énergie électrique $\leftrightarrow$ Énergie mécanique",
 savoirs=[
  "décrire la conversion réversible entre énergie électrique et énergie mécanique",
  "relier couple, vitesse, puissance, rendement et pertes",
  "interpréter caractéristiques mécaniques d'une machine et d'une charge",
  "déterminer le point de fonctionnement machine--charge et les quadrants",
  "exploiter essais à vide, en charge et données nominales pour identifier un modèle"],
 blocks=[
  ("Conversion", "Une machine électrique peut fonctionner en moteur ou en génératrice. La conversion est réversible ; les pertes électriques, magnétiques et mécaniques expliquent que le rendement reste inférieur à un."),
  ("Grandeurs mécaniques", r"La puissance mécanique en rotation vérifie $P=C\omega$. Une caractéristique couple--vitesse décrit la machine ; la charge impose sa propre caractéristique."),
  ("Machine et charge", "Le point de fonctionnement est l'intersection des caractéristiques machine et charge. Les signes de couple et vitesse permettent d'identifier les quadrants moteur ou générateur."),
  ("Essais et identification", "Les essais à vide, en charge ou au point nominal fournissent tensions, courants, vitesses, couples et puissances. Ils permettent de calculer pertes, rendement et paramètres utiles au modèle.")],
 method=[
  "Identifier le sens des flux d'énergie et le mode moteur ou générateur.",
  "Recenser les grandeurs électriques et mécaniques disponibles.",
  "Établir le bilan des puissances et localiser les pertes.",
  "Tracer ou exploiter les caractéristiques machine et charge.",
  "Déterminer le point de fonctionnement et le rendement.",
  "Comparer le résultat aux limites nominales de la machine."],
 retenir="la conversion électromécanique se comprend par les flux de puissance et le point de fonctionnement imposé par la machine et sa charge.",
 map=[
  ("Conversion", ["moteur", "génératrice", "réversibilité"]),
  ("Grandeurs", ["couple", "vitesse", "puissance", "rendement"]),
  ("Machine--charge", ["caractéristiques", "point de fonctionnement", "quadrants"]),
  ("Essais", ["à vide", "en charge", "identification", "nominal"])],
 map_flow=r"Identifier $\rightarrow$ Bilan $\rightarrow$ Caractéristiques $\rightarrow$ Point de fonctionnement $\rightarrow$ Rendement"),

"09": dict(
 folder="09-MCC", title="Machine à courant continu",
 subtitle="Modèle électromécanique, bilan de puissance et variation de vitesse",
 key_title="Relations fondamentales", key=r"$u=Ri+L\,\dfrac{di}{dt}+e$\qquad $e=K_e\omega$\qquad $C_{em}=K_t i$",
 map_key=r"$u=Ri+L\,di/dt+e$ ; $e=K_e\omega$ ; $C=K_ti$",
 savoirs=[
  "connaître constitution, inducteur, induit, collecteur, balais et flux magnétique",
  "établir l'équation électrique de l'induit et les relations de fcem et de couple",
  "réaliser le bilan des puissances et identifier pertes Joule, électromagnétiques et mécaniques",
  "distinguer fonctionnement moteur, génératrice, démarrage et régimes transitoires",
  "analyser la variation de vitesse par la tension d'induit et identifier les paramètres du modèle"],
 blocks=[
  ("Constitution et principe", "Le stator crée le flux inducteur et le rotor porte l'induit. Le collecteur et les balais assurent la commutation. La fcem est proportionnelle à la vitesse et le couple électromagnétique au courant d'induit."),
  ("Modèle électrique et mécanique", r"L'induit vérifie $u=Ri+L\,di/dt+e$, avec $e=K_e\omega$. Le couple vérifie $C_{em}=K_t i$. En unités SI et à flux constant, les constantes sont liées."),
  ("Bilan de puissance", "La puissance électrique absorbée se répartit entre pertes Joule, puissance électromagnétique, pertes mécaniques et puissance utile. En génératrice, le sens du flux de puissance s'inverse."),
  ("Commande et régimes", "Au démarrage la fcem est faible et le courant doit être limité. La vitesse se règle principalement par la tension d'induit à flux constant. Le modèle dynamique couple équations électrique et mécanique.")],
 method=[
  "Choisir les conventions moteur/génératrice et orienter tension, courant, couple et vitesse.",
  "Écrire l'équation électrique de l'induit.",
  "Utiliser les relations fcem--vitesse et couple--courant.",
  "Écrire l'équation mécanique avec charge et inertie si nécessaire.",
  "Établir le bilan de puissance et le rendement.",
  "Vérifier courant de démarrage, vitesse, couple et limites nominales."],
 retenir="la MCC relie directement courant et couple, ainsi que vitesse et force contre-électromotrice.",
 map=[
  ("Constitution", ["inducteur / induit", "collecteur / balais", "flux"]),
  ("Modèle", [r"$u=Ri+L\,di/dt+e$", r"$e=K_e\omega$", r"$C=K_t i$"]),
  ("Bilan", ["puissances", "pertes Joule", "rendement", "moteur / génératrice"]),
  ("Commande", ["démarrage", "variation de tension", "régime variable", "identification"])],
 map_flow=r"Orienter $\rightarrow$ Équation électrique $\rightarrow$ Couple $\rightarrow$ Mécanique $\rightarrow$ Bilan $\rightarrow$ Valider"),

"10": dict(
 folder="10-Électronique de Puissance", title="Électronique de puissance",
 subtitle="Conversion statique de l'énergie",
 key_title="Principe", key=r"Interrupteurs commandés + stockage d'énergie $\rightarrow$ conversion avec pertes limitées",
 map_key=r"Source $\rightarrow$ Convertisseur $\rightarrow$ Charge",
 savoirs=[
  "classer les convertisseurs DC--DC, AC--DC, DC--AC et AC--AC",
  "connaître diode, MOSFET, IGBT et thyristor et leurs états passant/bloqué",
  "utiliser rapport cyclique, valeurs moyenne et efficace, fréquence de découpage et ondulation",
  "analyser hacheurs Buck, Boost, deux quadrants et quatre quadrants",
  "analyser redressement, pont de diodes, harmoniques, facteur de puissance et principe du PFC"],
 blocks=[
  ("Interrupteurs de puissance", "Diode et semi-conducteurs commandés réalisent des commutations entre états passant et bloqué. Le choix dépend de la tension, du courant, de la fréquence et du besoin de réversibilité."),
  ("Hacheurs DC--DC", "Buck abaisse la tension moyenne, Boost l'élève. Les structures deux ou quatre quadrants rendent courant et/ou tension réversibles. Les inductances et condensateurs limitent les ondulations."),
  ("Redressement et onduleur", "Un pont de diodes transforme l'alternatif en continu ; l'onduleur réalise la conversion inverse. La commande de commutation façonne la valeur moyenne, la fréquence et le spectre de sortie."),
  ("Grandeurs et qualité d'énergie", "Rapport cyclique, fréquence de découpage et séquences de conduction permettent de calculer valeurs moyennes et ondulations. Harmoniques et facteur de puissance motivent filtrage et correction PFC.")],
 method=[
  "Identifier nature de la source, de la charge et les réversibilités demandées.",
  "Choisir la structure de convertisseur et les interrupteurs compatibles.",
  "Découper une période en séquences de conduction.",
  "Tracer tensions et courants dans chaque séquence.",
  "Calculer valeurs moyennes, efficaces et ondulations.",
  "Vérifier puissance, contraintes des composants et qualité d'énergie."],
 retenir="l'analyse d'un convertisseur part toujours des états des interrupteurs et des séquences de fonctionnement.",
 map=[
  ("Interrupteurs", ["diode", "MOSFET / IGBT", "passant / bloqué", "sources"]),
  ("Hacheurs", ["Buck", "Boost", "2 quadrants", "4 quadrants"]),
  ("Conversion AC", ["redressement", "pont de diodes", "onduleur", "PFC / harmoniques"]),
  ("Grandeurs", ["rapport cyclique", "moyenne / efficace", "ondulation", "puissance"])],
 map_flow=r"Identifier $\rightarrow$ Séquencer $\rightarrow$ Tracer $\rightarrow$ Calculer $\rightarrow$ Dimensionner $\rightarrow$ Vérifier"),

"11": dict(
 folder="11-Actions Mécaniques", title="Actions mécaniques",
 subtitle="Torseurs, équilibre, frottement et dynamique",
 key_title="Principe fondamental de la statique", key=r"$\displaystyle \sum \{\mathcal T_{\rm ext}\}=\{0\}$ pour un solide en équilibre",
 map_key=r"Isoler $\rightarrow$ BAME $\rightarrow$ Torseurs $\rightarrow$ Équations",
 savoirs=[
  "modéliser force, moment, glisseur, couple et action mécanique par un torseur",
  "représenter les actions transmissibles par les liaisons et appliquer les actions réciproques",
  "isoler un système, dresser le BAME et appliquer le principe fondamental de la statique",
  "traiter pression de contact, adhérence, glissement et lois de Coulomb",
  "connaître centre d'inertie, opérateur d'inertie, PFD et théorème de l'énergie cinétique"],
 blocks=[
  ("Torseur d'action mécanique", "Une action mécanique se représente par une résultante et un moment en un point. Le changement de point transporte le moment. Force seule et couple sont des cas particuliers."),
  ("Statique", "Après isolement, le BAME recense les actions extérieures. Le PFS impose l'annulation de la résultante et du moment ; une projection adaptée permet de résoudre les inconnues utiles."),
  ("Contacts et frottement", "Une pression répartie peut être remplacée par une action résultante. Avec frottement sec, l'effort tangentiel reste dans le cône de frottement en adhérence et atteint la limite au glissement."),
  ("Dynamique et énergie", "Le PFD relie torseur dynamique et actions extérieures. Selon le problème, le théorème de l'énergie cinétique fournit une relation scalaire efficace entre puissances, travail et variation d'énergie.")],
 method=[
  "Choisir le système à isoler et définir le repère d'étude.",
  "Dresser le BAME et modéliser chaque action par un torseur.",
  "Transporter les torseurs vers un point de réduction pertinent.",
  "Appliquer PFS, PFD ou théorème de l'énergie selon l'objectif.",
  "Projeter les équations pour éliminer les inconnues inutiles.",
  "Vérifier signes, unités, conditions de frottement et cohérence physique."],
 retenir="une résolution mécanique efficace commence par un isolement pertinent et une modélisation correcte des actions extérieures.",
 map=[
  ("Modélisation", ["force / moment", "torseur", "glisseur / couple", "liaisons"]),
  ("Statique", ["isolement", "BAME", "PFS", "actions réciproques"]),
  ("Frottement", ["pressions", "Coulomb", "adhérence / glissement", "arc-boutement"]),
  ("Dynamique", ["centre d'inertie", "inertie", "PFD", "énergie cinétique"])],
 map_flow=r"Isoler $\rightarrow$ Modéliser $\rightarrow$ Réduire $\rightarrow$ Équilibrer $\rightarrow$ Résoudre $\rightarrow$ Vérifier"),

"12": dict(
 folder="12-RDM", title="Résistance des matériaux",
 subtitle="Efforts intérieurs, contraintes, déformations et dimensionnement",
 key_title="Dimensionnement", key=r"Sollicitations $\rightarrow$ contraintes $\rightarrow$ déformations $\rightarrow$ critères de résistance et rigidité",
 map_key=r"Coupure $\rightarrow$ Cohésion $\rightarrow$ Contraintes $\rightarrow$ Déformations",
 savoirs=[
  "connaître hypothèses de poutre, Saint-Venant, Navier--Bernoulli, petites déformations et élasticité",
  "déterminer le torseur de cohésion et ses composantes $N$, $T$, $M_t$ et $M_f$",
  "identifier traction/compression, cisaillement, torsion et flexion",
  "relier efforts intérieurs, contraintes et déformations avec les lois de comportement",
  "dimensionner avec critères de résistance, coefficient de sécurité et limite de flèche"],
 blocks=[
  ("Hypothèses et coupure", "La RDM remplace une structure élancée par sa ligne moyenne et sa section. Une coupure fait apparaître le torseur de cohésion, action de la partie supprimée sur la partie conservée."),
  ("Sollicitations", r"Les composantes $N$, $T$, $M_t$ et $M_f$ correspondent aux sollicitations élémentaires. Les diagrammes le long de la poutre localisent les sections les plus sollicitées."),
  ("Contraintes et déformations", r"En traction, $\sigma=N/S$. En flexion, la contrainte normale varie avec la distance à la fibre neutre. La loi de Hooke relie contrainte et déformation dans le domaine élastique."),
  ("Dimensionnement", "Le critère de résistance compare la contrainte calculée à une valeur admissible ; le critère de rigidité limite déplacement, rotation ou flèche. Le coefficient de sécurité tient compte des incertitudes.")],
 method=[
  "Identifier la poutre, ses appuis, chargements et hypothèses de modèle.",
  "Déterminer les réactions extérieures par équilibre.",
  "Effectuer une coupure et calculer le torseur de cohésion.",
  "Tracer les diagrammes des efforts intérieurs utiles.",
  "Calculer contraintes et déformations dans les sections critiques.",
  "Vérifier résistance, rigidité et coefficient de sécurité."],
 retenir="le torseur de cohésion relie les actions extérieures aux contraintes et déformations qui servent au dimensionnement.",
 map=[
  ("Hypothèses", ["poutre", "Saint-Venant", "Navier--Bernoulli", "élasticité"]),
  ("Cohésion", [r"$N,T,M_t,M_f$", "coupure", "diagrammes"]),
  ("Sollicitations", ["traction / compression", "cisaillement", "torsion", "flexion"]),
  ("Dimensionnement", ["Hooke", "sécurité", "résistance", "flèche"])],
 map_flow=r"Modéliser $\rightarrow$ Équilibrer $\rightarrow$ Couper $\rightarrow$ Contraintes $\rightarrow$ Déformations $\rightarrow$ Vérifier"),

"13": dict(
 folder="13-MAS-MS", title="Machines asynchrones et synchrones",
 subtitle="Triphasé, onduleur et conversion électromécanique en alternatif",
 key_title="Synchronisme", key=r"$n_s=\dfrac{60f}{p}$\qquad $g=\dfrac{n_s-n}{n_s}$ pour la machine asynchrone",
 map_key=r"Triphasé $\rightarrow$ Onduleur $\rightarrow$ Champ tournant $\rightarrow$ Couple",
 savoirs=[
  "maîtriser tensions simples/composées, couplages étoile/triangle et puissances triphasées",
  "comprendre la génération triphasée par onduleur et la modulation de largeur d'impulsion",
  "définir vitesse synchrone, glissement, bilan de puissance et couple de la MAS",
  "comprendre commande à $V/f$ constant et influence de la fréquence",
  "modéliser la MS avec diagramme de Behn--Eschenburg, couple électromagnétique et autopilotage brushless"],
 blocks=[
  ("Système triphasé", "Trois tensions sinusoïdales déphasées de 120° alimentent les phases. Les couplages étoile et triangle relient tensions simples et composées. Les puissances active, réactive et apparente caractérisent la charge."),
  ("Onduleur triphasé", "À partir d'une source continue, six interrupteurs synthétisent des tensions triphasées. La MLI commande fréquence et amplitude du fondamental et donc les conditions d'alimentation de la machine."),
  ("Machine asynchrone", "Le champ statorique tourne à la vitesse de synchronisme. Le rotor présente un glissement nécessaire à l'induction des courants et au couple. Le bilan de puissance distingue pertes statoriques, rotorique et mécanique."),
  ("Machine synchrone", "Le rotor suit le champ tournant sans glissement en régime établi. Le diagramme de Behn--Eschenburg relie tension, courant et fcem. L'autopilotage synchronise la commande électronique avec la position rotorique.")],
 method=[
  "Identifier couplage, tensions, courants et nombre de paires de pôles.",
  "Calculer vitesse de synchronisme et, pour la MAS, le glissement.",
  "Établir le bilan des puissances et le couple utile.",
  "Exploiter le schéma ou diagramme vectoriel adapté à la machine.",
  "Relier fréquence et amplitude de l'onduleur au point de fonctionnement.",
  "Vérifier limites thermiques, couple, vitesse et rendement."],
 retenir="les machines alternatives se comprennent à partir du champ tournant, du synchronisme et du bilan de puissance.",
 map=[
  ("Triphasé", ["tensions simples / composées", "étoile / triangle", r"$P,Q,S$", "Boucherot"]),
  ("Onduleur", ["source continue", "MLI", "fréquence / amplitude"]),
  ("MAS", ["synchronisme", "glissement", "bilan / couple", r"$V/f$"]),
  ("MS", ["Behn--Eschenburg", "couple", "autopilotage", "brushless"])],
 map_flow=r"Réseau $\rightarrow$ Couplage $\rightarrow$ Synchronisme $\rightarrow$ Bilan $\rightarrow$ Couple $\rightarrow$ Commande"),

"14": dict(
 folder="14-Logique", title="Logique et systèmes à événements discrets",
 subtitle="Combinatoire, séquentiel, codeurs et communication réseau",
 key_title="Du besoin à la logique", key=r"Cahier des charges $\rightarrow$ variables $\rightarrow$ modèle $\rightarrow$ validation",
 map_key=r"Spécification $\rightarrow$ Logique / états $\rightarrow$ Réalisation $\rightarrow$ Validation",
 savoirs=[
  "utiliser variables booléennes, tables de vérité, opérateurs et algèbre de Boole",
  "simplifier par formes canoniques ou Karnaugh et connaître mux, décodeur, comparateur et additionneur",
  "modéliser systèmes séquentiels par états, transitions, événements, gardes et actions",
  "exploiter diagrammes SysML d'états et de séquence et codeurs incrémentaux/absolus",
  "comprendre réseaux, modèle OSI, supports, bus, protocoles, trames, parité et CRC"],
 blocks=[
  ("Logique combinatoire", "Les sorties dépendent des entrées présentes. Une table de vérité conduit à une équation logique ; algèbre de Boole et Karnaugh permettent de simplifier la réalisation."),
  ("Systèmes séquentiels", "Les sorties dépendent aussi d'un état mémorisé. États, transitions, événements, gardes et effets décrivent le comportement ; les diagrammes d'états et de séquence représentent les évolutions temporelles."),
  ("Codeurs", "Les codeurs incrémentaux produisent des voies A/B en quadrature et une référence Z ; les codeurs absolus fournissent directement un mot de position. La résolution dépend du nombre de points ou de bits."),
  ("Réseaux et bus", "Un réseau transporte des données selon architecture, support et protocole. Le modèle OSI sépare les fonctions ; trames, adressage, parité ou CRC assurent échange et contrôle des erreurs.")],
 method=[
  "Traduire le cahier des charges en entrées, sorties et comportements attendus.",
  "Pour le combinatoire, construire la table de vérité puis les équations.",
  "Simplifier les fonctions et choisir les blocs logiques adaptés.",
  "Pour le séquentiel, définir états, transitions, gardes et actions puis tester tous les scénarios.",
  "Pour un codeur, décoder les voies et calculer résolution ou position.",
  "Pour un réseau, identifier trame, champs, codage et contrôle d'erreur."],
 retenir="choisir le formalisme selon que le comportement dépend des entrées, d'un état mémorisé ou d'un échange réseau.",
 map=[
  ("Combinatoire", ["tables de vérité", "Boole", "Karnaugh", "mux / décodeurs"]),
  ("Séquentiel", ["états", "transitions", "gardes", "séquence SysML"]),
  ("Codeurs", ["incrémental A/B/Z", "absolu", "résolution"]),
  ("Communication", ["OSI", "supports / bus", "trames", "parité / CRC"])],
 map_flow=r"Spécifier $\rightarrow$ Modéliser $\rightarrow$ Simplifier / séquencer $\rightarrow$ Réaliser $\rightarrow$ Tester $\rightarrow$ Valider"),

"15": dict(
 folder="15-Outils numériques", title="Outils numériques",
 subtitle="Discrétisation, intégration et validation des modèles",
 key_title="Euler explicite", key=r"$y_{k+1}=y_k+h\,f(t_k,y_k)$",
 map_key=r"Modèle continu $\rightarrow$ Discrétisation $\rightarrow$ Calcul numérique",
 savoirs=[
  "discrétiser le temps par $t_k=t_0+kh$ et approximer les dérivées par différences finies",
  "utiliser la méthode d'Euler explicite et comprendre la notion de schéma numérique",
  "transformer une équation d'ordre deux en système d'équations du premier ordre",
  "analyser erreur de discrétisation, convergence et influence du pas",
  "étudier stabilité numérique et valider par cohérence physique ou solution de référence"],
 blocks=[
  ("Discrétisation", r"Le temps continu est remplacé par des instants $t_k=t_0+kh$. Les dérivées sont approchées par des différences entre valeurs successives ; le pas $h$ règle précision et coût."),
  ("Euler explicite", r"La pente est évaluée au début du pas puis utilisée pour avancer : $y_{k+1}=y_k+h f(t_k,y_k)$. La méthode est simple mais son erreur et sa stabilité dépendent fortement de $h$."),
  ("Équations d'ordre deux", "Une équation différentielle du second ordre est transformée en deux équations du premier ordre en introduisant une variable de vitesse ou d'état supplémentaire."),
  ("Validation", "La diminution du pas doit conduire vers une solution stable. On compare à une solution analytique, une mesure ou des invariants physiques et on surveille les erreurs cumulées.")],
 method=[
  "Écrire le modèle continu et identifier variables d'état et conditions initiales.",
  "Choisir un pas compatible avec les constantes de temps.",
  "Écrire le schéma numérique puis initialiser les variables.",
  "Itérer le calcul en stockant temps et grandeurs utiles.",
  "Tracer les résultats et tester plusieurs valeurs du pas.",
  "Valider convergence, stabilité numérique, unités et cohérence physique."],
 retenir="un résultat numérique n'est fiable qu'après une étude du pas, de la convergence et de la cohérence physique.",
 map=[
  ("Discrétisation", [r"$t_k=t_0+kh$", "différences finies", r"pas $h$"]),
  ("Euler", [r"$y_{k+1}=y_k+h f_k$", "schéma explicite", "erreur locale"]),
  ("Ordre deux", ["variables d'état", "position / vitesse", "système d'ordre 1"]),
  ("Validation", ["convergence", "stabilité", "comparaison", "cohérence physique"])],
 map_flow=r"Modéliser $\rightarrow$ Discrétiser $\rightarrow$ Calculer $\rightarrow$ Comparer $\rightarrow$ Raffiner $\rightarrow$ Valider"),
}

files = generate(DATA, Path('.'))
print(f"{len(files)} fichiers TeX mis à jour pour les cours 06 à 15.")
