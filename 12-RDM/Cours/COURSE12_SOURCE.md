![](12-RDM/Cours/pandoc/media/image1.png){width="8.494444444444444in"
height="4.148611111111111in"}

![](12-RDM/Cours/pandoc/media/image3.jpeg){width="4.258837489063867in"
height="2.6969695975503063in"}

Cycle 7 : Dimensionner les pièces d'un mécanisme

**Résistance des matériaux**

Thomas Lusseau

Lycée Robert Doisneau - ATS

# Table des matières {#table-des-matières .TOC-Heading .unnumbered}

[1. Besoin rempli par la résistance des matériaux
[5](#besoin-rempli-par-la-résistance-des-matériaux)](#besoin-rempli-par-la-résistance-des-matériaux)

[2. Hypothèses de la résistance des matériaux
[5](#hypothèses-de-la-résistance-des-matériaux)](#hypothèses-de-la-résistance-des-matériaux)

[2.1. Théorie des poutres droites
[5](#théorie-des-poutres-droites)](#théorie-des-poutres-droites)

[2.2. Matériaux de construction
[6](#matériaux-de-construction)](#matériaux-de-construction)

[2.3. Efforts invariants [6](#efforts-invariants)](#efforts-invariants)

[2.4. Hypothèse de Barré de Saint-Venant
[6](#hypothèse-de-barré-de-saint-venant)](#hypothèse-de-barré-de-saint-venant)

[2.5. Hypothèse de Navier-Bernoulli
[7](#hypothèse-de-navier-bernoulli)](#hypothèse-de-navier-bernoulli)

[2.6. Principe de superposition (de linéarité)
[7](#principe-de-superposition-de-linéarité)](#principe-de-superposition-de-linéarité)

[3. Modélisation des actions mécaniques extérieures
[7](#modélisation-des-actions-mécaniques-extérieures)](#modélisation-des-actions-mécaniques-extérieures)

[3.1. Actions mécaniques extérieures
[7](#actions-mécaniques-extérieures)](#actions-mécaniques-extérieures)

[3.2. Les liaisons [8](#les-liaisons)](#les-liaisons)

[4. Actions mécaniques intérieures (torseur de cohésion)
[8](#actions-mécaniques-intérieures-torseur-de-cohésion)](#actions-mécaniques-intérieures-torseur-de-cohésion)

[4.1. Coupure dans une poutre
[8](#coupure-dans-une-poutre)](#coupure-dans-une-poutre)

[4.2. Détermination du torseur de cohésion
[9](#détermination-du-torseur-de-cohésion)](#détermination-du-torseur-de-cohésion)

[4.3. Nature des sollicitations
[10](#nature-des-sollicitations)](#nature-des-sollicitations)

[5. Traction [11](#traction)](#traction)

[5.1. Définition [11](#définition)](#définition)

[5.2. Contrainte normale [12](#contrainte-normale)](#contrainte-normale)

[5.3. Condition de résistance
[12](#condition-de-résistance)](#condition-de-résistance)

[6. Flexion [13](#flexion)](#flexion)

[6.1. Condition de résistance
[14](#condition-de-résistance-1)](#condition-de-résistance-1)

[6.2. Déformations [14](#déformations)](#déformations)

[7. Sources [14](#sources)](#sources)

[8. Exercices du chapitre
[15](#exercices-du-chapitre)](#exercices-du-chapitre)

Définir les notions de poutre et les hypothèses fondamentales de la
résistance des matériaux

Identifier et caractériser les sollicitations simples.

Je connais :

+------------------------------------------------------------------+---+
| -   Les principales sollicitations : flexion simple, torsion     | ⃝  |
|     simple, traction--compression                                |   |
+==================================================================+===+
| -   L'expression des contraintes et déformations                 | ⃝  |
+------------------------------------------------------------------+---+
| -   Le torseur de cohésion                                       | ⃝  |
+------------------------------------------------------------------+---+
| -   Les notions coefficient de sécurité et résistance mécanique  | ⃝  |
+------------------------------------------------------------------+---+

Je sais :

+------------------------------------------------------------------+---+
| -   Poser les hypothèses nécessaires à une étude de RdM (Poutre, | ⃝  |
|     Navier-Bernoulli, ...)                                       |   |
+==================================================================+===+
| -   Identifier les contraintes, les déformations et les          | ⃝  |
|     sollicitations d'un solide                                   |   |
+------------------------------------------------------------------+---+
| -   Choisir un modèle de solide (indéformable ou déformable) en  | ⃝  |
|     fonction de l'objectif visé                                  |   |
+------------------------------------------------------------------+---+
| -   Déterminer le torseur de cohésion dans un solide             | ⃝  |
+------------------------------------------------------------------+---+
| -   Associer un modèle de contraintes à l'état de sollicitation  | ⃝  |
+------------------------------------------------------------------+---+
| -   Proposer ou justifier des conditions aux limites dans un     | ⃝  |
|     logiciel de simulation par éléments finis                    |   |
+------------------------------------------------------------------+---+
| -   Déterminer la répartition des contraintes dans une section   | ⃝  |
|     droite                                                       |   |
+------------------------------------------------------------------+---+
| -   Vérifier la résistance mécanique d'une poutre droite         | ⃝  |
+------------------------------------------------------------------+---+
| -   Déterminer le coefficient de sécurité par rapport aux        | ⃝  |
|     exigences du cahier des charges fonctionnel                  |   |
+------------------------------------------------------------------+---+
| -   Déterminer l'équation de la flèche dans une poutre droite    | ⃝  |
|     soumise à de la flexion, avec chargements ponctuels ou       |   |
|     répartition linéique constante de pression                   |   |
+------------------------------------------------------------------+---+

## Besoin rempli par la résistance des matériaux

La statique étudie l'équilibre des systèmes de solides, supposés
indéformables. La réalité montre que cette hypothèse fondamentale est
très restrictive et ne peut que rarement être correctement validée. De
plus, certains problèmes de statique (notion d'hyperstatisme) n'ont été
résolus que partiellement.

On introduit donc une nouvelle théorie, la Résistance des Matériaux
(RdM), qui permettra l'étude de solides déformables, à la condition
qu'ils soient modélisables par un élément longiligne : la poutre.

La RdM permet d'étudier les relations déformations-actions extérieures
dans les solides longilignes. La RdM permet aussi de calculer ou de
vérifier le dimensionnement des éléments d'un système mécanique et de
choisir le matériau à travers certains paramètres le caractérisant.

  -----------------------------------------------------------------------------------------------------------------------------------
  ![](12-RDM/Cours/pandoc/media/image5.png)   ![](12-RDM/Cours/pandoc/media/image6.png)   ![](12-RDM/Cours/pandoc/media/image7.png)
  ------------------------------------------- ------------------------------------------- -------------------------------------------
  Géométrie et maillage                       Déplacements                                Contraintes

  -----------------------------------------------------------------------------------------------------------------------------------

Etude d'un bissel (essieu porteur orientable par rapport au châssis) de
wagon

## Hypothèses de la résistance des matériaux

### Théorie des poutres droites

![](12-RDM/Cours/pandoc/media/image8.wmf)Les notions abordées dans ce
cours ne sont valables que pour des solides ayant une forme de
**poutre**, c'est-à-dire un solide pour lequel :

-   Il existe une **ligne moyenne**, continue, passant par les
    barycentres des sections du solide

-   La longueur L est au moins 4 à 5 fois supérieure au diamètre D

-   Il n'y a pas de brusque variation de section (trous, épaulements)

-   Le solide admet un seul et même **plan de symétrie pour les charges
    et la géométrie**

[Remarque]{.underline}

Dans le cas d'un solide constitué de plusieurs poutres droites, il
suffit de décomposer l'étude en autant d'études que de tronçons
rectilignes.

### Matériaux de construction

On suppose que les matériaux de construction possèdent les propriétés
suivantes :

Ils sont **homogènes**, la constitution est la même en chaque point

Ils sont **isotropes**, leurs propriétés physiques sont identiques dans
toutes les directions. L\'isotropie est vérifiée pour les aciers non
fibrés (les aciers laminés et forgés ne sont pas isotropes). Cette
hypothèse n\'est pas vérifiée pour le bois, les matériaux composites,
etc.

Ils sont **continus**, c'est à dire que les discontinuités
microscopiques sont négligées

Ils sont **élastiques** et **linéaires**

### ![](12-RDM/Cours/pandoc/media/image9.emf){width="3.348611111111111in" height="1.96875in"}Efforts invariants

Les déplacements sous charges étant petits, les efforts extérieurs sont
supposés invariants dans R(A,x~0~,y~0~,z~0~) repère lié à la poutre non
déformée avant et après application du chargement. Ainsi, on considère
que δ = 0.

La charge $\overrightarrow{B}$ n'est pas appliquée brutalement mais
progressivement. Les calculs devraient se faire dans la configuration
déformée, qu'on suppose proche donc confondue avec la configuration
initiale.

### Hypothèse de Barré de Saint-Venant

L'état des **sollicitations** (dans la section droite de centre G) dans
une région suffisamment **éloignée des points d'applications des charges
extérieures** appliquées à la poutre ne dépend que du torseur associé à
ces charges. Par éloigné, il faut entendre une distance au moins égale à
la plus grande dimension de la section transversale de la poutre.

+-----------------------------------+---+--------------------------------+
| ![](1                             | 1 | ![](12-RDM/                    |
| 2-RDM/Cours/pandoc/media/image10. | . | Cours/pandoc/media/image10.emf |
| emf){width="2.8018864829396324in" |   | ){width="3.1490452755905514in" |
| height="1.0620494313210849in"}    |   | height="0.905660542432196in"}  |
+===================================+===+================================+
| ~cas\ a~{τ~(S1→S1~}~G~            | = | ~cas\ b~{τ~(S1→S1)~}~G~        |
+-----------------------------------+---+--------------------------------+

### ![](12-RDM/Cours/pandoc/media/image11.emf){width="3.2263888888888888in" height="1.792361111111111in"}Hypothèse de Navier-Bernoulli

Les sections planes, normales à la ligne moyenne avant chargement
demeurent planes et normales à la ligne moyenne après chargement : **pas
de gauchissement (distorsion) des sections droites**

Cette hypothèse s'applique bien aux poutres élancées fléchies, ainsi
qu'à l'étude des sollicitations de traction, compression, torsion des
poutres de section circulaire flexion pure\...

Elle est mise en défaut pour des poutres de section non circulaire,
sollicitées en torsion, et pour des poutres courtes sollicitées en
flexion.

### Principe de superposition (de linéarité)

Les relations actions mécaniques extérieures / réactions aux appuis,
responsables des déformations sont supposées linéaires.

L'effet mécanique dû à un ensemble d'actions mécaniques agissant sur une
poutre dans son domaine élastique est égal à la somme des effets
produits par chaque action mécanique prise séparément.

![](12-RDM/Cours/pandoc/media/image12.emf){width="6.339622703412074in"
height="1.45751312335958in"}

## Modélisation des actions mécaniques extérieures

### Actions mécaniques extérieures

La modélisation du solide par une poutre implique le passage d'un espace
tridimensionnel à un espace unidimensionnel.

De la même façon, la modélisation des actions mécaniques extérieures à
la poutre résulte d'une transposition d'un problème tridimensionnel à un
problème unidimensionnel.

![](12-RDM/Cours/pandoc/media/image13.png){width="0.9805555555555555in"
height="0.4201388888888889in"}![](12-RDM/Cours/pandoc/media/image14.png){width="0.3301891951006124in"
height="0.40321741032370956in"}Les actions mécaniques extérieures
agissant sur la poutre pourront se présenter sous la forme de glisseurs
ou de couples, concentrés (vecteurs liés) ou répartis (charge volumique,
surfacique ou linéique).

![](12-RDM/Cours/pandoc/media/image15.png){width="0.4673611111111111in"
height="0.2923611111111111in"}

[Remarque]{.underline}

Un système d'actions mécaniques extérieures ne peut plus être remplacé
par un système d'actions mécaniques extérieures équivalent comme c'était
le cas en statique.

![](12-RDM/Cours/pandoc/media/image16.emf){width="4.820754593175853in"
height="0.8300251531058618in"}

### Les liaisons

La poutre est reliée au bâti par des liaisons qui induisent une
suppression des certains déplacements. Ces conditions de déplacement (en
translation ou en rotation) permettent d'apporter des renseignements
supplémentaires pour la résolution des problèmes.

+------------------+-----------------+---------------+----------------+
| 2.  ![](12       | 3.  ![](12-RDM/ | 4.  ![](12    | 5.  !          |
| -RDM/Cours/pando | Cours/pandoc/me | -RDM/Cours/pa | [](12-RDM/Cour |
| c/media/image17. | dia/image18.png | ndoc/media/im | s/pandoc/media |
| png){width="0.62 | ){width="0.5941 | age19.png){wi | /image20.png){ |
| 2642169728784in" | 010498687664in" | dth="0.539621 | width="0.68263 |
|                  |                 | 6097987752in" | 12335958006in" |
|   height="0.6944 |  height="0.5471 |     heig      |     he         |
| 860017497813in"} | 69728783902in"} | ht="0.4905653 | ight="0.622641 |
|                  |                 | 980752406in"} | 0761154856in"} |
+==================+=================+===============+================+
| 6.  *[Liaison    | 7.  *[Liaison   | 8.  *[Liaison | 9.  *[Liaison  |
|     encastreme   |     rotule      |     pivot     |     sphère     |
| nt]{.underline}* |     (appui      |     (a        |     cylindre   |
|                  |     fixe        | rticulation)] |     (appui     |
|                  | )]{.underline}* | {.underline}* |     simple)    |
|                  |                 |               | ]{.underline}* |
+------------------+-----------------+---------------+----------------+

## ![](12-RDM/Cours/pandoc/media/image21.wmf)Actions mécaniques intérieures (torseur de cohésion)

### Coupure dans une poutre

Considérons une poutre P, en équilibre sous l'effet d'actions mécaniques
extérieures.

Pour mettre en évidence les efforts transmis par la matière au niveau de
la section S, nous effectuons une **coupure imaginaire** dans un plan
perpendiculaire à la ligne moyenne. Elle sépare la poutre en deux
tronçons E1 et E2, tel que E = E1+E2.

Isolons le tronçon E1.

Les actions mécaniques que le tronçon E2 exerce sur le tronçon E1 à
travers la section droite S sont des actions mécaniques intérieures à la
poutre P.

Nous en ignorons à priori la nature, cependant la liaison entre E1 et E2
peut être modélisée par une liaison complète. On peut donc modéliser
l'action mécanique E2 sur E1 par un torseur appelé :

> **Torseur de cohésion* ***: ![](12-RDM/Cours/pandoc/media/image22.wmf)
> avec G sur la ligne moyenne.

[Vision globale : Torseur de cohésion]{.underline}

### Détermination du torseur de cohésion

Pour ce faire, deux méthodes sont envisageables.

[Isolement du tronçon **g**auche E1]{.underline}

Appliquons le PFS au tronçon
E1 :$\left\{ \tau_{(\overline{E1} \rightarrow E1)} \right\} = \left\{ \tau_{(\overline{E} \rightarrow E1)} \right\} + \left\{ \tau_{(E2 \rightarrow E1)} \right\} = \left\{ 0 \right\}$

D'où ![](12-RDM/Cours/pandoc/media/image23.wmf)

[Isolement du tronçon **d**roit E2]{.underline}

Appliquons le PFS au tronçon
E2 :$\left\{ \tau_{(\overline{E2} \rightarrow E2)} \right\} = \left\{ \tau_{(\overline{E} \rightarrow E2)} \right\} + \left\{ \tau_{(E1 \rightarrow E2)} \right\} = \left\{ 0 \right\}$

Soit
$\left\{ \tau_{(E1 \rightarrow E2)} \right\} = \  - \left\{ \tau_{(\overline{E} \rightarrow E2)} \right\}$

D'où ![](12-RDM/Cours/pandoc/media/image24.wmf)

[Remarques]{.underline}

-   Différentes notations coexistent pour désigner les tronçons gauche
    et droite :

Tronçon gauche = E1 (dans ce cours) = g (pour gauche) = x-

Tronçon droite = E2 (dans ce cours) = d (pour droite) = x+

Ainsi, avec la dernière notation, le torseur de cohésion s'écrira
$\left\{ T_{coh} \right\} = \left\{ T_{x + \rightarrow x -} \right\} = + \left\{ T_{ext \rightarrow x +} \right\} = - \left\{ T_{ext \rightarrow x -} \right\}$

-   Le torseur de cohésion est toujours exprimé au barycentre G de la
    section considérée

    *[Composantes du torseur de cohésion]{.underline}*

![](12-RDM/Cours/pandoc/media/image25.wmf)

> N : Effort **n**ormal sur (G,x), il est perpendiculaire à la section
> droite
>
> R T~y~ : Effort **t**ranchant sur (G,y)
>
> T~z~ : Effort **t**ranchant sur (G,z)
>
> Mt : Moment de **t**orsion sur (G,x), d'axe perpendiculaire à la
> section droite
>
> M~G~ Mf~y~ : Moment de **f**lexion sur (G,y)
>
> Mf~z~ : Moment de **f**lexion sur (G,z)

![](12-RDM/Cours/pandoc/media/image26.png){width="3.4256944444444444in"
height="2.3958333333333335in"}

### Nature des sollicitations

En fonction de « l'allure » du torseur de cohésion, une typologie des
**sollicitations** est établie.

On appelle **sollicitation simple** l\'état de contrainte d'une poutre
dont le torseur de cohésion ne comporte qu\'un élément.

On appelle **sollicitation composée** l'état de sollicitation d'une
poutre soumise à **plusieurs sollicitations simples** (par exemple :
traction + flexion pure).

+----------------+------+---------+--------+--------+----------------+
| **Nature des   | **Ef | *       | **     | **     | **Torseur de   |
| so             | fort | *Effort | Moment | Moment | cohésion**     |
| llicitations** | Norm | Tran    | de**   | de**   |                |
|                | al** | chant** |        |        |                |
|                |      |         | **Tor  | **Fle  |                |
|                |      |         | sion** | xion** |                |
+----------------+------+---------+--------+--------+----------------+
| **Traction     | N    | T~y~ =  | Mt=0   | Mf~y~  | ![](12-RDM/Cou |
| (N\>0)**       |      | 0       |        | = 0    | rs/pandoc/medi |
|                |      |         |        |        | a/image27.wmf) |
| **Compression  |      | T~z~ =  |        | Mf~z~  |                |
| (N\<0)**       |      | 0       |        | = 0    |                |
+----------------+------+---------+--------+--------+----------------+
| **Cisaillement | N=0  | T~y~ OU | Mt=0   | Mf~y~  | ![](12-RDM/Cou |
| simple**       |      | T~z~    |        | = 0    | rs/pandoc/medi |
|                |      |         |        |        | a/image28.wmf) |
|                |      |         |        | Mf~z~  |                |
|                |      |         |        | = 0    |                |
+----------------+------+---------+--------+--------+----------------+
| **Torsion      | N=0  | T~y~ =  | Mt     | Mf~y~  | ![](12-RDM/Cou |
| simple**       |      | 0       |        | = 0    | rs/pandoc/medi |
|                |      |         |        |        | a/image29.wmf) |
|                |      | T~z~ =  |        | Mf~z~  |                |
|                |      | 0       |        | = 0    |                |
+----------------+------+---------+--------+--------+----------------+
| **Flexion      | N=0  | T~y~ =  | Mt=0   | Mf~y~  | ![](12-RDM/Cou |
| pure**         |      | 0       |        | OU     | rs/pandoc/medi |
|                |      |         |        | Mf~z~  | a/image30.wmf) |
|                |      | T~z~ =  |        |        |                |
|                |      | 0       |        |        |                |
+----------------+------+---------+--------+--------+----------------+
| **Flexion      | N=0  | T~y~ OU | Mt=0   | Mf~y~  | ![](12-RDM/Cou |
| simple**       |      | T~z~    |        | OU     | rs/pandoc/medi |
|                |      |         |        | Mf~z~  | a/image31.wmf) |
+----------------+------+---------+--------+--------+----------------+

[Vision locale : Contrainte en un point d'une poutre]{.underline}

![](12-RDM/Cours/pandoc/media/image32.wmf)Les efforts de cohésion, dont
on connaît les éléments de réduction en G (grâce au torseur de
cohésion), sont des actions mécaniques que le tronçon E2 de la poutre
exerce sur le tronçon E1 à travers une section droite fictive S. La loi
de répartition dans cette section S de ces efforts élémentaires est
inconnue.

Regardons de plus près ce qui se passe dans cette coupure. Notons ∆f
l'action mécanique élémentaire au point M et ∆S l'élément de surface
entourant ce point.

Appelons n la normale extérieure en M au plan de la section S.

On appelle **vecteur contrainte** en M, relativement à la surface
élémentaire ∆S, orientée par la normale extérieure n, le vecteur noté
![](12-RDM/Cours/pandoc/media/image33.wmf) tel que :
![](12-RDM/Cours/pandoc/media/image34.wmf)

On appelle **contrainte
normale**![](12-RDM/Cours/pandoc/media/image35.wmf) la projection de
![](12-RDM/Cours/pandoc/media/image33.wmf) sur la normale extérieure n.

On appelle **contrainte
tangentielle**![](12-RDM/Cours/pandoc/media/image36.wmf) la projection
de ![](12-RDM/Cours/pandoc/media/image33.wmf) sur le plan de la facette
∆S.

Par conséquent ![](12-RDM/Cours/pandoc/media/image37.wmf)

Une contrainte s'exprime en Mpa = N/mm^2^

## Traction

### Définition

Une poutre est sollicitée en traction lorsque les actions aux extrémités
se réduisent à deux forces égales et opposées, portées par la ligne
moyenne Lm.

![](12-RDM/Cours/pandoc/media/image38.emf)

L'effort F est appelé **effort normal**, il est noté N. Quelle que soit
la section considérée de la poutre, il s'exerce toujours au barycentre G
de la section.

![](12-RDM/Cours/pandoc/media/image39.emf)

### Contrainte normale

+-----------+----------------------------------------------------------+
| ![](12    | Chaque élément de surface ∆S supporte un effort de       |
| -RDM/Cour | traction ∆f parallèle à la ligne moyenne.                |
| s/pandoc/ |                                                          |
| media/ima | Il y a répartition uniforme des contraintes dans la      |
| ge40.wmf) | section droite. D'où :                                   |
|           |                                                          |
|           | > ![](12-RDM/Cours/pandoc/media/image41.wmf)             |
+-----------+----------------------------------------------------------+

### Condition de résistance

Soient :

-   K~t~ le coefficient de concentration de contrainte : σ~maxi~ =
    K~t~×σ

-   R~e~ la résistance élastique du matériau (en Mpa)

-   s un coefficient de sécurité

-   R~pe~ la résistance pratique à la traction, avec R~pe~ = R~e~÷s

Alors, la condition de résistance s'écrit : σ~maxi~≤R~pe~

![](12-RDM/Cours/pandoc/media/image42.png){width="2.6145833333333335in"
height="1.3541666666666667in"}[Déformations]{.underline}

Soient :

-   L~0~ : longueur initiale de la poutre (en mm)

-   L : longueur de la poutre après déformation (en mm)

-   ∆L : Allongement de la poutre (en mm)

-   ε : Allongement relatif de la poutre (sans unité)

> ε = ∆L÷L~0~ ou ∆L = ε×L~0~

[Coefficient de Poisson]{.underline}

Il traduit un rapport de proportionnalité entre l'allongement
longitudinale (ε~L~) et l'allongement transversal (ε~D~)

> ε~D~ = -ν×ε~L~

*ν≈ 0,3 pour l'acier*

[Loi de Hooke]{.underline}

En déformation élastique, la contrainte σ varie linéairement en fonction
de l'allongement relatif ε.

σ = E×ε

![def_tract.gif](12-RDM/Cours/pandoc/media/image43.png){width="2.6020833333333333in"
height="1.3423611111111111in"}*E ≈ 210000 MPa pour l'acier*

+-------+--------------------------------------------------------------+
| > !   | **Tirant**                                                   |
| [](12 |                                                              |
| -RDM/ | Un tirant de 2 m de long supporte dans une section droite un |
| Cours | effort normal d'extension de N = 5000 N. Il est en acier     |
| /pand | pour lequel : R~e~ = 300 Mpa et E = 200000 Mpa. Déterminer   |
| oc/me | son diamètre minimal Ø et son allongement∆L, en prenant un   |
| dia/i | coefficient de sécurité s = 1,7.                             |
| mage4 |                                                              |
| 4.png |                                                              |
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

## Flexion

![](12-RDM/Cours/pandoc/media/image45.emf)[Contrainte
normale]{.underline}

> $$\sigma = E \times \frac{y}{\rho} = E \times y \times \frac{\Delta\theta}{L_{0}}$$

$$\sigma = \frac{Mf_{z}}{I_{Gz}} \times y\ ou\text{ M}\text{f}_{z} = \frac{E}{\rho} \times I_{\text{Gz}}$$

![](12-RDM/Cours/pandoc/media/image46.png){width="1.7069444444444444in"
height="2.453472222222222in"}

### Condition de résistance

Soient :

-   K~f~ le coefficient de concentration de contrainte : σ~maxi~ =
    K~f~×σ~moyen~

-   R~e~ la résistance élastique à l'extension du matériau (en Mpa)

-   s un coefficient de sécurité

-   R~pe~ la résistance pratique à l'extension, avec R~pe~ = R~e~÷s

Alors, la condition de résistance s'écrit : σ~maxi~≤R~pe~ et/ou f =
y~max~≤y~limite~ pour les contraintes technologiques

### Déformations

+--------------------+-------------------+---------------+------------+
| Equation           | ***Disposition    | ***Moment     | ***Flèche  |
| différentielle de  | des charges***    | fléchissant   | maxi f     |
| la déformée :      |                   | Mf (Nm)***    | (mm)***    |
|                    |                   |               |            |
| $$\text{y''} =     |                   |               |            |
|  \frac{\text{M}\te |                   |               |            |
| xt{f}_{z}}{E \time |                   |               |            |
| s I_{\text{Gz}}}$$ |                   |               |            |
|                    |                   |               |            |
| E : Module d'Young |                   |               |            |
| (en MPa)           |                   |               |            |
|                    |                   |               |            |
| I~Gz~ : Moment     |                   |               |            |
| quadratique (en    |                   |               |            |
| mm^4^)             |                   |               |            |
|                    |                   |               |            |
| Mf~z~ : Moment de  |                   |               |            |
| flexion (en Nmm)   |                   |               |            |
|                    |                   |               |            |
| F : Effort (N)     |                   |               |            |
| pour les charges   |                   |               |            |
| concentrées        |                   |               |            |
|                    |                   |               |            |
| F : Effort         |                   |               |            |
| linéique (N/mm)    |                   |               |            |
| pour les charges   |                   |               |            |
| réparties          |                   |               |            |
+====================+===================+===============+============+
|                    | ![](12-R          | ![]           | ![         |
|                    | DM/Cours/pandoc/m | (12-RDM/Cours | ](12-RDM/C |
|                    | edia/image47.png) | /pandoc/media | ours/pando |
|                    |                   | /image48.wmf) | c/media/im |
|                    | *Poutre sur 2     |               | age49.wmf) |
|                    | appuis*           |               |            |
+--------------------+-------------------+---------------+------------+
|                    | ![](12-R          | ![]           | ![         |
|                    | DM/Cours/pandoc/m | (12-RDM/Cours | ](12-RDM/C |
|                    | edia/image50.png) | /pandoc/media | ours/pando |
|                    |                   | /image51.wmf) | c/media/im |
|                    |                   |               | age52.wmf) |
+--------------------+-------------------+---------------+------------+
|                    | ![](12-R          | ![]           | ![         |
|                    | DM/Cours/pandoc/m | (12-RDM/Cours | ](12-RDM/C |
|                    | edia/image53.png) | /pandoc/media | ours/pando |
|                    |                   | /image54.wmf) | c/media/im |
|                    | *Poutre           |               | age55.wmf) |
|                    | encastrée*        |               |            |
+--------------------+-------------------+---------------+------------+
|                    | ![](12-R          | ![]           | ![         |
|                    | DM/Cours/pandoc/m | (12-RDM/Cours | ](12-RDM/C |
|                    | edia/image56.png) | /pandoc/media | ours/pando |
|                    |                   | /image57.wmf) | c/media/im |
|                    |                   |               | age58.wmf) |
+--------------------+-------------------+---------------+------------+

## Sources

Ce cours a été élaboré à l'aide de nombreuses ressources provenant de
documents publics d'industriels, des activités pédagogiques de collègues
de l'UPSTI.

## Exercices du chapitre

![](12-RDM/Cours/pandoc/media/image59.png){width="5.466666666666667in"
height="8.373527996500437in"}

![](12-RDM/Cours/pandoc/media/image60.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**TRACTION - COMPRESSION**

*([Source]{.underline} : Jérôme Letard)*

![traction-compression\\cable1.TIF](12-RDM/Cours/pandoc/media/image61.png){width="3.671527777777778in"
height="2.433333333333333in"}**Exercice 1 : Choix d'un câble**

On se propose de soulever une poutre de béton armé de 6 m de longueur et
dont la masse est de 2 tonnes.

Pour cela, on dispose symétriquement de deux sangles séparées d'une
distance a. Chaque sangle comporte un anneau sur lequel on ancre les
crochets d'une élingue formée de deux brins de câble de longueur l = 4 m
chacun.

Le câble de diamètre d est constitué de six torons de 19 fils de
diamètre d = 0,8 mm chacun et d'une âme textile(AT) dont on néglige la
résistance mécanique.

**1.** Déterminer la tension maximale dans un câble.

![traction-compression\\cable2.TIF](12-RDM/Cours/pandoc/media/image62.png){width="3.935416666666667in"
height="2.1104166666666666in"}**2.** Le coefficient de sécurité étant s
= 6 pour les structures de levage, en déduire le diamètre du câble à
choisir.

**3.** La contrainte limite élastique d'un fil est : R~e~ = 1770 N/mm².
Déterminer le coefficient de sécurité effectif

**Exercice 2 : Câble de puits de mine**

![](12-RDM/Cours/pandoc/media/image63.png){width="1.19375in"
height="2.453472222222222in"}[Objectif :]{.underline} Déterminer la
forme d'égale résistance d'un câble soumis à son propre poids et
supportant une nacelle de F = 2.10^3^daNen son extrémité.

[Caractéristiques du câble :]{.underline}

Poids volumique : ω =7,8 daN/dm^3^

Matière : acier, d'où une contrainte admissible : R~pe~=100MPa

Longueur L = 500 m

[Questions :]{.underline}

**1.** Soit un câble de diamètre Ø variable (pour obtenir la même
contrainte dans toutes les sections). On montre alors que la section
s'exprime par ![](12-RDM/Cours/pandoc/media/image64.wmf). Déterminer les
diamètres extrêmes du câble.

**2.** Soit un câble de section constante. Déterminer le diamètre du
câble supportant la même nacelle.

**3.** Calculer la masse respective des 2 câbles précédents.

**Exercice 3 : Bielle moteur**

[Compression]{.underline}

Une bielle de moteur diesel est soumise à un effort maximal de
compression de 150.10^3^ N. La partie centrale de cette bielle est
modélisée par un prisme de section S=300 mm² et de longueur L = 180 mm.

**1.** Si on adopte un coefficient de sécurité s = 1,2 quelle doit être
la limite R~e~ de l'acier spécial utilisé ?

**2.** Si le module d'élasticité longitudinale de cet acier vaut E =
2.10^5^MPa, quel est le raccourcissement de cette bielle lors de la
valeur maximale de l'effort de compression ?

[Parois minces]{.underline}

Le moteur diesel a un piston de diamètre d = 155 mm et il règne dans la
chambre d'explosion une pression effective p=8MPa. La chemise du
cylindre est un tube (longueur L, diamètre intérieur d et épaisseur e)
en fonte spéciale pour laquelle la contrainte pratique à l'extension
peut être prise égale à R~pe~ = 50 MPa. On admettra que l'épaisseur de
la paroi de la chemise est faible devant son diamètre intérieur d.

A l'intérieur de ce tube règne une pression p~i~.

Soit S la surface hachurée du tube.

L'effort normal est défini par N = p×L×d avec p = p~i~ -- p~atm~.

**3.** Calculer l'épaisseur à donner à la chemise.

**Exercice 4 : Maillon de chaîne**

![traction-compression\\chaine.TIF](12-RDM/Cours/pandoc/media/image65.png){width="2.3958333333333335in"
height="2.9618055555555554in"}[Mise en situation]{.underline}

La figure ci-contre représente une chaîne à rouleaux destinée à
transmettre une puissance rotative entre deux arbres parallèles. On se
propose d'étudier la résistance de la plaquette 1 à la sollicitation de
traction.

Le perçage situé dans le plan de coupe A-A engendre, dans la plaquette
étudiée, une concentration de contraintes normales caractérisée par le
coefficient K~tp~ = 1,6.

De même, on associe le coefficient K~tr~ = 1,05 à la réduction de la
section située au niveau du plan de coupe B.

L'acier qui constitue la pièce 1 a pour caractéristiques :

R~m~ = 1300 MPa, R~e~ = 1100 MPa, E = 2,2.10^5^ MPa.

[Questions]{.underline}

**1.** Evaluer F~lim~, charge de limite à la rupture de la chaîne en
traction statique.

**2.** En fonctionnement dynamique, dans une application particulière,
on impose un coefficient de sécurité s = 3. Quelle est alors la charge
maximale en service F~max~ ?

![](12-RDM/Cours/pandoc/media/image60.png){width="1.3555555555555556in"
height="0.3888888888888889in"} **FARDELEUSE**

*([Source]{.underline} : CCPTSI 2011)*

\*Etude des roulements menée en TSI1

**Mise en situation**

![http://www.benelite.com/v2/site/images/annonces/FAD-250.jpg](12-RDM/Cours/pandoc/media/image66.jpeg){width="3.254861111111111in"
height="2.5in"}

Le fardelage consiste à déposer un film plastique thermo-rétractable
puis à le chauffer pour qu'il épouse la forme du produit à emballer.
Cette opération est réalisée sur la fardeleuse ci-contre

Le produit à fardeler est convoyé par l'ensemble de motorisation
ci-dessous

![](12-RDM/Cours/pandoc/media/image67.png){width="3.905660542432196in"
height="1.0209962817147857in"}

![](12-RDM/Cours/pandoc/media/image68.png){width="2.5881944444444445in"
height="1.4902777777777778in"}

![](12-RDM/Cours/pandoc/media/image69.png){width="4.169444444444444in"
height="1.2236111111111112in"}Le tapis est entrainé par deux cylindres :
le cylindre moteur et le cylindre tendeur. Le tapis est entrainé par
adhérence. Pour que la transmission de puissance se fasse sans
glissement, le tapis doitêtre tendu. A l'arrêt, la tension **T~0~** est
réglée en translatant l'axe du cylindre tendeur.

On considérera que le tapis est positionné symétriquement sur chaque
cylindre.

Le cylindre tendeurest guidé en rotation par rapport à l'axe lié au bâti
par deux roulements en B et C. L'ensemblepouvant se déplacer par rapport
au bâti pour tendre le tapis.

**Dimensionnement de l'axe de la liaison pivot**

L'axe permettant de guider en rotation le cylindre récepteur est soumis
à des actions mécaniques.

On cherche tout d'abord à le dimensionner. L'axe sera considéré
cylindrique de diamètre d. On retient le modèle poutre et les conditions
limites suivantes pour l'axe :

Conditions limites sur l'axe

On suppose que l'axe est sur deux appuis en A et D et que les deux
roulements exercent deux efforts en B et C :

$\overrightarrow{F}$ = -F.y avec F = 230 N.

**1.** Donner la relation entre **T~0~**, la tension du tapis et **F**,
la norme des efforts en B et C.

**2.** Donner la résultante des efforts aux appuis en A et D sur l'axe
en fonction de **F**.

**3.** Exprimer les composantes du torseur de cohésion le long de la
poutre et tracer les diagrammes correspondants. A quelle sollicitation
est soumise la poutre ?

**4.** En négligeant l'effort tranchant T~y~, quelle zone de la poutre
est la plus sollicitée ?

**5.** Déterminer la contrainte maximale dans la poutre
$\sigma_{{xx}_{\max}}$

Pour dimensionner l'axe, on souhaite que la contrainte normale soit
inférieure à la limite élastique R~e~, corrigée d'un coefficient de
sécurité S~c~ supérieur à 1. On considérera S~c~ = 2.

**6.** Donner l'expression du diamètre minimal d~mini~ respectant le
critère de dimensionnement.

**Choix d'un matériau pour l'axe de la liaison pivot**

Pour l'axe, il a été choisi d'acheter des barres cylindriques chez un
métallurgiste. Il existe des barres avec des diamètres de 3 mm à 50 mm.
On donne dans le tableau suivant les différents aciers possibles pour
l'axe de la liaison pivot.

  ------------------------------------------------------------------------
  Acier           Etat                     R~e~ en MPa     R~m~ en MPa
  --------------- ------------------------ --------------- ---------------
  C22             Normalisé                240             430

                  Trempé et revenu         340             650

  C55             Normalisé                370             680

                  Trempé et revenu         550             950

  15 Cr Ni 6      Trempé et revenu         650             1000

  25 Cr Mo 4      Trempé et revenu         550             850
  ------------------------------------------------------------------------

**7.** Parmi les aciers proposés ci-dessus, choisir l'acier et l'état de
cet acier qui pourraient convenir pour l'application étudiée.

**8.** Pour l'acier choisi, déterminer la valeur de d~mini~.

**[QUESTIONS DE COURS]{.underline}**

**Soin :** *...... **(2 points)***

1.  Citer les deux principaux objectifs d'une étude de RdM. Préciser cet
    acronyme. ***(1 point)***

2.  Donner (sans les décrire) les 5 principales hypothèses qui
    permettent de simplifier le modèle d'une étude de RdM. ***(2,5
    points)***

3.  Ecrire le torseur de cohésion. Préciser le nom de ses 6 composantes.
    ***(2 points)***

4.  Donnerl'expression du vecteur contrainte
    ![](12-RDM/Cours/pandoc/media/image71.wmf). ***(0,5 point)***

5.  Donner la condition de résistance d'une pièce soumise à de la
    traction. Préciser les différents termes utilisés. ***(1,5 point)***

6.  Citer 6 sollicitations simples. ***(1,5 point)***

7.  Donner les deux lois de Hooke. Préciser le nom des modules ainsi que
    la relation entre ces deux modules. ***(2 points)***

8.  Compléter le tableau ci-dessous. ***(2 points)***

  ----------------------------------------------------------------------------------------------------
  Lettre grec                 θ                                                      γ       
  ------------- ------------- -------- --------- ------------ ------- -------------- ------- ---------
  Nom                                  epsilon                rhô                            

  Utilisation   Coefficient                      Contrainte           Contrainte             Angle de
  en RdM        de Poisson                       normale              tangentielle           torsion
  ----------------------------------------------------------------------------------------------------

9.  Relier correctement (en faisant preuve de logique). ***(1 point)***

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](12-RDM/Cours/pandoc/media/image72.png)   ![](12-RDM/Cours/pandoc/media/image73.png)   ![](12-RDM/Cours/pandoc/media/image74.png)   ![](12-RDM/Cours/pandoc/media/image75.png)
  -------------------------------------------- -------------------------------------------- -------------------------------------------- --------------------------------------------
                                                                                                                                         

                                                                                                                                         

                                                                                                                                         

  ![](12-RDM/Cours/pandoc/media/image76.wmf)   ![](12-RDM/Cours/pandoc/media/image77.wmf)   ![](12-RDM/Cours/pandoc/media/image78.wmf)   ![](12-RDM/Cours/pandoc/media/image79.wmf)
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

10. Comment s'appelle F ? ***(0,5 point)***

11. Donner l'expression de σ pour les deux sollicitations suivantes.
    ***(2 points)***

12. Donner le nom et les unités des grandeurs suivantes. ***(1 point)***

  ---------------------------------------------------------------------------
  Symbole   I~Gz~          y'             Mf~z~            R~pe~
  --------- -------------- -------------- ---------------- ------------------
  Nom                                                      

  Unité                                                    
  ---------------------------------------------------------------------------

13. Donner l'équation différentielle de la déformée en flexion. ***(1
    point)***

14. Pour les cas suivants, donner les conditions aux limites pour
    trouver les constantes d'intégration. ***(1,5 point)***

+----------------+-----------------+-----------------+-----------------+
|                |                 |                 | Condition de    |
|                |                 |                 | continuité en   |
|                |                 |                 | un point        |
+================+=================+=================+=================+
| y(x=0) =       | y(x=a) =        | y\'(x=a) =      | y~1~(x=a) =     |
|                |                 |                 |                 |
| y'(x=0) =      |                 |                 | y'~1~(x=a) =    |
+----------------+-----------------+-----------------+-----------------+

**[EXERCICE : DEFAUTS ET AUTOCONTRAINTES]{.underline}**

L'arbre (2) est lié au carter (1) par l'intermédiaire de deux
roulements.

Le premier, en O~1~ est un roulement à double rangée de billes à
contacts obliques dont les deux bagues sont arrêtées axialement. Il est
modélisé par une liaison pivot d'axe x~1~.

Le second, en A, est un roulement à billes à contact radial dont la
bague extérieure est libre en translation. Il est modélisé par une
liaison linéaire annulaire.

Après fabrication, on constate sur le carter (1) un défaut de coaxialité
entre les alésages qui reçoivent les bagues extérieures des deux
roulements. Ce défaut est caractérisé par δ~r~ sur le schéma qui suit.
Au montage, ce défaut va engendrer des efforts au niveau des liaisons et
des autocontraintes dans l'arbre.

L'exercice consiste à chiffrer ces divers effets sur ce montage de
roulements.

![](12-RDM/Cours/pandoc/media/image80.png){width="4.483333333333333in"
height="2.183373797025372in"}

**1.** On considère que le problème de mécanique est plan. L'axe y~1~
est choisi tel que z~A'~ = 0. On note X~O~, Y~O~ ... N~O~ ... Y~A~ les
composantes du torseur des actions de liaison du bâti sur l'arbre en
O~1~ et A.

**a.** En considérant le problème plan (en « 2D »), écrire les torseurs
des inconnues de liaisons aux points O~1~ et A. ***(2 points)***

**b.** Faire le bilan des inconnues de liaisons et en déduire le rang du
système d'équations issu du PFS (ordre d'hyperstatisme interne) de cette
liaison pivot entre arbre et carter. ***(1 point)***

**c.** Aucune charge extérieure n'agit sur l'arbre. En appliquant le
PFS, déterminer les 3 relations qui relient les inconnues de liaison.
***(3 points)***

**2.** La section de l'arbre a un moment quadratique I~Gz~ et son
matériau un module d'Young E

**a.** Montrer que l'expression littérale du moment fléchissant Mf~z~ en
fonction de x et des inconnues de la liaison en O~1~ est Mf~z~ = -N~O~ +
x×Y~O~. ***(2 points)***

**b.** En utilisant les deux conditions aux limites au point O~1~,
déterminer l'expression littérale de la déformée y(x) en fonction des
caractéristiques de l'arbre et des inconnues de la liaison en O~1~.
***(3 points)***

**c.** En utilisant la condition aux limites au point A (pour lever
l'hyperstaticité établie précédemment), montrer que
$Y_{A} = \frac{3.E.I_{Gz}.\delta_{r}}{L^{3}}$. Déterminer alors
l'expression littérale des inconnues de la liaison en O~1~ en fonction
des caractéristiques de l'arbre et du défaut δ~r~. ***(2 points)***

**d.** En déduire l'expression littérale de la déformée y(x) en fonction
des caractéristiques de l'arbre et du défaut δ~r~. ***(0 point)***

**3.** L'arbre a un diamètre de 20 mm ; L = 300 mm ; E = 2.10^5^MPa et
δ~r~ = 0,05 mm.

**a.** Calculer le moment quadratique I~Gz~=
$\frac{\pi D^{4}}{64}$.***(1 point)***

**b.** Calculer les actions de liaison. ***(2 point)***

**c.** Calculer le moment fléchissant maximal Mf~zmaxi~ puis
l'autocontrainte normale maximale σ~maxi~ dans l'arbre. ***(2 points)***

**[QCM]{.underline}**

Une seule réponse / question. Noircir la bonne réponse. Pour toutes les
AN, π = 3 et g = 10 m/s²

![](12-RDM/Cours/pandoc/media/image81.png){width="3.216666666666667in"
height="1.9152777777777779in"}+1 / bonne réponse -0,5 / mauvaise réponse
0 sans réponse

1.  Comment s'appelle ce diagramme ?

  -------------------------------------------------------------------------
  Hooke     Traction     Elasticité   Contrainte-déformation      Young
  --------- ------------ ------------ --------------------------- ---------
                                                                  

  -------------------------------------------------------------------------

2.  Quelle est la zone entre A et B ?

  -------------------------------------------------------------------------
  Elastique      Rupture       Striction     Plastique     Ecrouissage
  -------------- ------------- ------------- ------------- ----------------
                                                           

  -------------------------------------------------------------------------

3.  Quelle est la bonne réponse sur la caractéristique de l'acier E30 ?

$\varepsilon = \frac{\mathcal{\mathrm{\Delta}l}}{\mathcal{l}_{0}}$ est
l\'allongement en % de la matière

A est la limite à la rupture Entre B et C, σ = E×ε

C est l\'allongement maximum σ est une contrainte de cisaillement

Au-delà de 295 N/m² les déformations sont permanentes

4.  Quelle est la valeur du module d'Young (GPa) du plexiglas ?

  --------------------------------------------------------------------------
  62            3,1             80 à 130      11 à 13         210
  ------------- --------------- ------------- --------------- --------------
                                                              

  --------------------------------------------------------------------------

5.  ![](12-RDM/Cours/pandoc/media/image82.png){width="2.2075470253718286in"
    height="2.584905949256343in"}Quelle est la coordonnée z~G~ du centre
    de la surface {S1+S2} ?

  -------------------------------------------------------------------------
  0         20        25         32,5        33,9      40        45
  --------- --------- ---------- ----------- --------- --------- ----------
                                                                 

  -------------------------------------------------------------------------

6.  Quelle est la mauvaise réponse sur le torseur de cohésion ?

![](12-RDM/Cours/pandoc/media/image83.png){width="2.452777777777778in"
height="1.7270833333333333in"} M~f~ veut dire moment fléchissant

Le repère du torseur de cohésion est toujours le même que celui du
système étudié

L\'effort tranchant sur $\overrightarrow{z}$ est noté T~Z~

L\'effort tranchant sur $\overrightarrow{y}$ est noté N

M~t~ veut dire moment de torsion

Les composantes du torseur de cohésion sont les efforts de la partie de
poutre enlevée sur la partie de poutre dont on étudie l\'équilibre

7.  Une poutre de section carrée est soumise au torseur de cohésion .
    C'est une sollicitation de ?

  ------------------------------------------------------------------------------
  Traction   Compression   Cisaillement   Torsion   Flexion pure Flexion simple
  ---------- ------------- -------------- --------- ------------ ---------------
                                                                 

  ------------------------------------------------------------------------------

8.  Quel est l'intrus ?

  ------------------------------------------------------------------------------
  Résistance   Module de   Contrainte     Moment        Pression    Limite
  mécanique    Coulomb     tangentielle   fléchissant   uniforme    pratique au
                                                                    glissement
  ------------ ----------- -------------- ------------- ----------- ------------
                                                                    

  ------------------------------------------------------------------------------

9.  Dans un torseur de cohésion, que représente N ?

  -----------------------------------------------------------------------
  Effort      Newton      Moment      Effort      Moment net  Effort
  naturel                 nominal     national                normal
  ----------- ----------- ----------- ----------- ----------- -----------
                                                              

  -----------------------------------------------------------------------

10. ![](12-RDM/Cours/pandoc/media/image84.png){width="3.301388888888889in"
    height="1.3486111111111112in"}A quelle sollicitation est soumise la
    pièce n°4 ?

  ------------------------------------------------------------------------
  Cisaillement     Traction     Compression       Flexion     Torsion
  ---------------- ------------ ----------------- ----------- ------------
                                                              

  ------------------------------------------------------------------------

11. Quel torseur correspond à la déformation n 2 ?

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$\left\{ \begin{array}{r}              $$\left\{ \begin{array}{r}              $$\left\{ \begin{array}{r}              $$\left\{ \begin{array}{r}              $$\left\{ \begin{array}{r}              $$\left\{ \begin{array}{r}
  N \\                                    0 \\                                    0 \\                                    0 \\                                    0 \\                                    0 \\
  0 \\                                    T_{y} \\                                0 \\                                    0 \\                                    T_{y} \\                                0 \\
  0                                       0                                       0                                       0                                       T_{z}                                   0
  \end{array} \middle| \begin{array}{r}   \end{array} \middle| \begin{array}{r}   \end{array} \middle| \begin{array}{r}   \end{array} \middle| \begin{array}{r}   \end{array} \middle| \begin{array}{r}   \end{array} \middle| \begin{array}{r}
  0 \\                                    0 \\                                    0 \\                                    Mt \\                                   0 \\                                    0 \\
  0 \\                                    0 \\                                    0 \\                                    0 \\                                    0 \\                                    {Mf}_{y} \\
  0                                       {Mf}_{z}                                {Mf}_{z}                                0                                       0                                       {Mf}_{z}
  \end{array} \right\}_{G,R}$$            \end{array} \right\}_{G,R}$$            \end{array} \right\}_{G,R}$$            \end{array} \right\}_{G,R}$$            \end{array} \right\}_{G,R}$$            \end{array} \right\}_{G,R}$$
  --------------------------------------- --------------------------------------- --------------------------------------- --------------------------------------- --------------------------------------- ---------------------------------------
                                                                                                                                                                                                          

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

12. En quelle unité est exprimé le moment polaire ?

  ---------------------------------------------------------------------------
  mm       N/m^2^   mm^3^    N/mm^2^   MPa       mm^4^     Pa       mm^2^
  -------- -------- -------- --------- --------- --------- -------- ---------
                                                                    

  ---------------------------------------------------------------------------

13. Combien vaut la déformation relative d'un matériau possédant module
    d'Young de 40 GPa et recevant sur une surface de 260 mm² une force
    de 52 kN ?

  -----------------------------------------------------------------------
  0,3 %             0,5 %             1,5 %             2 %
  ----------------- ----------------- ----------------- -----------------
                                                        

  -----------------------------------------------------------------------

14. Quelle est la lettre utilisée pour désigner le coefficient de Lamé ?

  ------------------------------------------------------------------------
  ν        ε         λ        θ        ρ        τ        γ        σ
  -------- --------- -------- -------- -------- -------- -------- --------
                                                                  

  ------------------------------------------------------------------------

15. Dans une section droite de poutre rectiligne soumise à de la flexion
    pure, quel est le type de torseur de cohésion ?

  -----------------------------------------------------------------------
  Quelconque        Nul               Couple            Glisseur
  ----------------- ----------------- ----------------- -----------------
                                                        

  -----------------------------------------------------------------------

16. Combien vaut la contrainte exercée sur un matériau par une force
    normale de 48 N répartie uniformément sur une section circulaire de
    rayon 12 cm ?

  -----------------------------------------------------------------------
  120 Pa            1,1 kPa           6,7 kPa           280 kPa
  ----------------- ----------------- ----------------- -----------------
                                                        

  -----------------------------------------------------------------------

17. Une poutre horizontale de longueur $\mathcal{l}$ dont on néglige le
    poids propre est encastrée à une extrémité. Elle est chargée en son
    autre extrémité d'une force concentrée verticale
    $\overrightarrow{F}$. Quelle est l'expression du moment de flexion
    maximum ?

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$\frac{F\mathcal{l}^{2}}{2}$$   $$\frac{F\mathcal{l}}{4}$$   $$\frac{F\mathcal{l}}{8}$$   $$\frac{F\mathcal{l}^{2}}{8}$$   $$\frac{F\mathcal{l}}{2}$$   $$F\mathcal{l}$$
  -------------------------------- ---------------------------- ---------------------------- -------------------------------- ---------------------------- ------------------
                                                                                                                                                           

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

18. Combien vaut la contrainte maximale exercée sur un matériau par un
    moment de flexion de 75 Nm sur une section circulaire de diamètre 10
    cm ?

  -----------------------------------------------------------------------
  160 Pa            400 kPa           0,8 MPa           12,8 MPa
  ----------------- ----------------- ----------------- -----------------
                                                        

  -----------------------------------------------------------------------

19. Comment, sur une poutre droite, modélise-t-on le poids propre ?

Par un glisseur réduit au centre de gravité de la poutre

Par la pesanteur

Par une densité linéique de force

Par des moments appliqués aux points d'appui

20. Quelle est la sollicitation composée ?

  --------------------------------------------------------------------------
  Pelage         Extension      Flambage       Flexion déviée Cisaillement
  -------------- -------------- -------------- -------------- --------------
                                                              

  --------------------------------------------------------------------------

21. Dans un essai de cisaillement, l'effort appliqué à la poutre est
    parallèle à $\overrightarrow{y}$. Quelle composante parasite des
    éléments de réduction du {T~coh~} convient-il de négliger ?

  -----------------------------------------------------------------------
  N           T~y~        T~z~        Mt          Mf~y~       Mf~z~
  ----------- ----------- ----------- ----------- ----------- -----------
                                                              

  -----------------------------------------------------------------------

22. Combien vaut la contrainte maximale exercée dans une poutre
    circulaire de rayon 12 mm par un moment de torsion de 9 Nm ?

  -----------------------------------------------------------------------
  3,5 kPa           3,5 MPa           6,9 MPa           27,8 MPa
  ----------------- ----------------- ----------------- -----------------
                                                        

  -----------------------------------------------------------------------

---
## Inventaire des images
12-RDM/Cours/pandoc/media/image1.png
12-RDM/Cours/pandoc/media/image10.emf
12-RDM/Cours/pandoc/media/image11.emf
12-RDM/Cours/pandoc/media/image12.emf
12-RDM/Cours/pandoc/media/image13.png
12-RDM/Cours/pandoc/media/image14.png
12-RDM/Cours/pandoc/media/image15.png
12-RDM/Cours/pandoc/media/image16.emf
12-RDM/Cours/pandoc/media/image17.png
12-RDM/Cours/pandoc/media/image18.png
12-RDM/Cours/pandoc/media/image19.png
12-RDM/Cours/pandoc/media/image20.png
12-RDM/Cours/pandoc/media/image21.wmf
12-RDM/Cours/pandoc/media/image22.wmf
12-RDM/Cours/pandoc/media/image23.wmf
12-RDM/Cours/pandoc/media/image24.wmf
12-RDM/Cours/pandoc/media/image25.wmf
12-RDM/Cours/pandoc/media/image26.png
12-RDM/Cours/pandoc/media/image27.wmf
12-RDM/Cours/pandoc/media/image28.wmf
12-RDM/Cours/pandoc/media/image29.wmf
12-RDM/Cours/pandoc/media/image3.jpeg
12-RDM/Cours/pandoc/media/image30.wmf
12-RDM/Cours/pandoc/media/image31.wmf
12-RDM/Cours/pandoc/media/image32.wmf
12-RDM/Cours/pandoc/media/image33.wmf
12-RDM/Cours/pandoc/media/image34.wmf
12-RDM/Cours/pandoc/media/image35.wmf
12-RDM/Cours/pandoc/media/image36.wmf
12-RDM/Cours/pandoc/media/image37.wmf
12-RDM/Cours/pandoc/media/image38.emf
12-RDM/Cours/pandoc/media/image39.emf
12-RDM/Cours/pandoc/media/image40.wmf
12-RDM/Cours/pandoc/media/image41.wmf
12-RDM/Cours/pandoc/media/image42.png
12-RDM/Cours/pandoc/media/image43.png
12-RDM/Cours/pandoc/media/image44.png
12-RDM/Cours/pandoc/media/image45.emf
12-RDM/Cours/pandoc/media/image46.png
12-RDM/Cours/pandoc/media/image47.png
12-RDM/Cours/pandoc/media/image48.wmf
12-RDM/Cours/pandoc/media/image49.wmf
12-RDM/Cours/pandoc/media/image5.png
12-RDM/Cours/pandoc/media/image50.png
12-RDM/Cours/pandoc/media/image51.wmf
12-RDM/Cours/pandoc/media/image52.wmf
12-RDM/Cours/pandoc/media/image53.png
12-RDM/Cours/pandoc/media/image54.wmf
12-RDM/Cours/pandoc/media/image55.wmf
12-RDM/Cours/pandoc/media/image56.png
12-RDM/Cours/pandoc/media/image57.wmf
12-RDM/Cours/pandoc/media/image58.wmf
12-RDM/Cours/pandoc/media/image59.png
12-RDM/Cours/pandoc/media/image6.png
12-RDM/Cours/pandoc/media/image60.png
12-RDM/Cours/pandoc/media/image61.png
12-RDM/Cours/pandoc/media/image62.png
12-RDM/Cours/pandoc/media/image63.png
12-RDM/Cours/pandoc/media/image64.wmf
12-RDM/Cours/pandoc/media/image65.png
12-RDM/Cours/pandoc/media/image66.jpeg
12-RDM/Cours/pandoc/media/image67.png
12-RDM/Cours/pandoc/media/image68.png
12-RDM/Cours/pandoc/media/image69.png
12-RDM/Cours/pandoc/media/image7.png
12-RDM/Cours/pandoc/media/image71.wmf
12-RDM/Cours/pandoc/media/image72.png
12-RDM/Cours/pandoc/media/image73.png
12-RDM/Cours/pandoc/media/image74.png
12-RDM/Cours/pandoc/media/image75.png
12-RDM/Cours/pandoc/media/image76.wmf
12-RDM/Cours/pandoc/media/image77.wmf
12-RDM/Cours/pandoc/media/image78.wmf
12-RDM/Cours/pandoc/media/image79.wmf
12-RDM/Cours/pandoc/media/image8.wmf
12-RDM/Cours/pandoc/media/image80.png
12-RDM/Cours/pandoc/media/image81.png
12-RDM/Cours/pandoc/media/image82.png
12-RDM/Cours/pandoc/media/image83.png
12-RDM/Cours/pandoc/media/image84.png
12-RDM/Cours/pandoc/media/image9.emf
