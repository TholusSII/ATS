![](11-Actions Mécaniques/Cours/pandoc/media/image1.png){width="8.494444444444444in"
height="4.148611111111111in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image3.jpeg){width="2.772222222222222in"
height="2.484722222222222in"}

Cycle 6 : Analyser, Modéliser, Expérimenter et Résoudre les performances
de systèmes de solide d'une chaîne d'énergie

**Détermination des actions mécaniques**

Thomas Lusseau

Lycée Robert Doisneau - ATS

Table des matières

[1. Introduction [8](#introduction)](#introduction)

[2. Démarche de résolution pour déterminer les Actions Mécaniques
[8](#démarche-de-résolution-pour-déterminer-les-actions-mécaniques)](#démarche-de-résolution-pour-déterminer-les-actions-mécaniques)

[2.1. Démarche de résolution
[8](#démarche-de-résolution)](#démarche-de-résolution)

[2.2. Représenter le système : graphe de structure et schéma
d'architecture
[9](#représenter-le-système-graphe-de-structure-et-schéma-darchitecture)](#représenter-le-système-graphe-de-structure-et-schéma-darchitecture)

[2.3. Isoler une partie du système
[10](#isoler-une-partie-du-système)](#isoler-une-partie-du-système)

[2.4. Démarche de résolution : Stratégie d'isolement
[11](#démarche-de-résolution-stratégie-disolement)](#démarche-de-résolution-stratégie-disolement)

[2.5. Recenser les actions mécaniques
[15](#recenser-les-actions-mécaniques)](#recenser-les-actions-mécaniques)

[3. Actions mécaniques [16](#actions-mécaniques)](#actions-mécaniques)

[3.1. Définition [16](#définition)](#définition)

[3.2. Torseurs d'AM particuliers : Torseur glisseur, Torseur couple
[17](#torseurs-dam-particuliers-torseur-glisseur-torseur-couple)](#torseurs-dam-particuliers-torseur-glisseur-torseur-couple)

[3.3. Théorème des actions réciproques
[17](#théorème-des-actions-réciproques)](#théorème-des-actions-réciproques)

[3.4. Cas de l'action mécanique de la pesanteur
[17](#cas-de-laction-mécanique-de-la-pesanteur)](#cas-de-laction-mécanique-de-la-pesanteur)

[3.5. Actions mécaniques particulières à connaître
[19](#actions-mécaniques-particulières-à-connaître)](#actions-mécaniques-particulières-à-connaître)

[3.6. Actions mécaniques transmissibles par les liaisons usuelles
[21](#actions-mécaniques-transmissibles-par-les-liaisons-usuelles)](#actions-mécaniques-transmissibles-par-les-liaisons-usuelles)

[3.7. Cas particulier d'un problème plan
[25](#cas-particulier-dun-problème-plan)](#cas-particulier-dun-problème-plan)

[4. Etude de l'équilibre d'un système
[26](#etude-de-léquilibre-dun-système)](#etude-de-léquilibre-dun-système)

[4.1. Etude de l'équilibre : Principe de la Statique
[26](#etude-de-léquilibre-principe-de-la-statique)](#etude-de-léquilibre-principe-de-la-statique)

[4.2. Démarche de résolution d'un problème pour étudier l'équilibre
[27](#démarche-de-résolution-dun-problème-pour-étudier-léquilibre)](#démarche-de-résolution-dun-problème-pour-étudier-léquilibre)

[4.3. Conseils pour le choix du point de réduction
[27](#conseils-pour-le-choix-du-point-de-réduction)](#conseils-pour-le-choix-du-point-de-réduction)

[4.4. Inventaire (ou bilan) des actions mécaniques extérieurs (BAME)
[27](#inventaire-ou-bilan-des-actions-mécaniques-extérieurs-bame)](#inventaire-ou-bilan-des-actions-mécaniques-extérieurs-bame)

[4.5. Ensemble isolé soumis uniquement à des torseurs glisseurs
[28](#ensemble-isolé-soumis-uniquement-à-des-torseurs-glisseurs)](#ensemble-isolé-soumis-uniquement-à-des-torseurs-glisseurs)

[4.6. Synthèse de la démarche de résolution d'un problème d'équilibre
[31](#synthèse-de-la-démarche-de-résolution-dun-problème-déquilibre)](#synthèse-de-la-démarche-de-résolution-dun-problème-déquilibre)

[5. Définir une action mécanique : Point de vue local
[35](#définir-une-action-mécanique-point-de-vue-local)](#définir-une-action-mécanique-point-de-vue-local)

[5.1. Définir une action mécanique : du point de vue local au point de
vue global
[35](#définir-une-action-mécanique-du-point-de-vue-local-au-point-de-vue-global)](#définir-une-action-mécanique-du-point-de-vue-local-au-point-de-vue-global)

[5.2. Torseur des actions mécaniques
[36](#torseur-des-actions-mécaniques)](#torseur-des-actions-mécaniques)

[6. Prise en compte du phénomène de frottement
[40](#prise-en-compte-du-phénomène-de-frottement)](#prise-en-compte-du-phénomène-de-frottement)

[6.1. Frottement en translation
[40](#frottement-en-translation)](#frottement-en-translation)

[6.2. Prise en compte du phénomène de frottement dans une liaison pivot
[45](#prise-en-compte-du-phénomène-de-frottement-dans-une-liaison-pivot)](#prise-en-compte-du-phénomène-de-frottement-dans-une-liaison-pivot)

[6.3. Phénomène d'arc-boutement
[46](#phénomène-darc-boutement)](#phénomène-darc-boutement)

[7. Moment d'une force et Bras de Levier
[46](#moment-dune-force-et-bras-de-levier)](#moment-dune-force-et-bras-de-levier)

[8. Masse -- Centre d'inertie
[50](#masse-centre-dinertie)](#masse-centre-dinertie)

[8.1. Masse [50](#masse)](#masse)

[8.2. Centre d'inertie [50](#centre-dinertie)](#centre-dinertie)

[9. Opérateur d'inertie - Effets d'inertie
[53](#opérateur-dinertie---effets-dinertie)](#opérateur-dinertie---effets-dinertie)

[9.1. Moment d'inertie [53](#moment-dinertie)](#moment-dinertie)

[9.2. Produit d'inertie [54](#produit-dinertie)](#produit-dinertie)

[9.3. L'opérateur d'inertie : la matrice d'inertie d'un solide
\[I~0~(S)\]
[54](#lopérateur-dinertie-la-matrice-dinertie-dun-solide-i0s)](#lopérateur-dinertie-la-matrice-dinertie-dun-solide-i0s)

[9.4. Symétries matérielles
[56](#symétries-matérielles)](#symétries-matérielles)

[9.5. Théorème de Huygens généralisé
[57](#théorème-de-huygens-généralisé)](#théorème-de-huygens-généralisé)

[9.6. Détermination de la matrice d'inertie à partir des résultats
classiques
[59](#détermination-de-la-matrice-dinertie-à-partir-des-résultats-classiques)](#détermination-de-la-matrice-dinertie-à-partir-des-résultats-classiques)

[9.7. Equilibrage dynamique
[63](#equilibrage-dynamique)](#equilibrage-dynamique)

[10. Le théorème de l'énergie cinétique Galiléenne (ou
énergie-puissance)
[63](#le-théorème-de-lénergie-cinétique-galiléenne-ou-énergie-puissance)](#le-théorème-de-lénergie-cinétique-galiléenne-ou-énergie-puissance)

[10.1. Introduction [63](#introduction-1)](#introduction-1)

[10.2. Théorème de l'énergie cinétique Galiléenne (ou théorème énergie
puissance)
[63](#théorème-de-lénergie-cinétique-galiléenne-ou-théorème-énergie-puissance)](#théorème-de-lénergie-cinétique-galiléenne-ou-théorème-énergie-puissance)

[10.3. Démarche de résolution
[64](#démarche-de-résolution-1)](#démarche-de-résolution-1)

[10.4. Torseur cinétique [65](#torseur-cinétique)](#torseur-cinétique)

[10.5. Déterminer l'énergie cinétique d'un solide
[67](#déterminer-lénergie-cinétique-dun-solide)](#déterminer-lénergie-cinétique-dun-solide)

[10.6. Détermination du moment d'inertie équivalent et de la masse
équivalente
[69](#détermination-du-moment-dinertie-équivalent-et-de-la-masse-équivalente)](#détermination-du-moment-dinertie-équivalent-et-de-la-masse-équivalente)

[10.7. Notion de puissance mécanique
[72](#notion-de-puissance-mécanique)](#notion-de-puissance-mécanique)

[10.8. Puissance extérieure
[72](#puissance-extérieure)](#puissance-extérieure)

[10.9. Puissance développée par les actions mutuelles entre deux solides
(P~int~)
[72](#puissance-développée-par-les-actions-mutuelles-entre-deux-solides-pint)](#puissance-développée-par-les-actions-mutuelles-entre-deux-solides-pint)

[10.10. Travail, énergie potentielle et puissance
[75](#travail-énergie-potentielle-et-puissance)](#travail-énergie-potentielle-et-puissance)

[11. Principe Fondamental de la Dynamique
[76](#principe-fondamental-de-la-dynamique)](#principe-fondamental-de-la-dynamique)

[11.1. Enoncé du PFD [76](#enoncé-du-pfd)](#enoncé-du-pfd)

[11.2. Torseur Dynamique [77](#torseur-dynamique)](#torseur-dynamique)

[11.3. Cas simplifiés [78](#cas-simplifiés)](#cas-simplifiés)

[12. Sources [82](#sources)](#sources)

[13. Exercices du chapitre [83](#_Toc126746027)](#_Toc126746027)

[14. EQUILIBRE [84](#equilibre)](#equilibre)

[15. THEOREME DE L'ENERGIE CINETIQUE
[94](#theoreme-de-lenergie-cinetique)](#theoreme-de-lenergie-cinetique)

[16. PFD [128](#pfd)](#pfd)

Choisir et utiliser des démarches et des méthodes pour décrire et
caractériser les actions mécaniques d'un système afin de prévoir son
comportement et/ou de le dimensionner

Etude de l'équilibre

**Je connais :**

+----------------------------------------------------------------+-----+
| -   les différents types d'action mécanique ;                  | ⃝    |
+================================================================+=====+
| -   les torseurs particuliers : torseur couple et torseur      | ⃝    |
|     glisseur ;                                                 |     |
+----------------------------------------------------------------+-----+
| -   le théorème des actions réciproques ;                      | ⃝    |
+----------------------------------------------------------------+-----+
| -   les notions de frottement et d'adhérence et les lois de    | ⃝    |
|     Coulomb;                                                   |     |
+----------------------------------------------------------------+-----+
| -   la notion d'arc-boutement;                                 | ⃝    |
+----------------------------------------------------------------+-----+
| -   les torseurs d'actions mécaniques transmissibles par les   | ⃝    |
|     liaisons usuelles ;                                        |     |
+----------------------------------------------------------------+-----+
| -   le principe fondamental de la statique ;                   | ⃝    |
+----------------------------------------------------------------+-----+
| -   le théorème de la résultante statique et le théorème du    | ⃝    |
|     moment statique                                            |     |
+----------------------------------------------------------------+-----+
| -   les résultats pour les solides soumis au maximum à trois   | ⃝    |
|     actions mécaniques modélisables par des torseurs           |     |
|     glisseurs.                                                 |     |
+----------------------------------------------------------------+-----+

**Je sais :**

+----------------------------------------------------------------+-----+
| -   modéliser une action mécanique au niveau local et au       | ⃝    |
|     > niveau global à l'aide d'un torseur ;                    |     |
+================================================================+=====+
| -   modéliser au niveau local et au niveau global l'action     | ⃝    |
|     > mécanique de contact dans le cas d'une tendance au       |     |
|     > glissement avec adhérence ou d'un glissement avec        |     |
|     > frottement;                                              |     |
+----------------------------------------------------------------+-----+
| -   faire le bilan des actions mécaniques extérieures à un     | ⃝    |
|     > ensemble isolé;                                          |     |
+----------------------------------------------------------------+-----+
| -   simplifier un torseur d'actions mécaniques dans le cas     | ⃝    |
|     > d'un problème plan;                                      |     |
+----------------------------------------------------------------+-----+
| -   utiliser une méthode de résolution adaptée à une           | ⃝    |
|     > problématique.                                           |     |
+----------------------------------------------------------------+-----+

Masse et Inertie

**Je connais :**

+----------------------------------------------------------------+-----+
| -   La définition mathématique de la masse d'un solide ;       | ⃝    |
+================================================================+=====+
| -   La relation permettant de trouver la position du centre    | ⃝    |
|     d'inertie d'un ensemble de solides ;                       |     |
+----------------------------------------------------------------+-----+
| -   La différence entre moment d'inertie et produit d'inertie  | ⃝    |
|     ;                                                          |     |
+----------------------------------------------------------------+-----+
| -   La définition de la matrice d'inertie et ses composantes;  | ⃝    |
+----------------------------------------------------------------+-----+

**Je sais :**

+----------------------------------------------------------------+-----+
| -   déterminer la masse d'un solide homogène ;                 | ⃝    |
+================================================================+=====+
| -   déterminer la position du centre d'inertie d'un solide     | ⃝    |
|     > élémentaire et la position du centre d'inertie d'un      |     |
|     > ensemble de solides;                                     |     |
+----------------------------------------------------------------+-----+
| -   déterminer la forme de la matrice d'inertie d'un solide à  | ⃝    |
|     > partir de sa géométrie et des symétries matérielles;     |     |
+----------------------------------------------------------------+-----+
| -   déplacer la matrice d'inertie avec le théorème de          | ⃝    |
|     > Huygens;                                                 |     |
+----------------------------------------------------------------+-----+
| -   déterminer la résultante cinétique et le moment cinétique. | ⃝    |
+----------------------------------------------------------------+-----+

Théorème de l'énergie cinétique

**Je connais :**

+----------------------------------------------------------------+-----+
| -   La définition de l'énergie cinétique sous forme de         | ⃝    |
|     torseurs ;                                                 |     |
+================================================================+=====+
| -   L'expression des énergies cinétiques pour un mouvement de  | ⃝    |
|     translation et pour un mouvement de rotation ;             |     |
+----------------------------------------------------------------+-----+
| -   La définition de puissance d'une action mécanique sous     | ⃝    |
|     forme de torseurs ;                                        |     |
+----------------------------------------------------------------+-----+
| -   La définition de puissance des inter-efforts;              | ⃝    |
+----------------------------------------------------------------+-----+
| -   Les cas particuliers pour les calculs de puissance;        | ⃝    |
+----------------------------------------------------------------+-----+
| -   Le théorème général de l'énergie cinétique ;               | ⃝    |
+----------------------------------------------------------------+-----+
| -   L'expression des puissances « perdues » à partir des       | ⃝    |
|     rendements ;                                               |     |
+----------------------------------------------------------------+-----+

**Je sais :**

+----------------------------------------------------------------+-----+
| -   déterminer l'énergie cinétique d'un solide ou d'un         | ⃝    |
|     > ensemble de solides ;                                    |     |
+================================================================+=====+
| -   déterminer la puissance développée par une action          | ⃝    |
|     > mécanique;                                               |     |
+----------------------------------------------------------------+-----+
| -   déterminer un moment d'inertie équivalent;                 | ⃝    |
+----------------------------------------------------------------+-----+
| -   appliquer le TGEC pour déterminer une équation de          | ⃝    |
|     > mouvement;                                               |     |
+----------------------------------------------------------------+-----+

Principe Fondamental de la Dynamique

**Je connais :**

+----------------------------------------------------------------+-----+
| -   La définition du torseur dynamique ;                       | ⃝    |
+================================================================+=====+
| -   Les expressions de la résultante dynamique et du moment    | ⃝    |
|     dynamique ainsi que les cas particuliers (point fixe,      |     |
|     centre d'inertie) ;                                        |     |
+----------------------------------------------------------------+-----+
| -   Le PFD sous forme torsorielle et vectorielle ;             | ⃝    |
+----------------------------------------------------------------+-----+

**Je sais :**

+----------------------------------------------------------------+-----+
| -   déterminer le torseur dynamique d'un solide par rapport à  | ⃝    |
|     > un référentiel galiléen;                                 |     |
+================================================================+=====+
| -   appliquer le PFD à un ensemble de solides.                 | ⃝    |
+----------------------------------------------------------------+-----+

## Introduction

On a vu précédement que l'on pouvait, à l'aide d'une simulation
« manuelle» ou assistée par ordinateur, prévoir le comportement
cinématique des systèmes.

Mais cela ne suffit pas pour concevoir un système ou vérifier qu'il
répond bien aux attentes de ses utilisateurs. Il faut aussi s'intéresser
aux **actions mécaniques** auxquelles les constituants de ce système
sont soumis afin de **dimensionner les pièces qui le constituent,
prévoir leurs déformations ou bien déterminer certaines caractéristiques
des actionneurs comme le couple moteur.**

C'est l'application de différents principes qui, après avoir identifié
et caractérisé les différentes actions mécaniques connues et
recherchées, permettent d'étudier la relation de cause à effet entre les
performances d'un système et les actions mécaniques en présence.

## Démarche de résolution pour déterminer les Actions Mécaniques

### Démarche de résolution

La démarche utilisée pour un résoudre une problématique liée à la
détermination d'actions mécaniques sur un système en équilibre, peut se
résumer à :

### Représenter le système : graphe de structure et schéma d'architecture

Un des objectifs, lors de l'étude du comportement statique d'un système,
peut être de valider le dimensionnement des solutions techniques
adoptées par le concepteur du système pour réaliser les liaisons.

Dans ce cas, le schéma cinématique minimal construit à partir du graphe
des liaisons, ne suffit plus.

On utilise alors des outils de représentation qui collent plus à la
réalité technologique du système et qui font apparaître plus clairement
les différents constituants et les actions mécaniques mises en jeu.

Sur le graphe de structure et le schéma architectural figurent :

-   toutes ***les liaisons élémentaires*** sans les regrouper en
    liaisons équivalentes ;

-   ***les actions mécaniques extérieures et intérieures au système***
    (de contact ou à distance) : *couple moteur, pression d'un fluide,
    action d'un ressort, action de la pesanteur...*

Ces outils de représentation ne sont pas normalisés. L'objectif est de
faire apparaitre toutes les informations qui vont ensuite faciliter le
bilan des actions mécaniques lors de l'isolement de solides ou de
groupes de solides !

![](11-Actions Mécaniques/Cours/pandoc/media/image5.png){width="4.979166666666667in"
height="2.4493055555555556in"}***[Exemple :]{.underline}***

*L'ensemble gouvernail barre franche 1 est en liaison pivot d'axe
(A,*$\overrightarrow{z}$*) par rapport à la coque du bateau 0. Lorsque
le pilotage est automatique, l'ensemble 1 est actionné par un vérin
(2+3).*

![](11-Actions Mécaniques/Cours/pandoc/media/image6.png){width="5.232638888888889in"
height="1.9069444444444446in"}

La liaison pivot d'axe (A,$\overrightarrow{z}$) entre 1 et 0 est un
modèle adapté pour une étude du comportement cinématique du système car
Il traduit le mouvement de 1/0 observé sur le système réel.

Dans le cas d'une étude du comportement statique dont l'objectif serait
de dimensionner les solutions techniques qui permettent ce mouvement, il
faut tenir compte des composants technologiques utilisés. En
l'occurrence on utilise deux roulements à billes à contact radial ayant
pour centres de poussée respectifs les points A~1~ et A~2~ éloignés
d'une distance L. On choisit donc de modéliser ces composants
technologiques par une liaison sphérique rotule de centre A~1~ et une
liaison sphère-cylindre de centre A~2~ et de direction
$\overrightarrow{z}$. Cela permettra de déterminer plus facilement les
actions mécaniques exercées sur chacun des roulements à billes.

On ajoute aussi, sur le schéma cinématique et le graphe des liaisons,
des informations sur les actions mécaniques extérieures et intérieures
au système :

-   l'eau exerce une action mécanique sur le gouvernail modélisée
    globalement par une résultante
    $\overset{\rightarrow}{F_{eau \rightarrow 1}} = - F.\overrightarrow{x}$
    au point P ;

-   à l'intérieur du vérin, le fluide sous pression exerce une action
    mécanique sur le corps du vérin 3 ainsi que sur la tige du vérin 2 ;

-   seuls les ensembles 0 et 1 sont soumis à l'action mécanique de la
    pesanteur $\overrightarrow{g}$ (Hypothèse : on néglige cette AM sur
    les solides 2 et 3).

![](11-Actions Mécaniques/Cours/pandoc/media/image7.png){width="5.5in"
height="1.9534722222222223in"}

### Isoler une partie du système

Isoler un solide ou un ensemble de solides revient à définir une
frontière fictive qui englobe cet ensemble isolé et définir ainsi :

-   ***un milieu intérieur*** (qui est dans la frontière), noté
    $\Sigma$ ;

-   ***un milieu extérieur*** (qui est en dehors de la frontière) noté
    $\overline{\Sigma}$ .

Souvent on représente cet isolement avec une frontière. Chaque fois
qu'une action mécanique (AM) coupe cette frontière, on parlera d'action
mécanique extérieure.

**Quand on isole un solide (ou un ensemble de solides) le numéro du (ou
des) solide(s) isolé(s) se trouve toujours à droite.**

+-------+--------------------------------------------------------------+
| >     | **Pilote de bateau**                                         |
| ![](1 |                                                              |
| 1-Act | **Isoler l'ensemble** $\mathbf{\Sigma = 2 + 3}$              |
| ions  |                                                              |
| Mécan | ![](11-Actions Mécanique                                     |
| iques | s/Cours/pandoc/media/image9.png){width="5.895138888888889in" |
| /Cour | height="1.8486111111111112in"}                               |
| s/pan |                                                              |
| doc/m | Bilan des Actions Mécaniques (AM) extérieures à              |
| edia/ | $\Sigma = 2 + 3$ :                                           |
| image |                                                              |
| 8.png | -   AM de $0 \rightarrow 3$ ;                                |
| ){wid |                                                              |
| th="0 | -   AM de $1 \rightarrow 2$  ;                               |
| .6262 |                                                              |
| 69685 | -   AM de $pes \rightarrow 3$ ;                              |
| 03937 |                                                              |
| 01in" | -   AM de $pes \rightarrow 2$;                               |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Démarche de résolution : Stratégie d'isolement

Les systèmes mécaniques sont souvent conçus de telle façon à avoir une
loi entrée-sortie en effort : un effecteur est soumis à un effort qui se
transmet de solides en solides jusqu'à l'actionneur (souvent un moteur
ou un vérin), qui compense cet effort. Il est parfois nécessaire de
faire plusieurs isolements, à des sous-systèmes différents, afin de
déterminer les AM recherchées. Deux stratégies sont possibles :

-   Le calcul complet de toutes les AM possibles entre les solides, en
    isolant chacun des solides à l'exception du bâti. Ceci amène à 6 x
    (nombre de solides -- 1) équations pour un problème 3D. C'est le
    calcul que fait généralement un logiciel non optimisé.

-   L'application de **certaines équations** (parfois une seule)
    uniquement à certains sous-systèmes judicieusement choisis afin
    d'obtenir les efforts inconnus désirés avec le moins de calculs
    possibles.

Remarque : **On n'isole jamais le bâti** ou un système comprenant le
bâti, car le bâti est relié par liaison complète à un « support », et
cela fait 6 inconnues statiques qui empêchent la résolution des autres
inconnues recherchées.

Grâce au graphe de structure, il faut essayer de trouver par quels
systèmes passer pour aller des données connues jusqu'à celle recherchée,
en un minimum d'isolements et en un minimum d'équations. Un isolement
permet de trouver des relations entre les différentes AM extérieures à
l'ensemble isolé.

1.  Il faut commencer par rechercher les **systèmes soumis à 2 AM de
    type résultantes**, car on peut immédiatement en déduire la droite
    support de ces forces (et du coup éliminer des inconnues - une
    inconnue statique après isolement)

2.  Déterminer le nombre d'inconnues statiques de liaisons pour chaque
    isolement (elles doivent être inférieures ou égales à 6)

3.  Déterminer le « chemin » pour aller des AM connues aux AM à
    déterminer.

##### Rappel sur les inconnues de liaisons {#rappel-sur-les-inconnues-de-liaisons .unnumbered}

  ------------------------------------------------------------------------
  Ic         Is           Liaisons
  ---------- ------------ ------------------------------------------------
  1          5            Pivot, glissière, hélicoïdale

  2          4            Pivot glissant, sphérique à doigt

  3          3            Appui-plan, sphérique

  4          2            Cylindre-plan, sphère-cylindre

  5          1            Sphère-plan
  ------------------------------------------------------------------------

![](11-Actions Mécaniques/Cours/pandoc/media/image10.png){width="2.96875in"
height="1.2872342519685038in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image12.png){width="0.7472222222222222in"
height="0.5916666666666667in"}Pour une liaison hélicoïdale, il n'y a
qu'une seule inconnue cinématique indépendante puisque la translation
est liée à la rotation par le pas de la vis.

+-------+--------------------------------------------------------------+
| >     | **Grue de port**                                             |
| ![](1 |                                                              |
| 1-Act | **Donner une stratégie d'isolement pour déterminer l'effort  |
| ions  | du vérin sur le bras 2**                                     |
| Mécan | $\over                                                       |
| iques | rightarrow{\mathbf{R}_{\mathbf{1}\mathbf{b \rightarrow 2}}}$ |
| /Cour | **afin de maintenir la grue en équilibre par rapport à       |
| s/pan | l'effort de pesanteur.**                                     |
| doc/m |                                                              |
| edia/ | ![](11-Acti                                                  |
| image | ons Mécaniques/Cours/pandoc/media/image13.png){width="2.4in" |
| 8.png | height="2.30625i                                             |
| ){wid | n"}![](11-Actions Mécaniques/Cours/pandoc/media/image15.png) |
| th="0 |                                                              |
| .6262 | +---------------------------+----------------------------+   |
| 69685 | | **Isolement 1**           | **Isolement 2**            |   |
| 03937 | +===========================+============================+   |
| 01in" | | ![](11-Acti               | ![](11-A                   |   |
| >     | | ons Mécaniques/Cours/pand | ctions Mécaniques/Cours/pa |   |
| heigh | | oc/media/image13.png){wid | ndoc/media/image13.png){wi |   |
| t="0. | | th="1.6833333333333333in" | dth="1.6833333333333333in" |   |
| 65083 | | heig                      | hei                        |   |
| 33333 | | ht="1.617577646544182in"} | ght="1.617577646544182in"} |   |
| 33333 | |                           |                            |   |
| 4in"} | | $$\Sigma = 1a + 1b$$      | $$\Sigma = 2$$             |   |
|       | |                           |                            |   |
|       | | 10 inconnues statiques    | 5+1 = 6 inconnues          |   |
|       | | (réduites à 2 car deux AM | statiques                  |   |
|       | | de type glisseur)         |                            |   |
|       | |                           | Cet isolement permet       |   |
|       | | Cet isolement est soumis  | d'avoir une relation entre |   |
|       | | à deux AM de type         | l'AM                       |   |
|       | | glisseur et permet de     | $\mathbf{pe                |   |
|       | | diminuer le nombre        | s} \rightarrow \mathbf{2}$ |   |
|       | | d'inconnues statiques     | et                         |   |
|       | |                           | $\mathbf{1                 |   |
|       | |                           | b} \rightarrow \mathbf{2}$ |   |
|       | +---------------------------+----------------------------+   |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Pilote de bateau**                                         |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mécanique                                     |
| ions  | s/Cours/pandoc/media/image9.png){width="3.441666666666667in" |
| Mécan | height="1.8486111111111112in"}![](11-Actions Mécaniques/C    |
| iques | ours/pandoc/media/image16.jpeg){width="2.3916666666666666in" |
| /Cour | height="1.8509416010498687in"}                               |
| s/pan |                                                              |
| doc/m | **Déterminer la force délivrée par le vérin**                |
| edia/ | ${\overrightarrow{\mathbf{F}}}_{\mathbf{v}}$ **en fonction   |
| image | de la force de l'eau sur le gouvernail**                     |
| 8.png | ${\overr                                                     |
| ){wid | ightarrow{\mathbf{F}}}_{\mathbf{eau}\mathbf{\rightarrow 1}}$ |
| th="0 |                                                              |
| .6262 | ![](11-Actions Mécaniques/C                                  |
| 69685 | ours/pandoc/media/image16.jpeg){width="2.3916666666666666in" |
| 03937 | height="1.8506944444444444in"}![](11-Actions Mécaniques/C    |
| 01in" | ours/pandoc/media/image16.jpeg){width="2.3916666666666666in" |
| >     | height="1.8509416010498687in"}                               |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | ![Image5](11-Actio                                           |
| ![](1 | ns Mécaniques/Cours/pandoc/media/image17.jpeg){width="2.5in" |
| 1-Act | height="1.925in"}**Poussoir et coulisseau**                  |
| ions  |                                                              |
| Mécan | On associe les repères :                                     |
| iques |                                                              |
| /Cour | > \-                                                         |
| s/pan | > $R_{0}(O,\overset{\rightarrow}{x_{0}}                      |
| doc/m | ,\overset{\rightarrow}{y_{0}},\overset{\rightarrow}{z_{0}})$ |
| edia/ | > au bâti 0, tel que                                         |
| image | >                                                            |
| 8.png | $\overset{\rightarrow}{OB} = b.\overset{\rightarrow}{x_{0}}$ |
| ){wid | >                                                            |
| th="0 | > \-                                                         |
| .6262 | > $R_{1}(O,\overset{\rightarrow}{x_{1}}                      |
| 69685 | ,\overset{\rightarrow}{y_{1}},\overset{\rightarrow}{z_{1}})$ |
| 03937 | > au poussoir 1, tels que                                    |
| 01in" | > $\over                                                     |
| >     | set{\rightarrow}{BA} = \lambda.\overset{\rightarrow}{y_{0}}$ |
| heigh | > et                                                         |
| t="0. | > $\alpha =                                                  |
| 65083 | (\overset{\rightarrow}{x_{0}},\overset{\rightarrow}{x_{1}})$ |
| 33333 |                                                              |
| 33333 | Un système non représenté assure le maintien du contact du   |
| 4in"} | coulisseau 2 avec le poussoir 1 au point A.                  |
|       |                                                              |
|       | Le poussoir 1 est soumis au couple moteur $C_{m}$ et le      |
|       | piston 2 à l'action                                          |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image18.wmf) de |
|       | pression du fluide.                                          |
|       |                                                              |
|       | On suppose le problème plan, les liaisons sans frottement et |
|       | on néglige les effets d'inertie et de la pesanteur.          |
|       |                                                              |
|       | **L'objectif de l'étude est de déterminer une relation entre |
|       | F et** $\mathbf{C}_{\mathbf{m}}$ **lorsque le système est en |
|       | équilibre.**                                                 |
|       |                                                              |
|       | **Donner une stratégie d'isolement pour déterminer une       |
|       | relation entre le couple moteur** $\mathbf{C}_{\mathbf{m}}$  |
|       | **et l'effort** $\mathbf{F}$**.**                            |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Recenser les actions mécaniques

On définit :

-   des **actions mécaniques extérieures** qui correspondent à toutes
    > les actions mécaniques exercées par le milieu extérieur
    > $\overline{\Sigma}$ (solide, fluide, ressort, pesanteur, ...) et
    > qui agissent **SUR** un des éléments du milieu intérieur $\Sigma$.

-   des **actions mécaniques intérieures** qui correspondent à toutes
    > les actions mécaniques exercées par un élément (solide, fluide,
    > ressort, ...) appartenant au milieu intérieur $\Sigma$ et qui agit
    > sur un autre élément du milieu intérieur $\Sigma$.

Pour ***recenser les actions mécaniques extérieures***, on utilise ***le
graphe des structures*** sur lequel on vient directement ***entourer
l'ensemble isolé***.

Chaque trait coupé par notre frontière d'étude correspond à une action
mécanique extérieure que l'on décrit littéralement : AM de
![](11-Actions Mécaniques/Cours/pandoc/media/image19.wmf)
($i \in \overline{\Sigma}$ et $j \in \Sigma$)

Chacune de ces actions mécaniques est ensuite modélisée à l'aide d'un
torseur d'action mécanique : *\
*$$\left\{ T_{i \rightarrow j} \right\} = \begin{Bmatrix}
\overrightarrow{R_{i \rightarrow j}} \\
\overrightarrow{M_{A,i \rightarrow j}}
\end{Bmatrix}_{A}$$

Lors de cette étape, on s'attachera à vérifier la présence ou non
***d'hypothèses couramment utilisées ***:

-   ***action de la pesanteur négligeable*** (lorsque la norme du poids
    des pièces est négligeable devant l'intensité des autres actions
    mécaniques) ;

-   ***liaisons parfaites***.

La somme de ces torseurs forme le torseur des actions mécaniques
extérieures à
![](11-Actions Mécaniques/Cours/pandoc/media/image20.wmf) :

![](11-Actions Mécaniques/Cours/pandoc/media/image21.wmf) *n est le
nombre d'actions mécaniques extérieures*

+-------+--------------------------------------------------------------+
| >     | **Pilote de bateau**                                         |
| ![](1 |                                                              |
| 1-Act | **Isoler l'ensemble** $\mathbf{\Sigma = 2 + 3}$              |
| ions  |                                                              |
| Mécan | ![](11-Actions Mécanique                                     |
| iques | s/Cours/pandoc/media/image9.png){width="5.895138888888889in" |
| /Cour | height="1.8486111111111112in"}                               |
| s/pan |                                                              |
| doc/m | Bilan des actions mécaniques extérieures à                   |
| edia/ | $\Sigma = 2 + 3$ :                                           |
| image |                                                              |
| 8.png | -   AM de $0 \rightarrow 3$ (par l'intermédiaire d'une       |
| ){wid |     liaison sphérique de centre C) ;                         |
| th="0 |                                                              |
| .6262 | -   AM de $1 \rightarrow 2$ (par l'intermédiaire d'une       |
| 69685 |     liaison sphérique de centre B) ;                         |
| 03937 |                                                              |
| 01in" | -   AM de $pes \rightarrow 3$ (négligée) ;                   |
| >     |                                                              |
| heigh | -   AM de $pes \rightarrow 2$ (négligée) ;                   |
| t="0. |                                                              |
| 65083 | Sous forme de torseur :                                      |
| 33333 |                                                              |
| 33333 | $$\left\{ T_{0 \rightarrow 3} \right\} = \begin{Bmatrix}     |
| 4in"} | \overrightarrow{R_{0 \rightarrow 3}} \\                      |
|       | \overrightarrow{M_{C,0 \rightarrow 3}}                       |
|       | \end{Bmatri                                                  |
|       | x}_{C}\left\{ T_{1 \rightarrow 2} \right\} = \begin{Bmatrix} |
|       | \overrightarrow{R_{1 \rightarrow 2}} \\                      |
|       | \overrightarrow{M_{B,1 \rightarrow 2}}                       |
|       | \end{Bmatrix}_{B}$$                                          |
|       |                                                              |
|       | Donc :                                                       |
|       | $\left\{ T_{\over                                            |
|       | line{\Sigma} \rightarrow \Sigma} \right\} = \left\{ T_{0 \ri |
|       | ghtarrow 3} \right\} + \left\{ T_{1 \rightarrow 2} \right\}$ |
|       |                                                              |
|       | Attention, il faudra les exprimer au même point.             |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

Mais pour continuer il faut savoir associer des torseurs aux actions
mécaniques... Et choisir la bonne méthode de résolution (équilibre, PFD,
TECG).

## ![](11-Actions Mécaniques/Cours/pandoc/media/image22.png){width="1.5298611111111111in" height="2.970833333333333in"}Actions mécaniques

### Définition

On apelle Action Mécanique (AM), toute cause capable de :

-   **provoquer** ou **modifier le mouvement** d'un solide ;

-   **provoquer la déformation** d'un solide ;

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image23.jpeg){width="1.0006944444444446in"
    height="1.382638888888889in"}**et éventuellement maintenir à
    l'équilibre**

![](11-Actions Mécaniques/Cours/pandoc/media/image24.png){width="1.3222222222222222in"
height="1.0152777777777777in"}![](11-Actions Mécaniques/Cours/pandoc/media/image25.png){width="1.0333333333333334in"
height="1.28125in"}

On distingue :

-   les **actions mécaniques à distance**. Elles agissent sur tout le
    volume du solide. [Exemple :]{.underline} actions magnétiques,
    action de la pesanteur...

```{=html}
<!-- -->
```
-   les **actions mécaniques de contact**. Elles agissent directement
    sur la surface du solide.

[Exemples :]{.underline} pression d'un fluide, action de contact entre
deux solides...

Qu'elle soit à distance ou de contact, une AM a toujours une origine et
une cible. On utilisera donc la notation :
![](11-Actions Mécaniques/Cours/pandoc/media/image26.wmf)

**[Exemple :]{.underline}**

-   action de la pesanteur sur le solide 3 : $p \rightarrow 3$

-   action du solide 4 sur le solide 2 : $4 \rightarrow 2$

-   action d'un moteur sur le solide 1 : $m \rightarrow 1$

### Torseurs d'AM particuliers : Torseur glisseur, Torseur couple

+----------------------------------+-----------------------------------+
| **[Torseurs d'AM                 |                                   |
| particuliers :]{.underline}**    |                                   |
+==================================+===================================+
| Un torseur dont le ***moment est | Un torseur dont la ***résultante  |
| nul*** est appelé ***[torseur    | est nulle*** est appelé           |
| glisseur]{.underline}*** :       | ***[torseur                       |
|                                  | couple]{.underline}*** :          |
| $$\boxed{\left\{ T_{1 \rightarr  |                                   |
| ow 2} \right\} = \begin{Bmatrix} | $$\boxed{\left\{ T_{1 \rightar    |
| \overri                          | row 2} \right\} = \begin{Bmatrix} |
| ghtarrow{R_{1 \rightarrow 2}} \\ | \overrightarrow{0} \\             |
| \overrightarrow{0}               | \over                             |
| \end{Bmatrix}_{J}}$$             | rightarrow{M_{J,1 \rightarrow 2}} |
|                                  | \end{Bmatrix}_{J}}$$              |
| Cela signifie que l'action       |                                   |
| mécanique de $1 \rightarrow 2$   | Ce torseur reste le même pour     |
| ne va pas provoquer, modifier ou | tous les points de l'espace       |
| empêcher un mouvement de         | (invariant). En effet :           |
| rotation du solide 2 autour du   |                                   |
| point J.                         | $$\ov                             |
|                                  | errightarrow{M_{I,1 \rightarrow 2 |
| Exemples de torseur glisseur :   | }} = \overrightarrow{M_{J,1 \righ |
|                                  | tarrow 2}} + \overrightarrow{IJ}  |
| Pesanteur, effort d'un vérin,    | \land \underset{= \overrightarrow |
| ressort de traction,...          | {0}}{\overset{\overrightarrow{R_{ |
|                                  | 1 \rightarrow 2}}}{︸}} = \overri |
|                                  | ghtarrow{M_{j,1 \rightarrow 2}}$$ |
|                                  |                                   |
|                                  | Exemples de torseur couple :      |
|                                  |                                   |
|                                  | Couple moteur, ressort de         |
|                                  | torsion, couple de frottement     |
+----------------------------------+-----------------------------------+

### Théorème des actions réciproques

Le solide isolé (ou ensemble de solides) est toujours le solide (ou
ensemble de solides) à droite. Lorsqu'on passe d'un solide (ou ensemble
de solides) à un autre, le théorème des actions réciproques est
utilisé :

**Théorème des actions réciproques :**
$\boxed{\left\{ T_{1 \rightarrow 2} \right\} = - \left\{ T_{2 \rightarrow 1} \right\}}$

Il est donc à connaître...

### Cas de l'action mécanique de la pesanteur

Bien qu'elle puisse être parfois être négligée, l'action mécanique de la
pesanteur est présente dans toutes les études du comportement des
systèmes.

Nous nous limiterons cependant aux cas des solides homogènes,
c\'est-à-dire aux solides pour lesquels la masse volumique est constante
:

![](11-Actions Mécaniques/Cours/pandoc/media/image27.wmf) solide,
![](11-Actions Mécaniques/Cours/pandoc/media/image28.wmf)

  ---------------------------------------------------------------------------------------------------------
  *[Quelques ordres de          **Acier**       ![](11-Actions Mécaniques/Cours/pandoc/media/image29.wmf)
  grandeur :]{.underline}*                      
  ----------------------------- --------------- -----------------------------------------------------------
                                **Aluminium**   ![](11-Actions Mécaniques/Cours/pandoc/media/image30.wmf)

                                **PVC**         ![](11-Actions Mécaniques/Cours/pandoc/media/image31.wmf)
  ---------------------------------------------------------------------------------------------------------

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image32.jpeg){width="2.564583333333333in"
    height="2.1805555555555554in"}**[Point de vue local]{.underline}**

L'action de la pesanteur sur un solide 1 est une action mécanique à
distance. Le champ de force associé est tel que :

![](11-Actions Mécaniques/Cours/pandoc/media/image33.wmf)
$d\overrightarrow{F_{pes \rightarrow 1}(P)} = dm \cdot \overrightarrow{g} = \rho \cdot dv \cdot \overrightarrow{g}$

![](11-Actions Mécaniques/Cours/pandoc/media/image34.wmf)est appelé
champ de pesanteur :

-   Il est orienté suivant la verticale ascendante ;

-   sa norme est
    $\boxed{\left\| \overrightarrow{g} \right\| = g = 9,81m \cdot s^{- 2}}$.

```{=html}
<!-- -->
```
-   **[Point de vue global]{.underline}**

La ***résultante*** de l'action de la pesanteur sur 1 est telle que :

$\overrightarrow{R_{pes \rightarrow 1}} = \int_{V_{1}}^{}{d\overrightarrow{F_{pes \rightarrow 1}(P)}} = \int_{V_{1}}^{}{\rho \cdot dv \cdot \overrightarrow{g}} = \rho \cdot \overrightarrow{g} \cdot \int_{V_{1}}^{}{dv} = \rho \cdot \overrightarrow{g} \cdot V_{1} = \boxed{m_{1} \cdot \overrightarrow{g}}$
![](11-Actions Mécaniques/Cours/pandoc/media/image35.wmf)

Le ***moment résultant***, au point J, de l'action de la pesanteur sur 1
est tel que :

$$\overrightarrow{M_{J,pes \rightarrow 1}} = \int_{V_{1}}^{}\left( \overrightarrow{JP} \land \rho \cdot \overrightarrow{g} \right) \cdot dv = \int_{V_{1}}^{}{\overrightarrow{JP} \cdot dv \land \rho \cdot \overrightarrow{g}}$$

Il existe un point $G_{1}$, appelé ***centre de gravité*** du solide 1,
tel que :
$\int_{V_{1}}^{}{\overrightarrow{G_{1}P} \cdot dv} = \overrightarrow{0}$

Ainsi :
$\overrightarrow{M_{G_{1},pes \rightarrow 1}} = \int_{V_{1}}^{}{\overrightarrow{G_{1}P} \cdot dv \land \rho \cdot \overrightarrow{g}} = \overrightarrow{0}$

La position de ce centre de gravité (barycentre des masses élémentaires)
peut être trouvée grâce à :

$\overrightarrow{OG_{1}} = \frac{1}{V_{1}}\int_{V_{1}}^{}{\overrightarrow{OP} \cdot dv}$
ou
$\overrightarrow{OG_{1}} = \frac{1}{m_{1}}\int_{V_{1}}^{}{\overrightarrow{OP} \cdot dm}$
($m_{1} = \rho \cdot V_{1}etdm = \rho \cdot dv$)

En
effet :$\overrightarrow{0} = \int_{V_{1}}^{}{\overrightarrow{G_{1}P} \cdot dv} = \int_{V_{1}}^{}{\left( \overrightarrow{G_{1}O} + \overrightarrow{OP} \right) \cdot dv} = \int_{V_{1}}^{}{\overrightarrow{G_{1}O} \cdot dv} + \int_{V_{1}}^{}{\overrightarrow{OP} \cdot dv} = \overrightarrow{G_{1}O} \cdot V_{1} + \int_{V_{1}}^{}{\overrightarrow{OP} \cdot dv}$

![](11-Actions Mécaniques/Cours/pandoc/media/image36.png){width="3.3604166666666666in"
height="1.5465277777777777in"}$\Rightarrow \overrightarrow{OG_{1}} \cdot V_{1} = \int_{V_{1}}^{}{\overrightarrow{OP} \cdot dv}$

**Le centre de gravité est toujours situé sur les éléments de symétrie
du solide : point, plan, droite...**

*Dans le cas du pare-brise :* $G_{1}$ *est dans le plan*
$(O,\overrightarrow{y_{1}},\overrightarrow{z_{1}})$*.*Le
***[torseur]{.underline}***, au point $G_{1}$, de l'action de la
pesanteur sur 1 est un glisseur tel que :

![](11-Actions Mécaniques/Cours/pandoc/media/image37.wmf)

![600px-Panneau_attention](11-Actions Mécaniques/Cours/pandoc/media/image38.png){width="0.375in"
height="0.3177088801399825in"}**Il faut retenir que la pesanteur est un
torseur glisseur, qui est toujours exprimé dans le repère galiléen
(associé au bâti en général en ATS).**

### Actions mécaniques particulières à connaître

Il y a des actions mécaniques qu'il faut absolument connaître car elles
sont très utilisées

##### Action mécanique de la pesanteur {#action-mécanique-de-la-pesanteur .unnumbered}

L'action mécanique de la pesanteur, comme vu précédemment, peut être
modélisée par un torseur glisseur, exprimé au centre de gravité du
solide (ou d'un ensemble de solides). Il est **toujours exprimé dans le
repère galiléen** (associé au bâti en général en ATS).

![](11-Actions Mécaniques/Cours/pandoc/media/image39.wmf)![](11-Actions Mécaniques/Cours/pandoc/media/image40.jpeg){width="3.2810728346456695in"
height="1.0958398950131234in"}

##### Action mécanique de l'effort de pression {#action-mécanique-de-leffort-de-pression .unnumbered}

L'effort de pression, en général pour les vérins, est fonction de la
pression et de la surface du piston (éventuellement de la tige).

![](11-Actions Mécaniques/Cours/pandoc/media/image41.wmf)![](11-Actions Mécaniques/Cours/pandoc/media/image42.jpeg){width="2.9523239282589677in"
height="1.1439534120734909in"}

+-------+--------------------------------------------------------------+
| >     | **Vérin**                                                    |
| ![](1 |                                                              |
| 1-Act | Un vérin permettant d'actionner une pince est commandé en    |
| ions  | alimentant la chambre arrière (diamètre du piston            |
| Mécan | $D_{p} = 50\mspace{6mu} mm$ et diamètre de sa tige           |
| iques | $D_{t} = 18\mspace{6mu} mm$) avec la pression p~H~ .         |
| /Cour |                                                              |
| s/pan | Dans cette position, la chambre avant du vérin est toujours  |
| doc/m | alimentée avec une pression $p_{0} = 6\mspace{6mu} bar$ (1   |
| edia/ | bar =10^5^Pa). L'axe du vérin est noté y~3~. L'effort exercé |
| image | par le vérin est égal à 220N.                                |
| 8.png |                                                              |
| ){wid | **Déterminer, le modèle de l'action mécanique de la          |
| th="0 | pression** $\mathbf{p}_{\mathbf{H}}$ **sur la tige du vérin  |
| .6262 | en fonction de la surface du                                 |
| 69685 | piston**$\mathbf{S}_{\mathbf{p}}$**, de la surface occupée   |
| 03937 | par la tige** $\mathbf{S}_{\mathbf{t}}$**, de**              |
| 01in" | $\mathbf{p}_{\mathbf{H}}$ **et de**                          |
| >     | $\mathbf{p}_{\mathbf{0}}$ **. (Faire un dessin)**            |
| heigh |                                                              |
| t="0. | > $\                                                         |
| 65083 | left\{ T_{p_{H} \rightarrow tige} \right\} = \begin{Bmatrix} |
| 33333 | > \left( p_{H} \cdot S_{p} - p_{0} \                         |
| 33333 | cdot (S_{p} - S_{t}) \right) \cdot \overrightarrow{y_{3}} \\ |
| 4in"} | > \overrightarrow{0}                                         |
|       | > \end{Bmatrix}$                                             |
|       |                                                              |
|       | **En déduire la valeur de** $\mathbf{p}_{\mathbf{H}}$        |
|       | **exprimée en bar.**                                         |
|       |                                                              |
|       | On a $S_{p} = \pi \cdot \frac{{D_{p}}^{2}}{4}$ : surface du  |
|       | piston et $S_{t} = \pi \cdot \frac{{D_{t}}^{2}}{4}$ :        |
|       | surface de la tige                                           |
|       |                                                              |
|       | Donc :                                                       |
|       |                                                              |
|       | $$p_{H} = \frac{6 \cdot 10^{5}                               |
|       | \cdot \frac{\pi}{4} \cdot \left( (50 \cdot 10^{- 3})^{2} - ( |
|       | 18 \cdot 10^{- 3})^{2} \right) + 220}{\pi \cdot \frac{(50 \c |
|       | dot 10^{- 3})^{2}}{4}} \Rightarrow \boxed{p_{H} = ... bar}$$ |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

##### Action mécanique pour un ressort de traction {#action-mécanique-pour-un-ressort-de-traction .unnumbered}

L'action mécanique modélisation un ressort de traction est un torseur
glisseur dont la direction de l'effort est celle du ressort.

![](11-Actions Mécaniques/Cours/pandoc/media/image43.wmf)![](11-Actions Mécaniques/Cours/pandoc/media/image44.jpeg){width="2.7729516622922135in"
height="1.6417913385826772in"}

##### Action mécanique pour un couple moteur {#action-mécanique-pour-un-couple-moteur .unnumbered}

Outre les vérins vus précédemment, un des actionneurs les plus utilisé
est une machine tournante (souvent utilisée en moteur). Dans ce cas-là,
l'action mécanique est modélisée par un torseur couple, dont le moment
suivant l'axe de la pivot correspond au couple utile, souvent confondu
avec le couple électromagnétique, et noté C~m~.

![](11-Actions Mécaniques/Cours/pandoc/media/image45.wmf)

**Remarque** : Pour une charge, on peut aussi avoir un torseur couple
pour le couple résistant (négatif par convention).

##### Action mécanique pour un ressort de de torsion {#action-mécanique-pour-un-ressort-de-de-torsion .unnumbered}

Pour un ressort de torsion, nous avons le cas dual du ressort de
traction. Au lieu d'avoir un effort fonction du déplacement, il y a un
moment fonction de la variation angulaire. La raideur k est en N.m/rad.

![](11-Actions Mécaniques/Cours/pandoc/media/image46.wmf)

### Actions mécaniques transmissibles par les liaisons usuelles

![](11-Actions Mécaniques/Cours/pandoc/media/image47.jpeg){width="1.375in"
height="1.9583333333333333in"}

Dans un système, les solides exercent des actions mécaniques sur les
autres solides avec qui ils sont en contact. On dit alors qu'***ils
transmettent des actions mécaniques par l'intermédiaire des liaisons.***

***[Exemple :]{.underline}** Sur le pont ci-contre, une partie du poids
du pont est transmise aux haubans, qui eux même le transmettent au mât.*

-   **[Hypothèse de liaisons parfaites]{.underline}**

Sauf si le contraire est précisé, on considère que le ***contact***
entre les surfaces des solides en liaison se fait ***sans adhérence ni
frottement***. En l'absence de frottement, ***la puissance dissipée***
par échauffement au niveau de la liaison entre deux solides est
***supposée nulle***.

On admet l'expression de la puissance développée, au niveau de la
liaison entre deux solides 1 et 2, par les actions mécaniques transmises
par cette liaison :

$P(1 \leftrightarrow 2) = \left\{ T_{1 \rightarrow 2} \right\} \otimes \left\{ V_{2/1} \right\} = \begin{Bmatrix}
\overrightarrow{R_{1 \rightarrow 2}} \\
\overrightarrow{M_{J,1 \rightarrow 2}}
\end{Bmatrix}_{J} \otimes \begin{Bmatrix}
\overrightarrow{\Omega_{2/1}} \\
\overrightarrow{V_{J \in 2/1}}
\end{Bmatrix}_{J}$
(![](11-Actions Mécaniques/Cours/pandoc/media/image48.wmf) :
« comoment »)

Le comoment défini ci-dessus, qui se détaille à partir des éléments de
réduction des deux torseurs, doit donc être nul :
$P(1 \leftrightarrow 2) = \overrightarrow{R_{1 \rightarrow 2}} \cdot \overrightarrow{V_{J \in 2/1}} + \overrightarrow{M_{J,1 \rightarrow 2}} \cdot \overrightarrow{\Omega_{2/1}} = 0$

Le détail de ces deux produits scalaires conduit à la somme de 6 termes
indépendants de même signe qui doivent tous être nuls.

On en déduit ainsi, par ***dualité avec la forme des torseurs
cinématiques***, la forme des ***[torseurs d'actions mécaniques
transmissibles par les liaisons usuelles]{.underline}*** supposées sans
frottement :

-   pour ***chaque degrés de liberté supprimé***, il existe ***une
    composante d'action mécanique*** susceptible d'être transmise par la
    liaison ;

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image49.png){width="1.4in"
    > height="0.6430293088363954in"}réciproquement, aucune composante
    > d'action mécanique ne peut être transmise là ou un mouvement
    > relatif est possible.

[Exemple :]{.underline} Liaison glissière de direction
$\overrightarrow{x}$ entre 1 et 2.

![](11-Actions Mécaniques/Cours/pandoc/media/image50.png){width="6.524255249343832in"
height="2.466666666666667in"}

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ***Nom et description géométrique***                                                                                                                     ***Forme du torseur cinématique***                          ***Forme du torseur d'action mécanique transmissible***
  --------------------------------------------------------------- ---------------------------------------------------------------------------------------- ----------------------------------------------------------- -----------------------------------------------------------
  **GLISSIERE de direction**                                      ![](11-Actions Mécaniques/Cours/pandoc/media/image55.png){width="0.8951388888888889in"   ![](11-Actions Mécaniques/Cours/pandoc/media/image56.wmf)   ![](11-Actions Mécaniques/Cours/pandoc/media/image57.wmf)
  ![](11-Actions Mécaniques/Cours/pandoc/media/image54.wmf)       height="0.6513888888888889in"}                                                                                                                       

                                                                                                                                                           *Pour tout point A*                                         

  **APPUI PLAN de normale**                                       ![](11-Actions Mécaniques/Cours/pandoc/media/image59.png){width="0.9069444444444444in"   ![](11-Actions Mécaniques/Cours/pandoc/media/image60.wmf)   ![](11-Actions Mécaniques/Cours/pandoc/media/image61.wmf)
  ![](11-Actions Mécaniques/Cours/pandoc/media/image58.wmf)       height="0.8375in"}                                                                                                                                   

                                                                                                                                                           *Pour tout point A*                                         

  **CYLINDRE-PLAN (ou LINEAIRE RECTILIGNE) de contact**           ![](11-Actions Mécaniques/Cours/pandoc/media/image63.png){width="0.8840277777777777in"   ![](11-Actions Mécaniques/Cours/pandoc/media/image64.wmf)   ![](11-Actions Mécaniques/Cours/pandoc/media/image65.wmf)
  ![](11-Actions Mécaniques/Cours/pandoc/media/image62.wmf)**et   height="0.8722222222222222in"}                                                                                                                       
  de normale**                                                                                                                                                                                                         
  ![](11-Actions Mécaniques/Cours/pandoc/media/image58.wmf)                                                                                                                                                            

                                                                                                                                                           *Pour tout point A appartenant au plan*                     
                                                                                                                                                           ![](11-Actions Mécaniques/Cours/pandoc/media/image66.wmf)   

  **SPHERE-PLAN (ou PONCTUELLE) de contact O et de normale**      ![](11-Actions Mécaniques/Cours/pandoc/media/image67.png){width="0.8486111111111111in"   ![](11-Actions Mécaniques/Cours/pandoc/media/image68.wmf)   ![](11-Actions Mécaniques/Cours/pandoc/media/image69.wmf)
  ![](11-Actions Mécaniques/Cours/pandoc/media/image58.wmf)       height="0.7909722222222222in"}                                                                                                                       

                                                                                                                                                           *Pout tout point appartenant à la normale*                  
                                                                                                                                                           ![](11-Actions Mécaniques/Cours/pandoc/media/image70.wmf)   

  **PIVOT GLISSANT d'axe**                                        ![](11-Actions Mécaniques/Cours/pandoc/media/image71.png){width="0.9534722222222223in"   ![](11-Actions Mécaniques/Cours/pandoc/media/image72.wmf)   ![](11-Actions Mécaniques/Cours/pandoc/media/image73.wmf)
  ![](11-Actions Mécaniques/Cours/pandoc/media/image62.wmf)       height="0.8020833333333334in"}                                                                                                                       

                                                                                                                                                           *Pour tout point A appartenant à l'axe*                     
                                                                                                                                                           ![](11-Actions Mécaniques/Cours/pandoc/media/image74.wmf)   

  **PIVOT d'axe**                                                 ![](11-Actions Mécaniques/Cours/pandoc/media/image75.png){width="0.9770833333333333in"   ![](11-Actions Mécaniques/Cours/pandoc/media/image76.wmf)   ![](11-Actions Mécaniques/Cours/pandoc/media/image77.wmf)
  ![](11-Actions Mécaniques/Cours/pandoc/media/image62.wmf)       height="0.8138888888888889in"}                                                                                                                       

                                                                                                                                                           *Pour tout point A appartenant à l'axe*                     
                                                                                                                                                           ![](11-Actions Mécaniques/Cours/pandoc/media/image78.wmf)   
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bien entendu, on peut aussi utiliser une écriture en ligne de ces
torseurs :

> $$\boxed{\left\{ T_{1 \rightarrow 2} \right\} = \begin{Bmatrix}
> \overrightarrow{R_{1 \rightarrow 2}} \\
> \overrightarrow{M_{A,1 \rightarrow 2}}
> \end{Bmatrix}_{A} = \begin{Bmatrix}
> X_{1 \rightarrow 2} \cdot \overrightarrow{x} + Y_{1 \rightarrow 2} \cdot \overrightarrow{y} + Z_{1 \rightarrow 2} \cdot \overrightarrow{z} \\
> L_{A,1 \rightarrow 2} \cdot \overrightarrow{x} + M_{A,1 \rightarrow 2} \cdot \overrightarrow{y} + N_{A,1 \rightarrow 2} \cdot \overrightarrow{z}
> \end{Bmatrix}_{A}}$$

+-------------+-----------+-------------------+-----------------------+
| ***Nom et   |           | ***Forme du       | ***Forme du torseur   |
| description |           | torseur           | d'action mécanique    |
| géo         |           | cinématique***    | transmissible***      |
| métrique*** |           |                   |                       |
+=============+===========+===================+=======================+
| **          | ![](1     | ![](11            | ![](11-Actions        |
| HELICOIDALE | 1-Actions | -Actions Mécaniqu | Mécaniques/Cours/pand |
| d'axe**     |  Mécaniqu | es/Cours/pandoc/m | oc/media/image81.wmf) |
| ![          | es/Cours/ | edia/image80.wmf) |                       |
| ](11-Action | pandoc/me |                   |                       |
| s Mécanique | dia/image |                   |                       |
| s/Cours/pan | 79.png){w |                   |                       |
| doc/media/i | idth="0.7 |                   |                       |
| mage62.wmf) | 909722222 |                   |                       |
|             | 222222in" |                   |                       |
|             | hei       |                   |                       |
|             | ght="0.62 |                   |                       |
|             | 777777777 |                   |                       |
|             | 77778in"} |                   |                       |
+-------------+-----------+-------------------+-----------------------+
|             |           | *Pour tout point  |                       |
|             |           | A appartenant à   |                       |
|             |           | l'axe*            |                       |
|             |           | ![](11            |                       |
|             |           | -Actions Mécaniqu |                       |
|             |           | es/Cours/pandoc/m |                       |
|             |           | edia/image82.wmf) |                       |
|             |           |                   |                       |
|             |           | ***p : pas de la  |                       |
|             |           | liaison***        |                       |
+-------------+-----------+-------------------+-----------------------+
| **SPHERIQUE | ![](1     | ![](11            | ![](11-Actions        |
| (ou ROTULE) | 1-Actions | -Actions Mécaniqu | Mécaniques/Cours/pand |
| de centre   |  Mécaniqu | es/Cours/pandoc/m | oc/media/image85.wmf) |
| O**         | es/Cours/ | edia/image84.wmf) |                       |
|             | pandoc/me |                   |                       |
|             | dia/image |                   |                       |
|             | 83.png){w |                   |                       |
|             | idth="1.1 |                   |                       |
|             | 513888888 |                   |                       |
|             | 888888in" |                   |                       |
|             | hei       |                   |                       |
|             | ght="0.62 |                   |                       |
|             | 777777777 |                   |                       |
|             | 77778in"} |                   |                       |
+-------------+-----------+-------------------+-----------------------+
|             |           | *Seulement au     |                       |
|             |           | point O*          |                       |
+-------------+-----------+-------------------+-----------------------+
| **SPHERIQUE | ![](1     | ![](11            | ![](11-Actions        |
| A DOIGT (ou | 1-Actions | -Actions Mécaniqu | Mécaniques/Cours/pand |
| ROTULE A    |  Mécaniqu | es/Cours/pandoc/m | oc/media/image89.wmf) |
| DOIGT) de   | es/Cours/ | edia/image88.wmf) |                       |
| centre O et | pandoc/me |                   |                       |
| de rotation | dia/image |                   |                       |
| interdite** | 87.png){w |                   |                       |
| ![          | idth="1.1 |                   |                       |
| ](11-Action | 743055555 |                   |                       |
| s Mécanique | 555555in" |                   |                       |
| s/Cours/pan | hei       |                   |                       |
| doc/media/i | ght="0.65 |                   |                       |
| mage86.wmf) | 138888888 |                   |                       |
|             | 88889in"} |                   |                       |
+-------------+-----------+-------------------+-----------------------+
|             |           | *Seulement au     |                       |
|             |           | point O*          |                       |
+-------------+-----------+-------------------+-----------------------+
| **SPHE      | ![](1     | ![](11            | ![](11-Actions        |
| RE-CYLINDRE | 1-Actions | -Actions Mécaniqu | Mécaniques/Cours/pand |
| (ou         |  Mécaniqu | es/Cours/pandoc/m | oc/media/image92.wmf) |
| LINEAIRE    | es/Cours/ | edia/image91.wmf) |                       |
| ANNULAIRE)  | pandoc/me |                   |                       |
| de centre O | dia/image |                   |                       |
| et de       | 90.png){w |                   |                       |
| direction** | idth="0.9 |                   |                       |
| ![          | 534722222 |                   |                       |
| ](11-Action | 222223in" |                   |                       |
| s Mécanique | hei       |                   |                       |
| s/Cours/pan | ght="0.79 |                   |                       |
| doc/media/i | 097222222 |                   |                       |
| mage54.wmf) | 22222in"} |                   |                       |
+-------------+-----------+-------------------+-----------------------+
|             |           | *Seulement au     |                       |
|             |           | point O*          |                       |
+-------------+-----------+-------------------+-----------------------+

***Cas particulier de la liaison hélicoïdale :***

Pour cette liaison, la dualité entre la forme du torseur cinématique et
la forme du torseur d'action mécanique transmissible est moins évidente.

*[Rappel :]{.underline} cette liaison n'admet **qu'un seul degré de
liberté**. La translation et la rotation n'étant pas indépendantes.*

On cherche la forme du torseur d'action mécanique transmissible qui
assure une puissance développée au niveau de la liaison qui soit nulle :

$$P(1 \leftrightarrow 2) = \overrightarrow{R_{1 \rightarrow 2}} \cdot \overrightarrow{V_{J \in 2/1}} + \overrightarrow{M_{J,1 \rightarrow 2}} \cdot \overrightarrow{\Omega_{2/1}} = 0$$

Ce qui nous conduit, entre autres, à :
$\mspace{6mu} \pm X_{1 \rightarrow 2} \cdot \omega_{x,2/1} \cdot \frac{p}{2\pi} + L_{A,1 \rightarrow 2} \cdot \omega_{x,2/1} = 0$

Donc :
$\boxed{L_{A,1 \rightarrow 2} = \pm X_{1 \rightarrow 2} \cdot \frac{p}{2\pi}}$
le signe ![](11-Actions Mécaniques/Cours/pandoc/media/image93.wmf)dépend
du type de liaison hélicoïdale (pas à droite ou pas à gauche)

###  {#section .unnumbered}

+-------+--------------------------------------------------------------+
| >     | **Entrainement torseur d'AM transmissible**                  |
| ![](1 |                                                              |
| 1-Act | **Donner les torseurs d'AM transmissibles des liaisons       |
| ions  | suivantes**                                                  |
| Mécan |                                                              |
| iques | $L_{2/1}\ $: Liaison appui-plan de normale                   |
| /Cour | $(A,\overrightarrow{x_{0}})$                                 |
| s/pan |                                                              |
| doc/m | $\ L_{4/3}\ $: Liaison pivot d'axe                           |
| edia/ | $(B,\overrightarrow{y_{2}})$                                 |
| image |                                                              |
| 8.png | $L_{2/0}\ $: Liaison glissière de direction                  |
| ){wid | $(C,\overrightarrow{z_{3}})$                                 |
| th="0 |                                                              |
| .6262 | $L_{5/3}\ $: Liaison cylindre-plan de normale                |
| 69685 | $\left( P,\overrightarrow{z_{4}} \right)\ $ et d'axe         |
| 03937 | $\overrightarrow{x_{4}}$                                     |
| 01in" |                                                              |
| >     | $L_{6/2}\ $: Liaison sphérique de centre $D$                 |
| heigh |                                                              |
| t="0. | $L_{8/3}\ $: Liaison sphère-cylindre d'axe                   |
| 65083 | $\left( Q,\overrightarrow{z_{2}} \right)\ $                  |
| 33333 |                                                              |
| 33333 | $L_{8/3}\ $: Liaison hélicoïdale d'axe                       |
| 4in"} | $\left( M,\overrightarrow{z_{6}} \right)\ $                  |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Cas particulier d'un problème plan

On peut admettre que l'on est face à un problème « plan » si :

-   la **géométrie des liaisons** du système **présente un** **plan de
    symétrie,**

-   les **AM extérieures** exercées sur ce système **sont symétriques
    par rapport à ce plan**, c'est à dire que :

> \- les résultantes des AM extérieures sont parallèles au plan de
> symétrie,
>
> \- les moments des AM extérieures sont perpendiculaires au plan de
> symétrie.

-   Le système est représenté dans le plan

Dans le cas d'un **problème plan**, l'application de l'équilibre ne peut
fournir au maximum que **3 équations scalaires** :

-   ***2 équations issues du théorème de la résultante*** statique
    projeté sur les 2 axes de la base appartenant au plan ;

-   ***1 équation issue du théorème du moment statique*** projeté sur le
    3^ème^ axe de la base (perpendiculaire au plan).

+---+--------------------+-----------------------+--------------------+---+
| * |                    |                       |                    |   |
| * |                    |                       |                    |   |
| E |                    |                       |                    |   |
| x |                    |                       |                    |   |
| e |                    |                       |                    |   |
| m |                    |                       |                    |   |
| p |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| * |                    |                       |                    |   |
| * |                    |                       |                    |   |
+===+====================+=======================+====================+===+
| ! |                    |                       |                    |   |
| [ |                    |                       |                    |   |
| ] |                    |                       |                    |   |
| ( |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| - |                    |                       |                    |   |
| A |                    |                       |                    |   |
| c |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| s |                    |                       |                    |   |
|   |                    |                       |                    |   |
| M |                    |                       |                    |   |
| é |                    |                       |                    |   |
| c |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| i |                    |                       |                    |   |
| q |                    |                       |                    |   |
| u |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| C |                    |                       |                    |   |
| o |                    |                       |                    |   |
| u |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| p |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| d |                    |                       |                    |   |
| o |                    |                       |                    |   |
| c |                    |                       |                    |   |
| / |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| d |                    |                       |                    |   |
| i |                    |                       |                    |   |
| a |                    |                       |                    |   |
| / |                    |                       |                    |   |
| i |                    |                       |                    |   |
| m |                    |                       |                    |   |
| a |                    |                       |                    |   |
| g |                    |                       |                    |   |
| e |                    |                       |                    |   |
| 9 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| . |                    |                       |                    |   |
| p |                    |                       |                    |   |
| n |                    |                       |                    |   |
| g |                    |                       |                    |   |
| ) |                    |                       |                    |   |
| { |                    |                       |                    |   |
| w |                    |                       |                    |   |
| i |                    |                       |                    |   |
| d |                    |                       |                    |   |
| t |                    |                       |                    |   |
| h |                    |                       |                    |   |
| = |                    |                       |                    |   |
| " |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| . |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 5 |                    |                       |                    |   |
| 6 |                    |                       |                    |   |
| 9 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| 4 |                    |                       |                    |   |
| i |                    |                       |                    |   |
| n |                    |                       |                    |   |
| " |                    |                       |                    |   |
| h |                    |                       |                    |   |
| e |                    |                       |                    |   |
| i |                    |                       |                    |   |
| g |                    |                       |                    |   |
| h |                    |                       |                    |   |
| t |                    |                       |                    |   |
| = |                    |                       |                    |   |
| " |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| . |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 9 |                    |                       |                    |   |
| 6 |                    |                       |                    |   |
| 5 |                    |                       |                    |   |
| 2 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| 7 |                    |                       |                    |   |
| i |                    |                       |                    |   |
| n |                    |                       |                    |   |
| " |                    |                       |                    |   |
| } |                    |                       |                    |   |
| P |                    |                       |                    |   |
| o |                    |                       |                    |   |
| u |                    |                       |                    |   |
| r |                    |                       |                    |   |
| c |                    |                       |                    |   |
| e |                    |                       |                    |   |
| p |                    |                       |                    |   |
| r |                    |                       |                    |   |
| o |                    |                       |                    |   |
| b |                    |                       |                    |   |
| l |                    |                       |                    |   |
| è |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| p |                    |                       |                    |   |
| l |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| ! |                    |                       |                    |   |
| [ |                    |                       |                    |   |
| ] |                    |                       |                    |   |
| ( |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| - |                    |                       |                    |   |
| A |                    |                       |                    |   |
| c |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| s |                    |                       |                    |   |
|   |                    |                       |                    |   |
| M |                    |                       |                    |   |
| é |                    |                       |                    |   |
| c |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| i |                    |                       |                    |   |
| q |                    |                       |                    |   |
| u |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| C |                    |                       |                    |   |
| o |                    |                       |                    |   |
| u |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| p |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| d |                    |                       |                    |   |
| o |                    |                       |                    |   |
| c |                    |                       |                    |   |
| / |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| d |                    |                       |                    |   |
| i |                    |                       |                    |   |
| a |                    |                       |                    |   |
| / |                    |                       |                    |   |
| i |                    |                       |                    |   |
| m |                    |                       |                    |   |
| a |                    |                       |                    |   |
| g |                    |                       |                    |   |
| e |                    |                       |                    |   |
| 9 |                    |                       |                    |   |
| 5 |                    |                       |                    |   |
| . |                    |                       |                    |   |
| w |                    |                       |                    |   |
| m |                    |                       |                    |   |
| f |                    |                       |                    |   |
| ) |                    |                       |                    |   |
| , |                    |                       |                    |   |
| t |                    |                       |                    |   |
| o |                    |                       |                    |   |
| u |                    |                       |                    |   |
| s |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| t |                    |                       |                    |   |
| o |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| e |                    |                       |                    |   |
| u |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| d |                    |                       |                    |   |
| ' |                    |                       |                    |   |
| A |                    |                       |                    |   |
| M |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| t |                    |                       |                    |   |
| l |                    |                       |                    |   |
| a |                    |                       |                    |   |
| f |                    |                       |                    |   |
| o |                    |                       |                    |   |
| r |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
|   |                    |                       |                    |   |
| : |                    |                       |                    |   |
|   |                    |                       |                    |   |
| ! |                    |                       |                    |   |
| [ |                    |                       |                    |   |
| ] |                    |                       |                    |   |
| ( |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| - |                    |                       |                    |   |
| A |                    |                       |                    |   |
| c |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| s |                    |                       |                    |   |
|   |                    |                       |                    |   |
| M |                    |                       |                    |   |
| é |                    |                       |                    |   |
| c |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| i |                    |                       |                    |   |
| q |                    |                       |                    |   |
| u |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| C |                    |                       |                    |   |
| o |                    |                       |                    |   |
| u |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| p |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| d |                    |                       |                    |   |
| o |                    |                       |                    |   |
| c |                    |                       |                    |   |
| / |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| d |                    |                       |                    |   |
| i |                    |                       |                    |   |
| a |                    |                       |                    |   |
| / |                    |                       |                    |   |
| i |                    |                       |                    |   |
| m |                    |                       |                    |   |
| a |                    |                       |                    |   |
| g |                    |                       |                    |   |
| e |                    |                       |                    |   |
| 9 |                    |                       |                    |   |
| 6 |                    |                       |                    |   |
| . |                    |                       |                    |   |
| w |                    |                       |                    |   |
| m |                    |                       |                    |   |
| f |                    |                       |                    |   |
| ) |                    |                       |                    |   |
+---+--------------------+-----------------------+--------------------+---+
| E |                    |                       |                    |   |
| n |                    |                       |                    |   |
| g |                    |                       |                    |   |
| é |                    |                       |                    |   |
| n |                    |                       |                    |   |
| é |                    |                       |                    |   |
| r |                    |                       |                    |   |
| a |                    |                       |                    |   |
| l |                    |                       |                    |   |
| , |                    |                       |                    |   |
| i |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| t |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| n |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| n |                    |                       |                    |   |
| é |                    |                       |                    |   |
| d |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| s |                    |                       |                    |   |
| l |                    |                       |                    |   |
| ' |                    |                       |                    |   |
| é |                    |                       |                    |   |
| n |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| c |                    |                       |                    |   |
| é |                    |                       |                    |   |
| d |                    |                       |                    |   |
| ' |                    |                       |                    |   |
| u |                    |                       |                    |   |
| n |                    |                       |                    |   |
| e |                    |                       |                    |   |
| x |                    |                       |                    |   |
| e |                    |                       |                    |   |
| r |                    |                       |                    |   |
| c |                    |                       |                    |   |
| i |                    |                       |                    |   |
| c |                    |                       |                    |   |
| e |                    |                       |                    |   |
| q |                    |                       |                    |   |
| u |                    |                       |                    |   |
| e |                    |                       |                    |   |
| l |                    |                       |                    |   |
| ' |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| t |                    |                       |                    |   |
| f |                    |                       |                    |   |
| a |                    |                       |                    |   |
| c |                    |                       |                    |   |
| e |                    |                       |                    |   |
| à |                    |                       |                    |   |
| u |                    |                       |                    |   |
| n |                    |                       |                    |   |
| p |                    |                       |                    |   |
| r |                    |                       |                    |   |
| o |                    |                       |                    |   |
| b |                    |                       |                    |   |
| l |                    |                       |                    |   |
| è |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| p |                    |                       |                    |   |
| l |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| . |                    |                       |                    |   |
| M |                    |                       |                    |   |
| a |                    |                       |                    |   |
| i |                    |                       |                    |   |
| s |                    |                       |                    |   |
| i |                    |                       |                    |   |
| l |                    |                       |                    |   |
| f |                    |                       |                    |   |
| a |                    |                       |                    |   |
| u |                    |                       |                    |   |
| t |                    |                       |                    |   |
| ê |                    |                       |                    |   |
| t |                    |                       |                    |   |
| r |                    |                       |                    |   |
| e |                    |                       |                    |   |
| c |                    |                       |                    |   |
| a |                    |                       |                    |   |
| p |                    |                       |                    |   |
| a |                    |                       |                    |   |
| b |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| d |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| i |                    |                       |                    |   |
| m |                    |                       |                    |   |
| p |                    |                       |                    |   |
| l |                    |                       |                    |   |
| i |                    |                       |                    |   |
| f |                    |                       |                    |   |
| i |                    |                       |                    |   |
| e |                    |                       |                    |   |
| r |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| t |                    |                       |                    |   |
| o |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| e |                    |                       |                    |   |
| u |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| d |                    |                       |                    |   |
| ' |                    |                       |                    |   |
| A |                    |                       |                    |   |
| M |                    |                       |                    |   |
| e |                    |                       |                    |   |
| n |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| n |                    |                       |                    |   |
| u |                    |                       |                    |   |
| l |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| t |                    |                       |                    |   |
| c |                    |                       |                    |   |
| e |                    |                       |                    |   |
| r |                    |                       |                    |   |
| t |                    |                       |                    |   |
| a |                    |                       |                    |   |
| i |                    |                       |                    |   |
| n |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| c |                    |                       |                    |   |
| o |                    |                       |                    |   |
| m |                    |                       |                    |   |
| p |                    |                       |                    |   |
| o |                    |                       |                    |   |
| s |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| t |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| d |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| é |                    |                       |                    |   |
| l |                    |                       |                    |   |
| é |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| n |                    |                       |                    |   |
| t |                    |                       |                    |   |
| s |                    |                       |                    |   |
| d |                    |                       |                    |   |
| e |                    |                       |                    |   |
| r |                    |                       |                    |   |
| é |                    |                       |                    |   |
| d |                    |                       |                    |   |
| u |                    |                       |                    |   |
| c |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| . |                    |                       |                    |   |
|   |                    |                       |                    |   |
| * |                    |                       |                    |   |
| * |                    |                       |                    |   |
| * |                    |                       |                    |   |
| L |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| c |                    |                       |                    |   |
| o |                    |                       |                    |   |
| m |                    |                       |                    |   |
| p |                    |                       |                    |   |
| o |                    |                       |                    |   |
| s |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| t |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| à |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| n |                    |                       |                    |   |
| u |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| t |                    |                       |                    |   |
| c |                    |                       |                    |   |
| e |                    |                       |                    |   |
| l |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| q |                    |                       |                    |   |
| u |                    |                       |                    |   |
| i |                    |                       |                    |   |
| c |                    |                       |                    |   |
| o |                    |                       |                    |   |
| r |                    |                       |                    |   |
| r |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| p |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| d |                    |                       |                    |   |
| e |                    |                       |                    |   |
| n |                    |                       |                    |   |
| t |                    |                       |                    |   |
| à |                    |                       |                    |   |
| d |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| a |                    |                       |                    |   |
| c |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| s |                    |                       |                    |   |
| m |                    |                       |                    |   |
| é |                    |                       |                    |   |
| c |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| i |                    |                       |                    |   |
| q |                    |                       |                    |   |
| u |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| s |                    |                       |                    |   |
| u |                    |                       |                    |   |
| s |                    |                       |                    |   |
| c |                    |                       |                    |   |
| e |                    |                       |                    |   |
| p |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| b |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| d |                    |                       |                    |   |
| e |                    |                       |                    |   |
| f |                    |                       |                    |   |
| a |                    |                       |                    |   |
| i |                    |                       |                    |   |
| r |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| o |                    |                       |                    |   |
| r |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| r |                    |                       |                    |   |
| l |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| s |                    |                       |                    |   |
| o |                    |                       |                    |   |
| l |                    |                       |                    |   |
| i |                    |                       |                    |   |
| d |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| d |                    |                       |                    |   |
| u |                    |                       |                    |   |
| p |                    |                       |                    |   |
| l |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| * |                    |                       |                    |   |
| * |                    |                       |                    |   |
| * |                    |                       |                    |   |
+---+--------------------+-----------------------+--------------------+---+
|   | **Problème plan**  | **Problème plan**     | **Problème plan**  |   |
|   | ![]                | ![](11-Actions        | ![]                |   |
|   | (11-Actions Mécani | Mécaniques/Cours/pand | (11-Actions Mécani |   |
|   | ques/Cours/pandoc/ | oc/media/image98.wmf) | ques/Cours/pandoc/ |   |
|   | media/image97.wmf) |                       | media/image99.wmf) |   |
+---+--------------------+-----------------------+--------------------+---+
| ! |                    | ![](11-Actions M      | ![](               |   |
| [ |                    | écaniques/Cours/pando | 11-Actions Mécaniq |   |
| ] |                    | c/media/image102.wmf) | ues/Cours/pandoc/m |   |
| ( |                    |                       | edia/image104.wmf) |   |
| 1 |                    | ![](11-Actions M      |                    |   |
| 1 |                    | écaniques/Cours/pando | ![](               |   |
| - |                    | c/media/image103.wmf) | 11-Actions Mécaniq |   |
| A |                    |                       | ues/Cours/pandoc/m |   |
| c |                    |                       | edia/image105.wmf) |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| s |                    |                       |                    |   |
|   |                    |                       |                    |   |
| M |                    |                       |                    |   |
| é |                    |                       |                    |   |
| c |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| i |                    |                       |                    |   |
| q |                    |                       |                    |   |
| u |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| C |                    |                       |                    |   |
| o |                    |                       |                    |   |
| u |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| p |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| d |                    |                       |                    |   |
| o |                    |                       |                    |   |
| c |                    |                       |                    |   |
| / |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| d |                    |                       |                    |   |
| i |                    |                       |                    |   |
| a |                    |                       |                    |   |
| / |                    |                       |                    |   |
| i |                    |                       |                    |   |
| m |                    |                       |                    |   |
| a |                    |                       |                    |   |
| g |                    |                       |                    |   |
| e |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| 0 |                    |                       |                    |   |
| 0 |                    |                       |                    |   |
| . |                    |                       |                    |   |
| w |                    |                       |                    |   |
| m |                    |                       |                    |   |
| f |                    |                       |                    |   |
| ) |                    |                       |                    |   |
|   |                    |                       |                    |   |
| ! |                    |                       |                    |   |
| [ |                    |                       |                    |   |
| ] |                    |                       |                    |   |
| ( |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| - |                    |                       |                    |   |
| A |                    |                       |                    |   |
| c |                    |                       |                    |   |
| t |                    |                       |                    |   |
| i |                    |                       |                    |   |
| o |                    |                       |                    |   |
| n |                    |                       |                    |   |
| s |                    |                       |                    |   |
|   |                    |                       |                    |   |
| M |                    |                       |                    |   |
| é |                    |                       |                    |   |
| c |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| i |                    |                       |                    |   |
| q |                    |                       |                    |   |
| u |                    |                       |                    |   |
| e |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| C |                    |                       |                    |   |
| o |                    |                       |                    |   |
| u |                    |                       |                    |   |
| r |                    |                       |                    |   |
| s |                    |                       |                    |   |
| / |                    |                       |                    |   |
| p |                    |                       |                    |   |
| a |                    |                       |                    |   |
| n |                    |                       |                    |   |
| d |                    |                       |                    |   |
| o |                    |                       |                    |   |
| c |                    |                       |                    |   |
| / |                    |                       |                    |   |
| m |                    |                       |                    |   |
| e |                    |                       |                    |   |
| d |                    |                       |                    |   |
| i |                    |                       |                    |   |
| a |                    |                       |                    |   |
| / |                    |                       |                    |   |
| i |                    |                       |                    |   |
| m |                    |                       |                    |   |
| a |                    |                       |                    |   |
| g |                    |                       |                    |   |
| e |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| 0 |                    |                       |                    |   |
| 1 |                    |                       |                    |   |
| . |                    |                       |                    |   |
| w |                    |                       |                    |   |
| m |                    |                       |                    |   |
| f |                    |                       |                    |   |
| ) |                    |                       |                    |   |
+---+--------------------+-----------------------+--------------------+---+
|   |                    |                       |                    |   |
+---+--------------------+-----------------------+--------------------+---+

## Etude de l'équilibre d'un système 

### Etude de l'équilibre : Principe de la Statique

La condition nécessaire pour qu'un ***ensemble isolé***
![](11-Actions Mécaniques/Cours/pandoc/media/image106.wmf) ***soit en
équilibre*** par rapport à un repère galiléen est que ***la somme des
torseurs des actions mécaniques extérieures à***
![](11-Actions Mécaniques/Cours/pandoc/media/image106.wmf) ***soit
nulle*** :

![](11-Actions Mécaniques/Cours/pandoc/media/image107.wmf) pour tout
point A

Cette équation torsorielle conduit à 2 équations vectorielles :

-   **[Théorème de la résultante statique (TRS) :]{.underline}**
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image108.wmf)

-   **[Théorème du moment statique (TMS) :]{.underline}**
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image109.wmf)

Après avoir exprimé les différents vecteurs dans la même base
![](11-Actions Mécaniques/Cours/pandoc/media/image110.wmf), chacune de
ces équations vectorielles conduit à 3 ***équations scalaires***, soit
***6 au total*** :

![](11-Actions Mécaniques/Cours/pandoc/media/image111.wmf)

![](11-Actions Mécaniques/Cours/pandoc/media/image10.png){width="4.1875in"
height="1.8909722222222223in"}

### Démarche de résolution d'un problème pour étudier l'équilibre

![](11-Actions Mécaniques/Cours/pandoc/media/image112.jpeg){width="4.016666666666667in"
height="1.875in"}Dans tous les cas, pour étudier l'équilibre d'un
système, un graphe de structure est réalisé.

Une démarche possible pour résoudre la problématique posée est :

1.  Modéliser le système et établir le graphe des liaisons puis le
    > graphe de structure;

2.  Déterminer un isolement coupant la liaison aux inconnues recherchées
    > et **coupant le moins de liaisons non recherchées (nombre
    > d'inconnues statiques coupées inférieur ou égal au nombre
    > d'équations)**;

3.  Faire le Bilan des AM extérieures (BAME);

4.  Identifier les AM données et les AM recherchées ;

5.  Regarder si une relation peut être trouvée avec le Théorème de la
    > Résultante Statique. Si oui, il faut projeter (avec un produit
    > scalaire) les différentes résultantes et résoudre les équations
    > scalaires. Si non, il faut déplacer les torseurs.

6.  Choisir le point de réduction et les équations ne sollicitant pas
    > les inconnues non recherchées ;

7.  Ecrire le système d'équations en appliquant le TRS et/ou le TMS.
    > S'il ne peut être résolu, identifier les inconnues à rechercher et
    > proposer un nouvel isolement intelligent (coupant des inconnues
    > déjà trouvées).

### Conseils pour le choix du point de réduction

Choisir le point de réduction et les équations ne sollicitant pas les
inconnues non recherchées :

-   éviter de déplacer un torseur contenant beaucoup d'inconnues
    d'effort,

-   projeter sur des directions particulières.

### Inventaire (ou bilan) des actions mécaniques extérieurs (BAME) 

On définit :

-   des **actions mécaniques extérieures** qui correspondent à toutes
    > les actions mécaniques exercées par le milieu extérieur
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image113.wmf)
    > (solide, fluide, ressort, pesanteur, ...) et qui agissent **SUR**
    > un des éléments du milieu
    > intérieur![](11-Actions Mécaniques/Cours/pandoc/media/image20.wmf).

-   des **actions mécaniques intérieures** qui correspondent à toutes
    > les actions mécaniques exercées par un élément (solide, fluide,
    > ressort, ...) appartenant au milieu intérieur
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image20.wmf) et qui
    > agit sur un autre élément du milieu
    > intérieur![](11-Actions Mécaniques/Cours/pandoc/media/image20.wmf).

+-------+--------------------------------------------------------------+
| >     | **Console de bateau**                                        |
| ![](1 |                                                              |
| 1-Act | ***[Exemple :]{.underline}*** On choisit d'isoler un         |
| ions  | ensemble                                                     |
| Mécan | ![](11-Actions Mécaniques/Cours/pandoc/media/image114.wmf)   |
| iques |                                                              |
| /Cour | ![](11-Actions Mécanique                                     |
| s/pan | s/Cours/pandoc/media/image9.png){width="5.895138888888889in" |
| doc/m | height="1.8486111111111112in"}                               |
| edia/ |                                                              |
| image | Bilan des actions mécaniques extérieures à                   |
| 8.png | ![](11-Actions Mécaniques/Cours/pandoc/media/image114.wmf) : |
| ){wid |                                                              |
| th="0 | -   AM de                                                    |
| .6262 |     ![                                                       |
| 69685 | ](11-Actions Mécaniques/Cours/pandoc/media/image115.wmf)(par |
| 03937 |     l'intermédiaire d'une liaison sphérique de centre C) ;   |
| 01in" |                                                              |
| >     | -   AM de                                                    |
| heigh |     ![                                                       |
| t="0. | ](11-Actions Mécaniques/Cours/pandoc/media/image116.wmf)(par |
| 65083 |     l'intermédiaire d'une liaison sphérique de centre B) ;   |
| 33333 |                                                              |
| 33333 | -   AM de                                                    |
| 4in"} |                                                              |
|       |   ![](11-Actions Mécaniques/Cours/pandoc/media/image117.wmf) |
|       |     (négligée) ;                                             |
|       |                                                              |
|       | -   AM de                                                    |
|       |                                                              |
|       |   ![](11-Actions Mécaniques/Cours/pandoc/media/image118.wmf) |
|       |     (négligée) ;                                             |
|       |                                                              |
|       | Sous forme de torseur :                                      |
|       |                                                              |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image119.wmf)   |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image120.wmf)   |
|       |                                                              |
|       | Donc :                                                       |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image121.wmf)   |
|       |                                                              |
|       | ***[Exemple ]{.underline}:** Pilote automatique de bateau*   |
|       |                                                              |
|       | Le théorème du moment statique nous donne :                  |
|       |                                                              |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image122.wmf)   |
|       | Or                                                           |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image123.wmf)   |
|       |                                                              |
|       | et                                                           |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image124.wmf)   |
|       |                                                              |
|       | Donc                                                         |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image125.wmf)   |
|       |                                                              |
|       | Cette application du PFS ne nous permet pas de terminer      |
|       | parfaitement toutes les composantes inconnues du torseur     |
|       | d'AM de                                                      |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image116.wmf)   |
|       | mais les résultats obtenus seront utilisés plus tard pour    |
|       | répondre à une problématique concrète.                       |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Ensemble isolé soumis uniquement à des torseurs glisseurs

Dans un problème plan, le bilan des actions mécaniques peut dans
certains cas nous conduire à recenser ***au maximum 3 actions mécaniques
extérieures*** modélisables par des ***torseurs glisseurs***.

**Il faut utiliser les résultats ci-dessous car ils permettent de
résoudre rapidement certains problèmes. Il faut notamment repérer les
solides soumis à deux glisseurs (vérins, bielles, \...).**

Dans ces conditions, on pourra utiliser les résultats suivants :

+-----------------------------------------------------------------------+
| **ENSEMBLE ISOLE SOUMIS A 2 GLISSEURS**                               |
+=======================================================================+
| Si un ensemble isolé est en équilibre sous l'action de 2 glisseurs    |
| alors :                                                               |
|                                                                       |
| -   **ces 2 glisseurs sont opposés (même norme, même direction, sens  |
|     > contraire)**                                                    |
|                                                                       |
| -   **ces 2 glisseurs ont comme même direction : la droite d'action   |
|     > passant par les points ou sont exprimés les 2 torseurs          |
|     > glisseurs**                                                     |
+-----------------------------------------------------------------------+

**[Exemple :]{.underline}** Coffre motorisé d'Audi A8

![](11-Actions Mécaniques/Cours/pandoc/media/image126.png){width="2.44375in"
height="2.0347222222222223in"}Problème plan
![](11-Actions Mécaniques/Cours/pandoc/media/image127.wmf)

[Hypothèse :]{.underline} l'action de la pesanteur est négligeable sur
toutes les pièces sauf sur le coffre 28.

On isole la bielle 22, BAME à 22 :

-   action de ![](11-Actions Mécaniques/Cours/pandoc/media/image128.wmf)

-   action de ![](11-Actions Mécaniques/Cours/pandoc/media/image129.wmf)

-   action de
    ![](11-Actions Mécaniques/Cours/pandoc/media/image130.wmf) :
    négligée

En tenant compte des simplifications liées au problème plan dans
l'écriture des torseurs d'actions mécaniques transmissibles par les
liaisons pivot en D et C :

![](11-Actions Mécaniques/Cours/pandoc/media/image131.wmf)et
![](11-Actions Mécaniques/Cours/pandoc/media/image132.wmf)

![](11-Actions Mécaniques/Cours/pandoc/media/image133.png){width="3.8361111111111112in"
height="1.1993055555555556in"}Ces deux torseurs sont des torseurs
glisseurs, on a donc :

![](11-Actions Mécaniques/Cours/pandoc/media/image134.wmf)

et ![](11-Actions Mécaniques/Cours/pandoc/media/image135.wmf)

En effet, le théorème du moment statique nous donne :
![](11-Actions Mécaniques/Cours/pandoc/media/image138.wmf)

Or ![](11-Actions Mécaniques/Cours/pandoc/media/image139.wmf)et
![](11-Actions Mécaniques/Cours/pandoc/media/image140.wmf)

+-----------------------------------------------------------------------+
| **ENSEMBLE ISOLE SOUMIS A 3 GLISSEURS**                               |
+=======================================================================+
| Si un ensemble isolé est en équilibre sous l'action de 3 glisseurs    |
| alors :                                                               |
|                                                                       |
| -   **ces 3 glisseurs sont coplanaires**                              |
|                                                                       |
| -   **les directions de ces 3 glisseurs sont concourantes ou          |
|     > parallèles**                                                    |
|                                                                       |
| -   **la somme vectorielle de ces 3 glisseurs est nulle**             |
+-----------------------------------------------------------------------+

**[Exemple :]{.underline}** Coffre motorisé d'Audi A8

On isole le coffre 28, BAME à 28 :

-   action de $22 \rightarrow 28$ (direction (CD) déterminée en isolant
    la bielle 22)

-   action de $25 \rightarrow 22$

-   action de $pes \rightarrow 28$ (norme, sens et direction connues)

En tenant compte des simplifications liées au problème plan dans
l'écriture des torseurs d'actions mécaniques transmissibles par la
liaison pivot en B et C :

![](11-Actions Mécaniques/Cours/pandoc/media/image141.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image142.wmf)

De plus on a :
![](11-Actions Mécaniques/Cours/pandoc/media/image143.wmf)

Ces trois torseurs sont des torseurs glisseurs, on a donc :

![](11-Actions Mécaniques/Cours/pandoc/media/image144.png){width="2.3465277777777778in"
height="2.501388888888889in"}![](11-Actions Mécaniques/Cours/pandoc/media/image145.wmf)et
![](11-Actions Mécaniques/Cours/pandoc/media/image146.wmf)

On connait ![](11-Actions Mécaniques/Cours/pandoc/media/image147.wmf),
on peut donc trouver *J* et en déduire 
![](11-Actions Mécaniques/Cours/pandoc/media/image148.wmf)

![](11-Actions Mécaniques/Cours/pandoc/media/image149.png){width="2.7555555555555555in"
height="1.1861111111111111in"}On connait
![](11-Actions Mécaniques/Cours/pandoc/media/image150.wmf), on peut donc
déterminer ![](11-Actions Mécaniques/Cours/pandoc/media/image151.wmf)

> ***Ces résultats, pour les ensembles isolés soumis à 2 ou 3 glisseurs,
> seront particulièrement utiles pour la RESOLUTION GRAPHIQUE de
> problèmes !***

###  {#section-1 .unnumbered}

### Synthèse de la démarche de résolution d'un problème d'équilibre

Bien que chaque cas soit différent et que seule la pratique et la
confrontation à de nombreuses situations différentes permettent de se
préparer à faire face à des problématiques inédites, on peut proposer
les démarches de résolution ci-dessous :

![](11-Actions Mécaniques/Cours/pandoc/media/image152.png){width="6.360416666666667in"
height="6.2444444444444445in"}

+-----------------------------------------------------------------------+
| > ***[Remarque :]{.underline}***                                      |
| >                                                                     |
| > *Si, dans le cas d'un **problème plan**, le bilan des actions       |
| > mécaniques extérieures à un ensemble isolé fait apparaître **2 ou 3 |
| > torseurs glisseurs**, on peut alors imaginer une **traduction       |
| > graphique de l'équilibre** pour obtenir une valeur approchée de la  |
| > norme de l'action mécanique recherchée à partir de l'action         |
| > mécanique connue.*                                                  |
+=======================================================================+
+-----------------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Console de Bateau**                                        |
| ![](1 |                                                              |
| 1-Act | +-------------+---------------+-------------------------+    |
| ions  | | ***[Pr      |               | ***[Problématique       |    |
| Mécan | | oblématique |               | 2 :]{.underline}**      |    |
| iques | | 1 :]{.u     |               | Déterminer l'effort*    |    |
| /Cour | | nderline}** |               | ![](11-Actio            |    |
| s/pan | | Déterminer, |               | ns Mécaniques/Cours/pan |    |
| doc/m | | connaissant |               | doc/media/image154.wmf) |    |
| edia/ | | l'effort*   |               | *que doit développer le |    |
| image | | ![]         |               | vérin hydraulique pour  |    |
| 8.png | | (11-Actions |               | maintenir la barre en   |    |
| ){wid | |  Mécaniques |               | équilibre sous l'action |    |
| th="0 | | /Cours/pand |               | de l'eau sur le         |    |
| .6262 | | oc/media/im |               | safran.*                |    |
| 69685 | | age153.wmf) |               |                         |    |
| 03937 | | *développé* |               |                         |    |
| 01in" | | *par le     |               |                         |    |
| >     | | vérin pour  |               |                         |    |
| heigh | | maintenir   |               |                         |    |
| t="0. | | la barre en |               |                         |    |
| 65083 | | équilibre,  |               |                         |    |
| 33333 | | les AM      |               |                         |    |
| 33333 | | transmises  |               |                         |    |
| 4in"} | | par les     |               |                         |    |
|       | | liaisons en |               |                         |    |
|       | | A~1~ et     |               |                         |    |
|       | | A~2~ (en    |               |                         |    |
|       | | vue du      |               |                         |    |
|       | | dime        |               |                         |    |
|       | | nsionnement |               |                         |    |
|       | | des         |               |                         |    |
|       | | roulements  |               |                         |    |
|       | | à billes)*  |               |                         |    |
|       | +=============+===============+=========================+    |
|       | | Pour ces    | ![](11-Act    |                         |    |
|       | | deux        | ions Mécaniqu |                         |    |
|       | | pro         | es/Cours/pand |                         |    |
|       | | blématiques | oc/media/imag |                         |    |
|       | | d           | e155.png){wid |                         |    |
|       | | ifférentes, | th="3.9375in" |                         |    |
|       | | c'est le    | heig          |                         |    |
|       | | même        | ht="1.5659142 |                         |    |
|       | | isolement   | 607174104in"} |                         |    |
|       | | qui permet  |               |                         |    |
|       | | de faire    |               |                         |    |
|       | | apparaitre  |               |                         |    |
|       | | les actions |               |                         |    |
|       | | mécaniques  |               |                         |    |
|       | | connues et  |               |                         |    |
|       | | celles      |               |                         |    |
|       | | re          |               |                         |    |
|       | | cherchées : |               |                         |    |
|       | +-------------+---------------+-------------------------+    |
|       | | BAME à 1 :  |               | BAME à 1 :              |    |
|       | |             |               |                         |    |
|       | | Action de   |               | Action de               |    |
|       | | ![]         |               | ![](11-Actio            |    |
|       | | (11-Actions |               | ns Mécaniques/Cours/pan |    |
|       | |  Mécaniques |               | doc/media/image156.wmf) |    |
|       | | /Cours/pand |               | Action                  |    |
|       | | oc/media/im |               | de![](11-Actio          |    |
|       | | age156.wmf) |               | ns Mécaniques/Cours/pan |    |
|       | | Action de   |               | doc/media/image157.wmf) |    |
|       | | ![]         |               |                         |    |
|       | | (11-Actions |               | Action de               |    |
|       | |  Mécaniques |               | ![](11-Actio            |    |
|       | | /Cours/pand |               | ns Mécaniques/Cours/pan |    |
|       | | oc/media/im |               | doc/media/image158.wmf) |    |
|       | | age157.wmf) |               | Action de               |    |
|       | |             |               | ![](11-Actio            |    |
|       | | Action de   |               | ns Mécaniques/Cours/pan |    |
|       | | ![]         |               | doc/media/image159.wmf) |    |
|       | | (11-Actions |               |                         |    |
|       | |  Mécaniques |               | Action de               |    |
|       | | /Cours/pand |               | ![](11-Actio            |    |
|       | | oc/media/im |               | ns Mécaniques/Cours/pan |    |
|       | | age158.wmf) |               | doc/media/image160.wmf) |    |
|       | | Action de   |               |                         |    |
|       | | ![]         |               | Sous forme de torseurs  |    |
|       | | (11-Actions |               | écris **[en             |    |
|       | |  Mécaniques |               | ligne]{.underline}** :  |    |
|       | | /Cours/pand |               |                         |    |
|       | | oc/media/im |               | ![](11-Actio            |    |
|       | | age159.wmf) |               | ns Mécaniques/Cours/pan |    |
|       | |             |               | doc/media/image171.wmf) |    |
|       | | Action de   |               |                         |    |
|       | | ![]         |               | ![](11-Actio            |    |
|       | | (11-Actions |               | ns Mécaniques/Cours/pan |    |
|       | |  Mécaniques |               | doc/media/image172.wmf) |    |
|       | | /Cours/pand |               |                         |    |
|       | | oc/media/im |               | ![](11-Actio            |    |
|       | | age160.wmf) |               | ns Mécaniques/Cours/pan |    |
|       | |             |               | doc/media/image174.wmf) |    |
|       | | Sous forme  |               |                         |    |
|       | | de torseurs |               | ![](11-Actio            |    |
|       | | écris **[en |               | ns Mécaniques/Cours/pan |    |
|       | | co          |               | doc/media/image175.wmf) |    |
|       | | lonne]{.und |               |                         |    |
|       | | erline}** : |               | ![](11-Actio            |    |
|       | |             |               | ns Mécaniques/Cours/pan |    |
|       | | ![](11      |               | doc/media/image176.wmf) |    |
|       | | -Actions Mé |               |                         |    |
|       | | caniques/Co |               | ***[Théorème du moment  |    |
|       | | urs/pandoc/ |               | statique au point A~1~  |    |
|       | | media/image |               | projeté sur             |    |
|       | | 161.wmf)![] |               | l'axe]{.underline}***   |    |
|       | | (11-Actions |               | ![](11-Actions M        |    |
|       | |  Mécaniques |               | écaniques/Cours/pandoc/ |    |
|       | | /Cours/pand |               | media/image177.wmf)* :* |    |
|       | | oc/media/im |               | ![](11-Actio            |    |
|       | | age162.wmf) |               | ns Mécaniques/Cours/pan |    |
|       | |             |               | doc/media/image178.wmf) |    |
|       | | ![](11      |               |                         |    |
|       | | -Actions Mé |               | ![](11-Actions          |    |
|       | | caniques/Co |               | Mécaniques/Cours/pandoc |    |
|       | | urs/pandoc/ |               | /media/image179.wmf)Sur |    |
|       | | media/image |               | les calculs détaillés   |    |
|       | | 163.wmf)![] |               | sur l'exemple de        |    |
|       | | (11-Actions |               | droite, on voit que de  |    |
|       | |  Mécaniques |               | tous les produits       |    |
|       | | /Cours/pand |               | vectoriels qui font     |    |
|       | | oc/media/im |               | apparaître              |    |
|       | | age164.wmf) |               | ![](11-Actions M        |    |
|       | |             |               | écaniques/Cours/pandoc/ |    |
|       | | ![]         |               | media/image177.wmf)vont |    |
|       | | (11-Actions |               | être                    |    |
|       | |  Mécaniques |               | ![](11-Actions          |    |
|       | | /Cours/pand |               | Mécaniques/Cours/pandoc |    |
|       | | oc/media/im |               | /media/image180.wmf)*à* |    |
|       | | age165.wmf) |               | ![](11-Actions          |    |
|       | |             |               | Mécaniques/Cours/pandoc |    |
|       | | Pour        |               | /media/image177.wmf)*.* |    |
|       | | traduire    |               |                         |    |
|       | | cette       |               | ![](11-Actio            |    |
|       | | équation    |               | ns Mécaniques/Cours/pan |    |
|       | | torsorielle |               | doc/media/image181.wmf) |    |
|       | | en          |               |                         |    |
|       | | équations   |               |                         |    |
|       | | scalaires,  |               |                         |    |
|       | | il faut     |               |                         |    |
|       | | exprimer    |               |                         |    |
|       | | les         |               |                         |    |
|       | | différents  |               |                         |    |
|       | | torseurs au |               |                         |    |
|       | | même point  |               |                         |    |
|       | | et dans la  |               |                         |    |
|       | | même base.  |               |                         |    |
|       | |             |               |                         |    |
|       | | En          |               |                         |    |
|       | | choisissant |               |                         |    |
|       | | le point    |               |                         |    |
|       | | A~1~, on    |               |                         |    |
|       | | évite       |               |                         |    |
|       | | d'avoir à   |               |                         |    |
|       | | déplacer le |               |                         |    |
|       | | torseur     |               |                         |    |
|       | | dont la     |               |                         |    |
|       | | résultante  |               |                         |    |
|       | | est la plus |               |                         |    |
|       | | « lourde ». |               |                         |    |
|       | |             |               |                         |    |
|       | | ![]         |               |                         |    |
|       | | (11-Actions |               |                         |    |
|       | |  Mécaniques |               |                         |    |
|       | | /Cours/pand |               |                         |    |
|       | | oc/media/im |               |                         |    |
|       | | age167.wmf) |               |                         |    |
|       | |             |               |                         |    |
|       | | ![](11-Ac   |               |                         |    |
|       | | tions Mécan |               |                         |    |
|       | | iques/Cours |               |                         |    |
|       | | /pandoc/med |               |                         |    |
|       | | ia/image168 |               |                         |    |
|       | | .wmf)![](11 |               |                         |    |
|       | | -Actions Mé |               |                         |    |
|       | | caniques/Co |               |                         |    |
|       | | urs/pandoc/ |               |                         |    |
|       | | media/image |               |                         |    |
|       | | 169.wmf)![] |               |                         |    |
|       | | (11-Actions |               |                         |    |
|       | |  Mécaniques |               |                         |    |
|       | | /Cours/pand |               |                         |    |
|       | | oc/media/im |               |                         |    |
|       | | age170.wmf) |               |                         |    |
|       | +-------------+---------------+-------------------------+    |
|       | | Ce qui nous |               |                         |    |
|       | | donne :     |               |                         |    |
|       | |             |               |                         |    |
|       | | ![](11-Ac   |               |                         |    |
|       | | tions Mécan |               |                         |    |
|       | | iques/Cours |               |                         |    |
|       | | /pandoc/med |               |                         |    |
|       | | ia/image182 |               |                         |    |
|       | | .wmf)![](11 |               |                         |    |
|       | | -Actions Mé |               |                         |    |
|       | | caniques/Co |               |                         |    |
|       | | urs/pandoc/ |               |                         |    |
|       | | media/image |               |                         |    |
|       | | 183.wmf)![] |               |                         |    |
|       | | (11-Actions |               |                         |    |
|       | |  Mécaniques |               |                         |    |
|       | | /Cours/pand |               |                         |    |
|       | | oc/media/im |               |                         |    |
|       | | age184.wmf) |               |                         |    |
|       | |             |               |                         |    |
|       | | ![](11      |               |                         |    |
|       | | -Actions Mé |               |                         |    |
|       | | caniques/Co |               |                         |    |
|       | | urs/pandoc/ |               |                         |    |
|       | | media/image |               |                         |    |
|       | | 185.wmf)![] |               |                         |    |
|       | | (11-Actions |               |                         |    |
|       | |  Mécaniques |               |                         |    |
|       | | /Cours/pand |               |                         |    |
|       | | oc/media/im |               |                         |    |
|       | | age186.wmf) |               |                         |    |
|       | +-------------+---------------+-------------------------+    |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | ![Image5](11-Actio                                           |
| ![](1 | ns Mécaniques/Cours/pandoc/media/image17.jpeg){width="2.5in" |
| 1-Act | height="1.925in"}**Poussoir et coulisseau**                  |
| ions  |                                                              |
| Mécan | On associe les repères :                                     |
| iques |                                                              |
| /Cour | > \-                                                         |
| s/pan | > $R_{0}(O,\overset{\rightarrow}{x_{0}}                      |
| doc/m | ,\overset{\rightarrow}{y_{0}},\overset{\rightarrow}{z_{0}})$ |
| edia/ | > au bâti 0, tel que                                         |
| image | >                                                            |
| 8.png | $\overset{\rightarrow}{OB} = b.\overset{\rightarrow}{x_{0}}$ |
| ){wid | >                                                            |
| th="0 | > \-                                                         |
| .6262 | > $R_{1}(O,\overset{\rightarrow}{x_{1}}                      |
| 69685 | ,\overset{\rightarrow}{y_{1}},\overset{\rightarrow}{z_{1}})$ |
| 03937 | > au poussoir 1, tels que                                    |
| 01in" | >                                                            |
| >     | > $\over                                                     |
| heigh | set{\rightarrow}{BA} = \lambda.\overset{\rightarrow}{y_{0}}$ |
| t="0. | > et                                                         |
| 65083 | > $\alpha =                                                  |
| 33333 | (\overset{\rightarrow}{x_{0}},\overset{\rightarrow}{x_{1}})$ |
| 33333 |                                                              |
| 4in"} | Un système non représenté assure le maintien du contact du   |
|       | coulisseau 2 avec le poussoir 1 au point A.                  |
|       |                                                              |
|       | Le poussoir 1 est soumis au couple moteur $C_{m}$ et le      |
|       | piston 2 à l'action                                          |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image18.wmf) de |
|       | pression du fluide.                                          |
|       |                                                              |
|       | On suppose le problème plan, les liaisons sans frottement et |
|       | on néglige les effets d'inertie et de la pesanteur.          |
|       |                                                              |
|       | **L'objectif de l'étude est de déterminer une relation entre |
|       | F et** $\mathbf{C}_{\mathbf{m}}$ **lorsque le système est en |
|       | équilibre.**                                                 |
|       |                                                              |
|       | **Déterminer une relation entre le couple moteur**           |
|       | $\mathbf{C}_{\mathbf{m}}$ **et l'effort** $\mathbf{F}$**.**  |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

## Définir une action mécanique : Point de vue local

![](11-Actions Mécaniques/Cours/pandoc/media/image187.png){width="1.648611111111111in"
height="1.3770833333333334in"}L'action mécanique d'un élément 1 sur un
solide 2 (AM de
![](11-Actions Mécaniques/Cours/pandoc/media/image188.wmf)) est répartie
sur la surface (action de contact) ou sur le volume (action à distance)
du solide 2.

Soit P, un point appartenant à 2 et concerné par cette action mécanique.
On définit localement une **force élémentaire**
$d\overrightarrow{F_{1 \rightarrow 2}(P)}$ agissant sur une surface ou
un volume de dimension réduite définie au voisinage de P.

![](11-Actions Mécaniques/Cours/pandoc/media/image189.png){width="1.3611111111111112in"
height="1.0534722222222221in"}![](11-Actions Mécaniques/Cours/pandoc/media/image190.png){width="1.8611111111111112in"
height="1.4104166666666667in"}

L'expression de cette force élémentaire
$d\overrightarrow{F_{1 \rightarrow 2}(P)}$ varie en fonction de la
nature de l'élément de 2 associé à P :

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ***Nature de   ***Elément    ***Densité de l'action ***unité***                                                          ***Expression de***
  l'élément***   géométrique   mécanique***                                                                                $\mathbf{d}\overrightarrow{\mathbf{F}_{\mathbf{1 \rightarrow 2}}\mathbf{(P)}}$
                 associé***                                                                                                
  -------------- ------------- ---------------------- -------------------------------------------------------------------- --------------------------------------------------------------------------------
  *Ligne*        $$dl$$        *linéique*             $$\left\lbrack N \cdot m^{- 1} \right\rbrack$$                       $$\overrightarrow{q} \cdot dl$$
                               $\overrightarrow{q}$                                                                        

  *Surface*      $$ds$$        *surfacique*           $$\left\lbrack N \cdot m^{- 2} \right\rbrack ou\lbrack Pa\rbrack$$   $$\overrightarrow{q} \cdot ds$$
                               $\overrightarrow{q}$                                                                        

  *Volume*       $$dv$$        *volumique*            $$\left\lbrack N \cdot m^{- 3} \right\rbrack$$                       $\overrightarrow{q} \cdot dv$
                               $\overrightarrow{q}$                                                                        
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

L'ensemble des forces élémentaires agissant sur l'ensemble des éléments
concerné par l'action mécanique est appelé ***champ de forces*** associé
à l'action mécanique.

C'est la connaissance de ce champ de forces qui va permettre d'étudier
les déformations. d'un solide soumis à une action mécanique.

### Définir une action mécanique : du point de vue local au point de vue global

Pour étudier le comportement des systèmes, on fait l'hypothèse que les
pièces qui le constituent sont indéformables (sauf les pièces dont le
but est de se déformer, ressorts,...). Dans ce cas, on peut utiliser un
***modèle global*** des actions mécaniques.

Si on reprend le cas d'un solide 2 soumis à l'action mécanique d'un
élément 1, cela revient à considérer que ce dernier exerce sur le solide
2 une force $\overrightarrow{F_{1 \rightarrow 2}}$ tel que :

![](11-Actions Mécaniques/Cours/pandoc/media/image191.wmf) *Z* est la
zone du solide 2 sur laquelle s'exerce l'AM de
![](11-Actions Mécaniques/Cours/pandoc/media/image188.wmf)

![](11-Actions Mécaniques/Cours/pandoc/media/image192.png){width="4.35in"
height="1.7597255030621173in"}

### Torseur des actions mécaniques

-   **[Résultante de l'action mécanique]{.underline}**

La résultante de l'action mécanique de $1 \rightarrow 2$, notée
$\overrightarrow{R_{1 \rightarrow 2}}$ correspond à l'action mécanique
globale créée par toutes contributions
$d\overrightarrow{F_{1 \rightarrow 2}(P)}$ du champ de forces
élémentaires. On a donc :

![](11-Actions Mécaniques/Cours/pandoc/media/image193.wmf) *(Newton :
N)*

Mais cette notion de résultante ne suffit pas pour caractériser
correctement l'effet de cette action mécanique sur le solide 2. En
effet, on s'intéresse à la façon dont cette action mécanique va
provoquer, modifier ou empêcher le mouvement du solide 2.

***[Exemple :]{.underline}***

![](11-Actions Mécaniques/Cours/pandoc/media/image194.png){width="1.3729166666666666in"
height="1.2631944444444445in"}Pour les deux montages des clapets
anti-retour schématisés ci-dessous, la résultante
$\overrightarrow{R_{2 \rightarrow 1}}$ de l'action mécanique de l'eau 2
sur le clapet 1 est la même.

Pour autant, le mouvement du clapet engendré par cette action mécanique
sera différent d'un montage à l'autre :

-   rotation de centre A dans le sens horaire (montage 1) ;

-   rotation de centre B dans le sens anti-horaire (montage 2).

![](11-Actions Mécaniques/Cours/pandoc/media/image195.png){width="4.47761154855643in"
height="1.328358486439195in"}

Pour caractériser cette différence on utilise la notion de ***moment
résultant***.

-   **[Moment Résultant de l'action mécanique]{.underline}**

Le moment résultant de l'action mécanique de
![](11-Actions Mécaniques/Cours/pandoc/media/image188.wmf), exprimé en
un point J fixe, est un vecteur qui permet de « caractériser » la
capacité de cette action mécanique à provoquer, à modifier ou à empêcher
un mouvement de rotation du solide 2 autour de ce point J. Il est défini
par :

![](11-Actions Mécaniques/Cours/pandoc/media/image196.wmf) ***(Newton.
mètre : N.m)***

*Z* est la zone du solide 2 sur laquelle s'exerce l'AM de
![](11-Actions Mécaniques/Cours/pandoc/media/image188.wmf)

**[Torseur de l'action mécanique]{.underline}**

Pour faire le bilan des effets d'une action mécanique 1 agissant sur un
solide 2, on utilise le torseur suivant :
![](11-Actions Mécaniques/Cours/pandoc/media/image197.wmf)

On appelle « ***éléments de réduction*** » du torseur, au point J, de
l'AM de ![](11-Actions Mécaniques/Cours/pandoc/media/image188.wmf) :

-   La ***[résultante]{.underline}*** de l'AM de
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image188.wmf) :
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image198.wmf)*.*
    > [Elle est indépendante du point d'expression du
    > torseur.]{.underline}

-   Le ***[moment résultant]{.underline}*** de l'AM de
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image188.wmf)  :
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image199.wmf)*.* [Il
    > dépend du point d'expression du torseur.]{.underline}

***[Remarque :]{.underline}*** le moment vérifie la relation du champ
des moments d'un torseur (Varignon) :

![](11-Actions Mécaniques/Cours/pandoc/media/image200.wmf) de l'espace
![](11-Actions Mécaniques/Cours/pandoc/media/image201.wmf)

**Lorsqu'on déplace un torseur d'un point à un autre on utilisera cette
relation. On dit qu'on réduit le torseur (question : Réduire le torseur,
ou trouver les éléments de réduction,...)**

+-------+--------------------------------------------------------------+
| >     | ![](11-Actions Mé                                            |
| ![](1 | caniques/Cours/pandoc/media/image202.jpeg){width="1.95625in" |
| 1-Act | height="2.65in"}**Piston**                                   |
| ions  |                                                              |
| Mécan | **Déterminer l'action mécanique de l'air sur le piston,      |
| iques | notée** $\left\{ T_{p \rightarrow 8} \right\}_{A}$           |
| /Cour |                                                              |
| s/pan | $$\left\{ T_{p \rightarrow 8} \right\}_{A} = \begin{Bmatrix} |
| doc/m | \overrightarrow{R_{p \rightarrow 8}} \\                      |
| edia/ | \overrightarrow{M_{A,p \rightarrow 8}}                       |
| image | \end{Bmatrix} = \begin{Bmatrix}                              |
| 8.png | \int_{S}^{}\overrightarrow{dF_{p \rightarrow 8}(M)} \\       |
| ){wid | \int_{S}^{}{\overri                                          |
| th="0 | ghtarrow{AM} \land \overrightarrow{dF_{p \rightarrow 8}(M)}} |
| .6262 | \end{Bmatrix}$$                                              |
| 69685 |                                                              |
| 03937 | $$\overrightarr                                              |
| 01in" | ow{R_{p \rightarrow 8}} = \int_{S}^{}\overrightarrow{dF_{p \ |
| >     | rightarrow 8}(M)} = \int_{S}^{}{p \cdot ds \cdot \overrighta |
| heigh | rrow{x}} = \int_{S}^{}{p \cdot r \cdot dr \cdot d\theta \cdo |
| t="0. | t \overrightarrow{x}} = p \cdot S \cdot \overrightarrow{x}$$ |
| 65083 |                                                              |
| 33333 | $$ds = r \cdot d\theta \cdot dr$$                            |
| 33333 |                                                              |
| 4in"} | $$\overrightarrow{M_{A,p \rightarrow 8}} = \int_{S}^{}{      |
|       | \overrightarrow{AM} \land \overrightarrow{dF_{p \rightarrow  |
|       | 8}(M)}} = \int_{S}^{}{(r \cdot \cos\theta \cdot \overrightar |
|       | row{z} + r \cdot \sin\theta \cdot \overrightarrow{y}) \land  |
|       | p \cdot r \cdot dr \cdot d\theta \cdot \overrightarrow{x}}$$ |
|       |                                                              |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image203.wmf)   |
|       |                                                              |
|       | $$= p\int_{S}^{}{r^{2} \cdot dr \cdot \cos\theta \cdot d\    |
|       | theta \cdot \overrightarrow{y} - p\int_{S}^{}{r^{2} \cdot dr |
|       |  \cdot \sin\theta} \cdot d\theta \cdot \overrightarrow{z}}$$ |
|       |                                                              |
|       | $$= p \cdot \overrightarrow{y}\in                            |
|       | t_{0}^{R}{r^{2} \cdot dr}\int_{0}^{2\pi}{\cos\theta \cdot d\ |
|       | theta} - p \cdot \overrightarrow{z} \cdot \int_{0}^{R}{r^{2} |
|       |  \cdot dr} \cdot \int_{0}^{2\pi}{\sin\theta \cdot d\theta}$$ |
|       |                                                              |
|       | $$= p \cdot \overrightarrow{y}\left                          |
|       | \lbrack \frac{r^{3}}{3} \right\rbrack_{0}^{R}\left\lbrack \s |
|       | in\theta \right\rbrack_{0}^{2\pi} + p \cdot \overrightarrow{ |
|       | z} \cdot \left\lbrack \frac{r^{3}}{3} \right\rbrack_{0}^{R}  |
|       | \cdot \left\lbrack \cos\theta \right\rbrack_{0}^{2\pi} = 0$$ |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Barrage**                                                  |
| ![](1 |                                                              |
| 1-Act | ![1](11-Actions Mécaniques/Co                                |
| ions  | urs/pandoc/media/image204.jpeg){width="2.0652777777777778in" |
| Mécan | height="1.4055555555555554in"}Un barrage poids est un        |
| iques | barrage dont la propre masse suffit à résister à la pression |
| /Cour | exercée par l\'eau. Le barrage est soumis principalement à   |
| s/pan | l'action mécanique de l'eau (pression hydrostatique) et à    |
| doc/m | l'action mécanique de la pesanteur.                          |
| edia/ |                                                              |
| image | On s'intéresse à un barrage poids en béton de section        |
| 8.png | triangulaire qui repose sur le sol et qui permet une retenue |
| ){wid | d'eau de hauteur h pour l'alimentation des voies navigables. |
| th="0 |                                                              |
| .6262 | Le point O est situé dans le plan médian du barrage.         |
| 69685 |                                                              |
| 03937 | ![2](11-Actions Mécaniques/C                                 |
| 01in" | ours/pandoc/media/image205.png){width="3.0243055555555554in" |
| >     | height="2.066666666666667in"}[Les caractéristiques du        |
| heigh | barrage sont données ci-dessous :]{.underline}               |
| t="0. |                                                              |
| 65083 | m : masse du barrage considéré comme un solide homogène.     |
| 33333 |                                                              |
| 33333 | a = 20m : assise du barrage.                                 |
| 4in"} |                                                              |
|       | h = 25m : hauteur d'eau.                                     |
|       |                                                              |
|       | L = 80m : largeur du barrage.                                |
|       |                                                              |
|       | ρ~eau~ = 1000kg/m^3^ : masse volumique de l'eau.             |
|       |                                                              |
|       | **L'effort maximal de poussée doit être de 300.10^6^ N.**    |
|       |                                                              |
|       | **Donner l'expression de la force élémentaire de pression de |
|       | l'eau sur le barrage.**                                      |
|       |                                                              |
|       | ![](11-Actions Mécaniques/C                                  |
|       | ours/pandoc/media/image206.png){width="2.5131944444444443in" |
|       | height="1.8083333333333333in"}[Point de vue                  |
|       | local :]{.underline}                                         |
|       |                                                              |
|       | Sur chaque élément de surface $ds = dy \cdot dz$ situé       |
|       | autour d'un point Q de la paroi s'exerce un effort           |
|       | élémentaire :                                                |
|       |                                                              |
|       | $$d\overrightarrow{F_{eau \righta                            |
|       | rrow barrage}(Q)} = p(Q) \cdot ds \cdot \overrightarrow{x}$$ |
|       |                                                              |
|       | Les lois de l'hydrostatique permettent d'écrire :            |
|       | $p(Q) = \rho_{eau} \cdot g \cdot (h - z)$                    |
|       |                                                              |
|       | On a donc :                                                  |
|       |                                                              |
|       | $$\boxed{d\overrig                                           |
|       | htarrow{F_{eau \rightarrow barrage}(Q)} = \rho_{eau} \cdot g |
|       |  \cdot (h - z) \cdot dy \cdot dz \cdot \overrightarrow{x}}$$ |
|       |                                                              |
|       | **Déterminer les coordonnées du point**                      |
|       | $\mathbf{M(0,0,}\mathbf{z}_{\mathbf{M}}\mathbf{)}$ **ou le   |
|       | moment résultant de l'action mécanique de l'eau sur le       |
|       | barrage est nul. Donner, en ce point, l'expression du        |
|       | torseur de cette action mécanique.**                         |
|       |                                                              |
|       | On cherche le point $M(0,0,z_{M})$ pour lequel :             |
|       | $\overrig                                                    |
|       | htarrow{M_{M,eau \rightarrow barrage}} = \overrightarrow{0}$ |
|       |                                                              |
|       | Or :                                                         |
|       |                                                              |
|       | $$\overrightarrow{M_{M,eau \rig                              |
|       | htarrow barrage}} = \int_{S}^{}{\overrightarrow{MQ} \land}d\ |
|       | overrightarrow{F_{eau \rightarrow barrage}(Q)} = \int_{S}^{} |
|       | {\left( \overrightarrow{MO} + \overrightarrow{OQ} \right) \l |
|       | and}\rho_{eau} \cdot g \cdot (h - z) \cdot dy \cdot dz \cdot |
|       |  \overrightarrow{x} = \int_{S}^{}{\left( \left( - z_{M} \cdo |
|       | t \overrightarrow{z} \right) + \left( y \cdot \overrightarro |
|       | w{y} + z \cdot \overrightarrow{z} \right) \right) \land}\rho |
|       | _{eau} \cdot g \cdot (h - z) \cdot dy \cdot dz \cdot \overri |
|       | ghtarrow{x} = \int_{S}^{}{- y \cdot \rho_{eau} \cdot g \cdot |
|       |  (h - z) \cdot dy \cdot dz \cdot \overrightarrow{z}} + \int_ |
|       | {S}^{}{\left( z - z_{M} \right) \cdot \rho_{eau} \cdot g \cd |
|       | ot (h - z) \cdot dy \cdot dz \cdot \overrightarrow{y}} = 0$$ |
|       |                                                              |
|       | $$= - \rho                                                   |
|       | _{eau} \cdot g \cdot \overrightarrow{z} \cdot \int_{- \frac{ |
|       | L}{2}}^{\frac{L}{2}}{y \cdot}dy \cdot \int_{0}^{h}{(h - z) \ |
|       | cdot}dz + \rho_{eau} \cdot g \cdot \overrightarrow{y}\int_{0 |
|       | }^{h}{(z - z_{M}) \cdot}(h - z) \cdot dz\int_{- \frac{L}{2}} |
|       | ^{\frac{L}{2}} \cdot dy = \rho_{eau} \cdot g \cdot \overrigh |
|       | tarrow{z} \cdot \left\lbrack \frac{y^{2}}{2} \right\rbrack_{ |
|       | - \frac{L}{2}}^{\frac{L}{2}} \cdot \left\lbrack h \cdot z -  |
|       | \frac{z^{2}}{2} \right\rbrack_{0}^{h} + \rho_{eau} \cdot g \ |
|       | cdot \overrightarrow{y} \cdot \left\lbrack (h + z_{M})\frac{ |
|       | z^{2}}{2} - \frac{z^{3}}{3} - z \cdot z_{M} \cdot h \right\r |
|       | brack_{0}^{h} \cdot \lbrack y\rbrack_{- \frac{L}{2}}^{\frac{ |
|       | L}{2}} = 0 + \rho_{eau} \cdot g \cdot \overrightarrow{y} \cd |
|       | ot (\frac{h^{3}}{6} - \frac{z_{M} \cdot h^{2}}{2}) \cdot L$$ |
|       |                                                              |
|       | Pour que                                                     |
|       | $\overrigh                                                   |
|       | tarrow{M_{M,eau \rightarrow barrage}} = \overrightarrow{0}$, |
|       | il faut donc que $z_{M} = \frac{h}{3}$                       |
|       |                                                              |
|       | Au point M, le torseur de l'action mécanique de l'eau        |
|       | s'écrit :                                                    |
|       |                                                              |
|       | $$\l                                                         |
|       | eft\{ T_{eau \rightarrow barrage} \right\} = \begin{Bmatrix} |
|       | \overrightarrow{R_{eau \rightarrow barrage}} \\              |
|       | \overrightarrow{0}                                           |
|       | \end{Bmatrix}_{M}$$                                          |
|       |                                                              |
|       | Avec :                                                       |
|       |                                                              |
|       | $$\overrightarrow{R_{eau \                                   |
|       | rightarrow barrage}} = \int_{S}^{}{d\overrightarrow{F_{eau \ |
|       | rightarrow barrage}(Q)}} = \int_{S}^{}{\rho_{eau} \cdot g \c |
|       | dot (h - z) \cdot dy \cdot dz \cdot \overrightarrow{x}} = \r |
|       | ho_{eau} \cdot g \cdot \overrightarrow{x \cdot}\int_{0}^{h}{ |
|       | (h - z) \cdot}dz\int_{- \frac{L}{2}}^{\frac{L}{2}}{dy} = \rh |
|       | o_{eau} \cdot g \cdot \overrightarrow{x} \cdot \left\lbrack  |
|       | h \cdot z - \frac{z^{2}}{2} \right\rbrack_{0}^{h} \cdot \lbr |
|       | ack y\rbrack_{- \frac{L}{2}}^{\frac{L}{2}} = \rho_{eau} \cdo |
|       | t g \cdot L \cdot \frac{h^{2}}{2} \cdot \overrightarrow{x}$$ |
|       |                                                              |
|       | $$\boxed{\l                                                  |
|       | eft\{ T_{eau \rightarrow barrage} \right\} = \begin{Bmatrix} |
|       | \rho_{eau} \cdot                                             |
|       |  g \cdot L \cdot \frac{h^{2}}{2} \cdot \overrightarrow{x} \\ |
|       | \overrightarrow{0}                                           |
|       | \end{Bmatrix}_{M}}$$                                         |
|       |                                                              |
|       | ![](11-Actions Mécaniques/                                   |
|       | Cours/pandoc/media/image207.png){width="6.697916666666667in" |
|       | height="2.5in"}                                              |
|       |                                                              |
|       | **Vérifier le critère de l'effort de poussée.**              |
|       |                                                              |
|       | $$\overrightarrow{\left\| R_{eau \rightarrow                 |
|       |  barrage} \right\|} = \rho_{eau} \cdot g \cdot L \cdot \frac |
|       | {h^{2}}{2} = \boxed{245 \cdot 10^{6}N} < 300 \cdot 10^{6}N$$ |
|       |                                                              |
|       | Le critère est donc respecté.                                |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

## Prise en compte du phénomène de frottement 

### ![](11-Actions Mécaniques/Cours/pandoc/media/image208.jpeg){width="1.042361111111111in" height="1.4833333333333334in"}Frottement en translation

Le phénomène de frottement est omniprésent dans l'étude du comportement
et la conception des systèmes. Il peut être :

-   ***utile*** lorsqu'il s'agit de freiner ou d'accélérer un solide ;

-   ***néfaste*** lorsqu'il est à l'origine de pertes d'énergie ou
    d'usures trop importantes ;

-   ***négligeable*** dans la plupart des cas.

On différencie deux cas :

+--------------------+-------------------------------------------------+
| **FROTTEMENT**     | *Il existe un mouvement relatif entre les 2     |
|                    | solides*                                        |
| entre 2 solides en |                                                 |
| contact            |                                                 |
+====================+=================================================+
| **ADHERENCE**      | *Il existe une tendance au mouvement mais il    |
|                    | n'y a pas de mouvement relatif entre les 2      |
| entre 2 solides en | solides.*                                       |
| contact            |                                                 |
+--------------------+-------------------------------------------------+

![](11-Actions Mécaniques/Cours/pandoc/media/image209.png){width="4.692361111111111in"
height="1.2416666666666667in"}On peut illustrer cela avec l'exemple d'un
colis S~2~ posé sur un plan incliné S~1~ :

A partir d'une valeur limite de l'angle d'inclinaison
![](11-Actions Mécaniques/Cours/pandoc/media/image210.wmf), il y perte
d'adhérence entre S~2~ et S~1~. Il y a alors apparition d'un mouvement
relatif avec frottement de S~2~ par rapport à S~1~.

+------------+----------------+-----------------+---------------------+
| **Mise en  |                |                 |                     |
| évidence   |                |                 |                     |
| des        |                |                 |                     |
| phénomènes |                |                 |                     |
| de         |                |                 |                     |
| frottement |                |                 |                     |
| et         |                |                 |                     |
| d'a        |                |                 |                     |
| dhérence** |                |                 |                     |
+============+================+=================+=====================+
| *On prend  |                |                 |                     |
| l'exemple  |                |                 |                     |
| d'un colis |                |                 |                     |
| S~2~ posé  |                |                 |                     |
| sur un     |                |                 |                     |
| plan       |                |                 |                     |
| horizontal |                |                 |                     |
| S~1~.*     |                |                 |                     |
+------------+----------------+-----------------+---------------------+
| Le colis   | Une action     |                 | S~2~ se met à       |
| est au     | mécanique      |                 | glisser dans le     |
| repos      | extérieure     |                 | même sens que       |
|            | $\over         |                 | $\                  |
|            | rightarrow{F}$ |                 | overrightarrow{F}$. |
|            | agit sur S~2~  |                 |                     |
|            | et tend à le   |                 |                     |
|            | faire glisser  |                 |                     |
|            | par rapport à  |                 |                     |
|            | S~1~.          |                 |                     |
+------------+----------------+-----------------+---------------------+
| ![](11-A   | ![             | ![](11-Action   | !                   |
| ctions Méc | ](11-Actions M | s Mécaniques/Co | [](11-Actions Mécan |
| aniques/Co | écaniques/Cour | urs/pandoc/medi | iques/Cours/pandoc/ |
| urs/pandoc | s/pandoc/media | a/image213.wmf) | media/image214.wmf) |
| /media/ima | /image212.wmf) |                 |                     |
| ge211.wmf) |                |                 |                     |
+------------+----------------+-----------------+---------------------+
| ![](11-    | ![]            | ![](11-Actio    | ![](11-Acti         |
| Actions Mé | (11-Actions Mé | ns Mécaniques/C | ons Mécaniques/Cour |
| caniques/C | caniques/Cours | ours/pandoc/med | s/pandoc/media/imag |
| ours/pando | /pandoc/media/ | ia/image215.png | e215.png){width="1. |
| c/media/im | image215.png){ | ){width="1.1395 | 3256944444444445in" |
| age215.png | width="1.05833 | 833333333334in" | height="1.3         |
| ){width="1 | 33333333333in" | height="1.34861 | 486111111111112in"} |
| .046527777 | he             | 11111111112in"} |                     |
| 7777777in" | ight="1.348611 |                 |                     |
| height="1. | 1111111112in"} |                 |                     |
| 3486111111 |                |                 |                     |
| 111112in"} |                |                 |                     |
+------------+----------------+-----------------+---------------------+
|            | Il existe une  |                 | Il existe une       |
|            | action         |                 | action tangentielle |
|            | tangentielle   |                 | de frottement       |
|            | d'adhérence    |                 | !                   |
|            | $\overrigh     |                 | [](11-Actions Mécan |
|            | tarrow{T_{a}}$ |                 | iques/Cours/pandoc/ |
|            | de S~2~ sur    |                 | media/image216.wmf) |
|            | S~1~ (de même  |                 | de S~2~ sur S~1~    |
|            | norme et de    |                 | (de norme constante |
|            | sens opposée à |                 | et \<               |
|            | $\overr        |                 | ![                  |
|            | ightarrow{F}$) |                 | ](11-Actions Mécani |
|            | qui s'oppose à |                 | ques/Cours/pandoc/m |
|            | la tendance au |                 | edia/image217.wmf)) |
|            | mouvement      |                 | qui s'oppose (sans  |
|            | relatif entre  |                 | l'empêcher) au      |
|            | S~2~ et S~1~.  |                 | glissement de S~2~  |
|            |                |                 | par rapport à S~1~. |
|            | Cette action   |                 |                     |
|            | tangentielle   |                 |                     |
|            | d'adhérence a  |                 |                     |
|            | une limite     |                 |                     |
|            | $\overrightar  |                 |                     |
|            | row{T_{alim}}$ |                 |                     |
|            | (égale et      |                 |                     |
|            | opposée à      |                 |                     |
|            | $\overrightarr |                 |                     |
|            | ow{F_{\lim}}$) |                 |                     |
|            | à partir de    |                 |                     |
|            | laquelle       |                 |                     |
|            | l'opposition à |                 |                     |
|            | la tendance au |                 |                     |
|            | mouvement ne   |                 |                     |
|            | sera plus      |                 |                     |
|            | suffisante     |                 |                     |
|            | pour maintenir |                 |                     |
|            | S~2~ immobile. |                 |                     |
+------------+----------------+-----------------+---------------------+
|            | *              | ***ADHERENCE    | ***FROTTEMENT***    |
|            | **ADHERENCE*** | LIMITE***       |                     |
+------------+----------------+-----------------+---------------------+
| $\         |                |                 |                     |
| overrighta |                |                 |                     |
| rrow{P}$ : |                |                 |                     |
| résultante |                |                 |                     |
| de         |                |                 |                     |
| l'action   |                |                 |                     |
| de la      |                |                 |                     |
| pesanteur  |                |                 |                     |
| sur S~2~   |                |                 |                     |
|            |                |                 |                     |
| $\         |                |                 |                     |
| overrighta |                |                 |                     |
| rrow{N}$ : |                |                 |                     |
| résultante |                |                 |                     |
| des        |                |                 |                     |
| actions de |                |                 |                     |
| pression   |                |                 |                     |
| de contact |                |                 |                     |
| de S~1~    |                |                 |                     |
| sur S~2~   |                |                 |                     |
|            |                |                 |                     |
| $\         |                |                 |                     |
| overrighta |                |                 |                     |
| rrow{F}$ : |                |                 |                     |
| résultante |                |                 |                     |
| de         |                |                 |                     |
| l'action   |                |                 |                     |
| extérieure |                |                 |                     |
| agissant   |                |                 |                     |
| sur S~2~   |                |                 |                     |
| dans le    |                |                 |                     |
| but de le  |                |                 |                     |
| faire      |                |                 |                     |
| glisser    |                |                 |                     |
| sur S~1~   |                |                 |                     |
|            |                |                 |                     |
| $\over     |                |                 |                     |
| rightarrow |                |                 |                     |
| {T_{a}}$et |                |                 |                     |
| $\over     |                |                 |                     |
| rightarrow |                |                 |                     |
| {T_{f}}$ : |                |                 |                     |
| r          |                |                 |                     |
| ésultantes |                |                 |                     |
| des        |                |                 |                     |
| actions    |                |                 |                     |
| tan        |                |                 |                     |
| gentielles |                |                 |                     |
| d          |                |                 |                     |
| 'adhérence |                |                 |                     |
| et de      |                |                 |                     |
| frottement |                |                 |                     |
| de S~1~    |                |                 |                     |
| sur S~2~   |                |                 |                     |
+------------+----------------+-----------------+---------------------+

Evolution de la résultante des actions tangentielles de frottement et
d'adhérence :

+--------------------+-----------------------+------------------------+
| **ADHERENCE**      | ***ADHERENCE          | ***FROTTEMENT***       |
|                    | LIMITE***             |                        |
+====================+=======================+========================+
| $$\overrighta      | ![](11-Actions M      | ![](11-Actions         |
| rrow{T_{a}} = - \o | écaniques/Cours/pando |  Mécaniques/Cours/pand |
| verrightarrow{F}$$ | c/media/image218.wmf) | oc/media/image219.wmf) |
+--------------------+-----------------------+------------------------+
| angle d'adhérence  | angle d'adhérence     | angle de frottement    |
| ![](               | ![](11-Actions M      | ![](11-Actions         |
| 11-Actions Mécaniq | écaniques/Cours/pando |  Mécaniques/Cours/pand |
| ues/Cours/pandoc/m | c/media/image221.wmf) | oc/media/image222.wmf) |
| edia/image220.wmf) |                       |                        |
+--------------------+-----------------------+------------------------+
| ![](               | ![](11-Actions M      | ![](11-Actions         |
| 11-Actions Mécaniq | écaniques/Cours/pando |  Mécaniques/Cours/pand |
| ues/Cours/pandoc/m | c/media/image224.wmf) | oc/media/image226.wmf) |
| edia/image223.wmf) |                       |                        |
|                    | ![](11-Actions Méca   | ![](11-Actions         |
|                    | niques/Cours/pandoc/m |  Mécaniques/Cours/pand |
|                    | edia/image225.wmf)est | oc/media/image227.wmf) |
|                    | le ***coefficient     | est le ***coefficient  |
|                    | d'adhérence***        | de frottement***       |
+--------------------+-----------------------+------------------------+
| ![]                |                       |                        |
| (11-Actions Mécani |                       |                        |
| ques/Cours/pandoc/ |                       |                        |
| media/image228.png |                       |                        |
| ){width="2.6625in" |                       |                        |
| height="1.43       |                       |                        |
| 05555555555556in"} |                       |                        |
+--------------------+-----------------------+------------------------+

-   **[Point de vue local : loi de Coulomb]{.underline}**

Soient deux solides 1 et 2 en contact sur une surface S et ayant une
tendance au mouvement ou un mouvement relatif. La force élémentaire
![](11-Actions Mécaniques/Cours/pandoc/media/image229.wmf)de 1 sur 2 au
point P se décompose en :

-   une [***force élémentaire de pression***]{.underline}
    ![](11-Actions Mécaniques/Cours/pandoc/media/image230.wmf) normale
    au plan de contact (plan tangent commun aux deux solides) ;

-   une ***[force élémentaire tangentielle]{.underline}***
    ![](11-Actions Mécaniques/Cours/pandoc/media/image231.wmf)
    appartenant au plan de contact.

On a donc : ![](11-Actions Mécaniques/Cours/pandoc/media/image232.wmf)

+---------------------+-----------------------+------------------------+
| **ADHERENCE**       | ***ADHERENCE          | ***FROTTEMENT***       |
|                     | LIMITE***             |                        |
+=====================+=======================+========================+
| Vitesse de          | Vitesse de            | Vitesse de             |
| glissement!         | gliss                 | gl                     |
| [](11-Actions Mécan | ement![](11-Actions M | issement![](11-Actions |
| iques/Cours/pandoc/ | écaniques/Cours/pando |  Mécaniques/Cours/pand |
| media/image233.wmf) | c/media/image233.wmf) | oc/media/image234.wmf) |
+---------------------+-----------------------+------------------------+
| ![](11-Act          | ![]                   | ![](11-Actions Mécani  |
| ions Mécaniques/Cou | (11-Actions Mécanique | ques/Cours/pandoc/medi |
| rs/pandoc/media/ima | s/Cours/pandoc/media/ | a/image235.png){width= |
| ge235.png){width="1 | image235.png){width=" | "1.5815562117235347in" |
| .594627077865267in" | 1.6932327209098863in" | height="               |
| height="1.5         | height="1             | 1.5512817147856517in"} |
| 641021434820648in"} | .5384612860892388in"} |                        |
+---------------------+-----------------------+------------------------+
| !                   | ![](11-Actions M      | ![](11-Actions         |
| [](11-Actions Mécan | écaniques/Cours/pando |  Mécaniques/Cours/pand |
| iques/Cours/pandoc/ | c/media/image237.wmf) | oc/media/image238.wmf) |
| media/image236.wmf) | (angle d'adhérence    | (angle de frottement)  |
| (angle d'adhérence) | limite)               |                        |
+---------------------+-----------------------+------------------------+
| !                   | ![](11-Actions M      | ![](11-Actions         |
| [](11-Actions Mécan | écaniques/Cours/pando |  Mécaniques/Cours/pand |
| iques/Cours/pandoc/ | c/media/image241.wmf) | oc/media/image242.wmf) |
| media/image239.wmf) |                       |                        |
|                     | Coef. d'adhérence     | Coef. de frottement    |
| Coef. d'adhérence   | ![](11-Actions M      | ![](11-Actions         |
| !                   | écaniques/Cours/pando |  Mécaniques/Cours/pand |
| [](11-Actions Mécan | c/media/image240.wmf) | oc/media/image243.wmf) |
| iques/Cours/pandoc/ |                       |                        |
| media/image240.wmf) |                       |                        |
+---------------------+-----------------------+------------------------+
| ![](                | ![](11-Actions Méca   | ![](11-Actions Mé      |
| 11-Actions Mécaniqu | niques/Cours/pandoc/m | caniques/Cours/pandoc/ |
| es/Cours/pandoc/med | edia/image244.wmf)est | media/image244.wmf)est |
| ia/image244.wmf)est | **SUR** **le cône     | **SUR** **le cône de   |
| à **L'INTERIEUR**   | [d'adh                | [fro                   |
| **du cône           | érence]{.underline}** | ttement]{.underline}** |
| [d'adhér            |                       |                        |
| ence]{.underline}** |                       |                        |
+---------------------+-----------------------+------------------------+
| $d\o                | $d\overrightarrow{T_{ | $d\overrightarrow{T_   |
| verrightarrow{T_{1  | 1 \rightarrow 2}(P)}$ | {1 \rightarrow 2}(P)}$ |
| \rightarrow 2}(P)}$ | ***s'oppose à la      | ***s'oppose au         |
| ***s'oppose à la    | tendance au           | glissement de 2/1.***  |
| tendance au         | glissement de 2/1.*** | $d\overright           |
| glissement*** ***de |                       | arrow{T_{1 \rightarrow |
| 2/1.***             |                       |  2}(P)} \land \overrig |
|                     |                       | htarrow{V_{P \in 2/1}} |
|                     |                       |  = \overrightarrow{0}$ |
|                     |                       |                        |
|                     |                       | $d\overrightarrow      |
|                     |                       | {T_{1 \rightarrow 2}(P |
|                     |                       | )} \cdot \overrightarr |
|                     |                       | ow{V_{P \in 2/1}} < 0$ |
+---------------------+-----------------------+------------------------+

> **Coefficients de frottement et d'adhérence :**
> ![](11-Actions Mécaniques/Cours/pandoc/media/image245.wmf) **ou**
> ![](11-Actions Mécaniques/Cours/pandoc/media/image246.wmf)

![](11-Actions Mécaniques/Cours/pandoc/media/image247.png){width="2.5569444444444445in"
height="1.51875in"}Le coefficient d'adhérence
![](11-Actions Mécaniques/Cours/pandoc/media/image248.wmf)est toujours
légèrement supérieur au coefficient de frottement
![](11-Actions Mécaniques/Cours/pandoc/media/image249.wmf)(![](11-Actions Mécaniques/Cours/pandoc/media/image250.wmf)).

On fera cependant, lors de l'étude du comportement statique et dynamique
des systèmes, l'hypothèse simplificatrice qu'ils sont égaux. ***On
utilisera alors uniquement le coefficient de frottement que l'on
notera*** : ![](11-Actions Mécaniques/Cours/pandoc/media/image251.wmf)
ou ![](11-Actions Mécaniques/Cours/pandoc/media/image252.wmf)**.**

+---------------------------------+------------------------------------+
| La valeur de ce coefficient     |                                    |
+=================================+====================================+
| ne dépend pas** :**             | dépend essentiellement :           |
+---------------------------------+------------------------------------+
| -   de l'intensité de la force  | -   de la **nature des matériaux** |
|     élémentaire de pression ;   |     > en contact ;                 |
|                                 |                                    |
| -   de l'étendue de la surface  | -   de la présence ou non de       |
|     de contact.                 |     > **lubrifiant **;             |
|                                 |                                    |
|                                 | -   de l'état de rugosité,         |
|                                 |     > température,...              |
+---------------------------------+------------------------------------+

  ------------------------------------------------------------------------
  **matériaux** en       **f** ou **μ**        
  contact                                      
  ---------------------- --------------------- ---------------------------
                         Surfaces **sèches**   Surfaces **lubrifiées**

  **Acier/Acier**        **0.15**              **0.09**

  **Acier/Fonte**        **0.16**              **0.08 à 0.04**

  **Acier/Bronze**       **0.10**              **0.09**

  **Téflon/Acier**       **0.04**              **-**

  **Fonte/Bronze**       **0.20**              **0.08 à 0.04**

  **Nylon/Acier**        **0.35**              **0.12**

  **Bois/Bois**          **0.4 à 0.2**         **0.16 à 0.04**

  **Pneu/Route**         **0.6**               **0.30 à 0.10**
  ------------------------------------------------------------------------

*[Quelques ordres de grandeurs de coefficient de frottement
:]{.underline}*

-   **[Point de vue local]{.underline}**

Lors de la prise en compte du phénomène d'adhérence dans l'étude du
comportement statique d'un système, ***on se placera à la limite du
glissement*** pour exprimer le torseur de l'action mécanique de 1
agissant sur 2 :

![](11-Actions Mécaniques/Cours/pandoc/media/image253.wmf)

*Ainsi on pourra utiliser l'équation qui lie*
![](11-Actions Mécaniques/Cours/pandoc/media/image254.wmf)*(en général
connu),* ![](11-Actions Mécaniques/Cours/pandoc/media/image255.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image256.wmf) :
![](11-Actions Mécaniques/Cours/pandoc/media/image257.wmf)

En résumé :

-   L'existence d'un frottement dans une liaison implique qu'une
    composante nulle devient non nulle

-   L'effort tangentiel s'oppose toujours au mouvement

-   Pour modéliser l'AM, il faut isoler le solide en mouvement

-   Le cône de frottement se trouve toujours du côté du solide isolé

-   Le coefficient de frottement est positif et correspond au rapport de
    l'effort tangentiel et de l'effort normal ; on a :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image258.wmf)

-   L'angle $\varphi$ correspond au demi-angle au sommet du cône.

+-------+--------------------------------------------------------------+
| >     | **Inclinaison**                                              |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mécaniques                                    |
| ions  | /Cours/pandoc/media/image259.png){width="5.84292104111986in" |
| Mécan | height="4.599503499562554in"}                                |
| iques |                                                              |
| /Cour | **Déterminer l'angle à partir duquel la caisse se met à      |
| s/pan | glisser.**                                                   |
| doc/m |                                                              |
| edia/ |                                                              |
| image |                                                              |
| 8.png |                                                              |
| ){wid |                                                              |
| th="0 |                                                              |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Collecteur de MCC**                                        |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mécaniques/C                                  |
| ions  | ours/pandoc/media/image260.jpeg){width="6.253472222222222in" |
| Mécan | height="3.6868055555555554in"}                               |
| iques |                                                              |
| /Cour | **Déterminer l'angle à partir duquel la caisse se met à      |
| s/pan | glisser.**                                                   |
| doc/m |                                                              |
| edia/ | Le système représente un porte-balai de moteur à courant     |
| image | continu. Le levier sollicité par le ressort de traction      |
| 8.png | appuie le charbon sur le collecteur pour faire le contact    |
| ){wid | électrique. Pour un bon fonctionnement du moteur, l'effort   |
| th="0 | presseur sur le collecteur doit être de 6 N.                 |
| .6262 |                                                              |
| 69685 | La liaison charbon / collecteur au point E est assimilé à    |
| 03937 | une liaison ponctuelle de normale $\overrightarrow{y}$. avec |
| 01in" | frottement tel que                                           |
| >     | $\left\| \overright                                          |
| heigh | arrow{R_{collecteur \rightarrow charbon}} \right\| = \ 6\ N$ |
| t="0. | et f = 0,2.                                                  |
| 65083 |                                                              |
| 33333 | **Exprimer le torseur de l'action du collecteur sur le       |
| 33333 | charbon en E (calculer ses composantes).**                   |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Prise en compte du phénomène de frottement dans une liaison pivot

Dans le cas d'une liaison pivot, le frottement est modélisé par un
torseur couple avec un couple de frottement (sec, visqueux ou fluide)
qui est en général (par convention) affublé du signe « - ».

![](11-Actions Mécaniques/Cours/pandoc/media/image262.wmf)

##### ![](11-Actions Mécaniques/Cours/pandoc/media/image263.png){width="2.598611111111111in" height="1.9368055555555554in"}Autres phénomènes de frottements {#autres-phénomènes-de-frottements .unnumbered}

-   Résistance au pivotement

La résistance au pivotement est liée est un frottement qui apparait
lorsqu'on essaye de faire pivoter deux surfaces l'une sur l'autre (comme
un pneu sur le sol lorsqu'on est à l'arrêt). Elle se modélise par un
moment perpendiculaire au plan tangent aux deux surfaces.

-   Résistance au roulement

La résistance au roulement existe à partir du moment où on fait rouler
un solide sur un autre solide. La pression de contact due à une surface
très réduite (théoriquement ponctuelle ou linéaire) créé une déformation
plus ou moins importante qui induit une perte d'énergie. Ce phénomène
peut être modélisé par un torseur couple avec un moment qui tend à
s'opposer au mouvement de rotation.

![](11-Actions Mécaniques/Cours/pandoc/media/image264.png){width="6.569199475065616in"
height="2.495840988626422in"}

### Phénomène d'arc-boutement

![](11-Actions Mécaniques/Cours/pandoc/media/image265.png){width="0.8951388888888889in"
height="1.0569444444444445in"}On appelle arc-boutement, le phénomène
issu de l'adhérence pour lequel un équilibre subsiste indépendamment de
l'intensité de l'effort qui tend à le rompre.

**[Exemple :]{.underline}** sur un serre-joint c'est le phénomène
d'arc-boutement qui solidarise le mord mobile et le mord fixe après la
1^ère^ phase de réglage de l'écart entre les deux mords.

On peut aussi citer l'exemple du tiroir qui se bloque et les pinces de
la cordeuse vue en TP.

## ![](11-Actions Mécaniques/Cours/pandoc/media/image266.jpeg){width="2.6729166666666666in" height="1.7027777777777777in"}Moment d'une force et Bras de Levier

Le moment d'une force par rapport à un point est un outil qui permet de
mesurer la capacité de cette force à créer un mouvement de rotation
autour de ce point ou à l'empêcher.

Soit un effort
![](11-Actions Mécaniques/Cours/pandoc/media/image267.wmf) appliqué au
point Q. Le moment crée par cet effort au point P est un **vecteur**
noté ${\overrightarrow{M}}_{P,\overrightarrow{F}}$tel que :

$${\overrightarrow{M}}_{P,\overrightarrow{F}} = \overrightarrow{PQ} \land \overrightarrow{F}$$

Si on prend la norme du moment de cette force, on dit que le moment est
le produit de la force par le **bras de levier** (ici d=PH). Seule
contrainte, le bras de levier doit être perpendiculaire à la force.

$$\left\| {\overrightarrow{M}}_{P,\overrightarrow{F}} \right\| = \overline{PH}\left\| \overrightarrow{F} \right\| = Fd$$

Dans le cas où le bras de levier et la force ne sont pas
perpendiculaires, il faut faire des projections. Cela permet de vérifier
les résultats rapidement dans le cas où on doit calculer les moments de
glisseurs. En observant la tendance au mouvement de rotation il est
aussi possible de déterminer le sens et la direction.

+-------+--------------------------------------------------------------+
| >     | **Bras de leviers 1**                                        |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mécaniques/                                   |
| ions  | Cours/pandoc/media/image268.png){width="2.033333333333333in" |
| Mécan | height="1.0472222222222223in"}![](11-Actions Mécaniques/C    |
| iques | ours/pandoc/media/image268.png){width="1.9897123797025371in" |
| /Cour | height="1.0805555555555555in"}![](11-Action                  |
| s/pan | s Mécaniques/Cours/pandoc/media/image268.png){width="1.85in" |
| doc/m | height="1.0472222222222223in"}                               |
| edia/ |                                                              |
| image | **Déterminer le moment en O pour les trois cas ci-dessus.**  |
| 8.png |                                                              |
| ){wid |                                                              |
| th="0 |                                                              |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Bras de leviers 2**                                        |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mécaniques/                                   |
| ions  | Cours/pandoc/media/image269.png){width="6.183473315835521in" |
| Mécan | height="3.5243153980752404in"}                               |
| iques |                                                              |
| /Cour | **Calculer le moment résultant au niveau de l'axe de         |
| s/pan | rotation situé au centre du disque. Ces disques sont-ils à   |
| doc/m | l'équilibre ? Sinon, dans quel sens tourneront-ils ? Le      |
| edia/ | rayon du disque est de 10 cm.**                              |
| image |                                                              |
| 8.png |                                                              |
| ){wid |                                                              |
| th="0 |                                                              |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Vérin électrique**                                         |
| ![](1 |                                                              |
| 1-Act | Soit la modélisation d'un vérin électrique, en utilisant un  |
| ions  | modèle poutre :                                              |
| Mécan |                                                              |
| iques | ![](11-Actions Mécaniques/Cours/pandoc/media/image270.png)   |
| /Cour |                                                              |
| s/pan | **Déterminer les moments en A pour chaque effort (F, Y~A~,   |
| doc/m | X~A~, Y~B~)**                                                |
| edia/ |                                                              |
| image |                                                              |
| 8.png |                                                              |
| ){wid |                                                              |
| th="0 |                                                              |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | ![Image5](11-Actio                                           |
| ![](1 | ns Mécaniques/Cours/pandoc/media/image17.jpeg){width="2.5in" |
| 1-Act | height="1.925in"}**Poussoir et coulisseau**                  |
| ions  |                                                              |
| Mécan | On associe les repères :                                     |
| iques |                                                              |
| /Cour | > \-                                                         |
| s/pan | > $R_{0}(O,\overset{\rightarrow}{x_{0}}                      |
| doc/m | ,\overset{\rightarrow}{y_{0}},\overset{\rightarrow}{z_{0}})$ |
| edia/ | > au bâti 0, tel que                                         |
| image | >                                                            |
| 8.png | $\overset{\rightarrow}{OB} = b.\overset{\rightarrow}{x_{0}}$ |
| ){wid | >                                                            |
| th="0 | > \-                                                         |
| .6262 | > $R_{1}(O,\overset{\rightarrow}{x_{1}}                      |
| 69685 | ,\overset{\rightarrow}{y_{1}},\overset{\rightarrow}{z_{1}})$ |
| 03937 | > au poussoir 1, tels que                                    |
| 01in" | >                                                            |
| >     | > $\over                                                     |
| heigh | set{\rightarrow}{BA} = \lambda.\overset{\rightarrow}{y_{0}}$ |
| t="0. | > et                                                         |
| 65083 | > $\alpha =                                                  |
| 33333 | (\overset{\rightarrow}{x_{0}},\overset{\rightarrow}{x_{1}})$ |
| 33333 |                                                              |
| 4in"} | **Déterminer**                                               |
|       | $\overrightarrow{\mathbf{M}_{\mathbf{O,2 \rightarrow 1}}}$   |
|       | **en utilisant le bras de levier**                           |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Console de bateaux**                                       |
| ![](1 |                                                              |
| 1-Act | Soit une console portante de bateaux.                        |
| ions  |                                                              |
| Mécan | ![](11-Actions Mécaniques                                    |
| iques | /Cours/pandoc/media/image3.jpeg){width="4.066666666666666in" |
| /Cour | height="2.5083333333333333in"}                               |
| s/pan |                                                              |
| doc/m | **Déterminer la relation entre F3 et Fv en utilisant les     |
| edia/ | bras de leviers pour calculer les moments au point A autour  |
| image | de l'axe z et en appliquant le théorème du moment statique.  |
| 8.png | Les moments résultants en A des actions mécaniques en A, B   |
| ){wid | et D sont nuls.**                                            |
| th="0 |                                                              |
| .6262 | $$e \cdot F_{V} - c \cdot F_{3} = 0$$                        |
| 69685 |                                                              |
| 03937 | $$\Rightarrow F_{3} = \frac{e \cdot F_{V}}{c}$$              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

## ![](11-Actions Mécaniques/Cours/pandoc/media/image271.jpeg){width="2.7555555555555555in" height="1.7847222222222223in"}Masse -- Centre d'inertie

### Masse

Au point **P** d'un solide **S**, la masse *dm* d'un petit élément de
volume *dv* s'exprime : $dm = \rho.dv$

*La masse volumique, notée ρ est exprimée en kg/m^3.^*

La masse du solide S est alors :
$M = \int_{S}^{}{dm} = \int_{S}^{}{\rho.dv}$

Dans la plupart des cas, le matériau constituant le solide est homogène,
on a donc : $M = \rho.V$

*[Quelques ordres de grandeurs (eau : 1000 kg/m^3^)]{.underline}*

  ------------------------- ---------------------------------------------
  matériau                  Masse volumique

  Acier                     7850 kg/m^3^

  Aluminium                 2700 kg/m^3^

  Fonte                     6800-7400 kg/m^3^
  ------------------------- ---------------------------------------------

### Centre d'inertie

Le centre d'inertie d'un solide S est le barycentre G des masses
élémentaires :
$\int_{S}^{}{\overrightarrow{GP}.dm = \overrightarrow{0}}$

Soit un repère
$R(O,\overrightarrow{x},\overrightarrow{y},\overrightarrow{z})$ lié au
solide S

$$\overrightarrow{GP} = \overrightarrow{GO} + \overrightarrow{OP}$$

On a donc :

$\int_{S}^{}{\overrightarrow{GO}.dm + \int_{S}^{}{\overrightarrow{OP}.dm} = \overrightarrow{0}}$
$\overrightarrow{GO}\int_{S}^{}{dm + \int_{S}^{}{\overrightarrow{OP}.dm} = \overrightarrow{0}}$

Ce qui nous conduit à :
$\overrightarrow{OG} = \frac{1}{M}\int_{S}^{}{\overrightarrow{OP}.dm}$

**Le centre d'inertie se situe sur les éléments de symétrie du solide
(point, plan, droite)**

![](11-Actions Mécaniques/Cours/pandoc/media/image272.jpeg){width="2.204861111111111in"
height="1.4270833333333333in"}

**Remarque**

Le centre de gravité d'un solide est le point d'application de la
résultante des efforts de pesanteur.

On montre que :

##### Ensemble de solides {#ensemble-de-solides .unnumbered}

Le centre d'inertie d'un **ensemble Σ** de **n** **solides S~i~** , de
**masse mi** et **centre d'inertie** **G~i~**, est **G~Σ~** tel que:

$\overrightarrow{OG_{\Sigma}} = \frac{1}{M}\sum_{i = 1}^{n}{m_{i}.\overrightarrow{OG_{i}}}$
avec $M = \sum_{i = 1}^{n}m_{i}$

***Cette relation permet de déterminer la position du centre d'inertie
d'un solide complexe que l'on considère comme un assemblage de volumes
élémentaires***

+-------+--------------------------------------------------------------+
| >     | **Maison hantée**                                            |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mé                                            |
| ions  | caniques/Cours/pandoc/media/image273.jpeg){width="4.30625in" |
| Mécan | height="2.3618055555555557in"}                               |
| iques |                                                              |
| /Cour | La masse des passagers d'un véhicule est de 170kg, la masse  |
| s/pan | de la nacelle du véhicule est de 100kg. Le centre de gravité |
| doc/m | de la nacelle est déporté vers l\'arrière par addition d\'un |
| edia/ | contrepoids afin de faciliter son mouvement de rotation.     |
| image |                                                              |
| 8.png | **Déterminer la position du centre de gravité (noté CDG) de  |
| ){wid | la partie supérieure du chariot (Passagers + Nacelle +       |
| th="0 | Contrepoids) par rapport à l\'axe de rotation (voir figure   |
| .6262 | ci-contre).**                                                |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Echelle de pompier EPAS**                                  |
| ![](1 |                                                              |
| 1-Act | Dans une première approche, le parc échelle d'une échelle de |
| ions  | pompier peut être modélisé par un assemblage de trois        |
| Mécan | plaques rectangulaires homogènes d'épaisseur négligeable, de |
| iques | longueur L et de largeur h.                                  |
| /Cour |                                                              |
| s/pan | Chaque plaque a une masse notée m.                           |
| doc/m |                                                              |
| edia/ | ![modele%20echelle%203](11-Actions M                         |
| image | écaniques/Cours/pandoc/media/image274.png){width="5.15625in" |
| 8.png | height="2.0520833333333335in"}                               |
| ){wid |                                                              |
| th="0 | **Montrer que le vecteur position**                          |
| .6262 | $\overset{\rightarrow}{\mathbf{OG}}$ **du centre de gravité  |
| 69685 | G du parc échelle est tel que**                              |
| 03937 | $\overset{\rightarrow}{\mathbf{OG}}\mathbf{=}\               |
| 01in" | frac{\mathbf{L}}{\mathbf{2}}\mathbf{\cdot}{\overrightarrow{\ |
| >     | mathbf{x}}}_{\mathbf{5}}\mathbf{+}\frac{\mathbf{h}}{\mathbf{ |
| heigh | 3}}\mathbf{\cdot}{\overrightarrow{\mathbf{y}}}_{\mathbf{5}}$ |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
|       |                                                              |
+-------+--------------------------------------------------------------+

## Opérateur d'inertie - Effets d'inertie

![](11-Actions Mécaniques/Cours/pandoc/media/image275.jpeg){width="1.867361111111111in"
height="2.3152777777777778in"}La masse m ne permet pas à elle seule de
caractériser la difficulté de mettre un solide en mouvement ou de l'en
empêcher... On a besoin de connaître la façon dont cette masse est
répartie sur le solide. **Le moment d'inertie** et **le produit
d'inertie** caractérisent cette répartition autour d'un axe.

Ces deux quantités s'expriment en **kg.m²** et seront regroupées dans
l'opérateur d'inertie qui sera utilisé pour appliquer le principe
fondamental de la dynamique.

*L'inertie traduit le fait qu'il est plus facile de mettre en mouvement
de rotation un solide autour d'un axe plutôt qu'un autre. Par exemple
pour le balai ci-contre, il est plus facile d'entraîner en rotation
suivant l'axe* $\Delta_{1}$ *que suivant l'axe* $\Delta_{2}$*.*

*On peut retenir que plus la masse est éloignée de l'axe de rotation,
plus l'inertie sera grande.*

### ![](11-Actions Mécaniques/Cours/pandoc/media/image276.jpeg){width="2.9in" height="1.3284722222222223in"}Moment d'inertie

**Le moment d'inertie caractérise la répartition de la masse d'un solide
S autour d'un axe ∆.**

Plus il est grand, c'est-à-dire plus la matière est éloignée de l'axe,
et plus il sera difficile de mettre le solide en rotation autour de cet
axe.

On note : $I_{\Delta} = \int_{S}^{}{r²dm}$ , **r est la distance entre
le point P et l'axe ∆**

[Cas où le moment d'inertie est nul :]{.underline}

-   si le solide est assimilé à une tige rectiligne d'axe ∆ (rayon
    négligeable devant sa longueur),

-   si on considère un point matériel (dimensions négligeables)

![](11-Actions Mécaniques/Cours/pandoc/media/image277.jpeg){width="1.7673611111111112in"
height="1.9423611111111112in"}

##### Théorème de Huygens {#théorème-de-huygens .unnumbered}

On passe du moment d'inertie autour de l'axe ∆ et passant par le centre
d'inertie G du solide de masse m au moment d'inertie autour d'un axe
parallèle ∆', par la relation :

$I_{\Delta'} = I_{G\Delta} + md²$ **d est la distance entre l'axe ∆' et
G**

Cette relation est principalement utilisée pour calculer des moments
d'inertie dans le cas de mouvements plans...

### Produit d'inertie

Le produit d'inertie caractérise l'absence de symétrie dans la
répartition des masses autour des 3 axes d'un repère lié à un solide.

On définit par :

$J_{O_{yz}} = \int_{S}^{}{y.z.dm}$ , Le produit d'inertie du solide S
par rapport au plan$(O,\overrightarrow{y},\overrightarrow{z})$

$J_{O_{zx}} = \int_{S}^{}{z.x.dm}$, Le produit d'inertie du solide S par
rapport au plan$(O,\overrightarrow{z},\overrightarrow{x})$

$J_{O_{xy}} = \int_{S}^{}{x.y.dm}$, Le produit d'inertie du solide S par
rapport au plan$(O,\overrightarrow{x},\overrightarrow{y})$

x, y et z sont les coordonnées du point P auquel est associé le petit
élément de masse dm

![](11-Actions Mécaniques/Cours/pandoc/media/image278.jpeg){width="2.4930555555555554in"
height="1.2722222222222221in"}

Ce sont ces termes qui vont créer des effets de « balourd »
perpendiculaires à l'axe autour duquel on souhaite faire tourner le
solide et engendre des vibrations. Cet effet est parfois recherché
(machines vibratoires) ou combattu (machines tournantes).

### L'opérateur d'inertie : la matrice d'inertie d'un solide \[I~0~(S)\]

On peut synthétiser les notions « d'effet d'inertie » décrites
précédemment dans un opérateur linéaire d'inertie. Appliqué à un vecteur
$\overrightarrow{u}$ en un point O d'un solide S, il est défini par :

$$\left\lbrack I_{O}(S) \right\rbrack.\overrightarrow{u} = \int_{S}^{}{\overrightarrow{OP} \land (\overrightarrow{u} \land \overrightarrow{OP})dm}$$

Dans un repère orthonormé direct
$\left( O,\ \overrightarrow{x},\ \overrightarrow{y},\ \overrightarrow{z} \right)$
lié au solide S, et M un point de ce solide défini par
$\overrightarrow{OM} = x.\overrightarrow{x} + y.\overrightarrow{y} + z.\overrightarrow{z}$,
alors :

$${\lbrack I}_{M(S)}\rbrack = \overline{\overline{I_{M(S)}}} = \begin{pmatrix}
\int_{S}^{}{\left( y^{2} + z^{2} \right)dm} & - \int_{S}^{}{x.y.dm} & - \int_{S}^{}{z.x.dm} \\
 - \int_{S}^{}{x.y.dm} & \int_{S}^{}{\left( z^{2} + x^{2} \right)dm} & - \int_{S}^{}{y.z.dm} \\
 - \int_{S}^{}{z.x.dm} & - \int_{S}^{}{y.z.dm} & \int_{S}^{}{\left( x^{2} + y^{2} \right)dm}
\end{pmatrix}_{\left( \overrightarrow{x},\ \overrightarrow{y},\ \overrightarrow{z} \right)}$$

Cette matrice est souvent notée
${\lbrack I}_{M(S)}\rbrack = \overline{\overline{I_{M(S)}}} = \begin{pmatrix}
A & - F & - E \\
 - F & B & - D \\
 - E & - D & C
\end{pmatrix}_{\left( \overrightarrow{x},\ \overrightarrow{y},\ \overrightarrow{z} \right)}$

**A, B et C** sont respectivement les **moments d'inertie** par rapport
aux axes $\left( O,\ \overrightarrow{x} \right)$,
$\left( O,\ \overrightarrow{y} \right)$ et
$\left( O,\ \overrightarrow{z} \right)$ respectivement. Ces quantités
sont toujours positives. On note également A=I~Ox~, B=I~Oy~ et C=I~Oz~.

**D, E et F** sont les **produits d'inertie** par rapport aux axes,
respectivement,
$\left( O,\ \overrightarrow{y} \right)$-$\left( O,\ \overrightarrow{z} \right)$,
$\left( O,\ \overrightarrow{z} \right)$-$\left( O,\ \overrightarrow{x} \right)$,
$\left( O,\ \overrightarrow{x} \right)$-$\left( O,\ \overrightarrow{y} \right)$.
Ces quantités sont de signe quelconque. On note également D=P~Oyz~,
E=P~Oxz~ et F=P~Oxy~.

A, B, C, D, E et F s'expriment en kg.m^2^

-   La matrice d'inertie est **symétrique**

-   Les **moments d'inertie** sont sur la **diagonale**.

-   Les **produits d'inertie**, affectés du **signe moins** sont **en
    dehors de la diagonale**.

+-------+--------------------------------------------------------------+
| >     | **Bandeau d'affiches**                                       |
| ![](1 |                                                              |
| 1-Act | On donne ci-dessous le modèle volumique d'un rouleau         |
| ions  | d'affiche vide accompagné de ses propriétés de masse.        |
| Mécan |                                                              |
| iques |   ----------------------------                               |
| /Cour | ------------------------------------------------------------ |
| s/pan |   ![](11-Actions Mécaniques/                                 |
| doc/m | Cours/pandoc/media/image279.png){width="6.073418635170603in" |
| edia/ |   height="3.24375656167979in"}                               |
| image |   ----------------------------                               |
| 8.png | ------------------------------------------------------------ |
| ){wid |                                                              |
| th="0 |   ----------------------------                               |
| .6262 | ------------------------------------------------------------ |
| 69685 |                                                              |
| 03937 | **En utilisant le tableau des propriétés de masse du modèle  |
| 01in" | volumique, donner la valeur de**                             |
| >     | $\mathbf{                                                    |
| heigh | J}_{\mathbf{r}\mathbf{\ }\mathbf{mod}\mathbf{è}\mathbf{le}}$ |
| t="0. | **(moment d'inertie du modèle du rouleau vide par rapport à  |
| 65083 | son axe).**                                                  |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

##### Base principale d'inertie {#base-principale-dinertie .unnumbered}

La matrice ${\lbrack I}_{M(S)}\rbrack$ étant symétrique, elle est
diagonalisable. On démontre qu'en O il existe une base
$\left( \overrightarrow{x},\ \overrightarrow{y},\ \overrightarrow{z} \right)$
dite base principale en O telle que $I_{O(S)}$ soit diagonale :

${\lbrack I}_{O(S)}\rbrack = \begin{pmatrix}
A & 0 & 0 \\
0 & B & 0 \\
0 & 0 & C
\end{pmatrix}_{\left( \overrightarrow{x},\ \overrightarrow{y},\ \overrightarrow{z} \right)}$.
Dans ce cas A, B et C sont dits moments d'inertie principaux.

### Symétries matérielles

On dit qu'il y a symétrie matérielle lorsqu'il y a la fois : **symétrie
géométrique** et symétrie **de répartition des masses**. Prendre en
compte les symétries matérielles permet de simplifier l'expression des
matrices d'inerties.

##### Cas où le solide présente 1 plan de symétrie {#cas-où-le-solide-présente-1-plan-de-symétrie .unnumbered}

Le plan ![](11-Actions Mécaniques/Cours/pandoc/media/image280.wmf) est
plan de symétrie matérielle de normale
![](11-Actions Mécaniques/Cours/pandoc/media/image281.wmf) pour le
solide.

![](11-Actions Mécaniques/Cours/pandoc/media/image282.jpeg){width="6.009027777777778in"
height="2.172222222222222in"}

##### Cas où le solide présente 2 plans de symétrie {#cas-où-le-solide-présente-2-plans-de-symétrie .unnumbered}

![](11-Actions Mécaniques/Cours/pandoc/media/image283.jpeg){width="3.0388888888888888in"
height="3.126388888888889in"}Les plans
$(O,\overrightarrow{x},\overrightarrow{y})$ et
$(O,\overrightarrow{x},z)$ sont des plans de symétrie matérielle de
normales $\overrightarrow{z}$ et $\overrightarrow{y}$ pour le solide.

##### Cas où le solide présente 1 symétrie de révolution {#cas-où-le-solide-présente-1-symétrie-de-révolution .unnumbered}

![](11-Actions Mécaniques/Cours/pandoc/media/image284.jpeg){width="2.904861111111111in"
height="2.2888888888888888in"}Un solide de révolution autour de
![](11-Actions Mécaniques/Cours/pandoc/media/image281.wmf) possède au
moins deux plans de symétrie, donc les produits d'inertie sont nuls.

De plus, les axes $\overrightarrow{x}$ et $\overrightarrow{y}$
***[jouent le même rôle]{.underline}*** du point de vue de la géométrie
et de la répartition des masses, donc :

##### Cas où le solide est d'épaisseur négligeable {#cas-où-le-solide-est-dépaisseur-négligeable .unnumbered}

![](11-Actions Mécaniques/Cours/pandoc/media/image285.jpeg){width="2.9763888888888888in"
height="2.8222222222222224in"}Si l'épaisseur suivant
$\overrightarrow{z}$ est négligeable devant les autres dimensions (cas
d'une plaque) on peut considérer que $z = 0$ :

### ![](11-Actions Mécaniques/Cours/pandoc/media/image286.jpeg){width="3.2819444444444446in" height="1.820138888888889in"}Théorème de Huygens généralisé

Le **passage** de la **matrice d'inertie** en un **point quelconque A**
du solide S à la matrice d'inertie au **centre d'inertie G** s'écrit :

$\left\lbrack I_{A}(S) \right\rbrack = \left\lbrack I_{G}(S) \right\rbrack + m\begin{bmatrix}
b² + c² & - a.b & - a.c \\
 - a.b & a² + c² & - b.c \\
 - a.c & - b.c & a² + b²
\end{bmatrix}$

avec
$\overrightarrow{AG} = a.\overrightarrow{x} + b.\overrightarrow{y} + c.\overrightarrow{z}$

![600px-Panneau_attention](11-Actions Mécaniques/Cours/pandoc/media/image287.png){width="0.375in"
height="0.3173611111111111in"}

+-------+--------------------------------------------------------------+
| >     | **Panneau solaire**                                          |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mécaniques/C                                  |
| ions  | ours/pandoc/media/image288.png){width="2.8020833333333335in" |
| Mécan | height="1.8333333333333333in"}                               |
| iques |                                                              |
| /Cour | En première approximation, des panneaux solaires peuvent     |
| s/pan | être assimilés à des plaques de matériau homogène de masse   |
| doc/m | m, d\'épaisseur négligeable, de longueur a et de largeur b.  |
| edia/ |                                                              |
| image | **Déterminer les trois produits d'inertie en O du solide     |
| 8.png | S.**                                                         |
| ){wid |                                                              |
| th="0 | **En déduire \[I~G~(S)\] à l'aide de Huygens généralisé.**   |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Détermination de la matrice d'inertie à partir des résultats classiques

-   Pour l'ensemble des constantes d'inertie, si S~1~, ..., S~i~, ...,
    S~n~ sont n solides disjoints nous avons, si nous notons S la
    réunion de ces solides :
    \[$I_{O(S)}\rbrack = \sum_{i = 1}^{n}{\lbrack I_{O\left( S_{i} \right)}\rbrack}$

```{=html}
<!-- -->
```
-   Le tableau suivant donne la matrice d'inertie de quelques solides
    usuels. Chaque solide est homogène, de masse m et de centre de
    gravité G.

+---------------+-----------------+------------------------------------+
| **Tige        | ![File0077      | $$\begin{pmatrix}                  |
| rectiligne**  | .jpg](11-Action | m.\frac{h^{2}}{3} & 0 & 0 \\       |
|               | s Mécaniques/Co | 0 & m.\frac{h^{2}}{3} & 0 \\       |
| *Longueur     | urs/pandoc/medi | 0 & 0 & 0                          |
| 2.h*          | a/image289.jpeg | \end{pmatrix}_{\left( G,\  - ,\    |
|               | ){width="1.3722 | - ,\ \overrightarrow{z} \right)}$$ |
|               | 222222222222in" |                                    |
|               | height="1.26736 |                                    |
|               | 11111111112in"} |                                    |
+===============+=================+====================================+
| **Cercle**    | ![File007       | $$\begin{pmatrix}                  |
|               | 8.jpg](11-Actio | m.\frac{R^{2}}{4} & 0 & 0 \\       |
| *Rayon R*     | ns Mécaniques/C | 0 & m.\frac{R^{2}}{4} & 0 \\       |
|               | ours/pandoc/med | 0 & 0 & m.\frac{R^{2}}{2}          |
| *Aire*        | ia/image290.jpe | \end{pmatrix}_{\left( G,\  - ,\    |
| $\pi.R^{2}$   | g){width="1.395 | - ,\ \overrightarrow{z} \right)}$$ |
|               | 138888888889in" |                                    |
|               | height="1.15138 |                                    |
|               | 88888888888in"} |                                    |
+---------------+-----------------+------------------------------------+
| **Rectangle** | ![File0079      | $$\begin{pmatrix}                  |
|               | .jpg](11-Action | m.\frac{b^{2}}{3} & 0 & 0 \\       |
| *Aire         | s Mécaniques/Co | 0 & m.\frac{a^{2}}{3} & 0 \\       |
| S=4.a.b*      | urs/pandoc/medi | 0 & 0 & m.\fra                     |
|               | a/image291.jpeg | c{\left( a^{2} + b^{2} \right)}{3} |
|               | ){width="1.4652 | \end{pmatrix}_{\left( G,\ \o       |
|               | 777777777777in" | verrightarrow{x}\ \overrightarrow{ |
|               | height="1.15138 | y},\ \overrightarrow{z} \right)}$$ |
|               | 88888888888in"} |                                    |
+---------------+-----------------+------------------------------------+
| **Tronc de    | ![File0080      | $$\begin{pmatrix}                  |
| cylindre de   | .jpg](11-Action | m.\frac{R^{2}}{                    |
| révolution**  | s Mécaniques/Co | 4} + m.\frac{h^{2}}{12} & 0 & 0 \\ |
|               | urs/pandoc/medi | 0 & m.\frac{R^{                    |
| *Rayon R*     | a/image292.jpeg | 2}}{4} + m.\frac{h^{2}}{12} & 0 \\ |
|               | ){width="1.5118 | 0 & 0 & m.\frac{R^{2}}{2}          |
| *Volume*      | 055555555556in" | \end{pmatrix}_{\left( G,\  - ,\    |
| $V =          | height="1.34861 | - ,\ \overrightarrow{z} \right)}$$ |
|  \pi.R^{2}.h$ | 11111111112in"} |                                    |
+---------------+-----------------+------------------------------------+
| **Pa          | ![File0081      | $$\begin{pmatrix}                  |
| rallélépipède | .jpg](11-Action | \frac{m}{3}.\left                  |
| rectangle**   | s Mécaniques/Co | ( b^{2} + c^{2} \right) & 0 & 0 \\ |
|               | urs/pandoc/medi | 0 & \frac{m}{3}.\                  |
| *Volume       | a/image293.jpeg | left( c^{2} + a^{2} \right) & 0 \\ |
| V=8.a.b.c*    | ){width="1.2208 | 0 & 0 & \frac{                     |
|               | 333333333334in" | m}{3}.\left( a^{2} + b^{2} \right) |
|               | heig            | \end{pmatrix}_{\left( G,\ \o       |
|               | ht="1.08125in"} | verrightarrow{x}\ \overrightarrow{ |
|               |                 | y},\ \overrightarrow{z} \right)}$$ |
+---------------+-----------------+------------------------------------+
| **Boule**     | ![File0082      | $$\begin{pmatrix}                  |
|               | .jpg](11-Action | \frac{2}{5}m.R^{2} & 0 & 0 \\      |
| *Rayon R*     | s Mécaniques/Co | 0 & \frac{2}{5}m.R^{2} & 0 \\      |
|               | urs/pandoc/medi | 0 & 0 & \frac{2}{5}m.R^{2}         |
| *Volume*      | a/image294.jpeg | \end{                              |
| $             | ){width="1.3722 | pmatrix}_{(G,\  - ,\  - ,\  - )}$$ |
| V = \frac{4}{ | 222222222222in" |                                    |
| 3}.\pi.R^{3}$ | height="1.19791 |                                    |
|               | 66666666667in"} |                                    |
+---------------+-----------------+------------------------------------+

![](11-Actions Mécaniques/Cours/pandoc/media/image295.jpeg){width="6.692754811898513in"
height="4.249647856517935in"}

##### Quelques moments d'inertie à connaitre  {#quelques-moments-dinertie-à-connaitre .unnumbered}

![cylindre_creux](11-Actions Mécaniques/Cours/pandoc/media/image296.jpeg){width="1.4048611111111111in"
height="1.65625in"}Cylindre plein : $I_{x} = C = m.\frac{R^{2}}{2}$
Cylindre creux : $I_{x} = C = m.\frac{\left( r^{2} + R^{2} \right)}{2}$

![cylindre_plein](11-Actions Mécaniques/Cours/pandoc/media/image297.jpeg){width="1.3680555555555556in"
height="1.538888888888889in"}

+-------+--------------------------------------------------------------+
| >     | **Rotor MAS**                                                |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mécaniques/C                                  |
| ions  | ours/pandoc/media/image298.jpeg){width="4.104166666666667in" |
| Mécan | height="1.1770833333333333in"} Soit le modèle du rotor d'une |
| iques | MAS représenté ci-dessous :                                  |
| /Cour |                                                              |
| s/pan | ![](11-Actions M                                             |
| doc/m | écaniques/Cours/pandoc/media/image299.jpeg){width="2.3625in" |
| edia/ | height="0.9284722222222223in"}                               |
| image |                                                              |
| 8.png | **Déterminer l'angle à partir duquel la caisse se met à      |
| ){wid | glisser.**                                                   |
| th="0 |                                                              |
| .6262 | **Calculer l\'inertie du rotor du moteur Jm par rapport à    |
| 69685 | son axe à l\'aide du modèle simplifié donné ci-dessous. La   |
| 03937 | densité du matériau de ce rotor est 7,8kg /dm^3^.**          |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Rouleau d'affiches**                                       |
| ![](1 |                                                              |
| 1-Act | -   Un rouleau d'affiches en aluminium est modélisé de la    |
| ions  |     > manière suivante :                                     |
| Mécan |                                                              |
| iques | -   le rouleau supérieur vide est un cylindre creux en       |
| /Cour |     > aluminium de longueur $L$.                             |
| s/pan |                                                              |
| doc/m | -   une fois entièrement enroulé autour du rouleau           |
| edia/ |     > supérieur, le bandeau d'affiches est un cylindre creux |
| image |     > de longueur $L$.                                       |
| 8.png |                                                              |
| ){wid | +-------------------------------------------+------------+   |
| th="0 | |                                           | $$L =      |   |
| .6262 | |                                           | 3200\ mm$$ |   |
| 69685 | |                                           |            |   |
| 03937 | |                                           | **R        |   |
| 01in" | |                                           | ouleau** : |   |
| >     | |                                           |            |   |
| heigh | |                                           | Masse      |   |
| t="0. | |                                           | v          |   |
| 65083 | |                                           | olumique : |   |
| 33333 | |                                           | $          |   |
| 33333 | |                                           | \rho_{r} = |   |
| 4in"} | |                                           |  2,7\ kg.{ |   |
|       | |                                           | dm}^{- 3}$ |   |
|       | |                                           |            |   |
|       | |                                           | $$\p       |   |
|       | |                                           | hi d_{1} = |   |
|       | |                                           |  129\ mm$$ |   |
|       | |                                           |            |   |
|       | |                                           | $$\p       |   |
|       | |                                           | hi d_{2} = |   |
|       | |                                           |  140\ mm$$ |   |
|       | |                                           |            |   |
|       | |                                           | **Bandeau  |   |
|       | |                                           | d'af       |   |
|       | |                                           | fiches** : |   |
|       | |                                           |            |   |
|       | |                                           | Masse      |   |
|       | |                                           | vo         |   |
|       | |                                           | lumique. : |   |
|       | |                                           | $          |   |
|       | |                                           | \rho_{b} = |   |
|       | |                                           |  1,5\ kg.{ |   |
|       | |                                           | dm}^{- 3}$ |   |
|       | |                                           |            |   |
|       | |                                           | $$\p       |   |
|       | |                                           | hi d_{2} = |   |
|       | |                                           |  140\ mm$$ |   |
|       | |                                           |            |   |
|       | |                                           | $$\p       |   |
|       | |                                           | hi d_{3} = |   |
|       | |                                           |  150\ mm$$ |   |
|       | +===========================================+============+   |
|       | +-------------------------------------------+------------+   |
|       |                                                              |
|       | On note :                                                    |
|       |                                                              |
|       | -   $J_{r}$ : moment d'inertie du rouleau supérieur vide par |
|       |     > rapport à son axe,                                     |
|       |                                                              |
|       | -   $J_{b}$ : moment d'inertie du bandeau d'affiches         |
|       |     > enroulées par rapport à l'axe du\                      |
|       |     > rouleau sur lequel il est enroulé.                     |
|       |                                                              |
|       | **Donner l'expression de** $\mathbf{J}_{\mathbf{r}}$ **en    |
|       | fonction de** $\mathbf{\rho}_{\mathbf{r}}$**,**              |
|       | $\mathbf{L}$**,** $\mathbf{d}_{\mathbf{1}}$ **et**           |
|       | $\mathbf{d}_{\mathbf{2}}$**.**                               |
|       |                                                              |
|       | **Calculer** $\mathbf{J}_{\mathbf{r}}$**.**                  |
|       |                                                              |
|       | **Donner l'expression de** $\mathbf{J}_{\mathbf{b}}$ **en    |
|       | fonction de** $\mathbf{\rho}_{\mathbf{b}}$**,**              |
|       | $\mathbf{L}$**,** $\mathbf{d}_{\mathbf{2}}$ **et**           |
|       | $\mathbf{d}_{\mathbf{3}}$**.**                               |
|       |                                                              |
|       | **Quel est le domaine de variation de l'inertie du rouleau   |
|       | par rapport à son axe depuis le rouleau vide jusqu'au        |
|       | rouleau chargé du bandeau d'affiches ?**                     |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Equilibrage dynamique

**L'équilibrage dynamique** concerne les pièces en mouvement de rotation
autour d'un axe fixe dans un repère galiléen. C'est donc le cas des
machines électriques tournantes mais également des roues de voiture. Si
le système **n'est pas équilibré dynamiquement, cela va générer des
vibrations** dans l'ensemble du mécanisme, donc du bruit et
éventuellement une usure plus rapide des organes de guidage en rotation.

Un solide en rotation est **équilibré dynamiquement** si :

-   Son **centre d'inertie est situé sur l'axe de rotation**;

-   Les produits d'inertie qui « contiennent » la variable correspondant
    à l'axe sont nuls (ex: D et E doivent être nuls pour un solide en
    rotation autour de l'axe z) **l'axe de rotation du solide doit être
    un axe principal d'inertie**.

## Le théorème de l'énergie cinétique Galiléenne (ou énergie-puissance)

### Introduction

Lors de l'étude d'un mécanisme en mouvement, on peut, à l'aide de la
méthode énergétique, déterminer une équation scalaire liant les efforts
extérieurs aux paramètres de mouvement et à leurs dérivées.

Cette approche « globale » sera particulièrement adaptée pour l'étude
d'un :

\- **mécanisme à un seul degré de mobilité** afin d'obtenir la relation
entre les efforts extérieurs et le paramètre pilote du mouvement
(exemple : détermination du couple moteur)

\- **mécanisme de transformation de mouvement** afin de déterminer
rapidement l'amplification ou la réduction entre l'effort demandé par le
récepteur et celui fourni par le moteur : « loi entrée/sortie dynamique
»

### Théorème de l'énergie cinétique Galiléenne (ou théorème énergie puissance)

Soit E un ensemble de solides S~1~, S~2~ \... S~n~ en mouvement par
rapport à un repère galiléen Rg, on montre que le théorème de l'énergie
cinétique se traduit de la façon suivante :

$$\left( \frac{{dEc}_{E/Rg}}{dt} \right)_{Rg} = P_{\overline{E} \rightarrow E/Rg} + \sum_{i \neq j}^{1\ à\ n}P_{S_{i} \leftrightarrow S_{i}}$$

La dérivée par rapport au temps, de l'énergie cinétique galiléenne d'un
ensemble de solides E dans son mouvement par rapport à un repère
galiléen Rg est égale à la puissance développée par les actions
mécaniques extérieures à E dans son mouvement par rapport au repère
galiléen Rg et des puissances des actions mutuelles entre chaque solide
de E.

On peut aussi le retenir en version « simplifiée » :
$\left( \frac{{dEc}_{E/Rg}}{dt} \right)_{Rg} = P_{ext} + P_{int}$

E~c~ représente l'énergie cinétique de l'ensemble des solides en
mouvement, P~ext~, la somme des puissances extérieures à l'ensemble
isolé E, et P~int~ la somme des puissances intérieures à l'ensemble
isolé E.

L'ensemble isolé E, est toujours l'ensemble des solides en mouvement
(tous les solides sauf le bâti). Il n'y a pas de réflexion à avoir comme
lors du PFD.

### Démarche de résolution

1.  Représenter le système (graphe de structure);

2.  Isoler l'ensemble des solides en mouvement (tous sauf le bâti) ;

3.  Identifier les mouvements de chaque solide par rapport au repère
    galiléen (ou par rapport au bâti, car le repère galiléen est supposé
    être associé au bâti)

4.  Déterminer les énergies cinétiques en regardant bien les données et
    hypothèses (masse ou inertie négligées, etc...) ;

5.  Déterminer, si nécessaire, le moment d'inertie équivalent J~eq~ (ou
    la masse équivalente M~eq~), en exprimant toutes les vitesses en
    fonction de la vitesse angulaire de rotation du moteur (ou de la
    vitesse de translation).

6.  Identifier les efforts extérieurs à E et calculer les puissances
    développées par ces efforts en faisant très attention aux hypothèses
    de liaison parfaite (pas de frottement) et de transmission parfaite
    (rendement de transmission unitaire);

7.  Appliquer le TEC et déterminer l'équation de mouvement.

[Exemple :]{.underline}

Sur le graphe de structure suivant, on souhaite isoler l'ensemble
E=1+2+3 afin de déterminer le couple moteur en fonction des données de
masses, dimensions et d'inerties.

![](11-Actions Mécaniques/Cours/pandoc/media/image300.wmf){width="0.8281255468066492in"
height="0.4843744531933508in"}![](11-Actions Mécaniques/Cours/pandoc/media/image301.wmf){width="0.5675667104111985in"
height="0.3742650918635171in"}![](11-Actions Mécaniques/Cours/pandoc/media/image302.wmf){width="0.8072911198600174in"
height="0.4843755468066492in"}![](11-Actions Mécaniques/Cours/pandoc/media/image303.wmf){width="0.8506944444444444in"
height="0.4843744531933508in"}![](11-Actions Mécaniques/Cours/pandoc/media/image304.wmf){width="0.5711811023622048in"
height="0.4722222222222222in"}![](11-Actions Mécaniques/Cours/pandoc/media/image305.wmf){width="0.5711811023622048in"
height="0.4722222222222222in"}![](11-Actions Mécaniques/Cours/pandoc/media/image306.wmf){width="0.8038199912510936in"
height="0.4375in"}

-   L'énergie cinétique de l'ensemble se détermine en faisant la somme
    de l'énergie cinétique de chacun des solides

$$E_{c}(E/R_{g}) = E_{c}(1/R_{g}) + E_{c}(2/R_{g}) + E_{c}(3/R_{g})$$

-   Le mouvement de 1/0 est un mouvement de rotation (liaison pivot
    directe), le mouvement de 2/0 est un mouvement quelconque (pas de
    liaison directe), le mouvement de 3/0 est un mouvement de rotation
    (liaison pivot directe).

Pour la suite il faut savoir comment calculer l'énergie cinétique d'un
solide dans son mouvement par rapport au repère Galiléen.

![](11-Actions Mécaniques/Cours/pandoc/media/image10.png){width="4.1875in"
height="1.8909722222222223in"}

### Torseur cinétique

##### Notion de cinétique {#notion-de-cinétique .unnumbered}

La cinétique, théorie partielle de la mécanique, fait appel aux notions
de longueur, de temps, et de masse. Elle est le prolongement de la
cinématique puisque son élaboration ne demande que l'introduction d'une
nouvelle notion : celle de masse. La cinétique est utile pour l'étude et
les applications du Principe Fondamental de la Mécanique (aussi appelé
Principe Fondamental de la Dynamique) et pour la détermination de
l'énergie cinétique. Dans ce cours la masse sera invariante dans le
temps (on dit alors masse conservative).

##### Le torseur cinétique {#le-torseur-cinétique .unnumbered}

On l'appelle aussi *torseur des quantités de mouvement*.

Le torseur cinétique
$\left\{ C_{S/R} \right\}_{A} =_{A}^{}\begin{Bmatrix}
\overrightarrow{p_{S/R}}\ \ \  \\
\overrightarrow{\sigma_{A,\ S/R}}
\end{Bmatrix}$ a pour composantes :

-   $\overrightarrow{p_{S/R}}$ ou $\overrightarrow{R_{c\ S/R}}$, la
    quantité de mouvement,
    ![](11-Actions Mécaniques/Cours/pandoc/media/image315.wmf)

-   $\overrightarrow{\sigma_{A,\ S/R}}$ , le moment cinétique en un
    point A, ![](11-Actions Mécaniques/Cours/pandoc/media/image316.wmf)

$$\left\{ C_{S/R} \right\}_{A} =_{A}^{}\begin{Bmatrix}
\overrightarrow{p_{M/R}} = m.\overrightarrow{V_{G/R}}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\overrightarrow{\sigma_{A,\ S/R}} = m\overrightarrow{AG} \land \overrightarrow{V_{A/R}} + {\lbrack I}_{A(S)}\rbrack.\overrightarrow{\Omega_{S/R}}
\end{Bmatrix}$$

Où G représente le centre d'inertie du solide S.

Moyen mnémotechnique pour le moment : MAGVARIO

##### Cas particuliers {#cas-particuliers .unnumbered}

-   A est fixe dans R :
    $\overrightarrow{\sigma_{A,\ S/R}} = {\overrightarrow{\sigma}}_{A}(S/R) = \left\lbrack I_{A}(S) \right\rbrack.{\overrightarrow{\Omega}}_{S/R}$

-   A est confondu avec le centre d'inertie
    G :$\ \overrightarrow{\sigma_{G,\ S/R}} = {\overrightarrow{\sigma}}_{G}(S/R) = \left\lbrack I_{G}(S) \right\rbrack.{\overrightarrow{\Omega}}_{S/R}$

##### Changement de point du moment cinétique (théorème de Koenig) {#changement-de-point-du-moment-cinétique-théorème-de-koenig .unnumbered}

$${\overrightarrow{\sigma}}_{B}(S/R) = {\overrightarrow{\sigma}}_{A}(S/R) + \overrightarrow{BA} \land \underset{m.\overrightarrow{V}(G/R)}{\overset{{\overrightarrow{R}}_{c}(S/R)}{︸}}$$

##### Torseur cinétique d'un ensemble de solides $\mathbf{\Sigma}$ {#torseur-cinétique-dun-ensemble-de-solides-mathbfsigma .unnumbered}

Si on décompose le système de solides $\Sigma$ en solides élémentaires
$S_{i}$ :

$$\left\{ C_{\Sigma/R} \right\} = \sum_{i}^{}\left\{ C_{S_{i}/R} \right\}$$

+-------+--------------------------------------------------------------+
| >     | **Bielle-manivelle**                                         |
| ![](1 |                                                              |
| 1-Act | Sur cet exercice on reconnaitra une modélisation d'un        |
| ions  | système bielle manivelle en vue de calculs dynamiques. Les   |
| Mécan | solides 1, 2 et 3 sont considérés comme étant des barres     |
| iques | homogènes de longueur L, de masse m et ont pour centres de   |
| /Cour | gravité respectifs les points G~1~, G~2~ et G~3~.            |
| s/pan |                                                              |
| doc/m | ![](11-Actions Mécaniques/                                   |
| edia/ | Cours/pandoc/media/image317.png){width="4.147771216097988in" |
| image | height="1.5127515310586177in"}                               |
| 8.png |                                                              |
| ){wid | **Déterminer le torseur cinétique de l'ensemble E=1+2+3 au   |
| th="0 | point O dans son mouvement par rapport au repère 0.**        |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

##### Conservation de la quantité de mouvement {#conservation-de-la-quantité-de-mouvement .unnumbered}

Dans un **référentiel galiléen**, la **quantité de mouvement totale**
**d'un système isolé** ou pseudo-isolé est une quantité **conservée**.

+-------+--------------------------------------------------------------+
| >     | **Trains**                                                   |
| ![](1 |                                                              |
| 1-Act | Une locomotive de 90 t vient percuter, en roues libres, un   |
| ions  | ensemble de wagons immobiles de 135 t. Au moment du contact, |
| Mécan | la locomotive roule à 18 km/h.                               |
| iques |                                                              |
| /Cour | ![](11-Actions Mécaniques/                                   |
| s/pan | Cours/pandoc/media/image318.png){width="5.405555555555556in" |
| doc/m | height="0.6604166666666667in"}                               |
| edia/ |                                                              |
| image | **Déterminer la vitesse prise par l'ensemble après           |
| 8.png | l'accrochage.**                                              |
| ){wid |                                                              |
| th="0 |                                                              |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Déterminer l'énergie cinétique d'un solide

##### Définition {#définition-1 .unnumbered}

Soit un solide S de masse m en mouvement par rapport à un repère R. Le
mouvement est défini par :

-   le torseur cinématique au point A du solide S :
    $\left\{ V_{S/R} \right\}_{A} = \begin{Bmatrix}
    \overrightarrow{\Omega_{S/R}}\ \  \\
    \overrightarrow{V_{A,\ S/R}}
    \end{Bmatrix}$

-   le torseur cinétique au point A du solide S :
    $\left\{ C_{S/R} \right\}_{A} = \begin{Bmatrix}
    \overrightarrow{p_{S/R}}\ \ \  \\
    \overrightarrow{\sigma_{A,\ S/R}}
    \end{Bmatrix}$

Le double de l'énergie cinétique apparaît comme le comoment de ces deux
torseurs :

$$2.{Ec}_{S/R} = \left\{ V_{S/R} \right\}_{A}{\bigotimes\left\{ C_{S/R} \right\}}_{A}$$

$$2.{Ec}_{S/R} = \overrightarrow{\Omega_{S/R}}.\overrightarrow{\sigma_{A,\ S/R}} + \overrightarrow{V_{A,\ S/R}}.\overrightarrow{p_{S/R}}$$

*[Remarque :]{.underline}* la valeur du comoment (produit scalaire des
torseurs, que l'on note aussi $\bigotimes$) est indépendants du point de
réduction des torseurs, les deux torseurs devant être écrits au même
point.

[Remarque]{.underline} : L'énergie cinétique E~c~ (parfois notée aussi T
ou W) se conserve.

[Démonstration :]{.underline}

En passant par la vitesse du point A appartenant au même solide on a :

$$2E_{c}(S/R) = \int_{S}^{}{\underset{\overrightarrow{V}(M/R)}{\overset{\left( \overrightarrow{V}(A/R) + \overrightarrow{MA} \land {\overrightarrow{\Omega}}_{S/R} \right)}{︸}}.\overrightarrow{V}(M/R).dm}$$

$$2E_{c}(S/R) = \int_{S}^{}{\underset{\overrightarrow{V}(M/R)}{\overset{\left( \overrightarrow{V}(A/R) + {\overrightarrow{\Omega}}_{S/R} \land \overrightarrow{AM} \right)}{︸}}.\overrightarrow{V}(M/R).dm}$$

$$2E_{c}(S/R) = \overrightarrow{V}(A/R).\underset{{\overrightarrow{R}}_{c}(S/R)}{\overset{m.\overrightarrow{V}(G/R)}{︸}} + {\overrightarrow{\Omega}}_{S/R}.{\overrightarrow{\sigma}}_{A}(S/R)$$

$$2.E_{c}(S/R) = \left\{ V_{S/R} \right\} \otimes \left\{ C_{S/R} \right\}$$

##### Cas particuliers {#cas-particuliers-1 .unnumbered}

La plupart du temps, les mouvements sont des mouvements élémentaires
(rotation ou translation). Dans ces cas, le calcul de l'énergie
cinétique d'un solide peut être considérablement simplifié. Ces
résultats sont donc à connaitre parfaitement.

Solide S de moment d'inertie J en rotation autour d'un axe fixe :
$E_{c}(S/R) = \frac{1}{2}J{\Omega^{2}}_{S/R}$

Solide S de masse m en translation / Rg :
$E_{c}(S/R) = \frac{1}{2}m{V^{2}}_{G,S/R_{0}}$

+-------+--------------------------------------------------------------+
| >     | ![](11-Actions Mécaniques/C                                  |
| ![](1 | ours/pandoc/media/image319.png){width="3.3181824146981627in" |
| 1-Act | height="3.480042650918635in"}**Patinage**                    |
| ions  |                                                              |
| Mécan |                                                              |
| iques |                                                              |
| /Cour |                                                              |
| s/pan |                                                              |
| doc/m |                                                              |
| edia/ |                                                              |
| image |                                                              |
| 8.png |                                                              |
| ){wid |                                                              |
| th="0 |                                                              |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

##### Energie cinétique d'un ensemble de solides $\mathbf{\Sigma}$ {#energie-cinétique-dun-ensemble-de-solides-mathbfsigma .unnumbered}

Si on décompose le système de solides $\Sigma$ en solides élémentaires
$S_{i}$ :

$${E_{c}}_{\Sigma/R} = \sum_{i}^{}{E_{c}}_{S_{i}/R}$$

### Détermination du moment d'inertie équivalent et de la masse équivalente

On appelle **moment d'inertie équivalent**
$\mathbf{J}_{\mathbf{eq}}\mathbf{\ }$**ou « inertie équivalente »**
ramenée au solide S1, d'une chaîne de solide, le moment d'inertie d'un
solide qui tournant à la même vitesse que cet arbre, engendrerait la
même énergie cinétique que celle de l'ensemble des solides de la chaîne.
Il se déterminer à partir de l'énergie cinétique totale.

$$E_{c}(\Sigma/R) = \frac{1}{2}J_{eq}{\Omega_{m}}^{2}$$

![](11-Actions Mécaniques/Cours/pandoc/media/image320.jpeg){width="4.722222222222222in"
height="2.484027777777778in"}

On appelle **masse équivalente** ramenée au solide S1, d'une chaîne de
solides » , la masse d'un solide qui translatant à la même vitesse que
le solide S1, engendrerait la même énergie cinétique que celle de
l'ensemble des solides de la chaîne.

$$E_{c}(\Sigma/R) = \frac{1}{2}M_{eq}V^{2}$$

![](11-Actions Mécaniques/Cours/pandoc/media/image10.png){width="4.1875in"
height="1.8909722222222223in"}

+-------+--------------------------------------------------------------+
| >     | **Elévateur**                                                |
| ![](1 |                                                              |
| 1-Act | Un élévateur est constitué d'un socle (1), d'un coulisseau   |
| ions  | (3) et d'un mécanisme d'entraînement par la vis (2), l'écrou |
| Mécan | en A est solidaire du coulisseau. La position du coulisseau  |
| iques | est repérée par O~1~A = z et la position angulaire de la vis |
| /Cour | par l'angle $\varphi$. Toutes les liaisons sont sans         |
| s/pan | frottement. Le mécanisme évolue dans le plan vertical        |
| doc/m | $\left(                                                      |
| edia/ |  \text{O}_{\text{1}}\text{, }\overrightarrow{\text{y}_{\text |
| image | {1}}}\text{, }\overrightarrow{\text{z}_{\text{1}}} \right)$. |
| 8.png |                                                              |
| ){wid | *[Vis (2) :]{.underline}* masse m~2~ et                      |
| th="0 | $\te                                                         |
| .6262 | xt{I}_{\text{O}_{\text{1}}\text{(2)}}\text{=}\begin{bmatrix} |
| 69685 | \text{A}_{\text{2}} & \text{0} & \text{0} \\                 |
| 03937 | \text{0} & \text{A}_{\text{2}} & \text{0} \\                 |
| 01in" | \text{0} & \text{0} & \text{C}_{\text{2}}                    |
| >     | \end{bma                                                     |
| heigh | trix}_{\left( \text{O}_{\text{1}}\text{, }\overrightarrow{\t |
| t="0. | ext{x}_{\text{2}}}\text{,  }\overrightarrow{\text{y}_{\text{ |
| 65083 | 2}}}\text{, }\overrightarrow{\text{z}_{\text{2}}} \right)}$, |
| 33333 | son centre d'inertie est en G~2~.                            |
| 33333 |                                                              |
| 4in"} | *[Coulisseau (3) :]{.underline}* masse m~3~ et               |
|       | $\text{I}_{\text{A(3)}}\text{=}\begin{bmatrix}               |
|       | \text{A}_{\text{3}} & \text{0} & \text{0} \\                 |
|       | \text{0} & \text{B}_{\text{3}} & \text{0} \\                 |
|       | \text{0} & \text{0} & \text{C}_{\text{3}}                    |
|       | \end{bmatrix}_{\left( \text{A, }\overrightarrow{\t           |
|       | ext{x}_{\text{3}}}\text{,  }\overrightarrow{\text{y}_{\text{ |
|       | 3}}}\text{, }\overrightarrow{\text{z}_{\text{3}}} \right)}$, |
|       | son centre d'inertie est en A.                               |
|       |                                                              |
|       | ![image_elevateur.jpg](11-Actions Mécaniques/Co              |
|       | urs/pandoc/media/image321.jpeg){width="3.6084109798775152in" |
|       | height="2.8545614610673664in"}                               |
|       |                                                              |
|       | **Détermination de la relation entre le couple moteur et     |
|       | l'accélération**                                             |
|       |                                                              |
|       | La transformation de mouvement par vis-écrou est telle que : |
|       | $\text{z=-}\frac{\text{p.}\varphi}{\text{2.π}}$ où p est le  |
|       | pas de la vis.                                               |
|       |                                                              |
|       | **Donner la forme du théorème de l'énergie cinétique         |
|       | appliqué à l'ensemble mobile (2) + (3).**                    |
|       |                                                              |
|       | **Déterminer les expressions des énergies cinétiques**       |
|       | $\mathbf{E}_{\mathbf{c\ 2/1}}$ **et**                        |
|       | $\mathbf{E}_{\mathbf{c\ "/1}}$ **en fonction des             |
|       | caractéristiques inertielles des solides (2) et (3). En      |
|       | déduire l'énergie cinétique de l'ensemble mobile en          |
|       | fonction, en particulier, de la variable**                   |
|       | $\mathbf{\varphi}$**.**                                      |
|       |                                                              |
|       | **Donner l'expression du moment d'inertie**                  |
|       | $\mathbf{J}_{\mathbf{eq}}$ **de l'ensemble mobile ramenée à  |
|       | l'axe moteur**                                               |
|       | $\left( \text{O}_{\text{1}                                   |
|       | }\text{, }\overrightarrow{\text{z}_{\text{1}}} \right)$**.** |
|       |                                                              |
|       | **Donner l'expression de la masse équivalente**              |
|       | $\mathbf{M}_{\mathbf{eq}}$ **de l'ensemble mobile ramené au  |
|       | coulisseau.**                                                |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Notion de puissance mécanique

Les puissances extérieures sont celles « extérieures » à l'ensemble
isolé :

> $$P_{\overline{\Sigma} \rightarrow \Sigma/R} = P_{Cm \rightarrow 1/R} + P_{0 \rightarrow 1/R} + P_{0 \rightarrow 3/R} + P_{g \rightarrow 1/R} + P_{g \rightarrow 2/R} + P_{g \rightarrow 3/R}$$

Les puissances intérieures sont celles qui sont « intérieures » à
l'ensemble isolé.

$$\sum_{i,j = 1}^{n}P_{S_{i} \leftrightarrow S_{j}} = P_{1 \leftrightarrow 2} + P_{2 \leftrightarrow 3}$$

Dans le cas **des puissances, il faut bien faire attention aux
signes** ! Elles sont comptées **positives lorsqu'elles sont motrices ou
entrainantes** (moteur,...) et **négatives lorsqu'elles sont résistantes
(frottements,....).**

### Puissance extérieure

Le mouvement d'un solide S indéformable par rapport au repère $R$ est
connu et défini par le torseur cinématique :
$\left\{ V_{S/R} \right\}_{A} = \begin{Bmatrix}
\overrightarrow{\Omega_{S/R}}\ \  \\
\overrightarrow{V_{A,\ S/R}}
\end{Bmatrix}$

Si le torseur associé à l'action mécanique (d'origine quelconque) du
milieu j sur le solide S est noté
$\left\{ \tau_{j \rightarrow S} \right\}_{A} = \begin{Bmatrix}
\overrightarrow{R_{j \rightarrow S}}\ \ \ \  \\
\overrightarrow{M_{A,\ j \rightarrow S}}
\end{Bmatrix}$

![600px-Panneau_attention](11-Actions Mécaniques/Cours/pandoc/media/image38.png){width="0.375in"
height="0.3173611111111111in"}on montre que la puissance développé par
le torseur $
\left\{ \tau_{S \rightarrow R} \right\}_{A}\ $dans le repère $R$
est :$\ $

$$P_{j \rightarrow S/R} = \left\{ V_{S/R} \right\}_{A}\bigotimes\left\{ \tau_{j \rightarrow S} \right\}_{A}$$

$$P_{j \rightarrow S/R} = \overrightarrow{\Omega_{S/R}}.\overrightarrow{M_{A,\ j \rightarrow S}} + \overrightarrow{V_{A,\ S/R}}.\overrightarrow{R_{j \rightarrow S}}$$

### Puissance développée par les actions mutuelles entre deux solides (P~int~)

On dit aussi puissance des inter-efforts.

Considérons deux solides [1]{.underline} et [2]{.underline} en mouvement
par rapport à un repère R. La puissance développée par les actions
mutuelles entre les solides 1 et 2 pour une loi physique quelconque est
par définition :

$$P_{1 \rightarrow 2/R} + P_{2 \rightarrow 1/R} = P_{1 \leftrightarrow 2/R}$$

On démontre en utilisant le théorème des actions mutuelles que :

![600px-Panneau_attention](11-Actions Mécaniques/Cours/pandoc/media/image38.png){width="0.375in"
height="0.3173611111111111in"}

$$P_{1 \leftrightarrow 2} = \left\{ V_{2/1} \right\}\bigotimes\left\{ \tau_{1 \rightarrow 2} \right\}$$

Cette relation montre que la puissance développée par un torseur
d'inter-effort **est indépendante** du repère de référence R, seul
intervient le mouvement de 1/2. On pourra donc noter plus simplement
$P_{1 \leftrightarrow 2}$ sans faire mention du repère.

[Remarques importantes :]{.underline}

-   Elle n'existe pas s'il n'y a qu'un solide et elle est indépendante
    du repère R

-   Elle est **nulle dans le cas de liaisons parfaites et dans le cas de
    transmission parfaite (rendement unitaire). A VERIFIER TOUT LE
    TEMPS**

-   Elle existe lorsqu'il y a des **frottements**, un **ressort** ou un
    **moteur** entre les deux solides ...

-   Pour déterminer le torseur cinématique, on peut utiliser la
    composition des vitesses.

> $$\left\{ V_{2/1} \right\} = \left\{ V_{2/0} \right\} + \left\{ V_{0/1} \right\} = \left\{ V_{2/0} \right\} - \left\{ V_{1/0} \right\}$$

***Cas particuliers (A CONNAITRE) :***

Liaisons parfaites : Une liaison entre deux solides [1]{.underline} et
[2]{.underline} est dite énergétiquement parfaite si :
$P_{1 \leftrightarrow 2} = 0$

Puissance développée par une machine électrique :
$P_{m} = C_{u}\Omega_{m}$

Puissance développée par un glisseur (pesanteur, ...) :
$P = \overrightarrow{F} \cdot \overrightarrow{V}$

Solide fixe par rapport au repère R : $P = 0\ $

+-------+--------------------------------------------------------------+
| >     | ![image_elevateur.jpg](11-Actions Mécaniques/Co              |
| ![](1 | urs/pandoc/media/image322.jpeg){width="3.3152777777777778in" |
| 1-Act | height="2.622916666666667in"}**Elévateur**                   |
| ions  |                                                              |
| Mécan | Un couple moteur $C_{m}$ s'exerce en O~1~ sur la vis (2).    |
| iques |                                                              |
| /Cour | **Déterminer les expressions des diverses puissances         |
| s/pan | extérieure(s) développées par les efforts s'exerçant sur (2) |
| doc/m | et (3).**                                                    |
| edia/ |                                                              |
| image | **Déterminer la valeur des puissances intérieures au système |
| 8.png | isolé (faîte une hypothèse si nécessaire).**                 |
| ){wid |                                                              |
| th="0 | **Déduire de ce qui précède la relation entre le couple**    |
| .6262 | $\mathbf{C}_{\mathbf{m}}\mathbf{\ }$**et l'accélération**    |
| 69685 | $\mathbf{\Gamma}_{\mathbf{0}}$ **du coulisseau.**            |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

##### Transmission non parfaite {#transmission-non-parfaite .unnumbered}

Dans le cas où la transmission de la chaîne cinématique n'est pas
parfaite, il existe des pertes, et donc une puissance de pertes
(négative par convention) qui doit être prise en compte. Cependant, il
n'est pas question de calculer un comoment, car un rendement nous est en
général donné pour aider à quantifier ces pertes.

Parfois, la seule information sur les puissances est le rendement
(exemple rendement d'une transmission). La puissance perdue
(inter-efforts ou extérieure) peut alors être calculée de la manière
suivante à partir du rendement de la transmission $\eta$ et de la
puissance en entrée de la transmission $P_{e}$.

$P_{perdue} = (1 - \eta)P_{e}$ , si on considère qu'elle sera soustraite
au bilan de puissances.

Ou alors à partir d'un couple de frottement :
$P_{perdue} = C_{f}\omega_{e}$

Dans tous les cas, le fait d'avoir des pertes dans la transmission, se
traduit par le fait que la puissance disponible est inférieure. Dans le
cas d'un moteur on utilisera comme puissance utile moteur
$\eta C_{m}\Omega_{m}$ au lieu de $C_{m}\Omega_{m}$, $\eta$ représentant
le rendement global de la chaine de transmission du moteur.

+-------+--------------------------------------------------------------+
| >     | **Elévateur**                                                |
| ![](1 |                                                              |
| 1-Act | **Déterminer l'expression du couple moteur**                 |
| ions  | $\mathbf{C}_{\mathbf{m}}$ **si le rendement global de la     |
| Mécan | chaine cinématique**                                         |
| iques | $\mathbf{\eta}_{\mathbf{g}}\mathbf{= 0,8}$**.**              |
| /Cour |                                                              |
| s/pan |                                                              |
| doc/m |                                                              |
| edia/ |                                                              |
| image |                                                              |
| 8.png |                                                              |
| ){wid |                                                              |
| th="0 |                                                              |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

### Travail, énergie potentielle et puissance

On appelle ***travail d'une action mécanique*** entre l'instant initial
***t~i~*** et l'instant final ***t~f~*** la ***quantité W*** obtenue en
sommant la puissance entre ces deux instants
:$W = \int_{t_{i}}^{t_{f}}{P(t).dt}$

Ce ***travail*** s'exprime en ***Joules** (=Watt.s)* et en général,
dépend de la façon dont la puissance évolue entre les deux instants
***t~i~*** et ***t~f~*** et pas seulement des valeurs en ces deux
instants. Il existe un certain nombre de cas particuliers pour lesquels
le travail ne dépend du chemin suivi mais que des valeurs finales et
initiales d'une quantité appelée ***énergie potentielle U.*** Dans ce
cas-là le travail se calcul par :
$W = - \left( U(t_{f}) - U(t_{i}) \right)$

La ***puissance*** s'obtient alors par ***dérivation de l'énergie
potentielle :***$P = - \frac{dU}{dt}$

***Exemple :*** énergie potentielle de pesanteur

Soit un solide **S**, de masse **m**, de centre de gravité **G**, en
mouvement dans un référentiel **R** d'origine **O**.

La puissance développée par l'action de la pesanteur dans le mouvement
de S par rapport à R est :
$P = m.\overrightarrow{g}.\overrightarrow{V}(G/R)$

On a donc : $P = m.\overrightarrow{g}.\frac{d(\overrightarrow{OG})}{dt}$
(avec O l'origine du repère R)

$P = - \frac{d}{dt}\left\lbrack - m.\overrightarrow{g}.\overrightarrow{OG} \right\rbrack$,
on en déduit
$U_{pesanteur} = - m.\overrightarrow{g}.\overrightarrow{OG}$

![](11-Actions Mécaniques/Cours/pandoc/media/image323.jpeg){width="1.7222222222222223in"
height="1.3173611111111112in"}

##### Energie potentielle élastique {#energie-potentielle-élastique .unnumbered}

Soit un ressort, de raideur **k**, de longueur à vide **l~0~** que l'on
étire à une extrémité **A** jusqu'à une longueur **l**.

La ***force de rappel élastique*** vaut :

$$\overrightarrow{F} = - k(l - l_{0}).\overrightarrow{i}$$

$\overrightarrow{i}$ *est la direction suivant laquelle le ressort
s'allonge*

La puissance développée par cet effort est donc :

$$P = \overrightarrow{F}.\overrightarrow{V}(A/R) = - k(l - l_{0}).\overrightarrow{i}.\frac{dl}{dt}.\overrightarrow{i} = - \frac{k}{2}\frac{d(l - l_{0})^{2}}{dt}$$

Ce qui nous donne pour l'énergie potentielle :
$U_{ressort} = \frac{k}{2}(l - l_{0})^{2}$

## Principe Fondamental de la Dynamique

Le théorème de l'énergie cinétique permet d'avoir une équation scalaire
rapidement, et il est préférable de l'utiliser quand on cherche à
calculer un couple moteur. Par contre, dès qu'on cherche à dimensionner
un mécanisme en termes d'efforts dans les liaisons, il faudra appliquer
le PFD qui permet d'avoir 6 équations scalaires.

### Enoncé du PFD

Ce principe est également appelé ***principe fondamental de la
mécanique***.

A chaque instant t et pour tout ensemble isolé E le torseur associé aux
actions mécaniques extérieures sur E (noté
$\left\{ \tau_{\overline{E} \rightarrow E} \right\}$) est égal au
torseur dynamique de E (noté $\left\{ D_{E/R} \right\}$) calculé par
rapport à un repère que l'on supposera galiléen (fixe à l'échelle de ce
qu'on étudie) :

$$\left\{ \tau_{\overline{E} \rightarrow E} \right\} = \left\{ D_{E/R} \right\}$$

La démarche pour déterminer
$\left\{ \tau_{\overline{E} \rightarrow E} \right\}$ est exactement la
même que pour l'équilibre. L'équilibre est un cas particulier du PFD,
pour lequel le torseur dynamique est le torseur nul.

La seule difficulté est alors d'arriver à déterminer les composantes du
torseur dynamique.

Le principe fondamental de la mécanique, sous forme torsorielle,
entraîne deux équations vectorielles qui sont les théorèmes de la
mécanique pour un système S de masse m et de centre d'inertie G :

-   Théorème de la résultante dynamique :
    ${\overrightarrow{R}}_{\overline{A} \rightarrow A} = m.\overrightarrow{A_{G/R}}$

-   Théorème du moment dynamique :
    ${\overrightarrow{M}}_{A,\ \overline{A} \rightarrow A} = \overrightarrow{\delta_{A,\ S/R}}$

### Torseur Dynamique

Le torseur dynamique caractérise la **quantité** **d'accélération** d'un
solide S par rapport à un repère R. Le **torseur dynamique** pour un
solide S dans **son mouvement par rapport au repère R** s'exprime en un
**point A quelconque**, par :

$$\left\{ \tau_{\overline{S} \rightarrow S} \right\} = \left\{ D_{S/R} \right\}$$

$\left\{ D_{S/R} \right\} = \begin{Bmatrix}
m.\overrightarrow{A}(G_{S}/R) \\
{\overrightarrow{\delta}}_{A}(S/R)
\end{Bmatrix}_{A}$ ,
$\left\{ \tau_{\overline{S} \rightarrow S} \right\} = \begin{Bmatrix}
{\overrightarrow{R}}_{\overline{S} \rightarrow S} \\
{\overrightarrow{M}}_{A,\overline{S} \rightarrow S}
\end{Bmatrix}_{A}$

$${\overrightarrow{\delta}}_{A}(S/R) = m.\overrightarrow{V}(A/R) \land \overrightarrow{V}(G/R) + \frac{d}{dt}\left\lbrack {\overrightarrow{\sigma}}_{A}(S/R) \right\rbrack_{R}$$

Remarque :
${\overrightarrow{R}}_{d}(S/R) = \frac{d}{dt}\left\lbrack {\overrightarrow{R}}_{c}(S/R) \right\rbrack_{R}$ :
la résultante dynamique est la dérivée de la résultante cinétique.

Cas particuliers :

-   A est un point fixe dans R :
    ${\overrightarrow{\delta}}_{A}(S/R) = \frac{d}{dt}\left\lbrack {\overrightarrow{\sigma}}_{A}(S/R) \right\rbrack_{R}$

-   A est confondu avec le centre d'inertie
    G :${\overrightarrow{\delta}}_{G}(S/R) = \frac{d}{dt}\left\lbrack {\overrightarrow{\sigma}}_{G}(S/R) \right\rbrack_{R}$

*Pour le **calcul du moment dynamique**, nous aurons à faire en général
à deux cas :*

***1 →** Les **données de l'énoncé** du problème permettent d'exprimer
facilement la matrice d'inertie du solide S au point A.*

***2 →** Les **données de l'énoncé** du problème permettent d'exprimer
facilement la matrice d'inertie du solide S au centre d'inertie G.*

*[Différents chemins sont possibles :]{.underline}*

![](11-Actions Mécaniques/Cours/pandoc/media/image324.jpeg){width="3.115972222222222in"
height="2.0930555555555554in"}![](11-Actions Mécaniques/Cours/pandoc/media/image325.jpeg){width="2.941666666666667in"
height="2.267361111111111in"}

##### Torseur dynamique d'un ensemble de solides $\mathbf{\Sigma}$ {#torseur-dynamique-dun-ensemble-de-solides-mathbfsigma .unnumbered}

Si on décompose le système de solides $\Sigma$ en solides élémentaires
$S_{i}$ :

$$\left\{ D_{\Sigma/R} \right\} = \sum_{i}^{}\left\{ D_{S_{i}/R} \right\}$$

### Cas simplifiés

Lorsque le mouvement d'un solide (ou d'un ensemble de solide) par
rapport à un repère Galiléen est « élémentaire », il existe une
simplification des formules précédentes.

Translation rectiligne : $\sum_{}^{}F = ma$

Rotation : $J_{eq}\frac{d\Omega}{dt} = \sum_{}^{}C$

![](11-Actions Mécaniques/Cours/pandoc/media/image10.png){width="4.1875in"
height="1.8909722222222223in"}

+-------+--------------------------------------------------------------+
| >     | **Treuil**                                                   |
| ![](1 |                                                              |
| 1-Act | Un treuil entraîné par un motoréducteur électrique permet de |
| ions  | soulever une masse M.                                        |
| Mécan |                                                              |
| iques | Le rendement du réducteur est η~r~ = 0,8 et le rapport de    |
| /Cour | réduction est égal à 20. Le rayon de la poulie motrice est   |
| s/pan | noté R~p~. Le moment d'inertie de l'ensemble mobile ramené   |
| doc/m | sur l'arbre de rotation est J~eq~ = 1,6 kg.m².               |
| edia/ |                                                              |
| image | **Calculer le couple développé par le moteur**               |
| 8.png | $\mathbf{C}_{\mathbf{m}}$ **pour une accélération de la      |
| ){wid | masse** $\mathbf{a}_{\mathbf{Z}}$ **= 1,2 m/s²**             |
| th="0 |                                                              |
| .6262 |                                                              |
| 69685 |                                                              |
| 03937 |                                                              |
| 01in" |                                                              |
| >     |                                                              |
| heigh |                                                              |
| t="0. |                                                              |
| 65083 |                                                              |
| 33333 |                                                              |
| 33333 |                                                              |
| 4in"} |                                                              |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

+-------+--------------------------------------------------------------+
| >     | **Houlogénérateur SEAREV**                                   |
| ![](1 |                                                              |
| 1-Act | ![](11-Actions Mécaniques/Co                                 |
| ions  | urs/pandoc/media/image326.jpeg){width="3.1166666666666667in" |
| Mécan | height="1.6583333333333334in"}                               |
| iques |                                                              |
| /Cour | Le houlo-générateur est constitué d'un flotteur              |
| s/pan | [1]{.underline} et d'un pendule [2]{.underline} évoluant par |
| doc/m | rapport à la Terre [0]{.underline}. Les deux solides         |
| edia/ | [1]{.underline} et [2]{.underline} sont en liaison pivot     |
| image | d'axe $\left( \text{A,}\overrightarrow{z} \right)$. La       |
| 8.png | génératrice synchrone placée sur l'axe de liaison permet de  |
| ){wid | récupérer une partie de l'énergie des vagues.                |
| th="0 |                                                              |
| .6262 | ***Paramétrage ***                                           |
| 69685 |                                                              |
| 03937 | ![](11-Actions Mécaniques/Co                                 |
| 01in" | urs/pandoc/media/image327.jpeg){width="1.4333333333333333in" |
| >     | height="1.225in"}![](11-Actions Mécaniques/Co                |
| heigh | urs/pandoc/media/image328.jpeg){width="3.0416666666666665in" |
| t="0. | height="1.8083333333333333in"}Le point O origine du repère   |
| 65083 | est fixe par rapport à la terre et à l'altitude nulle. Le    |
| 33333 | vecteur $\overrightarrow{x_{0}}$ a pour direction la         |
| 33333 | verticale, le vecteur                                        |
| 4in"} | ![](11-Actions Mécaniques/Cours/pandoc/media/image329.wmf)a  |
|       | pour direction l'horizontale. La base                        |
|       | $\left( \overrightarr                                        |
|       | ow{x_{1}},\overrightarrow{y_{1}},\overrightarrow{z} \right)$ |
|       | est liée au flotteur 1 et la base                            |
|       | $\left( \overrightarr                                        |
|       | ow{x_{2}},\overrightarrow{y_{2}},\overrightarrow{z} \right)$ |
|       | est liée au pendule 2. Le mouvement de tangage du flotteur   |
|       | induit par la houle se traduit ici par une rotation du       |
|       | flotteur 1 par rapport à la Terre 0 autour de l'axe          |
|       | $\left( \text{O,}\overrightarrow{z} \right)$. Le paramètre   |
|       | angulaire est l'angle                                        |
|       | ![](11-Actions Mécaniques/Cours/pandoc/media/image330.wmf).  |
|       | L'axe de la liaison pivot entre le flotteur 1 et le pendule  |
|       | 2 est l'axe $\left( \text{A,}\overrightarrow{z} \right)$, le |
|       | point A est paramétré par                                    |
|       | $\overrightarrow{\text{OA}}\text{=d}\overrightarrow{x_{1}}$. |
|       | Le centre d'inertie du pendule 2 est le point G tel que      |
|       | $\overrightarrow{\text{AG}}\text{=L}\overrightarrow{x_{2}}$. |
|       |                                                              |
|       | ***Hypothèses***                                             |
|       |                                                              |
|       | -   ![](11-Actions Mécaniques/Co                             |
|       | urs/pandoc/media/image331.jpeg){width="1.5833333333333333in" |
|       |     > height="1.2666666666666666in"}Le flotteur est toujours |
|       |     > à la surface de l'eau.                                 |
|       |                                                              |
|       | -   Le flotteur est toujours incliné suivant la tangente à   |
|       |     > la surface de l'eau. On en déduit une variation de     |
|       |     > $\alpha$ donnée par                                    |
|       |     > $\alpha(t)\text                                        |
|       | {=}\text{α}_{0}\text{cos}\left( \text{ω}\text{.t} \right)$en |
|       |     > ayant noté t le temps, $\omega$ la pulsation de la     |
|       |     > houle et $\alpha_{0}$ l'amplitude angulaire du         |
|       |     > mouvement de tangage du flotteur.                      |
|       |                                                              |
|       | -   Le couple que la génératrice applique sur le pendule 2   |
|       |     > est de la forme                                        |
|       |     > $\o                                                    |
|       | verrightarrow{C_{r}}\text{=}\text{C}_{r}\overrightarrow{z}\t |
|       | ext{=-}\text{λ}\overset{\bullet}{\theta}\overrightarrow{z}$. |
|       |                                                              |
|       | ```{=html}                                                   |
|       | <!-- -->                                                     |
|       | ```                                                          |
|       | -   L'ensemble flottant est soumis à l'action de la          |
|       |     > pesanteur et à l'action de l'eau.                      |
|       |                                                              |
|       | **Caractéristiques d'inertie du flotteur et du pendule**     |
|       |                                                              |
|       | La masse du flotteur 1 est notée $m_{1}$, la masse du        |
|       | pendule 2 est notée $m_{2}$. Le moment d'inertie du pendule  |
|       | 2 autour de l'axe                                            |
|       | $\left( \text{A,}\overrightarrow{z} \right)$ est noté $J$.   |
|       | Les produits d'inertie autour de                             |
|       | $\left( \text{A,}\overrightarrow{z} \right)$ du pendule 2    |
|       | sont nuls.                                                   |
|       |                                                              |
|       | **Déterminer la vitesse du point A du flotteur 1 dans son    |
|       | mouvement par rapport à la Terre 0**                         |
|       | $\overrightarrow{\mathbf{V}_{\text{A,1/0}}}$**.**            |
|       |                                                              |
|       | **Déterminer la vitesse du point G du pendule 2 dans son     |
|       | mouvement par rapport à la Terre 0**                         |
|       | $\overrightarrow{\mathbf{V}_{\text{G,2/0}}}$**.**            |
|       |                                                              |
|       | **Déterminer le moment cinétique du pendule 2 dans son       |
|       | mouvement par rapport à 0 au point A**                       |
|       | $\overrightarrow{\mathbf{\sigma}_{\text{A,2/0}}}$**.**       |
|       |                                                              |
|       | **Déterminer le moment dynamique du pendule 2 dans son       |
|       | mouvement par rapport à 0 au point A**                       |
|       | $\overrightarrow{\mathbf{\delta}_{\text{A,2/0}}}$**.**       |
|       |                                                              |
|       | **Déterminer les moments au point A des actions extérieures  |
|       | s'appliquant sur le pendule 2.**                             |
|       |                                                              |
|       | **Écrire l'équation du mouvement qui régit l'évolution de**  |
|       | $\mathbf{\theta}$**, en fonction de** $\mathbf{\alpha}$ **et |
|       | des constantes du problème.**                                |
+=======+==============================================================+
+-------+--------------------------------------------------------------+

## Sources

Ce cours a été élaboré à l'aide de nombreuses ressources provenant de
différents collègues de l'UPSTI.\

## Exercices du chapitre

![](11-Actions Mécaniques/Cours/pandoc/media/image332.png){width="5.466666666666667in"
height="8.373527996500437in"}

## EQUILIBRE

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**POUSSOIR ET COULISSEAU**

![Image5](11-Actions Mécaniques/Cours/pandoc/media/image334.jpeg){width="4.052083333333333in"
height="2.8180555555555555in"}

On associe les repères :

> \-
> $R_{0}(O,\overset{\rightarrow}{x_{0}},\overset{\rightarrow}{y_{0}},\overset{\rightarrow}{z_{0}})$
> au bâti 0, tel que
> $\overset{\rightarrow}{OB} = b.\overset{\rightarrow}{x_{0}}$
>
> \-
> $R_{1}(O,\overset{\rightarrow}{x_{1}},\overset{\rightarrow}{y_{1}},\overset{\rightarrow}{z_{1}})$
> au poussoir 1, tels que
> $\overset{\rightarrow}{BA} = \lambda.\overset{\rightarrow}{y_{0}}$ et
> $\alpha = (\overset{\rightarrow}{x_{0}},\overset{\rightarrow}{x_{1}})$

Un système non représenté assure le maintien du contact du coulisseau 2
avec le poussoir 1 au point A.

Le poussoir 1 est soumis au couple moteur $C_{m}$ et le piston 2 à
l'action ![](11-Actions Mécaniques/Cours/pandoc/media/image18.wmf) de
pression du fluide.

On suppose le problème plan, les liaisons sans frottement et on néglige
les effets d'inertie et de la pesanteur.

**L'objectif de l'étude est de déterminer une relation entre F et**
$\mathbf{C}_{\mathbf{m}}$ **lorsque le système est en équilibre.**

Q1. Déterminer, en étudiant l'équilibre du système, une relation entre
$C_{m}$ et F.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**CLAPET D'AERATION**

Le dispositif représenté ci-dessous est une commande de l'ouverture d'un
clapet **[4]{.underline}** à partir d'un câble **[5]{.underline}** lié
en A au levier **[2]{.underline}**. Ce levier est relié à une biellette
**[3]{.underline}** qui agit en C sur le clapet **[4]{.underline}**
coudé. Un ressort **[6]{.underline}** doit assurer au volet
**[4]{.underline}** la position d'équilibre
![](11-Actions Mécaniques/Cours/pandoc/media/image335.wmf) sans action
sur le câble **[5]{.underline}**.

![Pim0001](11-Actions Mécaniques/Cours/pandoc/media/image336.jpeg){width="5.833333333333333in"
height="4.317685914260718in"}

[Données :]{.underline}

-   $O_{1}A = a,O_{1}B = b,O_{1}K = h,BC = d,CD = c,DG_{4} = q$

-   $\overrightarrow{CD}\bot\overrightarrow{DE},\alpha = (\overrightarrow{y_{1}},\overrightarrow{y_{2}}),\beta = (\overrightarrow{x_{1}},\overrightarrow{x_{4}}),\delta = (\overrightarrow{y_{1}},\overrightarrow{y_{3}})$

-   $\left\{ T_{6 \rightarrow 2} \right\} = \begin{Bmatrix}
     - F_{R} \cdot \overrightarrow{x_{1}} \\
    \overrightarrow{0}
    \end{Bmatrix}_{K}$

[Hypothèses :]{.underline}

-   On suppose le problème plan.

-   On néglige l'action de la pesanteur sauf sur le volet
    **[4]{.underline}** de masse M~4~ et de centre de
    gravité![](11-Actions Mécaniques/Cours/pandoc/media/image337.wmf).

**L'objectif de l'étude est de déterminer la tension de pose du ressort
F~R~ permettant de maintenir le volet dans la position d'équilibre**
$\beta = 0$ sans action sur le câble.

Q1. Déterminer, en appliquant le PFS aux isolements successifs de votre
choix, une relation entre $F_{R}$, $M_{4}$ , $g$ et les dimensions du
système.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**BRAS DE LE VIER ET BASCULEMENT**

![](11-Actions Mécaniques/Cours/pandoc/media/image338.png){width="2.3270833333333334in"
height="2.6979166666666665in"}On peut classer les leviers du corps
humain en trois catégories, permettant de classifier l'efficacité de
chacune des articulations du corps humain (inter-appui, inter-résistant
et inter-moteur).

**Système de levier inter-appui :** F est la force musculaire des
extenseurs du coup et R le poids de la tête. Le point d'appui est le
point A.

**Déterminer l'effort développé par les extenseurs pour obtenir
l'équilibre.**

![](11-Actions Mécaniques/Cours/pandoc/media/image339.png){width="3.1083333333333334in"
height="2.107638888888889in"}

**Système de levier inter-moteur** : Fm la force musculaire du biceps se
situe entre le point d'appui A et le poids R de 50N. **Déterminer
l'effort développé par le biceps pour obtenir l'équilibre.**

![](11-Actions Mécaniques/Cours/pandoc/media/image340.jpeg){width="4.052777777777778in"
height="2.3097222222222222in"}

**Déterminer la relation entre l'effort du vérin et l'effort dû au vent
en déterminant l'expression du moment en A en projection sur l'axe z.**

[Données :]{.underline}

> $\overrightarrow{AB} = a \cdot \overrightarrow{z}$
> $\overrightarrow{BC} = b \cdot \overrightarrow{z} - c \cdot \overrightarrow{y}$
>
> $$\overrightarrow{BG} = d \cdot \overrightarrow{z} + e \cdot \overrightarrow{y} + f \cdot \overrightarrow{x}$$

![C:\\Users\\Thomas\\Desktop\\modele-verin.jpg](11-Actions Mécaniques/Cours/pandoc/media/image341.jpeg){width="3.379166666666667in"
height="2.1590277777777778in"}

La figure ci-contre est une modélisation de la vis d'un vérin en vue de
son dimensionnement par la *RdM*. Elle est soumise aux actions
extérieures suivantes :

-   couple moteur en O
    > $\mathcal{T}_{\left\{ mot \rightarrow vis \right\}} = \begin{Bmatrix}
    > \overrightarrow{0} \\
    > C_{mot} \cdot \overrightarrow{x}
    > \end{Bmatrix}_{O}\ \ $

-   $\mathcal{T}_{\left\{ mot \rightarrow vis \right\}} = \begin{Bmatrix}
    > X_{vis} \cdot \overrightarrow{x} + Y_{vis} \cdot \overrightarrow{y} \\
    >  - C_{mot} \cdot \overrightarrow{x}
    > \end{Bmatrix}_{A}\ \ $

**Déterminer les inconnues de liaisons en O et en A (Y~0~; X~0~ et
Y~B~).**

![](11-Actions Mécaniques/Cours/pandoc/media/image342.emf){width="2.8006944444444444in"
height="3.754166666666667in"}**[Basculement Robot]{.underline}**

***Il est important de vérifier que le robot pourra réaliser le scénario
proposé en s\'assurant qu\'il ne basculera pas suite à l\'appui de la
personne sur l\'épaule.***

Dans cette étude statique, on suppose toutes les articulations bloquées
: les moteurs fournissent les couples de maintien nécessaires. On
propose le modèle simplifié, plan, de la figure 13, page suivante : Le
Robot (ensemble $(E)$ ) en équilibre, les deux pieds en appui sur le
sol.

Les liaisons $pieds\ /\ sol$ sont modélisées par deux liaisons
ponctuelles aux points $O_{D}$ et $O_{G}$ (Droit et Gauche). En
supposant qu'il n'y a pas de frottement au niveau des contacts
pieds/sol, on notera :

$$\mathcal{T}\left\{ solD \rightarrow E \right\} = \begin{Bmatrix}
Z_{01} \cdot \overrightarrow{z_{0}} \\
\overrightarrow{0}
\end{Bmatrix}_{O_{D}}\ \ \ \ \ \ \ \ \ \ \ \mathcal{\ \ \ \ \ \ \ \ \ \ \ \ T}\left\{ solG \rightarrow E \right\} = \begin{Bmatrix}
{Z'}_{01} \cdot \overrightarrow{z_{0}} \\
\overrightarrow{0}
\end{Bmatrix}_{O_{G}}$$

L\'effort de la personne sur le robot est modélisé par une force
verticale $\overrightarrow{F} = - F.\overrightarrow{z_{0}}$ appliquée au
point $D$ situé sur l\'épaule comme défini par la figure 13 :
$\overrightarrow{OD}.\overrightarrow{y_{0}} = e = 140\ mm$

La gravité exerce une force verticale
$\overrightarrow{P} = - Mg.\overrightarrow{z_{0}}$ appliquée au centre
de masse $G$ du robot.

Le point $O$ est situé à égale distance des deux pieds :
$\overrightarrow{O_{D}O} = \overrightarrow{{OO}_{G}} = d.\overrightarrow{y_{0}}$

+-----------------------------------------------------------------------+
| 1.  Ecrire les expressions de tous les torseurs des actions           |
|     mécaniques extérieures appliquées au robot $\mathbf{(E)}$ ainsi   |
|     modélisé et isolé.                                                |
|                                                                       |
| 2.  En étudiant l'équilibre de l'ensemble $\mathbf{(E)\ }$*,*         |
|     déterminer les expressions de                                     |
|     $\mathbf{                                                         |
| Z}_{\mathbf{01}}\mathbf{\ et\ }\mathbf{Z}_{\mathbf{01}}^{\mathbf{'}}$ |
|     en fonction *F*, *M*, *g*, *d* et *e* .                           |
|                                                                       |
| Pour vérifier le respect du critère de non-basculement du robot, il   |
| faut que les contacts en $O_{G}$ et $O_{D}$ respectent toujours la    |
| contrainte d\'unilatéralité : le sol ne peut exercer qu\'un effort de |
| réaction vertical ascendant sous chacun des pieds. Le basculement est |
| opéré si l'effort vertical est nul.                                   |
|                                                                       |
| 3.  En déduire les deux inégalités sur $Z_{01}\ et\ Z_{01}^{'}$ qui   |
|     découlent du respect de ce critère.                               |
|                                                                       |
| Données : Masse du Robot Roméo : $M = 40,5\ kg$.                      |
|                                                                       |
| Accélération de la pesanteur : $g = 9,81\ m.s^{- 2}$                  |
|                                                                       |
| Données géométriques : $d = 96\ mm$ ; $e = 140\ mm$                   |
|                                                                       |
| 4.  ![](11                                                            |
| -Actions Mécaniques/Cours/pandoc/media/image343.jpeg){width="2.475in" |
|     height="2.725in"}Quel est l\'effort maximum qui peut être exercé  |
|     sur le robot au point $\mathbf{D}$, tout en assurant la condition |
|     de non-basculement. Conclure quant au respect du cahier des       |
|     charges.                                                          |
+=======================================================================+
+-----------------------------------------------------------------------+

**[Basculement Bouteille]{.underline}**

Une pince de robot, modélisée par la force F, doit venir prélever une
bouteille. Déterminer l'expression de la hauteur maximale h~max~ qui
permet d'éviter le basculement, sachant que le contact se fait avec
frottement.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**BOUCHE DE CLIMATISATION**

![](11-Actions Mécaniques/Cours/pandoc/media/image345.png){width="2.825in"
height="2.5770833333333334in"}

On s'intéresse à une bouche de climatisation de bureau. L'air climatisé
arrive par le réseau d'air climatisé du bâtiment et est distribué par
plusieurs bouches. Le débit d'air entrant sur chaque bouche est
initialement réglé par l'intermédiaire d'un clapet dont l'ouverture est
maîtrisée par un vérin.

![](11-Actions Mécaniques/Cours/pandoc/media/image346.png){width="4.941666666666666in"
height="2.7569444444444446in"}Le schéma cinématique du système de
réglage du débit d'air dans la position « clapet fermé »
($\alpha = \frac{\pi}{6}$) est donné ci-dessous :

[Constituants et paramétrage :]{.underline}

-   Le repère
    $R_{0} = \left( O,\overrightarrow{x},\overrightarrow{y},\overrightarrow{z} \right)$
    est lié au conduit 0 considéré comme fixe.

-   Le repère
    $R_{2} = \left( D,\overrightarrow{x_{2}},\overrightarrow{y},\overrightarrow{z_{2}} \right)$
    est lié à la tige du vérin 2, avec
    $\alpha = \left( \overrightarrow{x},\overrightarrow{x_{2}} \right)$
    et
    $\overrightarrow{AB} = c \cdot \overrightarrow{y} + d \cdot \overrightarrow{z}$

[Hypothèses :]{.underline}

-   Les liaisons sont considérées comme parfaites.

-   L'action de la pesanteur sur les différents solides sera négligée
    sauf pour le clapet 1 de masse
    ![](11-Actions Mécaniques/Cours/pandoc/media/image347.wmf) et de
    centre de gravité
    ![](11-Actions Mécaniques/Cours/pandoc/media/image348.wmf) tel que
    $\overrightarrow{OG} = a \cdot \overrightarrow{y} - h \cdot \overrightarrow{z}$.

[Données :]{.underline}

-   $\overrightarrow{OA} = 2 \cdot a \cdot \overrightarrow{y}$
    $\overrightarrow{OM} = a \cdot \overrightarrow{y} - f \cdot \overrightarrow{z}$
    ![](11-Actions Mécaniques/Cours/pandoc/media/image349.wmf)

-   Action de la tige du vérin 2 sur le clapet 1 :
    $\left\{ T_{2 \rightarrow 1} \right\} = \begin{Bmatrix}
    X_{2 \rightarrow 1} \cdot \overrightarrow{x_{2}} \\
    \overrightarrow{0}
    \end{Bmatrix}_{B}$

-   Action de l'air sur le clapet 1 :
    $\left\{ T_{a \rightarrow 1} \right\} = \begin{Bmatrix}
    F_{a} \cdot \overrightarrow{x} \\
    \overrightarrow{0}
    \end{Bmatrix}_{M}$ avec
    ![](11-Actions Mécaniques/Cours/pandoc/media/image350.wmf)

***[Objectif :]{.underline}** Déterminer, dans la position du système
« clapet fermé », la valeur de l'action mécanique de l'actionneur sur le
clapet**.***

***Q1.** Justifier, à l'aide du Principe Fondamental de la Statique
appliqué sur l'ensemble E={2+3}, la forme du torseur*
$\left\{ T_{2 \rightarrow 1} \right\}$*.*

***Q2.** Déterminer, en appliquant le PFS sur le ou les isolements de
votre choix, l'expression de*
![](11-Actions Mécaniques/Cours/pandoc/media/image351.wmf) *en fonction
de* ![](11-Actions Mécaniques/Cours/pandoc/media/image352.wmf) *et des
dimensions du système lorsque le système est dans la position « clapet
fermé ».*

***Q3.** Faire l'application numérique.*

![](11-Actions Mécaniques/Cours/pandoc/media/image353.png){width="3.082638888888889in"
height="2.1347222222222224in"}Le concepteur du système de réglage du
débit d'air souhaite remplacer le vérin par un moteur électrique pour
commander l'ouverture du clapet.

Le schéma cinématique du système est alors le suivant :

***Q4.** Déterminer, en appliquant le PFS sur le ou les isolements de
votre choix, l'expression du couple moteur*
![](11-Actions Mécaniques/Cours/pandoc/media/image354.wmf) *en fonction
de* ![](11-Actions Mécaniques/Cours/pandoc/media/image352.wmf) *et des
dimensions du système lorsque le système est dans la position « clapet
fermé ».*

***Q5.** Faire l'application numérique.*

**[\
]{.underline}**

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**SUSPENSION AUTOMOBILE**

![](11-Actions Mécaniques/Cours/pandoc/media/image355.png){width="2.8916666666666666in"
height="3.1416666666666666in"}On s'intéresse à une suspension automobile
dont on donne ci-dessous un extrait du cahier des charges fonctionnel.

![](11-Actions Mécaniques/Cours/pandoc/media/image355.png){width="2.941666666666667in"
height="1.15in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image356.wmf)L'affaissement
statique correspond à la variation de longueur des ressorts
d'amortisseurs lors de leur écrasement sous le propre poids de la
voiture.

La figure ci-contre représente le schéma cinématique de la suspension,
en vue de face de la voiture :

-   1 est le châssis de la voiture ;

-   9 est le ressort ;

-   0 est la route.

[Hypothèses et données :]{.underline}

-   le problème est plan ;

-   l'action de la pesanteur est négligée sauf sur le châssis de la
    > voiture;

-   toutes les liaisons sont parfaites ;

-   l\'action du sol sur la roue est modélisée au point L par un torseur
    > glisseur dont la résultante est
    > :$\overrightarrow{R_{0 \rightarrow 6}} = F_{0 \rightarrow 6} \cdot \overrightarrow{y}$.

> $F_{0 \rightarrow 6}$ représente le quart du poids de la voiture
> (![](11-Actions Mécaniques/Cours/pandoc/media/image357.wmf)), qui est
> considéré comme étant réparti également sur les quatre roues.

-   l'action du ressort 9 sur 2 est modélisable par :

> $\left\{ T_{9 \rightarrow 2} \right\} = \begin{Bmatrix}
>  - k \cdot (\Delta\mathcal{l)} \cdot \overrightarrow{y} \\
> \overrightarrow{0}
> \end{Bmatrix}$ avec
> ![](11-Actions Mécaniques/Cours/pandoc/media/image358.wmf)

-   $a = 16cm,b = 33cm,c = 8cm,d = 25cm,h = 3cm,L = 15 cm,e = 9cm,\mu = 18cm$

> ![](11-Actions Mécaniques/Cours/pandoc/media/image359.wmf)

***[Objectif :]{.underline}** Vérifier le critère de la fonction FS1.*

***Q1.** Justifier, à l'aide du Principe Fondamental de la Statique
appliqué à 3, que* $Y_{4 \rightarrow 3} = 0$*.*

***Q2.** Déterminer, en appliquant le Principe Fondamental de la
Statique à l'ensemble E=4+6 au point D, les trois équations scalaires
liant les composantes d'actions mécaniques et les dimensions du
système.*

***Q3.** Déterminer, en appliquant le Principe Fondamental de la
Statique à 2 au point A, les trois équations scalaires liant les
composantes d'actions mécaniques et les dimensions du système.*

***Q4.** En déduire une relation entre* $F_{0 \rightarrow 6}$,
$\Delta\mathcal{l}$ et *les dimensions du système. Faire l'application
numérique.*

***Q5.** Conclure quant au respect du critère de la fonction FS1.*

*\
*

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**MACHINE DE TRACTION**

![](11-Actions Mécaniques/Cours/pandoc/media/image360.emf)On s'intéresse
à une machine de traction qui a pour objectif de déformer en traction
une éprouvette afin de connaître le comportement du matériau qui la
constitue. L\'éprouvette est serrée entre deux mandrins et le
déplacement d'un des deux mandrins, lors de la phase d'essais, permet de
tirer sur l'éprouvette.

![](11-Actions Mécaniques/Cours/pandoc/media/image361.emf)

Le schéma cinématique de la machine de traction est donné ci-dessous :

![](11-Actions Mécaniques/Cours/pandoc/media/image362.emf)

[Constituants :]{.underline}

-   un moteur (stator 0, rotor 6) délivrant un couple
    ![](11-Actions Mécaniques/Cours/pandoc/media/image363.wmf) ,

-   deux courroies 4 et 5,

-   deux vis 1 et 3 de pas à droite
    ![](11-Actions Mécaniques/Cours/pandoc/media/image364.wmf),

-   le mandrin supérieur 2.

[Hypothèses :]{.underline}

-   toutes les liaisons sont parfaites.

-   l'action de la pesanteur est négligée.

[Données :]{.underline}

-   L\'éprouvette exerce sur la pièce 2 une action mécanique modélisée
    par le glisseur :

$$\left\{ T_{ep \rightarrow 2} \right\} = \begin{Bmatrix}
 - F.\overrightarrow{y} \\
\overrightarrow{0}
\end{Bmatrix}_{O}$$

-   La courroie 4 exerce sur 1, grâce à l\'action du moteur, une action
    mécanique modélisée par le torseur :
    $\left\{ T_{4 \rightarrow 1} \right\} = \begin{Bmatrix}
    \overrightarrow{0} \\
    M_{4 \rightarrow 1}.\overrightarrow{y}
    \end{Bmatrix}_{A}$

-   $\overrightarrow{AB} = L.\overrightarrow{y}$ ;
    $\overrightarrow{BO} = D.\overrightarrow{x}$ ;
    $\overrightarrow{OC} = h.\overrightarrow{y}$

***[Objectif :]{.underline}** Vérifier le critère de la fonction FS1.*

***Pour des raisons de symétrie, on ne s'intéresse dans la suite qu'à la
moitié de gauche de la machine de traction, c\'est-à-dire aux solides 0,
1 et 2.***

***Q1.** Etablir le graphe de structure du système de la partie du
système étudiée : solides 0, 1 et 2.*

***Q2.** Déterminer, en appliquant le Principe Fondamental de la
Statique à 2 au point B, les six équations scalaires liant les
composantes d'actions mécaniques et les dimensions du système.*

***Q3.** Déterminer, en appliquant le Principe Fondamental de la
Statique à 1 au point B, les six équations scalaires liant les
composantes d'actions mécaniques et les dimensions du système.*

***Q4.** En déduire une relation entre*
![](11-Actions Mécaniques/Cours/pandoc/media/image365.wmf)*,*
![](11-Actions Mécaniques/Cours/pandoc/media/image366.wmf) *et les
dimensions du système.*

La courroie 4 s'enroule sans glisser autour de deux poulies de même
rayon liées à 1 et 6. Le couple délivré par le moteur est tel que :
$|C| = \left| M_{4 \rightarrow 1} \right| + \left| M_{6 \rightarrow 3} \right| = 2 \cdot \left| M_{4 \rightarrow 1} \right|$

***Q5.** Conclure quant au respect du critère de la fonction FS1.*

*\
*

## ![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in" height="0.3888888888888889in"}THEOREME DE L'ENERGIE CINETIQUE

**MACHINE 5 AXES**

*([Source]{.underline} : ATS 2006, Jacques Le Goff)*

![](11-Actions Mécaniques/Cours/pandoc/media/image367.png){width="3.8958333333333335in"
height="3.275in"}**Mise en situation**

*[On propose le paramétrage suivant :]{.underline}*

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image368.wmf) est
lié au châssis (0).

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image369.wmf) est
lié à l'ensemble {berceau+parc échelle} (5) ;

Avec :

![](11-Actions Mécaniques/Cours/pandoc/media/image370.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image371.wmf) ;

![](11-Actions Mécaniques/Cours/pandoc/media/image372.wmf) ;
![](11-Actions Mécaniques/Cours/pandoc/media/image373.wmf).

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image374.wmf) est
lié au vérin (3+4) ;

Avec :

![](11-Actions Mécaniques/Cours/pandoc/media/image375.wmf) ;
![](11-Actions Mécaniques/Cours/pandoc/media/image376.wmf)et
![](11-Actions Mécaniques/Cours/pandoc/media/image377.wmf)

**Guidage de l'axe « X »**

![](11-Actions Mécaniques/Cours/pandoc/media/image378.png){width="2.0520833333333335in"
height="0.8708333333333333in"}![](11-Actions Mécaniques/Cours/pandoc/media/image379.png){width="3.4791666666666665in"
height="2.65in"}![](11-Actions Mécaniques/Cours/pandoc/media/image380.png){width="5.9375in"
height="0.5270898950131233in"}![](11-Actions Mécaniques/Cours/pandoc/media/image381.png){width="5.9456342957130355in"
height="0.41656167979002623in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image382.png){width="5.479166666666667in"
height="1.6354166666666667in"}

> • la masse de l'outil est négligeable

![](11-Actions Mécaniques/Cours/pandoc/media/image383.png){width="5.625in"
height="1.6947954943132109in"}

1.  **Exprimer** l'inertie équivalente, notée J~eq~, des masses en
    mouvement ramenées sur l'arbre moteur par rapport à son axe de
    rotation

2.  **En déduire** l'expression du couple moteur noté C~mx~. *Les
    liaisons sont supposées parfaites.*

![](11-Actions Mécaniques/Cours/pandoc/media/image384.png){width="5.313194444444444in"
height="1.870294181977253in"}

3.  En phase d'accélération maximale sur l'axe « X », x''=10 m/s^2^ ,
    **calculer** le couple, noté C~mx~, que le moteur d'axe « X » doit
    développer.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![Senior](11-Actions Mécaniques/Cours/pandoc/media/image385.jpeg){width="0.36452646544181977in"
height="0.6145833333333334in"}**PANNEAUX DÉROULANTS**

*([Source]{.underline} : Concours ATS 2011)*

**Mise en situation**

Le panneau publicitaire déroulant, appartenant à la catégorie des MUPI
(Mobilier Urbain Pour l'Information), est un objet installé dans
l'espace public. C'est un media de masse qui permet de toucher le
consommateur sur son lieu de vie. La société JC DECAUX qui installe des
mobiliers urbains fixes s'est intéressée depuis longtemps à pouvoir
toucher un maximum de personnes grâce à l'utilisation de ces panneaux.

Ce panneau permet de faire défiler successivement dans un sens puis dans
l'autre jusqu'à 7 affiches avec un temps d'exposition constant pour
chaque affiche. Le format des affiches rétro éclairées est d'environ
8m². Le dispositif est constitué de deux rouleaux (longueur 3200mm et ∅
140mm). Le défilement s'effectue à la vitesse de 1m/s avec une rampe
d'accélération et de décélération de chacune 1 seconde. Lors de
l'enroulement sur le rouleau, on souhaite respecter la loi cinématique
suivante :

**Figure 1** : Loi cinématique de défilement d'une affiche du bandeau

Cahier des charges fonctionnel partiel :

  -------- -------------------- --------------------- --------------------
           ***Fonction de       ***Critère            ***Niveau***
           service***           d\'appréciation***    

           FP12                 Tension sur l'affiche \+ ou -- 10N
                                40N                   

           FT114                Vitesse 1m/s          \+ ou -- 10%

           FT115                Temps d'exposition 2s de 1s à 4s
  -------- -------------------- --------------------- --------------------

**Analyse de la solution à deux motorisations à commande alternée**

Cette solution peut être décrite par le schéma simplifié suivant :

**Figure 2** : Structure de la solution à deux motorisations

Dans un premier temps, on utilise deux groupes motoréducteurs
identiques. Le fonctionnement de ce système est décrit par le tableau
suivant :

  -----------------------------------------------------------------------
                                     Motorisation     Motorisation basse
                                     haute            
  ---------------------------------- ---------------- -------------------
  Enroulement sur rouleau haut       Alimentée        Non alimentée

  Enroulement sur rouleau bas        Non alimentée    Alimentée
  -----------------------------------------------------------------------

Au cours de l'enroulement du bandeau d'affiches sur un rouleau,
l'ensemble des pièces est donc entraîné par un seul moteur. Pour
garantir en permanence une tension suffisante dans l'affiche même en
régime établi, on décide d'implanter des organes de friction (frottement
sec) au niveau de chaque liaison pivot entre chaque rouleau et le bâti.
Pendant l'enroulement sur le rouleau haut, l'action mécanique de chaque
organe de friction sur chacun des rouleaux bas et haut peut être
modélisée par le torseur suivant dans lequel $C_{fr}$ désigne le couple
de frottement :

$\left\{ T(Frott\ :bâti \rightarrow rouleau\ haut) \right\} = \begin{Bmatrix}
\overrightarrow{0} & - C_{fr}.{\overrightarrow{X}}_{0}
\end{Bmatrix}_{A}$ ;
$\left\{ T(Frott\ :bâti \rightarrow rouleau\ bas) \right\} = \begin{Bmatrix}
\overrightarrow{0} & - C_{fr}.{\overrightarrow{X}}_{0}
\end{Bmatrix}_{B}\ $ avec $C_{fr} > 0$

Pour l'étude, on propose alors le schéma détaillé suivant :

**Figure 3** : Modèle retenu pour l'étude

**Hypothèses** :

-   le référentiel $R_{0}$ lié au bâti **0** est galiléen ;

-   initialement le bandeau d'affiches est entièrement enroulé sur le
    rouleau bas ;

-   on étudie l'enroulement du bandeau sur le rouleau haut ;

-   les rayons des rouleaux sont supposés constants durant l'enroulement
    du bandeau sur le rouleau haut (les deux rouleaux tournent à la même
    vitesse pendant l'enroulement du bandeau) ;

-   l'effet de la pesanteur est négligé face aux autres actions
    mécaniques ;

-   les liaisons sont supposées parfaites ;

-   les inerties des pièces des dispositifs poulies-courroie sont
    négligées ;

-   les courroies sont inextensibles et sans masse ;

-   le bandeau d'affiches est inextensible ;

-   la partie du bandeau d'affiches située entre les deux rouleaux
    (partie non enroulée) est sans masse.

On appelle :

-   $am$ : les arbres moteur des transmissions haute et basse ;

-   $aer$ : les arbres d'entrée des réducteurs haut et bas ;

-   $asr$ : les arbres de sortie des réducteurs haut et bas ;

-   $roul$ : les rouleaux haut et bas.

On note :

-   $J_{roul}$ : le moment d'inertie d'un rouleau vide par rapport à son
    axe ;

-   $J_{m}$ : le moment d'inertie de l'arbre moteur par rapport à son
    axe ;

-   $J_{eqr}$ : le moment d'inertie équivalent du réducteur ramené sur
    son arbre\
    d'entrée ;

-   $J_{b}$ : le moment d'inertie du bandeau d'affiches par rapport à
    l'axe d'un rouleau\
    lorsque le bandeau d'affiches est entièrement enroulé sur le dit
    rouleau ;

-   $\Omega_{roul}$ : la vitesse angulaire du rouleau autour de son axe
    par rapport à $R_{0}\ $;

-   $\Omega_{m}$ : la vitesse angulaire de l'arbre moteur autour de son
    axe par rapport à $R_{0}\ $;

-   $\Omega_{asr}$ : la vitesse angulaire de l'arbre de sortie du
    réducteur autour de son axe\
    par rapport à $R_{0}\ $;

-   $k_{r}$ : le rapport de transmission du réducteur :
    $k_{r} = \frac{\Omega_{asr}}{\Omega_{aer}} = \frac{\Omega_{asr}}{\Omega_{m}}$ ;

-   $k_{pc}$ : le rapport de transmission du dispositif
    poulies-courroie : $k_{pc} = \frac{\Omega_{roul}}{\Omega_{asr}}$ ;

-   $C_{m}$ : le couple exercé sur l'arbre moteur par le stator du
    moteur alimenté.

1.  Donner l'expression de la vitesse linéaire de l'affiche en régime
    > établi $V_{0}$ en fonction de $\Omega_{m}$, $k_{r}$, $k_{pc}$ et
    > du rayon d'enroulement $R$ du bandeau sur le rouleau.

Pendant la phase d'accélération du bandeau d'affiche, la vitesse de
défilement du bandeau est variable (figure 1). Elle est notée $V(t)$.
L'accélération linéaire du bandeau est constante. Elle est notée
$\gamma$.

2.  Donner l'expression de l'accélération linéaire de l'affiche $\gamma$
    > en fonction de $k_{r}$, $k_{pc}$, du rayon d'enroulement $R$ et de
    > l'accélération angulaire de l'arbre moteur notée
    > ${\dot{\Omega}}_{m}$.

Pour déterminer la tension dans l'affiche, on propose de se ramener au
modèle équivalent suivant :

**Figure 3** : Nouveu modèle retenu pour l'étude

On note :

-   $J_{eqh}$ : le moment d'inertie équivalent de toute la chaîne de
    > transmission haute ramené sur le rouleau haut ;

-   $J_{eqb}$ : le moment d'inertie équivalent de toute la chaîne de
    > transmission basse ramené sur le rouleau bas.

3.  En utilisant la figure 3, exprimer en fonction de $\Omega_{roul}$,
    > des différents moments d'inertie ($J_{roul}$, $J_{m}$, $J_{eqr}$,
    > $J_{b}$) et de $k_{r}$ et $k_{pc}$, l\'énergie cinétique
    > $T\left( \frac{S_{bas}}{0} \right)$ dans son mouvement par rapport
    > à $R_{0}$ de l'ensemble $S_{bas}$ formé par :

-   l'arbre moteur bas ;

-   l'arbre d'entrée bas du réducteur ;

-   l'arbre de sortie bas du réducteur ;

-   les arbres d'entrée et de sortie du dispositif poulies-courroie
    bas ;

-   le rouleau bas sur lequel est entièrement enroulé le bandeau
    d'affiches.

4.  En déduire l'expression du moment d'inertie équivalent $J_{eqb}$
    > ramenée sur le rouleau bas.

5.  Calculer $J_{eqb}$ si $J_{m} = 120\ kg.{mm}^{2}$,
    > $J_{eqr} = 1,5\ kg.{mm}^{2}$ et
    > $\left( J_{roul} + J_{b} \right) = 161500\ kg.{mm}^{2}$.

On cherche maintenant la tension dans l'affiche $T_{aff}$ (effort exercé
par la partie haute du bandeau s'enroulant sur le rouleau supérieur sur
la partie basse du bandeau se déroulant du rouleau inférieur).

L'action mécanique décrivant $T_{aff}$ est modélisée par le torseur
suivant :

$$\left\{ T(bandeau\ haut \rightarrow bandeau\ bas) \right\} = \begin{Bmatrix}
T_{aff}.{\overrightarrow{Z}}_{0} & \overrightarrow{0}
\end{Bmatrix}_{K}$$

Le modèle utilisé est le suivant :

**Figure 4** : Modèle pour l'analyse de la tension dans l'affiche

1.  

2.  

3.  

4.  1.  
    2.  

Détermination de la tension dans l'affiche en régime établi (vitesse
linéaire de défilement du bandeau $\mathbf{V}_{\mathbf{0}}$)

6.  Appliquer le théorème du moment résultant (Principe Fondamental de
    > la Statique) à l'ensemble Σ = {rouleau bas + bandeau bas} selon
    > l'axe $\left( B,{\overrightarrow{X}}_{0} \right)$ pour déterminer
    > la relation liant la tension dans l'affiche $T_{aff}$, le couple
    > de frottement $C_{fr}$ et le rayon d'enroulement $R$.

7.  Calculer la valeur de $C_{fr}$ si on souhaite fixer la tension
    > $T_{aff}$ dans l'affiche à $40\ N$ avec un rayon d'enroulement
    > $R = 76\ mm$.

Pour la suite de l'étude, on fixe le couple de frottement à
$C_{fr} = 3\ N.m$.

Détermination de la tension dans l'affiche en régime transitoire (phase
d'accélération du bandeau)

8.  Appliquer le théorème du moment dynamique à l'ensemble Σ = {rouleau
    > bas + bandeau bas} selon l'axe
    > $\left( B,{\overrightarrow{X}}_{0} \right)$ dans son mouvement par
    > rapport au repère galiléen $R_{0}$ pour déterminer la relation
    > liant la tension dans l'affiche $T_{aff}$, l'accélération linéaire
    > de l'affiche $\gamma$, l'inertie équivalente $J_{eqb}$, le rayon
    > d'enroulement $R$ et le couple de frottement $C_{fr}$.

9.  Calculer la tension dans l'affiche $T_{aff}$ si
    > $\gamma = 1\ m.s^{- 2}$, $k_{r} = \frac{1}{19,5}$, $k_{pc} = 2$,
    > $J_{eqb} = 173.10^{3}\ kg.{mm}^{2}$, $R = 76\ mm$ et
    > $C_{fr} = 3\ N.m$.

10. La tension dans l'affiche en régime transitoire respecte-t-elle le
    > cahier des charges fonctionnel (fonction FP12) ?

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**AGITATEUR**

*([Source]{.underline} : PSI 2006)*

**Mise en situation**

![](11-Actions Mécaniques/Cours/pandoc/media/image388.png){width="2.28125in"
height="1.4375in"} Dans le cadre d'expérimentations pour soigner les
malades du diabète, une équipe de chercheurs travaille sur une technique
de greffe de cellules du pancréas.

Ces cellules sont obtenues à partir d'un pancréas issu d'un don
d'organes. Elles sont isolées du pancréas puis purifiées. Ces dernières,
responsables de la sécrétion d'insuline, sont, après un maintien en
culture (24 à 48 heures) greffées à un patient diabétique.

Afin d'isoler les cellules, on place des fragments de pancréas au sein
d'une petite enceinte thermostatée . On a préalablement injecté un
mélange d'enzymes à l'intérieur du pancréas. Une fois placés dans
l'enceinte, les fragments de pancréas vont «baigner» dans cette enzyme,
ce qui va enclencher un phénomène de digestion. Tout au long de la
manipulation, la solution va circuler, dans un circuit fermé constitué
de l'enceinte, de tuyaux et d'une pompe. Pour faciliter l'action de
l'enzyme, l'opération se fait sous agitation permanente.

La digestion est aussi facilitée par le mouvement de billes en acier au
sein de l'enceinte. L'agitation dure 1h30 à 2h30 et doit permettre la
libération et la récolte des cellules du pancréas.

Nous allons dans la suite étudier le système d'agitation et de chauffage
de l'enceinte thermostatée

![Agitateur A3 H -
Feuille1](11-Actions Mécaniques/Cours/pandoc/media/image389.png){width="3.0541666666666667in"
height="2.191666666666667in"}

Le système est composé de deux chaînes cinématiques indépendantes  :

-   chaîne n°1 (principale) constituée d'un moteur électrique brushless
    **M~1~**, d'un excentrique **1**, d'une bielle **2** et du bras
    **3** sur lequel est montée la seconde chaîne cinématique ;

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image390.emf){width="1.6711614173228346in"
    height="2.666563867016623in"}chaîne n°2 (secondaire) constituée d'un
    moto réducteur électrique **M~2\ ~**solidaire du bras 3, d'un
    excentrique, d'une bielle et de l'ensemble {pince, enceinte}.

![Img1](11-Actions Mécaniques/Cours/pandoc/media/image391.png){width="2.9166666666666665in"
height="1.8125in"}

> Modèle simplifié de l\'ensemble {1} Schéma cinématique

**Etude mécanique de l'agitateur**

[Hypothèses]{.underline} :

-   la chaîne n°2 est à l'arrêt dans la position du plan de coupe A-A,
    l'enceinte est pleine et considérée homogène ;

-   l'ensemble mobile {3} est défini par : {3} = {Bras **3**, moteur
    **M~2~**, pince, enceinte} ;

• les liaisons sont considérées sans frottement ;

> • l'inertie ![](11-Actions Mécaniques/Cours/pandoc/media/image392.wmf)
> ainsi que la position du centre de masse
> ![](11-Actions Mécaniques/Cours/pandoc/media/image393.wmf) de
> l'ensemble mobile {3}
>
> ont été déterminées par un modeleur volumique :
> ![](11-Actions Mécaniques/Cours/pandoc/media/image394.wmf)** ;**
> ![](11-Actions Mécaniques/Cours/pandoc/media/image395.wmf) en mm ;

• la masse de l'ensemble mobile {3} est
![](11-Actions Mécaniques/Cours/pandoc/media/image396.wmf) ;

• les masses des « petites » pièces (bielle **2**, excentrique **1**,
axes, coussinets, circlips, vis) sont négligées devant les autres
pièces ;

• l'inertie de l'arbre du moteur M1 est négligée devant celle de
l'ensemble mobile {3} ;

• le calcul est effectué en régime permanent : vitesse d'entrée
constante de 120 tr/min ;

• on ne tient pas compte du {ressort} placé entre le bras **3** et le
châssis (voir photo ) ;

• les actions mécaniques des tuyaux sont négligeables ;

**Question 1 :** En appliquant le théorème de l'énergie cinétique à
l'ensemble des solides en mouvement, **déterminer** l'expression
littérale du couple moteur
![](11-Actions Mécaniques/Cours/pandoc/media/image397.wmf) en fonction
des grandeurs géométriques et d'inertie du système, ainsi que des
variables![](11-Actions Mécaniques/Cours/pandoc/media/image398.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image399.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image400.wmf).

![](11-Actions Mécaniques/Cours/pandoc/media/image401.png){width="3.3229166666666665in"
height="1.40625in"}

**Question 2 :** **Déterminer**, dans le cadre de l'approximation
![](11-Actions Mécaniques/Cours/pandoc/media/image402.wmf) « petit »,
l'expression du couple que devra fournir le moteur M1 à la vitesse
constante de 12 rad/s aux instants : t~1~ = 0,1 s, t~2~ = 0,15 s, t~3~ =
0,25 s et t~4~ = 0,35 s.

On désire caractériser l'influence du ressort vu sur la photo. Pour
simplifier on suppose qu'il reste vertical au cours du mouvement du bras
**3** et qu'il agit au point D. Sa raideur est *k* = *7 N/mm,* et pour
![](11-Actions Mécaniques/Cours/pandoc/media/image403.wmf) (bras
horizontal) son action sur le bras **3** est nulle. On donne
![](11-Actions Mécaniques/Cours/pandoc/media/image404.wmf) en mm.

**Question 3 :** En appliquant le théorème de l'énergie cinétique à
l'ensemble des solides en mouvement, déterminer l'expression littérale
du couple moteur C~m~ en fonction des grandeurs géométriques et
d'inertie du système, de la raideur k, ainsi que des
variables$\overset{..}{\theta_{3}}$, $\overset{.}{\theta_{3}}$ et
$\overset{.}{\theta_{1}}$.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**COFFRE MOTORISE A6**

*([Source]{.underline} : Centrale Supélec 2007)*

**Mise en situation**

![](11-Actions Mécaniques/Cours/pandoc/media/image405.png){width="1.5416666666666667in"
height="0.8645833333333334in"}Depuis 2005, un coffre motorisé est
proposé en option sur l'Audi A6. Ce système développé par la société
Valéo a été récompensé en 2002 par le prix de l'innovation électronique
automobile EPCOS/SIA dans la catégorie « Vie à bord, confort, habitacle
».

![](11-Actions Mécaniques/Cours/pandoc/media/image406.png){width="3.6145833333333335in"
height="1.5104166666666667in"}La motorisation du hayon permet
l'ouverture ou la fermeture automatique du coffre. L'ouverture
s'effectue soit à l'aide de la télécommande, soit par action sur une
touche située à proximité du conducteur, soit par action sur une touche
située sur la poignée du hayon. La fermeture s'effectue par action sur
une touche située sur la face interne du hayon.

Une unité électromécanique est présentée sur la **figure 3**. Elle est
constituée d'un moteur électrique relié par l'intermédiaire d'un
embrayage à un réducteur à trains épicycloïdaux transmettant la vitesse
de rotation adéquate au mécanisme de transformation de mouvement.

Le schéma cinématique de l'unité électromécanique relié au hayon et à la
caisse du véhicule est présenté sur la **figure 4**.

![](11-Actions Mécaniques/Cours/pandoc/media/image407.png){width="6.318623140857393in"
height="3.8649857830271217in"}

**Estimation du couple nécessaire à l'ouverture du hayon**

![](11-Actions Mécaniques/Cours/pandoc/media/image408.png){width="4.322916666666667in"
height="2.1614588801399823in"}Pour estimer le couple nécessaire à
l'ouverture du hayon, on opte pour le modèle de la **figure 6**.

Le hayon **[45]{.underline}** dont le tableau 1 reprend les principales
caractéristiques, est en liaison pivot d'axe
![](11-Actions Mécaniques/Cours/pandoc/media/image409.wmf)par rapport à
la caisse du véhicule **[0]{.underline}**. On définit le couple
nécessaire à la mise en mouvement par un torseur agissant sur
**[45]{.underline}** s'écrivant sous la forme :
![](11-Actions Mécaniques/Cours/pandoc/media/image410.wmf)

***[Hypothèses de calcul :]{.underline}***

• On notera ![](11-Actions Mécaniques/Cours/pandoc/media/image411.wmf)la
base liée au solide
![](11-Actions Mécaniques/Cours/pandoc/media/image412.wmf) .

• Le système de coffre motorisé ne fonctionne que si le véhicule est
immobile ; dans ce cas, le repère
![](11-Actions Mécaniques/Cours/pandoc/media/image413.wmf)est considéré
galiléen.

• L'accélération de la pesanteur s'écrit
![](11-Actions Mécaniques/Cours/pandoc/media/image414.wmf)avec
![](11-Actions Mécaniques/Cours/pandoc/media/image415.wmf) .

• La liaison pivot est supposée parfaite.

![](11-Actions Mécaniques/Cours/pandoc/media/image416.png){width="4.527638888888889in"
height="1.6491404199475066in"}

1.  Après avoir précisé le système isolé, et en utilisant le théorème de
    l'énergie cinétique, **déterminer** l'expression du couple
    ![](11-Actions Mécaniques/Cours/pandoc/media/image417.wmf)nécessaire
    à la mise en mouvement du hayon en fonction de
    ![](11-Actions Mécaniques/Cours/pandoc/media/image418.wmf).

2.  Après avoir précisé le système isolé, et en utilisant le principe
    fondamental de la dynamique, **déterminer** l'expression du couple
    ![](11-Actions Mécaniques/Cours/pandoc/media/image417.wmf)nécessaire
    à la mise en mouvement du hayon en fonction de
    ![](11-Actions Mécaniques/Cours/pandoc/media/image418.wmf).

Dans la suite, on suppose que la composante du couple liée aux effets
dynamique est négligeable devant celle liée à l'effet de la pesanteur :

3.  **Tracer** approximativement l'allure de la courbe représentative de
    ![](11-Actions Mécaniques/Cours/pandoc/media/image419.wmf).

4.  **Déterminer** la valeur maximale du couple que doit fournir chacune
    des unités électromécanique sachant que les deux unités produisent
    le même couple.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**DUO VOYAGEUR CONCEPT**

*([Source]{.underline} : CAPET Technologie 2009)*

**Mise en situation**

![duo_voyager](11-Actions Mécaniques/Cours/pandoc/media/image420.jpeg){width="2.3541666666666665in"
height="1.5729166666666667in"}BABOULIN, est une société française
spécialisée dans l'aménagement technique de véhicules en direction des
Personnes à Mobilité Réduite.

Le « Duo Voyageur Concept » est un système qui permet à la Personnes à
mobilité Réduite de s'installer dans une voiture, côté passager, sans
avoir à bouger de son fauteuil roulant.

Ce dernier, grâce à un bras articulé, passe directement de l'extérieur
du véhicule à la place du siège d'origine sans effort physique.

![](11-Actions Mécaniques/Cours/pandoc/media/image421.png){width="4.975694444444445in"
height="3.0677088801399823in"}On s'intéresse uniquement au la solution
qui permet la rotation, autour d'un axe vertical, du bras supportant le
siège par rapport au châssis de la voiture.

Cette solution qui permet la transmission d'un mouvement de rotation du
moteur en un mouvement de rotation du bras est modélisé sur la figure
ci-contre :

![](11-Actions Mécaniques/Cours/pandoc/media/image423.png){width="4.0625in"
height="2.1770833333333335in"}![](11-Actions Mécaniques/Cours/pandoc/media/image424.wmf)
est un repère lié au châssis **[0]{.underline}** de la voiture.

Le bras **[1]{.underline}** a une liaison pivot d'axe
![](11-Actions Mécaniques/Cours/pandoc/media/image425.wmf) avec le
châssis **[0]{.underline}**.

Soit ![](11-Actions Mécaniques/Cours/pandoc/media/image426.wmf) un
repère lié au bras **[1]{.underline}**. On pose
![](11-Actions Mécaniques/Cours/pandoc/media/image427.wmf)

Un moteur d'axe
![](11-Actions Mécaniques/Cours/pandoc/media/image428.wmf), tel que
![](11-Actions Mécaniques/Cours/pandoc/media/image429.wmf), a son stator
fixé au bras **[1]{.underline}** et son rotor **[2]{.underline}**
entraine en rotation le bras **[1]{.underline}** par l'intermédiaire
d'un engrenage à axes parallèles dont une roue est fixe par rapport au
châssis **[0]{.underline}**.

La roue liée au rotor **[2]{.underline}** a pour rayon primitif r~2~ et
celle liée au châssis **[0]{.underline}** a pour rayon primitif r~1~

On pose ![](11-Actions Mécaniques/Cours/pandoc/media/image430.wmf)

![](11-Actions Mécaniques/Cours/pandoc/media/image431.png){width="2.972916666666667in"
height="2.5694444444444446in"}![](11-Actions Mécaniques/Cours/pandoc/media/image432.png){width="4.263888888888889in"
height="2.7in"}

**Calcul de l'accélération angulaire du bras**

1.  En écrivant la condition de roulement sans glissement au point de
    contact J entre la roue lié à **[0]{.underline}** et la roue liée à
    **[2]{.underline}**, **déterminer** la relation entre
    ![](11-Actions Mécaniques/Cours/pandoc/media/image433.wmf)et![](11-Actions Mécaniques/Cours/pandoc/media/image434.wmf)
    en fonction de r~2~ et r~1~ puis de r~2~ et r~0~.

2.  En appliquant le théorème de l'énergie cinétique à l'ensemble des
    solides en mouvement, **déterminer** l'accélération angulaire du
    bras **[1]{.underline}** du robot en fonction du couple du moteur,
    de r~2~ et r~0~, des caractéristiques d'inertie des solides.

*Dans la suite, on nommera 2 l'ensemble 2+rotor*

*Dans la suite, on nommera 1 l'ensemble 1+stator*

Pour des raisons de confort de la personne à mobilité réduite, le cahier
des charges impose, qu'a partir de l'arrêt, le bras **[1]{.underline}**
sur lequel est fixé le fauteuil ne mette pas moins d'une seconde pour
atteindre la vitesse de rotation constante
![](11-Actions Mécaniques/Cours/pandoc/media/image435.wmf).

> On donne ![](11-Actions Mécaniques/Cours/pandoc/media/image436.wmf)

3.  **Vérifier** que l'accélération angulaire trouvée, respecte les
    performances imposées par le cahier des charges

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![](11-Actions Mécaniques/Cours/pandoc/media/image437.png){width="0.9166666666666666in"
height="0.6715277777777777in"}**BORNE SOLAIRE**

*([Source]{.underline} : ATS 2010)*

**Mise en situation**

> ![](11-Actions Mécaniques/Cours/pandoc/media/image438.png){width="3.1506944444444445in"
> height="2.1840277777777777in"}Le dispositif étudié est un système
> permettant de limiter ou d\'interdire la circulation dans des zones à
> accès réservé. Ce dispositif comporte :

-   un caisson intégrant la partie opérative, à savoir une borne
    motorisée rétractable dans le sol,

-   un caisson intégrant la partie commande comportant :

> \- une platine électronique de gestion,

\- une batterie d\'alimentation électrique du système,

\- des cellules photovoltaïques assurant la charge de la batterie.

> ![](11-Actions Mécaniques/Cours/pandoc/media/image440.png){width="3.2666666666666666in"
> height="4.833333333333333in"}Selon son concept innovant et breveté, le
> système utilise un module solaire pour recharger sa batterie.
> L\'installation d\'une borne de ce type ne nécessite aucune tranchée,
> aucun raccordement, ni abonnement EDF ; son alimentation est gratuite
> et peut être envisagée sur n\'importe quel site.
>
> Cependant, le fonctionnement du système est limité à un nombre de
> cycles dont la valeur dépend des conditions d\'ensoleillement. La
> problématique majeure pour ce système est donc d\'atteindre une
> autonomie suffisante, tout en minimisant le coût et l\'encombrement
> des moyens de production et de stockage de l\'énergie électrique.

![](11-Actions Mécaniques/Cours/pandoc/media/image442.png){width="3.8623392388451445in"
height="3.03125in"}

**Détermination des moments des couples moteurs en montée et en
descente**

**[Hypothèses :]{.underline}**

\- Les liaisons de l\'arbre 3 avec le chariot 1 sont considérées
parfaites.

\- L\'arbre de sortie du motoréducteur 2 est lié à l\'arbre 3 par
l\'intermédiaire d\'un limiteur de couple. On considère que le limiteur
de couple transmet à l\'arbre 3 le couple de sortie du réducteur
![](11-Actions Mécaniques/Cours/pandoc/media/image443.wmf) pour la
montée et ![](11-Actions Mécaniques/Cours/pandoc/media/image444.wmf)
pour la descente avec
![](11-Actions Mécaniques/Cours/pandoc/media/image445.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image446.wmf).

\- Le moteur fournit au niveau de l\'entrefer le couple
![](11-Actions Mécaniques/Cours/pandoc/media/image447.wmf) pour la
montée et ![](11-Actions Mécaniques/Cours/pandoc/media/image448.wmf)
pour la descente avec
![](11-Actions Mécaniques/Cours/pandoc/media/image449.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image450.wmf).

\- La masse de l\'arbre 3 et son inertie sont négligées. Le diamètre du
pignon 3 est ![](11-Actions Mécaniques/Cours/pandoc/media/image451.wmf)

\- On supposera le rendement du réducteur de type roue et vis sans fin :
![](11-Actions Mécaniques/Cours/pandoc/media/image452.wmf). On fait
l\'hypothèse que ce rendement est identique pour les deux sens de
rotation.

\- Rapport de réduction k du réducteur : 1/60. (Le réducteur et le
moteur forment le motoréducteur repéré 2 sur le schéma cinématique).

\- Pour le calcul de l\'inertie équivalente, on tiendra compte de la
masse du chariot repère 1 et de tous les éléments embarqués
![](11-Actions Mécaniques/Cours/pandoc/media/image453.wmf) (rappel :
![](11-Actions Mécaniques/Cours/pandoc/media/image454.wmf)) et de
l\'inertie du rotor du moteur
![](11-Actions Mécaniques/Cours/pandoc/media/image455.wmf).![](11-Actions Mécaniques/Cours/pandoc/media/image456.wmf).

\- On donne le torseur des actions mécaniques transmissibles par le bâti
0 sur le chariot 1 au niveau du guidage en A et en B (rappel : les
liaisons au niveau des guidages ne sont pas considérées parfaites) :

![](11-Actions Mécaniques/Cours/pandoc/media/image457.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image458.wmf)

Avec ![](11-Actions Mécaniques/Cours/pandoc/media/image459.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image460.wmf)

\- pour la montée :
![](11-Actions Mécaniques/Cours/pandoc/media/image461.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image462.wmf) ;

\- pour la descente :
![](11-Actions Mécaniques/Cours/pandoc/media/image463.wmf)et
![](11-Actions Mécaniques/Cours/pandoc/media/image464.wmf).

Les valeurs numériques des composantes sont exprimées en Newton (N).

\- On donne le torseur cinématique du chariot 1 dans son mouvement par
rapport au bâti 0 :

![](11-Actions Mécaniques/Cours/pandoc/media/image465.wmf) avec P un
point quelconque appartenant au chariot 1.
![](11-Actions Mécaniques/Cours/pandoc/media/image466.wmf) pour la
montée et ![](11-Actions Mécaniques/Cours/pandoc/media/image467.wmf)pour
la descente.

1.  **Déterminer** la puissance des actions mutuelles entre le chariot 1
    et l\'arbre 3 notée
    ![](11-Actions Mécaniques/Cours/pandoc/media/image468.wmf).
    Justifier la réponse.

2.  **Donner** l\'expression littérale de la puissance galiléenne
    développée par le chariot notée
    ![](11-Actions Mécaniques/Cours/pandoc/media/image469.wmf).

[Remarques]{.underline} :

\- S\'intéresser au poids uniquement ;

\- Préciser correctement les signes pour chaque phase du mouvement
(montée et descente).

3.  **Donner** l\'expression littérale de la puissance dissipée par
    frottement dans le guidage du chariot 1 avec le bâti 0 notée
    ![](11-Actions Mécaniques/Cours/pandoc/media/image470.wmf).

*Préciser correctement les signes pour chaque phase du mouvement (montée
et descente).*

4.  **Déterminer** l\'expression littérale de la puissance fournie par
    le moteur
    ![](11-Actions Mécaniques/Cours/pandoc/media/image471.wmf).

5.  **Donner** l\'expression littérale de l\'énergie cinétique
    galiléenne E de l\'ensemble en mouvement (chariot 1, arbre 3 et
    motoréducteur 2). Exprimer tous les termes de l\'énergie cinétique
    en fonction de la vitesse de rotation du moteur
    ![](11-Actions Mécaniques/Cours/pandoc/media/image472.wmf).

6.  **Donner** l\'expression littérale de l\'inertie équivalente J
    ramenée sur l\'arbre moteur en fonction de m, J~m~, dp~3~ et k.
    **Calculer** sa valeur numérique.

7.  En appliquant le théorème de l\'énergie cinétique et en utilisant
    les réponses aux questions précédentes, **donner** l\'expression du
    couple moteur
    ![](11-Actions Mécaniques/Cours/pandoc/media/image473.wmf) en phase
    de montée et
    ![](11-Actions Mécaniques/Cours/pandoc/media/image474.wmf) en phase
    de descente sans tenir compte du rendement du réducteur, et en
    considérant la vitesse constante.

8.  **Modifier** l\'expression de la réponse à la question précédente du
    couple moteur
    ![](11-Actions Mécaniques/Cours/pandoc/media/image473.wmf) en phase
    de montée et
    ![](11-Actions Mécaniques/Cours/pandoc/media/image474.wmf) en phase
    de descente en tenant compte du rendement du réducteur. Calculer
    leurs valeurs numériques.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**TREMIE DE STOCKAGE**

*([Source]{.underline} : CCP 2014)*

**Fonctionnement :**

Pour doser la quantité adéquate dans la trémie de stockage, il faut
contrôler le temps de rotation de la vis d'Archimède (qui permet
l'acheminement des granulés). La motorisation de la vis est assurée par
un ensemble motoréducteur (références constructeur **figure 2**).

![](11-Actions Mécaniques/Cours/pandoc/media/image475.wmf){width="5.964826115485565in"
height="2.4203969816272966in"}

**Figure 1 : schéma de l'installation d'acheminement des granulés**

**Connaissant les caractéristiques de la vis d'Archimède et la masse
volumique des granulés, combien de tours de vis faut-il effectuer pour
doser 2 kg de granulés ?**

Le couple résistant exercé par les granulés est difficile à modéliser.
Les valeurs retenues sont issues de la capitalisation de connaissances
du constructeur. Il sera admis que ce couple résistant C~r~ est constant
et que 70 % de la puissance moteur est nécessaire pour entraîner en
rotation la vis en régime établi.

Les liaisons sont supposées parfaites et R~0~ (repère lié au bâti) est
supposé galiléen.

Les extraits des catalogues constructeurs donnent les informations
suivantes :

Moteur utilisé : M1SD4

![](11-Actions Mécaniques/Cours/pandoc/media/image476.emf){width="5.913385826771654in"
height="1.977419072615923in"}Réducteur utilisé : C112_12.1 S1 M1SD4

![](11-Actions Mécaniques/Cours/pandoc/media/image477.emf){width="6.120433070866142in"
height="5.217569991251094in"}

**Figure 2 : extraits catalogues moteurs asynchrones et réducteurs**

**Sachant que la référence du moteur est M1SD4, donner la puissance du
moteur P~m~, sa fréquence de rotation n, le moment d'inertie du moteur
J~m~, en indiquant à chaque fois les unités.**

**Quel est le rapport de transmission du réducteur**
![](11-Actions Mécaniques/Cours/pandoc/media/image478.emf)** ? En
déduire le rapport de réduction**
![](11-Actions Mécaniques/Cours/pandoc/media/image479.emf)**.**

Une modélisation effectuée sur un logiciel (modeleur volumique) a permis
de calculer le moment d'inertie de la vis d'Archimède : J~v~ = 6.10^-6^
kg.m^2^.

On donne le moment d'inertie du réducteur ramené sur l'arbre moteur :
J~red~ = 1,9 10^-4^ kg.m^2^.

**Etude de la précision de la quantité de granulés acheminée dans la
trémie de stockage :**

Entre l'instant de la coupure de l'alimentation du moteur et celui de
l'arrêt complet de la vis, cette dernière a tourné d'un angle
![](11-Actions Mécaniques/Cours/pandoc/media/image480.emf) et l'arbre
moteur d'un angle
![](11-Actions Mécaniques/Cours/pandoc/media/image481.emf).

**Donner la relation entre**
![](11-Actions Mécaniques/Cours/pandoc/media/image482.emf) **et**
![](11-Actions Mécaniques/Cours/pandoc/media/image483.emf)**.**

**En régime établi, donner une relation entre C~r~, P~m~ et ω~m~ .**

**En isolant le système Σ = {moteur ; réducteur ; vis}, donner
l'expression de l'énergie cinétique T(Σ /R~0~) du système dans son
mouvement par rapport au bâti.**

-   **Mettre cette expression sous la forme**
    ![](11-Actions Mécaniques/Cours/pandoc/media/image484.emf)**. Donner
    la valeur numérique de J~eq~.**

-   **En utilisant le théorème d'énergie-puissance sous forme intégrée
    entre la coupure de l'alimentation et l'arrêt de la vis, donner
    l'expression littérale de**
    ![](11-Actions Mécaniques/Cours/pandoc/media/image485.emf)**.**

**En considérant qu'on achemine 2 kg de granulés de la vis d'Archimède à
la trémie de stockage, quelle précision (en %) a-t-on sur ce dosage ?
Quel paramètre devrait-on modifier pour diminuer ce pourcentage ?**

![](11-Actions Mécaniques/Cours/pandoc/media/image486.emf){width="1.4083333333333334in"
height="0.7318066491688539in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**Autofocus**

*([Source]{.underline} : Centrale Supélec 2019)*

![](11-Actions Mécaniques/Cours/pandoc/media/image487.png){width="5.460416666666666in"
height="3.2868055555555555in"}**Mise en situation**

Le dispositif permettant de mouvoir la lentille mobile ainsi que toutes
ses caractéristiques sont données ci-dessous.

**Hypothèses et notations**

-   Les seules masses et inertie à prendre en compte sont :

    -   la masse de la lentille notée M ;

    -   l'inertie de la lentille autour de son axe de rotation notée I ;

    -   l'inertie de la MCC autour de son axe de rotation notée I~m~.

-   les seules actions mécaniques à prendre en compte sont :

```{=html}
<!-- -->
```
-   l'action de la MCC sur la poulie motrice
    > $\left\{ T_{mot \rightarrow poulie} \right\} = \begin{Bmatrix}
    > 0 & 0 \\
    > 0 & 0 \\
    > 0 & C_{m}
    > \end{Bmatrix}_{{\overrightarrow{x}}_{0},{\overrightarrow{y}}_{0},{\overrightarrow{z}}_{0}}\ $;

-   l'action des frottements secs ramenés sur la poulie motrice
    > $\left\{ T_{Cr \rightarrow poulie} \right\} = \begin{Bmatrix}
    > 0 & 0 \\
    > 0 & 0 \\
    > 0 & {- C}_{0}
    > \end{Bmatrix}_{{\overrightarrow{x}}_{0},{\overrightarrow{y}}_{0},{\overrightarrow{z}}_{0}}\ $;

-   l'action des frottements fluides ramenés sur la poulie motrice
    > $\left\{ T_{f \rightarrow poulie} \right\} = \begin{Bmatrix}
    > 0 & 0 \\
    > 0 & 0 \\
    > 0 & {- f\omega}_{m}
    > \end{Bmatrix}_{{\overrightarrow{x}}_{0},{\overrightarrow{y}}_{0},{\overrightarrow{z}}_{0}}\ $;

-   l'action de la pesanteur est négligée.

```{=html}
<!-- -->
```
-   Les mouvements sont :$\left\{ V_{mot/0} \right\} = \begin{Bmatrix}
    0 & 0 \\
    0 & 0 \\
    \omega_{m} & 0
    \end{Bmatrix}_{{\overrightarrow{x}}_{0},{\overrightarrow{y}}_{0},{\overrightarrow{z}}_{0}}$ ; 
    et $\left\{ V_{lentille/0} \right\} = \begin{Bmatrix}
    0 & 0 \\
    0 & 0 \\
    \omega_{l} & V_{l}
    \end{Bmatrix}_{{\overrightarrow{x}}_{0},{\overrightarrow{y}}_{0},{\overrightarrow{z}}_{0}}$

> Le rapport de réduction est donné par :
> $k = \frac{\omega_{l}}{\omega_{m}} = \frac{r\phi_{1}}{\phi_{2}} = - \frac{Z_{3} \cdot Z_{7} \cdot Z_{9} \cdot Z_{11} \cdot Z_{14}}{Z_{6} \cdot Z_{8} \cdot Z_{10} \cdot Z_{13} \cdot Z_{15}} \cdot \frac{\phi_{1}}{\phi_{2}} = - 0,00188$

1.  Donner l'expression de l'inertie équivalente ramenée sur l'arbre de
    la MCC qui sera notée J.

2.  En utilisant le théorème de l'énergie cinétique, montrer que
    l'équation de mouvement s'écrit :

> $C_{m} = J\frac{d\omega_{m}}{dt} + C_{0} + f{.\omega}_{m}$

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**Spiralift**

*([Source]{.underline} : ATS 2017)*

![](11-Actions Mécaniques/Cours/pandoc/media/image488.png){width="5.646187664041995in"
height="2.6990135608048993in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image489.png){width="6.794511154855643in"
height="3.9107720909886265in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image490.png){width="7.25in"
height="5.854166666666667in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image491.png){width="7.268055555555556in"
height="2.5527777777777776in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image492.png){width="6.642145669291339in"
height="4.734417104111986in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image493.png){width="6.54461176727909in"
height="0.8685597112860892in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**MPLS**

*([Source]{.underline} : ATS 2016)*

La société Sonaréma-Fondex assemble, conditionne et diffuse des réchauds
à gaz portables de grande puissance. Ces réchauds sont conditionnés et
vendus en cartons. Depuis peu, l\'ouverture de la société à de nouveaux
marchés impose d\'accroître le rythme de la distribution. Dans ce
nouveau contexte, la société a besoin de palettiser ces cartons afin de
les acheminer vers ses principaux distributeurs.

+-----------------------------------+-----------------------------------+
| ![Réchaud.jpg](11-Actions Mécaniq | !                                 |
| ues/Cours/pandoc/media/image494.j | [DSC_0372.jpg](11-Actions Mécaniq |
| peg){width="2.2333770778652666in" | ues/Cours/pandoc/media/image495.j |
| height="1.9065627734033246in"}    | peg){width="2.6668143044619423in" |
|                                   | height="1.5281332020997376in"}    |
| Fig.1 : modèles de réchauds       |                                   |
| trépied                           | Fig.2 : réchaud emballé dans son  |
|                                   | carton                            |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

La société possède pour le conditionnement de cartons un système
automatisé commercialisé sous l\'acronyme MLPS pour Multi Level
Packaging System. Elle envisage d\'utiliser ce système pour satisfaire
ce nouveau besoin.

**IV.3. Validation du moteur assurant la translation du préhenseur**

[Objectif :]{.underline} vérifier que le couple du moteur de translation
existant est compatible avec les exigences de vitesse et d\'accélération
imposées.

Le mouvement de translation du préhenseur est obtenu à partir d\'un
motoréducteur et d\'un système poulie-courroie.

Pour la suite du problème, nous retiendrons la valeur **V=0,86 m.s^-1^**
pour la vitesse de translation du préhenseur.

Fig.17 : vue de principe de la motorisation de l\'unité en U

Dans le tableau ci-après sont rassemblées les différentes
caractéristiques et notations de la chaîne d\'énergie pour la fonction
\"déplacer en translation le préhenseur\".

+----------------------------------+-----------------------------------+
| **Eléments**                     | **Caractéristique et notation**   |
+==================================+===================================+
| Alimentation                     | Monophasée 230V / 50Hz            |
+----------------------------------+-----------------------------------+
| Moteur                           | Couple mécanique: C~m~            |
|                                  |                                   |
|                                  | Vitesse de rotation : Ω~m~        |
|                                  |                                   |
|                                  | Inertie arbre moteur : J~m~ =     |
|                                  | 83\*$10^{- 6}$ kg.m²              |
+----------------------------------+-----------------------------------+
| Réducteur                        | Inertie réducteur négligée        |
|                                  |                                   |
|                                  | Rapport de réduction : r =        |
|                                  | 1/11,83                           |
+----------------------------------+-----------------------------------+
| Poulie motrice                   | Inertie poulie motrice négligée   |
|                                  |                                   |
|                                  | Vitesse de rotation : Ω~p~        |
|                                  |                                   |
|                                  | Diamètre D = 100 mm               |
+----------------------------------+-----------------------------------+
| Courroie                         | Inertie négligée                  |
+----------------------------------+-----------------------------------+
| Poulie de renvoi                 | Inertie poulie motrice négligée   |
+----------------------------------+-----------------------------------+
| Préhenseur                       | Masse M = 1,2 kg                  |
|                                  |                                   |
|                                  | Vitesse de translation V=0,86     |
|                                  | m.s^-1^                           |
+----------------------------------+-----------------------------------+
| Carton                           | Masse m = 8 kg                    |
+----------------------------------+-----------------------------------+
| Frein                            | Inertie frein moteur ramenée sur  |
|                                  | l\'arbre moteur : J~f~ =          |
|                                  | 35\*$10^{- 6}$ kg.m²              |
+----------------------------------+-----------------------------------+

Tableau 1 : caractéristiques des éléments constitutifs de la chaîne
d\'énergie

Q12 Déterminer la vitesse de rotation de la poulie Ω~p~, puis celle du
moteur Ω~m~.

On appelle E l\'ensemble {rotor + frein + réducteur + poulie motrice +
courroie + poulie de renvoi + préhenseur + carton}.

Q13 Déterminer l\'expression de l\'énergie cinétique de l\'ensemble E
par rapport au bâti.

Q14 En déduire le moment d\'inertie équivalent J~eq~ de l\'ensemble E
ramené sur l\'arbre moteur.

[Hypothèses:]{.underline}

-   il y a glissement entre le préhenseur et le bâti

-   on note f le coefficient de frottement préhenseur/bâti. On prendra
    **f = 0,1**

-   les autres liaisons du mécanisme sont supposées parfaites

-   l\'accélération de la pesanteur **g = 10 m.s^-2^**.

Q15 En appliquant le théorème de l\'énergie cinétique à l\'ensemble E
dans son mouvement par rapport au bâti, déterminer une relation entre
l\'accélération angulaire ${\dot{\mathrm{\Omega}}}_{m}$ et le couple
mécanique C~m~.

Mettre cette relation sous la forme :
$J_{eq}*{\dot{\mathrm{\Omega}}}_{m} = C_{m} - C_{req}$ puis exprimer
C~req~ en fonction de m, M, f, D, r et g.

Faire l\'application numérique.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**Fauteuil dynamique de cinéma**

*([Source]{.underline} : CCS TSI 2015)*

Ce concept a été inventé au Canada en 2008, et s'est étendu à toute
l'Amérique du Nord avant de traverser l'Atlantique pour proposer un
cinéma dynamique avec une quantité d'effets spéciaux et spatiaux. Le
fauteuil dynamique de cinéma est principalement destiné à l'industrie du
divertissement et de la simulation. Un train filant à vive allure, une
poursuite à moto ou en avion de chasse dans un canyon, autant de scènes
fréquentes dans le cinéma d'action du xxie siècle. Pour ressentir au
mieux ces sensations, la technologie permet désormais de ressentir dans
son fauteuil les différents mouvements, par de fortes vibrations et
accélérations. Ce système repose sur la post-synchronisation des films.
Comme pour un doublage ou un sous-titrage, les mouvements du film sont
transmis au fauteuil. Le fauteuil dynamique permet de compléter la
palette sensorielle offerte au spectateur afin d'accroitre le réalisme
de son environnement. Les mouvements qui en résultent sont parfaitement
synchronisés avec le visuel à l'écran, créant ainsi une expérience
immersive d'un grand réalisme. Si la plate-forme à six degrés de liberté
s'est imposée dans le cas des simulateurs de vols, elle ne répond pas
aux exigences plus étendues des fauteuils dynamiques. Des solutions
spécifiques à un environnement de simulation aussi réaliste que possible
nécessitent le recours à un système de restitution des mouvements. Le
système étudié est une évolution en cours d'étude des fauteuils
dynamiques actuellement commercialisés, qui s'inspire des sièges
dynamiques utilisés pour l'entrainement des pilotes d'avion de chasse
(voir figure 1).

+--------------------+-------------------------------------------------+
| ![](11-Actions     | ![](11-Actions Mécaniques/Cours/pandoc/         |
| Mécaniques/Cours/p | media/image497.png){width="4.368465660542432in" |
| andoc/media/image4 | height="1.4534481627296587in"}                  |
| 96.png){width="1.5 |                                                 |
| 778794838145231in" | Publicité annonçant l'évolution des fauteuils   |
| height="1.95       | dynamiques                                      |
| 62018810148731in"} |                                                 |
|                    |                                                 |
| Fauteuil dynamique |                                                 |
| de cinéma          |                                                 |
| actuellement       |                                                 |
| commercialisé      |                                                 |
+====================+=================================================+
| ![](11-Actions     |                                                 |
|  Mécaniques/Cours/ |                                                 |
| pandoc/media/image |                                                 |
| 498.png){width="5. |                                                 |
| 644783464566929in" |                                                 |
| height="2.2        |                                                 |
| 12062554680665in"} |                                                 |
|                    |                                                 |
| Sièges dynamiques  |                                                 |
| de différents      |                                                 |
| constructeurs      |                                                 |
| mondiaux pour      |                                                 |
| l'entrainement des |                                                 |
| pilotes d'avion de |                                                 |
| chasse             |                                                 |
|                    |                                                 |
| **Figure 1**       |                                                 |
+--------------------+-------------------------------------------------+

***II.F -- Validation du dimensionnement du moteur du dosseret***

**Objectif**

Justifier le choix du moteur à courant continu et de son variateur
associé utilisé pour entrainer le dosseret du siège dynamique (figures 7
et 8).

Ces calculs visent à déterminer l'équation dynamique qui permet
d'obtenir le couple moteur en fonction des caractéristiques
géométriques, massiques et inertielles des pièces ainsi que des
conditions d'utilisation.

**II.F.1) Détermination du couple à la sortie du réducteur** 𝐶*~red~*

Hypothèses :

− toutes les liaisons sont supposées parfaites ;

− la masse du maneton est négligée ;

− la masse de la bielle est négligée ;

− le dosseret est assimilé à une plaque rectangulaire homogène
d'épaisseur négligeable ;

− l'effort exercé au point 𝐷 par la tête du spectateur sur le dosseret,
reste normal à la surface de contact ;

− l'accélération normale du dosseret est négligeable devant
l'accélération tangentielle de celui-ci.

Données :

− accélération maximale de la tête au point 𝐷, 𝑎~max~ = 7 m⋅s^−2^ ;

− effort (en newtons),
${\overrightarrow{F}}_{tête \rightarrow dosseret} = - 40.{\overrightarrow{x}'}_{4}$ ;

− rayon 𝐶𝐷 = 𝑞 = 85 mm ;

− distance de l'axe de rotation du dosseret au centre d'inertie de la
plaque, 𝐶𝐺 = 62 mm ;

− masse du dosseret, 𝑀*~d~* = 0,900 kg ;

− la matrice d'inertie de la plaque rectangulaire en 𝐺, centre de la
plaque, est donnée figure 18.

![](11-Actions Mécaniques/Cours/pandoc/media/image499.png){width="6.3in"
height="1.6255686789151356in"}

**Figure 18** Données concernant le dosseret

Afin de déterminer le couple moteur maximal 𝐶*~M~* , on propose
d'appliquer le théorème de l'énergie cinétique au système isolé 𝐸 =
{dosseret + bielle + maneton} en mouvement par rapport au châssis dont
le repère associé est supposé galiléen.

Pour un déplacement du dosseret qui entraine la tête du spectateur vers
l'avant :

1.  Déterminer l'expression littérale de l'énergie cinétique du système
    isolé 𝐸 par rapport au repère lié au sol supposé Galiléen, en
    fonction des différents paramètres.

2.  Appliquer le théorème de l'énergie cinétique au système isolé 𝐸 pour
    déterminer l'expression littérale du couple 𝐶*~red~* exercé par
    l'arbre de sortie du réducteur sur le dosseret.

3.  Calculer numériquement ce couple 𝐶*~red~*.

**II.F.2) Détermination du couple moteur**

Hypothèses :

− le réducteur a un facteur de perte estimé à 𝜂 = 0,9 ;

− le moment d'inertie des éléments mobiles du réducteur ramené à l'arbre
du moteur est négligé ;

− les liaisons (autres que celles dans le réducteur) sont supposées
parfaites.

Données :

− rapport de transmission du réducteur, 𝑟 = 1/50 ;

− moment d'inertie du rotor du moteur, 𝐽*~M~* = 15 × 10−5 kg.m².

4.  En appliquant le principe fondamental de la dynamique à l'arbre du
    moteur, calculer le couple moteur 𝐶*~M~* pour cette phase
    d'accélération.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**AEROGENERATEUR**

*([Source]{.underline} : ATS 2003, Jacques Le Goff)*

**Mise en situation**

![](11-Actions Mécaniques/Cours/pandoc/media/image500.png){width="4.179166666666666in"
height="1.875in"}Pour des raisons de sécurité, on choisit d\'intégrer un
dispositif de freinage d\'urgence. Ce dispositif peut notamment être
activé si un corps étranger percute une pale au point de l\'endommager
et de créer un « balourd ». Par soucis de simplification, on supposera
dans cette partie que la le multiplicateur et la génératrice sont
désaccouplées.

Avant d\'installer le frein, on s\'intéresse au risque de balourd du
rotor afin d\'en quantifier les effets. Le modèle d\'étude, représentant
l'ensemble (SE1) composé des éléments tournants associés au rotor et au
dispositif de régulation, est celui proposé sur la figure suivante :

![](11-Actions Mécaniques/Cours/pandoc/media/image501.png){width="2.841666666666667in"
height="2.6041666666666665in"}

**[Données et paramétrage :]{.underline}**

-   La liaison pivot est supposée parfaite ;

-   Le repère
    ![](11-Actions Mécaniques/Cours/pandoc/media/image502.wmf)lié au
    bâti de l'éolienne **[0]{.underline}** est galiléen ;

-   Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image503.wmf)
    est lié à l'ensemble tournant **[SE1]{.underline}** ;

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image504.wmf) est la
    masse de l'ensemble tournant **[SE1]{.underline}** ;

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image505.wmf) est
    l'angle paramétrant la position de l'ensemble **[SE1]{.underline}**
    dans son mouvement de rotation par rapport à **[0]{.underline}**.

-   L'action motrice du vent sur **[SE1]{.underline}** est modélisée en
    > H centre d'inertie de **[SE1]{.underline}**, par le torseur :
    > ![](11-Actions Mécaniques/Cours/pandoc/media/image506.wmf)

```{=html}
<!-- -->
```
-   Matrice d'inertie de l'ensemble **[SE1]{.underline}** :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image507.wmf)

-   Torseur, en H, des actions mécaniques transmissibles par la liaison
    pivot entre **[0]{.underline}** et **[SE1]{.underline}** noté :

> ![](11-Actions Mécaniques/Cours/pandoc/media/image508.wmf)

![](11-Actions Mécaniques/Cours/pandoc/media/image509.png){width="4.429166666666666in"
height="2.2104166666666667in"}![](11-Actions Mécaniques/Cours/pandoc/media/image510.png){width="4.739583333333333in"
height="1.6041666666666667in"}Le dispositif de freinage retenu est un
frein à disque composé d\'un disque **[d]{.underline}** et de deux
étriers. Par soucis de simplification, le frein est placé en sortie de
**[SE1]{.underline}** et découplé de **[SE2]{.underline}**. Le freinage
est réalisé par pression des garnitures d\'usure assurant le serrage de
part et d\'autre du disque. Chaque étrier supporte deux garnitures (une
de chaque côté du disque) pour lesquelles la surface de contact est
représentée en gris sur les figures ci-dessous :

L'action de freinage est modélisée par un couple pur
![](11-Actions Mécaniques/Cours/pandoc/media/image511.wmf)
avec ![](11-Actions Mécaniques/Cours/pandoc/media/image512.wmf).

**Dimensionnement du frein d'urgence**

1.   **Etablir**, dans le repère
    ![](11-Actions Mécaniques/Cours/pandoc/media/image513.wmf), la forme
    de la matrice
    ![](11-Actions Mécaniques/Cours/pandoc/media/image514.wmf) du
    disque, en supposant que celui-ci est parfaitement équilibré.

2.   **Etablir,** par application du théorème de l'énergie cinétique à
    l\'ensemble tournant {(SE1)+(d)}, l\'équation du mouvement de cet
    ensemble.

Pour simplifier l'étude, on suppose que l'action motrice du vent sur
**[SE1]{.underline}** est modélisée en A par le torseur :

![](11-Actions Mécaniques/Cours/pandoc/media/image515.wmf)

L'action de freinage est modélisée par un couple pur
![](11-Actions Mécaniques/Cours/pandoc/media/image511.wmf)
avec ![](11-Actions Mécaniques/Cours/pandoc/media/image512.wmf).

3.  **Déterminer** l'intensité du couple de freinage
    ![](11-Actions Mécaniques/Cours/pandoc/media/image516.wmf)constant à
    exercer pour immobiliser en 10 secondes l'esemble tourant à une
    vitesse de 215 tr/min. On utilisera les valeurs suivnates :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image517.wmf) et
    ![](11-Actions Mécaniques/Cours/pandoc/media/image518.wmf).

4.   **En deduire** la valeur de la pression p nécéssaire au dispositif
    de freinage. On prendra :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image519.wmf),
    ![](11-Actions Mécaniques/Cours/pandoc/media/image520.wmf),
    ![](11-Actions Mécaniques/Cours/pandoc/media/image521.wmf) et
    ![](11-Actions Mécaniques/Cours/pandoc/media/image522.wmf).

![](11-Actions Mécaniques/Cours/pandoc/media/image523.jpeg){width="2.0388888888888888in"
height="2.439583333333333in"}**Laveuse autoportée**

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source]{.underline} : ATS 2015)*

Présentation de la laveuse

La société Nilfisk propose une large gamme d'engins de nettoyage des
sols. Celle des laveuses autoportées répond aux besoins de lavage pour
des surfaces de plusieurs milliers de km carrés. C'est par exemple le
cas des sols de super et hyper-marché. Les qualités de ces machines
résident dans leur sécurité d'usage, leur faible nuisance sur
l'environnement, leur autonomie et leur maniabilité. Cette maniabilité
impose des encombrements minimisés en largeur et des rayons de giration
très faibles.

![chariot00](11-Actions Mécaniques/Cours/pandoc/media/image524.jpeg){width="1.9472222222222222in"
height="2.0479166666666666in"}Le modèle étudié dans ce sujet est la
laveuse BR 752 dont la structure du châssis à trois roues est
privilégiée pour autoriser des rayons de giration très petits. Sur la
gamme actuelle, la motorisation est assurée par la roue avant avec une
machine à courant continu. Une évolution est envisagée qui conduirait à
remplacer la motorisation avant par deux moteurs à l'arrière non
orientables mais commandés en vitesse. Cette modification doit *a
minima* maintenir les performances de la solution existante.

Ce sujet a pour but d'analyser les différentes performances de la
nouvelle laveuse et de justifier les solutions technologiques utilisées.
Pour cela, il est demandé de :

-   valider le critère de sécurité lors d'un freinage d'urgence lors du
    > déchargement ;

-   proposer une loi de commande des moteurs à partir de la cinématique
    > de la laveuse ;

-   valider une solution technologique numérique pour la loi de
    > commande ;

-   dimensionner des éléments de la chaîne d'acquisition de la vitesse
    > de rotation des roues ;

-   dimensionner et valider le choix des moteurs ;

-   concevoir une solution d'asservissement en vitesse des moteurs.

**L'objectif de cette partie est de déterminer les caractéristiques des
moteurs qui propulseront la laveuse, et de valider le choix de
celui-ci.**

Pour dimensionner les moteurs, on se place dans les conditions les plus
défavorables, c'est-à-dire pendant le lavage dans une montée de pente
maximale de 6 % (soit un angle
![](11-Actions Mécaniques/Cours/pandoc/media/image525.wmf)) et en phase
d'accélération. On ne négligera plus les inerties des roues et des
rotors moteurs et on prendra en compte le frottement de roulement et le
frottement des éléments lavant.

**Données**

-   masse du véhicule et du conducteur :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image526.wmf) = 500
    kg ;

```{=html}
<!-- -->
```
-   chaque moteur fournit le même couple
    ![](11-Actions Mécaniques/Cours/pandoc/media/image527.wmf), dans
    cette partie, on considère donc qu'il y a un seul moteur qui fournit
    un couple
    ![](11-Actions Mécaniques/Cours/pandoc/media/image528.wmf) ;

```{=html}
<!-- -->
```
-   vitesse maximale du véhicule en mode lavage :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image529.wmf) = 3
    km/h ;

-   vitesse de rotation du moteur :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image530.wmf),
    (![](11-Actions Mécaniques/Cours/pandoc/media/image531.wmf)pour le
    moteur gauche et
    ![](11-Actions Mécaniques/Cours/pandoc/media/image532.wmf)pour le
    moteur droit), car la laveuse avance en ligne droite dans cette
    partie ;

-   vitesse de rotation de l'arbre à la sortie du réducteur :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image533.wmf) ;

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image534.png){width="1.882638888888889in"
    height="2.0055555555555555in"}rapport de réduction du réducteur :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image535.wmf) ;

-   vitesse de rotation de la roue arrière gauche d'axe
    ![](11-Actions Mécaniques/Cours/pandoc/media/image536.wmf) :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image537.wmf) (ligne
    droite) ;

-   vitesse de rotation de la roue arrière droite d'axe
    ![](11-Actions Mécaniques/Cours/pandoc/media/image538.wmf) :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image539.wmf) (ligne
    droite) ;

-   moment d'inertie des roues avant, arrière droite et gauche autour de
    leur axe :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image540.wmf) ;

-   moment d'inertie du rotor du moteur autour de son axe :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image541.wmf) ;

-   rendement global de la chaîne de transmission :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image542.wmf) ;

-   rayon de la roue arrière motrice :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image543.wmf) = 0,15
    m ;

-   intensité de l'effort axial de frottement sec (Loi de Coulomb) dû
    aux frottements des brosses et de la raclette sur le sol :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image544.wmf)* *;

-   intensité de l'effort axial de frottement de roulement :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image545.wmf) avec
    ![](11-Actions Mécaniques/Cours/pandoc/media/image546.wmf) (voir
    figure 15) ;

-   on considérera que la roue avant roule sans glisser sur le sol.

**Q25. Exprimer**
![](11-Actions Mécaniques/Cours/pandoc/media/image547.wmf) en fonction
![](11-Actions Mécaniques/Cours/pandoc/media/image548.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image549.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image550.wmf).

**Q26. Exprimer** en fonction de
![](11-Actions Mécaniques/Cours/pandoc/media/image551.wmf) l'énergie
cinétique, dans son mouvement par rapport à
![](11-Actions Mécaniques/Cours/pandoc/media/image552.wmf) :

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image553.wmf), du
    châssis de la laveuse avec le conducteur ;

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image554.wmf), du rotor
    de l'arbre moteur ;

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image555.wmf), des
    trois roues de la laveuse ;

L'énergie cinétique des autres éléments dans leur mouvement par rapport
à ![](11-Actions Mécaniques/Cours/pandoc/media/image556.wmf) est
négligée.

**Q27. Exprimer** l'inertie équivalente
![](11-Actions Mécaniques/Cours/pandoc/media/image557.wmf)de l'ensemble,
ramenée sur l'arbre moteur.

**Q28.** **Écrire** le théorème de l'énergie cinétique appliqué au
véhicule complet.

**Q29. Exprimer** le couple moteur
![](11-Actions Mécaniques/Cours/pandoc/media/image558.wmf)en fonction de
![](11-Actions Mécaniques/Cours/pandoc/media/image559.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image560.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image561.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image562.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image563.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image564.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image565.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image566.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image567.wmf),
![](11-Actions Mécaniques/Cours/pandoc/media/image568.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image569.wmf). **Réaliser**
l'application numérique en considérant que la vitesse maximale est
atteinte en 5 s.

**Q30.** Les caractéristiques techniques du moteur préconisé par le
constructeur sont présentées dans l'annexe 4. À partir des résultats
obtenus aux questions précédentes, **justifier** que le moteur choisi
est bien adapté.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**TRAMWAY DE STRASBOURG**

*([Source]{.underline} : Concours 3^ème^ année ENS Cachan 2002)*

**Mise en situation**

Une rame de ce tramway est composée de trois voitures, supportées par
quatre bogies de quatre roues. Trois de ces bogies sont moteurs et sont
motorisés sur chacune des quatre roues : la motorisation totale d\'une
rame est donc assurée par douze moteurs. La puissance d'un moteur est
transmise à une roue par un réducteur (figure 2).

![](11-Actions Mécaniques/Cours/pandoc/media/image570.jpeg){width="2.2641502624671914in"
height="1.5728521434820648in"}

[Notations :]{.underline}

$\overrightarrow{V}$(rame/sol) = V.x : Vitesse de la rame par rapport au
sol (m/s)

$\overrightarrow{\mathrm{\Omega}}$(rotor/rame) = ω~mot~.z : Vitesse de
rotation d\'un moteur par rapport à la rame (rad/s)

$\overrightarrow{M}$(O~mot~,stator→rotor) = C~mot~.z : Couple exercé par
le stator d'un moteur sur son rotor et exprimé en un point de l'axe du
moteur considéré (N.m)

$\overrightarrow{\mathrm{\Omega}}$(roue/sol) = ω~roue~.z : Vitesse de
rotation d\'une roue par rapport au sol (rad/s)

$\overrightarrow{M}$(O~roue~,red→roue) = C~roue~.z : Couple exercé par
l'arbre de sortie d'un réducteur sur une roue motrice et exprimé en un
point de l'axe de la roue considérée (N.m)

g = 9,81 m.s^-2^ : Accélération de la pesanteur

[Hypothèses de modélisation :]{.underline}

Pour réaliser cette étude, nous considérerons :

-   La résistance au roulement, est répartie de façon égale sur toutes
    les roues, et modélisée par une force notée F~1~ telle que :

Norme :
$F_{1} = \left\| {\overrightarrow{F}}_{rail \rightarrow rame}^{} \right\| = e.M.g$
avec e coefficient de résistance au roulement

Direction : Parallèle au déplacement du tramway

-   La résistance à l\'avancement dans l\'air, est répartie sur toutes
    les roues motrices, et modélisée par une force notée F~2~ telle que
    :

> Norme :
> $F_{2} = \left\| {\overrightarrow{F}}_{air \rightarrow rame}^{} \right\| = k.V$
> avec k coefficient de pénétration dans l'air (qui constitue une
> linéarisation du modèle d'écoulement ½.ρ.S.C~x~.V^2^)

Direction : Parallèle au déplacement du tramway

-   Le roulement de chacune des roues s\'effectue sans glissement

    **Travail demandé**

**1.** **Compléter** le tableau suivant :

  -----------------------------------------------------------------------
  Pour une rame, combien y'a-t-il de :               
  -------------------------------------------------- --------------------
  Voitures                                           

  Bogies                                             

  Roues                                              

  Moteurs                                            

  Réducteurs                                         
  -----------------------------------------------------------------------

**2. Déterminer** l'énergie cinétique de la rame dans son mouvement par
rapport au sol. **Exprimer** cette grandeur en fonction de ω~mot~. **En
déduire** le moment d'inertie équivalent ramené à l'arbre [d'un
seul]{.underline} moteur J~eq~.

**3.** Lorsque le tramway se déplace dans le sens des x positif (V \> 0)
quel est le signe de la vitesse de rotation du moteur (ω~mot~) ?

[Objectif :]{.underline}

Vérifier que ce tramway est capable d'atteindre la vitesse maximale de
service.

Pour la suite du problème :

-   On prendra J~eq~ = 3,55 kg.m^2^ (inertie équivalente de la rame
    complète ramenée sur l'arbre d'un seul moteur)

-   On supposera toutes les liaisons parfaites (à l'exception du contact
    avec frottement roue / rail)

-   Pour les questions 4 et 5, on supposera que le tramway se déplace
    sur une voie parfaitement horizontale

**4.** En appliquant le théorème de l'énergie puissance à la rame
complète, **déterminer** la relation liant ω~mot~,
${\dot{\omega}}_{mot}$ et C~mot~.

**5.** A partir de la question précédente, en régime permanent,
**établir** la relation entre le couple moteur et la vitesse de rotation
du moteur. **Tracer** cette caractéristique sur le document réponse,
**en déduire** la vitesse de la rame en régime établi. **Conclure**

[Objectif :]{.underline}

Vérifier que le tramway étudié est capable de franchir la pente donnée
dans le cahier des charges.

Pour la suite du problème, on suppose qu'il existe une petite pente sur
le trajet. Celle-ci s'exprime par une valeur p%. On rappelle que l'angle
α correspondant à p% s'exprime par $\tan\alpha = \frac{p}{100}$

**6.** En considérant la rame complète, **déterminer** la puissance
développée par le poids

**7.** En reprenant l'étude de la question 4, **déterminer** la pente
maximale p~max~ que le tramway peut franchir. **Conclure**

**Annexe : Caractéristiques générales du système**

  -----------------------------------------------------------------------
  ***Caractéristiques générales du        
  tramway :***                            
  --------------------------------------- -------------------------------
  Longueur de la rame                     33,10 m

  Largeur de la rame                      2,4 m

  Hauteur de la rame                      3,10 m

  Masse à vide                            40 t

  Masse totale en fonctionnement          M = 60 t

  Nombre de places                        290 (dont 66 places assises)

  ***Performances attendues :***          

  Vitesse maximale en service             60 km/h

  Pente franchissable                     5 %

  ***Informations techniques              
  supplémentaires :***                    

  Diamètre d\'une roue (neuve)            D = 0,52 m

  Moment d\'inertie d\'une roue par       J~roue~ = 4,3 kg.m²
  rapport à son axe de rotation           

  Coefficient de frottement roue/rail     λ = 0,1
  (acier/acier)                           

  Coefficient de résistance au roulement  e = 0,01

  Coefficient de pénétration dans l\'air  k = 50 N.m^-1^.s

  Rapport de réduction du réducteur       r = 0,1

  Rendement du réducteur                  η = 0,8

  Puissance d\'un moteur                  P = 25 kW

  Moment d\'inertie d\'un rotor par       J~mot~ = 0,11 kg.m²
  rapport à son axe de rotation           

  Moment d\'inertie du réducteur          J~red~ négligé
  -----------------------------------------------------------------------

**Document réponse**

![](11-Actions Mécaniques/Cours/pandoc/media/image571.png){width="5.682200349956256in"
height="4.383333333333334in"}

##  PFD

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**VAG**

*([Source]{.underline} : ATS 2014)*

**PRESENTATION DU SYSTEME**

Le nouveau Centre Hospitalier Universitaire (CHU) de Dijon Bocage
Central a retenu pour sa logistique hôtelière hospitalière des VAG
(véhicule auto guidé) ou AGV (Automated guided vehicle). Neuf véhicules
autonomes à guidage laser (**Figure 3**) sont utilisés pour le transport
de déchets, plateaux repas, linges dans les parties non accessibles au
public (**Figure 4**). Le nombre de transports quotidiens par VAG est de
l'ordre de 930. Chaque transport est désigné sous le terme de mission.

  -----------------------------------------------------------------------------------------------------------------------------------------
  ![](11-Actions Mécaniques/Cours/pandoc/media/image572.emf){width="2.575in"   ![](11-Actions Mécaniques/Cours/pandoc/media/image573.png)
  height="1.925in"}                                                            
  ---------------------------------------------------------------------------- ------------------------------------------------------------
  **Figure 3 **VAG seul                                                        **Figure 4 **VAG déplaçant un chariot

  -----------------------------------------------------------------------------------------------------------------------------------------

**Partie 1 : étude de la fonction technique FT11 : « Assurer
l'avancement ».**

> **Les objectifs de cette partie sont les suivants:**

-   **Rechercher l'accélération linéaire maximale du VAG afin d'assurer
    le critère de non basculement du chariot et le non dérapage du VAG**

![](11-Actions Mécaniques/Cours/pandoc/media/image574.emf){width="4.016666666666667in"
height="4.030555555555556in"}Dans cette partie, le VAG est en
translation rectiligne, c\'est-à-dire que les roues directrices (roue
motrice et roue avant) ont la même orientation que les roues latérales
(voir schéma cinématique). Le VAG, dans cette configuration est modélisé
**Figure 5**.

La zone de contact entre le VAG et le chariot est de type surfacique,
délimitée par deux rectangles formés par des bandes rugueuses empêchant
le glissement du chariot par rapport au VAG, comme le montre la **Figure
3**.

Le coefficient d'adhérence entre le VAG et le chariot est suffisamment
grand pour que ce dernier ne puisse pas glisser par rapport au VAG,
quelle que soit son accélération. Par contre, en phase d'accélération
(respectivement en phase de décélération), le chariot peut basculer
autour de l'axe
![](11-Actions Mécaniques/Cours/pandoc/media/image575.wmf)
(respectivement
![](11-Actions Mécaniques/Cours/pandoc/media/image576.wmf){width="0.35833333333333334in"
height="0.3333333333333333in"} ), comme le montre la **Figure 6**.

![](11-Actions Mécaniques/Cours/pandoc/media/image577.emf){width="5.675in"
height="2.85in"}

**Figure 6** Basculements possibles du chariot

**Hypothèses, paramétrage et notations :**

+-------------------------+--------+----------------------------------+---+
| **Hypothèses**          |        |                                  |   |
+=========================+========+==================================+===+
| Les solides sont        |        |                                  |   |
| indéformables           |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Modélisation plane      |        |                                  |   |
| adoptée de l'ensemble   |        |                                  |   |
| Chariot+ VAG dans le    |        |                                  |   |
| plan                    |        |                                  |   |
| ![](11-Actions Méc      |        |                                  |   |
| aniques/Cours/pandoc/me |        |                                  |   |
| dia/image578.wmf){width |        |                                  |   |
| ="0.5416666666666666in" |        |                                  |   |
| height="0               |        |                                  |   |
| .24166666666666667in"}. |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| O est un point fixe par |        |                                  |   |
| rapport au sol. Une     |        |                                  |   |
| base orthonormée        |        |                                  |   |
| directe                 |        |                                  |   |
| ![](11-Actions Méca     |        |                                  |   |
| niques/Cours/pandoc/med |        |                                  |   |
| ia/image579.wmf){width= |        |                                  |   |
| "0.48333333333333334in" |        |                                  |   |
| height="                |        |                                  |   |
| 0.24166666666666667in"} |        |                                  |   |
| lui est attachée. Le    |        |                                  |   |
| repère                  |        |                                  |   |
| R~0~![](11-Actions Méc  |        |                                  |   |
| aniques/Cours/pandoc/me |        |                                  |   |
| dia/image580.wmf){width |        |                                  |   |
| ="0.6333333333333333in" |        |                                  |   |
| height="                |        |                                  |   |
| 0.24166666666666667in"} |        |                                  |   |
| est supposé galiléen.   |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Le chariot est modélisé |        |                                  |   |
| par un parallélépipède  |        |                                  |   |
| rectangle de longueur   |        |                                  |   |
| **L**, de largeur       |        |                                  |   |
| **b ** et hauteur       |        |                                  |   |
| **h~Ch ~**; son centre  |        |                                  |   |
| de gravité est noté     |        |                                  |   |
| G~Ch~. La position de   |        |                                  |   |
| G~ch~ dépend de la      |        |                                  |   |
| manière dont le chariot |        |                                  |   |
| est rempli. Des règles  |        |                                  |   |
| strictes sont imposées  |        |                                  |   |
| au personnel de         |        |                                  |   |
| l'hôpital pour le       |        |                                  |   |
| remplissage. La         |        |                                  |   |
| position de G~ch~ sera  |        |                                  |   |
| considérée comme        |        |                                  |   |
| invariante pour toute   |        |                                  |   |
| l'étude.                |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| L'étude est limitée au  |        |                                  |   |
| basculement en phase    |        |                                  |   |
| d'accélération          |        |                                  |   |
| (cas1,**Figure 6**).    |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| **Paramétrage**         |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Dimensions chariot      | **L    |                                  |   |
|                         | = 1441 |                                  |   |
|                         | mm ;   |                                  |   |
|                         | b      |                                  |   |
|                         |  = 616 |                                  |   |
|                         | mm ;   |                                  |   |
|                         | h~Ch   |                                  |   |
|                         |  ~= 18 |                                  |   |
|                         | 00mm** |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Masse Chariot           | **M    |                                  |   |
|                         |  = 450 |                                  |   |
|                         | kg**   |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Paramétrage géométrique | G      |                                  |   |
|                         | ~Ch :~ |                                  |   |
|                         | centre |                                  |   |
|                         | de     |                                  |   |
|                         | g      |                                  |   |
|                         | ravité |                                  |   |
|                         | du     |                                  |   |
|                         | c      |                                  |   |
|                         | hariot |                                  |   |
|                         |        |                                  |   |
|                         | !      |                                  |   |
|                         | [](11- |                                  |   |
|                         | Action |                                  |   |
|                         | s Méca |                                  |   |
|                         | niques |                                  |   |
|                         | /Cours |                                  |   |
|                         | /pando |                                  |   |
|                         | c/medi |                                  |   |
|                         | a/imag |                                  |   |
|                         | e581.w |                                  |   |
|                         | mf){wi |                                  |   |
|                         | dth="1 |                                  |   |
|                         | .35in" |                                  |   |
|                         | h      |                                  |   |
|                         | eight= |                                  |   |
|                         | "0.483 |                                  |   |
|                         | 333333 |                                  |   |
|                         | 333333 |                                  |   |
|                         | 34in"} |                                  |   |
|                         |        |                                  |   |
|                         | ![     |                                  |   |
|                         | ](11-A |                                  |   |
|                         | ctions |                                  |   |
|                         |  Mécan |                                  |   |
|                         | iques/ |                                  |   |
|                         | Cours/ |                                  |   |
|                         | pandoc |                                  |   |
|                         | /media |                                  |   |
|                         | /image |                                  |   |
|                         | 582.wm |                                  |   |
|                         | f)avec |                                  |   |
|                         | x      |                                  |   |
|                         | vari   |                                  |   |
|                         | able : |                                  |   |
|                         | **     |                                  |   |
|                         | h = 16 |                                  |   |
|                         | 4 mm** |                                  |   |
|                         |        |                                  |   |
|                         | Rayon  |                                  |   |
|                         | des    |                                  |   |
|                         | roues  |                                  |   |
|                         | du     |                                  |   |
|                         | VAG :  |                                  |   |
|                         | *      |                                  |   |
|                         | *r = 1 |                                  |   |
|                         | 05mm** |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Accélération de la      | *      |                                  |   |
| pesanteur               | *g = 9 |                                  |   |
|                         | ,81m∙s |                                  |   |
|                         | ^-2^** |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Paramétrage dynamique   | M      |                                  |   |
|                         | atrice |                                  |   |
|                         | d'i    |                                  |   |
|                         | nertie |                                  |   |
|                         | du     |                                  |   |
|                         | c      |                                  |   |
|                         | hariot |                                  |   |
|                         | r      |                                  |   |
|                         | éduite |                                  |   |
|                         | en     |                                  |   |
|                         | Gch,   |                                  |   |
|                         | dans   |                                  |   |
|                         | la     |                                  |   |
|                         | ba     |                                  |   |
|                         | se[^1] |                                  |   |
|                         | ![](   |                                  |   |
|                         | 11-Act |                                  |   |
|                         | ions M |                                  |   |
|                         | écaniq |                                  |   |
|                         | ues/Co |                                  |   |
|                         | urs/pa |                                  |   |
|                         | ndoc/m |                                  |   |
|                         | edia/i |                                  |   |
|                         | mage57 |                                  |   |
|                         | 9.wmf) |                                  |   |
|                         | {width |                                  |   |
|                         | ="0.48 |                                  |   |
|                         | 333333 |                                  |   |
|                         | 333333 |                                  |   |
|                         | 334in" |                                  |   |
|                         | hei    |                                  |   |
|                         | ght="0 |                                  |   |
|                         | .24166 |                                  |   |
|                         | 666666 |                                  |   |
|                         | 666667 |                                  |   |
|                         | in"} : |                                  |   |
|                         | *      |                                  |   |
|                         | *I(Gch |                                  |   |
|                         | ,Ch)** |                                  |   |
+-------------------------+--------+----------------------------------+---+
| **Notations valables    |        |                                  |   |
| pour toute l'étude**    |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Torseur des actions     |        | ![](11-Actions Mécaniqu          |   |
| mécaniques              |        | es/Cours/pandoc/media/image584.w |   |
| transmissible d'un      |        | mf){width="2.6416666666666666in" |   |
| solide i sur un solide  |        | height="0.7833333333333333in"}   |   |
| j                       |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| Torseur cinématique de  |        | ![](11-Actions Mécaniqu          |   |
| i par rapport à j       |        | es/Cours/pandoc/media/image585.w |   |
|                         |        | mf){width="0.9333333333333333in" |   |
|                         |        | height="0.5416666666666666in"}   |   |
+-------------------------+--------+----------------------------------+---+
| Torseur dynamique de i  |        | ![](11-Actions Mécaniques/       |   |
| par rapport au repère   |        | Cours/pandoc/media/image586.wmf) |   |
| R~0~                    |        |                                  |   |
+-------------------------+--------+----------------------------------+---+
| La dérivée temporelle   |        |                                  |   |
| première d'une grandeur |        |                                  |   |
| scalaire                |        |                                  |   |
| ![](11-Actions Méca     |        |                                  |   |
| niques/Cours/pandoc/med |        |                                  |   |
| ia/image587.wmf){width= |        |                                  |   |
| "0.19166666666666668in" |        |                                  |   |
| height="                |        |                                  |   |
| 0.21666666666666667in"} |        |                                  |   |
| est notée               |        |                                  |   |
| ![](11-Actions Méca     |        |                                  |   |
| niques/Cours/pandoc/med |        |                                  |   |
| ia/image588.wmf){width= |        |                                  |   |
| "0.15833333333333333in" |        |                                  |   |
| height="0.225in"} , sa  |        |                                  |   |
| dérivée                 |        |                                  |   |
| seco                    |        |                                  |   |
| nde ![](11-Actions Méca |        |                                  |   |
| niques/Cours/pandoc/med |        |                                  |   |
| ia/image589.wmf){width= |        |                                  |   |
| "0.15833333333333333in" |        |                                  |   |
| height="0.225in"}.      |        |                                  |   |
+-------------------------+--------+----------------------------------+---+

**Partie 1.1 Etude du basculement du chariot**

**L'objectif de cette partie est de rechercher l'accélération linéaire
maximale du VAG afin d'assurer le critère de non basculement du
chariot**

On se place juste avant le basculement qui aurait lieu dans le cas 1
(**Figure 6**). Ainsi, on supposera que le chariot est à la limite du
basculement, c\'est-à-dire dans la configuration géométrique de la
**Figure 5**.

1.  **Donner** l'expression de la résultante dynamique,
    ![](11-Actions Mécaniques/Cours/pandoc/media/image590.wmf){width="0.44166666666666665in"
    height="0.2916666666666667in"}, du chariot par rapport au sol en
    fonction de M et
    ![](11-Actions Mécaniques/Cours/pandoc/media/image591.wmf){width="0.11666666666666667in"
    height="0.15in"}.

2.  **Montrer**, avec les hypothèses adoptées, que le moment dynamique
    réduit en G~Ch~, du chariot par rapport au sol
    noté![](11-Actions Mécaniques/Cours/pandoc/media/image592.wmf){width="0.6333333333333333in"
    height="0.2833333333333333in"}, est nul. **En déduire** l'expression
    du moment dynamique, réduit en E, du chariot par rapport au sol,
    noté
    ![](11-Actions Mécaniques/Cours/pandoc/media/image593.wmf){width="0.5in"
    height="0.30833333333333335in"}en fonction de h~Ch~, M et
    ![](11-Actions Mécaniques/Cours/pandoc/media/image594.wmf){width="0.11666666666666667in"
    height="0.15in"} .

3.  **Justifier** **sans calcul** (à l'aide d'une figure par exemple),
    que la condition de non basculement du chariot, autour du point E,
    dans le cas 1 peut être formulée mathématiquement
    par :![](11-Actions Mécaniques/Cours/pandoc/media/image595.wmf){width="0.925in"
    height="0.25833333333333336in"}

4.  En utilisant la condition ci-dessus, en isolant le chariot et en
    appliquant le Théorème du Moment Dynamique réduit en E, en
    projection sur
    ![](11-Actions Mécaniques/Cours/pandoc/media/image596.wmf),
    **déterminer** la relation que doit satisfaire
    ![](11-Actions Mécaniques/Cours/pandoc/media/image597.wmf) pour
    éviter le basculement du chariot par rapport au VAG. La relation
    attendue est de la forme :

![](11-Actions Mécaniques/Cours/pandoc/media/image598.wmf){width="0.8166666666666667in"
height="0.20833333333333334in"}

> Avec
> ![](11-Actions Mécaniques/Cours/pandoc/media/image599.wmf){width="0.43333333333333335in"
> height="0.18333333333333332in"} , l'accélération maximale exprimée en
> fonction de L, g et h~Ch~.

5.  **Réaliser l'application numérique** pour
    ![](11-Actions Mécaniques/Cours/pandoc/media/image600.wmf){width="0.4083333333333333in"
    height="0.175in"}. **Comparer** cette valeur à l\'accélération
    maximale du cahier des charges et en **déduire** la valeur de
    l\'accélération qui satisfait aux deux critères de non basculement
    et de non dérapage.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**ECHELLE EPAS**

*([Source]{.underline} : PSI 2006)*

**Mise en situation**

**[On tiendra compte dans cette partie du fait que la plate-forme reste
toujours horizontale.]{.underline}**

![](11-Actions Mécaniques/Cours/pandoc/media/image601.png){width="4.916666666666667in"
height="3.7291666666666665in"}

Pendant la phase de dressage, les tourelles 1 et 2 sont fixes par
rapport au châssis du camion ; seul le berceau pivote autour de l'axe A,
entraînant avec lui le parc échelle et la plate-forme. Ce mouvement est
obtenu grâce aux vérins hydrauliques articulés en B et C avec la
tourelle 2 et le berceau.

*[On propose le paramétrage suivant :]{.underline}*

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image368.wmf) est
lié au châssis (0).

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image369.wmf) est
lié à l'ensemble {berceau+parc échelle} (5) ;

avec ![](11-Actions Mécaniques/Cours/pandoc/media/image370.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image371.wmf) ;
![](11-Actions Mécaniques/Cours/pandoc/media/image372.wmf) ;
![](11-Actions Mécaniques/Cours/pandoc/media/image373.wmf).

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image374.wmf) est
lié au vérin (3+4) ;

avec ![](11-Actions Mécaniques/Cours/pandoc/media/image375.wmf) ;
![](11-Actions Mécaniques/Cours/pandoc/media/image376.wmf)et
![](11-Actions Mécaniques/Cours/pandoc/media/image377.wmf)

![axe3a](11-Actions Mécaniques/Cours/pandoc/media/image602.png){width="6.0in"
height="5.302083333333333in"}

***[GEOMETRIE DU PARC ECHELLE :]{.underline}***

Dans une première approche, on modélisera le parc échelle par un
assemblage de trois plaques rectangulaires homogènes d'épaisseur
négligeable, de longueur L et de largeur h.

Chaque plaque a une masse notée
m.![modele%20echelle%203](11-Actions Mécaniques/Cours/pandoc/media/image274.png){width="5.15625in"
height="2.5625in"}

***[DONNEES :]{.underline}***

-   [Le parc échelle (5):]{.underline}

On notera la matrice d'inertie du parc échelle au point G (son centre de
gravité) dans la base
![](11-Actions Mécaniques/Cours/pandoc/media/image603.wmf)** :**

![](11-Actions Mécaniques/Cours/pandoc/media/image604.wmf)

Le parc échelle a une masse notée 3m et une longueur notée L.

Son centre de gravité G est tel que
![](11-Actions Mécaniques/Cours/pandoc/media/image605.wmf)**.**

Le parc échelle est solidaire du berceau avec
![](11-Actions Mécaniques/Cours/pandoc/media/image606.wmf).

-   [La plate forme chargée (6):]{.underline}

Pendant le redressement ou l'abaissement, la plate-forme reste toujours
horizontale.

Sa masse une fois chargée sera notée M et son centre de gravité est le
point G~P~ tel que :

![](11-Actions Mécaniques/Cours/pandoc/media/image607.wmf)

On notera la matrice d'inertie de la plate forme chargée au point G~P~
(son centre de gravité) dans la base
![](11-Actions Mécaniques/Cours/pandoc/media/image608.wmf)** :**
![](11-Actions Mécaniques/Cours/pandoc/media/image609.wmf)

-   [Le berceau (5):]{.underline}

Sa masse sera négligée devant les autres masses.

Il est incliné par rapport à l'horizontal d'un angle θ fonction du
temps.

-   [Les vérins (3+ 4):]{.underline}

Leurs masses seront négligées devant les autres masses.

Ils devront exercer un effort, modélisé par un glisseur de
résultante![](11-Actions Mécaniques/Cours/pandoc/media/image610.wmf),
permettant le déplacement θ.

**Questions**

**Question 1 :** Montrez que le vecteur position
![](11-Actions Mécaniques/Cours/pandoc/media/image611.wmf) du centre de
gravité G du parc échelle est tel que
![](11-Actions Mécaniques/Cours/pandoc/media/image612.wmf)

**Question 2 :** Déterminez l'expression littérale du moment dynamique
en A de l'ensemble {parc échelle + berceau} (5) par rapport au châssis
(0) : ![](11-Actions Mécaniques/Cours/pandoc/media/image613.wmf).

**Question 3 :** Déterminez l'expression littérale du moment dynamique
en A de la plate-forme (6) par rapport au châssis (0) :
![](11-Actions Mécaniques/Cours/pandoc/media/image614.wmf).

**Question 4 :** Déterminez l'expression littérale de l'effort R que
devra fournir l'ensemble des deux vérins sur le berceau, en fonction des
masses, des paramètres géométriques et de l'angle θ et de ses dérivées.

Indiquer clairement les sous-ensembles isolés, les actions mécaniques
prises en compte et les théorèmes utilisés.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**RUGOSIMETRE TRIDIMENSIONNEL A GRANDE
VITESSE**

*([Source ]{.underline}: J. Le Goff)*

**Mise en situation**

![](11-Actions Mécaniques/Cours/pandoc/media/image615.png){width="4.416666666666667in"
height="2.28125in"}La rugosimétrie est la mesure de l'état de surface
des pièces mécaniques. L'ordre de grandeur des défauts mesurés est le
micron. Cette mesure des états de surfaces est aussi répandue et
indispensable que la mesure des caractéristiques dimensionnelles et
géométriques des pièces mécaniques (longueur, orientation,
perpendicularité...).

La **figure 1** représente un relevé rugosimétrique tridimensionnel
d'une partie d'une aube de turbine de haute précision.

La mesure de rugosimétrie repose traditionnellement sur deux éléments
distincts : le capteur, qui peut être mécanique (palpeur) ou optique, et
le traitement du signal et des données (algorithmes informatiques), qui
permet de traduire les mesures physiques de base, produites par le
capteur, en données numériques exploitables, représentatives des
caractéristiques physiques de la surface analysée.

De la conjonction des caractéristiques techniques du capteur et du
traitement numérique vont découler les qualités essentielles du
rugosimètre : sa rapidité ; sa résolution ; sa précision ; son amplitude
de mesure.

**STRUCTURE GENERALE DU RUGOSIMETRE A GRANDE VITESSE**

![](11-Actions Mécaniques/Cours/pandoc/media/image616.png){width="3.25in"
height="2.411111111111111in"}Le principe d'un capteur opto-mécanique
(association d'un capteur optique et d'un capteur mécanique) a été
retenu, pour ce prototype. Il est décrit succinctement ci-après
(**figure 2**) :

\- un capteur optique assure une résolution verticale comparable à celle
des meilleurs capteurs mécaniques actuels (\< 10 nm). Ce capteur permet
une mesure des variations rapides des profils mesurés ;

\- un asservissement mécanique vertical à grande amplitude permet à la
tête optique de suivre les variations plus lentes des profils. Un second
capteur donne la position verticale de la tête optique.

Le profil complet sera obtenu par la somme des signaux fournis par les
deux capteurs. Le déplacement vertical du capteur optique est assuré par
une Unité de Rotation (**U.R**) portée par le coulisseau
**[2]{.underline}** (**figure 3**).

![](11-Actions Mécaniques/Cours/pandoc/media/image618.png){width="6.875in"
height="2.2395833333333335in"}

Ce capteur opto-mécanique est lui-même déplacé au dessus de la surface à
mesurer par une Unité de Translation (**U.T**) à vitesse régulée
(**figure 3**), ce qui permet d'obtenir un « profil 2D » : *z fonction
de x*.

La vitesse de déplacement visée est de 200 mm.s^-1^.

Le coût estimé de ce rugosimètre est de 10 000 euros.

**Questions**

**[Modélisation :]{.underline}**

La **figure 5** présente le schéma cinématique qui sera utilisé pour
cette partie de l'étude.
![](11-Actions Mécaniques/Cours/pandoc/media/image619.png){width="6.510416666666667in"
height="3.15625in"}

**[Données et paramétrage :]{.underline}**

L'accélération de la pesanteur sera notée
![](11-Actions Mécaniques/Cours/pandoc/media/image620.wmf)avec![](11-Actions Mécaniques/Cours/pandoc/media/image621.wmf).

On associe au Bâti **[0]{.underline}** le repère
![](11-Actions Mécaniques/Cours/pandoc/media/image622.wmf)que l'on
considère comme galiléen.

-   Le rotor **[1]{.underline}** est en liaison pivot avec le bâti
    **[0]{.underline}**. Paramètre angulaire :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image623.wmf)

Moment d'inertie du rotor 1 par rapport à l'axe
![](11-Actions Mécaniques/Cours/pandoc/media/image624.wmf) noté
![](11-Actions Mécaniques/Cours/pandoc/media/image625.wmf).

Centre d'inertie
![](11-Actions Mécaniques/Cours/pandoc/media/image626.wmf) avec
![](11-Actions Mécaniques/Cours/pandoc/media/image627.wmf)

Un moteur **M1** joue le rôle d'actionneur de l'**U.T** et exerce un
couple : ![](11-Actions Mécaniques/Cours/pandoc/media/image628.wmf)

-   Un coulisseau **[2]{.underline}** est en liaison hélicoïdale (pas
    ![](11-Actions Mécaniques/Cours/pandoc/media/image629.wmf)) avec le
    rotor **[1]{.underline}** et en liaison glissière avec le bâti
    **[0]{.underline}**. Paramètre de position :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image630.wmf)

Masse ![](11-Actions Mécaniques/Cours/pandoc/media/image631.wmf) avec
![](11-Actions Mécaniques/Cours/pandoc/media/image632.wmf)et centre
d'inertie ![](11-Actions Mécaniques/Cours/pandoc/media/image633.wmf).

-   L'ensemble **[3]{.underline}** est en liaison pivot d'axe
    ![](11-Actions Mécaniques/Cours/pandoc/media/image634.wmf) avec le
    coulisseau **[2]{.underline}**.

Paramètre angulaire :
![](11-Actions Mécaniques/Cours/pandoc/media/image635.wmf).

Masse ![](11-Actions Mécaniques/Cours/pandoc/media/image636.wmf) et
centre d'inertie
![](11-Actions Mécaniques/Cours/pandoc/media/image637.wmf) avec
![](11-Actions Mécaniques/Cours/pandoc/media/image638.wmf).

Matrice d'inertie en A :
![](11-Actions Mécaniques/Cours/pandoc/media/image639.wmf)

Un moteur **M3** joue le rôle d'actionneur de l'**U.R** et exerce un
couple : ![](11-Actions Mécaniques/Cours/pandoc/media/image640.wmf)

Comme le montre la photo de la **figure 6**. L'ensemble
**[3]{.underline}** est constitué d'un assemblage de plusieurs
éléments :

-   le bras **[4]{.underline}** en liaison pivot avec le coulisseau
    **[2]{.underline}** et mis en mouvement par le moteur **M3**,

-   la tête optique **[5]{.underline}** fixée sur ce bras ;

-   un contrepoids **[6]{.underline}** fixé aussi sur le bras.

Le contrepoids **[6]{.underline}** a été ajouté pour assurer que le
centre d'inertie
![](11-Actions Mécaniques/Cours/pandoc/media/image641.wmf)de l'ensemble
**[3]{.underline}** soit positionnée sur l'axe
![](11-Actions Mécaniques/Cours/pandoc/media/image642.wmf).

![](11-Actions Mécaniques/Cours/pandoc/media/image643.png){width="2.77994094488189in"
height="2.4390758967629047in"}

Les caractéristiques géométriques des différents éléments sont données
ci-après :

-   bras **[4]{.underline}** : masse
    ![](11-Actions Mécaniques/Cours/pandoc/media/image644.wmf)et centre
    d'inertie ![](11-Actions Mécaniques/Cours/pandoc/media/image645.wmf)
    avec ![](11-Actions Mécaniques/Cours/pandoc/media/image646.wmf) ;

```{=html}
<!-- -->
```
-   tête optique **[5]{.underline}** : masse
    ![](11-Actions Mécaniques/Cours/pandoc/media/image647.wmf)et centre
    d'inertie ![](11-Actions Mécaniques/Cours/pandoc/media/image648.wmf)
    avec ![](11-Actions Mécaniques/Cours/pandoc/media/image649.wmf) ;

-   contrepoids **[6]{.underline}** : masse
    ![](11-Actions Mécaniques/Cours/pandoc/media/image650.wmf)et centre
    d'inertie ![](11-Actions Mécaniques/Cours/pandoc/media/image651.wmf)
    avec ![](11-Actions Mécaniques/Cours/pandoc/media/image652.wmf) 

**[Question 1]{.underline}** -- **Déterminez** l'expression littérale de
la masse ![](11-Actions Mécaniques/Cours/pandoc/media/image653.wmf)du
contrepoids **[6]{.underline}** qui assure que le centre d'inertie
![](11-Actions Mécaniques/Cours/pandoc/media/image641.wmf)soit
positionné sur l'axe
![](11-Actions Mécaniques/Cours/pandoc/media/image642.wmf).**Réaliser**
l'application numérique.

**[Question 2]{.underline}** -- **Montrer**, que dans ce cas,
![](11-Actions Mécaniques/Cours/pandoc/media/image654.wmf).

**[Question 3]{.underline}** -- **Isoler** l'ensemble
**[3]{.underline}** et **faire le bilan**, à l'aide de torseurs, des
actions mécaniques extérieures qui agissent sur **[3]{.underline}**.

**[Question 4]{.underline}** -- **Justifier** que l'équation scalaire du
Principe Fondamental de la Dynamique appliquée à l'ensemble 3 qui permet
d'obtenir directement une relation entre le couple moteur
![](11-Actions Mécaniques/Cours/pandoc/media/image655.wmf), les
caractéristiques de masses et d'inertie de **[3]{.underline}** , les
dimensions du système, les paramètres de mouvement et leurs dérivées est
le théorème du moment dynamique en A en projection sur
![](11-Actions Mécaniques/Cours/pandoc/media/image656.wmf).

**[Question 5]{.underline}** -- **Déterminer** cette équation.

**[Question 6]{.underline}** -- **En déduire** l'expression littérale du
couple moteur ![](11-Actions Mécaniques/Cours/pandoc/media/image655.wmf)
en fonction de
![](11-Actions Mécaniques/Cours/pandoc/media/image657.wmf).

![](11-Actions Mécaniques/Cours/pandoc/media/image658.png){width="3.0in"
height="1.98125in"}

Lorsque le point focal de la tête optique suit le profil moyen d'une
surface,
l'angle![](11-Actions Mécaniques/Cours/pandoc/media/image659.wmf) reste
constant et égal à
![](11-Actions Mécaniques/Cours/pandoc/media/image660.wmf).

La loi de commande de l'unité de translation est représentée sur la
figure 7. La vitesse nominale (constante) recherchée est
notée![](11-Actions Mécaniques/Cours/pandoc/media/image661.wmf).

**[Question 7]{.underline}** -- **Déterminer** la valeur de
l'accélération,
notée![](11-Actions Mécaniques/Cours/pandoc/media/image662.wmf),
atteinte lors de la première phase du mouvement
(![](11-Actions Mécaniques/Cours/pandoc/media/image663.wmf)).

**[Question 8]{.underline}** -- **Donner** l'expression littérale du
couple moteur ![](11-Actions Mécaniques/Cours/pandoc/media/image655.wmf)
dans la phase d'accélération puis dans la phase à vitesse
constante![](11-Actions Mécaniques/Cours/pandoc/media/image661.wmf).

**[Question 9]{.underline}** -- **Calculer** la valeur maximale du
couple![](11-Actions Mécaniques/Cours/pandoc/media/image655.wmf).

**MLPS**

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source ]{.underline}: ATS 2016)*

La société Sonaréma-Fondex assemble, conditionne et diffuse des réchauds
à gaz portables de grande puissance. Ces réchauds sont conditionnés et
vendus en cartons. Depuis peu, l\'ouverture de la société à de nouveaux
marchés impose d\'accroître le rythme de la distribution. Dans ce
nouveau contexte, la société a besoin de palettiser ces cartons afin de
les acheminer vers ses principaux distributeurs.

La société possède pour le conditionnement de cartons un système
automatisé commercialisé sous l\'acronyme MLPS pour Multi Level
Packaging System. Elle envisage d\'utiliser ce système pour satisfaire
ce nouveau besoin.

+------------------------------------+---------------------------------+
| ![GEDC3418.JPG](11-Actions Méca    | ![](11-Actions Mécaniques       |
| niques/Cours/pandoc/media/image664 | /Cours/pandoc/media/image665.pn |
| .jpeg){width="2.616301399825022in" | g){width="2.3134634733158355in" |
| height="1.9585247156605425in"}     | height="2.1707950568678913in"}  |
|                                    |                                 |
| Fig.3 : vue générale du MLPS       | Fig.4 : modèle numérique du     |
|                                    | MLPS                            |
+====================================+=================================+
+------------------------------------+---------------------------------+

> **IV.2. Calcul des paramètres cinématiques**

[Objectifs :]{.underline} déterminer pour les ventouses équipant le
MLPS, l\'accélération maximale que peut subir le préhenseur de l\'unité
en U. On en déduira alors la vitesse linéaire V pour cette accélération.

Il faut s\'assurer qu\'il n\'y ait pas glissement entre le carton et les
ventouses. En effet, si le carton glisse par rapport aux ventouses il
risque soit d\'être lâché soit de se déplacer par rapport aux ventouses
et sera mal positionné sur la palette.

Le paramètre permettant d\'éviter ce glissement est la valeur de
l\'accélération. Nous devons à présent déterminer l\'accélération
maximale admissible par l\'unité en U pour qu\'il n\'y ait pas
glissement entre le carton et les ventouses.

Fig.16 : unité en U

[Notations:]{.underline}

-   le repère
    $(O,\ \overrightarrow{x},\ \overrightarrow{y},\ \overrightarrow{z})$
    lié au bâti est supposé galiléen

-   l\'ensemble préhenseur+carton est en translation rectiligne d\'axe
    $\overrightarrow{x}$

-   ${\overrightarrow{V}}_{G\epsilon carton/0} = V(t).\overrightarrow{x}$

-   ${\overrightarrow{a}}_{G\epsilon carton/0} = a(t).\overrightarrow{x}$

```{=html}
<!-- -->
```
-   la masse du carton est notée m, m=8 kg

```{=html}
<!-- -->
```
-   le centre d\'inertie du carton est noté G

```{=html}
<!-- -->
```
-   le coefficient d\'adhérence carton/ventouse est noté μ, μ=0,4

[Hypothèses:]{.underline}

-   le plan $(\overrightarrow{x},\ \overrightarrow{z})$ est plan de
    symétrie pour la géométrie et pour les efforts

-   en M, la ventouse de gauche exerce sur le carton une action
    mécanique modélisable par un glisseur:

> $$\left\{ T_{ventouse \rightarrow carton}^{M} \right\} = \ \begin{Bmatrix}
> X_{M} & 0 \\
> 0 & 0 \\
> Z_{M} & 0
> \end{Bmatrix}_{M}$$

-   en N, la ventouse de droite exerce sur le carton une action
    mécanique modélisable par un glisseur:

$$\left\{ T_{ventouse \rightarrow carton}^{N} \right\} = \ \begin{Bmatrix}
X_{N} & 0 \\
0 & 0 \\
Z_{N} & 0
\end{Bmatrix}_{N}$$

-   $\overrightarrow{GM} = \  - 0,1 \bullet \overrightarrow{x} + 0,07 \bullet \overrightarrow{z}$
    (en mètre)

-   $\overrightarrow{GN} = \ 0,1 \bullet \overrightarrow{x} + 0,07 \bullet \overrightarrow{z}$
    (en mètre)

Q1 A la limite du glissement, donner la relation entre $X_{M}$ et
$Z_{M}$ et entre $X_{N}$ et $Z_{N}$.

Q2 A la limite du glissement, appliquer le principe fondamental de la
dynamique au carton et en déduire l\'accélération maximale admissible
ainsi que les actions mécaniques encaissées par les ventouses.

La charge maximale unitaire (CMU) pour une ventouse de diamètre 75 mm en
caoutchouc

naturel est de 6 kg.

Q3 Les ventouses sont-elles capables d\'encaisser les efforts qui leur
sont appliqués? Justifier.

Les ventouses utilisées imposent une accélération linéaire limite
**a=4m.s^-2^**.

Le respect du cahier des charges impose que la relation entre la vitesse
V et l\'accélération a soit : $5,525 = 7,5*V - \frac{5*V²}{4}$.

Q4 Calculer les vitesses solutions de l\'équation précédente.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**MACHINE 5 AXES**

*([Source]{.underline} : ATS 2006, Jacques Le Goff)*

![](11-Actions Mécaniques/Cours/pandoc/media/image367.png){width="3.8958333333333335in"
height="3.275in"}**Mise en situation**

*[On propose le paramétrage suivant :]{.underline}*

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image368.wmf) est
lié au châssis (0).

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image369.wmf) est
lié à l'ensemble {berceau+parc échelle} (5) ;

Avec :

![](11-Actions Mécaniques/Cours/pandoc/media/image370.wmf) et
![](11-Actions Mécaniques/Cours/pandoc/media/image371.wmf) ;

![](11-Actions Mécaniques/Cours/pandoc/media/image372.wmf) ;
![](11-Actions Mécaniques/Cours/pandoc/media/image373.wmf).

Le repère ![](11-Actions Mécaniques/Cours/pandoc/media/image374.wmf) est
lié au vérin (3+4) ;

Avec :

![](11-Actions Mécaniques/Cours/pandoc/media/image375.wmf) ;
![](11-Actions Mécaniques/Cours/pandoc/media/image376.wmf)et
![](11-Actions Mécaniques/Cours/pandoc/media/image377.wmf)

**Guidage de l'électrobroche**

![](11-Actions Mécaniques/Cours/pandoc/media/image666.png){width="6.531944444444444in"
height="0.4270833333333333in"}![](11-Actions Mécaniques/Cours/pandoc/media/image667.png){width="3.9791666666666665in"
height="2.5625in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image668.png){width="3.4854166666666666in"
height="1.0013888888888889in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image669.png){width="5.643670166229222in"
height="0.7218088363954506in"}

1.  Exprimer la matrice d'inertie de l'outil
    ![](11-Actions Mécaniques/Cours/pandoc/media/image670.wmf) dans la
    base du repère
    ![](11-Actions Mécaniques/Cours/pandoc/media/image671.wmf).

2.  Exprimer dans la base du référentiel R~4~, la résultante dynamique
    de l'outil dans son mouvement par rapport à R~3~. Cette résultante
    sera notée :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image672.wmf).

*Les axes « X » et « Z » sont supposés bloqués et la broche tourne dans
le vide à vitesse constante.*

3.  Exprimer dans la base du référentiel R~4~, le moment dynamique au
    point S de l'outil dans son mouvement par rapport à R~3~. Ce moment
    sera notée :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image673.wmf).

*Les axes « X » et « Z » sont supposés bloqués et la broche tourne dans
le vide à vitesse constante.*

4.  Exprimer les torseurs des actions mécaniques, de S~5~ sur l'ensemble
    Σ=(rotor+outil), des liaisons en P et Q, respectivement exprimés en
    P et Q dans la base du repère R~4~.

5.  En appliquant le PFD, déterminer la norme des résultantes des
    torseurs de ces actions mécaniques dans les configurations 1 et 2
    (vitesse constante). Conclure.

    **Guidage de l'axe « X »**

![](11-Actions Mécaniques/Cours/pandoc/media/image378.png){width="2.0520833333333335in"
height="0.8708333333333333in"}![](11-Actions Mécaniques/Cours/pandoc/media/image379.png){width="4.072916666666667in"
height="3.1458333333333335in"}![](11-Actions Mécaniques/Cours/pandoc/media/image380.png){width="5.9375in"
height="0.5270898950131233in"}![](11-Actions Mécaniques/Cours/pandoc/media/image381.png){width="5.9456342957130355in"
height="0.41656167979002623in"}![](11-Actions Mécaniques/Cours/pandoc/media/image383.png){width="5.625in"
height="1.6947954943132109in"}

4.  Exprimer dans la base du référentiel R~3~, la résultante dynamique
    de l'ensemble (4+5) dans son mouvement par rapport à R~3~. Cette
    résultante sera notée
    :![](11-Actions Mécaniques/Cours/pandoc/media/image674.wmf)

*L'étude porte sur une phase d'usinage , en déplacement sur l'axe « X »*
uniquement

5.  Exprimer dans la base du référentiel R~3~, le moment dynamique au
    point O~4~ de l'ensemble (4+5) dans son mouvement par rapport à
    R~3~. Ce moment dynamique sera notée :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image675.wmf)

*L'étude porte sur une phase d'usinage , en déplacement sur l'axe « X »
uniquement*

6.  Exprimer le torseur des actions mécaniques de S~3~ sur S~4~ dans la
    liaison glissière d'axe « X », exprimée au point O~4~ dans la base
    du repère R~3~.

![](11-Actions Mécaniques/Cours/pandoc/media/image676.png){width="6.531944444444444in"
height="0.5743055555555555in"}

7.  En phase d'accélération maximale sur l'axe « X » :
    ![](11-Actions Mécaniques/Cours/pandoc/media/image677.wmf),
    déterminer les composantes du torseur des actions mécaniques exprimé
    à la question précédente

8.  Comparer l'incidence des efforts de coupe et des effets dynamiques
    sur le chargement de la liaison glissière.

*\
*

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![](11-Actions Mécaniques/Cours/pandoc/media/image678.png){width="0.5731113298337708in"
height="0.7641502624671916in"}**ROBOT MANIPULATEUR ARTICULE**

*[Source :]{.underline} Jean-Philippe Costes*

**Mise en situation**

On considère un robot manipulateur ABB IRB 7600 articulé à 6 axes comme
celui ci-dessous.

On souhaite déterminer le couple moteur à exercer sur l\'axe
**[2]{.underline}** (orienté par x~1~ ) pour une configuration
particulière où les axes **[3]{.underline}**, **[4]{.underline}**,
**[5]{.underline}** et **[6]{.underline}** sont verrouillés (bloqués).
Configuration pour laquelle on suppose donc que le robot peut se réduire
cinématiquement à deux solides dont on suppose connus les centres de
gravité et les opérateurs d\'inertie respectifs. En particulier, on
remarquera la symétrie du robot par rapport au plan (y~1~,z~0~=z~1~) ou
(y~2~,z~2~).

![](11-Actions Mécaniques/Cours/pandoc/media/image679.png){width="6.443067585301837in"
height="5.613968722659668in"}

On pose $\overrightarrow{OA} = a.{\overrightarrow{z}}_{0}$ et
$\overrightarrow{AG_{2}} = b.{\overrightarrow{y}}_{2}$, et on donne
l'opérateur d'inertie de **[2]{.underline}** en A exprimé dans la base
B~2~(x~1~,y~2~,z~2~) :
$\left\lbrack I_{A}(2) \right\rbrack = \begin{bmatrix}
A_{2} & 0 & 0 \\
0 & B_{2} & {- D}_{2} \\
0 & {- D}_{2} & C_{2}
\end{bmatrix}_{({\overrightarrow{x}}_{1},{\overrightarrow{y}}_{2},{\overrightarrow{z}}_{2})}$

Le bilan des AM extérieures pour **[2]{.underline}** donne :

-   L'action inconnue du moteur {T~m→2~} = $\begin{Bmatrix}
    \overrightarrow{0} \\
    C_{m}.{\overrightarrow{x}}_{1}
    \end{Bmatrix}_{A}$

-   L'action de la pesanteur {T~pes→2~} = $\begin{Bmatrix}
    {\overrightarrow{P}}_{2} = - M_{2}.g.{\overrightarrow{z}}_{0} \\
    \overrightarrow{0}
    \end{Bmatrix}_{G_{2}}$

-   L'action de la liaison pivot d'axe (A,x~1~) {T~1→2~} =
    $\begin{Bmatrix}
    {\overrightarrow{A}}_{1/2} \\
    {\overrightarrow{M}}_{A,1/2}
    \end{Bmatrix}_{A} = \begin{Bmatrix}
    X_{12} & 0 \\
    Y_{12} & M_{12} \\
    Z_{12} & N_{12}
    \end{Bmatrix}_{A,({\overrightarrow{x}}_{1},\overrightarrow{y} - ,\overrightarrow{z} - )}$

    **Travail demandé**

**1. Définir** l'équation à écrire pour exprimer le seul couple moteur
C~m~.

**2. Déterminer** au point A les torseurs cinématique et cinétique de
**[2]{.underline}** par rapport à **[0]{.underline}**.

**3. Déterminer** au point A les éléments utiles (selon Q1) du torseur
dynamique de **[2]{.underline}** par rapport à **[0]{.underline}**.

**4.** En écrivant l'équation définie Q1, **donner** l'expression de
C~m~ en fonction des paramètres α, θ et de leurs dérivées, des longueurs
et données d'inertie (A~2~, B~2~, C~2~, D~2~, et M~2~).

[Données numériques]{.underline}

M~2~ = 1064 kg b = 940 mm g = 9,81 m/s²

A~2~ = 103,6 kg.m² B~2~ = 36,8 kg.m² C~2~ = 80,8 kg.m² D~2~ = 28,0 kg.m²

θ ∈\[10°;150°\] ${\ddot{\theta}}_{maxi} = 10{^\circ}/s²$
${\dot{\alpha}}_{maxi} = 75{^\circ}/s$

**5. Faire** l'Aapplication numérique pour déterminer C~m~ maxi.

![](11-Actions Mécaniques/Cours/pandoc/media/image680.jpeg){width="0.8262981189851268in"
height="0.7525765529308837in"}

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**MACHINE DE REEDUCATION**

*[Source :]{.underline} Sujet CCP PSI 2013*

**Mise en situation**

**Présentation du système**

La machine de rééducation SYS-REEDUC est un système capable d\'évaluer
et d\'aider à la rééducation des membres inférieurs. Le principe de la
rééducation est de solliciter les différents muscles de la jambe afin de
récupérer un maximum de mobilité suite à un accident.

**Description du système**

Le mécanisme de la machine SYS-REEDUC suppose que la hanche est fixe par
rapport au bâti et que le mouvement est engendré par un support mobile
sur lequel repose le pied. De plus, afin de pouvoir développer une
chaîne cinématique permettant la réalisation de mouvement en chaîne
musculaire fermée et par analogie aux systèmes robotisés, l'ensemble
mécanique, constitué du membre inférieur et du dispositif de
rééducation, doit former une chaîne cinématique fermée.

![](11-Actions Mécaniques/Cours/pandoc/media/image681.png){width="6.613207567804024in"
height="3.9905653980752405in"}

La chaîne cinématique, présentée sur la figure ci-dessus, se compose du
bâti **0** (le haut du corps du patient est supposé lié au dossier du
bâti), du support mobile **1**, du support intermédiaire **2**, du
support de pied **3**, de la cuisse, de la jambe et du pied. Un seul
côté est représenté mais la machine réelle permet de travailler sur les
deux jambes en même temps si cela est nécessaire.

**Comportement dynamique du système**

**Modélisation**

![](11-Actions Mécaniques/Cours/pandoc/media/image682.png){width="6.733333333333333in"
height="2.862101924759405in"}

-   ![](11-Actions Mécaniques/Cours/pandoc/media/image683.wmf) la
    verticale ascendante

-   Support mobile **1** de masse M = 14 kg, de centre d\'inertie G~1~,
    tel que ![](11-Actions Mécaniques/Cours/pandoc/media/image684.wmf)

-   Support intermédiaire **2** de masse négligeable, en liaison pivot
    d\'axe ![](11-Actions Mécaniques/Cours/pandoc/media/image685.wmf)
    avec le support mobile **1**. On a
    ![](11-Actions Mécaniques/Cours/pandoc/media/image686.wmf) avec h~2~
    = 0,6 m. Le support est supposé fixe durant les phases
    d\'utilisation, ainsi l\'angle α est constant,
    ![](11-Actions Mécaniques/Cours/pandoc/media/image687.wmf)

-   Support de pied **3** de masse m = 4 kg et de moment d\'inertie sur
    l\'axe ![](11-Actions Mécaniques/Cours/pandoc/media/image688.wmf)
    noté J = 0,26 kg.m², de centre d\'inertie G~3~, tel que
    ![](11-Actions Mécaniques/Cours/pandoc/media/image689.wmf) avec h~4~
    = 10 mm et h~3~ = 50 mm. Le support de pied **3** est en liaison
    pivot
    d\'axe![](11-Actions Mécaniques/Cours/pandoc/media/image690.wmf)ou
    bien ![](11-Actions Mécaniques/Cours/pandoc/media/image691.wmf) avec
    le support intermédiaire **2**, l\'angle de cette rotation est noté
    θ~23~ tel que
    ![](11-Actions Mécaniques/Cours/pandoc/media/image692.wmf)

-   Le moteur 1, entraînant la translation du support mobile **1,**
    délivre un couple moteur, tel
    que![](11-Actions Mécaniques/Cours/pandoc/media/image693.wmf). Le
    moteur 1 entraîne un réducteur 1 de rapport de réduction
    ![](11-Actions Mécaniques/Cours/pandoc/media/image694.wmf). La
    sortie du réducteur est liée à la poulie de rayon r = 46,1 mm. On
    négligera les masses et inerties du moteur et du réducteur. On note
    ![](11-Actions Mécaniques/Cours/pandoc/media/image695.wmf) et
    ![](11-Actions Mécaniques/Cours/pandoc/media/image696.wmf)

-   Les poulies et la courroie sont supposées de masse négligeable. La
    courroie est supposée indéformable

-   Le moteur 2, entraînant la rotation du support de pied **3** par
    rapport au support intermédiaire **2**, délivre un couple moteur tel
    que![](11-Actions Mécaniques/Cours/pandoc/media/image697.wmf). Le
    moteur 2 entraîne un réducteur 2 de rapport de
    réduction![](11-Actions Mécaniques/Cours/pandoc/media/image698.wmf).
    On négligera les masses et inerties du moteur et du réducteur

-   Le patient exerce une action mécanique complexe composée :

```{=html}
<!-- -->
```
-   d\'une
    force![](11-Actions Mécaniques/Cours/pandoc/media/image699.wmf)
    exercée par le patient sur le support **3**, modélisée par un
    glisseur passant par le point P, tel
    que![](11-Actions Mécaniques/Cours/pandoc/media/image700.wmf)

-   un couple![](11-Actions Mécaniques/Cours/pandoc/media/image701.wmf)
    exercé par le patient sur le support **3** au point O~2~

```{=html}
<!-- -->
```
-   Les résistances au mouvement sont négligées. Les liaisons sont
    considérées comme parfaite

**Questions**

**1.** Isoler le tronçon de courroie AB et déduire une relation entre
F~cp~ et F~c1~.

**2.** Compléter le graphe des actions mécaniques ci-dessous. Ne pas
représenter la liaison entre la poulie réceptrice et le bâti d'une part
et la liaison entre la poulie réceptrice et la courroie d'autre part.

*Recopier ce graphe sur votre copie*

**3.** En isolant la poulie motrice et en appliquant le théorème de
votre choix, exprimer la relation entre C~M1~ et F~c1~.

**4.** En isolant le solide {3} et en appliquant le théorème de votre
choix, exprimer l\'équation du mouvement liant C~M3~(t) aux paramètres
du mouvement x(t) et θ~23~(t). Montrer que l'on obtient :

![](11-Actions Mécaniques/Cours/pandoc/media/image703.wmf)

**5.** En isolant l\'ensemble de solides {1 + 2 + 3} et en appliquant le
théorème de votre choix, exprimer l\'équation du mouvement liant
C~M1~(t) aux paramètres du mouvement x(t) et θ~23~(t). Montrer que l\'on
obtient :

![](11-Actions Mécaniques/Cours/pandoc/media/image704.wmf)

**6.** Que peut-on dire des équations et obtenues précédemment en
considérant que nous souhaitons réaliser un asservissement du système
sur ses différents paramètres. ?

**7.** En linéarisant l'équation , montrer que l'on obtient la relation
suivante rapportée à l\'axe moteur 1 :

![](11-Actions Mécaniques/Cours/pandoc/media/image705.wmf) où ω~m~ est
la vitesse de rotation du moteur 1

**8.** Ecrire l'équation dans le domaine de Laplace.

![](11-Actions Mécaniques/Cours/pandoc/media/image333.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**MACHINE REMPLISSAGE-SERTISSAGE**

*([Source]{.underline} : Centrale-Supélec TSI 2005)*

![remplissage sertissage
3](11-Actions Mécaniques/Cours/pandoc/media/image706.jpeg){width="2.783333333333333in"
height="2.0972222222222223in"}**Mise en situation**

Le système étudié est un sous-ensemble d'une unité de production de
vaporisateurs de parfum Givenchy à pompe manuelle. Pour cette étude, le
système est configuré pour la production de vaporisateurs de 100 ml avec
une cadence de 1800 vaporisateurs par heure. Les flacons sont placés
dans des alvéoles (16 alvéoles) d'un plateau, nommé *plateau alvéolé*,
tournant autour d'un axe vertical et qui vient les placer successivement
sous les différents postes. Pendant toute la production d'un
vaporisateur, le flacon est placé sur un support. On nommera par la
suite, *flacon*, noté **20**, l'ensemble {flacon+support}.

![](11-Actions Mécaniques/Cours/pandoc/media/image707.png){width="6.791666666666667in"
height="4.03709208223972in"}

Le mouvement de rotation continue de l'arbre **3** est transformé en une
rotation discontinue, d'axe vertical, du plateau alvéolé **8**, par
l'intermédiaire :

• D'un renvoi d'angle de rapport ρ~3~ = 1

> • D'un indexeur Ferguson permettant d'obtenir, pour le temps
> nécessaire à larotation d'un tour de son arbre d'entrée **6** :
>
> \- une rotation de son arbre de sortie **7** , d'1/4 de tour pendant
> 1/5^ème^ de ce temps
>
> \- un arrêt de cet arbre **7** , pendant les 4/5^ème^ restant

• D'un réducteur à engrenage cylindrique de rapport ρ~4~ = 4

**Entrainement du plateau alvéolé**

[Objet de l'étude :]{.underline}

Le système isolé, nommé *sous-ensemble* **E**, est constitué :

> • Du plateau alvéolé **8** équipé de sa roue dentée, modélisé par un
> cylindre homogène en acier (ρ = 7800 kg.m^-3^), de diamètre d~8~ = 580
> mm et d'épaisseur e~8~ = 20mm
>
> • De Nb~v~ = 15 flacons, repérés **20** (ensemble flacon+support).
> Chaque flacon est modélisé par une masse ponctuelle m~20~ = 0,5 kg,
> située dans le plan médian horizontal du plateau alvéolé et au rayon
> r~20~ = 276 mm

• De l'arbre de sortie **7** de l'indexeur, équipé de son pignon, dont
la masse sera négligée

[Hypothèse :]{.underline}

Lors de la rotation du plateau alvéolé, le flacon glisse sur le bâti. Le
facteur de frottement de glissement au contact du flacon sur le bâti est
estimé à f~20/0~ = 0,15. Toutes les autres liaisons sont supposées
parfaites.

[Notations :]{.underline}

![](11-Actions Mécaniques/Cours/pandoc/media/image708.wmf) repère lié au
bâti ;

![](11-Actions Mécaniques/Cours/pandoc/media/image709.wmf) vitesse
angulaire de l'arbre **3** par rapport au bâti **0** ;

![](11-Actions Mécaniques/Cours/pandoc/media/image710.wmf) vitesse
angulaire du plateau alvéolé **8** par rapport au bâti ; ω~8/0~ \> 0 ;

![](11-Actions Mécaniques/Cours/pandoc/media/image711.wmf) vitesse
angulaire de l'arbre de sortie de l'indexeur **7** par rapport au bâti.

**1.** Donner l'expression littérale puis calculer la valeur du moment
d'inertie J~E~, de l'ensemble **E** autour de l'axe
![](11-Actions Mécaniques/Cours/pandoc/media/image712.wmf).

**2.** La loi de mouvement imposée au plateau alvéolé **8**, est
modélisée par la loi en trapèze ci-dessous.

Après avoir retrouvé, sur les courbes ci-dessous, le déplacement
angulaire θ~8~, du plateau **8** pendant le temps t~f~, exprimer puis
calculer la valeur maximum de la vitesse angulaire du plateau
ω~8/0\ maxi~.

**3.** Appliquer le théorème de l'énergie cinétique au système isolé
**E** pour déterminer l'expression littérale du couple C~7~ installé sur
l'arbre de sortie de l'indexeur. Calculer la valeur de C~7~ en phase
d'accélération (g = 9,81 m.s^-2^).

**4.** Pour un rendement global de l'indexeur égal à η~i~ = 0,8,
calculer la valeur maximum de la puissance P~6~, nécessaire au niveau de
l'arbre d'entrée **6** de l'indexeur.

![remplissage sertissage
2](11-Actions Mécaniques/Cours/pandoc/media/image713.jpeg){width="5.413888888888889in"
height="3.6034722222222224in"}![](11-Actions Mécaniques/Cours/pandoc/media/image714.png){width="2.1173611111111112in"
height="3.263888888888889in"}

[^1]: Rappel : le chariot est en translation rectiligne suivant
    ![](11-Actions Mécaniques/Cours/pandoc/media/image583.wmf), la base
    ![](11-Actions Mécaniques/Cours/pandoc/media/image579.wmf){width="0.48333333333333334in"
    height="0.24166666666666667in"} est donc fixe par rapport au
    chariot.

---
## Inventaire des images
11-Actions Mécaniques/Cours/pandoc/media/image1.png
11-Actions Mécaniques/Cours/pandoc/media/image10.png
11-Actions Mécaniques/Cours/pandoc/media/image100.wmf
11-Actions Mécaniques/Cours/pandoc/media/image101.wmf
11-Actions Mécaniques/Cours/pandoc/media/image102.wmf
11-Actions Mécaniques/Cours/pandoc/media/image103.wmf
11-Actions Mécaniques/Cours/pandoc/media/image104.wmf
11-Actions Mécaniques/Cours/pandoc/media/image105.wmf
11-Actions Mécaniques/Cours/pandoc/media/image106.wmf
11-Actions Mécaniques/Cours/pandoc/media/image107.wmf
11-Actions Mécaniques/Cours/pandoc/media/image108.wmf
11-Actions Mécaniques/Cours/pandoc/media/image109.wmf
11-Actions Mécaniques/Cours/pandoc/media/image110.wmf
11-Actions Mécaniques/Cours/pandoc/media/image111.wmf
11-Actions Mécaniques/Cours/pandoc/media/image112.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image113.wmf
11-Actions Mécaniques/Cours/pandoc/media/image114.wmf
11-Actions Mécaniques/Cours/pandoc/media/image115.wmf
11-Actions Mécaniques/Cours/pandoc/media/image116.wmf
11-Actions Mécaniques/Cours/pandoc/media/image117.wmf
11-Actions Mécaniques/Cours/pandoc/media/image118.wmf
11-Actions Mécaniques/Cours/pandoc/media/image119.wmf
11-Actions Mécaniques/Cours/pandoc/media/image12.png
11-Actions Mécaniques/Cours/pandoc/media/image120.wmf
11-Actions Mécaniques/Cours/pandoc/media/image121.wmf
11-Actions Mécaniques/Cours/pandoc/media/image122.wmf
11-Actions Mécaniques/Cours/pandoc/media/image123.wmf
11-Actions Mécaniques/Cours/pandoc/media/image124.wmf
11-Actions Mécaniques/Cours/pandoc/media/image125.wmf
11-Actions Mécaniques/Cours/pandoc/media/image126.png
11-Actions Mécaniques/Cours/pandoc/media/image127.wmf
11-Actions Mécaniques/Cours/pandoc/media/image128.wmf
11-Actions Mécaniques/Cours/pandoc/media/image129.wmf
11-Actions Mécaniques/Cours/pandoc/media/image13.png
11-Actions Mécaniques/Cours/pandoc/media/image130.wmf
11-Actions Mécaniques/Cours/pandoc/media/image131.wmf
11-Actions Mécaniques/Cours/pandoc/media/image132.wmf
11-Actions Mécaniques/Cours/pandoc/media/image133.png
11-Actions Mécaniques/Cours/pandoc/media/image134.wmf
11-Actions Mécaniques/Cours/pandoc/media/image135.wmf
11-Actions Mécaniques/Cours/pandoc/media/image138.wmf
11-Actions Mécaniques/Cours/pandoc/media/image139.wmf
11-Actions Mécaniques/Cours/pandoc/media/image140.wmf
11-Actions Mécaniques/Cours/pandoc/media/image141.wmf
11-Actions Mécaniques/Cours/pandoc/media/image142.wmf
11-Actions Mécaniques/Cours/pandoc/media/image143.wmf
11-Actions Mécaniques/Cours/pandoc/media/image144.png
11-Actions Mécaniques/Cours/pandoc/media/image145.wmf
11-Actions Mécaniques/Cours/pandoc/media/image146.wmf
11-Actions Mécaniques/Cours/pandoc/media/image147.wmf
11-Actions Mécaniques/Cours/pandoc/media/image148.wmf
11-Actions Mécaniques/Cours/pandoc/media/image149.png
11-Actions Mécaniques/Cours/pandoc/media/image15.png
11-Actions Mécaniques/Cours/pandoc/media/image150.wmf
11-Actions Mécaniques/Cours/pandoc/media/image151.wmf
11-Actions Mécaniques/Cours/pandoc/media/image152.png
11-Actions Mécaniques/Cours/pandoc/media/image153.wmf
11-Actions Mécaniques/Cours/pandoc/media/image154.wmf
11-Actions Mécaniques/Cours/pandoc/media/image155.png
11-Actions Mécaniques/Cours/pandoc/media/image156.wmf
11-Actions Mécaniques/Cours/pandoc/media/image157.wmf
11-Actions Mécaniques/Cours/pandoc/media/image158.wmf
11-Actions Mécaniques/Cours/pandoc/media/image159.wmf
11-Actions Mécaniques/Cours/pandoc/media/image16.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image160.wmf
11-Actions Mécaniques/Cours/pandoc/media/image161.wmf
11-Actions Mécaniques/Cours/pandoc/media/image162.wmf
11-Actions Mécaniques/Cours/pandoc/media/image163.wmf
11-Actions Mécaniques/Cours/pandoc/media/image164.wmf
11-Actions Mécaniques/Cours/pandoc/media/image165.wmf
11-Actions Mécaniques/Cours/pandoc/media/image167.wmf
11-Actions Mécaniques/Cours/pandoc/media/image168.wmf
11-Actions Mécaniques/Cours/pandoc/media/image169.wmf
11-Actions Mécaniques/Cours/pandoc/media/image17.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image170.wmf
11-Actions Mécaniques/Cours/pandoc/media/image171.wmf
11-Actions Mécaniques/Cours/pandoc/media/image172.wmf
11-Actions Mécaniques/Cours/pandoc/media/image174.wmf
11-Actions Mécaniques/Cours/pandoc/media/image175.wmf
11-Actions Mécaniques/Cours/pandoc/media/image176.wmf
11-Actions Mécaniques/Cours/pandoc/media/image177.wmf
11-Actions Mécaniques/Cours/pandoc/media/image178.wmf
11-Actions Mécaniques/Cours/pandoc/media/image179.wmf
11-Actions Mécaniques/Cours/pandoc/media/image18.wmf
11-Actions Mécaniques/Cours/pandoc/media/image180.wmf
11-Actions Mécaniques/Cours/pandoc/media/image181.wmf
11-Actions Mécaniques/Cours/pandoc/media/image182.wmf
11-Actions Mécaniques/Cours/pandoc/media/image183.wmf
11-Actions Mécaniques/Cours/pandoc/media/image184.wmf
11-Actions Mécaniques/Cours/pandoc/media/image185.wmf
11-Actions Mécaniques/Cours/pandoc/media/image186.wmf
11-Actions Mécaniques/Cours/pandoc/media/image187.png
11-Actions Mécaniques/Cours/pandoc/media/image188.wmf
11-Actions Mécaniques/Cours/pandoc/media/image189.png
11-Actions Mécaniques/Cours/pandoc/media/image19.wmf
11-Actions Mécaniques/Cours/pandoc/media/image190.png
11-Actions Mécaniques/Cours/pandoc/media/image191.wmf
11-Actions Mécaniques/Cours/pandoc/media/image192.png
11-Actions Mécaniques/Cours/pandoc/media/image193.wmf
11-Actions Mécaniques/Cours/pandoc/media/image194.png
11-Actions Mécaniques/Cours/pandoc/media/image195.png
11-Actions Mécaniques/Cours/pandoc/media/image196.wmf
11-Actions Mécaniques/Cours/pandoc/media/image197.wmf
11-Actions Mécaniques/Cours/pandoc/media/image198.wmf
11-Actions Mécaniques/Cours/pandoc/media/image199.wmf
11-Actions Mécaniques/Cours/pandoc/media/image20.wmf
11-Actions Mécaniques/Cours/pandoc/media/image200.wmf
11-Actions Mécaniques/Cours/pandoc/media/image201.wmf
11-Actions Mécaniques/Cours/pandoc/media/image202.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image203.wmf
11-Actions Mécaniques/Cours/pandoc/media/image204.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image205.png
11-Actions Mécaniques/Cours/pandoc/media/image206.png
11-Actions Mécaniques/Cours/pandoc/media/image207.png
11-Actions Mécaniques/Cours/pandoc/media/image208.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image209.png
11-Actions Mécaniques/Cours/pandoc/media/image21.wmf
11-Actions Mécaniques/Cours/pandoc/media/image210.wmf
11-Actions Mécaniques/Cours/pandoc/media/image211.wmf
11-Actions Mécaniques/Cours/pandoc/media/image212.wmf
11-Actions Mécaniques/Cours/pandoc/media/image213.wmf
11-Actions Mécaniques/Cours/pandoc/media/image214.wmf
11-Actions Mécaniques/Cours/pandoc/media/image215.png
11-Actions Mécaniques/Cours/pandoc/media/image216.wmf
11-Actions Mécaniques/Cours/pandoc/media/image217.wmf
11-Actions Mécaniques/Cours/pandoc/media/image218.wmf
11-Actions Mécaniques/Cours/pandoc/media/image219.wmf
11-Actions Mécaniques/Cours/pandoc/media/image22.png
11-Actions Mécaniques/Cours/pandoc/media/image220.wmf
11-Actions Mécaniques/Cours/pandoc/media/image221.wmf
11-Actions Mécaniques/Cours/pandoc/media/image222.wmf
11-Actions Mécaniques/Cours/pandoc/media/image223.wmf
11-Actions Mécaniques/Cours/pandoc/media/image224.wmf
11-Actions Mécaniques/Cours/pandoc/media/image225.wmf
11-Actions Mécaniques/Cours/pandoc/media/image226.wmf
11-Actions Mécaniques/Cours/pandoc/media/image227.wmf
11-Actions Mécaniques/Cours/pandoc/media/image228.png
11-Actions Mécaniques/Cours/pandoc/media/image229.wmf
11-Actions Mécaniques/Cours/pandoc/media/image23.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image230.wmf
11-Actions Mécaniques/Cours/pandoc/media/image231.wmf
11-Actions Mécaniques/Cours/pandoc/media/image232.wmf
11-Actions Mécaniques/Cours/pandoc/media/image233.wmf
11-Actions Mécaniques/Cours/pandoc/media/image234.wmf
11-Actions Mécaniques/Cours/pandoc/media/image235.png
11-Actions Mécaniques/Cours/pandoc/media/image236.wmf
11-Actions Mécaniques/Cours/pandoc/media/image237.wmf
11-Actions Mécaniques/Cours/pandoc/media/image238.wmf
11-Actions Mécaniques/Cours/pandoc/media/image239.wmf
11-Actions Mécaniques/Cours/pandoc/media/image24.png
11-Actions Mécaniques/Cours/pandoc/media/image240.wmf
11-Actions Mécaniques/Cours/pandoc/media/image241.wmf
11-Actions Mécaniques/Cours/pandoc/media/image242.wmf
11-Actions Mécaniques/Cours/pandoc/media/image243.wmf
11-Actions Mécaniques/Cours/pandoc/media/image244.wmf
11-Actions Mécaniques/Cours/pandoc/media/image245.wmf
11-Actions Mécaniques/Cours/pandoc/media/image246.wmf
11-Actions Mécaniques/Cours/pandoc/media/image247.png
11-Actions Mécaniques/Cours/pandoc/media/image248.wmf
11-Actions Mécaniques/Cours/pandoc/media/image249.wmf
11-Actions Mécaniques/Cours/pandoc/media/image25.png
11-Actions Mécaniques/Cours/pandoc/media/image250.wmf
11-Actions Mécaniques/Cours/pandoc/media/image251.wmf
11-Actions Mécaniques/Cours/pandoc/media/image252.wmf
11-Actions Mécaniques/Cours/pandoc/media/image253.wmf
11-Actions Mécaniques/Cours/pandoc/media/image254.wmf
11-Actions Mécaniques/Cours/pandoc/media/image255.wmf
11-Actions Mécaniques/Cours/pandoc/media/image256.wmf
11-Actions Mécaniques/Cours/pandoc/media/image257.wmf
11-Actions Mécaniques/Cours/pandoc/media/image258.wmf
11-Actions Mécaniques/Cours/pandoc/media/image259.png
11-Actions Mécaniques/Cours/pandoc/media/image26.wmf
11-Actions Mécaniques/Cours/pandoc/media/image260.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image262.wmf
11-Actions Mécaniques/Cours/pandoc/media/image263.png
11-Actions Mécaniques/Cours/pandoc/media/image264.png
11-Actions Mécaniques/Cours/pandoc/media/image265.png
11-Actions Mécaniques/Cours/pandoc/media/image266.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image267.wmf
11-Actions Mécaniques/Cours/pandoc/media/image268.png
11-Actions Mécaniques/Cours/pandoc/media/image269.png
11-Actions Mécaniques/Cours/pandoc/media/image27.wmf
11-Actions Mécaniques/Cours/pandoc/media/image270.png
11-Actions Mécaniques/Cours/pandoc/media/image271.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image272.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image273.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image274.png
11-Actions Mécaniques/Cours/pandoc/media/image275.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image276.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image277.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image278.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image279.png
11-Actions Mécaniques/Cours/pandoc/media/image28.wmf
11-Actions Mécaniques/Cours/pandoc/media/image280.wmf
11-Actions Mécaniques/Cours/pandoc/media/image281.wmf
11-Actions Mécaniques/Cours/pandoc/media/image282.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image283.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image284.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image285.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image286.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image287.png
11-Actions Mécaniques/Cours/pandoc/media/image288.png
11-Actions Mécaniques/Cours/pandoc/media/image289.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image29.wmf
11-Actions Mécaniques/Cours/pandoc/media/image290.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image291.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image292.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image293.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image294.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image295.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image296.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image297.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image298.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image299.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image3.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image30.wmf
11-Actions Mécaniques/Cours/pandoc/media/image300.wmf
11-Actions Mécaniques/Cours/pandoc/media/image301.wmf
11-Actions Mécaniques/Cours/pandoc/media/image302.wmf
11-Actions Mécaniques/Cours/pandoc/media/image303.wmf
11-Actions Mécaniques/Cours/pandoc/media/image304.wmf
11-Actions Mécaniques/Cours/pandoc/media/image305.wmf
11-Actions Mécaniques/Cours/pandoc/media/image306.wmf
11-Actions Mécaniques/Cours/pandoc/media/image31.wmf
11-Actions Mécaniques/Cours/pandoc/media/image315.wmf
11-Actions Mécaniques/Cours/pandoc/media/image316.wmf
11-Actions Mécaniques/Cours/pandoc/media/image317.png
11-Actions Mécaniques/Cours/pandoc/media/image318.png
11-Actions Mécaniques/Cours/pandoc/media/image319.png
11-Actions Mécaniques/Cours/pandoc/media/image32.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image320.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image321.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image322.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image323.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image324.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image325.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image326.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image327.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image328.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image329.wmf
11-Actions Mécaniques/Cours/pandoc/media/image33.wmf
11-Actions Mécaniques/Cours/pandoc/media/image330.wmf
11-Actions Mécaniques/Cours/pandoc/media/image331.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image332.png
11-Actions Mécaniques/Cours/pandoc/media/image333.png
11-Actions Mécaniques/Cours/pandoc/media/image334.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image335.wmf
11-Actions Mécaniques/Cours/pandoc/media/image336.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image337.wmf
11-Actions Mécaniques/Cours/pandoc/media/image338.png
11-Actions Mécaniques/Cours/pandoc/media/image339.png
11-Actions Mécaniques/Cours/pandoc/media/image34.wmf
11-Actions Mécaniques/Cours/pandoc/media/image340.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image341.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image342.emf
11-Actions Mécaniques/Cours/pandoc/media/image343.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image345.png
11-Actions Mécaniques/Cours/pandoc/media/image346.png
11-Actions Mécaniques/Cours/pandoc/media/image347.wmf
11-Actions Mécaniques/Cours/pandoc/media/image348.wmf
11-Actions Mécaniques/Cours/pandoc/media/image349.wmf
11-Actions Mécaniques/Cours/pandoc/media/image35.wmf
11-Actions Mécaniques/Cours/pandoc/media/image350.wmf
11-Actions Mécaniques/Cours/pandoc/media/image351.wmf
11-Actions Mécaniques/Cours/pandoc/media/image352.wmf
11-Actions Mécaniques/Cours/pandoc/media/image353.png
11-Actions Mécaniques/Cours/pandoc/media/image354.wmf
11-Actions Mécaniques/Cours/pandoc/media/image355.png
11-Actions Mécaniques/Cours/pandoc/media/image356.wmf
11-Actions Mécaniques/Cours/pandoc/media/image357.wmf
11-Actions Mécaniques/Cours/pandoc/media/image358.wmf
11-Actions Mécaniques/Cours/pandoc/media/image359.wmf
11-Actions Mécaniques/Cours/pandoc/media/image36.png
11-Actions Mécaniques/Cours/pandoc/media/image360.emf
11-Actions Mécaniques/Cours/pandoc/media/image361.emf
11-Actions Mécaniques/Cours/pandoc/media/image362.emf
11-Actions Mécaniques/Cours/pandoc/media/image363.wmf
11-Actions Mécaniques/Cours/pandoc/media/image364.wmf
11-Actions Mécaniques/Cours/pandoc/media/image365.wmf
11-Actions Mécaniques/Cours/pandoc/media/image366.wmf
11-Actions Mécaniques/Cours/pandoc/media/image367.png
11-Actions Mécaniques/Cours/pandoc/media/image368.wmf
11-Actions Mécaniques/Cours/pandoc/media/image369.wmf
11-Actions Mécaniques/Cours/pandoc/media/image37.wmf
11-Actions Mécaniques/Cours/pandoc/media/image370.wmf
11-Actions Mécaniques/Cours/pandoc/media/image371.wmf
11-Actions Mécaniques/Cours/pandoc/media/image372.wmf
11-Actions Mécaniques/Cours/pandoc/media/image373.wmf
11-Actions Mécaniques/Cours/pandoc/media/image374.wmf
11-Actions Mécaniques/Cours/pandoc/media/image375.wmf
11-Actions Mécaniques/Cours/pandoc/media/image376.wmf
11-Actions Mécaniques/Cours/pandoc/media/image377.wmf
11-Actions Mécaniques/Cours/pandoc/media/image378.png
11-Actions Mécaniques/Cours/pandoc/media/image379.png
11-Actions Mécaniques/Cours/pandoc/media/image38.png
11-Actions Mécaniques/Cours/pandoc/media/image380.png
11-Actions Mécaniques/Cours/pandoc/media/image381.png
11-Actions Mécaniques/Cours/pandoc/media/image382.png
11-Actions Mécaniques/Cours/pandoc/media/image383.png
11-Actions Mécaniques/Cours/pandoc/media/image384.png
11-Actions Mécaniques/Cours/pandoc/media/image385.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image388.png
11-Actions Mécaniques/Cours/pandoc/media/image389.png
11-Actions Mécaniques/Cours/pandoc/media/image39.wmf
11-Actions Mécaniques/Cours/pandoc/media/image390.emf
11-Actions Mécaniques/Cours/pandoc/media/image391.png
11-Actions Mécaniques/Cours/pandoc/media/image392.wmf
11-Actions Mécaniques/Cours/pandoc/media/image393.wmf
11-Actions Mécaniques/Cours/pandoc/media/image394.wmf
11-Actions Mécaniques/Cours/pandoc/media/image395.wmf
11-Actions Mécaniques/Cours/pandoc/media/image396.wmf
11-Actions Mécaniques/Cours/pandoc/media/image397.wmf
11-Actions Mécaniques/Cours/pandoc/media/image398.wmf
11-Actions Mécaniques/Cours/pandoc/media/image399.wmf
11-Actions Mécaniques/Cours/pandoc/media/image40.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image400.wmf
11-Actions Mécaniques/Cours/pandoc/media/image401.png
11-Actions Mécaniques/Cours/pandoc/media/image402.wmf
11-Actions Mécaniques/Cours/pandoc/media/image403.wmf
11-Actions Mécaniques/Cours/pandoc/media/image404.wmf
11-Actions Mécaniques/Cours/pandoc/media/image405.png
11-Actions Mécaniques/Cours/pandoc/media/image406.png
11-Actions Mécaniques/Cours/pandoc/media/image407.png
11-Actions Mécaniques/Cours/pandoc/media/image408.png
11-Actions Mécaniques/Cours/pandoc/media/image409.wmf
11-Actions Mécaniques/Cours/pandoc/media/image41.wmf
11-Actions Mécaniques/Cours/pandoc/media/image410.wmf
11-Actions Mécaniques/Cours/pandoc/media/image411.wmf
11-Actions Mécaniques/Cours/pandoc/media/image412.wmf
11-Actions Mécaniques/Cours/pandoc/media/image413.wmf
11-Actions Mécaniques/Cours/pandoc/media/image414.wmf
11-Actions Mécaniques/Cours/pandoc/media/image415.wmf
11-Actions Mécaniques/Cours/pandoc/media/image416.png
11-Actions Mécaniques/Cours/pandoc/media/image417.wmf
11-Actions Mécaniques/Cours/pandoc/media/image418.wmf
11-Actions Mécaniques/Cours/pandoc/media/image419.wmf
11-Actions Mécaniques/Cours/pandoc/media/image42.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image420.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image421.png
11-Actions Mécaniques/Cours/pandoc/media/image423.png
11-Actions Mécaniques/Cours/pandoc/media/image424.wmf
11-Actions Mécaniques/Cours/pandoc/media/image425.wmf
11-Actions Mécaniques/Cours/pandoc/media/image426.wmf
11-Actions Mécaniques/Cours/pandoc/media/image427.wmf
11-Actions Mécaniques/Cours/pandoc/media/image428.wmf
11-Actions Mécaniques/Cours/pandoc/media/image429.wmf
11-Actions Mécaniques/Cours/pandoc/media/image43.wmf
11-Actions Mécaniques/Cours/pandoc/media/image430.wmf
11-Actions Mécaniques/Cours/pandoc/media/image431.png
11-Actions Mécaniques/Cours/pandoc/media/image432.png
11-Actions Mécaniques/Cours/pandoc/media/image433.wmf
11-Actions Mécaniques/Cours/pandoc/media/image434.wmf
11-Actions Mécaniques/Cours/pandoc/media/image435.wmf
11-Actions Mécaniques/Cours/pandoc/media/image436.wmf
11-Actions Mécaniques/Cours/pandoc/media/image437.png
11-Actions Mécaniques/Cours/pandoc/media/image438.png
11-Actions Mécaniques/Cours/pandoc/media/image44.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image440.png
11-Actions Mécaniques/Cours/pandoc/media/image442.png
11-Actions Mécaniques/Cours/pandoc/media/image443.wmf
11-Actions Mécaniques/Cours/pandoc/media/image444.wmf
11-Actions Mécaniques/Cours/pandoc/media/image445.wmf
11-Actions Mécaniques/Cours/pandoc/media/image446.wmf
11-Actions Mécaniques/Cours/pandoc/media/image447.wmf
11-Actions Mécaniques/Cours/pandoc/media/image448.wmf
11-Actions Mécaniques/Cours/pandoc/media/image449.wmf
11-Actions Mécaniques/Cours/pandoc/media/image45.wmf
11-Actions Mécaniques/Cours/pandoc/media/image450.wmf
11-Actions Mécaniques/Cours/pandoc/media/image451.wmf
11-Actions Mécaniques/Cours/pandoc/media/image452.wmf
11-Actions Mécaniques/Cours/pandoc/media/image453.wmf
11-Actions Mécaniques/Cours/pandoc/media/image454.wmf
11-Actions Mécaniques/Cours/pandoc/media/image455.wmf
11-Actions Mécaniques/Cours/pandoc/media/image456.wmf
11-Actions Mécaniques/Cours/pandoc/media/image457.wmf
11-Actions Mécaniques/Cours/pandoc/media/image458.wmf
11-Actions Mécaniques/Cours/pandoc/media/image459.wmf
11-Actions Mécaniques/Cours/pandoc/media/image46.wmf
11-Actions Mécaniques/Cours/pandoc/media/image460.wmf
11-Actions Mécaniques/Cours/pandoc/media/image461.wmf
11-Actions Mécaniques/Cours/pandoc/media/image462.wmf
11-Actions Mécaniques/Cours/pandoc/media/image463.wmf
11-Actions Mécaniques/Cours/pandoc/media/image464.wmf
11-Actions Mécaniques/Cours/pandoc/media/image465.wmf
11-Actions Mécaniques/Cours/pandoc/media/image466.wmf
11-Actions Mécaniques/Cours/pandoc/media/image467.wmf
11-Actions Mécaniques/Cours/pandoc/media/image468.wmf
11-Actions Mécaniques/Cours/pandoc/media/image469.wmf
11-Actions Mécaniques/Cours/pandoc/media/image47.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image470.wmf
11-Actions Mécaniques/Cours/pandoc/media/image471.wmf
11-Actions Mécaniques/Cours/pandoc/media/image472.wmf
11-Actions Mécaniques/Cours/pandoc/media/image473.wmf
11-Actions Mécaniques/Cours/pandoc/media/image474.wmf
11-Actions Mécaniques/Cours/pandoc/media/image475.wmf
11-Actions Mécaniques/Cours/pandoc/media/image476.emf
11-Actions Mécaniques/Cours/pandoc/media/image477.emf
11-Actions Mécaniques/Cours/pandoc/media/image478.emf
11-Actions Mécaniques/Cours/pandoc/media/image479.emf
11-Actions Mécaniques/Cours/pandoc/media/image48.wmf
11-Actions Mécaniques/Cours/pandoc/media/image480.emf
11-Actions Mécaniques/Cours/pandoc/media/image481.emf
11-Actions Mécaniques/Cours/pandoc/media/image482.emf
11-Actions Mécaniques/Cours/pandoc/media/image483.emf
11-Actions Mécaniques/Cours/pandoc/media/image484.emf
11-Actions Mécaniques/Cours/pandoc/media/image485.emf
11-Actions Mécaniques/Cours/pandoc/media/image486.emf
11-Actions Mécaniques/Cours/pandoc/media/image487.png
11-Actions Mécaniques/Cours/pandoc/media/image488.png
11-Actions Mécaniques/Cours/pandoc/media/image489.png
11-Actions Mécaniques/Cours/pandoc/media/image49.png
11-Actions Mécaniques/Cours/pandoc/media/image490.png
11-Actions Mécaniques/Cours/pandoc/media/image491.png
11-Actions Mécaniques/Cours/pandoc/media/image492.png
11-Actions Mécaniques/Cours/pandoc/media/image493.png
11-Actions Mécaniques/Cours/pandoc/media/image494.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image495.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image496.png
11-Actions Mécaniques/Cours/pandoc/media/image497.png
11-Actions Mécaniques/Cours/pandoc/media/image498.png
11-Actions Mécaniques/Cours/pandoc/media/image499.png
11-Actions Mécaniques/Cours/pandoc/media/image5.png
11-Actions Mécaniques/Cours/pandoc/media/image50.png
11-Actions Mécaniques/Cours/pandoc/media/image500.png
11-Actions Mécaniques/Cours/pandoc/media/image501.png
11-Actions Mécaniques/Cours/pandoc/media/image502.wmf
11-Actions Mécaniques/Cours/pandoc/media/image503.wmf
11-Actions Mécaniques/Cours/pandoc/media/image504.wmf
11-Actions Mécaniques/Cours/pandoc/media/image505.wmf
11-Actions Mécaniques/Cours/pandoc/media/image506.wmf
11-Actions Mécaniques/Cours/pandoc/media/image507.wmf
11-Actions Mécaniques/Cours/pandoc/media/image508.wmf
11-Actions Mécaniques/Cours/pandoc/media/image509.png
11-Actions Mécaniques/Cours/pandoc/media/image510.png
11-Actions Mécaniques/Cours/pandoc/media/image511.wmf
11-Actions Mécaniques/Cours/pandoc/media/image512.wmf
11-Actions Mécaniques/Cours/pandoc/media/image513.wmf
11-Actions Mécaniques/Cours/pandoc/media/image514.wmf
11-Actions Mécaniques/Cours/pandoc/media/image515.wmf
11-Actions Mécaniques/Cours/pandoc/media/image516.wmf
11-Actions Mécaniques/Cours/pandoc/media/image517.wmf
11-Actions Mécaniques/Cours/pandoc/media/image518.wmf
11-Actions Mécaniques/Cours/pandoc/media/image519.wmf
11-Actions Mécaniques/Cours/pandoc/media/image520.wmf
11-Actions Mécaniques/Cours/pandoc/media/image521.wmf
11-Actions Mécaniques/Cours/pandoc/media/image522.wmf
11-Actions Mécaniques/Cours/pandoc/media/image523.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image524.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image525.wmf
11-Actions Mécaniques/Cours/pandoc/media/image526.wmf
11-Actions Mécaniques/Cours/pandoc/media/image527.wmf
11-Actions Mécaniques/Cours/pandoc/media/image528.wmf
11-Actions Mécaniques/Cours/pandoc/media/image529.wmf
11-Actions Mécaniques/Cours/pandoc/media/image530.wmf
11-Actions Mécaniques/Cours/pandoc/media/image531.wmf
11-Actions Mécaniques/Cours/pandoc/media/image532.wmf
11-Actions Mécaniques/Cours/pandoc/media/image533.wmf
11-Actions Mécaniques/Cours/pandoc/media/image534.png
11-Actions Mécaniques/Cours/pandoc/media/image535.wmf
11-Actions Mécaniques/Cours/pandoc/media/image536.wmf
11-Actions Mécaniques/Cours/pandoc/media/image537.wmf
11-Actions Mécaniques/Cours/pandoc/media/image538.wmf
11-Actions Mécaniques/Cours/pandoc/media/image539.wmf
11-Actions Mécaniques/Cours/pandoc/media/image54.wmf
11-Actions Mécaniques/Cours/pandoc/media/image540.wmf
11-Actions Mécaniques/Cours/pandoc/media/image541.wmf
11-Actions Mécaniques/Cours/pandoc/media/image542.wmf
11-Actions Mécaniques/Cours/pandoc/media/image543.wmf
11-Actions Mécaniques/Cours/pandoc/media/image544.wmf
11-Actions Mécaniques/Cours/pandoc/media/image545.wmf
11-Actions Mécaniques/Cours/pandoc/media/image546.wmf
11-Actions Mécaniques/Cours/pandoc/media/image547.wmf
11-Actions Mécaniques/Cours/pandoc/media/image548.wmf
11-Actions Mécaniques/Cours/pandoc/media/image549.wmf
11-Actions Mécaniques/Cours/pandoc/media/image55.png
11-Actions Mécaniques/Cours/pandoc/media/image550.wmf
11-Actions Mécaniques/Cours/pandoc/media/image551.wmf
11-Actions Mécaniques/Cours/pandoc/media/image552.wmf
11-Actions Mécaniques/Cours/pandoc/media/image553.wmf
11-Actions Mécaniques/Cours/pandoc/media/image554.wmf
11-Actions Mécaniques/Cours/pandoc/media/image555.wmf
11-Actions Mécaniques/Cours/pandoc/media/image556.wmf
11-Actions Mécaniques/Cours/pandoc/media/image557.wmf
11-Actions Mécaniques/Cours/pandoc/media/image558.wmf
11-Actions Mécaniques/Cours/pandoc/media/image559.wmf
11-Actions Mécaniques/Cours/pandoc/media/image56.wmf
11-Actions Mécaniques/Cours/pandoc/media/image560.wmf
11-Actions Mécaniques/Cours/pandoc/media/image561.wmf
11-Actions Mécaniques/Cours/pandoc/media/image562.wmf
11-Actions Mécaniques/Cours/pandoc/media/image563.wmf
11-Actions Mécaniques/Cours/pandoc/media/image564.wmf
11-Actions Mécaniques/Cours/pandoc/media/image565.wmf
11-Actions Mécaniques/Cours/pandoc/media/image566.wmf
11-Actions Mécaniques/Cours/pandoc/media/image567.wmf
11-Actions Mécaniques/Cours/pandoc/media/image568.wmf
11-Actions Mécaniques/Cours/pandoc/media/image569.wmf
11-Actions Mécaniques/Cours/pandoc/media/image57.wmf
11-Actions Mécaniques/Cours/pandoc/media/image570.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image571.png
11-Actions Mécaniques/Cours/pandoc/media/image572.emf
11-Actions Mécaniques/Cours/pandoc/media/image573.png
11-Actions Mécaniques/Cours/pandoc/media/image574.emf
11-Actions Mécaniques/Cours/pandoc/media/image575.wmf
11-Actions Mécaniques/Cours/pandoc/media/image576.wmf
11-Actions Mécaniques/Cours/pandoc/media/image577.emf
11-Actions Mécaniques/Cours/pandoc/media/image578.wmf
11-Actions Mécaniques/Cours/pandoc/media/image579.wmf
11-Actions Mécaniques/Cours/pandoc/media/image58.wmf
11-Actions Mécaniques/Cours/pandoc/media/image580.wmf
11-Actions Mécaniques/Cours/pandoc/media/image581.wmf
11-Actions Mécaniques/Cours/pandoc/media/image582.wmf
11-Actions Mécaniques/Cours/pandoc/media/image583.wmf
11-Actions Mécaniques/Cours/pandoc/media/image584.wmf
11-Actions Mécaniques/Cours/pandoc/media/image585.wmf
11-Actions Mécaniques/Cours/pandoc/media/image586.wmf
11-Actions Mécaniques/Cours/pandoc/media/image587.wmf
11-Actions Mécaniques/Cours/pandoc/media/image588.wmf
11-Actions Mécaniques/Cours/pandoc/media/image589.wmf
11-Actions Mécaniques/Cours/pandoc/media/image59.png
11-Actions Mécaniques/Cours/pandoc/media/image590.wmf
11-Actions Mécaniques/Cours/pandoc/media/image591.wmf
11-Actions Mécaniques/Cours/pandoc/media/image592.wmf
11-Actions Mécaniques/Cours/pandoc/media/image593.wmf
11-Actions Mécaniques/Cours/pandoc/media/image594.wmf
11-Actions Mécaniques/Cours/pandoc/media/image595.wmf
11-Actions Mécaniques/Cours/pandoc/media/image596.wmf
11-Actions Mécaniques/Cours/pandoc/media/image597.wmf
11-Actions Mécaniques/Cours/pandoc/media/image598.wmf
11-Actions Mécaniques/Cours/pandoc/media/image599.wmf
11-Actions Mécaniques/Cours/pandoc/media/image6.png
11-Actions Mécaniques/Cours/pandoc/media/image60.wmf
11-Actions Mécaniques/Cours/pandoc/media/image600.wmf
11-Actions Mécaniques/Cours/pandoc/media/image601.png
11-Actions Mécaniques/Cours/pandoc/media/image602.png
11-Actions Mécaniques/Cours/pandoc/media/image603.wmf
11-Actions Mécaniques/Cours/pandoc/media/image604.wmf
11-Actions Mécaniques/Cours/pandoc/media/image605.wmf
11-Actions Mécaniques/Cours/pandoc/media/image606.wmf
11-Actions Mécaniques/Cours/pandoc/media/image607.wmf
11-Actions Mécaniques/Cours/pandoc/media/image608.wmf
11-Actions Mécaniques/Cours/pandoc/media/image609.wmf
11-Actions Mécaniques/Cours/pandoc/media/image61.wmf
11-Actions Mécaniques/Cours/pandoc/media/image610.wmf
11-Actions Mécaniques/Cours/pandoc/media/image611.wmf
11-Actions Mécaniques/Cours/pandoc/media/image612.wmf
11-Actions Mécaniques/Cours/pandoc/media/image613.wmf
11-Actions Mécaniques/Cours/pandoc/media/image614.wmf
11-Actions Mécaniques/Cours/pandoc/media/image615.png
11-Actions Mécaniques/Cours/pandoc/media/image616.png
11-Actions Mécaniques/Cours/pandoc/media/image618.png
11-Actions Mécaniques/Cours/pandoc/media/image619.png
11-Actions Mécaniques/Cours/pandoc/media/image62.wmf
11-Actions Mécaniques/Cours/pandoc/media/image620.wmf
11-Actions Mécaniques/Cours/pandoc/media/image621.wmf
11-Actions Mécaniques/Cours/pandoc/media/image622.wmf
11-Actions Mécaniques/Cours/pandoc/media/image623.wmf
11-Actions Mécaniques/Cours/pandoc/media/image624.wmf
11-Actions Mécaniques/Cours/pandoc/media/image625.wmf
11-Actions Mécaniques/Cours/pandoc/media/image626.wmf
11-Actions Mécaniques/Cours/pandoc/media/image627.wmf
11-Actions Mécaniques/Cours/pandoc/media/image628.wmf
11-Actions Mécaniques/Cours/pandoc/media/image629.wmf
11-Actions Mécaniques/Cours/pandoc/media/image63.png
11-Actions Mécaniques/Cours/pandoc/media/image630.wmf
11-Actions Mécaniques/Cours/pandoc/media/image631.wmf
11-Actions Mécaniques/Cours/pandoc/media/image632.wmf
11-Actions Mécaniques/Cours/pandoc/media/image633.wmf
11-Actions Mécaniques/Cours/pandoc/media/image634.wmf
11-Actions Mécaniques/Cours/pandoc/media/image635.wmf
11-Actions Mécaniques/Cours/pandoc/media/image636.wmf
11-Actions Mécaniques/Cours/pandoc/media/image637.wmf
11-Actions Mécaniques/Cours/pandoc/media/image638.wmf
11-Actions Mécaniques/Cours/pandoc/media/image639.wmf
11-Actions Mécaniques/Cours/pandoc/media/image64.wmf
11-Actions Mécaniques/Cours/pandoc/media/image640.wmf
11-Actions Mécaniques/Cours/pandoc/media/image641.wmf
11-Actions Mécaniques/Cours/pandoc/media/image642.wmf
11-Actions Mécaniques/Cours/pandoc/media/image643.png
11-Actions Mécaniques/Cours/pandoc/media/image644.wmf
11-Actions Mécaniques/Cours/pandoc/media/image645.wmf
11-Actions Mécaniques/Cours/pandoc/media/image646.wmf
11-Actions Mécaniques/Cours/pandoc/media/image647.wmf
11-Actions Mécaniques/Cours/pandoc/media/image648.wmf
11-Actions Mécaniques/Cours/pandoc/media/image649.wmf
11-Actions Mécaniques/Cours/pandoc/media/image65.wmf
11-Actions Mécaniques/Cours/pandoc/media/image650.wmf
11-Actions Mécaniques/Cours/pandoc/media/image651.wmf
11-Actions Mécaniques/Cours/pandoc/media/image652.wmf
11-Actions Mécaniques/Cours/pandoc/media/image653.wmf
11-Actions Mécaniques/Cours/pandoc/media/image654.wmf
11-Actions Mécaniques/Cours/pandoc/media/image655.wmf
11-Actions Mécaniques/Cours/pandoc/media/image656.wmf
11-Actions Mécaniques/Cours/pandoc/media/image657.wmf
11-Actions Mécaniques/Cours/pandoc/media/image658.png
11-Actions Mécaniques/Cours/pandoc/media/image659.wmf
11-Actions Mécaniques/Cours/pandoc/media/image66.wmf
11-Actions Mécaniques/Cours/pandoc/media/image660.wmf
11-Actions Mécaniques/Cours/pandoc/media/image661.wmf
11-Actions Mécaniques/Cours/pandoc/media/image662.wmf
11-Actions Mécaniques/Cours/pandoc/media/image663.wmf
11-Actions Mécaniques/Cours/pandoc/media/image664.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image665.png
11-Actions Mécaniques/Cours/pandoc/media/image666.png
11-Actions Mécaniques/Cours/pandoc/media/image667.png
11-Actions Mécaniques/Cours/pandoc/media/image668.png
11-Actions Mécaniques/Cours/pandoc/media/image669.png
11-Actions Mécaniques/Cours/pandoc/media/image67.png
11-Actions Mécaniques/Cours/pandoc/media/image670.wmf
11-Actions Mécaniques/Cours/pandoc/media/image671.wmf
11-Actions Mécaniques/Cours/pandoc/media/image672.wmf
11-Actions Mécaniques/Cours/pandoc/media/image673.wmf
11-Actions Mécaniques/Cours/pandoc/media/image674.wmf
11-Actions Mécaniques/Cours/pandoc/media/image675.wmf
11-Actions Mécaniques/Cours/pandoc/media/image676.png
11-Actions Mécaniques/Cours/pandoc/media/image677.wmf
11-Actions Mécaniques/Cours/pandoc/media/image678.png
11-Actions Mécaniques/Cours/pandoc/media/image679.png
11-Actions Mécaniques/Cours/pandoc/media/image68.wmf
11-Actions Mécaniques/Cours/pandoc/media/image680.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image681.png
11-Actions Mécaniques/Cours/pandoc/media/image682.png
11-Actions Mécaniques/Cours/pandoc/media/image683.wmf
11-Actions Mécaniques/Cours/pandoc/media/image684.wmf
11-Actions Mécaniques/Cours/pandoc/media/image685.wmf
11-Actions Mécaniques/Cours/pandoc/media/image686.wmf
11-Actions Mécaniques/Cours/pandoc/media/image687.wmf
11-Actions Mécaniques/Cours/pandoc/media/image688.wmf
11-Actions Mécaniques/Cours/pandoc/media/image689.wmf
11-Actions Mécaniques/Cours/pandoc/media/image69.wmf
11-Actions Mécaniques/Cours/pandoc/media/image690.wmf
11-Actions Mécaniques/Cours/pandoc/media/image691.wmf
11-Actions Mécaniques/Cours/pandoc/media/image692.wmf
11-Actions Mécaniques/Cours/pandoc/media/image693.wmf
11-Actions Mécaniques/Cours/pandoc/media/image694.wmf
11-Actions Mécaniques/Cours/pandoc/media/image695.wmf
11-Actions Mécaniques/Cours/pandoc/media/image696.wmf
11-Actions Mécaniques/Cours/pandoc/media/image697.wmf
11-Actions Mécaniques/Cours/pandoc/media/image698.wmf
11-Actions Mécaniques/Cours/pandoc/media/image699.wmf
11-Actions Mécaniques/Cours/pandoc/media/image7.png
11-Actions Mécaniques/Cours/pandoc/media/image70.wmf
11-Actions Mécaniques/Cours/pandoc/media/image700.wmf
11-Actions Mécaniques/Cours/pandoc/media/image701.wmf
11-Actions Mécaniques/Cours/pandoc/media/image703.wmf
11-Actions Mécaniques/Cours/pandoc/media/image704.wmf
11-Actions Mécaniques/Cours/pandoc/media/image705.wmf
11-Actions Mécaniques/Cours/pandoc/media/image706.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image707.png
11-Actions Mécaniques/Cours/pandoc/media/image708.wmf
11-Actions Mécaniques/Cours/pandoc/media/image709.wmf
11-Actions Mécaniques/Cours/pandoc/media/image71.png
11-Actions Mécaniques/Cours/pandoc/media/image710.wmf
11-Actions Mécaniques/Cours/pandoc/media/image711.wmf
11-Actions Mécaniques/Cours/pandoc/media/image712.wmf
11-Actions Mécaniques/Cours/pandoc/media/image713.jpeg
11-Actions Mécaniques/Cours/pandoc/media/image714.png
11-Actions Mécaniques/Cours/pandoc/media/image72.wmf
11-Actions Mécaniques/Cours/pandoc/media/image73.wmf
11-Actions Mécaniques/Cours/pandoc/media/image74.wmf
11-Actions Mécaniques/Cours/pandoc/media/image75.png
11-Actions Mécaniques/Cours/pandoc/media/image76.wmf
11-Actions Mécaniques/Cours/pandoc/media/image77.wmf
11-Actions Mécaniques/Cours/pandoc/media/image78.wmf
11-Actions Mécaniques/Cours/pandoc/media/image79.png
11-Actions Mécaniques/Cours/pandoc/media/image8.png
11-Actions Mécaniques/Cours/pandoc/media/image80.wmf
11-Actions Mécaniques/Cours/pandoc/media/image81.wmf
11-Actions Mécaniques/Cours/pandoc/media/image82.wmf
11-Actions Mécaniques/Cours/pandoc/media/image83.png
11-Actions Mécaniques/Cours/pandoc/media/image84.wmf
11-Actions Mécaniques/Cours/pandoc/media/image85.wmf
11-Actions Mécaniques/Cours/pandoc/media/image86.wmf
11-Actions Mécaniques/Cours/pandoc/media/image87.png
11-Actions Mécaniques/Cours/pandoc/media/image88.wmf
11-Actions Mécaniques/Cours/pandoc/media/image89.wmf
11-Actions Mécaniques/Cours/pandoc/media/image9.png
11-Actions Mécaniques/Cours/pandoc/media/image90.png
11-Actions Mécaniques/Cours/pandoc/media/image91.wmf
11-Actions Mécaniques/Cours/pandoc/media/image92.wmf
11-Actions Mécaniques/Cours/pandoc/media/image93.wmf
11-Actions Mécaniques/Cours/pandoc/media/image94.png
11-Actions Mécaniques/Cours/pandoc/media/image95.wmf
11-Actions Mécaniques/Cours/pandoc/media/image96.wmf
11-Actions Mécaniques/Cours/pandoc/media/image97.wmf
11-Actions Mécaniques/Cours/pandoc/media/image98.wmf
11-Actions Mécaniques/Cours/pandoc/media/image99.wmf
