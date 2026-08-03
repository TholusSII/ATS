![](10-Électronique de Puissance/Cours/pandoc/media/image1.png){width="8.494444444444444in"
height="4.148611111111111in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image3.jpeg){width="2.379861111111111in"
height="2.1319444444444446in"}

Cycle 5 : Analyser, Modéliser, Expérimenter et Résoudre la distribution
et la conversion d\'énergie en continu

**Variation de vitesse d'une MCC**

Thomas Lusseau

Lycée Robert Doisneau - ATS

# **Table des matières** {#table-des-matières .TOC-Heading .unnumbered}

[1. Généralités sur l'électronique de puissance
[5](#généralités-sur-lélectronique-de-puissance)](#généralités-sur-lélectronique-de-puissance)

[1.1. Introduction [5](#introduction)](#introduction)

[1.2. Composants de base d'un CVS -- Bras de pont
[6](#composants-de-base-dun-cvs-bras-de-pont)](#composants-de-base-dun-cvs-bras-de-pont)

[1.3. Nature des sources [7](#nature-des-sources)](#nature-des-sources)

[1.4. Règles d'association des sources
[8](#règles-dassociation-des-sources)](#règles-dassociation-des-sources)

[1.5. Modification des sources
[9](#modification-des-sources)](#modification-des-sources)

[1.6. Forme du courant pour différents modèles de charge
[9](#forme-du-courant-pour-différents-modèles-de-charge)](#forme-du-courant-pour-différents-modèles-de-charge)

[1.7. Commutations possibles
[10](#commutations-possibles)](#commutations-possibles)

[1.8. Rapport cyclique et découpage
[10](#rapport-cyclique-et-découpage)](#rapport-cyclique-et-découpage)

[1.9. Valeur moyenne [11](#valeur-moyenne)](#valeur-moyenne)

[1.10. Valeur efficace [12](#valeur-efficace)](#valeur-efficace)

[2. Composants en électronique de puissance
[13](#composants-en-électronique-de-puissance)](#composants-en-électronique-de-puissance)

[2.1. Introduction [13](#introduction-1)](#introduction-1)

[2.2. Caractéristique statique (états bloqué /passant)
[14](#caractéristique-statique-états-bloqué-passant)](#caractéristique-statique-états-bloqué-passant)

[2.3. Caractéristique dynamique (commutation spontanée/commandée)
[14](#caractéristique-dynamique-commutation-spontanéecommandée)](#caractéristique-dynamique-commutation-spontanéecommandée)

[2.4. Association de composants
[15](#association-de-composants)](#association-de-composants)

[2.5. Pertes des composants de puissance
[15](#pertes-des-composants-de-puissance)](#pertes-des-composants-de-puissance)

[2.6. Dimensionnement des composants de puissance
[16](#dimensionnement-des-composants-de-puissance)](#dimensionnement-des-composants-de-puissance)

[3. Méthode d'étude des convertisseurs DC-DC
[17](#méthode-détude-des-convertisseurs-dc-dc)](#méthode-détude-des-convertisseurs-dc-dc)

[4. Hacheur série (ou Buck, ou abaisseur, ou dévolteur)
[17](#_Toc124946331)](#_Toc124946331)

[4.1. Schéma de principe [17](#schéma-de-principe)](#schéma-de-principe)

[4.2. Quadrants du hacheur Buck
[20](#quadrants-du-hacheur-buck)](#quadrants-du-hacheur-buck)

[5. Hacheur parallèle (ou Boost, ou survolteur, élévateur)
[21](#hacheur-parallèle-ou-boost-ou-survolteur-élévateur)](#hacheur-parallèle-ou-boost-ou-survolteur-élévateur)

[5.1. Schéma de principe
[21](#schéma-de-principe-1)](#schéma-de-principe-1)

[5.2. Quadrants du hacheur Boost
[24](#quadrants-du-hacheur-boost)](#quadrants-du-hacheur-boost)

[6. Hacheur 2 quadrants (2Q)
[24](#hacheur-2-quadrants-2q)](#hacheur-2-quadrants-2q)

[6.1. Constitution du hacheur 2 quadrants
[24](#constitution-du-hacheur-2-quadrants)](#constitution-du-hacheur-2-quadrants)

[6.2. Commande complémentaire
[25](#commande-complémentaire)](#commande-complémentaire)

[6.3. Formes d'onde [25](#formes-donde)](#formes-donde)

[6.4. Calcul de la tension de sortie et de l'ondulation de courant
[26](#calcul-de-la-tension-de-sortie-et-de-londulation-de-courant)](#calcul-de-la-tension-de-sortie-et-de-londulation-de-courant)

[7. Hacheur 4 quadrants
[27](#hacheur-4-quadrants)](#hacheur-4-quadrants)

[7.1. Constitution du hacheur 4 quadrants
[27](#constitution-du-hacheur-4-quadrants)](#constitution-du-hacheur-4-quadrants)

[7.2. Formes d'onde [28](#formes-donde-1)](#formes-donde-1)

[7.3. Calcul de la tension de sortie et de l'ondulation de courant
[28](#calcul-de-la-tension-de-sortie-et-de-londulation-de-courant-1)](#calcul-de-la-tension-de-sortie-et-de-londulation-de-courant-1)

[8. Hacheur à conversion indirecte
[29](#hacheur-à-conversion-indirecte)](#hacheur-à-conversion-indirecte)

[9. Généralités sur les convertisseurs AC-DC
[30](#généralités-sur-les-convertisseurs-ac-dc)](#généralités-sur-les-convertisseurs-ac-dc)

[9.1. Convertisseurs AC-DC
[30](#convertisseurs-ac-dc)](#convertisseurs-ac-dc)

[10. Redressement monophasé non commandé
[31](#redressement-monophasé-non-commandé)](#redressement-monophasé-non-commandé)

[10.1. Diode de puissance
[31](#diode-de-puissance)](#diode-de-puissance)

[10.2. Montage PD2 [32](#montage-pd2)](#montage-pd2)

[10.3. Puissance instantanée et active
[33](#puissance-instantanée-et-active)](#puissance-instantanée-et-active)

[10.4. Puissance réactive et puissance apparente
[34](#puissance-réactive-et-puissance-apparente)](#puissance-réactive-et-puissance-apparente)

[10.5. Facteur de puissance
[35](#facteur-de-puissance)](#facteur-de-puissance)

[10.6. Décomposition en série de Fourier
[36](#décomposition-en-série-de-fourier)](#décomposition-en-série-de-fourier)

[10.7. Puissance déformante
[37](#puissance-déformante)](#puissance-déformante)

[10.8. Transformateur monophasé parfait
[38](#transformateur-monophasé-parfait)](#transformateur-monophasé-parfait)

[11. Redresseur à absorption sinusoïdale
[38](#redresseur-à-absorption-sinusoïdale)](#redresseur-à-absorption-sinusoïdale)

[11.1. Introduction [38](#introduction-2)](#introduction-2)

[11.2. Structure à deux étages
[39](#structure-à-deux-étages)](#structure-à-deux-étages)

[11.3. Structure mono étage
[40](#structure-mono-étage)](#structure-mono-étage)

[12. Sources [40](#sources)](#sources)

[13. Exercices du chapitre [41](#_Toc124946363)](#_Toc124946363)

Donner les démarches et outils nécessaires à la correction des systèmes
asservis.

**Je connais :**

-   les différentes natures de sources (courant, tension) ainsi que leur
    règles d'associations ; ⃝

-   les caractéristiques d'un interrupteur à l'état passant (tension
    nulle) et à l'état bloqué (courant nul) ; ⃝

-   la forme du courant de la charge d'un convertisseur statique pour
    les charges : courant constant, L-E, R-L-E ; ⃝

-   la définition du rapport cyclique; ⃝

-   les définitions de valeur moyenne et efficace ; ⃝

-   les principaux composants utilisés en électronique de puissance
    (Diode, MOS, IGBT) ; ⃝

-   l'association MOS+Diode têtes bêches qui permet d'avoir un
    interrupteur réversible en courant. ⃝

-   les schémas de principe du hacheur série, 2Q et 4Q ; ⃝

-   la démarche pour tracer toutes les tensions et les courants du
    convertisseur (schémas équivalents, modèle à l'état passant des
    interrupteurs, ...) ; ⃝

-   la démarche pour déterminer la relation entre la tension d'entrée et
    la tension de sortie (en passant par les valeurs moyennes) ; ⃝

-   la démarche pour déterminer l'expression de l'ondulation de courant,
    ainsi que la valeur du rapport cyclique pour laquelle elle est
    maximale. ⃝

**Je sais :**

-   tracer l'allure du courant de la charge d'un convertisseur statique
    > pour les charges : courant constant, L-E, R-L-E ; ⃝

-   déterminer le rapport cyclique à partir d'un chronogramme; ⃝

-   calculer une valeur moyenne et/ou efficace à partir d'un
    > chronogramme ;  ⃝

-   reconnaître une diode, un transistor MOS ou IGBT sur un schéma
    > électrique. ⃝

-   tracer l'allure des tensions et courant pour n'importe quel
    > convertisseur DC-DC ; ⃝

-   déterminer la relation entre la tension de sortie et la tension
    > d'entrée pour n'importe quel convertisseur DC-DC ; ⃝

-   déterminer l'expression de l'ondulation de courant pour n'importe
    > quel convertisseur DC-DC ; ⃝

-   déterminer quel composant est passant à partir des chronogrammes de
    > tension et courant dans la charge pour n'importe quel
    > convertisseur DC-DC. ⃝

## Généralités sur l'électronique de puissance

### Introduction

L'énergie électrique se présente sous deux formes :

-   continue ou DC (piles, batteries...);

-   alternative ou AC (distribution EDF...)

![](10-Électronique de Puissance/Cours/pandoc/media/image5.jpeg){width="3.5743055555555556in"
height="2.870138888888889in"}On parle d'électronique de puissance
lorsqu'on étudie les **convertisseurs statiques d'énergie (CVS)**
permettant de modifier la présentation de l'énergie suivant nos besoins
(chargeur de batterie, interconnexion France-GB en continu, contrôle de
vitesse d'un moteur...).

On différencie donc **l'électronique des courants faibles qui traite des
informations** codées sous la forme de signaux électriques et
**l'électronique de puissance (ou courants forts) qui traite de la
transformation de l'énergie**.

Les différents variateurs (ou convertisseurs) d'électronique de
puissance sont résumés sur la figure ci-contre. Ils sont aussi utilisés
pour transformer la présentation de l'énergie électrique pour alimenter
des circuits autres que les moteurs.

##### Exemples d'utilisation de l'ENPU {#exemples-dutilisation-de-lenpu .unnumbered}

![](10-Électronique de Puissance/Cours/pandoc/media/image6.jpeg){width="1.4784722222222222in"
height="1.3604166666666666in"}L'électronique de puissance est présente
dans de nombreux systèmes et pour toutes les gammes de puissances (du mW
au MW).

**Alimentation de PC**

A partir du secteur (230 V AC), l'alimentation de PC permet de fournir
différentes tensions continues (5, 12, 3, 3 V, -12 V) pour les
différents éléments électroniques du PC.

**TGV PBKA (Paris -- Berlin -- Cologne -- Amsterdam)**

Ce TGV doit pouvoir fonctionner avec les différentes alimentations :

-   ![](10-Électronique de Puissance/Cours/pandoc/media/image7.png){width="2.026388888888889in"
    height="1.323611111111111in"}1500 Volts continu

-   3000 Volts continu

-   15000 Volts 16 2/3 Hertz alternatif monophasé

-   25000 Volts 50 Hertz alternatif monophasé

![](10-Électronique de Puissance/Cours/pandoc/media/image8.png){width="1.2319444444444445in"
height="0.8548611111111111in"}

**Exemple d'un convertisseur DC-DC**

On souhaite faire varier la tension continue pour faire varier la
vitesse d'une MCC. Une solution simple qui pourrait être envisagée est
d'utiliser un potentiomètre ou un réseau résistif.

$U_{s} = \frac{R_{2}.R_{c}}{R_{1}.\left( R_{2} + R_{c} \right) + R_{2}R_{c}}.U_{e}$ ;
$\eta = \frac{P_{s}}{P_{e}} = \frac{U^{2}\left( R_{c}.R_{2} + R_{1}\left( R_{2} + R_{c} \right) \right)}{\left( R_{2} + R_{c} \right).R_{c}.E^{2}}$

Ce montage comporte plusieurs problèmes

-   La **tension de sortie dépend de la charge** (R~c~) ;

-   Le **rendement est très faible** (\<20%) car une grande partie est
    dissipée par effet Joule.

Pour obtenir un rendement élevé, les convertisseurs statiques utilisent
des **interrupteurs électroniques** à la place des résistances.

Ceci a pour conséquences :

-   **La disparition des pertes par effet Joule ;**

-   **L'ajout de circuits électroniques de commande pour les
    interrupteurs ;**

Un CVS doit permettre de convertir la présentation de l'énergie
électrique avec un **rendement maximal**.

### Composants de base d'un CVS -- Bras de pont

Un CVS doit permettre de convertir la présentation de l'énergie
électrique avec un **rendement maximal**. Le montage précédent est donc
à éviter et les convertisseurs statiques (CVS) utilisent des
interrupteurs électroniques. Les éléments autorisés sont donc uniquement
ceux dissipant pas (ou peu) de puissance.

Les interrupteurs électroniques sont donc utilisés pour dissiper le
minimum de puissance (nulle s'ils sont idéaux). Il n'y a que deux états
possibles pour un interrupteur (ouvert ou fermé)

Si on remplace maintenant les résistances par des interrupteurs idéaux
il n'y aura pas de pertes lors du transfert.

Avec deux interrupteurs il y a alors 4 possibilités illustrées
ci-dessous.

![](10-Électronique de Puissance/Cours/pandoc/media/image9.png){width="4.583333333333333in"
height="1.8284722222222223in"}

### Nature des sources

Un CVS permet le transfert d'énergie entre la source et la charge. Ce
transfert peut être direct ou inverse.

Les sources/charge peuvent être modélisées par deux types de sources :

-   **Les sources de tension ;**

-   **Les sources de courant.**

+-----------------------------------+-----------------------------------+
| **Source de tension**             | **Source de courant**             |
+===================================+===================================+
| Une source de tension permet      | Une source de courant permet      |
| d'imposer la tension quel que     | d'imposer le courant quelle que   |
| soit le courant demandé.          | soit la tension.                  |
|                                   |                                   |
| **[Ex]{.underline}** : batterie,  | **[Ex]{.underline}** : panneaux   |
| réseau EDF, ...                   | solaires, MCC, ...                |
+-----------------------------------+-----------------------------------+

### Règles d'association des sources

Nous avons vu dans le cas précédent que tous les cas de commutations des
interrupteurs du bras de pont n'étaient pas possibles. Il y a alors des
règles à respecter lorsqu'un convertisseur est utilisé.

1.  Les sources de tension ne doivent jamais être court-circuitée (mais
    peuvent être ouvertes) (1)

```{=html}
<!-- -->
```
2.  Le circuit des sources de courant ne doit jamais être ouvert (mais
    peuvent être en court-circuit). (2)

```{=html}
<!-- -->
```
3.  Les sources de même nature ne peuvent pas être connectées entre
    elles (deux sources de tension ou deux sources de courant
    connectées). On ne peut connecter entre elles que des sources de
    nature différentes. (3a et 3b)

```{=html}
<!-- -->
```
4.  Uniquement les sources de natures différentes peuvent être
    connectées directement.

### Modification des sources

Une source de tension associée à un CVS peut être « vue » comme une
source de courant par ajout d'une inductance.

$${u_{L}(t) = L\frac{di(t)}{dt} = U_{e} - u(t),\ Soit\ \ \frac{di(t)}{dt} = \frac{U_{e} - u(t)}{L}
}{Si\ \ L\ grand\ alors\ \frac{di(t)}{dt} \rightarrow 0\ soit\boxed{\ i(t) = cte}}$$

![](10-Électronique de Puissance/Cours/pandoc/media/image10.jpeg){width="2.8381944444444445in"
height="0.9284722222222223in"}

De même, une source de courant peut être « vue » comme une source de
tension par ajout d'un condensateur.

$${i_{C} = C\frac{du(t)}{dt} = I_{0} - i(t),\ \ Soit\ \ \frac{du(t)}{dt} = \frac{I_{0} - i(t)}{C}
}{Si\ \ C\ est\ grand\ alors\ \frac{du(t)}{dt} \rightarrow 0\ soit\boxed{\ u(t) = cte}}$$

### Forme du courant pour différents modèles de charge

Suivant si la source de courant est de type courant constant ou homogène
à une source du courant, il existera une ondulation de courant.

![](10-Électronique de Puissance/Cours/pandoc/media/image11.jpeg){width="3.436111111111111in"
height="1.2083333333333333in"}

-   **Source de courant idéale :**

Dans le cas d'une source de courant idéale, le courant absorbé par la
charge est constant quelle que soit la tension à ses bornes.

![](10-Électronique de Puissance/Cours/pandoc/media/image12.jpeg){width="3.4365080927384075in"
height="1.5185793963254592in"}

-   **Charge L-E :**

Dans le cas d'une charge L-E, il existe une ondulation de courant qui
dépend de la période de découpage T~d~, de $\alpha$, et de la valeur de
l'inductance L.

-   ![](10-Électronique de Puissance/Cours/pandoc/media/image13.jpeg){width="3.433333333333333in"
    height="1.5784831583552057in"}**Charge R-L-E :**

Dans le cas d'une charge RLE, il existe aussi une ondulation de courant
mais l'évolution du courant n'est plus linéaire mais exponentielle.
Cependant si L/R \>\> T~d~ on peut considérer l'évolution comme
linéaire.

### Commutations possibles

![](10-Électronique de Puissance/Cours/pandoc/media/image14.jpeg){width="3.3808737970253717in"
height="2.1083333333333334in"}Nous avons vu dans le paragraphe « Règle
d'association des sources » que tous les cas de commutation pour un bras
de pont n'étaient pas possibles. Au final, les commutations possibles
pour un CVS sont les suivantes.

Pour respecter les règles précédentes il faut dans le cas précédent que
les interrupteurs soient **commandés de manière complémentaire :**
$\mathbf{K}_{\mathbf{1}}\mathbf{=}\overline{\mathbf{K}_{\mathbf{2}}}$

(Quand K2 est fermé K1 doit être ouvert et inversement)

### ![](10-Électronique de Puissance/Cours/pandoc/media/image15.jpeg){width="3.5125in" height="1.6430555555555555in"}Rapport cyclique et découpage

La commutation des différents interrupteurs se fait de manière
périodique (ou répétitive). On parle de **période de découpage** (en
général notée T~d~).

La **fréquence de découpage** associée est en général notée f~d~.

![](10-Électronique de Puissance/Cours/pandoc/media/image16.jpeg){width="2.825in"
height="1.1118055555555555in"}Si, sur une période de découpage la durée
de conduction de K1 est la même que celle de K2, on obtient l'allure
suivante pour la tension u(t).

Le **rapport cyclique** est défini comme le rapport entre la durée à
l'état haut t~on~ et la période de découpage T~d~ :
$\alpha = \frac{t_{on}}{T_{d}}$

La valeur moyenne de la tension u(t) sur une période de découpage est
alors :

$< u(t) > = u = \frac{1}{T_{d}}\left\lbrack E.\alpha.T_{d} \right\rbrack = \boxed{\alpha.E}$

Pour faire varier la valeur moyenne de la tension, il suffit alors de
faire varier le **rapport cyclique**.

Ce n'est plus la **valeur instantanée qui est réglée mais la valeur
moyenne**. Si la fréquence de découpage est assez grande, la charge (par
exemple une MCC) ne « verra » que la valeur moyenne.

### Valeur moyenne

![](10-Électronique de Puissance/Cours/pandoc/media/image17.jpeg){width="2.825in"
height="1.7125in"}Un signal électrique est **périodique** s'il se répète
de manière identique à chaque période, notée **T et exprimée en
seconde(s).**

La **Fréquence** correspond au nombre de périodes par seconde. Elle
s'exprime en **Hertz (Hz)**et se calcule directement depuis la Période

$$\boxed{f = \frac{1}{T}}\ en\ Hz$$

**Définition Valeur moyenne :**

La valeur moyenne d'un signal (tension ou courant) périodique est
définie par la relation suivante :

$$\boxed{< s > = \bar{s} = \frac{1}{T}\int_{0}^{T}{s(t).dt}\ }\ $$

+-------+--------------------------------------------------------------+
| > ![] | **Calculs de valeurs moyennes**                              |
| (10-É |                                                              |
| lectr | **Déterminer les valeurs moyennes des signaux suivants**     |
| oniqu |                                                              |
| e de  | ![](10-Électronique de Puissance/                            |
| Puiss | Cours/pandoc/media/image19.jpeg){width="3.970272309711286in" |
| ance/ | height="1.8333333333333333in"}                               |
| Cours |                                                              |
| /pand | ![](10-Électronique de Puissance/                            |
| oc/me | Cours/pandoc/media/image19.jpeg){width="4.031441382327209in" |
| dia/i | height="2.9166666666666665in"}                               |
| mage1 |                                                              |
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

### Valeur efficace

**Définition Valeur efficace :**

La valeur efficace d'un signal (tension ou courant) périodique est
définie comme la racine de la valeur moyenne du carré du signal (RMS) :

$$\boxed{S = S_{eff} = \sqrt{< s^{2} >} = \sqrt{\frac{1}{T}\int_{0}^{T}{s^{2}(t).dt}}\ }\ $$

![](10-Électronique de Puissance/Cours/pandoc/media/image20.png){width="9.689413823272091e-4in"
height="8.956692913385827e-4in"}**Une valeur efficace est forcément
positive.**

+-------+--------------------------------------------------------------+
| > ![] | **Calculs de valeurs efficaces**                             |
| (10-É |                                                              |
| lectr | **Déterminer les valeurs efficaces des signaux suivants**    |
| oniqu |                                                              |
| e de  | ![](10-Électronique de Puissance/                            |
| Puiss | Cours/pandoc/media/image21.jpeg){width="5.575396981627296in" |
| ance/ | height="1.348969816272966in"}                                |
| Cours |                                                              |
| /pand | $$U = U_{eff} = \sqrt{< u^{2} >} = \sqrt{\frac{1}{           |
| oc/me | T}\left\lbrack {U_{M}}^{2}T \right\rbrack} = \boxed{U_{M}}$$ |
| dia/i |                                                              |
| mage1 | ![](10-Électronique de Puissance/                            |
| 8.png | Cours/pandoc/media/image19.jpeg){width="3.970138888888889in" |
| ){wid | height="1.2261898512685914in"}                               |
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

## Composants en électronique de puissance

### Introduction

Les composants utilisés en électronique de puissance sont utilisés comme
des **interrupteurs** qui peuvent être **commandables** ou non. On
introduit alors la notion de **commutation** (passage de l'état ouvert à
l'état fermé) et on définit les **caractéristiques statiques**
(intrinsèque du composant) et **dynamiques** (passage d'un état à
l'autre - dépend du circuit associé).

On utilisera aussi la notion de **réversibilité en courant** (aptitude à
laisser passer des courants directs et inverses à l'état passant) ou
**réversibilité en tension** (aptitude à supporter des tensions directes
et inverses à l'état bloqué).

![](10-Électronique de Puissance/Cours/pandoc/media/image22.jpeg){width="2.9229166666666666in"
height="1.6131944444444444in"}On dira alors si le composant (ou le
convertisseur statique) est **réversible** ou **bidirectionnel** en
courant ou tension. Dans le cas contraire on dira qu'il
est**unidirectionnel.**

Quel que soit le composant électronique utilisé, son **fonctionnement
idéalisé sera celui d'un interrupteur** qui peut être unidirectionnel ou
bidirectionnel en tension et courant suivant les **associations**.Ce qui
change entre les différents composants est sa **commutation (spontanée,
ou commandée)** et son **circuit de commande (en tension, en courant,
...).**

Les composants commandés ont trois pattes car ils disposent d'une
**patte ou électrodede commande**.

![](10-Électronique de Puissance/Cours/pandoc/media/image23.jpeg){width="3.7180555555555554in"
height="1.0395833333333333in"}![](10-Électronique de Puissance/Cours/pandoc/media/image24.jpeg){width="3.420138888888889in"
height="2.020138888888889in"}

### Caractéristique statique (états bloqué /passant)

![](10-Électronique de Puissance/Cours/pandoc/media/image25.jpeg){width="3.283333333333333in"
height="2.683333333333333in"}Dans la **caractéristique statique**, on va
voir apparaître deux régimes (ou états) statiques différents : **l'état
bloqué** et **l'état passant**. On la représente dans le plan u-i. Les
interrupteurs ne fournissant pas d'énergie, leur caractéristique
statique se trouve dans les **quadrants 1 et 3** en convention
récepteur.

Pour **l'état bloqué**, on aura une résistance très grande (i proche de
0).

Pour **l'état passant** une résistance très faible (u proche 0).

La **caractéristique statique** est une **caractéristique intrinsèque du
composant** (ne dépend pas du montage associé).

![](10-Électronique de Puissance/Cours/pandoc/media/image26.jpeg){width="3.1305555555555555in"
height="1.5152777777777777in"}La **caractéristique dynamique** est
confondue avec la caractéristique statique et correspond au passage
entre les deux états (passant et bloqué). On parle alors de
**commutation**.

Cette dernière **dépend alors des contraintes imposées par le circuit
extérieur** associé au composant.

On distingue deux types de commutation :

-   la **commutation naturelle** (ou spontanée) ;

-   la **commutation commandée.**

### Caractéristique dynamique (commutation spontanée/commandée)

![](10-Électronique de Puissance/Cours/pandoc/media/image27.jpeg){width="1.9847222222222223in"
height="0.9604166666666667in"}**Commutation naturelle (ou spontanée)**

Dans le cas de la **commutation spontanée**, le passage d'un état à
l'autre ne **dépend que de l'évolution des grandeurs du circuit
associé**. Cette commutation s'effectue avec un **changement de
quadrant** et la caractéristique passe par zéro (on reste toujours en
fonctionnement récepteur).

**Commutation commandée :**

![](10-Électronique de Puissance/Cours/pandoc/media/image28.jpeg){width="2.061111111111111in"
height="1.0215277777777778in"}La **commutation commandée** s'effectue
**sans changer de quadrant**. Pour changer d'état, il faut donc
**changer la résistance interne du semi-conducteur au moyen
d'électrodes** de commande.

Dans le cas de la **commutation commandée, l'interrupteur va agir sur le
circuit extérieur** et donc subir les contraintes extérieures. Dans ce
cas-là, plus la fréquence de commutation sera élevée plus les pertes de
commutations seront élevées.

### Association de composants

Quasiment tous les interrupteurs utilisés en électronique de puissance
sont **unidirectionnels**. Pour obtenir des interrupteurs
**bidirectionnels** en tension ou en courant, il faut faire des
**associations de composants.**

L'association la plus utilisée est celle d'un transistor et d'une diode
têtes bêches.

![](10-Électronique de Puissance/Cours/pandoc/media/image29.jpeg){width="2.4319444444444445in"
height="1.5in"}![](10-Électronique de Puissance/Cours/pandoc/media/image30.jpeg){width="2.3756944444444446in"
height="1.1458333333333333in"}![](10-Électronique de Puissance/Cours/pandoc/media/image31.jpeg){width="2.4479166666666665in"
height="1.1381944444444445in"}

### Pertes des composants de puissance

Jusqu'à présent les composants électroniques étaient supposés idéaux. En
réalité, il existe différentes pertes qui vont jouer sur le rendement.

On distingue les pertes suivantes :

-   **pertes en conductions**(à l'état passant, indépendant de la
    > fréquence de commutation). On néglige les pertes à l'état bloqué.

-   **pertes de commutations** (passage d'un état à l'autre, dépendant
    > de la fréquence de commutation).

Les pertes en conductions peuvent se déterminer à partir du modèle
équivalent à l'état passant.

![](10-Électronique de Puissance/Cours/pandoc/media/image32.jpeg){width="6.520956911636046in"
height="2.109722222222222in"}

Les pertes en conduction de la diode sont alors donnée par la puissance
dissipée à l'état passant, soit :
$P_{cond} = V_{o} < i_{D} > + r_{D}{I_{D}}^{2}$

### ![](10-Électronique de Puissance/Cours/pandoc/media/image33.jpeg){width="1.1in" height="1.1236111111111111in"}Dimensionnement des composants de puissance

Les **pertes des composants se transforment en chaleur** qu'il est
nécessaire d'évacuer afin d'éviter la **destruction du composant**
(possible pour une température de jonction de 150ºC). On associera donc
aux composants de puissances des **dispositifs de refroidissement**
(radiateurs, ...).

Les composants de puissance utilisés sont dimensionnés pour certaines
valeurs de tension et de courant.

Au-delà de ces valeurs « admissibles » le composant sera détruit ou sa
durée de vie sera grandement diminuée.

Ces valeurs sont indiquées dans les documentations constructeurs
(datasheet) dans une application, il faut trouver les valeurs des
tensions et courants moyens et efficaces aux bornes du composant
considéré.

![diode_Page_1](10-Électronique de Puissance/Cours/pandoc/media/image34.jpeg){width="4.370814741907261in"
height="6.1819444444444445in"}

## Méthode d'étude des convertisseurs DC-DC

Une méthode d'étude pour étudier les convertisseurs DC-DC est la
suivante :

1.  Identifier les sources (tension/courant et l'approximation utilisée
    pour la source de courant (I constant, L-E, R-L-E) et tracer
    l'allure du courant.

2.  Regarder la commande des interrupteurs.

3.  Dessiner des schémas équivalents pour les phases de fonctionnement.

4.  Ecrire la loi des mailles et la loi des nœuds avec les interrupteurs

5.  Tracer les chronogrammes sur une période en utilisant les schémas
    équivalents

6.  Bien vérifier que le produit courant tension pour un interrupteur
    parfait est nul (passant u=0, i≠0 et bloqué i=0, u≠0)

7.  Déterminer les grandeurs demandées (valeur moyenne, valeur
    efficace,...), bien penser à la maille de l'inductance pour
    l'ondulation de courant.

![](10-Électronique de Puissance/Cours/pandoc/media/image9.png){width="4.583333333333333in"
height="1.8284722222222223in"}

## Hacheur série (ou Buck, ou abaisseur, ou dévolteur)

### Schéma de principe

Un **hacheur série** est un convertisseur DC-DC permettant d'obtenir une
tension de sortie continue et **inférieure ou égale** **à la tension
d'entrée**. Le schéma de principe est le suivant.

Il y a alors 3 phases de fonctionnement possibles suivant l'état de
l'interrupteur K et du courant dans la charge.

-   K est fermé donc u~D~ = U~e~

-   K est ouvert et i~L~ ≠ 0, donc u~D~ = 0

-   K est ouvert et i~L~ = 0, donc u~D~ = U~s~

> L'interrupteur K est commandé périodiquement de 0 à $\alpha$T.
>
> Ce signal de commande (ou de découpage) est appelé **MLI (Modulation
> de Largeur d'impulsion** ou **PWM (Pulse Width Modulation).**

+-------+------------------------------+------------------------------+
| > ![] | **Etude du hacheur série**   |                              |
| (10-É |                              |                              |
| lectr | 1.                           |                              |
| oniqu |   ![](10-Électronique de Pui |                              |
| e de  | ssance/Cours/pandoc/media/im |                              |
| Puiss | age35.jpeg){width="2.4125in" |                              |
| ance/ |                              |                              |
| Cours | height="1.6375in"}Identifier |                              |
| /pand |     les sources              |                              |
| oc/me |     (tension/courant et      |                              |
| dia/i |     l'approximation utilisée |                              |
| mage1 |     pour la source de        |                              |
| 8.png |     courant (I constant,     |                              |
| ){wid |     L-E, R-L-E) et tracer    |                              |
| th="0 |     l'allure du courant.     |                              |
| .6262 |                              |                              |
| 69685 | > **Source de courant de     |                              |
| 03937 | > type L-E**                 |                              |
| 01in" |                              |                              |
| >     | 2.  Regarder la commande des |                              |
| heigh |     interrupteurs.           |                              |
| t="0. |                              |                              |
| 65083 | **K passant de 0 à**         |                              |
| 33333 | $\mathbf{\alpha T}$ **(donc  |                              |
| 33333 | D bloquée -- commande        |                              |
| 4in"} | complémentaire)**            |                              |
|       |                              |                              |
|       | **D passante de**            |                              |
|       | $\mathbf{\alpha T}$ **à**    |                              |
|       | $\mathbf{T}$ **(donc K       |                              |
|       | bloqué -- commande           |                              |
|       | complémentaire)**            |                              |
|       |                              |                              |
|       | 3.  Dessiner des schémas     |                              |
|       |     équivalents pour les     |                              |
|       |     phases de                |                              |
|       |     fonctionnement.          |                              |
+=======+==============================+==============================+
|       | **0 \< t \<**                | $\mathbf{\alpha}$**T \< t \< |
|       | $\mathbf{\alpha}$**T**       | T**                          |
|       |                              |                              |
|       | Dans le cas où K est         | ![](10-Électronique de Pui   |
|       | passant, la diode D est      | ssance/Cours/pandoc/media/im |
|       | bloquée puisqu'elle est      | age37.png){width="3.15625in" |
|       | polarisée en inverse (v~D~=  | height                       |
|       | -E). Le schéma équivalent    | ="1.1208333333333333in"}Dans |
|       | est alors le suivant :       | le cas où K est bloqué, la   |
|       |                              | diode D est naturellement    |
|       | ![](10-Électronique de P     | passante (diode roue libre   |
|       | uissance/Cours/pandoc/media/ | assurant la continuité du    |
|       | image36.png){width="3.125in" | courant dans l'inductance).  |
|       | he                           | Le schéma équivalent est le  |
|       | ight="1.2333333333333334in"} | suivant :                    |
+-------+------------------------------+------------------------------+
|       | 4.  Ecrire la loi des        |                              |
|       |     mailles et la loi des    |                              |
|       |     nœuds avec les           |                              |
|       |     interrupteurs            |                              |
|       |                              |                              |
|       | $$\mathbf                    |                              |
|       | {U}_{\mathbf{e}}\mathbf{=}\m |                              |
|       | athbf{u}_{\mathbf{K}}\mathbf |                              |
|       | {+}\mathbf{u}_{\mathbf{D}}$$ |                              |
|       |                              |                              |
|       | $$\mathbf                    |                              |
|       | {i}_{\mathbf{L}}\mathbf{=}\m |                              |
|       | athbf{i}_{\mathbf{K}}\mathbf |                              |
|       | {+}\mathbf{i}_{\mathbf{D}}$$ |                              |
+-------+------------------------------+------------------------------+
|       | 5.  Tracer les chronogrammes |                              |
|       |     sur une période en       |                              |
|       |     utilisant les schémas    |                              |
|       |     équivalents              |                              |
|       |                              |                              |
|       | ![](10-É                     |                              |
|       | lectronique de Puissance/Cou |                              |
|       | rs/pandoc/media/image39.png) |                              |
|       | {width="2.585604768153981in" |                              |
|       | h                            |                              |
|       | eight="4.166666666666667in"} |                              |
|       |                              |                              |
|       | 6.  Bien vérifier que le     |                              |
|       |     produit courant tension  |                              |
|       |     pour un interrupteur     |                              |
|       |     parfait est nul (passant |                              |
|       |     u=0, i≠0 et bloqué i=0,  |                              |
|       |     u≠0)                     |                              |
|       |                              |                              |
|       | 7.  Déterminer les grandeurs |                              |
|       |     demandées (valeur        |                              |
|       |     moyenne, valeur          |                              |
|       |     efficace,...), bien      |                              |
|       |     penser à la maille de    |                              |
|       |     l'inductance pour        |                              |
|       |     l'ondulation de courant  |                              |
|       |                              |                              |
|       | **En régime permanent, il    |                              |
|       | est possible de déterminer   |                              |
|       | la tension de sortie**       |                              |
|       | $\mathbf{U}_{\mathbf{s}}$    |                              |
|       | **en utilisant l'égalité sur |                              |
|       | les valeurs moyennes.**      |                              |
|       |                              |                              |
|       | $$                           |                              |
|       | \mathbf{<}\mathbf{U}_{\mathb |                              |
|       | f{s}}\mathbf{> =}\mathbf{U}_ |                              |
|       | {\mathbf{s}}\mathbf{= <}\mat |                              |
|       | hbf{u}_{\mathbf{D}}\mathbf{> |                              |
|       | }\mathbf{-}\mathbf{<}\mathbf |                              |
|       | {u}_{\mathbf{L}}\mathbf{>}$$ |                              |
|       |                              |                              |
|       | **Nous pouvons trouver**     |                              |
|       | $\mathbf{<}\mathb            |                              |
|       | f{u}_{\mathbf{D}}\mathbf{>}$ |                              |
|       | **avec les chronogrammes     |                              |
|       | précédents mais nous n'avons |                              |
|       | aucune information sur**     |                              |
|       | $\mathbf{u}_{\               |                              |
|       | mathbf{L}}\mathbf{(t)}$**.** |                              |
|       |                              |                              |
|       | $$\m                         |                              |
|       | athbf{<}\mathbf{u}_{\mathbf{ |                              |
|       | D}}\mathbf{> =}\frac{\mathbf |                              |
|       | {1}}{\mathbf{T}}\int_{\mathb |                              |
|       | f{0}}^{\mathbf{T}}{\mathbf{u |                              |
|       | }_{\mathbf{D}}\mathbf{(t)}}\ |                              |
|       | mathbf{dt =}\frac{\mathbf{1} |                              |
|       | }{\mathbf{T}}\left\lbrack \m |                              |
|       | athbf{U}_{\mathbf{e}}\mathbf |                              |
|       | {.\alpha T} \right\rbrack\ma |                              |
|       | thbf{=}\boxed{\mathbf{\alpha |                              |
|       | .}\mathbf{U}_{\mathbf{e}}}$$ |                              |
|       |                              |                              |
|       | $$\mathbf{U}_{\mathbf{s}}\ma |                              |
|       | thbf{=}\boxed{\mathbf{\alpha |                              |
|       | .}\mathbf{U}_{\mathbf{e}}}$$ |                              |
|       |                              |                              |
|       | $$\mathbf{<}\m               |                              |
|       | athbf{u}_{\mathbf{L}}\mathbf |                              |
|       | {> \  =}\frac{\mathbf{1}}{\m |                              |
|       | athbf{T}}\int_{\mathbf{0}}^{ |                              |
|       | \mathbf{T}}{\mathbf{u}_{\mat |                              |
|       | hbf{L}}\left( \mathbf{t} \ri |                              |
|       | ght)}\mathbf{dt =}\frac{\mat |                              |
|       | hbf{1}}{\mathbf{T}}\int_{\ma |                              |
|       | thbf{0}}^{\mathbf{T}}{\mathb |                              |
|       | f{L}\frac{\mathbf{d}\mathbf{ |                              |
|       | i}_{\mathbf{L}}\left( \mathb |                              |
|       | f{t} \right)}{\mathbf{dt}}}\ |                              |
|       | mathbf{dt =}\frac{\mathbf{L} |                              |
|       | }{\mathbf{T}}\left\lbrack \m |                              |
|       | athbf{i}_{\mathbf{L}}\left(  |                              |
|       | \mathbf{t} \right) \right\rb |                              |
|       | rack_{\mathbf{t = 0}}^{\math |                              |
|       | bf{t = T}}\mathbf{=}\frac{\m |                              |
|       | athbf{L}}{\mathbf{T}}\left\l |                              |
|       | brack \mathbf{i}_{\mathbf{L} |                              |
|       | }\left( \mathbf{T} \right)\m |                              |
|       | athbf{-}\mathbf{i}_{\mathbf{ |                              |
|       | L}}\left( \mathbf{0} \right) |                              |
|       |  \right\rbrack\mathbf{= 0}$$ |                              |
|       |                              |                              |
|       | ![](10-Électronique de Pu    |                              |
|       | issance/Cours/pandoc/media/i |                              |
|       | mage40.jpeg){width="2.575in" |                              |
|       | he                           |                              |
|       | ight="1.4541666666666666in"} |                              |
|       |                              |                              |
|       | ###                          |                              |
|       | ## Calcul de l'ondulation de |                              |
|       |  courant {#calcul-de-londula |                              |
|       | tion-de-courant .unnumbered} |                              |
|       |                              |                              |
|       | **L'ondulation de courant    |                              |
|       | notée**                      |                              |
|       | $\mathbf{\De                 |                              |
|       | lta}\mathbf{i}_{\mathbf{L}}$ |                              |
|       | **correspond à la différence |                              |
|       | entre la valeur minimale et  |                              |
|       | maximale du courant          |                              |
|       | traversant l'inductance sur  |                              |
|       | une période. Si cette        |                              |
|       | ondulation est trop          |                              |
|       | importante il y a plus de    |                              |
|       | risque d'avoir un régime     |                              |
|       | discontinu. Pour diminuer    |                              |
|       | cette ondulation il faudra   |                              |
|       | augmenter l'inductance L.**  |                              |
|       |                              |                              |
|       | $$                           |                              |
|       | \mathbf{\Delta}\mathbf{i}_{\ |                              |
|       | mathbf{L}}\mathbf{=}\mathbf{ |                              |
|       | i}_{\mathbf{Lmax}}\mathbf{-} |                              |
|       | \mathbf{i}_{\mathbf{Lmin}}$$ |                              |
|       |                              |                              |
|       | **Pour**$\mathbf{\ 0         |                              |
|       | \  < \ t\  < \alpha T}$**,** |                              |
|       | **il y a transfert direct    |                              |
|       | d'énergie entre la source et |                              |
|       | la charge. On a alors le     |                              |
|       | courant traversant           |                              |
|       | l'inductance L qui vaut :**  |                              |
|       |                              |                              |
|       | $$\mathbf{u}_{\mat           |                              |
|       | hbf{L}}\mathbf{(t) = L}\frac |                              |
|       | {\mathbf{d}\mathbf{i}_{\math |                              |
|       | bf{L}}}{\mathbf{dt}}\mathbf{ |                              |
|       | =}\mathbf{U}_{\mathbf{e}}\ma |                              |
|       | thbf{-}\mathbf{U}_{\mathbf{s |                              |
|       | }}\mathbf{\ }\mathbf{\Righta |                              |
|       | rrow}\frac{\mathbf{d}\mathbf |                              |
|       | {i}_{\mathbf{L}}\mathbf{(t)} |                              |
|       | }{\mathbf{dt}}\mathbf{=}\fra |                              |
|       | c{\mathbf{U}_{\mathbf{e}}\ma |                              |
|       | thbf{-}\mathbf{U}_{\mathbf{s |                              |
|       | }}\mathbf{\ }}{\mathbf{L}}$$ |                              |
|       |                              |                              |
|       | **On a donc le courant qui   |                              |
|       | va croître                   |                              |
|       | (**$\                        |                              |
|       | mathbf{U}_{\mathbf{e}}\mathb |                              |
|       | f{>}\mathbf{U}_{\mathbf{s}}$ |                              |
|       | **) à partir d'une valeur    |                              |
|       | minimale i~Lmin~ , on a :**  |                              |
|       |                              |                              |
|       | $$\boxed{\mathbf{i}_{        |                              |
|       | \mathbf{L}}\mathbf{(t) =}\fr |                              |
|       | ac{\mathbf{U}_{\mathbf{e}}\m |                              |
|       | athbf{-}\mathbf{U}_{\mathbf{ |                              |
|       | s}}\mathbf{\ }}{\mathbf{L}}\ |                              |
|       | mathbf{t\  + \ }\mathbf{i}_{ |                              |
|       | \mathbf{Lmin}}}\mathbf{\ pou |                              |
|       | r\ 0\  < \ t\  < \alpha T}$$ |                              |
|       |                              |                              |
|       | $$\                          |                              |
|       | mathbf{\Delta}\mathbf{i}_{\m |                              |
|       | athbf{L}}\mathbf{=}\mathbf{i |                              |
|       | }_{\mathbf{Lmax}}\mathbf{-}\ |                              |
|       | mathbf{i}_{\mathbf{Lmin}}\ma |                              |
|       | thbf{=}\mathbf{i}_{\mathbf{L |                              |
|       | }}\left( \mathbf{\alpha T} \ |                              |
|       | right)\mathbf{-}\mathbf{i}_{ |                              |
|       | \mathbf{Lmin}}\mathbf{=}\fra |                              |
|       | c{\mathbf{U}_{\mathbf{e}}\ma |                              |
|       | thbf{-}\mathbf{U}_{\mathbf{s |                              |
|       | }}\mathbf{\ }}{\mathbf{L}}\m |                              |
|       | athbf{\alpha T + \ }\mathbf{ |                              |
|       | i}_{\mathbf{Lmin}}\mathbf{-} |                              |
|       | \mathbf{i}_{\mathbf{Lmin}}$$ |                              |
|       |                              |                              |
|       | $$\boxed{\mathbf{\D          |                              |
|       | elta}\mathbf{i}_{\mathbf{L}} |                              |
|       | \mathbf{=}\frac{\mathbf{U}_{ |                              |
|       | \mathbf{e}}\mathbf{-}\mathbf |                              |
|       | {\alpha}\mathbf{U}_{\mathbf{ |                              |
|       | e}}\mathbf{\ }}{\mathbf{L}}\ |                              |
|       | mathbf{\alpha T =}\frac{\mat |                              |
|       | hbf{U}_{\mathbf{e}}\mathbf{\ |                              |
|       |  }}{\mathbf{LF}}\mathbf{\alp |                              |
|       | ha}\left( \mathbf{1}\mathbf{ |                              |
|       | -}\mathbf{\alpha} \right)}$$ |                              |
+-------+------------------------------+------------------------------+

### Quadrants du hacheur Buck

![](10-Électronique de Puissance/Cours/pandoc/media/image41.jpeg){width="2.7527777777777778in"
height="1.7180555555555554in"}Un **hacheur série** est un convertisseur
DC-DC permettant d'obtenir une tension de sortie continue et
**inférieure ou égale** **à la tension d'entrée**. Le schéma de principe
est le suivant.

**La tension de sortie est variable mais toujours positive. Le hacheur
série** est un convertisseur **non réversible en tension**.

Les différents composants étant unidirectionnels en courant, cette
structure est **non** **réversible en courant**. La structure peut se
mettre sous la forme d'un « bras de pont » où l'interrupteur K est un
interrupteur commandé et D est une diode (commutation naturelle).

![](10-Électronique de Puissance/Cours/pandoc/media/image42.jpeg){width="2.3670636482939633in"
height="1.1505030621172354in"}![](10-Électronique de Puissance/Cours/pandoc/media/image43.jpeg){width="2.691998031496063in"
height="1.4827876202974628in"}

## ![](10-Électronique de Puissance/Cours/pandoc/media/image44.jpeg){width="3.1131944444444444in" height="2.7368055555555557in"}Hacheur parallèle (ou Boost, ou survolteur, élévateur)

### Schéma de principe

Un **hacheur parallèle** est un convertisseur DC-DC permettant d'obtenir
une tension de sortie continue et **supérieure** **à la tension
d'entrée**. Le schéma de principe est le suivant.

+-------+------------------------------+------------------------------+
| > ![] | **Etude du hacheur           |                              |
| (10-É | parallèle**                  |                              |
| lectr |                              |                              |
| oniqu | ![](10-Éle                   |                              |
| e de  | ctronique de Puissance/Cours |                              |
| Puiss | /pandoc/media/image44.jpeg){ |                              |
| ance/ | width="3.1131944444444444in" |                              |
| Cours | he                           |                              |
| /pand | ight="2.7368055555555557in"} |                              |
| oc/me |                              |                              |
| dia/i | 4.                           |                              |
| mage1 |   ![](10-Électronique de Pui |                              |
| 8.png | ssance/Cours/pandoc/media/im |                              |
| ){wid | age35.jpeg){width="2.4125in" |                              |
| th="0 |                              |                              |
| .6262 | height="1.6375in"}Identifier |                              |
| 69685 |     les sources              |                              |
| 03937 |     (tension/courant et      |                              |
| 01in" |     l'approximation utilisée |                              |
| >     |     pour la source de        |                              |
| heigh |     courant (I constant,     |                              |
| t="0. |     L-E, R-L-E) et tracer    |                              |
| 65083 |     l'allure du courant.     |                              |
| 33333 |                              |                              |
| 33333 | > **Source de courant de     |                              |
| 4in"} | > type L-E**                 |                              |
|       |                              |                              |
|       | 5.  Regarder la commande des |                              |
|       |     interrupteurs.           |                              |
|       |                              |                              |
|       | **K passant de 0 à**         |                              |
|       | $\mathbf{\alpha T}$ **(donc  |                              |
|       | D bloquée -- commande        |                              |
|       | complémentaire)**            |                              |
|       |                              |                              |
|       | **D passante de**            |                              |
|       | $\mathbf{\alpha T}$ **à**    |                              |
|       | $\mathbf{T}$ **(donc K       |                              |
|       | bloqué -- commande           |                              |
|       | complémentaire)**            |                              |
|       |                              |                              |
|       | 6.  Dessiner des schémas     |                              |
|       |     équivalents pour les     |                              |
|       |     phases de                |                              |
|       |     fonctionnement.          |                              |
+=======+==============================+==============================+
|       | **0 \< t \<**                | $\mathbf{\alpha}$**T \< t \< |
|       | $\mathbf{\alpha}$**T**       | T**                          |
|       |                              |                              |
|       | Dans le cas où K est         | Dans le cas où K est bloqué, |
|       | passant, la diode D est      | la diode D est naturellement |
|       | bloquée puisqu'elle est      | passante (diode roue libre   |
|       | polarisée en inverse (v~D~=  | assurant la continuité du    |
|       | -E). Le schéma équivalent    | courant dans l'inductance).  |
|       | est alors le suivant :       | Le schéma équivalent est le  |
|       |                              | suivant :                    |
|       | ![](10-Éle                   |                              |
|       | ctronique de Puissance/Cours | ![](10-Éle                   |
|       | /pandoc/media/image45.jpeg){ | ctronique de Puissance/Cours |
|       | width="3.2916666666666665in" | /pandoc/media/image46.jpeg){ |
|       | he                           | width="3.2993055555555557in" |
|       | ight="1.2784722222222222in"} | he                           |
|       |                              | ight="1.2666666666666666in"} |
+-------+------------------------------+------------------------------+
|       | 5.  Ecrire la loi des        |                              |
|       |     mailles et la loi des    |                              |
|       |     nœuds avec les           |                              |
|       |     interrupteurs            |                              |
|       |                              |                              |
|       | $$\mathbf                    |                              |
|       | {U}_{\mathbf{e}}\mathbf{=}\m |                              |
|       | athbf{u}_{\mathbf{K}}\mathbf |                              |
|       | {+}\mathbf{u}_{\mathbf{D}}$$ |                              |
|       |                              |                              |
|       | $$\mathbf                    |                              |
|       | {i}_{\mathbf{L}}\mathbf{=}\m |                              |
|       | athbf{i}_{\mathbf{K}}\mathbf |                              |
|       | {+}\mathbf{i}_{\mathbf{D}}$$ |                              |
+-------+------------------------------+------------------------------+
|       | 6.  Tracer les chronogrammes |                              |
|       |     sur une période en       |                              |
|       |     utilisant les schémas    |                              |
|       |     équivalents              |                              |
|       |                              |                              |
|       | ![](10-Éle                   |                              |
|       | ctronique de Puissance/Cours |                              |
|       | /pandoc/media/image47.jpeg){ |                              |
|       | width="2.7395833333333335in" |                              |
|       | h                            |                              |
|       | eight="4.420833333333333in"} |                              |
|       |                              |                              |
|       | 8.  Bien vérifier que le     |                              |
|       |     produit courant tension  |                              |
|       |     pour un interrupteur     |                              |
|       |     parfait est nul (passant |                              |
|       |     u=0, i≠0 et bloqué i=0,  |                              |
|       |     u≠0)                     |                              |
|       |                              |                              |
|       | 9.  Déterminer les grandeurs |                              |
|       |     demandées (valeur        |                              |
|       |     moyenne, valeur          |                              |
|       |     efficace,...), bien      |                              |
|       |     penser à la maille de    |                              |
|       |     l'inductance pour        |                              |
|       |     l'ondulation de courant  |                              |
|       |                              |                              |
|       | **En régime permanent, il    |                              |
|       | est possible de déterminer   |                              |
|       | la tension de sortie Vs en   |                              |
|       | utilisant l'égalité sur les  |                              |
|       | valeurs moyennes.**          |                              |
|       |                              |                              |
|       | $$\m                         |                              |
|       | athbf{E = <}\mathbf{u}_{\mat |                              |
|       | hbf{K}}\mathbf{> + <}\mathbf |                              |
|       | {u}_{\mathbf{L}}\mathbf{>}$$ |                              |
|       |                              |                              |
|       | **Nous pouvons trouver       |                              |
|       | \<u~K~\> avec les            |                              |
|       | chronogrammes précédents     |                              |
|       | mais nous n'avons aucune     |                              |
|       | information sur u~L~(t).**   |                              |
|       |                              |                              |
|       | $$\mathbf{<}                 |                              |
|       | \mathbf{u}_{\mathbf{K}}\math |                              |
|       | bf{(t) > =}\frac{\mathbf{1}} |                              |
|       | {\mathbf{T}}\int_{\mathbf{0} |                              |
|       | }^{\mathbf{T}}{\mathbf{u}_{\ |                              |
|       | mathbf{K}}\mathbf{(t)}}\math |                              |
|       | bf{dt =}\frac{\mathbf{1}}{\m |                              |
|       | athbf{T}}\left\lbrack \mathb |                              |
|       | f{V}_{\mathbf{s}}\mathbf{.}\ |                              |
|       | left( \mathbf{T}\mathbf{-}\m |                              |
|       | athbf{\alpha T} \right) \rig |                              |
|       | ht\rbrack\mathbf{=}\boxed{\l |                              |
|       | eft( \mathbf{1}\mathbf{-}\ma |                              |
|       | thbf{\alpha} \right)\mathbf{ |                              |
|       | .}\mathbf{V}_{\mathbf{s}}}$$ |                              |
|       |                              |                              |
|       | $$\mathbf{<}\mathbf{         |                              |
|       | u}_{\mathbf{L}}\mathbf{(t) > |                              |
|       |  =}\frac{\mathbf{1}}{\mathbf |                              |
|       | {T}}\int_{\mathbf{0}}^{\math |                              |
|       | bf{T}}{\mathbf{u}_{\mathbf{L |                              |
|       | }}\mathbf{(t)}}\mathbf{dt}$$ |                              |
|       |                              |                              |
|       | $$\mat                       |                              |
|       | hbf{<}\mathbf{u}_{\mathbf{L} |                              |
|       | }\mathbf{(t) > =}\frac{\math |                              |
|       | bf{1}}{\mathbf{T}}\int_{\mat |                              |
|       | hbf{0}}^{\mathbf{T}}{\mathbf |                              |
|       | {L}\frac{\mathbf{d}\mathbf{i |                              |
|       | }_{\mathbf{L}}\mathbf{(t)}}{ |                              |
|       | \mathbf{dt}}}\mathbf{dt =}\f |                              |
|       | rac{\mathbf{L}}{\mathbf{T}}\ |                              |
|       | int_{\mathbf{i}_{\mathbf{L}} |                              |
|       | \mathbf{(0)}}^{\mathbf{i}_{\ |                              |
|       | mathbf{L}}\mathbf{(T)}}{\mat |                              |
|       | hbf{d}\mathbf{i}_{\mathbf{L} |                              |
|       | }\mathbf{(t)}}\mathbf{= 0}$$ |                              |
|       |                              |                              |
|       | $$\mathbf{E = <}\ma          |                              |
|       | thbf{u}_{\mathbf{K}}\mathbf{ |                              |
|       | > + <}\mathbf{u}_{\mathbf{L} |                              |
|       | }\mathbf{> \  = \  <}\mathbf |                              |
|       | {u}_{\mathbf{K}}\mathbf{>}$$ |                              |
|       |                              |                              |
|       | $$\mathbf{V}_{\              |                              |
|       | mathbf{s}}\mathbf{=}\boxed{\ |                              |
|       | frac{\mathbf{E}}{\mathbf{1}\ |                              |
|       | mathbf{-}\mathbf{\alpha}}}$$ |                              |
|       |                              |                              |
|       | **En théorie, V~s~ peut être |                              |
|       | infinie mais en réalité elle |                              |
|       | est limitée par les          |                              |
|       | semi-conducteurs qui ne sont |                              |
|       | pas parfaits.**              |                              |
|       |                              |                              |
|       | #####                        |                              |
|       |  Calcul de l'ondulation de c |                              |
|       | ourant {#calcul-de-londulati |                              |
|       | on-de-courant-1 .unnumbered} |                              |
|       |                              |                              |
|       | **L'ondulation de courant    |                              |
|       | notée**                      |                              |
|       | $\mathbf{\De                 |                              |
|       | lta}\mathbf{i}_{\mathbf{L}}$ |                              |
|       | **correspond à la différence |                              |
|       | entre la valeur minimale et  |                              |
|       | maximale du courant          |                              |
|       | traversant l'inductance sur  |                              |
|       | une période.**               |                              |
|       |                              |                              |
|       | $$                           |                              |
|       | \mathbf{\Delta}\mathbf{i}_{\ |                              |
|       | mathbf{L}}\mathbf{=}\mathbf{ |                              |
|       | i}_{\mathbf{Lmax}}\mathbf{-} |                              |
|       | \mathbf{i}_{\mathbf{Lmin}}$$ |                              |
|       |                              |                              |
|       | **Pour**$\mathbf{\           |                              |
|       |  0\  < \ t\  < \alpha T}$**, |                              |
|       | il y a transfert direct      |                              |
|       | d'énergie entre la source et |                              |
|       | la charge. On a alors le     |                              |
|       | courant traversant           |                              |
|       | l'inductance L qui vaut :**  |                              |
|       | $\mathbf                     |                              |
|       | {u}_{\mathbf{L}}\mathbf{= L} |                              |
|       | \frac{\mathbf{d}\mathbf{i}_{ |                              |
|       | \mathbf{L}}}{\mathbf{dt}}\ma |                              |
|       | thbf{= E}\mathbf{-}\mathbf{u |                              |
|       | }_{\mathbf{K}}\mathbf{\ }\ma |                              |
|       | thbf{\Rightarrow}\frac{\math |                              |
|       | bf{d}\mathbf{i}_{\mathbf{L}} |                              |
|       | }{\mathbf{dt}}\mathbf{=}\fra |                              |
|       | c{\mathbf{E\ }}{\mathbf{L}}$ |                              |
|       |                              |                              |
|       | **On a donc le courant qui   |                              |
|       | va croître (E \> 0) à partir |                              |
|       | d'une valeur minimale        |                              |
|       | i~Lmin~ et on a :**          |                              |
|       |                              |                              |
|       | $$\boxed{\mathbf{i}_{\       |                              |
|       | mathbf{L}}\mathbf{(t) =}\fra |                              |
|       | c{\mathbf{E\ }}{\mathbf{L}}\ |                              |
|       | mathbf{t\  + \ }\mathbf{i}_{ |                              |
|       | \mathbf{Lmin}}}\mathbf{\ pou |                              |
|       | r\ 0\  < \ t\  < \alpha T}$$ |                              |
|       |                              |                              |
|       | $$\boxed                     |                              |
|       | {\mathbf{i}_{\mathbf{L}}\mat |                              |
|       | hbf{(t) =}\frac{\mathbf{E}\m |                              |
|       | athbf{-}\mathbf{V}_{\mathbf{ |                              |
|       | s}}\mathbf{\ }}{\mathbf{L}}\ |                              |
|       | mathbf{t\  + \ }\mathbf{i}_{ |                              |
|       | \mathbf{Lmax}}}\mathbf{\ pou |                              |
|       | r\ \alpha T\  < \ t\  < T}$$ |                              |
|       |                              |                              |
|       | $$\mathbf{\Delt              |                              |
|       | a}\mathbf{i}_{\mathbf{L}}\ma |                              |
|       | thbf{=}\mathbf{i}_{\mathbf{L |                              |
|       | max}}\mathbf{-}\mathbf{i}_{\ |                              |
|       | mathbf{Lmin}}\mathbf{=}\math |                              |
|       | bf{i}_{\mathbf{L}}\mathbf{(\ |                              |
|       | alpha T)}\mathbf{-}\mathbf{i |                              |
|       | }_{\mathbf{Lmin}}\mathbf{=}\ |                              |
|       | frac{\mathbf{E}}{\mathbf{L}} |                              |
|       | \mathbf{\alpha T\ }\boxed{\m |                              |
|       | athbf{+ \ }\mathbf{i}_{\math |                              |
|       | bf{Lmin}}}\boxed{\mathbf{-}\ |                              |
|       | mathbf{i}_{\mathbf{Lmin}}}$$ |                              |
|       |                              |                              |
|       | $$\bo                        |                              |
|       | xed{\mathbf{\Delta}\mathbf{i |                              |
|       | }_{\mathbf{L}}\mathbf{=}\fra |                              |
|       | c{\mathbf{E\ }}{\mathbf{L}}\ |                              |
|       | mathbf{\alpha T =}\frac{\mat |                              |
|       | hbf{V}_{\mathbf{s}}\mathbf{\ |                              |
|       |  }}{\mathbf{LF}}\mathbf{\alp |                              |
|       | ha}\left( \mathbf{1}\mathbf{ |                              |
|       | -}\mathbf{\alpha} \right)}$$ |                              |
+-------+------------------------------+------------------------------+

### Quadrants du hacheur Boost

![](10-Électronique de Puissance/Cours/pandoc/media/image48.jpeg){width="3.1034722222222224in"
height="1.1666666666666667in"}Un **hacheur parallèle** est un
convertisseur DC-DC permettant d'obtenir une tension de sortie continue
et **supérieure** **à la tension d'entrée**. Le schéma de principe est
le suivant.

![](10-Électronique de Puissance/Cours/pandoc/media/image49.jpeg){width="3.428472222222222in"
height="1.2819444444444446in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image50.jpeg){width="6.739583333333333in"
height="1.6319444444444444in"}Si on considère que la source de tension
est V~s~, on obtient le schéma suivant ou **la charge (L, E) devient
génératrice**. **La tension de sortie est variable mais toujours
positive. Le hacheur parallèle** est un convertisseur **non réversible
en tension et en courant.** **Cependant, dans ce cas, le quadrant de
fonctionnement est un quadrant générateur.**

## Hacheur 2 quadrants (2Q)

### ![](10-Électronique de Puissance/Cours/pandoc/media/image51.jpeg){width="2.645138888888889in" height="1.9166666666666667in"}Constitution du hacheur 2 quadrants

Le hacheur série et le hacheur parallèle sont deux **convertisseurs
unidirectionnels**. Si on veut pouvoir réaliser de la **récupération
d'énergie** (transfert de la charge vers la source) à **vitesse
variable**, il faut associer ces deux structures de hacheur.

Cette structure est très utilisée pour les applications à vitesse
variable ne nécessitant qu'une inversion en courant (fonctionnement dans
les quadrants 1 et 4) comme le Scot'elec, le VAE, la 106 Vedelic ...

![](10-Électronique de Puissance/Cours/pandoc/media/image52.jpeg){width="6.145833333333333in"
height="1.75625in"}

### Commande complémentaire

![](10-Électronique de Puissance/Cours/pandoc/media/image53.jpeg){width="3.0381944444444446in"
height="1.6284722222222223in"}

L'ensemble T~1~-D~2~ correspond à un hacheur série et l'ensemble
T~2~-D~1~ correspond à un hacheur parallèle.

Afin d'éviter le court-circuit de la source de tension, on commande K~1~
et K~2~ de manière complémentaire.

![](10-Électronique de Puissance/Cours/pandoc/media/image54.jpeg){width="2.3673611111111112in"
height="2.3993055555555554in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image55.jpeg){width="4.410416666666666in"
height="2.1979166666666665in"}

Lorsqu'un des interrupteurs (K~1~ ou K~2~) est fermé, il y a **un des
deux semi-conducteurs qui le compose (D~i~ ou T~i~) qui conduit suivant
le signe du courant.**

### Formes d'onde

Les composants passants dépendent de la charge et du signe du courant.
Pour tracer les chronogrammes, on peut remplacer K~1~ et K~2~ par deux
interrupteurs bidirectionnels en courant et commandés de manière
complémentaire.

Lorsqu'un des interrupteurs (K~1~ ou K~2~) est fermé, il y a **un des
deux semi-conducteurs qui le compose (D~i~ ou T~i~) qui conduit.** La
conduction dépendra de la commande et du sens du courant.

![](10-Électronique de Puissance/Cours/pandoc/media/image56.jpeg){width="4.183333333333334in"
height="1.3097222222222222in"}

Il existe alors 3 cas possibles :

-   \<i\> \> 0 ;

-   \<i\> = 0 ;

-   \<i\> \< 0 .

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **\<i\> \> 0**                                                                                   **\<i\> \< 0**                                                                                   **\<i\> = 0**
  ------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------
  ![](10-Électronique de Puissance/Cours/pandoc/media/image57.jpeg){width="2.3766830708661417in"   ![](10-Électronique de Puissance/Cours/pandoc/media/image58.jpeg){width="2.3048611111111112in"   ![](10-Électronique de Puissance/Cours/pandoc/media/image59.jpeg){width="2.3727646544181975in"
  height="3.128571741032371in"}                                                                    height="3.0347222222222223in"}                                                                   height="3.128571741032371in"}

  Dans le cas où \<i\> \> 0, le fonctionnement du hacheur 2Q est analogue à celui du hacheur       Dans le cas où \<i\> \< 0, le fonctionnement du hacheur 2Q est analogue à celui du hacheur       Dans le cas où \<i\> = 0, le fonctionnement du hacheur 2Q est analogue alternativement à celui
  série. Le **fonctionnement est alors moteur**.                                                   parallèle. Le fonctionnement est alors celui du **freinage**.                                    du hacheur série et du hacheur parallèle. Le fonctionnement est alors celui d'un **moteur à
                                                                                                                                                                                                    vide.**
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Calcul de la tension de sortie et de l'ondulation de courant

Le calcul de la valeur de la tension de sortie est analogue à celui du
hacheur série.

$$< V_{s} > = < u_{D2}(t) > = \frac{1}{T}\int_{0}^{T}{u_{D2}(t)}dt = \frac{1}{T}\lbrack E.\alpha T\rbrack = \boxed{\alpha.E}$$

L'expression de l'ondulation de courant est aussi analogue à celle
trouvée pour le hacheur série.

$$\boxed{\Delta i_{L} = \frac{ET\ }{L}\alpha(1 - \alpha)}$$

## Hacheur 4 quadrants

### ![](10-Électronique de Puissance/Cours/pandoc/media/image60.jpeg){width="3.361111111111111in" height="1.3305555555555555in"}Constitution du hacheur 4 quadrants

Le passage du hacheur 4 quadrants au hacheur 2 quadrants est réalisé en
« dupliquant » la structure du hacheur 2Q. Il permet d'inverser le signe
de la tension et ainsi de fonctionner dans les quatre quadrants.

![](10-Électronique de Puissance/Cours/pandoc/media/image61.jpeg){width="3.529861111111111in"
height="3.223611111111111in"}Cette structure permet d'inverser le signe
de la tension aux bornes de la charge tout en gardant la réversibilité
en courant du hacheur 2Q.

**Il y a toujours deux interrupteurs qui conduisent simultanément.**

Pour tracer les chronogrammes, on peut remplacer K~1~, K~2~, K3 et K~4~
par quatre interrupteurs bidirectionnels en courant.

### Formes d'onde

![](10-Électronique de Puissance/Cours/pandoc/media/image62.jpeg){width="2.901388888888889in"
height="1.5027777777777778in"}Pour tracer les chronogrammes, on peut
remplacer K~1~ et K~2~ par deux interrupteurs bidirectionnels en courant
et commandés de manière complémentaire.

Lorsqu'un des interrupteurs (K~1~ ou K~2~) est fermé, il y a **un des
deux semi-conducteurs qui le compose (D~i~ ou T~i~) qui conduit.** La
conduction dépendra de la commande et du sens du courant.

Il existe alors 3 cas possibles : \<i\> \> 0 ; \<i\> = 0 ; \<i\> \< 0 .

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **\<i\> \> 0**                                                                                   **\<i\> \< 0**                                                                                  **\<i\> = 0**
  ------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------
  ![](10-Électronique de Puissance/Cours/pandoc/media/image63.jpeg){width="2.2676137357830273in"   ![](10-Électronique de Puissance/Cours/pandoc/media/image64.jpeg){width="2.250103893263342in"   ![](10-Électronique de Puissance/Cours/pandoc/media/image65.jpeg){width="2.2646905074365704in"
  height="2.984722222222222in"}                                                                    height="2.9857141294838145in"}                                                                  height="2.9857141294838145in"}

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Le fonctionnement dans les 4 quadrants dépend des signes des valeurs
moyennes du courant et de la tension.

### Calcul de la tension de sortie et de l'ondulation de courant

Le calcul de la valeur de la tension de sortie est analogue à celui du
hacheur série.

$$< V_{s} > = < u(t) > = \frac{1}{T}\int_{0}^{T}{u(t)}dt = \frac{1}{T}\left\lbrack U_{M}.\alpha T - U_{M}(T - \alpha T) \right\rbrack$$

$$< V_{s} > = < u(t) > = \frac{1}{T}\lbrack 2.E.\alpha T - ET\rbrack = \boxed{E\lbrack 2.\alpha - 1\rbrack}$$

Tous calculs faits, l'expression de l'ondulation de courant est le
double de celle trouvée pour les hacheurs 1Q et 2Q.

$$\boxed{\Delta i_{L} = 2\alpha(1 - \alpha)\frac{ET\ }{L}}$$

## Hacheur à conversion indirecte

Pour relier deux sources de tensions, une inductance jouant le rôle de
source de courant est ajoutée. L'énergie est alors stockée dans
l'inductance lors de la première phase puis restituées lors de la
seconde.

![](10-Électronique de Puissance/Cours/pandoc/media/image66.jpeg){width="2.7490080927384075in"
height="1.4648917322834645in"}![](10-Électronique de Puissance/Cours/pandoc/media/image67.jpeg){width="2.6726192038495187in"
height="1.448426290463692in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image68.jpeg){width="2.8756944444444446in"
height="2.998611111111111in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image69.wmf){width="3.2333333333333334in"
height="0.43767497812773404in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image70.wmf){width="0.775in"
height="0.530003280839895in"}

## Généralités sur les convertisseurs AC-DC

### Convertisseurs AC-DC

Les **convertisseurs AC-DC** associés à un filtre de sortie, permettent
d'obtenir une tension continue de valeur moyenne \<u~ch~\> à partir
d'une source de tension alternative sinusoïdale.

C'est le convertisseur statique le plus répandu et trois types sont
utilisés :

-   les **redresseurs non commandés utilisant des diodes** : ils ne
    permettent pas de régler la tension de sortie;

![](10-Électronique de Puissance/Cours/pandoc/media/image71.jpeg){width="5.976744313210848in"
height="1.3411865704286965in"}

-   les **redresseurs commandés utilisant des thyristors** : ils
    permettent de régler la tension de sortie ;

![](10-Électronique de Puissance/Cours/pandoc/media/image72.jpeg){width="3.2558136482939632in"
height="1.0604319772528434in"}

-   les **redresseurs MLI** : ils permettent d'absorber un courant
    sinusoïdal.

    Hypothèses et méthode d'étude

Pour simplifier l'étude, on considérera dans tout le cours que :

-   Les **interrupteurs sont idéaux** (pas de pertes, pas de chute de
    tension, ...);

-   Le **rendement du convertisseur est unitaire** (Les puissances
    actives d'entrées et de sortie sont égales);

-   La **conduction est continue** (le courant dans la charge ne
    s'annule jamais);

-   La tension d'entrée est sinusoïdale et de la forme (V est la valeur
    efficace):

$$v_{e}(t) = \overset{\hat{}}{V}.sin(\omega t) = V.\sqrt{2}.sin(\omega t)$$

[Pour étudier et dimensionner un redresseur, on peut procéder par les
différentes étapes suivantes :]{.underline}

-   **Identification de la commande** de chaque semi-conducteur (ou
    interrupteur) de puissance (voir s'il est commandé ou non, quel est
    le paramètre de commande,...)

-   **Identification de la charge** (courant constant, résistance, ...)

-   **Intervalles de conduction de chaque semi-conducteur** (ou
    interrupteur) de puissance

-   **Tracé des chronogrammes** des courants et tensions d'entrée, de
    sortie et dans les semi-conducteurs de puissance.

-   **Calcul des valeurs moyennes et efficaces** en fonction des
    paramètres de commandes

-   **Calcul des contraintes sur les semi-conducteurs**
    (Dimensionnement)

-   **Calcul du facteur de puissance**

-   (Dimensionnement des filtres d'entrées et de sortie)

## Redressement monophasé non commandé

### Diode de puissance

![](10-Électronique de Puissance/Cours/pandoc/media/image73.jpeg){width="0.85in"
height="0.6388888888888888in"}On parle de redresseur monophasé **non
commandé** pour les convertisseurs AC-DC **utilisant des diodes comme
interrupteurs** car ce sont des **composants non commandés**.

La diode de puissance correspond au composant de base de l'électronique
de puissance. Son symbole est représenté ci-contre où A représente
l'**anode** et K la **cathode**.

C'est un composant **unidirectionnel en courant et en tension** et dont
la **commutation est spontanée** et dépendante du signe du courant i~D~
et de la tension v~AK~ :

-   i~D~ \> 0 et v~AK~ \> 0 **interrupteur fermé (diode passante) ;**

-   v~AK~ \< 0 **interrupteur ouvert (diode bloquée).**

![](10-Électronique de Puissance/Cours/pandoc/media/image74.jpeg){width="3.115972222222222in"
height="1.6652777777777779in"}Pour une diode réelle (et pour le choix
d'une diode), les caractéristiques importantes sont les suivantes :

-   Courants moyen direct (I~FAV~);

-   Courants direct maximal (I~D~);

-   Courants direct maximal (I~FM~);

-   Tension inverse maximale (V~RRM~);

-   Tension de seuil (V~0~) et résistance dynamique (r~D~) pour le
    calcul des pertes.

[Exemples de diodes de puissance]{.underline}

![a8e4bfb76c55444250cfaf2e097d3388](10-Électronique de Puissance/Cours/pandoc/media/image75.jpeg){width="0.8354166666666667in"
height="0.8354166666666667in"}![narbi_1116422275_diode](10-Électronique de Puissance/Cours/pandoc/media/image76.jpeg){width="0.9731725721784776in"
height="0.8881408573928259in"}

![L4359069-01](10-Électronique de Puissance/Cours/pandoc/media/image77.jpeg){width="0.7506944444444444in"
height="0.5576388888888889in"}

[Exemples de convertisseur AC-DC (pont de diodes) intégré]{.underline}

![R395435-01](10-Électronique de Puissance/Cours/pandoc/media/image78.jpeg){width="1.0458333333333334in"
height="0.9972222222222222in"}

### Montage PD2

Les montages redresseurs double-alternance sont aussi appelés montages à
commutation parallèle double ou PDq, q représentant le nombre de phases.
En monophasé, on aura donc les **montages PD2** (pont de Graëtz)
représenté ci-dessous.

![](10-Électronique de Puissance/Cours/pandoc/media/image79.jpeg){width="2.453472222222222in"
height="1.26875in"}

$$v_{e}(t) = \overset{\hat{}}{V}.sin(\omega t) = 230.\sqrt{2}.sin(314.t)$$

Pour des diodes ayant leurs **cathodes communes (cathodes reliées entre
elles)**, la diode qui peut conduire est celle qui a **son potentiel
d'anode le plus élevé**.

Pour des diodes ayant leurs **anodes communes (anodes reliées entre
elles)**, la diode qui peut conduire est celle qui a **son potentiel de
cathode le plus bas**.

![](10-Électronique de Puissance/Cours/pandoc/media/image80.jpeg){width="3.3833333333333333in"
height="2.6875in"}

D~1~ et D~2~ ont leurs cathodes communes

D~3~ et D~4~ leurs anodes communes.

![](10-Électronique de Puissance/Cours/pandoc/media/image81.jpeg){width="3.0347331583552055in"
height="1.8255818022747157in"}![](10-Électronique de Puissance/Cours/pandoc/media/image82.jpeg){width="3.1548392388451445in"
height="1.8953488626421697in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image83.jpeg){width="2.9864402887139105in"
height="1.7906977252843395in"}![](10-Électronique de Puissance/Cours/pandoc/media/image84.jpeg){width="3.015404636920385in"
height="1.8139545056867892in"}

$$< v_{ch} > = \frac{1}{\pi}\int_{0}^{\pi}{v_{ch}(\theta)\ d\theta} = \frac{1}{\pi}\int_{0}^{\pi}{\overset{\hat{}}{V}.sin(\theta)\ d\theta}$$

$$< v_{ch} > = \frac{1}{\pi}\int_{0}^{\pi}{\overset{\hat{}}{V}.sin(\theta)\ d\theta} = \frac{\overset{\hat{}}{V}}{\pi}\left\lbrack - cos(\theta) \right\rbrack_{0}^{\pi}$$

$$< v_{ch} > = \frac{\overset{\hat{}}{V}}{\pi}\lbrack 1 + 1\rbrack_{0}^{\pi} = \boxed{\frac{2.\overset{\hat{}}{V}}{\pi} = \frac{2.V.\sqrt{2}}{\pi}}$$

$$I_{D1} = \sqrt{\frac{1}{2\pi}\left\lbrack {I_{ch}}^{2}.\pi - 0 \right\rbrack} = \boxed{\frac{I_{ch}}{\sqrt{2}} = 42,4\ A}$$

$$< i_{D1} \geq \frac{1}{2\pi}\left\lbrack I_{ch}.\pi - 0 \right\rbrack = \boxed{\frac{I_{ch}}{2} = 30\ A}$$

$$\boxed{V_{RRM} = - \overset{\hat{}}{V} = - 33\sqrt{2}\ V}$$

### Puissance instantanée et active

En régime sinusoïdal, les **échanges d'énergies ne peuvent plus être
quantifiés comme en continu** vu que courant et tension sont **variables
en tout instant**. On définit alors plusieurs puissances pour traduire
tous ces échanges d'énergies

![](10-Électronique de Puissance/Cours/pandoc/media/image85.jpeg){width="1.0229166666666667in"
height="0.5923611111111111in"}$Soit:\left\{ \begin{aligned}
 & \ u(t)\  = \ \ U.\sqrt{2}.cos(\omega.t) \\
 & \ i(t)\  = \ \ I.\sqrt{2}.cos(\omega.t - \phi)
\end{aligned} \right.\ $

La **puissance instantanée** est le produit de la tension par le courant
en valeurs instantanées : $\boxed{p(t) = u(t).i(t)}$

Elle traduit en tout instant les échanges d'énergie entre le réseau et
le dipôle. Elle s'exprime en **Watts (W).** En régime sinusoïdal elle
vaut:

![](10-Électronique de Puissance/Cours/pandoc/media/image86.jpeg){width="2.860465879265092in"
height="0.7190234033245845in"}

La puissance active est définie pour des signaux périodiques comme la
valeur moyenne de la puissance instantanée.

$$\boxed{P = < p > = \frac{1}{T}\int_{0}^{T}{u(t).i(t)dt}}$$

En régime sinusoïdal, la puissance active s'exprime par la relation
suivante.

$$\boxed{P = < p > = U.I.cos(\phi)}$$

On voit donc que la puissance active consommée dépend de notre "charge"
(i.e de notre récepteur et de l'association de dipôle réalisée). **U et
I sont les valeurs efficaces**

Le produit I.cos(j) est aussi appelé **intensité active** (I~a~) : c'est
l'intensité qui est réellement utile à notre charge :
$\boxed{P = U.I_{a}}$

### ![](10-Électronique de Puissance/Cours/pandoc/media/image87.jpeg){width="1.86875in" height="1.5458333333333334in"}Puissance réactive et puissance apparente

Le diagramme de Fresnel d'un dipôle en prenant la tension comme
référence des phases est le suivant :

L'intensité active ne correspond pas à la valeur du courant réellement
transportée par les lignes électriques.

Par analogie avec la puissance active on définit donc la puissance
réactive :

$$\boxed{Q = U.I.sin\phi}$$

Elle traduit l'importance de l'échange d'énergie entre la source et les
éléments réactifs (bobine et condensateur qui peuvent être vus comme des
"réactances"). Elle s'exprime en **VAR** (Voltampères Réactifs)

**Puissance apparente :**

La puissance apparente, notée S, ne traduit pas les échanges d'énergies
mais permet de réaliser le dimensionnement des différents éléments d'un
circuit (ex: transformateurs\...). Elle est définie par :
$\boxed{S = U.I}$

Elle s'exprime en **VA** (VoltAmpères). **U et I sont les valeurs
efficaces**

Des 3 puissances précédentes, on peut déduire les relations suivantes:

$$\boxed{S = \sqrt{P^{2} + Q^{2}}}\ et\ \boxed{Q = P.tan(\phi)}$$

Ces relations sont **valables uniquement lorsque la tension et le
courant sont sinusoïdaux**.

### Facteur de puissance

On définit le **facteur de puissance f~p~** comme le rapport entre la
puissance active et la puissance apparente :
$\boxed{f_{p} = \frac{P}{S}}$

Il est sans unité et il est toujours \<1.

**Importance du facteur de puissance :**

Un convertisseur AC-DC « branché » sur le réseau peut être vu par le
schéma suivant :

![](10-Électronique de Puissance/Cours/pandoc/media/image88.jpeg){width="3.4186056430446192in"
height="1.1130347769028872in"}

La **puissance active** est la puissance « réellement consommée » par la
charge et dans nos hypothèses (rendement unitaire du convertisseur),
elle est égale à la puissance active « vue » par le réseau. Le facteur
de puissance « vu par le réseau » est donc :

$$\boxed{f_{p} = \frac{P_{e}}{S_{e}}\underset{\eta = 1}{\overset{=}{︸}}\frac{P_{ch}}{U_{e}.I_{e}}}$$

La section des câbles transportant l'électricité, dépend de la valeur
efficace du courant les traversant.

$$\boxed{I_{e} = \frac{P_{ch}}{U_{e}.f_{p}}}$$

Le convertisseur AC-DC doit non seulement permettre la conversion avec
un très bon rendement mais aussi avec un facteur de puissance le plus
proche de 1 afin de ne pas surdimensionner les éléments en amont
(transformateur, ...).

### Décomposition en série de Fourier

Dans les convertisseurs AC-DC, le courant fourni par le réseau **n'est
pas purement sinusoïdal** mais périodique. La théorie en régime
sinusoïdal n'est donc plus utilisable.

Cependant, le **courant étant périodique**, il est décomposable en
**série de Fourier**. Le courant est alors une **somme infinie de
fonctions sinusoïdales de fréquences multiples** qu'on appelle
**harmoniques**. Un circuit comportant des signaux non sinusoïdaux peut
donc être étudié par la superposition de signaux sinusoïdaux.

**[Théorème de Fourier :]{.underline}**

Un signal s(t) (continu et dérivable) de période T (**fréquence f**)
peut être décomposé en une somme comprenant :

-   Un **terme constant** (sa valeur moyenne);

-   Un terme sinusoïdal de fréquence f (appelé **fondamental ou premier
    harmonique**);

-   Une suite (infinie ou non) de fonctions sinusoïdales de fréquence
    multiple entier de f que l'on appelle **harmoniques**.

$$\boxed{s(t) = a_{0} + \sum_{n = 1}^{\infty}S_{n}sin\ (n.\omega.t + \phi_{n})}$$

Où :

-   S~0~ est la valeur moyenne du signal (composante continue);

-   S~n~ est **l'amplitude** de l'harmonique de rang n (ou coefficient
    de Fourier de rang n), (composante alternative);

-   j~n~ est la phase du signal de rang n.

Le spectre d'un signal est un graphique ayant en abscisse le rang des
harmoniques et en ordonnées la valeur efficace des harmoniques (qui peut
être ramené par rapport au fondamental).

**[Exemple du signal carré :]{.underline}**

![](10-Électronique de Puissance/Cours/pandoc/media/image89.jpeg){width="2.7325590551181103in"
height="1.433814523184602in"}
![](10-Électronique de Puissance/Cours/pandoc/media/image90.jpeg){width="2.7674409448818897in"
height="1.5263713910761154in"}

La décomposition en série de Fourier a permis de déterminer l'expression
suivante :

$$\boxed{u(t) = \frac{4U_{\max}}{\pi}\sum_{p = 0}^{\infty}\frac{sin\ \left( (2p + 1)\omega t \right)}{(2p + 1)}\ \ }$$

$$\boxed{u(t) = \frac{4U_{\max}}{\pi}\left( sin\ (\omega t) + \frac{sin\ (3\omega t)}{3} + \frac{sin\ (5\omega t)}{5} + ... \right)\ }$$

### Puissance déformante

Dans le cas où le **courant absorbé par la charge ne soit pas purement
sinusoïdal mais périodique**, il est décomposable en série de Fourier.
On démontre alors que la **puissance active n'est transportée que par le
fondamental du courant**, on a alors:

$$\boxed{P_{e} = V_{e}.I_{e1}.cos\phi_{1}}\ et\ \boxed{Q_{e} = V_{e}.I_{e1}.sin\phi_{1}}$$

I~e1~ représente la valeur efficace du fondamental et j~1~ le déphasage
entre i~e1~(t) et v~e~(t). Cependant, les autres harmoniques de courant
existent et font partie de l'intensité efficace totale. Par définition,
on a toujours (en utilisant Parseval) :

$$\boxed{S_{e} = V_{e}.\sqrt{\sum_{n = 1}^{\infty}{I_{en}}^{2}}\ }$$

Par définition, les termes manquants qui représentent la puissance
transportée par les harmoniques de courant est appelée **puissance
déformante**. On a alors :

$$\boxed{{S_{e}}^{2} = \ {P_{e}}^{2} + {Q_{e}}^{2} + D^{2}\ }\ et\ \boxed{D = V_{e.}\sqrt{\sum_{n = 2}^{\infty}{I_{en}}^{2}}}$$

$$\boxed{f_{p} = \frac{P_{e}}{S_{e}} = \frac{P_{e}}{\sqrt{{P_{e}}^{2} + {Q_{e}}^{2} + D^{2}}}}$$

Dans le cas des **convertisseurs AC-DC cette puissance déformante est
présente** et influe grandement sur le facteur de puissance. En général,
on ne demande pas de la calculer mais il est important de savoir qu'elle
existe et qu'elle **influe sur le dimensionnement**. Pour **éliminer les
harmoniques**, on utilise des **filtres (passifs ou actifs)** qui
permettent de respecter la norme CEI 61000-3-2.

### Transformateur monophasé parfait

![](10-Électronique de Puissance/Cours/pandoc/media/image91.jpeg){width="3.685416666666667in"
height="1.8597222222222223in"}Le transformateur monophasé est un
dispositif utilisé pour **adapter l'énergie électrique alternative.** Il
permet d'isoler deux réseaux électriques : c'est **l'isolation
galvanique**. Le transfert d'énergie se fait magnétiquement

![](10-Électronique de Puissance/Cours/pandoc/media/image92.jpeg){width="3.441666666666667in"
height="0.6430555555555556in"}Il est constitué d'un circuit magnétique
sur lequel sont bobinés disposés deux enroulements conducteurs et
isolés : **l'enroulement primaire et l'enroulement secondaire.**

Les symboles utilisés sont les suivants :

Sur ces deux symboles, on a repéré les **bornes homologues** qui
représentent le **sens des bobinages, donc du champ magnétique crée**
(un courant entrant par une borne homologue crée un **flux positif**
dans le circuit magnétique).

On définit **le rapport de transformation m **:

$$\boxed{m\  = \frac{N_{2}}{N_{1}} = \frac{U_{2}}{U_{1}} = \frac{I_{1}}{I_{2}}}$$

Si **m \> 1,** le transformateur est **élévateur de tension,** sinon il
est **abaisseur.**

Le transformateur est un dispositif qui est parfaitement **réversible**
(on peut inverser le rôle du primaire et du secondaire). Dans le cas du
transformateur parfait, toutes les puissances se conservent et le
rendement est don égal à 1 :
$\boxed{P_{1} = P_{2}},\ \boxed{Q_{1} = Q_{2}},\ \boxed{S_{1} = S_{2}}$

## Redresseur à absorption sinusoïdale

### Introduction

Le redresseur à absorption sinusoïdal est le « dernier né » et pallie
aux problèmes de facteur de puissance. En effet, les différentes
solutions que nous avons pu voir ne permettent pas d'obtenir un facteur
de puissance unitaire et une tension de sortie parfaitement continue.

Le redresseur à absorption sinusoïdale ou PFC (Power Factor Corrector)
est un redresseur dont la commande est asservie en courant, pour un
obtenir un courant d'entrée sinusoïdal et ainsi réduire les harmoniques
de basses fréquences. Ces redresseurs sont aussi asservis en tension
pour obtenir une tension continue.

On a principalement deux structures :

-   la structure deux étages utilisant un convertisseur Boost (hacheur
    élévateur);

-   la structure mono-étage ou convertisseur PFC.

![zer](10-Électronique de Puissance/Cours/pandoc/media/image93.jpeg){width="3.5215277777777776in"
height="2.082638888888889in"}![ghfj](10-Électronique de Puissance/Cours/pandoc/media/image94.jpeg){width="3.1506944444444445in"
height="1.9597222222222221in"}

### Structure à deux étages

Dans cette structure, on utilise comme charge un hacheur boost (ou
élévateur de tension) dont on asservit la commande pour obtenir un
courant d'entrée sinusoïdal (pour ne pas avoir d'harmoniques) et en
phase avec la tension d'entrée (pour ne pas avoir de puissance
réactive).

Pour cela il y a deux boucles qui sont réalisées : une **boucle de
courant** pour absorber un courant sinusoïdal en phase avec la tension
d'entrée et une **boucle de tension** afin d'obtenir une tension
constante aux bornes de la charge.

La consigne est alors élaborée à partir de la tension réseau dont on
prend la valeur absolue. Cette consigne est comparée au courant absorbé
par la charge (redressé double alternance.

Les courbes obtenues par cette structure sont représentées sur les
figures suivantes où on peut s'apercevoir que le courant est
parfaitement en phase avec la tension d'entrée. Il persiste quelques
harmoniques mais qui sont de fréquences assez élevées et qui peuvent
être éliminées par filtrage.

![qsd](10-Électronique de Puissance/Cours/pandoc/media/image95.jpeg){width="3.593748906386702in"
height="3.593748906386702in"}

### Structure mono étage

Dans la structure mono-étage, on utilise la même structure que le
hacheur 4 quadrants. La commande est alors élaborée de la même manière
que précédemment en utilisant deux boucles de courant et de tension. La
consigne est elle aussi générée de la même manière comme le montre la
figure suivante.

![ghfj](10-Électronique de Puissance/Cours/pandoc/media/image94.jpeg){width="3.1506944444444445in"
height="1.9597222222222221in"}

L'avantage de la structure à deux étages est de permettre une dynamique
plus élevée pour le courant. Ces structures sont aujourd'hui utilisées
dans les petites alimentations du fait des grandes restrictions
appliquées par les normes. Elles sont aussi présentes dans les systèmes
éoliens car elles permettent de fournir de l'énergie réactive.

## Sources

Ce cours a été élaboré à l'aide de nombreuses ressources provenant de
différents collègues de l'UPSTI.\

## Exercices du chapitre

![](10-Électronique de Puissance/Cours/pandoc/media/image96.png){width="5.466666666666667in"
height="8.373527996500437in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image97.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![scooter](10-Électronique de Puissance/Cours/pandoc/media/image98.jpeg){width="0.9625in"
height="0.6416666666666667in"}
![chariot_situation](10-Électronique de Puissance/Cours/pandoc/media/image99.jpeg){width="0.6508978565179353in"
height="0.6744181977252843in"} **CHARIOT DE GOLF ÉLECTRIQUE**

**Mise en situation**

![](10-Électronique de Puissance/Cours/pandoc/media/image100.png){width="2.126388888888889in"
height="1.7409722222222221in"}Le terrain de golf est constitué d'un
parcours comprenant de 9 à 18 trous, que le golfeur doit parcourir
successivement. La distance totale effectuée pour 18 trous est d'environ
8 km et le temps de jeu d'environ 4h.

![](10-Électronique de Puissance/Cours/pandoc/media/image101.jpeg){width="1.4743055555555555in"
height="1.4465277777777779in"}L'ensemble des clubs nécessaires (maximum
de 14 ) ainsi que le sac permettant de les ranger représente un poids
d'environ 20 kg. Le golf est un sport qui nécessite beaucoup de
concentration, d'adresse, et une bonne condition physique. Afin de
permettre au joueur d'économiser le maximum d'énergie, le transport du
matériel est assuré par un chariot à propulsion électrique.

Ce chariot permet de ransporter sans effort sur 2 parcours de golf de 18
trous vallonnés secs ou boueux (**12 à 15 Km**) un sac de golf de 20
kilos à l'aide d'un **véhicule à énergie électrique embarquée pour des
vitesses variant entre 1 km/h et 8 km/h.**

Le chariot de golf est un véhicule avec énergie embarquée.
L'alimentation en énergie est assurée par un accumulateur (batterie) de
24 Ah et une tension de 12 V. La motorisation est constituée d'un moto
réducteur à roue et vis sans fin transmettant le mouvement aux roues.
Pour effectuer les virages, les roues comportent des roues libres.

La commande du moteur en vitesse variable est effectuée en boucle
ouverte (pas de retour d\'information du moteur vers la partie
commande). Le principe utilisé est basé sur le \"hachage\" de la source
de tension continue (Ubat=12v) à partir d\'un signal de commande (Uc) de
type M.L.I. (Modulation de Largeur d\'Impulsion).

![golf](10-Électronique de Puissance/Cours/pandoc/media/image102.jpeg){width="5.1194444444444445in"
height="2.0416666666666665in"}La modulation de largeur d\'impulsion
(MLI) consiste à générer aux bornes du moteur une tension rectangulaire
périodique :

• de fréquence élevée par rapport à l\'inertie du moteur.

• de rapport cyclique α variable.

Le microprocesseur génère le signal de commande du hacheur (UcPIC) sous
forme d\'un signal carré à fréquence fixe (T = 130μs) et rapport
cyclique (α) variable.

**Travail demandé**

1.  **Déterminer** les quadrants de fonctionnement du moteur du chariot
    de golf électrique.

2.  **Déterminer** les quadrants de fonctionnement du variateur associé
    à la MCC.

![toto](10-Électronique de Puissance/Cours/pandoc/media/image103.jpeg){width="2.966666666666667in"
height="3.092361111111111in"}

On considérera dans un premier temps que la machine à courant continu
est équivalent à une source de courant idéale.

La diode et les transistors sont considérés comme idéaux. C'est un
hacheur série. L'interrupteur K est commandé de 0 à αT.

![](10-Électronique de Puissance/Cours/pandoc/media/image104.jpeg){width="2.703077427821522in"
height="2.151162510936133in"}

3.  **Représenter** les tensions u(t) et v~DS~(t) sur une période de
    découpage et pour un rapport cyclique α = 0,5.

4.  **Déterminer** la relation entre \<u\>, la tension de la batterie
    U~b~ et le rapport cyclique α.

![](10-Électronique de Puissance/Cours/pandoc/media/image105.jpeg){width="2.9916666666666667in"
height="1.429861111111111in"}

Le moteur d\'entraînement utilisé est une MCC à aimants permanents de
tension nominale 12 V. Le rapport de réduction est 25 et le diamètre des
roues est de 300 mm. Tension d\'alimentation de l\'induit : U~N~ = 12 V
; Résistance de l\'induit : R~a~ = 0,2 Ω, coefficient de fém k~e~ =0,028
V/rad/s.

Un premier modèle pour la MCC est une charge L~a~-E ci-contre.

5.  **Déterminer** la relation entre la tension \<u\> et la fém E.

6.  **Déterminer** la relation entre la fém E et la vitesse du
    chariot V. En déduire la relation entre \<u\> et la vitesse du
    chariot de golf.

7.  ![](10-Électronique de Puissance/Cours/pandoc/media/image106.jpeg){width="2.676388888888889in"
    height="1.2784722222222222in"}**Déterminer** la relation entre la
    vitesse V (en km/h) du chariot et le rapport cyclique α.
    **Conclure** si les vitesses annoncées dans le cahier des charges
    sont atteignables.

Un essai a permis de déterminer que, sur terrain plat, le chariot de
golf ne démarre que pour un rapport cyclique minimal de 20%. Le modèle
précédent était incomplet et on utilise un deuxième modèle pour la MCC :
une charge R-L-E.

8.  **Déterminer** le couple résistant total C~rd~ (incluant le couple
    de pertes du moteur) que doit vaincre le moteur au démarrage.

9.  **Donner** la nouvelle plage de variation de vitesse possible si on
    considère le couple résistant indépendant de la vitesse de rotation.

Afin d'éviter une conduction discontinue, on souhaite que l'ondulation
du courant soit limitée à 1 A. Pour réaliser cette étude, on considérera
la MCC comme une charge L-E.

10. **Donner** l'expression du courant d'induit, noté i~a~(t), dans le
    cas où les transistors sont commandés (on pourra faire un schéma
    équivalent). On notera i~amin~ la valeur initiale.

11. **Donner** l'expression du courant d'induit, noté ia(t), dans le cas
    où les transistors ne sont pas commandés (on pourra faire un schéma
    équivalent). On notera i~amax~ la valeur initiale.

12. **Déterminer** l'expression de l'ondulation de courant.

13. **Déterminer** l'expression de l'ondulation maximale de courant en
    fonction de U~b~, T et L~a~.

On souhaite une ondulation maximale de courant de 1 A afin d'éviter une
conduction discontinue. L'inductance d'induit du moteur vaut 470 mH.

14. **Déterminer** l'inductance d'induit minimale permettant d'obtenir
    l'ondulation maximale de 1 A. En déduire s'il est nécessaire
    d'ajouter une inductance en série avec le moteur.

![](10-Électronique de Puissance/Cours/pandoc/media/image107.jpeg){width="2.7042858705161854in"
height="3.4302318460192476in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image97.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![portail08_p](10-Électronique de Puissance/Cours/pandoc/media/image108.jpeg){width="0.7083333333333334in"
height="0.53125in"}**COMMANDE D'UN PORTAIL AUTOMATIQUE**

*([Source]{.underline} : ATS 2004)*

**Mise en situation**

1.  ![](10-Électronique de Puissance/Cours/pandoc/media/image109.png){width="2.4479166666666665in"
    height="1.7604166666666667in"}

    Le thème du sujet est l'étude d'une porte automatique coulissant. Un
    usager peut déclencher l'ouverture de la porte depuis son véhicule
    par une action sur la télécommande qui lui a été fournie.

Le synoptique du portail est représenté ci-contre :

*1a et 1b : barrière IR extérieure,*

*2a et 2b : barrière IR intérieure,*

![](10-Électronique de Puissance/Cours/pandoc/media/image110.png){width="2.602777777777778in"
height="1.5833333333333333in"}*3 : palpeur,*

*4a et 4b : capteurs de télécommande,*

*5a et 5b : capteurs de fin de course*

Le moteur et l'armoire électrique de commande ne sont pas représentés.

![](10-Électronique de Puissance/Cours/pandoc/media/image111.png){width="2.9270833333333335in"
height="1.0520833333333333in"}

Le moteur électrique de la porte de garage est alimentée par un hacheur
série dont la structure est représentée ci-dessous :

[Hypothèses :]{.underline}

-   D est une diode idéale sans seuil.

-   La tension aux bornes du moteur à courant continu est égale à sa
    f.e.m. E proportionnelle à la vitesse de rotation du moteur : E=k.N
    avec k=5,25.10^-2^ V/(tr.min^-1^).

-   L'intensité i du courant ne s'annule jamais et varie entre les
    valeurs minimales et maximales I~m~ et I~M~.

[Données :]{.underline}

-   La tension d'alimentation du hacheur est constante et vaut V~S~ =
    210 V.

-   K est un interrupteur commandé par la tension u~C~ représentée
    ci-dessous.

![](10-Électronique de Puissance/Cours/pandoc/media/image112.png){width="2.6770833333333335in"
height="1.28125in"}

Pour t∈\[0,αT\] K est fermé et pour t∈\[αT ,T\] K est ouvert. T
représente la période de découpage et vaut [T=0,1 ms]{.underline}.

**Étude de la commande**

**Question 1 :** **Représenter** l'allure de la tension v~D~ (t) sur le
**document réponse DR1**.

**Question 2 :** **Exprimer** la valeur moyenne de la tension v~D~ en
fonction de α et V~S~ puis en déduire la relation entre E, α et V~S~.

**Question 3 :** **Déterminer** la valeur du rapport cyclique α qui
permet de régler la vitesse de rotation du moteur à N = 1000 tr.min^-1^.

**Question 4 :** **Déterminer** l'expression de i(t) pour t ∈\[0,α*T*\]
puis pour t ∈\[α*T* ,*T*\].

**Question 5 :** **Exprimer** l'ondulation de courant Δi = I~M~ -- I~m~
en fonction de α, V~S~, L et T.

**Question 6 :** **Représenter** l'allure de Δi en fonction de α. Pour
quelle valeur de α l'ondulation de courant est-elle maximale ?
**Calculer** (Δi)~max.~

**Question 7 :** Représenter l'allure de i~K~ sur le **document réponse
DR1** et exprimer sa valeur moyenne en fonction de α, I~m~ et I~M~.

![](10-Électronique de Puissance/Cours/pandoc/media/image113.png){width="1.78125in"
height="2.8541666666666665in"}**Question 8 :** **Représenter** l'allure
de i~D~ sur le **document réponse DR1** et exprimer sa valeur moyenne en
fonction de α, I~m~ et I~M~.

En réalité, le hacheur n'alimente pas directement le moteur : on
intercale comme indiqué sur la figure ci-contre un système de relais
piloté par un interrupteur commandé par une tension v~3~.

Au repos, lorsque la tension aux bornes de la bobine est nulle, les
interrupteurs sont dans la position représentée sur la figure. Lorsque
la tension aux bornes de la bobine est égale à 12 V, les interrupteurs
sont dans l'autre position.

**Question 9 :** **Indiquer** les quadrants de fonctionnement possibles
du moteur obtenus par l'association « hacheur série + système de
relais ».

**Question 10 :** **Conclure** sur l'utilité de ce système de relais

**DOCUMENT RÉPONSE DR1**

![tre](10-Électronique de Puissance/Cours/pandoc/media/image114.jpeg){width="5.572916666666667in"
height="6.604166666666667in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image97.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![C:\\Users\\Thomas\\Desktop\\Prius.png](10-Électronique de Puissance/Cours/pandoc/media/image115.png){width="0.9395833333333333in"
height="0.5729166666666666in"}**TOYOTA PRIUS**

*([Source]{.underline} : Concours Centrale Supélec TSI 2006)*

**Mise en situation**

![figure01-petit](10-Électronique de Puissance/Cours/pandoc/media/image116.jpeg){width="2.8875in"
height="1.7583333333333333in"}Le constructeur automobile japonais
**TOYOTA** commercialise un véhicule de tourisme à motorisation hybride,
la **TOYOTA PRIUS**. Cette motorisation repose sur la combinaison d'un
moteur électrique et d'un moteur à essence.

L\'idée d\'associer à bord d\'un même véhicule, un moteur électrique et
un moteur thermique permet de conserver un excellent niveau de
performances dynamiques, tout en diminuant sensiblement la pollution en
milieu urbain, grâce à une gestion énergétique optimisée.

En **technologie hybride**, un **calculateur sélectionne le meilleur
mode opératoire** en fonction de n'importe quelle situation. Il opte
pour la propulsion électrique seule lorsque cela est possible ou pour
une répartition entre propulsion électrique et thermique lorsque cela
est nécessaire. La batterie se recharge automatiquement grâce au moteur
essence mais aussi lors des décélérations ou du freinage.

Les émissions de CO~2~ sont de 104 g.km^-1^, soit un niveau qui lui
permet de rivaliser avec les voitures diesel citadines, les émissions
d'oxyde d'azote et d'hydrates de carbone sont plus faibles que pour
n'importe quelle voiture à moteur thermique existante. Quant aux
émissions de particules, inconvénient important des moteurs diesel,
elles sont réduites à zéro.

![figure02](10-Électronique de Puissance/Cours/pandoc/media/image117.jpeg){width="4.166666666666667in"
height="2.3020833333333335in"}La chaîne simplifiée de transmission est
représentée ci-dessous.

*.*

Dans la **première version** de la PRIUS (année 2000) les convertisseurs
**CV7** et **CV9** étaient directement reliés à la batterie **BAT8**
(figure2).

Dans la **seconde version** **(étudiée ici)** de la PRIUS (année 2004),
le constructeur a intercalé un convertisseur DC/DC entre la batterie et
les convertisseurs **CV7** et **CV9.**

Ce convertisseur permet d'obtenir une tension d'alimentation de **CV7**
et **CV9** de 500 V à partir d'une tension aux bornes de la batterie
*BAT8* comprise entre 150 V et 260 V.

La structure du convertisseur DC-DC intercalé est la suivante :

![figure09](10-Électronique de Puissance/Cours/pandoc/media/image118.jpeg){width="4.239583333333333in"
height="2.3020833333333335in"} Les interrupteurs **K~1~** et **K~2~**
sont des **IGBT** (Insulated Gate Bipolar Transistor). La période du
signal de commande des interrupteurs **K~1~** et **K~2~** est **T~h~ =
50 µs**.

L'interrupteur **K~1~** est commandé à la fermeture de l'instant **t =
0** à l'instant **t = αT~h~**, puis à l'ouverture de l'instant **t =
αT~h~** à l'instant **t = T~h~**.

La commande de l'interrupteur **K~2~** est complémentaire de la commande
de l'interrupteur **K~1~**.

**Détermination de la plage de variation du rapport cyclique α**

La tension **U~0~** est la tension continue mesurée aux bornes de la
batterie. Cette tension **U~0~** dépend de la température de la
batterie, de la quantité d'électricité stockée dans la batterie et de la
valeur moyenne du courant **i~b~**. On donne **150 V \< U~0~ \< 260 V**.

**[Objectif de l'étude :]{.underline} Déterminer** la plage de variation
du rapport cyclique **α** permettant d'obtenir une tension **U~1~
constante** quelle que soit la valeur de la tension batterie **U~0~**.

**[Critère :]{.underline}** La tension **U~1~** doit être une tension
continue constante égale à **500 V**.

**[Hypothèses :]{.underline}**

-   Tous les interrupteurs sont considérés comme idéaux ;

-   La conduction est continue dans **BAT8** ;

-   Pendant une période de hachage, le courant **i~b~** est soit
    strictement positif, soit strictement négatif.

1.  ** Donner**, pour **0 ≤ t ≤ αT~h~**,, les expressions des grandeurs
    **u~c~ (t)**, **v~K1~ (t),** **v~K2~ (t) et u~L~(t)** en fonction de
    **U~1~** et **U~0~**.

2.  **  Donner**, pour **αT~h~ ≤ t ≤ T~h~**, les expressions des
    grandeurs **u~c~ (t)**, **v~K1~ (t),** **v~K2~ (t) et u~L~(t)** en
    fonction de **U~1~** et **U~0~**.

3.  **Déterminer** l'expression de **\<u~c~\>** en fonction de **α** et
    **U~1~**.

4.  **Déterminer** l'expression de **\<u~c~\>** en fonction de **U~0~**.
    **Exprimer** alors **α** en fonction de **U~0~** et **U~1~**.

5.   **Conclure** sur la plage de variation du rapport cyclique **α.**

**Dimensionnement de la bobine de lissage L du convertisseur DC / DC**

La durée de vie et la quantité d'électricité que l'on peut stocker dans
les batteries de type NiMH dépendent beaucoup de la valeur de
l'ondulation du courant batterie **i~b~**. Afin d'obtenir une durée de
vie de la batterie d'environ **150.000 km**, on souhaite limiter
l'ondulation de ce courant à **2 A** maximum, quel que soit le mode de
fonctionnement de la batterie.

**[Objectif de l'étude :]{.underline} Déterminer** la valeur de
l'inductance permettant d'obtenir une durée de vie de batterie d'environ
**150.000 km**.

**[Critère :]{.underline}** L'ondulation de courant doit toujours être
**inférieure à 2A**.

**[Hypothèses :]{.underline}**

-   Tous les interrupteurs sont considérés **idéaux** ;

-   La conduction est **continue** ;

-   Quelle que soit la valeur de **i~S~**, on a la relation **U~0~ =
    α U~1 ~**;

-   À **t = 0**, **i~b~ = i~bmini~**.

6.   **Établir**, pour **0 ≤ t ≤ αT~h~**, l'expression de **i~b~ (t)**
    en fonction de **U~1~**, **α**, **i~bmini~** et **L**.

7.  ** Établir** l'expression de l'ondulation **∆I~b~ = i~bmaxi~ --
    i~bmini~** en fonction de **U~1~**, **α**, **T~h~** et **L**.

8.  **Montrer** que l'ondulation **∆I~b~** est maximale pour une
    certaine valeur de **α**, notée **α~1~** dont vous donnerez la
    valeur numérique**.**

9.  ** Etablir** l'expression de **∆I~b~(α~1~).**

10.  **Conclure** sur la valeur minimale de l'inductance **L** de la
    bobine de lissage.

**Choix des interrupteurs du convertisseur DC / DC**

**[Objectif de l'étude :]{.underline} Déterminer** les contraintes en
tension et en courant pour les interrupteurs K~1~-D~1~ et K~2~-D~2~ et
**choisir** le module qui convient dans la documentation constructeur.

**[Hypothèses :]{.underline}**

a.  Tous les interrupteurs sont considérés comme idéaux ;

b.  Quelle que soit la valeur de **i~S~**, on a la relation **U~0~ =
    α U~1 ~**;

c.  On **[néglige l'ondulation du courant]{.underline}** i~b~(t). D'où
    i~b~ = I~b~ avec -- 200 A ≤ I~b~ ≤ 80 A.

```{=html}
<!-- -->
```
11.  **Indiquer**, à partir des réponses obtenues aux **questions 1 et
    > 2**, les valeurs numériques maximales des tensions aux bornes des
    > différents composants **K~1~, D~1~**, **K~2~** et **D~2~**.

12.  **Tracer** **i~D1~(t)**, **i~K1~ (t),** **i~K2~ (t), i~D2~(t)** et
    > **i~s~(t)** pour **α = 0,5**. Vous envisagerez les cas **I~b~ \>
    > 0** puis **I~b~ \< 0** et vous indiquerez les composants qui
    > doivent être passants dans chaque cas.

13.   À partir de la réponse à la question précédente, **déterminer**
    > les valeurs efficaces et moyennes des courants **i~D1~(t)**,
    > **i~K1~ (t),** **i~K2~ (t), i~D2~(t)** et **i~s~(t)** en fonction
    > de **α** et de **I~b~**.

14.   Compte-tenu des réponses aux questions **5** et **13**,
    > **indiquer** les valeurs numériques maximales des courants moyens
    > qui participent au choix des composants **K~1~, D~1~, K~2~** et
    > **D~2~**.

Le constructeur de composants **MITSUBISHI** a développé des modules
IGBT qui regroupent dans un même boîtier les composants **K~1~, D~1~,
K~2~, D~2~**.

Les caractéristiques principales des modules sont :

**V~CES~** : Tension collecteur-émetteur maximale.

**I~C~** : courant collecteur moyen maximal pour l'IGBT.

**I~E~ **: courant direct moyen pour la diode.

**I~CM~ **: courant crête maximal pour l'IGBT.

**I~EM~**~ ~: courant crête maximal pour la diode.

> **Pour tous les modules du tableau I~E~ = I~C~ et I~EM~ = I~CM~ =
> 2I~C~.**

+---------+-----------+-----------+-----------+-----------+-----------+
| **I~C~  | **100**   | **150**   | **200**   | **300**   | **400**   |
| (A)**   |           |           |           |           |           |
|         |           |           |           |           |           |
| *       |           |           |           |           |           |
| *V~CES~ |           |           |           |           |           |
| (V)**   |           |           |           |           |           |
+---------+-----------+-----------+-----------+-----------+-----------+
| **600** |           | CM1       | CM2       | CM3       | CM4       |
|         |           | 50-DY12NF | 00-DY12NF | 00-DY12NF | 00-DY12NF |
+---------+-----------+-----------+-----------+-----------+-----------+
| *       | CM1       | CM1       | CM2       | CM3       | CM4       |
| *1200** | 00-DY24NF | 50-DY24NF | 00-DY24NF | 00-DY24NF | 00-DY24NF |
+---------+-----------+-----------+-----------+-----------+-----------+

15. ** Choisir** le module qui convient à l'application étudiée, en
    > prenant un coefficient de sécurité de **1,1** sur les tensions et
    > de **1,2** sur les courants.

**DOCUMENT RÉPONSE N°1**

![](10-Électronique de Puissance/Cours/pandoc/media/image97.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**BOURREUSE ZCA 2000 LGV**

*([Source]{.underline} : ATS 2020)*

![](10-Électronique de Puissance/Cours/pandoc/media/image119.png){width="6.3in"
height="2.8666666666666667in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image120.png){width="6.3in"
height="3.8152777777777778in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image121.png){width="6.3in"
height="2.6590277777777778in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image122.png){width="7.268055555555556in"
height="3.783333333333333in"}

**BORNE SOLAIRE**

![](10-Électronique de Puissance/Cours/pandoc/media/image97.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source]{.underline} : ATS 2010)*

![](10-Électronique de Puissance/Cours/pandoc/media/image123.png){width="1.8916666666666666in"
height="1.8319444444444444in"}**Modélisation du moteur**

L\'objectif de cette partie est d\'établir le modèle électrique
équivalent du motoréducteur. Les valeurs de chaque paramètre seront
identifiées à partir de différents résultats d\'essais

Le système est équipé d\'un motoréducteur à courant continu. Celui-ci
est l\'association d\'un moteur à aimants permanents de tension nominale
12V et d\'un réducteur de rapport 1/60 (figure 6.a ci-contre)

L\'induit du moteur peut être représenté par son schéma électrique
équivalent, faisant intervenir sa résistance notée
![](10-Électronique de Puissance/Cours/pandoc/media/image124.wmf) son
inductance notée
![](10-Électronique de Puissance/Cours/pandoc/media/image125.wmf), et sa
force électromotrice notée
![](10-Électronique de Puissance/Cours/pandoc/media/image126.wmf).

**Q29** : Sachant que l\'on note
![](10-Électronique de Puissance/Cours/pandoc/media/image127.wmf) le
courant absorbé par le moteur et
![](10-Électronique de Puissance/Cours/pandoc/media/image128.wmf) sa
tension d\'alimentation, représenter le schéma équivalent de l\'induit
du moteur en utilisant une convention récepteur.

**6.1. Essai rotor bloqué**

On alimente le moteur avec une tension réduite et parfaitement continue,
tout en maintenant le rotor bloqué.

**Q30** : Montrer que cet essai permet de déterminer la valeur de
![](10-Électronique de Puissance/Cours/pandoc/media/image124.wmf), dont
on donnera l\'expression.

Lors d\'un essai rotor bloqué, on mesure
![](10-Électronique de Puissance/Cours/pandoc/media/image129.wmf) et
![](10-Électronique de Puissance/Cours/pandoc/media/image130.wmf).

**Q31** : Déduire de cet essai la valeur numérique de
![](10-Électronique de Puissance/Cours/pandoc/media/image124.wmf).

**6.2. Essai en charge**

La vitesse angulaire de l\'arbre moteur est notée
![](10-Électronique de Puissance/Cours/pandoc/media/image131.wmf).

**Q32** : En considérant le courant
![](10-Électronique de Puissance/Cours/pandoc/media/image127.wmf)
parfaitement continu, exprimer
![](10-Électronique de Puissance/Cours/pandoc/media/image132.wmf), la
constante de fem du moteur, en fonction de
![](10-Électronique de Puissance/Cours/pandoc/media/image133.wmf),
![](10-Électronique de Puissance/Cours/pandoc/media/image124.wmf),
![](10-Électronique de Puissance/Cours/pandoc/media/image127.wmf) et
![](10-Électronique de Puissance/Cours/pandoc/media/image134.wmf).

Lors d\'un essai en charge, on mesure :
![](10-Électronique de Puissance/Cours/pandoc/media/image135.wmf) ;
![](10-Électronique de Puissance/Cours/pandoc/media/image130.wmf)
(parfaitement continu) et
![](10-Électronique de Puissance/Cours/pandoc/media/image136.wmf)

**Q33** : Déduire de cet essai la valeur numérique de
![](10-Électronique de Puissance/Cours/pandoc/media/image132.wmf).

**6.3. Détermination de l\'inductance d\'induit**
![](10-Électronique de Puissance/Cours/pandoc/media/image125.wmf)

Le moteur est déconnecté du système pour être alimenté par le montage
suivant (figure 6.b)

![](10-Électronique de Puissance/Cours/pandoc/media/image137.wmf)

Figure 6.b : Essai du moteur avec un convertisseur électronique

La tension
![](10-Électronique de Puissance/Cours/pandoc/media/image138.wmf) est
constante et sa valeur est positive. Le courant
![](10-Électronique de Puissance/Cours/pandoc/media/image139.wmf) est
toujours strictement positif.

![](10-Électronique de Puissance/Cours/pandoc/media/image140.wmf) et
![](10-Électronique de Puissance/Cours/pandoc/media/image141.wmf) sont
des interrupteurs électroniques considérés parfaits. Le convertisseur
est commandé de façon périodique, de période
![](10-Électronique de Puissance/Cours/pandoc/media/image142.wmf)[,]{.smallcaps}
et présente deux phases différentes de fonctionnement :

\- Pendant la première phase, de durée
![](10-Électronique de Puissance/Cours/pandoc/media/image143.wmf) (avec
![](10-Électronique de Puissance/Cours/pandoc/media/image144.wmf)),
![](10-Électronique de Puissance/Cours/pandoc/media/image140.wmf) est
passant et
![](10-Électronique de Puissance/Cours/pandoc/media/image141.wmf)
bloqué.

\- Pendant la seconde phase, soit le reste du temps,
![](10-Électronique de Puissance/Cours/pandoc/media/image140.wmf) est
bloqué et
![](10-Électronique de Puissance/Cours/pandoc/media/image141.wmf)
passant.

**Q34** : Quel nom porte ce convertisseur électronique ? Comment
appelle-t-on la grandeur notée
![](10-Électronique de Puissance/Cours/pandoc/media/image145.wmf) ?

Le convertisseur est constitué d\'une diode et d\'un transistor.

**Q35** : Dessiner le schéma du montage en faisant apparaître
l\'emplacement de ces composants.

**Q36** : Parmi les sigles suivants, déterminer lesquels correspondent à
des technologies de transistor : GTI, MOS, IGBT, AOC et MMX. Quelles
sont les fréquences maximales de fonctionnement de chacun de ces
composants ? (donner uniquement un ordre de grandeur)

L\'étude est menée en régime permanent. La période
![](10-Électronique de Puissance/Cours/pandoc/media/image142.wmf) ayant
une valeur très inférieure à
![](10-Électronique de Puissance/Cours/pandoc/media/image146.wmf), la
résistance
![](10-Électronique de Puissance/Cours/pandoc/media/image124.wmf) sera
négligée pour les 6 questions suivantes.

**Q37** : Exprimer
![](10-Électronique de Puissance/Cours/pandoc/media/image147.wmf), la
valeur moyenne de la tension
![](10-Électronique de Puissance/Cours/pandoc/media/image148.wmf) en
fonction de
![](10-Électronique de Puissance/Cours/pandoc/media/image145.wmf) et
![](10-Électronique de Puissance/Cours/pandoc/media/image138.wmf).
Détailler le calcul.

**Q38** : Exprimer la fem du
moteur![](10-Électronique de Puissance/Cours/pandoc/media/image149.wmf),
en fonction de
![](10-Électronique de Puissance/Cours/pandoc/media/image145.wmf) et
![](10-Électronique de Puissance/Cours/pandoc/media/image138.wmf).
Préciser les hypothèses qui mènent à cette relation.

**Q39** : Donner l\'expression de
![](10-Électronique de Puissance/Cours/pandoc/media/image139.wmf)
lorsque
![](10-Électronique de Puissance/Cours/pandoc/media/image140.wmf) est
fermé. On notera
![](10-Électronique de Puissance/Cours/pandoc/media/image150.wmf) la
valeur du courant au début de cette phase de fonctionnement.

**Q40** : En déduire l\'expression de
![](10-Électronique de Puissance/Cours/pandoc/media/image151.wmf), en
fonction de
![](10-Électronique de Puissance/Cours/pandoc/media/image138.wmf),
![](10-Électronique de Puissance/Cours/pandoc/media/image142.wmf)[.]{.smallcaps}
![](10-Électronique de Puissance/Cours/pandoc/media/image145.wmf) et
![](10-Électronique de Puissance/Cours/pandoc/media/image152.wmf),
l\'ondulation de courant (définie par :
![](10-Électronique de Puissance/Cours/pandoc/media/image153.wmf))

La figure 6.c ci-dessous montre la tension appliquée au moteur et le
courant qu\' absorbe lors d\'un essai réalisé avec le convertisseur
électronique.

![](10-Électronique de Puissance/Cours/pandoc/media/image154.wmf)

Figure 6.c : Tension et courant du moteur avce le convertisseur
électronique

**Q41** : Déduire les valeurs numériques de
![](10-Électronique de Puissance/Cours/pandoc/media/image138.wmf)[,]{.smallcaps}
![](10-Électronique de Puissance/Cours/pandoc/media/image142.wmf)[,]{.smallcaps}
![](10-Électronique de Puissance/Cours/pandoc/media/image145.wmf) et
![](10-Électronique de Puissance/Cours/pandoc/media/image152.wmf)
correspondantes à cet essai.

**Q42** : En déduire la valeur numérique de
![](10-Électronique de Puissance/Cours/pandoc/media/image151.wmf)

![](10-Électronique de Puissance/Cours/pandoc/media/image97.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![C:\\Users\\Thomas\\Desktop\\chevres.png](10-Électronique de Puissance/Cours/pandoc/media/image155.png){width="0.8958333333333334in"
height="0.59375in"}**SYSTÈME AUTOMATIQUE DE DISTRIBUTION D'ALIMENTS POUR
CHÈVRES**

*([Source]{.underline} : Concours CCP TSI 2007)*

**Mise en situation**

Ce système est destiné à l'élevage (intensif) de chèvres pour la
production laitière. Il assure la distribution automatique des aliments
plusieurs fois par jour afin de favoriser leur assimilation par les
animaux. L'augmentation de la production laitière peut alors atteindre
20 %.

Ce système comporte un convoyeur mobile sur un rail IPN, convoyeur
constitué de deux éléments principaux :

> \- un chariot alimenté par batteries (déplacement sur le rail IPN),
>
> \- une trémie de stockage d'aliments permettant leur distribution
> (cette trémie compartimentée reçoit différents éléments : blé, maïs,
> ... compléments (minéraux où médicaments)).
>
> \- sous chaque compartiment, une bande transporteuse dont la vitesse
> est asservie à la vitesse de déplacement du chariot, assure la
> distribution du produit.

![](10-Électronique de Puissance/Cours/pandoc/media/image156.emf){width="4.3069444444444445in"
height="2.9270833333333335in"}**Description du fonctionnement**

Des systèmes de chargement amènent les aliments depuis des silos de
stockage vers les différents compartiments de la trémie ; dans le même
temps, les batteries sont mises en charge.

Au début de chaque cycle, le convoyeur se déplace jusqu'au point de
début de distribution ; par la suite, les aliments sont déposés en
continu à une vitesse de déplacement voisine de 30 m/min. Dans les
virages, la vitesse passe à environ 15 m/min. A la fin du cycle, le
convoyeur regagne le poste de chargement. L'étude porte sur le chariot
du convoyeur.

**Analyse fonctionnelle sommaire**

FP1 Déplacer la trémie le long du rail

FP2 Amener la trémie sous les systèmes d'alimentation

FC3 Permettre la connexion électrique au chargeur

FC4 Etre adapté au milieu environnant

**Description du chariot du convoyeur**

![](10-Électronique de Puissance/Cours/pandoc/media/image157.emf){width="3.9583333333333335in"
height="1.8229166666666667in"}Chaque tête, articulée autour d'un axe
vertical, comporte huit galets de guidage du chariot sur le rail. Les
batteries embarquées sur le chariot fournissent l'énergie électrique au
groupe motoréducteur à roue et vis.

Le groupe motoréducteur permet la propulsion du chariot par
l'intermédiaire de la roue motrice encastrée à l'extrémité de l'arbre de
sortie du réducteur. Ce sous-ensemble est monté sur un berceau articulé
soumis à l'action d'un ressort de poussée assurant le roulement sans
glissement de la roue motrice sur le rail.

![](10-Électronique de Puissance/Cours/pandoc/media/image158.emf){width="4.552083333333333in"
height="2.78125in"}

Les deux têtes sont conçues de manière identique.

Sur la tête libre, une roue de friction entraîne une lame d'impulsion
métallique au moyen d'un système pignons-chaîne. La vitesse du convoyeur
est mesurée à partir de la détection des passages de la lame d'impulsion
par un capteur inductif.

Le cahier des charges du système Capristar implique l'utilisation d'un
entraînement à vitesse variable. Le schéma de puissance d'entraînement
choisi de la machine à courant continu est le suivant :

![](10-Électronique de Puissance/Cours/pandoc/media/image159.emf){width="4.825694444444444in"
height="1.6354166666666667in"}

L représente une inductance de lissage mise en série avec la M.C.C.

Nous n'étudierons ni le redresseur, ni le module de freinage. La
première partie du sujet sera consacrée à l'identification de certains
paramètres de la machine à courant continu. Celle-ci sera suivie d'une
étude théorique du hacheur quatre quadrants.

Tout au long du sujet, la tension E, tension d'entrée du hacheur 4
quadrants, sera supposée continue et égale à 30 V. L'acronyme M.C.C.
sera utilisé tout au long du sujet pour désigner la machine à courant
continu.

Le réducteur associé à la MCC a un rapport de réduction de 1/21. Le
diamètre extérieur de la roue motrice est noté D~3~ = 100 mm.

![](10-Électronique de Puissance/Cours/pandoc/media/image160.emf){width="3.0729166666666665in"
height="1.5208333333333333in"}**Identification des paramètres de la
MCC**

La M.C.C. est à aimants permanents. Elle est modélisée dans cet exercice
par une force électromotrice e~M~(t) en série avec une résistance R~M~
et une inductance L~M~.

> FFigure 1 : Modèle équivalent de la M.C.C.

16. ** **Si on suppose que le courant dans le moteur est continu et égal
    à I, **donner** la relation liant ce courant et le couple
    électromagnétique C~EM~. En utilisant la courbe donnée en annexe,
    **déterminer** la valeur du coefficient de couple K de la machine à
    courant continu PM024 0922 utilisée dans cet entraînement.

17. Si on suppose que la tension aux bornes du moteur et la vitesse de
    rotation sont constantes et respectivement égales à U et à Ω,
    **donner** la relation entre la tension U et la vitesse de rotation
    Ω lorsque le courant dans le moteur est nul. **Déduire** de la
    courbe de l'annexe la tension d'alimentation du moteur qui a été
    utilisée pour faire les mesures.

18.  **Conclure** sur la relation entre la vitesse de déplacement du
    convoyeur V~c~ et la tension d'alimentation de la MCC \<u~s~\> si on
    considère la résistance R~m~ négligeable.

**Étude du hacheur 4 quadrants**

**[Critère :]{.underline}** Nous rappelons le cahier des charges :

\- vitesse de 30 m/mn, en ligne droite et horizontale,

\- ramenée progressivement à 50% de la vitesse nominale dans les
virages,

\- 2 sens (avant et arrière).

**[Hypothèses :]{.underline}**

-   Tous les interrupteurs sont considérés **idéaux** ;

-   La conduction est **continue** .

Chaque interrupteur est réalisé par un transistor I.G.B.T. en parallèle
avec une diode. La structure du hacheur quatre quadrants est donc la
suivante :

![](10-Électronique de Puissance/Cours/pandoc/media/image161.emf){width="4.354166666666667in"
height="1.7916666666666667in"}

Figure 2 : Schéma de principe de l'ensemble hacheur à I.G.B.T.-M.C.C.

19. Quels peuvent être le signe du courant de sortie moyen \<i(t)\> et
    celui de la tension moyenne \<u~s~(t)\> de sortie d'un hacheur
    quatre quadrants ? **Justifier** le choix du hacheur quatre
    quadrants pour le cahier des charges.

20. Pourquoi a-t-on placé un module de freinage en amont du hacheur
    (voir la présentation du sujet) ? Pour répondre à cette question,
    raisonner en terme de transfert d'énergie entre la source (le réseau
    électrique) et la charge (la M.C.C.).

Le hacheur quatre quadrants est commandé de la manière suivante : les
transistors T1-T4 d'une part et T2-T3 d'autre part sont commandés
simultanément à la fermeture et à l'ouverture. Le signal de commande est
périodique de période T et de fréquence f = 1/T = 20 kHz. Pour t compris
entre 0 et αT, T1-T4 sont fermés et T2-T3 sont ouverts. Sur le reste de
la période (t compris entre αT et T), T2-T3 sont fermés et T1-T4 sont
ouverts.

21. Représenter l'évolution de la tension de sortie u~s~(t) sur 3
    périodes avec α = 0,75 sur le document réponse n°1.

22. Le courant est supposé [continu]{.underline} dans la charge
    (i(t)=I). Indiquer sur le chronogramme de la question précédente
    (document réponse n°1) les composants qui conduisent à chaque
    instant de la période. Traiter le cas où le courant I dans la charge
    est positif et le cas où le courant est négatif.

23. Tracer, à partir de la question précédente et toujours sur le
    document réponse n°1, l'évolution du courant d'entrée i~e~(t) du
    hacheur lorsque le courant dans la machine est négatif et que le
    rapport cyclique α vaut 0,75. Le courant i(t)=I est toujours supposé
    continu. Quel est le signe de la valeur moyenne du courant i~e~(t) ?
    **En déduire** si, dans ce cas, la machine a un fonctionnement
    moteur ou générateur.

24. Que vaut la tension moyenne de sortie \<u~s~(t)\> lorsque α=0, α
    =0,5 et α =1 ? Déterminer la loi \<u~s~(t)\>=f(α) qui est une
    fonction linéaire.

25.  **Conclure** sur la plage de variation du rapport cyclique **α**
    pour obtenir les deux vitesses de déplacement du convoyeur énoncées
    dans le cahier des charges et pour les deux sens.

**DOCUMENT ANNEXE**

**Caractéristiques du moteur PM024 0922**

Ces caractéristiques sont tracées avec une tension d'alimentation
constante aux bornes du moteur.

![](10-Électronique de Puissance/Cours/pandoc/media/image162.emf){width="3.375in"
height="5.786135170603674in"}![](10-Électronique de Puissance/Cours/pandoc/media/image162.emf){width="3.375in"
height="2.6179341644794403in"}

**DOCUMENT RÉPONSE N°1**

![](10-Électronique de Puissance/Cours/pandoc/media/image163.emf){width="6.291666666666667in"
height="5.260416666666667in"}

1.  Donner les définitions mathématiques de la valeur moyenne V~moy~ et
    de la valeur efficace V~eff~ d'une tension v(t), de période T. ***(3
    points)***

2.  Donner les rapports cycliques puis les valeurs moyennes et efficaces
    des signaux suivants. ***(4 points)***

3.   Donner la caractéristique d'une diode idéale et indiquer les états
    passant et bloqué. ***(3 points)***

On étudie le montage ci-contre. **La conduction est dans tous les cas
continue, l'ondulation de courant est non négligeable. K est commandé
durant l'intervalle \[0 ; αT\].**

4.   Tracer les allures de u~D~, u~K~, i~L~, i~D~, i~K~. ***(6
    points)***

5.   En déduire la valeur de V~s~ en fonction de E et α. Justifier vos
    relations. ***(4 points)***

![](10-Électronique de Puissance/Cours/pandoc/media/image97.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![C:\\Users\\Thomas\\Desktop\\chevres.png](10-Électronique de Puissance/Cours/pandoc/media/image155.png){width="0.8958333333333334in"
height="0.59375in"} **SYSTÈME**

**AUTOMATIQUE DE DISTRIBUTION D'ALIMENTS POUR CHÈVRES**

*([Source]{.underline} : Concours CCP TSI 2007)*

**Mise en situation**

Ce système est destiné à l'élevage (intensif) de chèvres pour la
production laitière. Il assure la distribution automatique des aliments
plusieurs fois par jour afin de favoriser leur assimilation par les
animaux. L'augmentation de la production laitière peut alors atteindre
20 %.

Ce système comporte un convoyeur mobile sur un rail IPN, convoyeur
constitué de deux éléments principaux :

> \- un chariot alimenté par batteries (déplacement sur le rail IPN),
>
> \- une trémie de stockage d'aliments permettant leur distribution
> (cette trémie compartimentée reçoit différents éléments : blé, maïs,
> ... compléments (minéraux où médicaments)).
>
> \- sous chaque compartiment, une bande transporteuse dont la vitesse
> est asservie à la vitesse de déplacement du chariot, assure la
> distribution du produit.

![](10-Électronique de Puissance/Cours/pandoc/media/image156.emf){width="4.3069444444444445in"
height="2.9270833333333335in"}**Description du fonctionnement**

Des systèmes de chargement amènent les aliments depuis des silos de
stockage vers les différents compartiments de la trémie ; dans le même
temps, les batteries sont mises en charge.

Au début de chaque cycle, le convoyeur se déplace jusqu'au point de
début de distribution ; par la suite, les aliments sont déposés en
continu à une vitesse de déplacement voisine de 30 m/min. Dans les
virages, la vitesse passe à environ 15 m/min. A la fin du cycle, le
convoyeur regagne le poste de chargement. L'étude porte sur le chariot
du convoyeur.

![](10-Électronique de Puissance/Cours/pandoc/media/image168.emf){width="4.517716535433071e-3in"
height="2.840113735783027e-3in"}

**Analyse fonctionnelle sommaire**

FP1 Déplacer la trémie le long du rail

FP2 Amener la trémie sous les systèmes d'alimentation

FC3 Permettre la connexion électrique au chargeur

FC4 Etre adapté au milieu environnant

**Description du chariot du convoyeur**

![](10-Électronique de Puissance/Cours/pandoc/media/image157.emf){width="3.9583333333333335in"
height="1.8229166666666667in"}Chaque tête, articulée autour d'un axe
vertical, comporte huit galets de guidage du chariot sur le rail. Les
batteries embarquées sur le chariot fournissent l'énergie électrique au
groupe motoréducteur à roue et vis.

Le groupe motoréducteur permet la propulsion du chariot par
l'intermédiaire de la roue motrice encastrée à l'extrémité de l'arbre de
sortie du réducteur. Ce sous-ensemble est monté sur un berceau articulé
soumis à l'action d'un ressort de poussée assurant le roulement sans
glissement de la roue motrice sur le rail.

![](10-Électronique de Puissance/Cours/pandoc/media/image158.emf){width="4.552083333333333in"
height="2.78125in"}

Les deux têtes sont conçues de manière identique.

Sur la tête libre, une roue de friction entraîne une lame d'impulsion
métallique au moyen d'un système pignons-chaîne. La vitesse du convoyeur
est mesurée à partir de la détection des passages de la lame d'impulsion
par un capteur inductif.

Le cahier des charges du système Capristar implique l'utilisation d'un
entraînement à vitesse variable. Le schéma de puissance d'entraînement
choisi de la machine à courant continu est le suivant :

![](10-Électronique de Puissance/Cours/pandoc/media/image159.emf){width="4.825694444444444in"
height="1.6354166666666667in"}

L représente une inductance de lissage mise en série avec la M.C.C.

Nous n'étudierons ni le redresseur, ni le module de freinage. La
première partie du sujet sera consacrée à l'identification de certains
paramètres de la machine à courant continu. Celle-ci sera suivie d'une
étude théorique du hacheur quatre quadrants.

Tout au long du sujet, la tension E, tension d'entrée du hacheur 4
quadrants, sera supposée continue et égale à 30 V. L'acronyme M.C.C.
sera utilisé tout au long du sujet pour désigner la machine à courant
continu.

Le réducteur associé à la MCC a un rapport de réduction de 1/21. Le
diamètre extérieur de la roue motrice est noté D~3~ = 100 mm.

**Dimensionnement du convertisseur AC-DC**

Le convertisseur AC/DC utilisé est un redresseur de type Pont de Graëtz.

![](10-Électronique de Puissance/Cours/pandoc/media/image169.jpeg){width="7.456944444444445in"
height="1.7902777777777779in"}L'inductance L~f~ confère un caractère de
source de courant dynamique en sortie du redresseur, de courant constant
**I~ch~ = 60 A**. Le filtre de sortie L~f~-C~f~ permet d'obtenir la
valeur moyenne de la tension v~ch~(t) en sortie du filtre, soit E =
\<v~ch~\>.

![](10-Électronique de Puissance/Cours/pandoc/media/image170.wmf)

1.  **Tracer** les chronogrammes des signaux v~ch~(t), i~d1~(t),
    i~d3~(t), i~e~(t) et **indiquer** pour chaque phase de
    fonctionnement les semi-conducteurs en conduction.

2.  **Etablir** l'expression de la valeur moyenne de v~ch~(t) en
    fonction de la valeur efficace de la tension d'entrée V puis sa
    valeur numérique.

3.  **En déduire** la valeur de V permettant d'obtenir E=30V.

4.  **Indiquer** les différentes contraintes sur les diodes composants
    le redresseur (courant moyen, courant efficace et tension inverse
    maximale).

5.  **Calculer** la puissance active au niveau de la charge puis celle
    au niveau de l'entrée.

6.  **Calculer** la puissance active au niveau de la charge puis celle
    au niveau de l'entrée.

7.  **En déduire** le facteur de puissance vu du réseau.

8.  **Déterminer** la puissance apparente du transformateur.

9.  **Déterminer** la valeur du rapport de transformation m pour obtenir
    E=30V.

![](10-Électronique de Puissance/Cours/pandoc/media/image171.jpeg){width="4.267442038495188in"
height="2.5697681539807524in"}![](10-Électronique de Puissance/Cours/pandoc/media/image172.jpeg){width="4.302326115485564in"
height="2.581395450568679in"}![](10-Électronique de Puissance/Cours/pandoc/media/image173.jpeg){width="4.255814741907262in"
height="2.5581397637795273in"}![](10-Électronique de Puissance/Cours/pandoc/media/image174.jpeg){width="4.267442038495188in"
height="2.5697670603674543in"}

![](10-Électronique de Puissance/Cours/pandoc/media/image97.png){width="1.3555555555555556in"
height="0.3888888888888889in"}

![ASI](10-Électronique de Puissance/Cours/pandoc/media/image175.jpeg){width="0.7291666666666666in"
height="0.5520833333333334in"}**ALIMENTATION SANS INTERRUPTION**

**Mise en situation**

Une **Alimentation Sans Interruption** (ou *ASI*, ou en anglais
***UPS***, *Uninterruptible Power Supply*) est un dispositif de
l\'électronique de puissance qui permet de fournir à un système
électrique ou électronique une alimentation électrique stable et
dépourvue de coupure ou de microcoupure, quoi qu\'il se produise sur le
réseau électrique.

Une ASI est constituée de trois éléments principaux :

-   un ensemble « redresseur + convertisseur DC-DC », alimenté par le
    réseau EDF, qui transforme la tension alternative en tension
    continue ;

-   une batterie est maintenue chargée, qui, lors d'une coupure, fournit
    l'énergie nécessaire à l'alimentation de la charge par l'onduleur ;

```{=html}
<!-- -->
```
-   un onduleur (convertisseur DC/AC) qui transforme la tension continue
    en tension alternative pour alimenter les appareils connectés.

![](10-Électronique de Puissance/Cours/pandoc/media/image176.wmf)Le
filtre de sortie du redresseur L~s~-C~s~ permet d'obtenir la valeur
moyenne de la tension v~ch~(t) en sortie du filtre. L'ensemble est
alimenté par le réseau EDF :

*[Objectif de l'étude :]{.underline}* **Dimensionner** l'ensemble
« redresseur+filtre » de l'ASI :

-   **Déterminer** les contraintes sur les diodes et la puissance
    apparente nécessaire pour un transformateur d'isolement ;

-   **Calculer** l'inductance de filtrage permettant de limiter
    l'ondulation de courant à 5% du courant nominal.

On considère dans un premier temps l'ondulation de courant négligeable.
Le courant i~ch~ est donc constant : i~ch~= I~ch~ = 10 A. Ce courant
correspond au courant nominal délivré par le redresseur.

1.  **Tracer** les chronogrammes des signaux v~ch~, i~d1~, i~d3~, i~e~
    et **indiquer** pour chaque phase de fonctionnement les
    semi-conducteurs en conduction.

2.  **Etablir** l'expression de la valeur moyenne de v~ch~ en fonction
    de la valeur efficace de la tension d'entrée V puis sa valeur
    numérique.

3.  **Indiquer** les différentes contraintes sur les diodes composants
    le redresseur (courant moyen, courant efficace et tension inverse
    maximale).

4.  **Calculer** la puissance active au niveau de la charge puis celle
    au niveau de l'entrée.

5.  **En déduire** le facteur de puissance vu du réseau et la puissance
    apparente pour un transformateur d'isolement.

La tension v~ch~ n'étant pas constante, le courant i~ch~ n'est pas
constant et présente une ondulation de courant. On souhaite dimensionner
l'inductance L~s~ afin de limiter cette ondulation de courant à 5% du
courant nominal (I~ch~ = 10 A).

On supposera que la tension aux bornes du condensateur est constante et
que le courant i~ch~ est périodique. On propose alors d'utiliser le
développement en série de Fourier de la tension v~ch~ pour déterminer la
valeur de l'inductance L~s~. Le développement en série de Fourier de la
tension v~ch~ est :

![](10-Électronique de Puissance/Cours/pandoc/media/image177.wmf)

6.  **Calculer** la valeur numérique de l'inductance L~s~ permettant de
    limiter l'ondulation de courant à 5% du courant nominal (I~ch~
    =10 A) en se limitant au premier harmonique.

**DOCUMENT RÉPONSE**

1.  **Donner** les définitions mathématiques des puissances active,
    réactive et apparente ainsi que la définition du facteur de
    puissance. ***(4 points)***

Soit le convertisseur suivant :

2.  ** Tracer** l'allure de la tension de sortie v~ch~ et **indiquer**
    pour chaque phase de fonctionnement les semi-conducteurs en
    conduction. ***(3 points)***

3.   **Etablir** l'expression de la valeur moyenne de v~ch~ en fonction
    de la valeur efficace de la tension d'entrée V. ***(3 points)***

4.   **En déduire** la valeur du rapport de transformation m du
    transformateur permettant d'avoir \<v~ch~\> = 32V. ***(2 points)***

5.  ** Déterminer** le facteur de puissance vu du réseau et la puissance
    apparente nécessaire pour le transformateur si I~ch~ = 5 A.
    **Indiquer** vos hypothèses. ***(3 points)***

---
## Inventaire des images
10-Électronique de Puissance/Cours/pandoc/media/image1.png
10-Électronique de Puissance/Cours/pandoc/media/image10.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image100.png
10-Électronique de Puissance/Cours/pandoc/media/image101.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image102.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image103.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image104.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image105.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image106.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image107.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image108.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image109.png
10-Électronique de Puissance/Cours/pandoc/media/image11.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image110.png
10-Électronique de Puissance/Cours/pandoc/media/image111.png
10-Électronique de Puissance/Cours/pandoc/media/image112.png
10-Électronique de Puissance/Cours/pandoc/media/image113.png
10-Électronique de Puissance/Cours/pandoc/media/image114.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image115.png
10-Électronique de Puissance/Cours/pandoc/media/image116.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image117.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image118.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image119.png
10-Électronique de Puissance/Cours/pandoc/media/image12.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image120.png
10-Électronique de Puissance/Cours/pandoc/media/image121.png
10-Électronique de Puissance/Cours/pandoc/media/image122.png
10-Électronique de Puissance/Cours/pandoc/media/image123.png
10-Électronique de Puissance/Cours/pandoc/media/image124.wmf
10-Électronique de Puissance/Cours/pandoc/media/image125.wmf
10-Électronique de Puissance/Cours/pandoc/media/image126.wmf
10-Électronique de Puissance/Cours/pandoc/media/image127.wmf
10-Électronique de Puissance/Cours/pandoc/media/image128.wmf
10-Électronique de Puissance/Cours/pandoc/media/image129.wmf
10-Électronique de Puissance/Cours/pandoc/media/image13.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image130.wmf
10-Électronique de Puissance/Cours/pandoc/media/image131.wmf
10-Électronique de Puissance/Cours/pandoc/media/image132.wmf
10-Électronique de Puissance/Cours/pandoc/media/image133.wmf
10-Électronique de Puissance/Cours/pandoc/media/image134.wmf
10-Électronique de Puissance/Cours/pandoc/media/image135.wmf
10-Électronique de Puissance/Cours/pandoc/media/image136.wmf
10-Électronique de Puissance/Cours/pandoc/media/image137.wmf
10-Électronique de Puissance/Cours/pandoc/media/image138.wmf
10-Électronique de Puissance/Cours/pandoc/media/image139.wmf
10-Électronique de Puissance/Cours/pandoc/media/image14.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image140.wmf
10-Électronique de Puissance/Cours/pandoc/media/image141.wmf
10-Électronique de Puissance/Cours/pandoc/media/image142.wmf
10-Électronique de Puissance/Cours/pandoc/media/image143.wmf
10-Électronique de Puissance/Cours/pandoc/media/image144.wmf
10-Électronique de Puissance/Cours/pandoc/media/image145.wmf
10-Électronique de Puissance/Cours/pandoc/media/image146.wmf
10-Électronique de Puissance/Cours/pandoc/media/image147.wmf
10-Électronique de Puissance/Cours/pandoc/media/image148.wmf
10-Électronique de Puissance/Cours/pandoc/media/image149.wmf
10-Électronique de Puissance/Cours/pandoc/media/image15.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image150.wmf
10-Électronique de Puissance/Cours/pandoc/media/image151.wmf
10-Électronique de Puissance/Cours/pandoc/media/image152.wmf
10-Électronique de Puissance/Cours/pandoc/media/image153.wmf
10-Électronique de Puissance/Cours/pandoc/media/image154.wmf
10-Électronique de Puissance/Cours/pandoc/media/image155.png
10-Électronique de Puissance/Cours/pandoc/media/image156.emf
10-Électronique de Puissance/Cours/pandoc/media/image157.emf
10-Électronique de Puissance/Cours/pandoc/media/image158.emf
10-Électronique de Puissance/Cours/pandoc/media/image159.emf
10-Électronique de Puissance/Cours/pandoc/media/image16.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image160.emf
10-Électronique de Puissance/Cours/pandoc/media/image161.emf
10-Électronique de Puissance/Cours/pandoc/media/image162.emf
10-Électronique de Puissance/Cours/pandoc/media/image163.emf
10-Électronique de Puissance/Cours/pandoc/media/image168.emf
10-Électronique de Puissance/Cours/pandoc/media/image169.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image17.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image170.wmf
10-Électronique de Puissance/Cours/pandoc/media/image171.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image172.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image173.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image174.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image175.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image176.wmf
10-Électronique de Puissance/Cours/pandoc/media/image177.wmf
10-Électronique de Puissance/Cours/pandoc/media/image18.png
10-Électronique de Puissance/Cours/pandoc/media/image19.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image20.png
10-Électronique de Puissance/Cours/pandoc/media/image21.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image22.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image23.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image24.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image25.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image26.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image27.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image28.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image29.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image3.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image30.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image31.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image32.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image33.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image34.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image35.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image36.png
10-Électronique de Puissance/Cours/pandoc/media/image37.png
10-Électronique de Puissance/Cours/pandoc/media/image39.png
10-Électronique de Puissance/Cours/pandoc/media/image40.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image41.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image42.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image43.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image44.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image45.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image46.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image47.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image48.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image49.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image5.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image50.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image51.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image52.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image53.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image54.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image55.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image56.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image57.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image58.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image59.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image6.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image60.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image61.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image62.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image63.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image64.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image65.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image66.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image67.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image68.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image69.wmf
10-Électronique de Puissance/Cours/pandoc/media/image7.png
10-Électronique de Puissance/Cours/pandoc/media/image70.wmf
10-Électronique de Puissance/Cours/pandoc/media/image71.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image72.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image73.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image74.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image75.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image76.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image77.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image78.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image79.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image8.png
10-Électronique de Puissance/Cours/pandoc/media/image80.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image81.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image82.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image83.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image84.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image85.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image86.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image87.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image88.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image89.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image9.png
10-Électronique de Puissance/Cours/pandoc/media/image90.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image91.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image92.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image93.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image94.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image95.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image96.png
10-Électronique de Puissance/Cours/pandoc/media/image97.png
10-Électronique de Puissance/Cours/pandoc/media/image98.jpeg
10-Électronique de Puissance/Cours/pandoc/media/image99.jpeg
