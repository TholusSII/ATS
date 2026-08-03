![](14-Logique/Cours/pandoc/media/image1.png){width="8.494444444444444in"
height="4.148611111111111in"}

![](14-Logique/Cours/pandoc/media/image3.png){width="2.7333333333333334in"
height="2.65in"}

Cycle 8 : Analyser, Modéliser, Expérimenter et Résoudre les systèmes à
évènements discrets

**Logique combinatoire, logique séquentielle, graphes d'états,
communication réseau**

Thomas Lusseau

Lycée Robert Doisneau - ATS

# **Table des matières** {#table-des-matières .TOC-Heading .unnumbered}

[1. Généralités sur les systèmes logiques combinatoires
[4](#généralités-sur-les-systèmes-logiques-combinatoires)](#généralités-sur-les-systèmes-logiques-combinatoires)

[1.1. Symboles et notations
[4](#symboles-et-notations)](#symboles-et-notations)

[1.2. Démarche de synthèse d'un système combinatoire
[4](#démarche-de-synthèse-dun-système-combinatoire)](#démarche-de-synthèse-dun-système-combinatoire)

[1.3. Table de vérité [5](#table-de-vérité)](#table-de-vérité)

[1.4. Equation logique à partir de la table de vérité
[8](#equation-logique-à-partir-de-la-table-de-vérité)](#equation-logique-à-partir-de-la-table-de-vérité)

[1.5. Règles de l'algèbre de Boole
[8](#règles-de-lalgèbre-de-boole)](#règles-de-lalgèbre-de-boole)

[1.6. Modélisation et représentation des opérateurs logiques
[9](#modélisation-et-représentation-des-opérateurs-logiques)](#modélisation-et-représentation-des-opérateurs-logiques)

[1.7. Optimisation de l'équation logique
[10](#optimisation-de-léquation-logique)](#optimisation-de-léquation-logique)

[1.8. Synthèse de l'équation logique
[10](#synthèse-de-léquation-logique)](#synthèse-de-léquation-logique)

[1.9. Fonctions combinatoires particulières
[12](#fonctions-combinatoires-particulières)](#fonctions-combinatoires-particulières)

[1.10. Technologie des circuits intégrés
[18](#technologie-des-circuits-intégrés)](#technologie-des-circuits-intégrés)

[2. Systèmes à évènements Discrets (SED)
[22](#systèmes-à-évènements-discrets-sed)](#systèmes-à-évènements-discrets-sed)

[2.1. Exemple introductif
[22](#exemple-introductif)](#exemple-introductif)

[2.2. Systèmes séquentiels
[23](#systèmes-séquentiels)](#systèmes-séquentiels)

[2.3. Diagramme d'état (stm)
[24](#diagramme-détat-stm)](#diagramme-détat-stm)

[2.4. Démarche de modélisation du comportement séquentiel d'un système
par un graphe d'états
[25](#démarche-de-modélisation-du-comportement-séquentiel-dun-système-par-un-graphe-détats)](#démarche-de-modélisation-du-comportement-séquentiel-dun-système-par-un-graphe-détats)

[2.5. État et ses activités associées
[25](#état-et-ses-activités-associées)](#état-et-ses-activités-associées)

[2.6. Franchissement des transitions
[27](#franchissement-des-transitions)](#franchissement-des-transitions)

[2.7. Evènement [28](#evènement)](#evènement)

[2.8. Garde [28](#garde)](#garde)

[2.9. Equation logique [29](#equation-logique)](#equation-logique)

[2.10. Effet [29](#effet)](#effet)

[2.11. Pseudos-états [30](#pseudos-états)](#pseudos-états)

[2.12. État composite [33](#état-composite)](#état-composite)

[2.13. Historique d'un état composite
[34](#historique-dun-état-composite)](#historique-dun-état-composite)

[2.14. État composite orthogonal
[34](#état-composite-orthogonal)](#état-composite-orthogonal)

[3. Diagramme de séquence (sd)
[38](#diagramme-de-séquence-sd)](#diagramme-de-séquence-sd)

[3.1. Diagramme de séquence
[38](#diagramme-de-séquence)](#diagramme-de-séquence)

[4. CODEUR INCREMENTAL ET ABSOLU
[39](#codeur-incremental-et-absolu)](#codeur-incremental-et-absolu)

[4.1. Familles de capteurs
[39](#familles-de-capteurs)](#familles-de-capteurs)

[4.2. Vocabulaire de métrologie
[40](#vocabulaire-de-métrologie)](#vocabulaire-de-métrologie)

[4.3. Les codeurs [40](#les-codeurs)](#les-codeurs)

[5. RESEAUX ET BUS DE TERRAIN
[45](#reseaux-et-bus-de-terrain)](#reseaux-et-bus-de-terrain)

[5.1. Introduction sur les données
[45](#introduction-sur-les-données)](#introduction-sur-les-données)

[5.2. Qualité de service : QoS
[45](#qualité-de-service-qos)](#qualité-de-service-qos)

[5.3. Architecture des réseaux de communication
[45](#architecture-des-réseaux-de-communication)](#architecture-des-réseaux-de-communication)

[5.4. Couches du modèle OSI
[46](#couches-du-modèle-osi)](#couches-du-modèle-osi)

[5.5. Les supports de transmission
[47](#les-supports-de-transmission)](#les-supports-de-transmission)

[5.6. Multiplexage
[50](#principemultiplexagemultiplexage)](#principemultiplexagemultiplexage)

[5.7. Les erreurs de transmission
[51](#les-erreurs-de-transmission)](#les-erreurs-de-transmission)

[5.8. Topologie des réseaux
[54](#topologie-des-réseaux)](#topologie-des-réseaux)

[5.9. Types de liaisons des réseaux de communication
[55](#types-de-liaisons-des-réseaux-de-communication)](#types-de-liaisons-des-réseaux-de-communication)

[5.10. Architecture de la chaîne de transmission
[56](#architecture-de-la-chaîne-de-transmission)](#architecture-de-la-chaîne-de-transmission)

[5.11. Caractéristiques de la transmission
[57](#caractéristiques-de-la-transmission)](#caractéristiques-de-la-transmission)

[5.1. Protocoles des réseaux de communication
[58](#protocoles-des-réseaux-de-communication)](#protocoles-des-réseaux-de-communication)

[6. Sources [71](#sources)](#sources)

[7. Exercices du chapitre [72](#_Toc130196631)](#_Toc130196631)

## Généralités sur les systèmes logiques combinatoires

### Symboles et notations

![](14-Logique/Cours/pandoc/media/image5.jpeg){width="3.1069444444444443in"
height="1.5722222222222222in"}Un **système combinatoire** est un système
**logique** (ou booléen) traitant des informations sous **forme logique
(ou booléenne)** et dont les **états des sorties sont
[exclusivement]{.underline} définis à partir des entrées**.

On peut alors représenter un système combinatoire par un bloc entre les
variables d'entrées et de sortie. Les sorties sont reliées aux entrées
par une **fonction logique ne dépendant que des entrées.**

Les entrées et sorties d'un tel système sont des **variables logiques
(ou binaires, ou booléennes)** qui ne peuvent prendre que **deux valeurs
0 ou 1** permettant de représenter l'état d'un objet :

-   ouvert ou fermé;

-   vrai ou faux;

-   tension de 5V ou de 0V;

-   tout ou rien;

-   présent ou absent, ...

**L'état logique « 1 »** informe que l'entrée a été actionnée. **L'état
logique « 0 »** informe que l'entrée n'a pas été actionnée.

### Démarche de synthèse d'un système combinatoire

A partir du cahier des charges d'un système qui nous incite à mettre en
œuvre un **système combinatoire**, on obtient un chronogramme, une
**table de vérité** ou une **équation logique** décrivant le
fonctionnement des sorties en fonction des entrées.

Pour arriver jusqu'à la **synthèse** (solution câblée -ou programmée -),
on doit passer par différentes opérations :

-   La **table de vérité** ou **l'équation logique** : elle traduit le
    > cahier des charges.

-   L**'optimisation** : elle a pour but de réduire les **opérateurs
    > logiques** pour réaliser l'équation logique.

-   ![](14-Logique/Cours/pandoc/media/image6.jpeg){width="2.1055555555555556in"
    > height="1.0798611111111112in"} La **synthèse** : c'est la
    > réalisation matérielle du circuit réalisant le système
    > combinatoire.

On peut alors représenter les différentes phases de la synthèse d'une
fonction logique combinatoire par le schéma suivant :

+-----------------------------------------------------------------------+
| **Table de vérité en code binaire :**                                 |
|                                                                       |
| ![](14                                                                |
| -Logique/Cours/pandoc/media/image7.jpeg){width="2.3780883639545056in" |
| height="3.4069761592300964in"}                                        |
+=======================================================================+
+-----------------------------------------------------------------------+

### Table de vérité

Le fonctionnement d'un système combinatoire est décrit par une **table
de vérité**. Elle permet de faire **correspondre l'état des sorties en
fonction de l'état des entrées** et cela pour **toutes les combinaisons
possibles des entrées**.

Pour un système combinatoire de **n entrées** il y aura **2^n^
combinaisons (ou cas)** possibles (3 entrées 8 combinaisons, 4 entrées
16 combinaisons, ...).

**L'équation logique de la sortie** peut alors être déterminée en
recherchant toutes les **combinaisons d'entrées pour lesquelles la
sortie vaut 1.**

![](14-Logique/Cours/pandoc/media/image8.png){width="3.71875in"
height="1.5166666666666666in"}

+--------+-------------------------------------------------------------+
| > ![]  | ![C:\                                                       |
| (14-Lo | \Users\\Thomas\\Desktop\\moto_store_ext2.jpg](14-Logique/Co |
| gique/ | urs/pandoc/media/image11.jpeg){width="1.4590277777777778in" |
| Cours/ | height="1.113888888888889in"}**Store SOMFY**                |
| pandoc |                                                             |
| /media | L\'entreprise SOMFY propose toute une gamme de matériels    |
| /image | \"grand public\" dont le store SOMFY fait partie.           |
| 10.png |                                                             |
| ){widt | Ce store est composé de cinq éléments :                     |
| h="0.6 |                                                             |
| 262696 | -   Un store qui protège l\'utilisateur des rayons du       |
| 850393 |     soleil.                                                 |
| 701in" |                                                             |
| >      | -   Un opérateur tubulaire capable d\'enrouler ou de        |
| height |     dérouler le store.                                      |
| ="0.65 |                                                             |
| 083333 | -   Un capteur de vent qui détecte la présence de vent.     |
| 333333 |                                                             |
| 34in"} | -   Un capteur solaire qui détecte la présence de soleil.   |
|        |                                                             |
|        | -   Un automatisme vent / soleil qui permet à               |
|        |     l\'utilisateur de commander en mode manuel ou en mode   |
|        |     automatique le store.                                   |
|        |                                                             |
|        | ![sdf](14-Logique/Co                                        |
|        | urs/pandoc/media/image12.jpeg){width="3.2736111111111112in" |
|        | height="1.8055555555555556in"}                              |
|        |                                                             |
|        | Par mesure de sécurité (pour l\'utilisateur comme pour le   |
|        | store), [l\'action du vent est toujours prioritaire sur     |
|        | l\'action du soleil]{.underline} et ce, aussi bien en mode  |
|        | automatique qu\'en mode manuel. Le diagramme sagittal       |
|        | ci-dessous, présente les différents constituants de ce      |
|        | système.                                                    |
|        |                                                             |
|        | [Cahier des charges :]{.underline}                          |
|        |                                                             |
|        | Si le vent devient supérieur à un seuil préréglé, le module |
|        | de commande monte le store et le laisse en position haute.  |
|        | Cette fonction est prioritaire sur toutes les autres pour   |
|        | des raisons de sécurité.                                    |
|        |                                                             |
|        | En l'absence de vent, l'utilisateur peut commander la       |
|        | montée ou la descente du store par des inverseurs. Cette    |
|        | fonction manuelle est prioritaire sur la fonction soleil    |
|        | qui, lorsque la luminosité devient supérieure au seuil      |
|        | préréglé, provoque la descente du store.                    |
|        |                                                             |
|        | Le schéma structurel est donné ci-dessous.                  |
|        |                                                             |
|        | ![sdf](14-Logique/C                                         |
|        | ours/pandoc/media/image13.jpeg){width="5.625025153105862in" |
|        | height="4.416666666666667in"}                               |
|        |                                                             |
|        | **En vous aidant du cahier des charges, et de la            |
|        | présentation du système, lister les entrées et sorties du   |
|        | système.**                                                  |
|        |                                                             |
|        | **Etablir la table de vérité du système effectuant le       |
|        | traitement numérique des informations (fonction FP4).**     |
|        |                                                             |
|        | **Déterminer l'équation logique de la sortie CD.**          |
+========+=============================================================+
+--------+-------------------------------------------------------------+

**Etat logique indifférent « X » :**

Pour **certaines combinaisons d'entrées**, il peut arriver qu'on ne
puisse **pas déterminer l'état de la sortie logique car la combinaison
des entrées ne peut pas se produire ou qu'elle ne nous intéresse pas.**

Dans ces cas-là, il existe un **état logique appelé indifférent, noté «
X » ou « - » qui peut prendre les valeurs « 0 » ou « 1 ».**

### Equation logique à partir de la table de vérité

**L'équation logique d'une sortie** peut se déduire à partir de la table
de vérité traduisant le cahier des charges. Il suffit alors de lister
les combinaisons des entrées (reliées par un ET logique) pour lesquelles
la sortie est activée (« 1 » logique) et de les séparer par un OU
logique.

Soit un système combinatoire à deux entrées (a et b) et une sortie (S).
La sortie est activée si une action est faite sur b [ET]{.underline} pas
sur a [OU]{.underline} si une action est faite sur a et sur b. Ceci se
traduit par l'équation logique : $S = b.\overline{a} + b.a$

Pour réaliser la synthèse de cette équation logique, il faut définir
deux **opérateurs logiques,** On les nomme **BOOLEEN**. A l'opérateur
**ET** est associé l'opérateur mathématique « **.** ». A l'opérateur
**OU** est associé l'opérateur mathématique «** +** ». **Et nous
obtenons l'appellation « ALGEBRE DE BOOLE »**

### Règles de l'algèbre de Boole

![](14-Logique/Cours/pandoc/media/image14.png){width="6.267361111111111in"
height="3.0972222222222223in"}![](14-Logique/Cours/pandoc/media/image15.wmf){width="1.1645833333333333in"
height="0.3472222222222222in"}![](14-Logique/Cours/pandoc/media/image16.wmf){width="0.8243055555555555in"
height="0.3888888888888889in"}

![](14-Logique/Cours/pandoc/media/image17.wmf)![](14-Logique/Cours/pandoc/media/image18.wmf){width="0.5in"
height="0.22152777777777777in"}

![](14-Logique/Cours/pandoc/media/image19.wmf)![](14-Logique/Cours/pandoc/media/image20.wmf){width="0.7555555555555555in"
height="0.225in"}

![](14-Logique/Cours/pandoc/media/image21.wmf){width="0.325in"
height="0.24722222222222223in"}

![](14-Logique/Cours/pandoc/media/image22.jpeg){width="5.38125in"
height="0.6493055555555556in"}

### Modélisation et représentation des opérateurs logiques

On utilise différentes représentations pour les opérateurs logiques :

-   **Les symboles (normes IEC --européenne -- et ANSI -- américaine
    --);**

-   Les **schémas logiques à contact** (équivalent électrique)

-   **L'équation logique** (ou booléenne);

-   La **table de vérité** (état des sorties en fonction des entrées);

-   Les **chronogrammes** (évolution de la variable logique dans le
    temps.

+--------------------+--------------+--------------+--------+----------+
| **Schéma           | **Symbole**  | **Table de   | *      | **Eq     |
| électrique**       |              | vérité**     | *Nom** | uation** |
+====================+==============+==============+========+==========+
| **a L**            |              |   ---- ----  | **NON  | **L=a**  |
|                    |              |   a    L     | (      |          |
|                    |              |              | NOT)** |          |
|                    |              |   0    1     |        |          |
|                    |              |              |        |          |
|                    |              |   1    0     |        |          |
|                    |              |   ---- ----  |        |          |
+--------------------+--------------+--------------+--------+----------+
| **a L**            |              |   ---- ----  | **OUI  | **L=a**  |
|                    |              |   a    L     | (      |          |
|                    |              |              | YES)** |          |
|                    |              |   0    0     |        |          |
|                    |              |              |        |          |
|                    |              |   1    1     |        |          |
|                    |              |   ---- ----  |        |          |
+--------------------+--------------+--------------+--------+----------+
| **a b L**          |              |              | **ET   | *        |
|                    |              |  ------- --- | (      | *L=a.b** |
|                    |              | ---- ------- | AND)** |          |
|                    |              |   **a**   *  |        |          |
|                    |              | *b**   **L** |        |          |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *0**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *1**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *0**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *1**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |  ------- --- |        |          |
|                    |              | ---- ------- |        |          |
+--------------------+--------------+--------------+--------+----------+
| **a L**            |              |              | *      | **L      |
|                    |              |  ------- --- | *NONET | =a       |
| **b**              |              | ---- ------- | (N     | .b=a+b** |
|                    |              |   **a**   *  | AND)** |          |
|                    |              | *b**   **L** |        |          |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *0**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *1**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *0**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *1**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |  ------- --- |        |          |
|                    |              | ---- ------- |        |          |
+--------------------+--------------+--------------+--------+----------+
| **a L**            | ![](14-Log   |              | **OU** | *        |
|                    | ique/Cours/p |  ------- --- |        | *L=a+b** |
| **b**              | andoc/media/ | ---- ------- | **     |          |
|                    | image23.wmf) |   **a**   *  | (OR)** |          |
|                    |              | *b**   **L** |        |          |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *0**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *1**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *0**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *1**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |  ------- --- |        |          |
|                    |              | ---- ------- |        |          |
+--------------------+--------------+--------------+--------+----------+
| a b L              | ![](14-Log   |              | *      | **L      |
|                    | ique/Cours/p |  ------- --- | *NONOU | =a       |
|                    | andoc/media/ | ---- ------- | (      | +b=a.b** |
|                    | image24.wmf) |   **a**   *  | NOR)** |          |
|                    |              | *b**   **L** |        |          |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *0**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *1**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *0**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *1**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |  ------- --- |        |          |
|                    |              | ---- ------- |        |          |
+--------------------+--------------+--------------+--------+----------+
| **a b L**          | ![](14-Log   |              | **OU   | **L      |
|                    | ique/Cours/p |  ------- --- | excl   | =ab+ab** |
|                    | andoc/media/ | ---- ------- | usif** |          |
|                    | image25.wmf) |   **a**   *  |        | **=a**   |
|                    |              | *b**   **L** | **(    | ![]      |
|                    |              |              | XOR)** | (14-Logi |
|                    |              |   **0**   *  |        | que/Cour |
|                    |              | *0**   **0** |        | s/pandoc |
|                    |              |              |        | /media/i |
|                    |              |   **0**   *  |        | mage26.w |
|                    |              | *1**   **1** |        | mf)**b** |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *0**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *1**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |  ------- --- |        |          |
|                    |              | ---- ------- |        |          |
+--------------------+--------------+--------------+--------+----------+
| **a a**            | ![](14-Log   |              | **NON  | **L=(a** |
|                    | ique/Cours/p |  ------- --- | OU     | ![](     |
| **b b L**          | andoc/media/ | ---- ------- | ex     | 14-Logiq |
|                    | image27.wmf) |   **a**   *  | clsuif | ue/Cours |
|                    |              | *b**   **L** | (N     | /pandoc/ |
|                    |              |              | XOR)** | media/im |
|                    |              |   **0**   *  |        | age28.wm |
|                    |              | *0**   **1** |        | f)**b)** |
|                    |              |              |        |          |
|                    |              |   **0**   *  |        |          |
|                    |              | *1**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *0**   **0** |        |          |
|                    |              |              |        |          |
|                    |              |   **1**   *  |        |          |
|                    |              | *1**   **1** |        |          |
|                    |              |              |        |          |
|                    |              |  ------- --- |        |          |
|                    |              | ---- ------- |        |          |
+--------------------+--------------+--------------+--------+----------+

### Optimisation de l'équation logique

Plus d'opérateurs logiques seront présents dans l'équation logique plus
la complexité de réalisation sera grande.

On cherche donc à optimiser au maximum l'équation logique via
différentes méthodes

-   Par l'algèbre de Boole;

-   Par les tableaux de Karnaugh;

-   Avec un logiciel.

Une des premières méthodes de simplification est la **simplification
algébrique**.

Pour cela, on utilise les théorèmes de l\'algèbre booléenne vu
précédemment. La méthode est la suivante :

-   On transforme l'expression pour obtenir une somme de produits (ou
    **forme disjonctive**);

-   On analyse de chaque produit pour trouver les variables communes
    pour les mettre en facteur et les éliminer.

$$L = a.\overline{b}.c + a.\overline{b}.\overline{c} + a.b.c = a.\overline{b}\underset{= 1}{\overset{\left( c + \overline{c} \right)}{︸}} + a.b.c = a.\overline{b} + a.b.c = a.\underset{\overline{b} + c}{\overset{\left( \overline{b} + b.c \right)}{︸}} = \boxed{a.\overline{b} + a.c}$$

### Synthèse de l'équation logique

La **synthèse de l'équation logique** consiste en la réalisation «
matérielle » de la fonction logique. On a principalement 3 synthèses
différentes suivant la complexité de l'équation logique :

-   La synthèse directe;

-   La synthèse avec portes NAND et NOR;

-   La synthèse par multiplexeur;

-   La synthèse par circuits programmables.

##### Synthèse directe {#synthèse-directe .unnumbered}

La synthèse directe consiste à **utiliser directement tous les
opérateurs** présents dans l'équation logique. On obtient alors ce qu'on
appelle un **logigramme**.

**Règle de construction :** Partir de la sortie puis rechercher
l'opérateur logique qui sépare l'équation.

> Equation logique de départ : S = ( a + b.c ).d
>
> ![](14-Logique/Cours/pandoc/media/image29.jpeg){width="3.0465113735783027in"
> height="0.951347331583552in"}
>
> Pour une réalisation « câblée », il faut alors disposer de tous les
> circuits logiques.

Plus on aura de diversité et plus le circuit sera complexe. **Elle n'est
utilisée que dans des cas simples**.

+--------+-------------------------------------------------------------+
| > ![]  | **Equations logiques**                                      |
| (14-Lo |                                                             |
| gique/ | **Donner les équations des sorties S1, S2 et S3.**          |
| Cours/ |                                                             |
| pandoc | ![exo1](14-Logique/C                                        |
| /media | ours/pandoc/media/image30.png){width="3.2083333333333335in" |
| /image | height="3.2762576552930884in"}                              |
| 10.png |                                                             |
| ){widt |                                                             |
| h="0.6 |                                                             |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

##### Synthèse par circuits programmables {#synthèse-par-circuits-programmables .unnumbered}

Les circuits logiques programmables appelés PLD se répartissent en
différentes familles et sont des solutions de plus en plus utilisées. On
distingue principalement deux types de familles :

-   Les **circuits ASIC** (Application Specific Integrated Circuit),
    sont des circuits qui ne sont pas reconfigurables et qui sont prévus
    pour des applications spécifiques (téléphone portable,...);

-   Les **circuits PLD** (Programmable Logic Device), sont des circuits
    avec ds associations de blocs combinatoires configurables par
    l'utilisateur. Il y a alors plusieurs familles suivant les besoins.

    -   Les **FPGA** (Field Programmable Gate Array),

    -   Les **PAL** (Programmable Array Logic),

    -   Les **GAL** (Generic Array Logic),

    -   Les **CPLD** (Programmable Logic Device)

### Fonctions combinatoires particulières

##### Codeur, Décodeur et Transcodeur {#codeur-décodeur-et-transcodeur .unnumbered}

Dans un **système combinatoire** complexe, on utilisera un « cerveau »
ou calculateur qui permet de traiter les informations d'entrées et de
définir les sorties en conséquence.

Par exemple, si on souhaite réaliser le circuit d'affichage d'un code
tapé au clavier, on aura la structure suivante.

![](14-Logique/Cours/pandoc/media/image31.jpeg){width="2.779070428696413in"
height="1.4096741032370954in"}

Deux interfaces, appelées **codeur et décodeur**, ont été ajoutées afin
de permettre la « **communication** » entre le clavier, le calculateur
et l'afficheur. En effet, chacun à un code propre qui n'est pas
forcément compris par tout le monde. Le **codeur** permet de
**transcrire un code quelconque en des informations binaires
exploitables par le calculateur**. C'est un circuit combinatoire
comportant n entrées (une seule entrée est active à la fois) et p
sorties.

![](14-Logique/Cours/pandoc/media/image32.jpeg){width="3.197674978127734in"
height="1.3472167541557305in"}

Le **décodeur** permet de réaliser l'opération inverse du codeur. Il
permet de transcrire des informations binaires fournies par le
calculateur en un code quelconque.

C'est un circuit combinatoire comportant n entrées et p = 2^n^ sorties.

A une combinaison d'entrées, il ne correspond [qu'une seule sortie
active.]{.underline}

![](14-Logique/Cours/pandoc/media/image33.jpeg){width="2.978597987751531in"
height="1.3255818022747157in"}

Un **transcodeur** est un circuit combinatoire comportant n entrées et p
sorties. C'est un **« convertisseur de code ».** Le plus connu est le
transcodeur Gray/Binaire ou le BCD/7 segments pour l'affichage.
L'afficheur 7 segments permet, à partir de 7 LEDs d'afficher tous les
chiffres décimaux comme sur la figure suivante.

![](14-Logique/Cours/pandoc/media/image34.jpeg){width="2.5232567804024497in"
height="1.1911318897637795in"}

**[Table de vérité du décodeur 7 segments :]{.underline}**

  ------- --- --------------- ---------- ---------- ---------- -- ----- --------------- ------- ------- ------- ------- ------- ------- -------
              **Sorties du                                              **Segments de                                                   
              Calculateur**                                             l'afficheur**                                                   

  **N**       **a~3~**        **a~2~**   **a~1~**   **a~0~**                            **a**   **b**   **c**   **d**   **e**   **f**   **g**

  **0**       0               0          0          0                                   1       1       1       1       1       1       0

  **1**       0               0          0          1                                   0       1       1       0       0       0       0

  **2**       0               0          1          0                                   1       1       0       1       1       0       1

  **3**       0               0          1          1                                   1       1       1       1       0       0       1

  **4**       0               1          0          0                                   0       1       1       0       0       1       1

  **5**       0               1          0          1                                   1       0       1       1       0       1       1

  **6**       0               1          1          0                                   1       0       1       1       1       1       1

  **7**       0               1          1          1                                   1       1       1       0       0       0       0

  **8**       1               0          0          0                                   1       1       1       1       1       1       1

  **9**       1               0          0          1                                   1       1       1       1       0       1       1
  ------- --- --------------- ---------- ---------- ---------- -- ----- --------------- ------- ------- ------- ------- ------- ------- -------

**L'équation logique de la sortie** peut alors être déterminée en
recherchant toutes les **combinaisons d'entrées pour lesquelles la
sortie vaut 1.**

> Le **code Gray (ou binaire réfléchi)**, également appelé binaire
> réfléchi, est un code **binaire** qui présente la particularité
> qu\'**un seul bit change d\'état entre deux combinaisons
> successives**.
>
> Ce qui permet d\'éviter des erreurs de lecture.

+-----------------------------------+-----------------------------------+
| ##### Code bi                     | ##### C                           |
| naire {#code-binaire .unnumbered} | ode Gray {#code-gray .unnumbered} |
|                                   |                                   |
|   ----------                      |   ----------                      |
| --------------------------------- | --------------------------------- |
|                                   |                                   |
| $$2^{2}$$   $$2^{1}$$   $$2^{0}$$ | $$2^{2}$$   $$2^{1}$$   $$2^{0}$$ |
|   ------- --                      |   ------- --                      |
| --------- ----------- ----------- | --------- ----------- ----------- |
|                                   |                                   |
| 0       0           0           0 | 0       0           0           0 |
|                                   |                                   |
|                                   |                                   |
| 1       0           0           1 | 1       0           0           1 |
|                                   |                                   |
|                                   |                                   |
| 2       0           1           0 | 2       0           1           1 |
|                                   |                                   |
|                                   |                                   |
| 3       0           1           1 | 3       0           1           0 |
|                                   |                                   |
|                                   |                                   |
| 4       1           0           0 | 4       1           1           0 |
|                                   |                                   |
|                                   |                                   |
| 5       1           0           1 | 5       1           1           1 |
|                                   |                                   |
|                                   |                                   |
| 6       1           1           0 | 6       1           0           1 |
|                                   |                                   |
|                                   |                                   |
| 7       1           1           1 | 7       1           0           0 |
|   ----------                      |   ----------                      |
| --------------------------------- | --------------------------------- |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | ![conditionneuse](14-Logique/Co                             |
| (14-Lo | urs/pandoc/media/image35.jpeg){width="1.1354166666666667in" |
| gique/ | height="0.9583333333333334in"}**Conditionneuse de comprimés |
| Cours/ | pharmaceutiques**                                           |
| pandoc |                                                             |
| /media | Une unité de conditionnement de médicaments permet de       |
| /image | mettre en flacon une quantité préréglée de comprimés de     |
| 10.png | façon automatique.                                          |
| ){widt |                                                             |
| h="0.6 | Ces comprimés sont déversés sur un plateau tournant         |
| 262696 | entraîné par une machine à courant continu. Le débit des    |
| 850393 | comprimés sortant de la trémie est contrôlé par une trappe. |
| 701in" | Le débit est réglable de façon à maintenir un nombre de     |
| >      | comprimés suffisant sur la sole par ouverture ou fermeture  |
| height | d'une trappe (par l'intermédiaire de 2 boutons poussoirs à  |
| ="0.65 | bascule). La trappe est actionnée par un vérin électrique   |
| 083333 | VE.                                                         |
| 333333 |                                                             |
| 34in"} | ![api](1                                                    |
|        | 4-Logique/Cours/pandoc/media/image36.jpeg){width="3.4375in" |
|        | height="1.65625in"}                                         |
|        |                                                             |
|        | Le conditionnement de comprimés délivre une information     |
|        | numérique sur un mot de 8 bits, soit un octet A = \[a7 a6   |
|        | a5 ... a0\] correspondant à la position souhaitée du vérin. |
|        |                                                             |
|        | La course totale du vérin est de 50 mm. Le pas de la vis    |
|        | est de 1mm.                                                 |
|        |                                                             |
|        | Le code GRAY fourni par le codeur présente l'inconvénient   |
|        | de ne pas permettre de manière simple les opérations        |
|        | arithmétiques de base et notamment la comparaison entre les |
|        | nombres qui le composent. On envisage de concevoir un       |
|        | circuit combinatoire (appelé transcodeur) permettant de     |
|        | passer du code GRAY au code binaire naturel, et ainsi de    |
|        | fournir une information directement exploitable par         |
|        | l'automate.                                                 |
|        |                                                             |
|        | ![qsd](14-Logique/C                                         |
|        | ours/pandoc/media/image37.jpeg){width="5.333333333333333in" |
|        | height="0.8958333333333334in"}                              |
|        |                                                             |
|        | **Déterminer la résolution du codeur rotatif 8 bits en      |
|        | degrés puis en mm.**                                        |
|        |                                                             |
|        | **Etablir les équations logiques des sorties B1 à B4 du     |
|        | transcodeur en fonction des entrées G1 à G4.**              |
|        |                                                             |
|        | **En déduire l'expression logique liant le bit Bi en        |
|        | fonction du bit Bi+1 et du bit Gi pour n bits.**            |
|        |                                                             |
|        | **Dessiner le logigramme complet du transcodeur 4 bits en   |
|        | utilisant les opérateurs logiques élémentaires notamment    |
|        | l'opérateur OU EXCLUSIF.**                                  |
+========+=============================================================+
+--------+-------------------------------------------------------------+

##### Multiplexeur / Démultiplexeur {#multiplexeur-démultiplexeur .unnumbered}

Un **multiplexeur** est un « aiguilleur » d'information. On sélectionne
l'information à envoyer en sortie à partir **d'entrées de sélections**.
Un multiplexeur est donc un système combinatoire comportant N entrées de
données et une sortie qui permet de transmettre les informations
présentent en entrée suivant les n entrées de sélection (N = 2^n^).

Il existe souvent une **entrée dite de « validation** **»** (ou enable
en anglais) qui permet de valider le fonctionnement du Mux. Si le Mux
n'est pas validé, la sortie sera toujours nulle. Cette entrée est
généralement active à l'état bas (d'où la présence du petit triangle sur
l'entrée).

![](14-Logique/Cours/pandoc/media/image38.jpeg){width="2.860465879265092in"
height="1.9131692913385827in"}![](14-Logique/Cours/pandoc/media/image39.jpeg){width="2.813953412073491in"
height="1.3367410323709537in"}

Par exemple, pour un MUX 8 vers 1, il suffit d'avoir 3 entrées de
sélections. La table de vérité du fonctionnement est la suivante.

![](14-Logique/Cours/pandoc/media/image40.jpeg){width="2.099024496937883in"
height="2.662790901137358in"}

Un **démultiplexeur** réalise l'opération inverse d'un multiplexeur en
aiguillant une donnée d'entrée vers une des 2n sorties choisie par les n
entrées de sélection. Les applications des multiplexeurs /
démultiplexeurs sont diverses  : synthèse d'une fonction logique,
multiplexage d'un système combinatoire (afin de limiter la complexité et
les coûts, conversion série/parallèle et la génération de fonctions
(GBF).

![](14-Logique/Cours/pandoc/media/image41.jpeg){width="3.182916666666667in"
height="1.5348840769903762in"}![](14-Logique/Cours/pandoc/media/image42.jpeg){width="2.534884076990376in"
height="1.2075437445319335in"}

**Synthèse à base de multiplexeur :**

Le **multiplexeur** permet de « découper » la table de vérité et ainsi
de **sélectionner en sortie l'une des 2n entrées**. Il suffit alors de
mettre les entrées comme sélecteur et de « recopier » la table de vérité
sur les entrées de données.

![](14-Logique/Cours/pandoc/media/image43.jpeg){width="4.430232939632546in"
height="1.9857874015748032in"}

### Technologie des circuits intégrés

##### Familles technologiques {#familles-technologiques .unnumbered}

Pour synthétiser une fonction logique, on peut utiliser des **circuits
intégrés logiques** qui sont classés suivant leur **technologie de
fabrication** **(TTL, CMOS, ECL,...).** Les différents critères
(électriques et temporels) permettant de comparer les performances d'une
famille technologique sont :

-   Les **tensions d'alimentations** ;

-   Les **niveaux de tensions associés aux niveaux logiques** (pour
    quelle tension on aura un « 0 » ou un « 1 »);

-   Les **courants maximums d'entrée et de sortie** ;

-   La **puissance maximale consommée** ;

-   Le **temps de propagation** et les temps de montée et de descente.

Chaque technologie aura alors ses points forts et ses points faibles et
on choisira la technologie suivant l'application souhaitée.

##### Niveaux de tension {#niveaux-de-tension .unnumbered}

![](14-Logique/Cours/pandoc/media/image44.jpeg){width="3.081395450568679in"
height="1.8553149606299213in"}Les circuits logiques sont alimentés entre
deux tensions : **0V (ou VSS ou GND)** et **+Vcc (ou VDD).**

Dans les circuits intégrés logiques, on a une tension qui est associée à
chaque niveau logique (0 ou 1).

Le **« 1 »** correspond alors au potentiel le plus élevé (**H comme
High**) et le **« 0 »** comme le potentiel le plus bas (**L comme
Low**).

##### ![](14-Logique/Cours/pandoc/media/image45.jpeg){width="2.9944444444444445in" height="1.7777777777777777in"}Temps de propagation {#temps-de-propagation .unnumbered}

Le **temps de propagation d'une porte** est le **temps (ou retard) que
met l'information à apparaître en sortie**. Ce temps de propagation est
**dû à deux choses** : le **temps de propagation à travers le circuit
électronique** et la **durée nécessaire à l'évolution de la sortie**.
Par exemple on peut voir les temps de propagations d'une porte NON :

##### Sortance (fan out) {#sortance-fan-out .unnumbered}

La sortance est le **nombre d'entrées que peut piloter une porte
logique**. Dans le cas où la sortance n'est pas suffisante, on utilise
des circuits « bufferisés » qui permettent d'augmenter le courant
disponible en sortie (on a un montage Darlington sur les transistors de
sortie). Les circuits à sortie bufférisé sont repérés par le symbole
amplification 

##### Consommation {#consommation .unnumbered}

La puissance consommée dépend du courant total consommé (nombre de
portes utilisées) pour la technologie TTL mais aussi de la fréquence
pour la technologie CMOS. Pour des fréquences élevées, la puissance
consommée par les technologies TTL est aussi fonction de la fréquence.

##### Résistances de rappel (Pull-up, Pull-down) {#résistances-de-rappel-pull-up-pull-down .unnumbered}

En électronique numérique il faut faire extrêmement attention aux
**tensions appliquées aux entrées des portes logiques**.

![](14-Logique/Cours/pandoc/media/image46.jpeg){width="2.7093022747156605in"
height="1.8836100174978128in"}En effet, si les **potentiels ne sont pas
imposés sur toutes les entrées** (entrée non connectée par exemple), son
état est **indéterminé et peut prendre la valeur « 0 » ou « 1 » suivant
le gabarit de tension**.

Pour fixer les potentiels, on ajoute ce qu'on appelle les **résistances
de tirages ou pull-up**. Une résistance de tirage permet d'imposer un
potentiel sur une entrée logique. On parle de pull-up, lorsque la
résistance est reliée au +Vcc et de pull-down lorsqu'elle est reliée à
la masse.

Dans l'exemple du pull up ci-dessus, la résistance permet d'avoir un
potentiel de référence (+Vcc), lorsque le bouton poussoir « a » n'est
pas actionné. Elle évite ainsi d'avoir des potentiels flottants.

##### Sortie standard {#sortie-standard .unnumbered}

![](14-Logique/Cours/pandoc/media/image47.jpeg){width="2.785416666666667in"
height="1.6722222222222223in"} La sortie de portes logiques
«** standards** » peut-être vue comme deux transistors T1 et T2 qui sont
tour à tour bloqué ou saturé de manière complémentaire. On a alors deux
états possibles en sortie « 0 » ou « 1 », comme le montre les figures
suivantes.

Le principal inconvénient de la sortie standard est **qu'on ne peut pas
relier plusieurs portes sur un même bus** car on risque d'avoir un
conflit (deux circuits peuvent très bien imposer un niveau différent
alors qu'un seul est utilisé).

![](14-Logique/Cours/pandoc/media/image48.jpeg){width="2.697674978127734in"
height="1.7918503937007875in"}![](14-Logique/Cours/pandoc/media/image49.jpeg){width="2.9302329396325457in"
height="1.63666447944007in"}

![](14-Logique/Cours/pandoc/media/image50.jpeg){width="2.344828302712161in"
height="1.5313167104111987in"}

##### Sortie « collecteur ouvert » {#sortie-collecteur-ouvert .unnumbered}

Les portes ayant une sortie à **collecteur ouvert** ont une sortie avec
un seul transistor, dont le collecteur est relié à la sortie (collecteur
« ouvert »). Cette sortie est représentée sur les figures ci-dessous.

Cette structure n'a aucun problème pour imposer le niveau bas ou « 0 »,
mais **ne peut imposer le niveau haut** ou « 1 ». Pour « l'aider » à
imposer ce niveau haut, il **faut alors une résistance de pull-up**, qui
n'interférera pas sur le niveau bas comme le montre la figure suivante.

![](14-Logique/Cours/pandoc/media/image51.jpeg){width="2.6567443132108486in"
height="1.9534886264216973in"}![](14-Logique/Cours/pandoc/media/image52.jpeg){width="3.2908628608923887in"
height="1.8305752405949256in"}

##### Sortie « 3 états » {#sortie-3-états .unnumbered}

Les circuits logiques à sortie **« 3 états »** utilisent comme la sortie
standard deux transistors. Cependant, il existe dans ces circuits une
**entrée supplémentaire dite de validation (ou Enable en anglais)** qui
permet de « déconnecter » le circuit d'un bus et ainsi d'éviter les
conflits.

![](14-Logique/Cours/pandoc/media/image53.jpeg){width="3.465517279090114in"
height="1.8403488626421698in"}

En effet, lorsque l'entrée de validation n'est pas active, on retrouve
le fonctionnement standard avec deux états possibles « 0 » ou « 1 ».

Cependant, lorsqu'on n'utilise plus le circuit, on peut le désactiver
via l'entrée de validation. Les deux transistors sont alors bloqués et
on n'impose aucun niveau logique en sortie comme l'illustre les figures
suivantes.

![](14-Logique/Cours/pandoc/media/image54.jpeg){width="3.9069772528433946in"
height="2.080638670166229in"}

On définit alors un troisième état qui est l'état **Haute Impédance ou
HiZ**. On peut alors connecter plusieurs circuits sur un même bus sans
risque de conflit s'ils sont actifs chacun leur tour. Ces sorties sont
notamment utilisées pour les mémoires (bus d'adresses et bus de
données).

## Systèmes à évènements Discrets (SED)

### Exemple introductif

On souhaite réaliser la commande d'un moteur d'ouverture du hayon **M+**
à partir des différentes entrées logiques du système :

-   **ph = 1** si le coffre est en position haute (coffre ouvert);

-   **t0 = 1**; si une pression est exercée sur l'une des touches
    > d'ouverture automatique ;

Le chronogramme du fonctionnement souhaité est le suivant : Lorsqu'on
appuie sur la commande d'ouverture (t0) le hayon s'ouvre (M+) jusqu'à
atteindre la position haute (ph).

Pour trouver la table de vérité de ce système il suffit d'étudier les
différents cas du chronogramme. Un système combinatoire de 2 entrées a 4
possibilités.

![](14-Logique/Cours/pandoc/media/image55.jpeg){width="6.837156605424322in"
height="1.675129046369204in"}

Pour trouver la table de vérité de ce système il suffit alors de
rajouter une entrée qui représente l'état présent du moteur M+.

![](14-Logique/Cours/pandoc/media/image56.jpeg){width="2.876615266841645in"
height="2.0295133420822395in"}

$${M^{+}}_{n + 1} = \overline{to}.\overline{ph}.{M^{+}}_{n} + to.\overline{ph}.\overline{{M^{+}}_{n}} + to.\overline{ph}.{M^{+}}_{n} = to.\overline{ph} + \overline{to}.\overline{ph}.{M^{+}}_{n} = to.\overline{ph} + \overline{ph}.{M^{+}}_{n}$$

L'équation logique de la sortie est alors :
${M^{+}}_{n + 1} = to.\overline{ph} + \overline{ph}.{M^{+}}_{n} = \overline{ph}.\left( to + {M^{+}}_{n} \right)$

Cette équation logique peut être représentée par un logigramme.

![](14-Logique/Cours/pandoc/media/image57.jpeg){width="2.369024496937883in"
height="1.1770308398950131in"}

La différence par rapport aux logigrammes de circuits combinatoires est
le **retour d'état** de la sortie du système comme entrée. Pour cela, il
faut **mémoriser l'état du système**.

### Systèmes séquentiels

Nous avons vu les systèmes combinatoires pour lesquels **à un état des
entrées correspondait un unique état des sorties**. Il existait alors
une table de correspondance entre entrées et sorties qu'on appelait
**table de vérité.** Dans les systèmes séquentiels, les états des
sorties ne dépendent plus uniquement des entrées du système **mais aussi
des événements antérieurs.**

**Une même combinaison des entrées, à un certain instant, ne donne pas
toujours la même sortie** mais dépend aussi de l'état précédent de cette
dernière. C'est l'« **effet mémoire** » qui utilise la notion **d'état
interne du système.**

![](14-Logique/Cours/pandoc/media/image58.jpeg){width="3.4159722222222224in"
height="1.5902777777777777in"}Ce dernier sera stable, tant qu'aucune
combinaison des entrées n'aura fait changer d'état. **Les états des
sorties dépendent donc des états des entrées mais aussi de** **l'état
interne antérieur du système**. On peut représenter un système
séquentiel à partir d'un système combinatoire à partir du schéma suivant
où on mémorise l'état interne du système.

Pour décrire les systèmes séquentiels, on n'utilise donc plus la table
de vérité mais ce qu'on appelle une **table des états** où on prend en
compte l'état interne du système qui est ajouté comme variable d'entrée.
Pour trouver **l'état futur** (Q~n+1~), on utilise **l'état présent** du
système (Q~n~).

![](14-Logique/Cours/pandoc/media/image59.jpeg){width="2.4347222222222222in"
height="0.8361111111111111in"}

Un système est dit à logique séquentielle, lorsque la ou les sorties
**dépendent de la combinaison des entrées mais aussi de l\'état
précédent des sorties et de la variable temps.**

[Explication :]{.underline} Une même cause (même combinaison des entrées
e~1~, e~2~, ..., e ~n~) peut produire des effets différents (états
différents des sorties S~1~, S~2~, ..., S ~p~). L\'effet peut persister
si la cause disparaît. S~i~= f(e~1~,e~2~,...,e ~n~; S~1~,S~2~,\...,S~p~;
t)

**Comment décrire le comportement séquentiel d'un système ?**

La description du comportement d'un système séquentiel peut être
réalisée notamment par :

-   L'outil graphe d'états ;

-   L'outil algorithme (ou algorigramme).

Il s'agit essentiellement d'outils graphiques permettant de modéliser le
comportement séquentiel en termes de déroulement d'actions temporelles.
Ces outils sont, à la base, des outils de modélisation du comportement
séquentiel, mais peuvent aussi servir à la programmation des composants
réalisant la fonction Traiter de la chaîne d'information
(microcontrôleur, microprocesseur, automate programmable, ...).

Les variables d'entrées de la fonction Traiter sont alors les grandeurs
fournies par la fonction Acquérir (capteurs, ...) et les variables de
sorties sont les informations destinées à la fonction Communiquer, qui
permettront d'élaborer les ordres à la chaîne d'énergie

Quel que soit l'outil adopté pour modéliser le comportement séquentiel
d'un système, il existe souvent plusieurs « solutions ». « La solution »
la plus simple et celle qui respecte l'ensemble des contraintes est donc
à privilégier. C'est le rôle de l'ingénieur de choisir le « bon » outil,
et la « meilleure solution ».

Les systèmes à événements discrets (SED) se définissent par opposition
aux systèmes continus dont l\'évolution est continue dans le temps et
peut être décrite par des équations différentielles. Dans un SED, le
passage d'un état à un autre est déclenché par des événements ponctuels.
Contrairement aux systèmes continus où les informations traitées sont de
nature analogique, les systèmes à événements discrets manipulent des
informations logiques ou numériques.

### Diagramme d'état (stm)

##### Présentation {#présentation .unnumbered}

En langage SysML, un diagramme d'état (stm) est nécessairement associé à
un bloc du diagramme de définitions de blocs (bdd) ou du diagramme de
blocs internes (ibd). Ce bloc peut être le système, un sous-système ou
un composant.

> Le **diagramme d'état** représente le **comportement** du système et
> ses changements d'état en fonction des interactions.

+--------+-------------------------------------------------------------+
| > ![]  | ![](14-Logique/Co                                           |
| (14-Lo | urs/pandoc/media/image60.jpeg){width="1.8645833333333333in" |
| gique/ | height="1.6534722222222222in"}**Vidéo Surveillance**        |
| Cours/ |                                                             |
| pandoc | Le diagramme ci-dessous décrit le fonctionnement d'un       |
| /media | système de vidéo-surveillance.                              |
| /image |                                                             |
| 10.png | On y trouve :                                               |
| ){widt |                                                             |
| h="0.6 | -   5 états : *Repos* ,  *Initialisation*,                  |
| 262696 |     *Diagnostic*, *Arrêt* et *Fonctionnement* ;             |
| 850393 |                                                             |
| 701in" | -   ![](14-Logique/C                                        |
| >      | ours/pandoc/media/image61.png){width="5.7868055555555555in" |
| height |     height="2.68125in"}des transitions entre les états,     |
| ="0.65 |     représentées par des flèches, et qui précisent sous     |
| 083333 |     quelles conditions le système passe d\'un état à un     |
| 333333 |     autre.                                                  |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

On peut remarquer, avec cet exemple, que la représentation du
**comportement** est en générale fonctionnelle dans les diagrammes
d'état. Aucune information technique sur la manière dont sont transmises
les informations, ni sur la façon dont sont réalisées les activités,
n'est précisée.

### D**émarche** de modélisation du comportement séquentiel d'un système par un graphe d'états 

Etape 1 : Définir la frontière du système et recenser les variables
d'entrées et de sorties ;

Etape 2 : Recenser, nommer et tracer les états du système ;

Etape 3 : Tracer les transitions entre les états en fonction du
comportement séquentiel souhaité ou observé ;

Etape 4 : Définir les conditions (et évènements) associées à chaque
transition et les actions associées à chaque état ;

Etape 5 : Vérifier les propriétés de complétude et de non contradiction
pour le graphe d'états complet.

### État et ses activités associées

Un **état (représenté par un rectangle aux bords arrondis)** modélise
une **phase du fonctionnement** du système.

-   Pendant cette période, l\'état est dit **actif** et le système
    accomplit :

> \- une simple **activité** ;
>
> \- OU une séquence d'activités ;
>
> \- OU est **en attente**.

-   En dehors de cette période, l\'état est dit **inactif**.

Par définition :

-   il n'y a qu'**un seul état actif** à **chaque instant** ;

-   un état possède un **titre unique** dans le diagramme.

Le lancement des activités à l\'intérieur de l\'état actif est organisé
selon des mots réservés :

  ---------------------------------------------------------------------------------------------------------------------------------------------
  ***entry***   Activité ayant une **fin**, elle ne peut **pas**   ![](14-Logique/Cours/pandoc/media/image62.png){width="1.100317147856518in"
                être **interrompue**. Elle est **exécutée** lors   height="0.8277613735783027in"}
                de l'**activation de l'état**. Exemple :           
                allumer/éteindre un voyant, incrémenter un         
                compteur,...                                       
  ------------- -------------------------------------------------- ----------------------------------------------------------------------------
  ***do***      Activités **interruptibles**. Elles sont           
                **exécutées** dans l\'**ordre** de leur            
                **écriture**, à partir de l\'instant où l'activité 
                associée à *entry* est terminée.                   

  ***exit***    Activité ayant une **fin**, elle ne peut **pas**   
                être **interrompue**. Elle est **exécutée** lors   
                de la **désactivation de l'état**, à l'instant de  
                la sortie de l'état.                               
  ---------------------------------------------------------------------------------------------------------------------------------------------

> Remarques :
>
> les trois comportements ***entry***, ***do*** et ***exit*** ne peuvent
> être **utilisés qu'une seule fois par état**, mais il est également
> possible de n'en **utiliser qu'une partie** (seulement *entry* par
> exemple) ;
>
> si **aucun mot** réservé n\'est utilisé, cela correspond à un
> ***do** *;
>
> un **état vide** (sans activité) indique un **état d'attente** ;

+--------+-------------------------------------------------------------+
| > ![]  | ![](14-Logique/Co                                           |
| (14-Lo | urs/pandoc/media/image63.jpeg){width="1.0104166666666667in" |
| gique/ | height="1.0104166666666667in"}**Lave-linge**                |
| Cours/ |                                                             |
| pandoc | **Lister les états d'un graphe d'états qui permet de        |
| /media | contrôler un lave-linge.**                                  |
| /image |                                                             |
| 10.png | Un cycle complet d'un lave-linge est composé de 5 états :   |
| ){widt |                                                             |
| h="0.6 | -   Prélavage ;                                             |
| 262696 |                                                             |
| 850393 | -   Lavage ;                                                |
| 701in" |                                                             |
| >      | -   Rinçage ;                                               |
| height |                                                             |
| ="0.65 | -   Essorage ;                                              |
| 083333 |                                                             |
| 333333 | -   Arrêt.                                                  |
| 34in"} |                                                             |
|        | > ![](14-Logique/Cours/pandoc/media/image64.png)            |
+========+=============================================================+
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | ![Vecteur Stock feu rouge \| Adobe                          |
| (14-Lo | Stock](14-Logique/Co                                        |
| gique/ | urs/pandoc/media/image65.jpeg){width="0.4895833333333333in" |
| Cours/ | height="1.2569772528433947in"}**Feu Rouge**                 |
| pandoc |                                                             |
| /media | **Lister les états d'un graphe d'états qui permet de        |
| /image | contrôler un feu rouge.**                                   |
| 10.png |                                                             |
| ){widt |                                                             |
| h="0.6 |                                                             |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

### Franchissement des transitions

Une fois recensés tous les états d'un système, il faut ensuite en
modéliser ses évolutions en identifiant les conditions de changement
d'état.

> Une **transition** (représentée graphiquement par une flèche) modélise
> la possibilité d\'un **passage** instantané d\'un **état** vers **un
> autre**.
>
> On appelle **état source** l\'état de départ d\'une transition, et
> **état cible** l\'état d\'arrivée d'une transition

La **transition** :

-   est **instantanée** ;

-   n\'est évaluée que si l\'état source est actif.

-   Son **franchissement** est **conditionné** par des **événements
    déclencheurs** et des **conditions de garde**.

Ces événements et conditions de franchissement ainsi que l'éventuel
effet associé à la transition sont indiqués le long de la flèche qui la
symbolise suivant la notation :

+---------------------------------+--------------------------------+---+
| > **événement \[garde\] /       |                                |   |
| > effet**                       |                                |   |
+=================================+================================+===+
| ![](14-Logiq                    | Une transition réflexive       |   |
| ue/Cours/pandoc/media/image66.p | entraîne une sortie de l\'état |   |
| ng){width="1.866068460192476in" | puis un retour dans ce même    |   |
| height="0.7797462817147857in"}  | état, avec appel des           |   |
|                                 | éventuelles activités *exit*   |   |
|                                 | et *entry*.                    |   |
+---------------------------------+--------------------------------+---+

### Evènement

> Un **événement** correspond au changement d'état d'une variable
> observée. Il est **daté** dans le temps et il est **traité
> instantanément** lors de son **occurrence** (front montant ou
> descendant) (apparition).

+--------------------------------------------+-------------------------+
| Exemples :                                 |                         |
|                                            |                         |
| Appui sur un bouton, arrivée en fin de     |                         |
| course d'un mécanisme, dépassement d'une   |                         |
| valeur seuil...                            |                         |
+============================================+=========================+
+--------------------------------------------+-------------------------+

> Un **événement** n'est **jamais mémorisé** et est donc perdu s'il ne
> mène à aucune évolution du diagramme d'état.

Il est possible d'utiliser des variables internes (compteurs ou horloge)
pour spécifier un événement déclencheur :

  -----------------------------------------------------------------------
  *when*    Se déclenche lors du changement d'état d'une valeur interne
            au diagramme d'état. Il permet par exemple d'utiliser un
            compteur : *when(N=3)*.
  --------- -------------------------------------------------------------
  *after    se déclenche après une durée T passé dans l'état d'amont. Il
  (T)*      permet de réaliser une temporisation.

  *at (D)*  se déclenche à la date D dans un référentiel de temps dont
            l'origine correspond généralement au démarrage du
            fonctionnement du système.
  -----------------------------------------------------------------------

> Si une **transition** n'a **pas d'événement** spécifié,
> l'**événement** déclencheur **implicite** est la fin des
> **d'activités** liées au ***do** de l'**état source***.

### Garde

> La **garde** est une **condition de franchissement** de la transition.
> C'est une condition logique évaluée à l'instant de l'évènement
> déclencheur.

Contrairement à l'événement qui, lui, est localisé dans le temps, la
garde traduit une condition qui dure dans le temps et qui doit
persister.

![Résultat de recherche d\'images pour \"bouton arret
urgence\"](14-Logique/Cours/pandoc/media/image67.jpeg){width="0.911334208223972in"
height="1.0173917322834645in"}

+--------------------------------------------+-------------------------+
| **Exemple** :                              |                         |
|                                            |                         |
| Pour un bouton :                           |                         |
|                                            |                         |
| \- l'événement est associé à l'instant où  |                         |
| le bouton est enfoncé ;                    |                         |
|                                            |                         |
| \- la garde est associé à l'état du        |                         |
| bouton : enfoncé ou non.                   |                         |
+============================================+=========================+
+--------------------------------------------+-------------------------+

> Si une **garde** n'est **pas présente** le long d'une transition, elle
> est **considérée** comme toujours **vraie**.

La syntaxe d'une condition de garde vérifiant si l'état TOTO est actif
est : \[in TOTO\].

### Equation logique

  ----------------------------------------------------------------------------------------------------
  La condition            ![](14-Logique/Cours/pandoc/media/image68.png){width="4.289864391951006in"
  **logique** évaluée     height="1.5300043744531933in"}
  pour la garde peut-être 
  le résultat d'une       
  combinaison de l'état   
  de plusieurs grandeurs  
  logiques, on parle      
  alors du résultat d'une 
  équation logique.       
  ----------------------- ----------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------

Dans ce type d'équation, on utilise des opérateurs logiques selon les
règles de l'algèbre de BOOLE.

Ces 4 opérateurs logiques sont : **OUI**, **NON**, **OU**, **ET**. Ils
permettent de réaliser les opérations de base :

+------------------------+--------------+----------------+------------+
| Entrées : **a** et     |              |                |            |
| **b** résultat : **S** |              |                |            |
+========================+==============+================+============+
| **OUI**                | notée        | *qui donne à S | ![](14     |
|                        | ![](14-Log   | la valeur 1 si | -Logique/C |
|                        | ique/Cours/p | et seulement   | ours/pando |
|                        | andoc/media/ | si*            | c/media/im |
|                        | image69.wmf) |                | age70.wmf) |
+------------------------+--------------+----------------+------------+
| **NON**                | notée        |                | ![](14     |
|                        | ![](14-Log   |                | -Logique/C |
| (appelé aussi          | ique/Cours/p |                | ours/pando |
| « complément »)        | andoc/media/ |                | c/media/im |
|                        | image71.wmf) |                | age72.wmf) |
+------------------------+--------------+----------------+------------+
| **OU**                 | notée        |                | ![](14-L   |
|                        | ![](14-Log   |                | ogique/Cou |
| (appelé aussi « somme  | ique/Cours/p |                | rs/pandoc/ |
| logique »)             | andoc/media/ |                | media/imag |
|                        | image73.wmf) |                | e74.wmf)OU |
|                        |              |                | ![](14     |
|                        |              |                | -Logique/C |
|                        |              |                | ours/pando |
|                        |              |                | c/media/im |
|                        |              |                | age75.wmf) |
+------------------------+--------------+----------------+------------+
| **ET**                 | notée        |                | ![](14-L   |
|                        | ![](14-Log   |                | ogique/Cou |
| (appelé aussi          | ique/Cours/p |                | rs/pandoc/ |
| « produit logique »)   | andoc/media/ |                | media/imag |
|                        | image76.wmf) |                | e77.wmf)ET |
|                        |              |                | ![](14     |
|                        |              |                | -Logique/C |
|                        |              |                | ours/pando |
|                        |              |                | c/media/im |
|                        |              |                | age78.wmf) |
+------------------------+--------------+----------------+------------+

> L'opérateur logique **OU** correspond à un montage en **parallèle**.
>
> L'opérateur logique **ET** correspond à un montage en **série**.

### Effet

> Un **effet** est une **activité** accomplie lorsque la **transition**
> est **franchie**.

Les activités associées aux effets sont considérées instantanées, par
exemple on peut définir une variable /N=1

> Une transition peut ne pas avoir d'effet associé.

+--------+-------------------------------------------------------------+
| > ![]  | ![Vecteur Stock feu rouge \| Adobe                          |
| (14-Lo | Stock](14-Logique/Co                                        |
| gique/ | urs/pandoc/media/image65.jpeg){width="0.4895833333333333in" |
| Cours/ | height="1.2569772528433947in"}**Feu Rouge**                 |
| pandoc |                                                             |
| /media | **Réaliser le graphe d'états du feu rouge.**                |
| /image |                                                             |
| 10.png |                                                             |
| ){widt |                                                             |
| h="0.6 |                                                             |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

###  {#section .unnumbered}

### Pseudos-états

> Un **pseudo-état** est un état ne pouvant **pas** avoir
> d'**activité**.

Ils servent essentiellement comme éléments de liaison et pour indiquer
l'état initial ou l'arrêt du diagramme d'état.

##### Pseudo-état initial ![](14-Logique/Cours/pandoc/media/image79.png){width="0.3851126421697288in" height="0.12133748906386702in"} {#pseudo-état-initial .unnumbered}

> **Unique** et **obligatoire**, il est activé au **lancement** de la
> machine à états et marque le début de l'exécution du diagramme d'état.
> Il n'a aucune transition entrante.

##### Pseudo-état final ![](14-Logique/Cours/pandoc/media/image80.png){width="0.29581146106736655in" height="0.15776574803149607in"} {#pseudo-état-final .unnumbered}

> **Optionnel**, il signe la **fin de l'exécution du diagramme d'état**.
> Il n'a aucune transition sortante.

##### Pseudo-état jonction ![](14-Logique/Cours/pandoc/media/image81.png){width="0.13821850393700788in" height="0.13821850393700788in"} {#pseudo-état-jonction .unnumbered}

> Utilisé pour **regrouper** (« factoriser ») des **conditions de
> franchissement de transition**, en particulier des gardes communes à
> un événement.

Il permet de partager des segments de transition et d'aboutir à une
notation plus lisible des chemins alternatifs.

> L'**évaluation** des **conditions de garde** en **aval** du
> pseudo-état est réalisée **avant** qu'il ne soit atteint.

+--------+-------------------------------------------------------------+
| > ![]  | **Pseudo état jonction**                                    |
| (14-Lo |                                                             |
| gique/ | +---------------------------+---------------------------+   |
| Cours/ | | ![](14-Logi               | ![](14-Logique/Cours/pan  |   |
| pandoc | | que/Cours/pandoc/media/im | doc/media/image83.png){wi |   |
| /media | | age82.png){width="2.77in" | dth="2.717169728783902in" |   |
| /image | | heigh                     | heigh                     |   |
| 10.png | | t="1.3779472878390202in"} | t="1.3243055555555556in"} |   |
| ){widt | |                           |                           |   |
| h="0.6 | | Exemple sans pseudo-état  | Exemple avec pseudo-état  |   |
| 262696 | | jonction                  | jonction                  |   |
| 850393 | +===========================+===========================+   |
| 701in" | +---------------------------+---------------------------+   |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

##### Pseudo-état décision ![](14-Logique/Cours/pandoc/media/image84.png){width="0.3077066929133858in" height="0.15178258967629046in"} {#pseudo-état-décision .unnumbered}

> Utilisé pour une sélection ou une convergence de séquences exclusives.
>
> L'**évaluation** des **conditions de garde** en **aval** du
> pseudo-état est réalisée **au moment** (contrairement au pseud état
> jonction) où il est atteint.
>
> Les **conditions de gardes** doivent être **exclusives**.

L\'utilisation d\'une clause \[*else*\] est recommandée après un
pseudo-état décision, car elle garantit un modèle correct en englobant
tout ce qui n'est pas décrit dans les autres expressions logiques et en
assurant ainsi qu'un moins un segment en aval est franchissable.

+--------+-------------------------------------------------------------+
| > ![]  | ![](14-Logique/C                                            |
| (14-Lo | ours/pandoc/media/image85.emf){width="2.0659722222222223in" |
| gique/ | height="1.1659722222222222in"}**Pseudo état jonction**      |
| Cours/ |                                                             |
| pandoc | Ci-contre, dès que l'événement apparaît, le pseudo-état     |
| /media | décision est atteint. Si la condition est vraie, c'est      |
| /image | l'état 2 qui devient actif, sinon, c'est l'état 3.          |
| 10.png |                                                             |
| ){widt |                                                             |
| h="0.6 |                                                             |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **Vrai ou Faux**                                            |
| (14-Lo |                                                             |
| gique/ | **Ces deux portions de diagramme d'état décrivent-ils des   |
| Cours/ | comportements identiques ?**                                |
| pandoc |                                                             |
| /media | !                                                           |
| /image | [](14-Logique/Cours/pandoc/media/image86.png){width="5.6in" |
| 10.png | height="0.775in"}                                           |
| ){widt |                                                             |
| h="0.6 | ![]                                                         |
| 262696 | (14-Logique/Cours/pandoc/media/image87.png){width="2.425in" |
| 850393 | height="1.2166666666666666in"}                              |
| 701in" |                                                             |
| >      | **Ce diagramme d'état est-il correct ?**                    |
| height |                                                             |
| ="0.65 | **Ces deux diagrammes d'état sont-ils équivalents ? Les     |
| 083333 | gardes sont bien exclusives.**                              |
| 333333 |                                                             |
| 34in"} | ![]                                                         |
|        | (14-Logique/Cours/pandoc/media/image88.png){width="5.575in" |
|        | height="1.0416666666666667in"}                              |
+========+=============================================================+
+--------+-------------------------------------------------------------+

### État composite

> Un **état composite** décrit les **évolutions internes** d'un **état**
> à l'aide d'un **autre diagramme d'état**.
>
> ![](14-Logique/Cours/pandoc/media/image89.png){width="0.8778576115485565in"
> height="0.4507917760279965in"}
>
> Pour repérer un état composite, un signe symbolisant des lunettes est
> apposé sur l'état.

Cette structure qui englobe plusieurs sous-états exclusifs considérés
comme *hiérarchiquement inférieur* au diagramme principal, permet de
rendre ce dernier plus lisible en entrant séparément dans le détail des
évolutions internes du système.

+--------+-------------------------------------------------------------+
| > ![]  | ![](14-Logique/C                                            |
| (14-Lo | ours/pandoc/media/image90.png){width="1.1354166666666667in" |
| gique/ | height="1.0166666666666666in"}**Radio-réveil**              |
| Cours/ |                                                             |
| pandoc | ![](14-Logique/C                                            |
| /media | ours/pandoc/media/image91.png){width="3.3388210848643918in" |
| /image | height="2.6156135170603676in"}![](14-Logique/C              |
| 10.png | ours/pandoc/media/image92.png){width="3.5083333333333333in" |
| ){widt | height="1.4666666666666666in"}                              |
| h="0.6 |                                                             |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

  ------------------------------------- ---------------------------------

  ------------------------------------- ---------------------------------

> Une transition qui atteint la bordure d'un état composite est
> équivalente à une transition qui atteint l'état initial de sa région
> interne.
>
> Une transition qui sort de la bordure d'un état composite est
> équivalente à une transition qui sort de tous les états de sa région
> interne.

### Historique d'un état composite

+-----------------------------------------------------------------------+
| > L'**état actif** au **moment** de la **sortie** d'un **état         |
| > composite** peut être **mémorisé** par l'indication **historique**. |
| >                                                                     |
| > ![](14-                                                             |
| Logique/Cours/pandoc/media/image93.png){width="0.33541666666666664in" |
| > height="0.30416666666666664in"}                                     |
| >                                                                     |
| > Lors de la **réactivation** de l'**état composite**, celui-ci se    |
| > **réactive à cet état.**                                            |
+=======================================================================+
+-----------------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **Arrêt d'urgence**                                         |
| (14-Lo |                                                             |
| gique/ | L'*historique* est utilisé ici pour permettre à un système  |
| Cours/ | de recommencer en cours de cycle lors du redémarrage après  |
| pandoc | un appui sur l'arrêt d'urgence (ARU).                       |
| /media |                                                             |
| /image | ![C:\\Users\\ja                                             |
| 10.png | ck\\AppData\\Local\\Temp\\SNAGHTML3652582b.PNG](14-Logique/ |
| ){widt | Cours/pandoc/media/image94.png){width="4.244317585301837in" |
| h="0.6 | height="2.106680883639545in"}                               |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

### État composite orthogonal 

> Dans un **état composite orthogonal**, **plusieurs diagrammes
> d\'états** peuvent évoluer **simultanément** dans des **régions**
> séparées par des pointillés.
>
> Les **différentes régions** de l'état orthogonal **fonctionnent** en
> **parallèle** sans **aucune influence** les unes sur les autres
> (plusieurs états sont actifs en même temps).
>
> Une **transition** qui atteint la **bordure** d'un état **composite
> orthogonal** est **équivalente** à une **transition** qui atteint les
> **états initiaux** de **toutes** ses **régions**.
>
> **Toutes** les **régions** d'un **état composite orthogonal** doivent
> **atteindre** leur **état final** pour que l'**état composite** soit
> considéré comme **terminé**. Ce n'est qu'à cette condition que la
> **transition** de **sortie** de l\'**état composite** devient
> **franchissable**.

+--------+-------------------------------------------------------------+
| > ![]  | ![](14-Logique/Co                                           |
| (14-Lo | urs/pandoc/media/image95.jpeg){width="0.4543241469816273in" |
| gique/ | height="1.0227274715660541in"}**Distributeur de boissons**  |
| Cours/ |                                                             |
| pandoc | ![](14-Logique/C                                            |
| /media | ours/pandoc/media/image96.emf){width="5.6272856517935255in" |
| /image | height="1.765152012248469in"}                               |
| 10.png |                                                             |
| ){widt |                                                             |
| h="0.6 |                                                             |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

> L'**activation** et la **sortie** d'un **état composite**
> **orthogonal** peuvent être également symbolisés par des **barres de
> synchronisation *fork*** et ***join*** qui fonctionnent par paire.
>
> Les **transitions,** nécessairement **automatiques**, qui **partent**
> d\'une barre de synchronisation ***fork*** sont **franchies
> simultanément**.
>
> La **transition** qui **part** d'une barre de synchronisation
> ***join*** n'est **franchissable** qu\'après le **franchissement** de
> **toutes** les **transitions,** nécessairement **automatiques**, qui
> **convergent** vers cette barre.

+--------+-------------------------------------------------------------+
| > ![]  | ![](14-Logique/Co                                           |
| (14-Lo | urs/pandoc/media/image95.jpeg){width="0.4543241469816273in" |
| gique/ | height="1.0227274715660541in"}**Distributeur de boissons**  |
| Cours/ |                                                             |
| pandoc | ![](14-Logique/                                             |
| /media | Cours/pandoc/media/image97.emf){width="5.690332458442695in" |
| /image | height="1.8939391951006124in"}                              |
| 10.png |                                                             |
| ){widt |                                                             |
| h="0.6 |                                                             |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **Turbine à gaz**                                           |
| (14-Lo |                                                             |
| gique/ | La plupart des pays de l'Union Européenne ont entamé une    |
| Cours/ | transition énergétique afin de réduire les émissions des    |
| pandoc | gaz à effet de serre. Ainsi, la part des énergies           |
| /media | renouvelables comme le solaire ou l'éolien augmente. Leur   |
| /image | principal inconvénient est leur intermittence. Il est alors |
| 10.png | nécessaire de disposer de sources permettant de pallier ce  |
| ){widt | défaut. Les turbines à gaz (**figure 1**) sont souvent la   |
| h="0.6 | solution privilégiée pour leur rendement, leur réactivité   |
| 262696 | et leur impact environnemental. Ce sont des machines        |
| 850393 | tournantes thermodynamiques appartenant à la famille des    |
| 701in" | moteurs à combustion interne. Elles peuvent produire de     |
| >      | l'électricité et de la chaleur à partir de la combustion du |
| height | gaz.                                                        |
| ="0.65 |                                                             |
| 083333 | Du fait de leur taille relativement réduite et de leur      |
| 333333 | capacité de production, ces turbines sont aussi parfois     |
| 34in"} | installées loin de toute autre source d'énergie             |
|        | (plateformes maritimes par exemple) afin de fournir         |
|        | électricité et chaleur. Ces types de sources d'énergie sont |
|        | aussi utilisés dans divers bâtiments (usines, universités,  |
|        | bâtiments publics en tout genre) comme source de secours en |
|        | cas de panne de la source principale d'énergie.             |
|        |                                                             |
|        | ![](1                                                       |
|        | 4-Logique/Cours/pandoc/media/image98.png){width="2.56875in" |
|        | height="4.340277777777778in"}![](14-Logique/C               |
|        | ours/pandoc/media/image99.png){width="4.3879965004374455in" |
|        | height="1.760132327209099in"}                               |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image100.png){width="2.886111111111111in" |
|        | height="1.6694444444444445in"}Le principe de fonctionnement |
|        | de ces turbines (schématisé sur la **figure 2**) repose sur |
|        | la combustion d'un gaz (G) injecté dans une chambre de      |
|        | combustion (Ch). Ce gaz mélangé à de l'air (E) comprimé via |
|        | un compresseur à ailettes (C) est brûlé mettant ainsi en    |
|        | rotation un arbre (A) par l'intermédiaire de roues à aubes  |
|        | (T) par lesquelles passe le gaz de combustion. La rotation  |
|        | de cet arbre permet ensuite de générer un courant           |
|        | électrique par l'intermédiaire d'un alternateur (non        |
|        | représenté sur la **figure 2**). Les gaz d'échappement (Ec) |
|        | peuvent ensuite être utilisés pour produire de la chaleur.  |
|        |                                                             |
|        | **Figure 2 -** Schéma de principe de fonctionnement d'une   |
|        | turbine gaz                                                 |
|        |                                                             |
|        | Il est toutefois à noter que ce principe ne fonctionne      |
|        | qu'une fois la turbine déjà lancée. Il est donc nécessaire  |
|        | de disposer d'un système de lancement électrique ou         |
|        | pneumatique.                                                |
|        |                                                             |
|        | Le démarrage de la turbine est décrit par le diagramme      |
|        | d'état.                                                     |
|        |                                                             |
|        | **À l'aide des éléments précédents, compléter le            |
|        | chronogramme.**                                             |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image101.png){width="5.786097987751531in" |
|        | height="2.7827099737532808in"}                              |
|        |                                                             |
|        | Les variables associées à ce chronogramme sont notées ainsi |
|        | :                                                           |
|        |                                                             |
|        | \- E représente l'état embrayé (le moteur de démarrage      |
|        | entraîne l'arbre de la turbine) ;                           |
|        |                                                             |
|        | \- D représente l'état débrayé (le moteur de démarrage      |
|        | n'entraîne plus l'arbre) ;                                  |
|        |                                                             |
|        | \- AV représente la phase d'augmentation de vitesse du      |
|        | moteur grâce au variateur (état à 1                         |
|        |                                                             |
|        | lorsque la vitesse augmente, 0 sinon) ;                     |
|        |                                                             |
|        | \- C représente l'état du capteur de vitesse (son état est  |
|        | à 1 lorsque la vitesse du moteur atteint la vitesse         |
|        | d'autonomie *Ntr*, sinon son état est 0).                   |
|        |                                                             |
|        | ![](14-Logique/Co                                           |
|        | urs/pandoc/media/image102.emf){width="0.9854166666666667in" |
|        | height="1.5041666666666667in"}E**n déduire le temps de      |
|        | cycle de démarrage et le comparer au cahier des charges.**  |
+========+=============================================================+
+--------+-------------------------------------------------------------+

## Diagramme de séquence (sd) 

Un autre diagramme du langage SysML permet de décrire le
**comportement** séquentiel d'un système. Il s'agit du diagramme de
séquence.

### Diagramme de séquence

Un diagramme de séquence est rattaché à un cas d'utilisation et décrit
ce dernier en entier ou en partie, ce qui correspond à un scénario de
fonctionnement possible, défini dans un cadre précis.

> Il décrit, dans l'**ordre chronologique**, l'**enchaînement** des
> **interactions** (ou messages) entre les **acteurs** du système ou
> entre des **composants** du système eux-mêmes.

Les principaux éléments sont :

+---------+-----+-----------+--------------+-------------------+----+---+---+
| **Ligne | Li  |           |              |                   |    |   |   |
| de      | gne |           |              |                   |    |   |   |
| vie**   | ver |           |              |                   |    |   |   |
|         | tic |           |              |                   |    |   |   |
|         | ale |           |              |                   |    |   |   |
|         | en  |           |              |                   |    |   |   |
|         | po  |           |              |                   |    |   |   |
|         | int |           |              |                   |    |   |   |
|         | ill |           |              |                   |    |   |   |
|         | ée. |           |              |                   |    |   |   |
|         | Une |           |              |                   |    |   |   |
|         | p   |           |              |                   |    |   |   |
|         | our |           |              |                   |    |   |   |
|         | cha |           |              |                   |    |   |   |
|         | que |           |              |                   |    |   |   |
|         | é   |           |              |                   |    |   |   |
|         | lém |           |              |                   |    |   |   |
|         | ent |           |              |                   |    |   |   |
|         | d   |           |              |                   |    |   |   |
|         | ial |           |              |                   |    |   |   |
|         | ogu |           |              |                   |    |   |   |
|         | ant |           |              |                   |    |   |   |
|         | (a  |           |              |                   |    |   |   |
|         | cte |           |              |                   |    |   |   |
|         | ur, |           |              |                   |    |   |   |
|         | sy  |           |              |                   |    |   |   |
|         | stè |           |              |                   |    |   |   |
|         | me, |           |              |                   |    |   |   |
|         | sou |           |              |                   |    |   |   |
|         | s-s |           |              |                   |    |   |   |
|         | yst |           |              |                   |    |   |   |
|         | ème |           |              |                   |    |   |   |
|         | ou  |           |              |                   |    |   |   |
|         | co  |           |              |                   |    |   |   |
|         | mpo |           |              |                   |    |   |   |
|         | san |           |              |                   |    |   |   |
|         | t). |           |              |                   |    |   |   |
+=========+=====+===========+==============+===================+====+===+===+
| **      | Ba  |           |              |                   |    |   |   |
| Période | nde |           |              |                   |    |   |   |
| d'act   | ver |           |              |                   |    |   |   |
| ivité** | tic |           |              |                   |    |   |   |
|         | ale |           |              |                   |    |   |   |
|         | sur |           |              |                   |    |   |   |
|         | une |           |              |                   |    |   |   |
|         | li  |           |              |                   |    |   |   |
|         | gne |           |              |                   |    |   |   |
|         | de  |           |              |                   |    |   |   |
|         | v   |           |              |                   |    |   |   |
|         | ie. |           |              |                   |    |   |   |
|         | Opt |           |              |                   |    |   |   |
|         | ion |           |              |                   |    |   |   |
|         | nel |           |              |                   |    |   |   |
|         | les |           |              |                   |    |   |   |
|         | el  |           |              |                   |    |   |   |
|         | les |           |              |                   |    |   |   |
|         | f   |           |              |                   |    |   |   |
|         | aci |           |              |                   |    |   |   |
|         | lit |           |              |                   |    |   |   |
|         | ent |           |              |                   |    |   |   |
|         | la  |           |              |                   |    |   |   |
|         | l   |           |              |                   |    |   |   |
|         | ect |           |              |                   |    |   |   |
|         | ure |           |              |                   |    |   |   |
|         | du  |           |              |                   |    |   |   |
|         | d   |           |              |                   |    |   |   |
|         | iag |           |              |                   |    |   |   |
|         | ram |           |              |                   |    |   |   |
|         | me. |           |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
| **Me    | Flè |           |              |                   |    |   |   |
| ssage** | che |           |              |                   |    |   |   |
|         | ho  |           |              |                   |    |   |   |
|         | riz |           |              |                   |    |   |   |
|         | ont |           |              |                   |    |   |   |
|         | ale |           |              |                   |    |   |   |
|         | un  |           |              |                   |    |   |   |
|         | idi |           |              |                   |    |   |   |
|         | rec |           |              |                   |    |   |   |
|         | tio |           |              |                   |    |   |   |
|         | nne |           |              |                   |    |   |   |
|         | lle |           |              |                   |    |   |   |
|         | en  |           |              |                   |    |   |   |
|         | tre |           |              |                   |    |   |   |
|         | d   |           |              |                   |    |   |   |
|         | eux |           |              |                   |    |   |   |
|         | lig |           |              |                   |    |   |   |
|         | nes |           |              |                   |    |   |   |
|         | de  |           |              |                   |    |   |   |
|         | vie |           |              |                   |    |   |   |
|         | rep |           |              |                   |    |   |   |
|         | rés |           |              |                   |    |   |   |
|         | ent |           |              |                   |    |   |   |
|         | ant |           |              |                   |    |   |   |
|         | un  |           |              |                   |    |   |   |
|         | é   |           |              |                   |    |   |   |
|         | lém |           |              |                   |    |   |   |
|         | ent |           |              |                   |    |   |   |
|         | de  |           |              |                   |    |   |   |
|         | co  |           |              |                   |    |   |   |
|         | mmu |           |              |                   |    |   |   |
|         | nic |           |              |                   |    |   |   |
|         | ati |           |              |                   |    |   |   |
|         | on. |           |              |                   |    |   |   |
|         | E   |           |              |                   |    |   |   |
|         | lle |           |              |                   |    |   |   |
|         | déc |           |              |                   |    |   |   |
|         | len |           |              |                   |    |   |   |
|         | che |           |              |                   |    |   |   |
|         | une |           |              |                   |    |   |   |
|         | p   |           |              |                   |    |   |   |
|         | éri |           |              |                   |    |   |   |
|         | ode |           |              |                   |    |   |   |
|         | d   |           |              |                   |    |   |   |
|         | 'ac |           |              |                   |    |   |   |
|         | tiv |           |              |                   |    |   |   |
|         | ité |           |              |                   |    |   |   |
|         | (un |           |              |                   |    |   |   |
|         | c   |           |              |                   |    |   |   |
|         | omp |           |              |                   |    |   |   |
|         | ort |           |              |                   |    |   |   |
|         | eme |           |              |                   |    |   |   |
|         | nt) |           |              |                   |    |   |   |
|         | c   |           |              |                   |    |   |   |
|         | hez |           |              |                   |    |   |   |
|         | le  |           |              |                   |    |   |   |
|         | re  |           |              |                   |    |   |   |
|         | cev |           |              |                   |    |   |   |
|         | eur |           |              |                   |    |   |   |
|         | du  |           |              |                   |    |   |   |
|         | me  |           |              |                   |    |   |   |
|         | ssa |           |              |                   |    |   |   |
|         | ge, |           |              |                   |    |   |   |
|         | p   |           |              |                   |    |   |   |
|         | our |           |              |                   |    |   |   |
|         | q   |           |              |                   |    |   |   |
|         | ui, |           |              |                   |    |   |   |
|         | l   |           |              |                   |    |   |   |
|         | \'a |           |              |                   |    |   |   |
|         | rri |           |              |                   |    |   |   |
|         | vée |           |              |                   |    |   |   |
|         | d\  |           |              |                   |    |   |   |
|         | 'un |           |              |                   |    |   |   |
|         | m   |           |              |                   |    |   |   |
|         | ess |           |              |                   |    |   |   |
|         | age |           |              |                   |    |   |   |
|         | est |           |              |                   |    |   |   |
|         | un  |           |              |                   |    |   |   |
|         | évé |           |              |                   |    |   |   |
|         | nem |           |              |                   |    |   |   |
|         | ent |           |              |                   |    |   |   |
|         | déc |           |              |                   |    |   |   |
|         | len |           |              |                   |    |   |   |
|         | che |           |              |                   |    |   |   |
|         | ur. |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | Ce  |           |              |                   |    |   |   |
|         | m   |           |              |                   |    |   |   |
|         | ess |           |              |                   |    |   |   |
|         | age |           |              |                   |    |   |   |
|         | p   |           |              |                   |    |   |   |
|         | eut |           |              |                   |    |   |   |
|         | êtr |           |              |                   |    |   |   |
|         | e : |           |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
|         | -   |           |              |                   |    |   |   |
|         |  sy |           |              |                   |    |   |   |
|         | nch |           |              |                   |    |   |   |
|         | ron |           |              |                   |    |   |   |
|         | e : |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |  l\ |           |              |                   |    |   |   |
|         | 'ém |           |              |                   |    |   |   |
|         | ett |           |              |                   |    |   |   |
|         | eur |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | att |           |              |                   |    |   |   |
|         | end |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | une |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |  ré |           |              |                   |    |   |   |
|         | pon |           |              |                   |    |   |   |
|         | se, |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | son |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | com |           |              |                   |    |   |   |
|         | por |           |              |                   |    |   |   |
|         | tem |           |              |                   |    |   |   |
|         | ent |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | est |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | blo |           |              |                   |    |   |   |
|         | qué |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |   p |           |              |                   |    |   |   |
|         | end |           |              |                   |    |   |   |
|         | ant |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |  l' |           |              |                   |    |   |   |
|         | att |           |              |                   |    |   |   |
|         | ent |           |              |                   |    |   |   |
|         | e ; |           |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
|         | -   |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | asy |           |              |                   |    |   |   |
|         | nch |           |              |                   |    |   |   |
|         | ron |           |              |                   |    |   |   |
|         | e : |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |  l\ |           |              |                   |    |   |   |
|         | 'ém |           |              |                   |    |   |   |
|         | ett |           |              |                   |    |   |   |
|         | eur |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | n\' |           |              |                   |    |   |   |
|         | att |           |              |                   |    |   |   |
|         | end |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | pas |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |  de |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |  ré |           |              |                   |    |   |   |
|         | pon |           |              |                   |    |   |   |
|         | se, |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | son |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | com |           |              |                   |    |   |   |
|         | por |           |              |                   |    |   |   |
|         | tem |           |              |                   |    |   |   |
|         | ent |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | con |           |              |                   |    |   |   |
|         | tin |           |              |                   |    |   |   |
|         | u ; |           |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
|         | -   |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         | une |           |              |                   |    |   |   |
|         |     |           |              |                   |    |   |   |
|         |  ré |           |              |                   |    |   |   |
|         | pon |           |              |                   |    |   |   |
|         | se. |           |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
|         | Il  |           |              |                   |    |   |   |
|         | est |           |              |                   |    |   |   |
|         | po  |           |              |                   |    |   |   |
|         | ssi |           |              |                   |    |   |   |
|         | ble |           |              |                   |    |   |   |
|         | d\  |           |              |                   |    |   |   |
|         | 'av |           |              |                   |    |   |   |
|         | oir |           |              |                   |    |   |   |
|         | un  |           |              |                   |    |   |   |
|         | m   |           |              |                   |    |   |   |
|         | ess |           |              |                   |    |   |   |
|         | age |           |              |                   |    |   |   |
|         | ré  |           |              |                   |    |   |   |
|         | fle |           |              |                   |    |   |   |
|         | xif |           |              |                   |    |   |   |
|         | c   |           |              |                   |    |   |   |
|         | orr |           |              |                   |    |   |   |
|         | esp |           |              |                   |    |   |   |
|         | ond |           |              |                   |    |   |   |
|         | ant |           |              |                   |    |   |   |
|         | à   |           |              |                   |    |   |   |
|         | une |           |              |                   |    |   |   |
|         | in  |           |              |                   |    |   |   |
|         | ter |           |              |                   |    |   |   |
|         | act |           |              |                   |    |   |   |
|         | ion |           |              |                   |    |   |   |
|         | i   |           |              |                   |    |   |   |
|         | nte |           |              |                   |    |   |   |
|         | rne |           |              |                   |    |   |   |
|         | au  |           |              |                   |    |   |   |
|         | c   |           |              |                   |    |   |   |
|         | omp |           |              |                   |    |   |   |
|         | osa |           |              |                   |    |   |   |
|         | nt. |           |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
| **Fra   | Ca  |           |              |                   |    |   |   |
| gment** | dre |           |              |                   |    |   |   |
|         | eng |           |              |                   |    |   |   |
|         | lob |           |              |                   |    |   |   |
|         | ant |           |              |                   |    |   |   |
|         | une |           |              |                   |    |   |   |
|         | par |           |              |                   |    |   |   |
|         | tie |           |              |                   |    |   |   |
|         | de  |           |              |                   |    |   |   |
|         | la  |           |              |                   |    |   |   |
|         | sé  |           |              |                   |    |   |   |
|         | que |           |              |                   |    |   |   |
|         | nce |           |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
|         | *   | Boucle,   |              | ![](14-           |    |   |   |
|         | **l | le        |              | Logique/Cours/pan |    |   |   |
|         | oop | fragment  |              | doc/media/image10 |    |   |   |
|         | *** | est       |              | 3.png){width="3.0 |    |   |   |
|         |     | maintenu  |              | 01149387576553in" |    |   |   |
|         |     | pendant   |              | height="0.627     |    |   |   |
|         |     | une durée |              | 5131233595801in"} |    |   |   |
|         |     | qui       |              |                   |    |   |   |
|         |     | dépend de |              |                   |    |   |   |
|         |     | la        |              |                   |    |   |   |
|         |     | condition |              |                   |    |   |   |
|         |     | de garde. |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
|         | *** | Séquence  |              | ![](14-L          |    |   |   |
|         | par | en        |              | ogique/Cours/pand |    |   |   |
|         | *** | p         |              | oc/media/image104 |    |   |   |
|         |     | arallèle. |              | .png){width="2.60 |    |   |   |
|         |     | Les       |              | 29527559055117in" |    |   |   |
|         |     | régions   |              | height="0.655     |    |   |   |
|         |     | peuvent   |              | 7064741907261in"} |    |   |   |
|         |     | être      |              |                   |    |   |   |
|         |     | exécutées |              |                   |    |   |   |
|         |     | simul     |              |                   |    |   |   |
|         |     | tanément. |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
|         | *** | Séquences |              | ![](14-L          |    |   |   |
|         | alt | alt       |              | ogique/Cours/pand |    |   |   |
|         | *** | ernatives |              | oc/media/image105 |    |   |   |
|         |     | condi     |              | .png){width="2.52 |    |   |   |
|         |     | tionnées. |              | 49956255468065in" |    |   |   |
|         |     | Seule la  |              | height="0.731     |    |   |   |
|         |     | région    |              | 9291338582677in"} |    |   |   |
|         |     | dont la   |              |                   |    |   |   |
|         |     | condition |              |                   |    |   |   |
|         |     | est vraie |              |                   |    |   |   |
|         |     | s         |              |                   |    |   |   |
|         |     | 'exécute. |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+
|         |     |           |              |                   |    |   |   |
+---------+-----+-----------+--------------+-------------------+----+---+---+

+--------+-------------------------------------------------------------+
| > ![]  | ![](14-Logique/C                                            |
| (14-Lo | ours/pandoc/media/image106.png){width="1.074818460192476in" |
| gique/ | height="1.0698097112860891in"}![](14-Logique/C              |
| Cours/ | ours/pandoc/media/image107.png){width="1.236742125984252in" |
| pandoc | height="0.6761362642169729in"}**Système de vente de repas   |
| /media | en ligne**                                                  |
| /image |                                                             |
| 10.png | ![](1                                                       |
| ){widt | 4-Logique/Cours/pandoc/media/image108.png){width="5.4625in" |
| h="0.6 | height="4.554166666666666in"}                               |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

## CODEUR INCREMENTAL ET ABSOLU

### Familles de capteurs

Pour contrôler le bon fonctionnement d\'une chaîne d\'énergie, il est
nécessaire de mesurer des grandeurs physiques. Les 3 types de capteurs
qui permettent d\'acquérir des grandeurs sont :

-   **les capteurs :** délivre une information **analogique**
    > (potentiomètre linéaire, rotatif, règle magnétique, cellule
    > magnétorésistive, tachymètre , génératrice tachymétrique,
    > accéléromètre, débitmètre, dynamomètre, jauges de déformation,
    > cellules pièzo-électriques, manomètre\...)

-   **les codeurs :** délivre une information **numérique** (codeur
    > incrémental, absolu)

-   **les détecteurs :** délivre une information **logique** (détecteur
    > fin de course ILS, détecteur à effet hall, boutons\...)

### Vocabulaire de métrologie

> **Résolution :** Plus petite variation de grandeur mesurable par le
> capteur.
>
> *[Ex :]{.underline} Le codeur incrémental à une résolution de 0,087°.*
>
> **Sensibilité :** Variation du signal de sortie par rapport à la
> variation du signal d\'entrée. *[Ex :]{.underline} Le capteur de
> température LM35 a une sensibilité de 10mV/°C.*

![](14-Logique/Cours/pandoc/media/image109.png){width="2.2694444444444444in"
height="0.9381944444444444in"}

> **Fidélité :** Répétabilité de la mesure
>
> **Justesse :** Réponse proche de la valeur vraie.
>
> **Précision :** Écart entre la valeur vraie et la valeur mesurée.

### Les codeurs

**Le codeur est généralement placé en amont du réducteur**, car pour un
même mouvement, on obtient plus d\'impulsion et donc une meilleure
résolution.

##### Codeur incrémental (ou roue codeuse) {#codeur-incrémental-ou-roue-codeuse .unnumbered}

> ![](14-Logique/Cours/pandoc/media/image111.png){width="1.5704702537182853in"
> height="1.3304352580927383in"}[Codeur incrémental (ou roue codeuse)
> :]{.underline}
>
> Un codeur incrémental est un générateur d'**impulsions** qui fournit 2
> voies en **quadrature** et un top zéro. Elles sont divisées en n
> secteurs angulaires égaux, alternativement opaques et transparents.
>
> Ils fonctionnent sur le principe de **comptage** et **décomptage**
> **d\'impulsions** et donne donc le déplacement relatif.
>
> n s\'appelle le nombre de périodes, c\'est le nombre d\'impulsions qui
> sont délivrées par le codeur pour un tour complet de son disque.
>
> ![incremental.jpg](14-Logique/Cours/pandoc/media/image112.jpeg){width="2.104861111111111in"
> height="1.8020833333333333in"}![](14-Logique/Cours/pandoc/media/image113.png){width="2.3722222222222222in"
> height="2.1625in"}

**Avantages :**

> Mesure prise à coût raisonnable ;
>
> Entrées de comptage adaptées (voies A, B, Z) en standard sur les
> automates programmables récents ;
>
> Obtention aisée de la vitesse par intégration numérique.
>
> **Inconvénients :**
>
> Perte totale des informations en cas de coupure d\'énergie ;
>
> Nécessite une procédure de prise d\'origine.

![](14-Logique/Cours/pandoc/media/image114.png){width="1.613888888888889in"
height="0.9645833333333333in"}![](14-Logique/Cours/pandoc/media/image115.png){width="2.6770833333333335in"
height="0.8868055555555555in"}

Disque d\'un codeur incrémental et pistes en quadrature de phase

> Les pistes intérieures et extérieures sont en **quadrature de phase**,
> ce qui permet de :

-   connaitre le **sens de rotation** du capteur

-   **améliorer par 2 la résolution** du capteur.

+------------------------------------+---------------------------------+
| > Déterminer le sens de rotation   |                                 |
+====================================+=================================+
| > ![](14                           | > ![](14-Logiqu                 |
| -Logique/Cours/pandoc/media/image1 | e/Cours/pandoc/media/image119.p |
| 18.png){width="2.18786198600175in" | ng){width="2.178814523184602in" |
| > height="1.1652176290463692in"}   | >                               |
| >                                  |  height="1.1652187226596675in"} |
| > Le front montant de la voie      | >                               |
| > verte se présente avant celui de | > Le front montant de la voie   |
| > la voie rouge.                   | > rouge se présente avant celui |
|                                    | > de la voie verte.             |
+------------------------------------+---------------------------------+

##### ![](14-Logique/Cours/pandoc/media/image120.png){width="1.2654286964129484in" height="1.0260870516185476in"}Codeur absolu (ou numérique) {#codeur-absolu-ou-numérique .unnumbered}

> [Codeur absolu (ou numérique) :]{.underline}
>
> Délivre un signal image de la position à mesurer **sous forme d\'un
> code numérique binaire** et donne le déplacement absolu.
>
> Il dispose de N pistes, généralement agencées suivant le code
> **Gray**.
>
> La piste intérieure correspond au bit de poids le plus fort.
>
> **Avantages :**

-   Chaque secteur possédant son code unique, il est inutile de
    > déterminer le sens de rotation ;

-   Pas de perte d\'information en cas de coupure d\'énergie ;

-   Code connu en permanence, pas besoin de procéder à la Prise
    > d\'Origine Machine lors de la mise sous tension ;

-   Pas d\'erreur de lecture avec le code Gray.

![](14-Logique/Cours/pandoc/media/image121.png){width="1.0645833333333334in"
height="1.0368055555555555in"}

> **Inconvénients :**

-   Relativement onéreux ;

-   Interface avec la commande plus complexe (N entrées) ;

-   Nécessite un transcodeur pour reconvertir le signal en binaire
    > naturel.

+--------+-------------------------------------------------------------+
| > ![]  | **Simulateur de moto - Codeur incrémental -- Asservissement |
| (14-Lo | d'un vérin**                                                |
| gique/ |                                                             |
| Cours/ | ![](14-Logique/Co                                           |
| pandoc | urs/pandoc/media/image122.emf){width="1.5006944444444446in" |
| /media | height="1.55in"}                                            |
| /image |                                                             |
| 10.png | Les usagers de deux-roues motorisés sont soumis à un risque |
| ){widt | accru d'accidents en comparaison aux autres catégories      |
| h="0.6 | d'usagers.                                                  |
| 262696 |                                                             |
| 850393 | Dans le but de réduire ce risque, la simulation de conduite |
| 701in" | offre une nouvelle opportunité pour appréhender le          |
| >      | comportement des conducteurs dans un cadre sécuritaire et   |
| height | constitue un outil alternatif pour la formation à la        |
| ="0.65 | conduite.                                                   |
| 083333 |                                                             |
| 333333 | ![](14-Logique/C                                            |
| 34in"} | ours/pandoc/media/image123.png){width="5.897916666666666in" |
|        | height="2.5548611111111112in"}                              |
|        |                                                             |
|        | Le capteur de position utilisé est un codeur optique        |
|        | composé de deux voies (Voies A et B) qui permettent de      |
|        | détecter le sens de rotation. Le diagramme d'état du        |
|        | document réponse DR4 décrit le comptage des impulsions      |
|        | Nmes. L'allure des signaux reçus (après traitement          |
|        | électronique) est donnée sur la figure 16.                  |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image124.png){width="5.897916666666666in" |
|        | height="2.1930555555555555in"}                              |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image125.png){width="5.897916666666666in" |
|        | height="1.5208333333333333in"}                              |
|        |                                                             |
|        | **Compléter sur le document réponse, le chronogramme        |
|        | donnant l'évolution de la valeur N~mes~ renvoyée par le     |
|        | compteur. Indiquer sur le diagramme d'état à quel numéro de |
|        | mesure (mesures numérotées sur la figure 16) correspond     |
|        | chacun des états.**                                         |
|        |                                                             |
|        | Le complément de la variable logique A (respectivement B)   |
|        | est noté !A respectivement !B) sur le diagramme. Selon le   |
|        | contexte, la notation A pourra se référer à un évènement ou |
|        | à une condition de garde.                                   |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image126.png){width="5.897916666666666in" |
|        | height="2.6319444444444446in"}                              |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image127.png){width="5.897916666666666in" |
|        | height="4.384722222222222in"}                               |
|        |                                                             |
|        | **En vous appuyant sur le diagramme de définition de blocs  |
|        | (figure 13) et sur le schéma bloc de l'asservissement       |
|        | (figure 14), donner la valeur du gain K~cap~ du codeur.**   |
+========+=============================================================+
+--------+-------------------------------------------------------------+

## RESEAUX ET BUS DE TERRAIN

### Introduction sur les données

Aujourd'hui, de nombreux types de données doivent être transmises :

-   La parole et son haute-fidélité;

-   Des données alphanumériques (texte, fichiers de données,...);

-   Des images fixes (N/B et couleurs);

-   Images animées (Télévision par exemple);

-   Informations multimédias (Combinaisons précédentes)

La transmission de données aura alors plusieurs critères de performances
(disponibilité, taux d'erreur, débit, ....)

###  Qualité de service : QoS

Elle se traduit sous différentes exigences :

-   La disponibilité des moyens de transfert de l'information (liés au
    taux de panne des équipements et liaisons);

-   Le taux d'erreur maximal, exprimé par le rapport entre le nombre de
    bits dont la valeur est modifiée par rapport au nombre total de bits
    d'informations émis ;

-   Le débit de transfert ;

-   Le délai, c'est à dire, la durée entre la décision d'émettre et la
    réception par le destinataire.

Ces exigences varient en fonction de la nature des informations à
transmettre.

  ------------- ----------------- ---------------- -------------- --------------
                **Importance de   **Importance du  **Importance   **Importance
                la                Taux d'erreur**  du Débit**     du Délai**
                disponibilité**                                   

  **Voix**      Important         Peu important    Peu important  Très faible ou
                                                                  constant

  **Images      Peu important     Peu important    Très important Très faible
  animées**                                                       

  **Texte,      Important         Très faible      Peu important  Peu important
  images                          (10^-9^)                        
  fixes**                                                         
  ------------- ----------------- ---------------- -------------- --------------

### Architecture des réseaux de communication

Dans l'architecture d'un réseau, on peut distinguer quatre catégories de
réseaux (en fonction de l'étendue de leur zone de fonctionnement) :

-   le réseau personnel : PAN (Personal Area Network) qui relie des
    machines sur quelques mètres ;

-   le réseau local : LAN (Local Area Network) qui est adapté à la
    taille d'un site d'entreprise;

-   le réseau métropolitain : MAN (Metropolitan Area Network) qui est un
    réseau étendu à l'échelle d'une ville ;

-   le réseau étendu : WAN (Wide Area Network) qui couvre une grande
    zone géographique (typiquement à l'échelle d'un pays, d'un
    continent).

![](14-Logique/Cours/pandoc/media/image128.png){width="5.35974300087489in"
height="4.63382217847769in"}

### Couches du modèle OSI

Le modèle OSI (de l'anglais open systems interconnection) est une norme
de communica-\
tion, en réseau, de tous les systèmes informatiques. C'est un modèle de
communications entre\
ordinateurs proposé par l'ISO (international organization for
standardization) qui décrit les\
fonctionnalités nécessaires à la communication et l'organisation de ces
fonctions. Il norme l'organisation de l'architecture réseau en sept
couches :

• 7. Application ;\
• 6. Présentation ;\
• 5. Session ;\
• 4. Transport ;\
• 3. Réseaux ;\
• 2. Liaison ;\
• 1. Physique.

![](14-Logique/Cours/pandoc/media/image129.png){width="6.901388888888889in"
height="2.1791666666666667in"}

On peut faire une métaphore entre la communication entre appareils
informatiques et\
entre humain. Dans les deux cas des règles sont mises en place. Par
exemple, si vous voulez communiquer avec une personne, vous ne vous
adresserez pas de la même manière s'il s'agit d'un parent, d'un
enseignant, d'un camarade de classe ou d'un bébé.

### Les supports de transmission

#####  Caractéristiques des supports de transmission {#caractéristiques-des-supports-de-transmission .unnumbered}

On distingue les caractéristiques principales suivantes :

-   **Le taux d'erreur** : Rapport du nombre de bits émis erronés reçus
    au cours d'une période d'observation sur le nombre total de bits
    transmis pendant cette période.

-   **Le débit binaire** D exprimé en bit/s. Représente le nombre de
    bits transmis par seconde.

-   La rapidité de modulation R exprimée en Baud. Indique le nombre de
    symboles transmis par unité de temps.

-   **Bande Passante à -3 dB :** Plage de fréquence pour laquelle la
    puissance du signal de sortie est au pire divisée par 2 par rapport
    au signal d'entrée.

-   **Bruits et distorsions :** Même si les signaux sont transmis dans
    la bande passante du support, les signaux sont déformés (distorsions
    d'amplitude et/ou de phase). Des perturbations extérieures (foudre,
    champ électromagnétique, interférences, ...) peuvent également
    introduire des bruits.

-   **Capacité limite :** Quantité maximale d'information transportable
    par unité de temps.

#####   {#section-1 .unnumbered}

##### Les différents supports de transmission {#les-différents-supports-de-transmission .unnumbered}

Les supports de transmission peuvent être des câbles dans lesquels
circulent des signaux électriques, l\'atmosphère où circulent des ondes
radio, ou des fibres optiques qui propagent des ondes lumineuses.

-   ![](14-Logique/Cours/pandoc/media/image130.emf){width="2.277083333333333in"
    height="0.9881944444444445in"}**Le câble à paires torsadées** (et
    souvent blindées) : Les paires torsadées sont composées de 2
    conducteurs en cuivre isolés l'un de l'autre et enroulés de façon
    hélicoïdale. Cela permet de réduire les influences
    électromagnétiques parasites provenant de l'environnement.

> Le câble RJ45 couramment utilisé pour les réseaux ethernet est
> constitué de 4 paires torsadées.

*[Utilisation :]{.underline}* Liaisons téléphoniques, réseaux en
étoile...

*[Inconvénient :]{.underline}* Atténuation importante

*[Débit maximal :]{.underline}* Jusqu'à 100Mbits/s (voire 1000Mbits/s
pour certains câbles)

-   **Les câbles coaxiaux** :

> ![](14-Logique/Cours/pandoc/media/image131.emf){width="3.15in"
> height="0.9283377077865267in"}*[Utilisation :]{.underline}* antennes
> TV... Câbles remplacés par fibres optiques sur des longues distances.

*[Débit maximal :]{.underline}* Plusieurs centaines de Mbits/s

> ![](14-Logique/Cours/pandoc/media/image130.emf){width="1.225in"
> height="0.81875in"}

-   **L'atmosphère** : Utilisation des ondes électromagnétiques dans
    l'atmosphère ou le vide. Ce support comprend les faisceaux
    hertziens, les rayons infrarouges et les rayons laser.

> Les ondes radio (radiofréquences 2,4 GHz) permettent de connecter des
> machines entre elles sans utiliser de câbles. La norme la plus
> utilisée actuellement pour les réseaux sans fil est la norme IEEE
> 802.11, mieux connue sous le nom de Wi-Fi. Le Wi-Fi permet de relier
> des machines à une liaison haut débit (plusieurs dizaines de Mbits/s)
> sur un rayon de plusieurs dizaines de mètres en intérieur (plusieurs
> centaines de mètres en extérieur).

*[Avantage :]{.underline}* Pas de support physique

> *[Inconvénients :]{.underline}* Conditions météorologiques,
> confidentialité

*[Débit maximal :]{.underline}* Plusieurs dizaines de Mbits/s (Plusieurs
centaines de Mbit/s avec certains matériels)

![](14-Logique/Cours/pandoc/media/image132.emf){width="4.158333333333333in"
height="2.2083333333333335in"}

![](14-Logique/Cours/pandoc/media/image130.emf){width="0.71875in"
height="0.9583333333333334in"}

-   **La fibre optique** : Constituée d'un fil de verre très fin. Le
    coeur de la fibre propage la lumière.

> La fibre optique autorise des vitesses de communication très élevées
> (plus de 100 Gigabit/s) ou en milieu très fortement parasité.
>
> ![](14-Logique/Cours/pandoc/media/image133.emf){width="2.3979166666666667in"
> height="1.05in"}
>
> *[Avantages :]{.underline}* masse linéique très faible, BP immense (30
> THz), faible atténuation, insensibilité aux parasites
> électromagnétiques, ...

*[Inconvénients :]{.underline}* Prix de la fibre, prix des modulateurs,
mode de pose.

*[Débit maximal :]{.underline}* 1 à 100 Gbits/s

-   ![](14-Logique/Cours/pandoc/media/image134.emf){width="1.2868055555555555in"
    height="1.2465277777777777in"}![](14-Logique/Cours/pandoc/media/image135.emf){width="2.564583333333333in"
    height="1.2625in"}**La liaison CPL (Courants Porteurs en Ligne) :**
    il s'agit d'une technique permettant le transfert d\'informations
    numériques en passant par les lignes électriques. La technologie CPL
    superpose un signal à hautes fréquences au signal électrique
    classique (50Hz, 23V). Le signal est reçu par tout boitier se
    trouvant dans le même circuit électrique.

> ![](14-Logique/Cours/pandoc/media/image136.emf){width="2.05in"
> height="2.5125in"}
>
> Il est bien sûr possible de mixer le CPL avec d\'autres supports de
> transmission, comme le montre le schéma ci-contre :

*[Débit maximal :]{.underline}* 200 à 2000 Mbits/s

> Par défaut, l\'installation de boitier CPL ne nécessite aucune
> configuration ni programme.
>
> Cependant, si on veut sécuriser quelque peu le réseau CPL, on utilise
> un outil spécifique qui permet de donner un nom au réseau CPL. Ce nom
> permet de rendre ce réseau invisible aux autres boitiers.

### ![principemultiplexage](14-Logique/Cours/pandoc/media/image137.jpeg){width="4.625in" height="2.1493055555555554in"}Multiplexage

Lorsque la bande passante d'un support physique est nettement supérieure
au spectre du signal à émettre, il est intéressant d'utiliser ce même
support pour transmettre plusieurs signaux. On parle alors de
MULTIPLEXAGE.

2 possibilités :

-   Multiplexage fréquentiel;

![](14-Logique/Cours/pandoc/media/image138.jpeg){width="4.802083333333333in"
height="2.183333333333333in"}

[Principe :]{.underline} On découpe la bande passante du support en
plusieurs sous bandes. Chaque sous bande est affectée à une voie de
transmission.

Chaque signal d'entrée est modulé en fréquence. La voie n est modulée
par une porteuse à la fréquence f~n~.

Dans ce cas, le multiplexeur joue le rôle d'un additionneur de n signaux
à différentes fréquences.

![](14-Logique/Cours/pandoc/media/image139.jpeg){width="3.2868055555555555in"
height="1.8222222222222222in"}![](14-Logique/Cours/pandoc/media/image140.jpeg){width="3.8965277777777776in"
height="2.1222222222222222in"}A la réception, on filtre le signal reçu
S(t) par des filtres passe bande qui récupère les signaux Si1(t), et
après une démodulation de fréquence, on réobtient les signaux originaux
Si(t).

-   Multiplexage temporel.

###  Les erreurs de transmission

Entre les deux extrémités d'une liaison, la présence des imperfections
du support de transmission (affaiblissement, déphasage), et la présence
de bruit électromagnétique, perturbent de façon aléatoire les données
transmises. Ces perturbations se traduisent au niveau de l'information
reçue, par des modifications : soit des disparitions, soit des
adjonctions, soit des inversions (0 en 1 ou 1 en 0).

L'objet de cette partie, est d'aborder les méthodes couramment utilisées
dans les réseaux informatiques, pour protéger les données émises contre
les erreurs introduites par le canal de transmission.

![](14-Logique/Cours/pandoc/media/image141.emf){width="4.959722222222222in"
height="1.0097222222222222in"}Ces techniques utilisent un codeur à
l'émission et un décodeur à la réception, comme le montre la figure
ci-contre.

La technique adoptée dans la plupart des systèmes de détection
d'erreurs, consiste à ajouter des bits supplémentaires (dit redondants)
à chaque bloc de données avant de le transmettre sur le support de
transmission.

#####   {#section-2 .unnumbered}

##### Contrôle de parité (LRC) {#contrôle-de-parité-lrc .unnumbered}

Le contrôle de parité est aussi appelé LRC (Longitudinal Redundancy
Check).

Il existe deux types de contrôle de parité (pair et impair) et il est
indispensable que l'émetteur et le récepteur s'entendent sur le type à
utiliser pour l'ensemble de la transmission.

**Parité paire :** Lorsque le nombre de « 1 » dans les données envoyées
est impair, le bit de parité (bit de contrôle) est placé à « 1 » de
manière à ce que le nombre total de « 1 » soit pair y compris le bit de
parité. Dans le cas contraire, le bit de parité est placé à « 0 ».

![](14-Logique/Cours/pandoc/media/image142.emf){width="5.070833333333334in"
height="0.6520833333333333in"}

**Parité impaire :** Elle correspond au système inverse.

Quelle que soit la parité choisie, si un bit est modifié au cours de la
transmission, les calculs de parité effectués par l'émetteur et par le
récepteur différeront.

Cette méthode est peu performante, le contrôle fonctionne correctement
seulement si le nombre de bits modifiés est impair.

Si on met cela sous forme d'équation logique, le ou exclusif est très
utile.

$$Bp_{paire} = \overset{\underset{n}{i = 1}}{\oplus}d_{i}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Bp_{impaire} = \overline{\overset{\underset{n}{i = 1}}{\oplus}d_{i}}$$

+--------+-------------------------------------------------------------+
| > ![]  | **Exemples**                                                |
| (14-Lo |                                                             |
| gique/ | **Parité paire :**                                          |
| Cours/ |                                                             |
| pandoc | **Quelle doit être le bit de parité pour la donnée          |
| /media | suivante :**                                                |
| /image |                                                             |
| 10.png | 11001011                                                    |
| ){widt |                                                             |
| h="0.6 | La donnée contenant 5 état 1, le bit de parité paire est    |
| 262696 | positionné à 1,\                                            |
| 850393 | ramenant ainsi le nombre de 1 à 6.                          |
| 701in" |                                                             |
| >      | **Parité impaire :**                                        |
| height |                                                             |
| ="0.65 | **Quelle doit être le bit de parité pour la donnée          |
| 083333 | suivante :**                                                |
| 333333 |                                                             |
| 34in"} | 11001011                                                    |
|        |                                                             |
|        | La donnée contenant 5 état 1, le bit de parité paire est    |
|        | positionné à 0,\                                            |
|        | laissant ainsi un nombre de 1 impaire                       |
+========+=============================================================+
+--------+-------------------------------------------------------------+

![](14-Logique/Cours/pandoc/media/image8.png){width="4.733333333333333in"
height="1.8333333333333333in"}

##### Contrôle de Redondance cyclique (CRC)  {#contrôle-de-redondance-cyclique-crc .unnumbered}

![](14-Logique/Cours/pandoc/media/image143.emf){width="3.1958333333333333in"
height="0.6173611111111111in"}La méthode de détection d'erreurs appelée
CRC (Cyclic Redundancy Check) permet de détecter plus d'erreurs que le
contrôle de parité. Elle nécessite l'ajout de bits redondants r~0~ à
r~k~, calculés à partir des données a~0~ à a~n~. Les polynômes CRC ou
FCS qui utilisent les bits r~0~ à r~k~ sont établis à partir de normes.

[Exemple :]{.underline} 3 octets à transmettre

1 1 0 0 1 1 0 0

\+ 1 0 1 1 0 0 1 0

\+ 0 1 0 0 1 1 0 1

0 0 1 1 0 0 1 1

On fait une addition binaire Modulo 2 entre chaque bit sans retenue.

Par contrôle polynomial (par abus de langage CRC=Cyclic Redundancy
Check) :

  -------- -------- -------- ------- ------- ------- ------- ------- -------
  a~n-1~   a~n-2~   a~n-3~   ...     ...     ...     ...     a~1~    a~0~

  -------- -------- -------- ------- ------- ------- ------- ------- -------

On considère la trame à transmettre comme un groupe de bits. On lui
associe un polynôme P(X) tel que le coefficient de degré i corresponde à
la valeur du i^ème^ bit.

$$P(X) = \sum_{k = 0}^{n - 1}{a_{k}.X^{k}}$$

On choisit un polynôme appelé polynôme générateur G(X) de degré « r »
ayant des propriétés spécifiques.

On calcule X^r^\*P(X) et on le divise par G(X). Le reste de cette
division polynomiale est un autre polynôme noté R(X).

On transmet :

  -------- -------- -------- ------- ------- ------- ------- ------- ------- -------
  a~n-1~   a~n-2~   a~n-3~   ...     a~1~    a~0~    r~k~    ...     r~1~    r~0~

  -------- -------- -------- ------- ------- ------- ------- ------- ------- -------

A la réception, on vérifie que le reste de la division par G(X) est nul.

[Exemple :]{.underline}

+--------+-------------------------------------------------------------+
| > ![]  | **Exemples**                                                |
| (14-Lo |                                                             |
| gique/ | Soit la séquence 1001 à envoyer ;                           |
| Cours/ |                                                             |
| pandoc | Le polynôme P(X) vaut donc X^3^+1;                          |
| /media |                                                             |
| /image | Si le polynôme générateur est G(X)=X^3^+X+1, le degré de    |
| 10.png | G(x) est r=3;                                               |
| ){widt |                                                             |
| h="0.6 | Par conséquent P(X).X^3^ vaut X^6^+X                        |
| 262696 |                                                             |
| 850393 |                                                             |
| 701in" |                                                             |
| >      |                                                             |
| height |                                                             |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

#####  {#section-3 .unnumbered}

##### Accusé de réception {#accusé-de-réception .unnumbered}

La détection d'erreur suivie d'une retransmission est la solution la
plus utilisée dans les réseaux informatiques.

Des mécanismes d'accusés de réception (ACKnowledge acquittements) sous
la forme de blocs de données spéciaux permettent de confirmer à
l'émetteur que les données transmises sont bien arrivées sans erreur.

##### Notion de taux d'erreurs {#notion-de-taux-derreurs .unnumbered}

Dans la pratique, on mesure la qualité d'une liaison numérique (qualité
de transmission) par le taux d'erreur appelée BER (Bit Error Rate), il
est donné par le nombre de bits erronés rapporté au nombre total de bit
transmis.

Le taux d'erreurs varie en pratique de 10^-4^ (ligne téléphonique) à
10^-9^ (réseaux locaux).

Le taux d'erreurs est devenu très satisfaisant descendant souvent sous
la barre des 10^-9^ : cela provient de techniques de codage plus
performantes et de l'utilisation de support de transmission de très
bonnes qualités comme la fibre optique

###  Topologie des réseaux

La **topologie c'est l'organisation physique d'un réseau**. Pour
résumer, elle permet de savoir comment sont raccordés tous les éléments
pouvant communiquer entre eux ?

![etoile](14-Logique/Cours/pandoc/media/image144.jpeg){width="1.825in"
height="1.6111111111111112in"}

**Topologie en étoile**

C'est la topologie la plus courante. Toutes les stations sont reliées à
un unique composant central : le concentrateur (hub). Quand une station
émet vers le concentrateur (qui peut être un switch ou un hub), celui-ci
envoie les données à celle qui en est le destinataire (switch) ou à
toutes les autres machines (hub).

> **Avantages / Inconvénients**
>
> Ce type de réseau est facile à mettre en place et à surveiller. La
> panne d'une station ne met pas en cause l'ensemble du réseau. Par
> contre, il faut plus de câbles que pour les autres topologies, et si
> le concentrateur tombe en panne, tout le réseau est hors d'état de
> fonctionner. De plus, le débit utile de circulation de données est
> moins bon que pour les autres topologies.

![anneau](14-Logique/Cours/pandoc/media/image145.png){width="1.8736111111111111in"
height="1.8736111111111111in"}\
**Topologie en anneau**

Développée par IBM, cette architecture est principalement utilisée par
les réseaux Token-Ring 1. Elle utilise la technique d'accès par "jeton".
Les informations circulent de station en\
station, en suivant l'anneau. Un jeton circule autour de l'anneau. La
station qui a le jeton émet des données qui font le tour de l'anneau.
Lorsque les données reviennent, la station qui les a envoyées les
élimine du réseau et passe le jeton à son voisin, et ainsi de suite\...

> **Avantages / Inconvénients**
>
> Cette topologie permet d'avoir un débit proche de 90% de la bande
> passante (capacité à transporter un type d'information dans un canal).
> De plus, le signal qui circule est régénéré par chaque station. En
> réalité les ordinateurs d'un réseau en anneau ne sont pas reliés en
> boucle, mais sont reliés à un répartiteur (appelé MAU, Multistation
> Access Unit) qui va gérer la communication entre les ordinateurs qui
> lui sont reliés en impartissant à chacun d'entre eux un temps de
> parole.

##### Topologie en bus {#topologie-en-bus .unnumbered}

![bus](14-Logique/Cours/pandoc/media/image146.png){width="2.0909722222222222in"
height="0.7479166666666667in"}Le bus est un segment central où circulent
les informations. Il s'étend sur toute la longueur du réseau et les
machines viennent s'y connecter. Lorsqu'une station émet des données,
elles circulent sur toute la longueur du bus et la station destinatrice
peut les récupérer. Une seule station peut émettre à la fois. En bout de
bus, un "bouchon" permet de supprimer définitivement les informations
pour qu'une autre station puisse émettre.

> **Avantages / Inconvénients**
>
> L'avantage du bus réside dans la simplicité de sa mise en œuvre. Par
> contre, en cas de rupture de la structure bus, le réseau devient
> inutilisable. Notons également que le signal n'est jamais régénéré, ce
> qui limite la longueur des câbles (car plus un signal électrique
> parcours un câble métallique, plus son amplitude diminue).

##### ![maillee](14-Logique/Cours/pandoc/media/image147.png){width="1.9222222222222223in" height="1.7173611111111111in"}Topologie maillée {#mailleetopologie-maillée .unnumbered}

La topologie maillée (c.f. Figure 3.4) est une évolution de la topologie
en étoile. Très utilisée dans les très grands réseaux, elle permet
d'offrir des chemins différents pour relier\
deux points, ce qui évite les problèmes en cas de rupture d'une liaison.

> **Avantages / Inconvénients**
>
> L'avantage de la structure maillée est que la topologie est robuste et
> sûre. Par contre, les coûts de mise en place sont importants.

### Types de liaisons des réseaux de communication

Au sein d'un réseau local, on distingue deux modes de fonctionnement
(c.f. Figure 3.5) :\
• Liaison client-serveur (server based network) : elle désigne un mode
de communication\
à travers un réseau entre un client (logiciel implémenté sur un
ordinateur) qui envoie\
des requêtes 2, et un serveur qui attend les requêtes et y répond ;\
• Liaison point à point (peer to peer) : Ce mode est adapté pour les
liaisons simples\
qui transportent des données entre deux matériels homologues. Cette
liaison permet un\
fonctionnement bidirectionnel simultané.

![](14-Logique/Cours/pandoc/media/image148.png){width="3.971836176727909in"
height="2.097024278215223in"}

### Architecture de la chaîne de transmission

![](14-Logique/Cours/pandoc/media/image149.emf){width="5.983333333333333in"
height="2.2583333333333333in"}

La **source** est l'équipement qui génère les données à transmettre
(Ordinateur, ...)

L'**émetteur** reçoit en entrée la suite de données binaires ou un
signal analogique et fournit en sortie un signal dont les
caractéristiques sont adaptées au support de transmission (adaptation en
tension, courant, optique...)

Le **récepteur** réalise la fonction inverse pour donner le message au
**destinataire**.

Pour une transmission sur une voie de communication entre deux machines,
la communication peut s\'effectuer de différentes manières. La
transmission est caractérisée par :

-   le modes de transmission

-   le sens des échanges

-   la synchronisation : synchrone ou asynchrone

-   le protocole de communication utilisé

> ![](14-Logique/Cours/pandoc/media/image8.png){width="5.898148512685914in"
> height="2.75in"}

### Caractéristiques de la transmission

Pour une transmission sur une voie de communication entre deux machines,
la communication peut s\'effectuer de différentes manières. La
transmission est caractérisée par :

-   le **sens des échanges**;

![](14-Logique/Cours/pandoc/media/image150.jpeg){width="2.7395833333333335in"
height="1.8034722222222221in"}Pour une transmission entre deux points,
la plupart du temps, il faut traiter un dialogue et non un monologue. Il
faut donc une convention pour fixer le sens de la transmission.

-   Dans un seul sens : liaison **simplex**

-   Dans les deux sens non simultanément : liaison **half duplex**

-   Dans les deux sens simultanément : liaison **full duplex** ou
    **duplex intégral**

![undefined](14-Logique/Cours/pandoc/media/image151.png){width="3.1791666666666667in"
height="2.828236001749781in"}

-   le mode de transmission : **série ou parallèle**;

    -   Lors d'une liaison parallèle, chaque BIT est transmis sur un
        fil, (rapide mais consommateur de fil)

    -   Pour une liaison série, les bits sont transmis les uns après les
        autres, (lent mais moins consommateur de fils).

-   la synchronisation : **synchrone ou asynchrone**.

> **Liaison asynchrone** : Chaque caractère est émis de façon
> irrégulière dans le temps Imaginons qu\'un seul bit soit transmis
> pendant une longue période de silence. Le récepteur ne pourrait savoir
> s\'il s\'agit de 00010000, ou 10000000 ou encore 00000100\...
>
> ![RS-232 is Simple, Robust Communications
> Method](14-Logique/Cours/pandoc/media/image152.jpeg){width="3.6944444444444446in"
> height="1.3855096237970255in"}**Liaison synchrone** : Emetteur et
> Récepteur sont cadencés à la même horloge (CLK). Le récepteur reçoit
> de façon continue les informations au rythme où l\'émetteur les
> envoie.

### Protocoles des réseaux de communication

Les réseaux utilisent une architecture en couches, dans laquelle la
communication entre\
les appareils obéit à des règles précises définies par des protocoles de
communication. Les\
informations pouvant être altérées durant le transport, il faut
superviser la circulation des\
données. Le protocole spécifie le format des unités de données
échangées, leur délimitation, les moyens de contrôler leur validité
ainsi que le mode de correction des erreurs détectées.

Les données sont encapsulées, puis scindées en paquets. La petite taille
des paquets permet de réduire le délai global d'acheminement des
messages. Ces paquets sont ensuite adaptés au type d'appareil avec
lequel on veut communiquer, on appelle alors cet élément une trame.
Cette trame est finalement convertie en un signal physique adapté au
support de communication (câble métallique, air, fibre optique). Voici
un exemple d'encapsulation de données, qui donne une trame.

![](14-Logique/Cours/pandoc/media/image153.png){width="6.901388888888889in"
height="0.8701388888888889in"}

Un protocole est donc un ensemble de règles régissant les échanges de
données entre\
équipements informatiques. Pour qu'un message soit correctement reçu et
interprété il faut respecter quelques règles :

\- s'adresser au bon destinataire, (adresse)

\- lui indiquer que la communication débute, (bit de start)

\- parler la même « langue » etc\... (même débit, même codage,...)

En format simplifié, cela donnerait :

  ------------- ------------------------------------- ----------------------
  **En-tête**   **Données applicatives**              **Terminateur**

  ------------- ------------------------------------- ----------------------

Ce qui est vrai pour nous l'est également pour les machines. Une
information ne sera donc jamais envoyée seule mais sera toujours
précédée et terminée par des données (binaires) dites « de service ».
Celles qui précédent l'information à transmettre (donnée(s)
applicative(s)) constituent l'en-tête, celles qui la suivent
correspondent au terminateur.

Définir un protocole de liaison de données consiste notamment à préciser
:

-   le format des trames (nombre de bit total d'une trame);

-   le critère de début et de fin de trame;

-   la place et la signification des différents champs dans une trame;

-   la technique de détection d'erreur utilisée;

-   les règles de dialogue : procédure après détection d'erreur, règle
    de priorité, ...

##### Codage {#codage .unnumbered}

![](14-Logique/Cours/pandoc/media/image154.jpeg){width="4.125694444444444in"
height="2.2944444444444443in"}**Code de MANCHESTER** : Il introduit une
transition au milieu de chaque intervalle.

Il consiste en fait à faire un OU exclusif entre le signal et le signal
d\'horloge. Ce qui se traduit par un front montant lorsque le bit est à
zéro, un front descendant dans le cas contraire.

On envoie les bits en série à chaque front montant de l'horloge.

**Code de MILLER** : Identique au code de MANCHESTER, à ceci près
qu\'une transition apparaît au milieu de l\'intervalle alternativement
uniquement lorsque le bit est à 1. De plus, pour éviter les longues
suites de 0 posant toujours un problème lors de la synchronisation à la
réception, si un bit 0 est suivi d'un autre 0, on rajoute une transition
à la fin du temps d'horloge.

![](14-Logique/Cours/pandoc/media/image155.png){width="4.532622484689414in"
height="1.2938648293963255in"}

![bipolaire](14-Logique/Cours/pandoc/media/image156.png){width="2.595138888888889in"
height="2.0652777777777778in"}**Code bipolaire simple** : Codage sur
trois niveaux.

Il propose trois états de la grandeur transportée sur le support
physique :

-   La valeur 0 lorsque le bit est à 0

-   Alternativement +X et -X lorsque le bit est à 1

+--------+-------------------------------------------------------------+
| > ![]  | **Clavier de PC**                                           |
| (14-Lo |                                                             |
| gique/ | > Lorsqu'un clavier émet un code vers un PC il se comporte  |
| Cours/ | > en **émetteur** et le PC en **récepteur**.                |
| pandoc |                                                             |
| /media | ![](14-Logique/C                                            |
| /image | ours/pandoc/media/image157.png){width="5.897916666666666in" |
| 10.png | height="4.0368055555555555in"}                              |
| ){widt |                                                             |
| h="0.6 | 1.  **Mode de transmission** : série point à point          |
| 262696 |                                                             |
| 850393 | 2.  **Synchronisation** : synchrone sur front descendant    |
| 701in" |                                                             |
| >      | 3.  **Codage** : « 1 » : 5 V , « 0 » : 0V                   |
| height |                                                             |
| ="0.65 | 4.  **Format de la** **trame**                              |
| 083333 |                                                             |
| 333333 | <table>                                                     |
| 34in"} | <colgroup>                                                  |
|        | <col style="width: 12%" />                                  |
|        | <col style="width: 4%" />                                   |
|        | <col style="width: 2%" />                                   |
|        | <col style="width: 4%" />                                   |
|        | <col style="width: 1%" />                                   |
|        | <col style="width: 7%" />                                   |
|        | <col style="width: 7%" />                                   |
|        | <col style="width: 7%" />                                   |
|        | <col style="width: 7%" />                                   |
|        | <col style="width: 0%" />                                   |
|        | <col style="width: 6%" />                                   |
|        | <col style="width: 7%" />                                   |
|        | <col style="width: 16%" />                                  |
|        | <col style="width: 15%" />                                  |
|        | </colgroup>                                                 |
|        | <tbody>                                                     |
|        | <tr class="odd">                                            |
|        | <td><strong>En-tête</strong></td>                           |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td colspan="6"><strong>Données                             |
|        | applicatives</strong></td>                                  |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td colspan="2"><blockquote>                                |
|        | <p><strong>Terminateur</strong></p>                         |
|        | </blockquote></td>                                          |
|        | </tr>                                                       |
|        | <tr class="even">                                           |
|        | <td>Start</td>                                              |
|        | <td></td>                                                   |
|        | <td colspan="10">Données ‘Code IBM du caractère’</td>       |
|        | <td><blockquote>                                            |
|        | <p>Parité</p>                                               |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>Stop</p>                                                 |
|        | </blockquote></td>                                          |
|        | </tr>                                                       |
|        | <tr class="odd">                                            |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>b0</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>b1</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>b2</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b3</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b4</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b5</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td>b6</td>                                                 |
|        | <td><blockquote>                                            |
|        | <p>b7</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | <tr class="even">                                           |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | <tr class="odd">                                            |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | </tbody>                                                    |
|        | </table>                                                    |
|        |                                                             |
|        | **Donner le débit de transmission et le temps bit**         |
|        |                                                             |
|        | $T_{b} = 100\ \mu s$ $D_{b} = \frac{1}{T_{b}} = 10\ kbit/s$ |
|        |                                                             |
|        | **Décoder la trame**                                        |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image158.png){width="5.897916666666666in" |
|        | height="1.2in"}                                             |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image159.png){width="5.897916666666666in" |
|        | height="0.4907403762029746in"}                              |
+========+=============================================================+
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **Communication RS232**                                     |
| (14-Lo |                                                             |
| gique/ | ![](14-Logique/Cou                                          |
| Cours/ | rs/pandoc/media/image160.jpeg){width="3.3715277777777777in" |
| pandoc | height="2.6078707349081367in"}                              |
| /media |                                                             |
| /image | 1.  **Mode de transmission** : série point à point          |
| 10.png |                                                             |
| ){widt | 2.  **Synchronisation** : asynchrone avec un débit de 9600  |
| h="0.6 |     bits/s                                                  |
| 262696 |                                                             |
| 850393 | 3.  **Codage** : « 0 » : 12 V , « 1 » : -12V                |
| 701in" |                                                             |
| >      | 4.  **Format de la** **trame**                              |
| height |                                                             |
| ="0.65 | <table style="width:100%;">                                 |
| 083333 | <colgroup>                                                  |
| 333333 | <col style="width: 26%" />                                  |
| 34in"} | <col style="width: 6%" />                                   |
|        | <col style="width: 8%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 9%" />                                   |
|        | <col style="width: 8%" />                                   |
|        | <col style="width: 0%" />                                   |
|        | </colgroup>                                                 |
|        | <tbody>                                                     |
|        | <tr class="odd">                                            |
|        | <td colspan="2" rowspan="2"><strong>Début de la             |
|        | trame</strong></td>                                         |
|        | <td><blockquote>                                            |
|        | <p>Start</p>                                                |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b0</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b1</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b2</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b3</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b4</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b5</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b6</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b7</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>Bit de</p>                                               |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>Bit</p>                                                  |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | <tr class="even">                                           |
|        | <td><blockquote>                                            |
|        | <p>bit</p>                                                  |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>parité</p>                                               |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>de</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | <tr class="odd">                                            |
|        | <td><strong>du message</strong></td>                        |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>stop</p>                                                 |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | </tbody>                                                    |
|        | </table>                                                    |
|        |                                                             |
|        | **Donner le temps bit**                                     |
|        |                                                             |
|        | $T_{b} = \frac{1}{D_{b}} = 104\ \mu s$                      |
|        |                                                             |
|        | **Décoder la trame**                                        |
+========+=============================================================+
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **Liaison MODBUS**                                          |
| (14-Lo |                                                             |
| gique/ | **Liaison multipoints (Réseau) : Bus de terrain Modbus**    |
| Cours/ |                                                             |
| pandoc | Dès qu\'un système (voiture, avion, réseau téléphonique...) |
| /media | atteint un certain niveau de complexité, **l\'approche      |
| /image | point-à-point devient impossible** du fait de l\'immense    |
| 10.png | quantité de câblage à installer et de son coût (en masse,   |
| ){widt | matériaux, main d\'œuvre).                                  |
| h="0.6 |                                                             |
| 262696 | **Présentation**                                            |
| 850393 |                                                             |
| 701in" | On représente ci-dessous un exemple de **réseau             |
| >      | industriel** mettant en œuvre différents **protocoles\***   |
| height | de communication (liaison RS232, liaison RS485, MODBUS,     |
| ="0.65 | Ethernet).                                                  |
| 083333 |                                                             |
| 333333 | ![](14-Logique/Co                                           |
| 34in"} | urs/pandoc/media/image161.jpeg){width="5.837187226596676in" |
|        | height="2.6in"}                                             |
|        |                                                             |
|        | > **Notes**                                                 |
|        | >                                                           |
|        | > PLC\* (Programmable Logic Controller) = API               |
|        | >                                                           |
|        | > Loop controller\* = Régulateur                            |
|        | >                                                           |
|        | > Gateway = passerelle                                      |
|        | >                                                           |
|        | > L'étude qui suit se limite aux échanges entre le **PLC**  |
|        | > (maître MODBUS) et les trois loop controllers (esclaves   |
|        | > MODBUS). Le protocole **Modbus** est limité à son mode    |
|        | > **ASCII asynchrone.**                                     |
|        | >                                                           |
|        | > **Dans le mode ASCII asynchrone, le format des trames est |
|        | > le suivant :**                                            |
|        |                                                             |
|        | +-------+----------+----------+---------+------+-----+---+  |
|        | | **En  | *        | > **Code | > **Do  | **L  | **Q |   |  |
|        | | t     | *Adresse | > fo     | nnées** | RC** | ueu |   |  |
|        | | ête** | du**     | nction** |         |      | e** |   |  |
|        | |       |          |          |         |      |     |   |  |
|        | |       | **destin |          |         |      |     |   |  |
|        | |       | ataire** |          |         |      |     |   |  |
|        | +-------+----------+----------+---------+------+-----+---+  |
|        | |       |          |          |         |      |     |   |  |
|        | +-------+----------+----------+---------+------+-----+---+  |
|        | | **:** | > 2      | > 2      | > N\*2  | > 2  | >   |   |  |
|        | |       | > ca     | > ca     | >       | > ca |  CR |   |  |
|        | |       | ractères | ractères | > car   | ract | >   |   |  |
|        | |       |          |          | actères | ères | >   |   |  |
|        | |       |          |          |         |      |  LF |   |  |
|        | +-------+----------+----------+---------+------+-----+---+  |
|        |                                                             |
|        | ![](14-Logique/Cou                                          |
|        | rs/pandoc/media/image162.jpeg){width="3.4256944444444444in" |
|        | height="0.5354166666666667in"}                              |
|        |                                                             |
|        | **Décodage partiel d'une trame MODBUS**                     |
|        |                                                             |
|        | > Dans une transmission asynchrone **type RS232**, le       |
|        | > récepteur se synchronise à **chaque** **caractère**       |
|        | > transmis lors du front montant du bit de start.           |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image163.png){width="5.104166666666667in" |
|        | height="0.7708333333333334in"}                              |
|        |                                                             |
|        | La transmission étant configurable, elle est paramétrée ici |
|        | avec :                                                      |
|        |                                                             |
|        | -   **8 bits de donnée** (bit0 à bit7) (Exemple : si        |
|        |     > b7b6b5b4b3b2b1b0 = 01000111, le caractère transmis    |
|        |     > est G).                                               |
|        |                                                             |
|        | -   **parité paire** (dans l'exemple précédent, le bit de   |
|        |     parité est à zéro).                                     |
|        |                                                             |
|        | -   **1 bit de stop**                                       |
|        |                                                             |
|        | > Le signal ci-dessous contient **deux** caractères ASCII.  |
|        |                                                             |
|        | ![](14-Logique/Co                                           |
|        | urs/pandoc/media/image164.jpeg){width="5.604166666666667in" |
|        | height="1.1027777777777779in"}                              |
|        |                                                             |
|        | **Décodez le signal ci-dessus en utilisant les tableaux et  |
|        | précisez la position des deux caractères ASCII dans la      |
|        | trame Modbus.**                                             |
|        |                                                             |
|        | <table style="width:100%;">                                 |
|        | <colgroup>                                                  |
|        | <col style="width: 10%" />                                  |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 12%" />                                  |
|        | <col style="width: 8%" />                                   |
|        | <col style="width: 2%" />                                   |
|        | <col style="width: 11%" />                                  |
|        | <col style="width: 10%" />                                  |
|        | </colgroup>                                                 |
|        | <tbody>                                                     |
|        | <tr class="odd">                                            |
|        | <td colspan="9"><blockquote>                                |
|        | <p><u>Trame du premier caractère</u></p>                    |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | <tr class="even">                                           |
|        | <td><blockquote>                                            |
|        | <p>Start</p>                                                |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td colspan="6"><blockquote>                                |
|        | <p>Caractère</p>                                            |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>parité</p>                                               |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>stop</p>                                                 |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | <tr class="odd">                                            |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>b7</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b6</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b5</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b4</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b3</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b2</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b1</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b0</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>Hexa</p>                                                 |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>ASCII</p>                                                |
|        | </blockquote></td>                                          |
|        | </tr>                                                       |
|        | <tr class="even">                                           |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | </tbody>                                                    |
|        | </table>                                                    |
|        |                                                             |
|        | <table>                                                     |
|        | <colgroup>                                                  |
|        | <col style="width: 10%" />                                  |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 4%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 12%" />                                  |
|        | <col style="width: 9%" />                                   |
|        | <col style="width: 2%" />                                   |
|        | <col style="width: 11%" />                                  |
|        | <col style="width: 11%" />                                  |
|        | </colgroup>                                                 |
|        | <tbody>                                                     |
|        | <tr class="odd">                                            |
|        | <td colspan="10">Trame du deuxième caractère</td>           |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | <tr class="even">                                           |
|        | <td><blockquote>                                            |
|        | <p>Start</p>                                                |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td colspan="5">Caractère</td>                              |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>parité</p>                                               |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>stop</p>                                                 |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | <tr class="odd">                                            |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>b7</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b6</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b5</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b4</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>b3</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td>b2</td>                                                 |
|        | <td>b1</td>                                                 |
|        | <td><blockquote>                                            |
|        | <p>b0</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>Hexa</p>                                                 |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>ASCII</p>                                                |
|        | </blockquote></td>                                          |
|        | </tr>                                                       |
|        | <tr class="even">                                           |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | <td></td>                                                   |
|        | </tr>                                                       |
|        | </tbody>                                                    |
|        | </table>                                                    |
|        |                                                             |
|        | > Position des deux caractères ASCII :                      |
|        | >                                                           |
|        |  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
|        |                                                             |
|        | **Décodage d'une transaction**                              |
|        |                                                             |
|        | > La trame ci-dessous a été relevée lors d'une question     |
|        | > transmise par le **PLC (API)** à un des contrôleurs de    |
|        | > boucle (Loop controller).                                 |
|        |                                                             |
|        | ![](14-Logique/Cou                                          |
|        | rs/pandoc/media/image165.jpeg){width="5.9631944444444445in" |
|        | height="3.2666666666666666in"}                              |
|        |                                                             |
|        | **Donnez l'adresse de l'esclave (contrôleur de boucle)      |
|        | destinataire de cette trame.**                              |
|        |                                                             |
|        | [Extrait du protocole MODBUS]{.underline}                   |
|        |                                                             |
|        | +------+----+-------------------+---------------------+     |
|        | |      | >  | > **Fonction      | > **Contenu** **du  |     |
|        | |      | ** | > réalisée**      | > champ des         |     |
|        | |      | Co |                   | > données**         |     |
|        | |      | de |                   |                     |     |
|        | |      | ** |                   |                     |     |
|        | +------+----+-------------------+---------------------+     |
|        | |      | >  | > Lecture de n    | > Adresse du        |     |
|        | |      | \$ | > mots            | > premier mot à     |     |
|        | |      | 04 | > consécutifs de  | > lire (4           |     |
|        | |      |    | > 6 bits          | > caractères) et    |     |
|        | |      |    |                   | > nombre de mots (4 |     |
|        | |      |    |                   | > caractères)       |     |
|        | +------+----+-------------------+---------------------+     |
|        |                                                             |
|        | **Donnez l'adresse où commencera la lecture dans la mémoire |
|        | de l'esclave et le nombre de mots lus par le maitre.**      |
|        |                                                             |
|        | [Complément : trame renvoyée par l'esclave en réponse à     |
|        | cette question]{.underline}                                 |
|        |                                                             |
|        | ![](14-Logique/Cou                                          |
|        | rs/pandoc/media/image167.jpeg){width="0.7708333333333334in" |
|        | height="0.625in"}                                           |
|        |                                                             |
|        | +-------------------------------+-----------------------+   |
|        | | > **Esclave N°\_\_**          |                       |   |
|        | +-------------------------------+-----------------------+   |
|        | | > **Adresse**                 | **Donnée**            |   |
|        | +-------------------------------+-----------------------+   |
|        | | > **?**                       | **9C**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **EE**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **42**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **81**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **64**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **58**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **62**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **D2**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **5A**                |   |
|        | +-------------------------------+-----------------------+   |
|        | |                               | **D2**                |   |
|        | +-------------------------------+-----------------------+   |
|        |                                                             |
|        | <table style="width:100%;">                                 |
|        | <colgroup>                                                  |
|        | <col style="width: 12%" />                                  |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 6%" />                                   |
|        | <col style="width: 7%" />                                   |
|        | <col style="width: 0%" />                                   |
|        | <col style="width: 8%" />                                   |
|        | <col style="width: 9%" />                                   |
|        | <col style="width: 8%" />                                   |
|        | <col style="width: 8%" />                                   |
|        | <col style="width: 9%" />                                   |
|        | <col style="width: 5%" />                                   |
|        | <col style="width: 6%" />                                   |
|        | <col style="width: 6%" />                                   |
|        | </colgroup>                                                 |
|        | <tbody>                                                     |
|        | <tr class="odd">                                            |
|        | <td></td>                                                   |
|        | <td>:</td>                                                  |
|        | <td>01</td>                                                 |
|        | <td>04</td>                                                 |
|        | <td><blockquote>                                            |
|        | <p>0A</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td></td>                                                   |
|        | <td><blockquote>                                            |
|        | <p>9CEE</p>                                                 |
|        | </blockquote></td>                                          |
|        | <td>4281</td>                                               |
|        | <td>6458</td>                                               |
|        | <td><blockquote>                                            |
|        | <p>62D2</p>                                                 |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>5AD2</p>                                                 |
|        | </blockquote></td>                                          |
|        | <td>88</td>                                                 |
|        | <td><blockquote>                                            |
|        | <p>CR</p>                                                   |
|        | </blockquote></td>                                          |
|        | <td><blockquote>                                            |
|        | <p>LF</p>                                                   |
|        | </blockquote></td>                                          |
|        | </tr>                                                       |
|        | </tbody>                                                    |
|        | </table>                                                    |
|        |                                                             |
|        | Cette trame est une réponse positive de l'esclave numéro    |
|        | \_\_\_\_\_\_ à une demande de lecture (fonction \$04) de    |
|        | **cinq** mots consécutifs situés à partir de l'adresse      |
|        | \_\_\_\_\_\_\_                                              |
|        |                                                             |
|        | Le champ données contient le nombre d'octets utiles (ici    |
|        | 10) ainsi que la valeur des mots envoyés par l'esclave      |
|        | (\$9CEE, \$4281, \$6458, \$62D2, \$5AD2). Le LRC est \$88   |
+========+=============================================================+
|        |                                                             |
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **Objectif d'appareil photo**                               |
| (14-Lo |                                                             |
| gique/ | Les objectifs photographiques de la marque Canon sont       |
| Cours/ | reliés aux boitiers via sept connexions permettant la       |
| pandoc | communication entre ces deux parties. Le protocole de       |
| /media | communication utilisé entre le boitier et l'objectif        |
| /image | photographique est de type maitre-esclave et utilise la     |
| 10.png | communication série SPI. Le détail est donné figure 7.      |
| ){widt |                                                             |
| h="0.6 | ![](14-Logique/C                                            |
| 262696 | ours/pandoc/media/image168.png){width="5.897916666666666in" |
| 850393 | height="2.3270833333333334in"}                              |
| 701in" |                                                             |
| >      | Les valeurs sur MISO et MOSI sont interprétées sur les      |
| height | fronts montants du signal d'horloge SCK. Un 0 logique est   |
| ="0.65 | codé par une tension de 0 V et un 1 logique est codé par    |
| 083333 | une tension de 5 V. La transmission se fait octet par       |
| 333333 | octet, le bit de poids fort en premier.                     |
| 34in"} |                                                             |
|        | Lors d'un essai de mise au point, une trame de              |
|        | communication entre le boitier et l'objectif photographique |
|        | a été interceptée. Cette trame, représentée figure A du     |
|        | document réponse, contient la valeur de l'ordre de          |
|        | déplacement demandée par le boitier à l'objectif            |
|        | photographique, codée sur deux octets. L'octet de poids     |
|        | fort est transmis en premier.                               |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image169.png){width="5.897916666666666in" |
|        | height="4.827083333333333in"}                               |
|        |                                                             |
|        | **Indiquer le contenu des deux octets transmis par le       |
|        | boitier sur le tableau A du document réponse.**             |
|        |                                                             |
|        | **Décoder l'ordre de déplacement de la lentille mobile,     |
|        | codé sur un entier signé 16 bits, envoyé à l'objectif       |
|        | photographique. En déduire le déplacement en mm qui a été   |
|        | demandé.**                                                  |
|        |                                                             |
|        | Lors de la demande de déplacement de la lentille mobile, le |
|        | boitier va transmettre à l'objectif photographique une      |
|        | trame de trois octets, via la ligne MOSI : une commande sur |
|        | un octet puis, l'ordre de déplacement codé sur deux octets. |
|        | L'objectif photographique confirme la prise en compte de    |
|        | ces informations en full-duplex via la ligne MISO.          |
|        |                                                             |
|        | Afin que la communication entre le boitier et l'objectif    |
|        | photographique n'ait pas d'impact sur la dynamique du       |
|        | système, il est nécessaire qu'un échange pour la consigne   |
|        | de déplacement entre le boitier et l'objectif               |
|        | photographique soit réalisé en moins de 0,5 ms.             |
|        |                                                             |
|        | **Donner, à partir de la figure A du document réponse et de |
|        | l'explication précédente, le temps de transmission 𝑡com     |
|        | nécessaire pour un échange entre le boitier et l'objectif   |
|        | photographique.**                                           |
+========+=============================================================+
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **RS232 ASCII**                                             |
| (14-Lo |                                                             |
| gique/ | La trame ci-dessous est transmise au PC par la carte SSI.   |
| Cours/ |                                                             |
| pandoc | ![](14-                                                     |
| /media | Logique/Cours/pandoc/media/image170.jpeg){width="4.71875in" |
| /image | height="2.28125in"}                                         |
| 10.png |                                                             |
| ){widt | **Sachant que les informations délivrées par l'oscilloscope |
| h="0.6 | sont des valeurs hexadécimales, identifiez les caractères   |
| 262696 | ASCII transmis. Reconstituez la trame, en binaire, sur le   |
| 850393 | signal (1) ci-dessus.**                                     |
| 701in" |                                                             |
| >      | **Calculez le temps bit et la durée du message.**           |
| height |                                                             |
| ="0.65 | > **Annexe 2 : Table des caractères ASCII**                 |
| 083333 | >                                                           |
| 333333 | > **Utilisation de la table**                               |
| 34in"} |                                                             |
|        | **Exemple : « A » = 41~(16)~**                              |
|        |                                                             |
|        | ![](14-Logique/Co                                           |
|        | urs/pandoc/media/image171.jpeg){width="4.607638888888889in" |
|        | height="2.6530347769028872in"}                              |
+========+=============================================================+
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **BUS CAN - Voiture**                                       |
| (14-Lo |                                                             |
| gique/ | > Dans sa version **basse vitesse** (125kbits/s), le **bus  |
| Cours/ | > CAN** (**C**ontroler **A**rea **N**etwork) est utilisé    |
| pandoc | > dans l'automobile pour relier les **équipements de        |
| /media | > confort** (éclairage, lève-vitre, rétroviseur etc.)       |
| /image | >                                                           |
| 10.png | > ![](14-Logique/C                                          |
| ){widt | ours/pandoc/media/image172.png){width="4.505840988626422in" |
| h="0.6 | > height="2.683333333333333in"}                             |
| 262696 | >                                                           |
| 850393 | > La **figure 1** ci-dessous représente [quatre             |
| 701in" | > équipements]{.underline} : deux moteurs de lève vitre,    |
| >      | > une console de commande et un tableau de bord.            |
| height |                                                             |
| ="0.65 | Ces éléments communiquent par l'intermédiaire d'un bus CAN  |
| 083333 | composé d'un **média de transmission** (fils électriques)   |
| 333333 | et d'unités de contrôle électroniques (**ECU**). Le format  |
| 34in"} | d'une trame CAN est représenté ci-dessous :                 |
|        |                                                             |
|        | ![](14-Logique/Co                                           |
|        | urs/pandoc/media/image173.jpeg){width="7.276388888888889in" |
|        | height="3.3784722222222223in"}                              |
|        |                                                             |
|        | ![](14-Logique/Co                                           |
|        | urs/pandoc/media/image174.jpeg){width="5.908333333333333in" |
|        | height="2.7430555555555554in"}                              |
|        |                                                             |
|        | **Entourez l'en-tête, le terminateur et les données sur le  |
|        | schéma ci-dessus.**                                         |
|        |                                                             |
|        | La tension de l'alternateur (Voltage) peut être déterminée  |
|        | à partir de la relation : Voltage = **k**.Tx                |
|        |                                                             |
|        | **Calculez le coefficient k.**                              |
|        |                                                             |
|        | **Quelle information apparaîtra dans le champ Tx de la      |
|        | trame CAN si le paramètre EngSpeed = 3432 ?**               |
+========+=============================================================+
+--------+-------------------------------------------------------------+

+--------+-------------------------------------------------------------+
| > ![]  | **BUS CAN - Microfraisage**                                 |
| (14-Lo |                                                             |
| gique/ | Le réseau de terrain utilisé par la machine de              |
| Cours/ | microfraisage par électro-érosion est le CAN (Control Area  |
| pandoc | Network), protocole de communication série supportant des   |
| /media | systèmes temps réel avec un haut niveau de fiabilité. Le    |
| /image | BUS CAN est particulièrement adapté pour les environnements |
| 10.png | pollués par les parasites électromagnétiques comme c'est le |
| ){widt | cas pour le système étudié où de nombreux arcs électriques  |
| h="0.6 | sont créés.                                                 |
| 262696 |                                                             |
| 850393 | L'unité de commande (Master Control Unit ou MCU) de la      |
| 701in" | machine à électro-érosion communique en utilisant le        |
| >      | protocole CAN avec :                                        |
| height |                                                             |
| ="0.65 | -- 7 contrôleurs de mouvement MCDC3002 ;                    |
| 083333 |                                                             |
| 333333 | -- 8 modules BIO (Basic Input and Output) CAN.              |
| 34in"} |                                                             |
|        | Le réseau permet de transmettre des consignes (de position, |
|        | de vitesse ou autres) et des informations (vitesses,        |
|        | positions, \...) entre les différents éléments du système.  |
|        |                                                             |
|        | Il est aussi très utile dans les situations d'urgence,      |
|        | comme lorsque les équipements du système sont soumis à des  |
|        | situations critiques (échauffement excessif, surintensité,  |
|        | emballement, \...). Ces équipements doivent avertir tous    |
|        | les autres composants.                                      |
|        |                                                             |
|        | ![](14-Logique/C                                            |
|        | ours/pandoc/media/image175.png){width="5.897916666666666in" |
|        | height="2.1694444444444443in"}Aussi, lors de la mise au     |
|        | point du système, un test de procédure d'urgence est        |
|        | effectué : un contrôleur de mouvement envoie un message     |
|        | d'urgence concernant un défaut grave comme une surintensité |
|        | aux autres équipements. Les trames échangées sont alors     |
|        | relevées sur un oscilloscope (figure 17) et analysées.      |
|        |                                                             |
|        | Pour valider la procédure, le message doit être envoyé en   |
|        | moins de 1 ms et présenter le bon code d'urgence.           |
|        |                                                             |
|        | **Déterminer le nombre de bits nécessaire pour transmettre  |
|        | un message entre l'unité de commande et un contrôleur de    |
|        | mouvement.**                                                |
|        |                                                             |
|        | **À partir de la trame CAN (figure 17 en page 25),          |
|        | déterminer la durée d'un bit ainsi que le débit binaire. En |
|        | déduire la durée de la trame. Conclure quant à l'exigence   |
|        | de durée.**                                                 |
|        |                                                             |
|        | ![](14                                                      |
|        | -Logique/Cours/pandoc/media/image176.png){width="3.59375in" |
|        | height="2.2625in"}                                          |
|        |                                                             |
|        | Le champ de l'identificateur contient 11 bits. La société   |
|        | Faulhaber réserve les 4 premiers bits de poids forts aux    |
|        | fonctions et les 7 autres bits pour l'adresse du nœud       |
|        | (figure 18).                                                |
|        |                                                             |
|        | **Donner le code de la fonction de la trame de la figure 17 |
|        | ainsi que l'adresse du nœud.**                              |
|        |                                                             |
|        | La société Faulhaber précise également que dans le cas d'un |
|        | message d'urgence, l'identificateur admet une valeur en     |
|        | hexadécimal comprise entre 81h et FFh.                      |
|        |                                                             |
|        | **Préciser alors le code en hexadécimal de la fonction      |
|        | Emergency (Urgence). Conclure sur la validité de ce         |
|        | message.**                                                  |
+========+=============================================================+
+--------+-------------------------------------------------------------+

## Sources

Ce cours a été élaboré à l'aide de nombreuses ressources provenant de
différents collègues de l'UPSTI.\

## Exercices du chapitre

![](14-Logique/Cours/pandoc/media/image177.png){width="5.466666666666667in"
height="8.373527996500437in"}

![](14-Logique/Cours/pandoc/media/image178.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**PORTE DE GARAGE**

*([Source]{.underline} : ATS 2004)*

1.  **Mise en situation**

![](14-Logique/Cours/pandoc/media/image180.png){width="2.25in"
height="1.6666666666666667in"}Le thème du sujet est l'étude d'une porte
automatique coulissant. Un usager peut déclencher l'ouverture de la
porte depuis son véhicule par une action sur la télécommande qui lui a
été fournie.

Le synoptique du portail est représenté ci-contre :

*1a et 1b : barrière IR extérieure,*

*2a et 2b : barrière IR intérieure,*

*3 : palpeur,*

![](14-Logique/Cours/pandoc/media/image181.png){width="2.540277777777778in"
height="1.4895833333333333in"}*4a et 4b : capteurs de télécommande,*

*5a et 5b : capteurs de fin de course*

Le moteur et l'armoire électrique de commande ne sont pas représentés.

Pour la sécurité des personnes, le système comporte deux barrières
infra-rouges : l'une à l'intérieur du garage et l'autre à l'extérieur,
ainsi qu'un palpeur qui est un capteur de contact localisé sur toute la
tranche de la porte.

Les signaux logiques issus de ces dispositifs de sécurité sont notés I1,
I2 et PP. Ils valent « 1 » lorsque le système est au repos et « 0 « en
cas d'activation de la sécurité.

L'activation d'une sécurité doit être sans effet sur le système si la
porte est en train de s'ouvrir, par contre si la porte est en train de
se refermer elle doit bien sûr se rouvrir.

Les variables logiques qui commandent la porte sont notées MO, MF et A
pour « marche ouverture », « marche fermeture » et « arrêt ». Ces
variables de commande sont liées à quatre variables de contrôle notées
RX, FC, SO et SC qui sont décrites ci-dessous :

-   RX vaut « 1 » si l'ordre d'ouverture est donné par une
    télécommande ;

-   SO vaut « 1 » si la porte est en train de s'ouvrir ;

-   FC vaut « 1 » si la porte touche un capteur de fin de course ;

-   SC vaut « 0 » si une sécurité est activée.

> ![table_verite](14-Logique/Cours/pandoc/media/image182.jpeg){width="2.2043919510061243in"
> height="2.145997375328084in"}

1.  **Travail demandé**

```{=html}
<!-- -->
```
1.  **Indiquer** pourquoi le palpeur est-il nécessaire en plus des deux
    barrières infra-rouges.

2.  **Donner** l'expression de la variable SC en fonction de I1, I2 et
    PP.

3.  A l'aide de la table de vérité donnée ci-dessus, **déterminer**
    l'expression la plus simple de A, à l'aide d'un tableau de Karnaugh.

4.  **Représenter** sur le document réponse le schéma logique permettant
    d'obtenir A.

5.  A l'aide de la table de vérité, **déterminer** l'expression la plus
    simple de MO, à l'aide d'un tableau de Karnaugh.

6.  **Représenter,** sur le document réponse, le schéma logique
    permettant d'obtenir MO.

![garage](14-Logique/Cours/pandoc/media/image183.jpeg){width="6.666666666666667in"
height="7.03125in"}

![](14-Logique/Cours/pandoc/media/image178.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**COMMANDE DE FEUX TRICOLORES**

Nous proposons de réaliser le décodeur d\'un montage électronique
permettant le fonctionnement des feux tricolores d\'un carrefour routier
comportant 2 voies (voie 1 et 2. voir le dessin du carrefour ci-contre).

Le principe du montage électronique complet est présenté dans le schéma
synoptique ci-dessous :

![toto2](14-Logique/Cours/pandoc/media/image184.jpeg){width="4.166666666666667in"
height="1.8958333333333333in"}[Explication du principe :]{.underline}

\- L\'horloge délivre une impulsion toutes les 2 secondes.

\- Cette impulsion est appliquée à l'entrée d\'horloge d\'un compteur
diviseur par 16.

\- Les 4 sorties (a, b, c, d) du compteur délivrent des signaux logiques
conformes aux chronogrammes qui suivent, et sont appliqués aux entrées
du décodeur (voir chronogrammes).

[Chronogrammes:]{.underline}

![toto](14-Logique/Cours/pandoc/media/image185.jpeg){width="5.3805555555555555in"
height="5.077083333333333in"}

 

1.  A partir des chronogrammes, donner la table de vérité de chaque
    sortie du décodeur en fonction des sorties du compteur.

2.  En déduire les équations de chaque sortie.

![](14-Logique/Cours/pandoc/media/image178.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**PANNE D'UN HYDROPLANEUR**

+---+-------------------------------------------+------------------------+
| ! |                                           | ![](14-Logi            |
| [ |                                           | que/Cours/pandoc/media |
| ] |                                           | /image187.jpeg){width= |
| ( |                                           | "2.4833333333333334in" |
| 1 |                                           | height="               |
| 4 |                                           | 1.7416666666666667in"} |
| - |                                           |                        |
| L |                                           |                        |
| o |                                           |                        |
| g |                                           |                        |
| i |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| e |                                           |                        |
| / |                                           |                        |
| C |                                           |                        |
| o |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| s |                                           |                        |
| / |                                           |                        |
| p |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| d |                                           |                        |
| o |                                           |                        |
| c |                                           |                        |
| / |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| i |                                           |                        |
| a |                                           |                        |
| / |                                           |                        |
| i |                                           |                        |
| m |                                           |                        |
| a |                                           |                        |
| g |                                           |                        |
| e |                                           |                        |
| 1 |                                           |                        |
| 8 |                                           |                        |
| 6 |                                           |                        |
| . |                                           |                        |
| p |                                           |                        |
| n |                                           |                        |
| g |                                           |                        |
| ) |                                           |                        |
| { |                                           |                        |
| w |                                           |                        |
| i |                                           |                        |
| d |                                           |                        |
| t |                                           |                        |
| h |                                           |                        |
| = |                                           |                        |
| " |                                           |                        |
| 4 |                                           |                        |
| . |                                           |                        |
| 8 |                                           |                        |
| 1 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| 6 |                                           |                        |
| i |                                           |                        |
| n |                                           |                        |
| " |                                           |                        |
| h |                                           |                        |
| e |                                           |                        |
| i |                                           |                        |
| g |                                           |                        |
| h |                                           |                        |
| t |                                           |                        |
| = |                                           |                        |
| " |                                           |                        |
| 3 |                                           |                        |
| . |                                           |                        |
| 5 |                                           |                        |
| i |                                           |                        |
| n |                                           |                        |
| " |                                           |                        |
| } |                                           |                        |
+===+===========================================+========================+
| D | ![](14-Logique/Cours/pandoc/media/        |                        |
| a | image188.png){width="2.591666666666667in" |                        |
| n | height="3.5166666666666666in"}            |                        |
| s |                                           |                        |
| l |                                           |                        |
| ' |                                           |                        |
| o |                                           |                        |
| b |                                           |                        |
| j |                                           |                        |
| e |                                           |                        |
| c |                                           |                        |
| t |                                           |                        |
| i |                                           |                        |
| f |                                           |                        |
| d |                                           |                        |
| ' |                                           |                        |
| o |                                           |                        |
| p |                                           |                        |
| t |                                           |                        |
| i |                                           |                        |
| m |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| f |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| c |                                           |                        |
| t |                                           |                        |
| i |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| d |                                           |                        |
| ' |                                           |                        |
| u |                                           |                        |
| n |                                           |                        |
| h |                                           |                        |
| y |                                           |                        |
| d |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| - |                                           |                        |
| p |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| i |                                           |                        |
| l |                                           |                        |
| f |                                           |                        |
| a |                                           |                        |
| u |                                           |                        |
| t |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| i |                                           |                        |
| r |                                           |                        |
| c |                                           |                        |
| o |                                           |                        |
| m |                                           |                        |
| p |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| o |                                           |                        |
| u |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| p |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| c |                                           |                        |
| é |                                           |                        |
| d |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| f |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| c |                                           |                        |
| t |                                           |                        |
| i |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| p |                                           |                        |
| r |                                           |                        |
| é |                                           |                        |
| v |                                           |                        |
| u |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| , |                                           |                        |
| c |                                           |                        |
| o |                                           |                        |
| m |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| c |                                           |                        |
| e |                                           |                        |
| l |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| ' |                                           |                        |
| a |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| c |                                           |                        |
| a |                                           |                        |
| s |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| p |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| m |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| s |                                           |                        |
| i |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| d |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| é |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| , |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| i |                                           |                        |
| i |                                           |                        |
| m |                                           |                        |
| p |                                           |                        |
| o |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| ' |                                           |                        |
| é |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| i |                                           |                        |
| g |                                           |                        |
| n |                                           |                        |
| a |                                           |                        |
| l |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| é |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| p |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| t |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| v |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| i |                                           |                        |
| r |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| p |                                           |                        |
| ê |                                           |                        |
| c |                                           |                        |
| h |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| l |                                           |                        |
| ' |                                           |                        |
| h |                                           |                        |
| y |                                           |                        |
| d |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| - |                                           |                        |
| p |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| . |                                           |                        |
|   |                                           |                        |
| À |                                           |                        |
| c |                                           |                        |
| h |                                           |                        |
| a |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| m |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| é |                                           |                        |
| e |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| f |                                           |                        |
| a |                                           |                        |
| c |                                           |                        |
| e |                                           |                        |
| , |                                           |                        |
| l |                                           |                        |
| ' |                                           |                        |
| h |                                           |                        |
| y |                                           |                        |
| d |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| - |                                           |                        |
| p |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| c |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| c |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| à |                                           |                        |
| u |                                           |                        |
| n |                                           |                        |
| r |                                           |                        |
| é |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| a |                                           |                        |
| u |                                           |                        |
| s |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| f |                                           |                        |
| i |                                           |                        |
| l |                                           |                        |
| ( |                                           |                        |
| I |                                           |                        |
| R |                                           |                        |
| I |                                           |                        |
| D |                                           |                        |
| I |                                           |                        |
| U |                                           |                        |
| M |                                           |                        |
| ) |                                           |                        |
| a |                                           |                        |
| f |                                           |                        |
| i |                                           |                        |
| n |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| d |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| é |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| g |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| é |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| . |                                           |                        |
| L |                                           |                        |
| \ |                                           |                        |
| ' |                                           |                        |
| h |                                           |                        |
| y |                                           |                        |
| d |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| - |                                           |                        |
| p |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| d |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| p |                                           |                        |
| o |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| l |                                           |                        |
| o |                                           |                        |
| g |                                           |                        |
| é |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| d |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| d |                                           |                        |
| é |                                           |                        |
| r |                                           |                        |
| i |                                           |                        |
| v |                                           |                        |
| e |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| d |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| c |                                           |                        |
| h |                                           |                        |
| a |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| e |                                           |                        |
| a |                                           |                        |
| i |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| t |                                           |                        |
| a |                                           |                        |
| b |                                           |                        |
| i |                                           |                        |
| l |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| a |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| . |                                           |                        |
| C |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| o |                                           |                        |
| l |                                           |                        |
| u |                                           |                        |
| t |                                           |                        |
| i |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| i |                                           |                        |
| m |                                           |                        |
| p |                                           |                        |
| l |                                           |                        |
| i |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| e |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| e |                                           |                        |
| , |                                           |                        |
| p |                                           |                        |
| o |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| é |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| f |                                           |                        |
| a |                                           |                        |
| c |                                           |                        |
| e |                                           |                        |
| , |                                           |                        |
| l |                                           |                        |
| ' |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| g |                                           |                        |
| i |                                           |                        |
| n |                                           |                        |
| p |                                           |                        |
| i |                                           |                        |
| v |                                           |                        |
| o |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| l |                                           |                        |
| u |                                           |                        |
| i |                                           |                        |
| - |                                           |                        |
| m |                                           |                        |
| ê |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| ' |                                           |                        |
| u |                                           |                        |
| n |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| a |                                           |                        |
| r |                                           |                        |
| t |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| o |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| p |                                           |                        |
| o |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| f |                                           |                        |
| a |                                           |                        |
| i |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| é |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| g |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| u |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| x |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| d |                                           |                        |
| é |                                           |                        |
| d |                                           |                        |
| i |                                           |                        |
| é |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| a |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| é |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| a |                                           |                        |
| u |                                           |                        |
| I |                                           |                        |
| R |                                           |                        |
| I |                                           |                        |
| D |                                           |                        |
| I |                                           |                        |
| U |                                           |                        |
| M |                                           |                        |
| . |                                           |                        |
| P |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| d |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| c |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| p |                                           |                        |
| h |                                           |                        |
| a |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| , |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| p |                                           |                        |
| o |                                           |                        |
| s |                                           |                        |
| i |                                           |                        |
| t |                                           |                        |
| i |                                           |                        |
| f |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| b |                                           |                        |
| a |                                           |                        |
| s |                                           |                        |
| c |                                           |                        |
| u |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| , |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| i |                                           |                        |
| p |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| c |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| r |                                           |                        |
| ô |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| g |                                           |                        |
| a |                                           |                        |
| g |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| l |                                           |                        |
| ' |                                           |                        |
| h |                                           |                        |
| y |                                           |                        |
| d |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| - |                                           |                        |
| p |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| , |                                           |                        |
| n |                                           |                        |
| ' |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| t |                                           |                        |
| p |                                           |                        |
| a |                                           |                        |
| s |                                           |                        |
| a |                                           |                        |
| c |                                           |                        |
| t |                                           |                        |
| i |                                           |                        |
| f |                                           |                        |
| . |                                           |                        |
|   |                                           |                        |
| E |                                           |                        |
| n |                                           |                        |
| f |                                           |                        |
| i |                                           |                        |
| n |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| c |                                           |                        |
| h |                                           |                        |
| a |                                           |                        |
| r |                                           |                        |
| g |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| b |                                           |                        |
| a |                                           |                        |
| t |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| i |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| o |                                           |                        |
| u |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| c |                                           |                        |
| a |                                           |                        |
| s |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| o |                                           |                        |
| u |                                           |                        |
| c |                                           |                        |
| i |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| c |                                           |                        |
| h |                                           |                        |
| n |                                           |                        |
| i |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| e |                                           |                        |
| , |                                           |                        |
| l |                                           |                        |
| ' |                                           |                        |
| h |                                           |                        |
| y |                                           |                        |
| d |                                           |                        |
| r |                                           |                        |
| o |                                           |                        |
| - |                                           |                        |
| p |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| d |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| p |                                           |                        |
| o |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| d |                                           |                        |
| ' |                                           |                        |
| u |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| b |                                           |                        |
| a |                                           |                        |
| l |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| A |                                           |                        |
| R |                                           |                        |
| G |                                           |                        |
| O |                                           |                        |
| S |                                           |                        |
| ( |                                           |                        |
| d |                                           |                        |
| o |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| l |                                           |                        |
| \ |                                           |                        |
| ' |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| t |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| e |                                           |                        |
| e |                                           |                        |
| s |                                           |                        |
| t |                                           |                        |
| d |                                           |                        |
| a |                                           |                        |
| n |                                           |                        |
| s |                                           |                        |
| l |                                           |                        |
| a |                                           |                        |
| d |                                           |                        |
| é |                                           |                        |
| r |                                           |                        |
| i |                                           |                        |
| v |                                           |                        |
| e |                                           |                        |
| v |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| t |                                           |                        |
| i |                                           |                        |
| c |                                           |                        |
| a |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| ) |                                           |                        |
| q |                                           |                        |
| u |                                           |                        |
| i |                                           |                        |
| p |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| m |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| d |                                           |                        |
| e |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| l |                                           |                        |
| o |                                           |                        |
| c |                                           |                        |
| a |                                           |                        |
| l |                                           |                        |
| i |                                           |                        |
| s |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| t |                                           |                        |
| d |                                           |                        |
| ' |                                           |                        |
| e |                                           |                        |
| n |                                           |                        |
| v |                                           |                        |
| o |                                           |                        |
| y |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| u |                                           |                        |
| n |                                           |                        |
| n |                                           |                        |
| a |                                           |                        |
| v |                                           |                        |
| i |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| p |                                           |                        |
| o |                                           |                        |
| u |                                           |                        |
| r |                                           |                        |
| l |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| é |                                           |                        |
| c |                                           |                        |
| u |                                           |                        |
| p |                                           |                        |
| é |                                           |                        |
| r |                                           |                        |
| e |                                           |                        |
| r |                                           |                        |
| . |                                           |                        |
+---+-------------------------------------------+------------------------+

Dans ce cas de dysfonctionnement, l'hydro-planeur adopte le comportement
décrit par le diagramme d'état ci-dessous :

![](14-Logique/Cours/pandoc/media/image189.jpeg){width="6.571428258967629in"
height="3.6271850393700786in"}

1.  Compléter les chronogrammes qui correspondent à la séquence des
    signaux de commande fournis par l'unité de traitement pour obtenir
    le fonctionnement souhaité dans le cas où la première et la deuxième
    transmission IRIDIUM échouent (lorsqu'un élément doit être activé,
    il sera représenté par un niveau haut).

![](14-Logique/Cours/pandoc/media/image190.png){width="7.268055555555556in"
height="2.0069444444444446in"}![](14-Logique/Cours/pandoc/media/image190.png){width="7.268055555555556in"
height="1.2958333333333334in"}

![](14-Logique/Cours/pandoc/media/image178.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**PORTE DE GARAGE BASCULANTE**

On souhaite qu\'une porte de garage basculante ait le comportement
suivant :

-   la mise en mouvement est réalisée par un moteur à 2 sens de
    rotation, permettant de l'ouvrir ou de la fermer ;

-   le moteur est alimenté par deux contacteurs, l'un pour l'ouverture
    (MO) et l'autre pour la fermeture (MF) ;

-   une fois la porte ouverte ou fermée, le moteur est à l\'arrêt ;

-   en fin d\'ouverture ou de fermeture, lorsque la porte arrive en
    butée, un capteur de courant à effet hall (CS) détecte une
    surintensité moteur ;

-   un boîtier mural comporte deux boutons, l\'un pour la commande
    ouverture (BO), l\'autre pour la fermeture (BF) ;

-   une télécommande possède un seul bouton (Tel). Si la porte est
    ouverte ou en phase d'ouverture, il commande la fermeture ; si elle
    est fermée ou en phase fermeture, il commande l\'ouverture.

-   ![](14-Logique/Cours/pandoc/media/image191.jpeg){width="2.98125in"
    height="1.9722222222222223in"}les commandes d'ouverture ou de
    fermeture sont retenues uniquement si le bouton mural commandant le
    mouvement opposé n'est pas actionné ;

-   on suppose qu\'à la mise en route, la porte est fermée.

Les consignes sont traitées comme des consignes impulsionnelles, sur
front montant.

Nous n\'étudierons pas les cas de mise en défaut : coupure courant ou
arrêt en position semi-ouverte.

1.  Lister et nommer les entrées (IHM et capteur) et sorties (IMH et
    préactionneur).

2.  Lister les états possibles de la porte et les positionner dans un
    diagramme d'état.

3.  Indiquer l\'état initial et l\'éventuel état final.

4.  Compléter le diagramme avec l\'ensemble des transitions possibles.

5.  Compléter le diagramme avec l\'ensemble des activités des différents
    états.

6.  Compléter le chronogramme ci-dessous.

![](14-Logique/Cours/pandoc/media/image178.png){width="1.3555555555555556in"
height="0.3888888888888889in"} 

**LAVE-LINGE ET REVEIL**

On souhaite modéliser le cycle complet d'un lave-linge comportant 5
étapes :

-   Prélavage ;

-   Lavage ;

-   Rinçage ;

-   Essorage ;

-   Arrêt.

On définit les entrées/sorties suivantes :

-   **M** : bouton poussoir « Marche » ;

-   **P** : « Prélavage » sélectionné ;

-   **C** : valeur courante (en minutes) d'un compteur permettant de
    mesurer la durée d'un état et qui est remis à zéro automatiquement
    au début de chaque état.

```{=html}
<!-- -->
```
-   Commande_moteur : égale à 1 si le moteur doit tourner, sinon 0 ;

• Vitesse

I.  Les durées des différentes étapes de lavage sont fixées par le
    constructeur :

-   prélavage : 10 minutes avec le moteur qui tourne à 1000 tr/min;

-   lavage : 30 minutes avec le moteur qui tourne à 1000 tr/min ;

-   rinçage : 10 minutes avec le moteur qui tourne à 1000 tr/min;

-   essorage : 5 minutes avec le moteur qui tourne à 1400 tr/min.

1.  Recenser/définir les variables d'entrées et de sorties.

2.  Recenser, nommer et tracer les états du système.

3.  Tracer les transitions entre les états en fonction du comportement
    séquentiel souhaité ou observé.

4.  Définir les conditions (et évènements) associées à chaque transition
    et les actions associées à chaque état.

5.  Compléter ce graphe d'états afin de pouvoir interrompre le cycle du
    lave-linge quel que soit l'état actif de celui-ci. La variable
    d'entrée associée à la demande d'arrêt est la variable binaire Stop.

    1.  **Réveil**

Considérons un réveil simplifié :

-   On peut mettre l'alarme '*on*' ou '*off*' ;

-   Quand l'heure courante devient égale à l'heure d'alarme, le réveil
    > sonne sans s'arrêter.

-   On peut interrompre la sonnerie.

1.  Dessiner le diagramme d'états correspondant.

2.  Compléter le diagramme d'états précédent pour prendre en compte le
    fait que la sonnerie du réveil s'arrête d'elle-même au bout d'un
    certain temps.

![](14-Logique/Cours/pandoc/media/image178.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![](14-Logique/Cours/pandoc/media/image192.png){width="0.7048611111111112in"
height="0.5163648293963254in"}**BORNE SOLAIRE**

*([Source]{.underline} : ATS 2010)*

1.  **Mise en situation**

> ![](14-Logique/Cours/pandoc/media/image193.png){width="3.1506944444444445in"
> height="2.1840277777777777in"}Le dispositif étudié est un système
> permettant de limiter ou d\'interdire la circulation dans des zones à
> accès réservé. Ce dispositif comporte :

-   un caisson intégrant la partie opérative, à savoir une borne
    > motorisée rétractable dans le sol,

-   un caisson intégrant la partie commande comportant :

> \- une platine électronique de gestion,
>
> \- une batterie d\'alimentation électrique du système,
>
> \- des cellules photovoltaïques assurant la charge de la batterie.
>
> Selon son concept innovant et breveté, le système utilise un module
> solaire pour recharger sa batterie. L\'installation d\'une borne de ce
> type ne nécessite aucune tranchée, aucun raccordement, ni abonnement
> EDF ; son alimentation est gratuite et peut être envisagée sur
> n\'importe quel site.
>
> Cependant, le fonctionnement du système est limité à un nombre de
> cycles dont la valeur dépend des conditions d\'ensoleillement. La
> problématique majeure pour ce système est donc d\'atteindre une
> autonomie suffisante, tout en minimisant le coût et l\'encombrement
> des moyens de production et de stockage de l\'énergie électrique. Le
> panneau, la batterie et la motorisation du système sont reliés grâce à
> un dispositif appelé régulateur de charge, qui est étudier ici.

***Régulateur de charge pour système photovoltaïque*** (Extraits
documentation constructeur)

[A. Présentation générale]{.underline}

Le régulateur de charge est un dispositif électronique au fonctionnement
entièrement automatique. Il relie le panneau photovoltaïque, la batterie
et les équipements destinataires de l'électricité produite.

Sa fonction principale est de contrôler l'état de charge de la batterie.
Il autorise la charge complète de celle-ci en éliminant le risque de
surcharge. Il peut également interrompre l'alimentation des
destinataires pour éviter une décharge profonde. Le régulateur, décrit
ci-dessous, mesure la tension aux bornes de la batterie et assure une
régulation série « tout ou rien ».

![](14-Logique/Cours/pandoc/media/image195.png){width="4.586805555555555in"
height="1.8875in"}[B. Schéma de principe]{.underline}

[C. Principe de fonctionnement]{.underline}

\- Fonctionnement normal : les contacts des relais RC et RD sont fermés.

\- Limitation de charge : Si la tension batterie dépasse la valeur
EB\[max\], le relais RC s'ouvre. Il se referme automatiquement au bout
de 10 minutes, sauf si la tension batterie est devenue inférieure à
EB\[min\] pendant cette durée.

\- Limitation de décharge : Si la tension batterie devient inférieure à
la valeur EB\[min\], le relais RD s'ouvre. Il se referme lorsque la
tension a atteint la valeur EB\[nominal\].

1.  **Étude du fonctionnement du régulateur de charge**

```{=html}
<!-- -->
```
1.  Compléter le **document réponse**, en indiquant l'état des contacts
    RC et RD (état logique « 0 » pour ouvert), selon l'état de charge de
    la batterie.

2.  Toujours sur le **document réponse**, indiquer le sens des
    transferts d'énergie en précisant pour chaque élément, s'il reçoit
    de l'énergie (R), s'il fournit de l'énergie (F), ou s'il n'est pas
    en service (∅).

3.  Représenter le fonctionnement en utilisant le formalisme des graphes
    d'états.

    1.  **Document Réponse**

![](14-Logique/Cours/pandoc/media/image196.png){width="7.2822462817147855in"
height="5.047094269466316in"}

![](14-Logique/Cours/pandoc/media/image178.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**ROBOT MARTIEN SPIRIT**

![Macintosh HD:Users:olivierlegallo:Documents:Dossiers du
bureau:Lycée:TD, colles, devoirs:2014-15:PSI\*:Devoirs:DS6:Spirit:UC
Spirit.tiff](14-Logique/Cours/pandoc/media/image197.png){width="3.570136701662292in"
height="1.8452384076990376in"}

![Macintosh
HD:Users:olivierlegallo:Desktop:Mars_Spirit_Home_Plate.jpg](14-Logique/Cours/pandoc/media/image198.jpeg){width="2.0340277777777778in"
height="1.73125in"}

Le robot SPIRIT a été conçu par la NASA pour étudier la composition
chimique de la surface de la planète Mars. Les principaux composants de
ce robot sont :

-   Un corps, appelé « Warm Electronic Box », dont la fonction est
    > d'assurer la liaison entre les divers composants. Il supporte les
    > batteries qui sont chargées par des capteurs solaires. Il protège
    > également l'électronique embarquée des agressions extérieures.

-   Une tête périscopique orientable dont la fonction est d'orienter le
    > système de vision appelé « Pancam » (Panoramic Camera) qui se
    > trouve à 1,40 m de hauteur. Ce dernier fournit une vue en trois
    > dimensions de l'environnement. Le traitement des images acquises
    > par les caméras du Pancam permet à Spirit de réaliser une
    > cartographie des terrains et donc de trouver de manière autonome
    > son chemin en évitant les obstacles. Cette autonomie de
    > déplacement est renforcée par l'utilisation de quatre caméras de
    > direction situées sur le corps.

-   ![Macintosh
    > HD:Users:olivierlegallo:Desktop:lr2.jpg](14-Logique/Cours/pandoc/media/image199.jpeg){width="3.9743055555555555in"
    > height="2.939583333333333in"}Un bras articulé (image ci-contre),
    > dont la fonction est d'amener un barillet portant quatre outils
    > (une foreuse, un microscope et deux spectromètres) à proximité
    > d'une roche à étudier. L'étude de la roche par ces quatre outils
    > se fait par des carottages horizontaux.

-   Six roues, animées chacune par un motoréducteur, dont la fonction
    > est d'assurer le déplacement de Spirit sur un sol caillouteux. Les
    > deux roues avant et arrière possèdent de plus un moteur de
    > direction permettant au robot d'effectuer des changements de
    > direction jusqu'à un demi-tour sur place.

-   Un système de communication et des antennes haute et basse
    > fréquence, dont la fonction est de permettre à Spirit de
    > communiquer avec la terre.

Le BDD qui suit précise cette structure matérielle.

![Macintosh HD:Users:olivierlegallo:Documents:Dossiers du
bureau:Lycée:TD, colles, devoirs:2014-15:PSI\*:Devoirs:DS6:Spirit:BDD
Spirit.tiff](14-Logique/Cours/pandoc/media/image200.png){width="6.96875in"
height="9.96111111111111in"}

On s'intéresse ici uniquement à la phase de prospection. Comme précisé
précédemment, l'analyse est réalisée grâce à quatre outils installés sur
un barillet rotatif :

-   La foreuse à lame (notée fo) : elle est utilisée pour obtenir une
    > surface analysable. Afin de supprimer la croûte rocheuse, un trou
    > cylindrique de profondeur minimale est effectué. Un capteur mesure
    > la profondeur de perçage et envoie l'information pt (perçage
    > terminé) lorsque l'objectif est atteint. Le perçage normal se fait
    > à vitesse minimale et effort maximal. L'information fo_r signale
    > que la foreuse est rentrée en position de repos, l'information
    > fo_s signale que la foreuse est sortie, prête à l'emploi.

-   Le microscope optique (noté mi) : il renseigne sur la morphologie de
    > la roche (taille des particules, agencement, texture, etc.).
    > L'électronique signale la fin de l'analyse optique par
    > l'information fin_a. L'information mi_r signale que le microscope
    > est rentré en position repos, l'information mi_s que le microscope
    > est sorti, prêt à l'emploi.

-   L'analyseur APSX (noté ap) : il mène des analyses aux rayons X et α,
    > de manière à déterminer la composition élémentaire de la roche.

-   Le spectromètre de Moessbauer (noté sp) : il permet de détecter la
    > présence de minéraux ferreux et de quantifier la teneur en Fe^2+^
    > et Fe^3+^.

![](14-Logique/Cours/pandoc/media/image201.png){width="6.845138888888889in"
height="3.3256944444444443in"}

Figure 8 : Détail du barillet d'exploration

Initialement, la foreuse se trouve face à la surface à étudier (la
position du barillet est mesurée par un capteur angulaire). Le
déroulement normal d'une phase de prospection est spécifié par le
diagramme d'états page suivante.

La phase de prospection débute lorsque la commande de départ d est
donnée et que le barillet se trouve foreuse face à la surface
(information p0 délivrée par le capteur angulaire).

Le perçage s'effectue alors (à vitesse minimale et effort maximal)
jusqu'à ce que la profondeur voulue soit atteinte (information pt), puis
la foreuse se rétracte et le barillet tourne de 90° (position p90) dans
le sens positif.

Puis viennent les phases d'analyse optique, APSX et spectromètre avec
une rotation de 90° du barillet à chaque fois, jusqu'au retour à la
position initiale du barillet.

Les phases d'analyse ASPX et spectromètre ne sont pas étudiées et donc
les états composites correspondants ne sont pas fournis.

![Macintosh HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image202.png){width="6.182638888888889in"
height="4.757638888888889in"}![Macintosh
HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image203.png){width="4.844444444444444in"
height="3.245833333333333in"}

En pratique, ce fonctionnement normal peut être perturbé par deux
situations :

-   **Pathologie 1- échec de la phase de perçage :** le forage peut
    > échouer si la roche se révèle trop résistante. Dans ce cas, on
    > renonce à l'analyse et le système doit revenir en situation
    > initiale.

-   **Pathologie 2 - échec de la phase d'analyse :** le microscope
    > optique de haute précision a une profondeur de champ très réduite,
    > en conséquence, si l'état de surface à l'issue de la phase de
    > perçage est médiocre, l'analyse optique ne peut pas être menée. Il
    > est alors nécessaire de recommencer la phase de perçage, cette
    > fois à vitesse maximale et effort minimal, ces conditions
    > permettant d'améliorer notablement l'état d'une surface
    > préexistante.

**Questions**

Les réponses sont à apporter sur le document-réponses fourni page
suivante.

**Question 1 :**

Proposer une modification de l'état composite de perçage permettant de :

\- renoncer au perçage si la profondeur attendue n'est pas atteinte au
delà d'une durée maximale t_max ;

\- créer une variable « perçage échoué » telle que :

perçage échoué = 0 si le perçage est réussi

perçage échoué = 1 en cas d'échec.

**Question 2 :**

Modifier le diagramme de prospection en conséquence pour que, dans le
cas d'un échec du perçage, le système revienne en situation initiale.

**Question 3 :**

En fonctionnement normal, l'électronique signale la fin de l'analyse
optique par l'information fin_a. Dans le cas de la pathologie 2, cette
information n'est jamais validée mais le système valide une information
S_imp (surface impropre). Proposer une modification de l'état composite
d'analyse optique permettant de :

\- renoncer à l'analyse optique si l'information S_imp est reçue ;

\- créer une variable « analyse échouée » telle que :

analyse échouée = 0 si l'analyse est réussie

analyse échouée = 1 en cas d'échec.

**Question 4 :**

Poursuivre la modification du diagramme de prospection pour que, dans le
cas d'un échec de l'analyse optique, la phase de perçage soit relancée.

**Question 5 :**

Modifier pour finir l'état composite de perçage de manière à ce que les
conditions de forage correspondent à la façon dont cet état a été
activé : perçage normal (vitesse min, effort max) ou perçage fin
(vitesse max, effort min) s'il s'agit d'améliorer la surface.

![Mars](14-Logique/Cours/pandoc/media/image204.jpeg){width="1.836111111111111in"
height="1.9493055555555556in"}

**DOCUMENT-RÉPONSES**

![Macintosh HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image205.png){width="3.6in"
height="3.154861111111111in"}![Macintosh
HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image206.png){width="3.5770833333333334in"
height="3.1243055555555554in"}

**Q1 Q3**

![Macintosh HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image207.png){width="5.591666666666667in"
height="3.5520833333333335in"}**Q2 et Q4**

![Macintosh HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image208.png){width="4.545138888888889in"
height="3.426388888888889in"}

**Q5**

**CORRECTION**

![Macintosh HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image209.png){width="3.63125in"
height="3.1395833333333334in"}![Macintosh
HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image210.png){width="3.548611111111111in"
height="3.109027777777778in"}

**Q1 Q3**

![Macintosh HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image211.png){width="6.477777777777778in"
height="3.7354166666666666in"}

**Q2 et Q4**

![Macintosh HD:Users:olivierlegallo:Desktop:Sans
titre.tiff](14-Logique/Cours/pandoc/media/image212.png){width="4.361805555555556in"
height="3.404861111111111in"}

**Q5**

![](14-Logique/Cours/pandoc/media/image178.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**Gus : Une révolution dans le
déplacement**

![](14-Logique/Cours/pandoc/media/image213.emf){width="1.125in"
height="2.058333333333333in"}Depuis plus de six ans la société OPUS
TECHNOLOGIES conçoit, met au point et fabrique un fauteuil électrique
particulièrement innovant, appelé GUS, acronyme de **G**yropode
**U**tilitaire et **S**portif (figures 1 et 2).

Ce fauteuil est destiné, aussi bien aux Personnes à Mobilité Réduite
(PMR), qu'aux séniors à la recherche d'une assistance dans les
déplacements du quotidien.

Son design, son principe de fonctionnement basé sur une solution de type
Gyropode et sa maniabilité sont pensés pour modifier le regard de chacun
sur les handicapés en fauteuil roulant et plus généralement le regard
que nous portons sur le handicap (figure 2).

Le diagramme de contexte de la figure 3, présente ainsi le GUS dans son
environnement immédiat.

![](14-Logique/Cours/pandoc/media/image214.emf){width="5.591666666666667in"
height="5.075in"}

***Diagrammes états transitions du fonctionnement du GUS***

Le fonctionnement du GUS commence lors de l'installation de la personne
sur le fauteuil. Cette action déclenche l'événement **ON**.

Il se termine lorsque la personne quitte le fauteuil. Cette action
déclenche l'événement OFF.

En situation de fonctionnement, on distingue deux modes principaux. Ils
correspondent à des états dans lequel le GUS peut se trouver.

-   Un mode **Arrêt** dans lequel le béquillage est actif et durant
    lequel les asservissements sont désactivés. Ce mode ne consomme
    quasiment pas d'énergie car seule la veille de la carte de commande
    est activée.

-   Un mode **Marche** dans lequel le béquillage est inactif et durant
    lequel les asservissements sont actifs. Ce mode correspond au
    fonctionnement normal du fauteuil et autorise tous les déplacements
    en assurant l'équilibre du fauteuil. Lors de ce mode, les paramètres
    du GUS sont surveillés en temps réel. Le système de béquillage se
    met en fonctionnement, désactivant les asservissements, si au moins
    un des paramètres indique qu'un risque de perte d'équilibre est
    détecté. GUS passe alors en mode **Arrêt**.

Les événements à prendre en considération sont :

-   ON : Début d'utilisation du fauteuil lors de l'installation de la
    personne ;

-   OFF : Fin d'utilisation du fauteuil et retrait de la personne.

```{=html}
<!-- -->
```
-   CMB : Commande Manuelle de Béquillage (béquillage actif) ;

-   CMD : Commande Manuelle de Dé-béquillage (béquillage inactif) ;

-   CAB : Commande Automatique de Béquillage (béquillage actif)

**Question 1 :** A l'aide des informations précédentes, compléter le
document réponse DR1, correspondant au modèle de comportement
macroscopique régissant le fonctionnement du GUS.

![](14-Logique/Cours/pandoc/media/image215.emf){width="4.566666666666666in"
height="3.190424321959755in"}

En réalité, lors de l'activation du mode Marche, deux sous-ensembles
sont activés en même temps, chacun d'entre eux ayant une fonction bien
précise. Le premier de nom **Déplacement/Asservissement** gère
l'équilibre du fauteuil et son déplacement suivant les souhaits de la
personne. Le second nommé **Surveillance** veille au respect des
paramètres critiques du GUS et déclenche l'évènement **CAB** si
nécessaire, évitant ainsi toute chute accidentelle.

**Question 2 :** A l'aide de la description de l'état **Marche**,
compléter le document réponse DR2, correspondant au modèle de
comportement complet régissant le fonctionnement du GUS.

![](14-Logique/Cours/pandoc/media/image216.emf){width="6.3in"
height="4.563888888888889in"}

**Question 3 :** Vis-à-vis de la modélisation comportementale abordée et
sachant que l'opération de béquillage se fait en moins de 200 ms,
conclure sur le respect des exigences 1.2 et 1.2.1 du document technique
DT1.

![](14-Logique/Cours/pandoc/media/image217.emf){width="6.3in"
height="9.75in"}

---
## Inventaire des images
14-Logique/Cours/pandoc/media/image1.png
14-Logique/Cours/pandoc/media/image10.png
14-Logique/Cours/pandoc/media/image100.png
14-Logique/Cours/pandoc/media/image101.png
14-Logique/Cours/pandoc/media/image102.emf
14-Logique/Cours/pandoc/media/image103.png
14-Logique/Cours/pandoc/media/image104.png
14-Logique/Cours/pandoc/media/image105.png
14-Logique/Cours/pandoc/media/image106.png
14-Logique/Cours/pandoc/media/image107.png
14-Logique/Cours/pandoc/media/image108.png
14-Logique/Cours/pandoc/media/image109.png
14-Logique/Cours/pandoc/media/image11.jpeg
14-Logique/Cours/pandoc/media/image111.png
14-Logique/Cours/pandoc/media/image112.jpeg
14-Logique/Cours/pandoc/media/image113.png
14-Logique/Cours/pandoc/media/image114.png
14-Logique/Cours/pandoc/media/image115.png
14-Logique/Cours/pandoc/media/image118.png
14-Logique/Cours/pandoc/media/image119.png
14-Logique/Cours/pandoc/media/image12.jpeg
14-Logique/Cours/pandoc/media/image120.png
14-Logique/Cours/pandoc/media/image121.png
14-Logique/Cours/pandoc/media/image122.emf
14-Logique/Cours/pandoc/media/image123.png
14-Logique/Cours/pandoc/media/image124.png
14-Logique/Cours/pandoc/media/image125.png
14-Logique/Cours/pandoc/media/image126.png
14-Logique/Cours/pandoc/media/image127.png
14-Logique/Cours/pandoc/media/image128.png
14-Logique/Cours/pandoc/media/image129.png
14-Logique/Cours/pandoc/media/image13.jpeg
14-Logique/Cours/pandoc/media/image130.emf
14-Logique/Cours/pandoc/media/image131.emf
14-Logique/Cours/pandoc/media/image132.emf
14-Logique/Cours/pandoc/media/image133.emf
14-Logique/Cours/pandoc/media/image134.emf
14-Logique/Cours/pandoc/media/image135.emf
14-Logique/Cours/pandoc/media/image136.emf
14-Logique/Cours/pandoc/media/image137.jpeg
14-Logique/Cours/pandoc/media/image138.jpeg
14-Logique/Cours/pandoc/media/image139.jpeg
14-Logique/Cours/pandoc/media/image14.png
14-Logique/Cours/pandoc/media/image140.jpeg
14-Logique/Cours/pandoc/media/image141.emf
14-Logique/Cours/pandoc/media/image142.emf
14-Logique/Cours/pandoc/media/image143.emf
14-Logique/Cours/pandoc/media/image144.jpeg
14-Logique/Cours/pandoc/media/image145.png
14-Logique/Cours/pandoc/media/image146.png
14-Logique/Cours/pandoc/media/image147.png
14-Logique/Cours/pandoc/media/image148.png
14-Logique/Cours/pandoc/media/image149.emf
14-Logique/Cours/pandoc/media/image15.wmf
14-Logique/Cours/pandoc/media/image150.jpeg
14-Logique/Cours/pandoc/media/image151.png
14-Logique/Cours/pandoc/media/image152.jpeg
14-Logique/Cours/pandoc/media/image153.png
14-Logique/Cours/pandoc/media/image154.jpeg
14-Logique/Cours/pandoc/media/image155.png
14-Logique/Cours/pandoc/media/image156.png
14-Logique/Cours/pandoc/media/image157.png
14-Logique/Cours/pandoc/media/image158.png
14-Logique/Cours/pandoc/media/image159.png
14-Logique/Cours/pandoc/media/image16.wmf
14-Logique/Cours/pandoc/media/image160.jpeg
14-Logique/Cours/pandoc/media/image161.jpeg
14-Logique/Cours/pandoc/media/image162.jpeg
14-Logique/Cours/pandoc/media/image163.png
14-Logique/Cours/pandoc/media/image164.jpeg
14-Logique/Cours/pandoc/media/image165.jpeg
14-Logique/Cours/pandoc/media/image167.jpeg
14-Logique/Cours/pandoc/media/image168.png
14-Logique/Cours/pandoc/media/image169.png
14-Logique/Cours/pandoc/media/image17.wmf
14-Logique/Cours/pandoc/media/image170.jpeg
14-Logique/Cours/pandoc/media/image171.jpeg
14-Logique/Cours/pandoc/media/image172.png
14-Logique/Cours/pandoc/media/image173.jpeg
14-Logique/Cours/pandoc/media/image174.jpeg
14-Logique/Cours/pandoc/media/image175.png
14-Logique/Cours/pandoc/media/image176.png
14-Logique/Cours/pandoc/media/image177.png
14-Logique/Cours/pandoc/media/image178.png
14-Logique/Cours/pandoc/media/image18.wmf
14-Logique/Cours/pandoc/media/image180.png
14-Logique/Cours/pandoc/media/image181.png
14-Logique/Cours/pandoc/media/image182.jpeg
14-Logique/Cours/pandoc/media/image183.jpeg
14-Logique/Cours/pandoc/media/image184.jpeg
14-Logique/Cours/pandoc/media/image185.jpeg
14-Logique/Cours/pandoc/media/image186.png
14-Logique/Cours/pandoc/media/image187.jpeg
14-Logique/Cours/pandoc/media/image188.png
14-Logique/Cours/pandoc/media/image189.jpeg
14-Logique/Cours/pandoc/media/image19.wmf
14-Logique/Cours/pandoc/media/image190.png
14-Logique/Cours/pandoc/media/image191.jpeg
14-Logique/Cours/pandoc/media/image192.png
14-Logique/Cours/pandoc/media/image193.png
14-Logique/Cours/pandoc/media/image195.png
14-Logique/Cours/pandoc/media/image196.png
14-Logique/Cours/pandoc/media/image197.png
14-Logique/Cours/pandoc/media/image198.jpeg
14-Logique/Cours/pandoc/media/image199.jpeg
14-Logique/Cours/pandoc/media/image20.wmf
14-Logique/Cours/pandoc/media/image200.png
14-Logique/Cours/pandoc/media/image201.png
14-Logique/Cours/pandoc/media/image202.png
14-Logique/Cours/pandoc/media/image203.png
14-Logique/Cours/pandoc/media/image204.jpeg
14-Logique/Cours/pandoc/media/image205.png
14-Logique/Cours/pandoc/media/image206.png
14-Logique/Cours/pandoc/media/image207.png
14-Logique/Cours/pandoc/media/image208.png
14-Logique/Cours/pandoc/media/image209.png
14-Logique/Cours/pandoc/media/image21.wmf
14-Logique/Cours/pandoc/media/image210.png
14-Logique/Cours/pandoc/media/image211.png
14-Logique/Cours/pandoc/media/image212.png
14-Logique/Cours/pandoc/media/image213.emf
14-Logique/Cours/pandoc/media/image214.emf
14-Logique/Cours/pandoc/media/image215.emf
14-Logique/Cours/pandoc/media/image216.emf
14-Logique/Cours/pandoc/media/image217.emf
14-Logique/Cours/pandoc/media/image22.jpeg
14-Logique/Cours/pandoc/media/image23.wmf
14-Logique/Cours/pandoc/media/image24.wmf
14-Logique/Cours/pandoc/media/image25.wmf
14-Logique/Cours/pandoc/media/image26.wmf
14-Logique/Cours/pandoc/media/image27.wmf
14-Logique/Cours/pandoc/media/image28.wmf
14-Logique/Cours/pandoc/media/image29.jpeg
14-Logique/Cours/pandoc/media/image3.png
14-Logique/Cours/pandoc/media/image30.png
14-Logique/Cours/pandoc/media/image31.jpeg
14-Logique/Cours/pandoc/media/image32.jpeg
14-Logique/Cours/pandoc/media/image33.jpeg
14-Logique/Cours/pandoc/media/image34.jpeg
14-Logique/Cours/pandoc/media/image35.jpeg
14-Logique/Cours/pandoc/media/image36.jpeg
14-Logique/Cours/pandoc/media/image37.jpeg
14-Logique/Cours/pandoc/media/image38.jpeg
14-Logique/Cours/pandoc/media/image39.jpeg
14-Logique/Cours/pandoc/media/image40.jpeg
14-Logique/Cours/pandoc/media/image41.jpeg
14-Logique/Cours/pandoc/media/image42.jpeg
14-Logique/Cours/pandoc/media/image43.jpeg
14-Logique/Cours/pandoc/media/image44.jpeg
14-Logique/Cours/pandoc/media/image45.jpeg
14-Logique/Cours/pandoc/media/image46.jpeg
14-Logique/Cours/pandoc/media/image47.jpeg
14-Logique/Cours/pandoc/media/image48.jpeg
14-Logique/Cours/pandoc/media/image49.jpeg
14-Logique/Cours/pandoc/media/image5.jpeg
14-Logique/Cours/pandoc/media/image50.jpeg
14-Logique/Cours/pandoc/media/image51.jpeg
14-Logique/Cours/pandoc/media/image52.jpeg
14-Logique/Cours/pandoc/media/image53.jpeg
14-Logique/Cours/pandoc/media/image54.jpeg
14-Logique/Cours/pandoc/media/image55.jpeg
14-Logique/Cours/pandoc/media/image56.jpeg
14-Logique/Cours/pandoc/media/image57.jpeg
14-Logique/Cours/pandoc/media/image58.jpeg
14-Logique/Cours/pandoc/media/image59.jpeg
14-Logique/Cours/pandoc/media/image6.jpeg
14-Logique/Cours/pandoc/media/image60.jpeg
14-Logique/Cours/pandoc/media/image61.png
14-Logique/Cours/pandoc/media/image62.png
14-Logique/Cours/pandoc/media/image63.jpeg
14-Logique/Cours/pandoc/media/image64.png
14-Logique/Cours/pandoc/media/image65.jpeg
14-Logique/Cours/pandoc/media/image66.png
14-Logique/Cours/pandoc/media/image67.jpeg
14-Logique/Cours/pandoc/media/image68.png
14-Logique/Cours/pandoc/media/image69.wmf
14-Logique/Cours/pandoc/media/image7.jpeg
14-Logique/Cours/pandoc/media/image70.wmf
14-Logique/Cours/pandoc/media/image71.wmf
14-Logique/Cours/pandoc/media/image72.wmf
14-Logique/Cours/pandoc/media/image73.wmf
14-Logique/Cours/pandoc/media/image74.wmf
14-Logique/Cours/pandoc/media/image75.wmf
14-Logique/Cours/pandoc/media/image76.wmf
14-Logique/Cours/pandoc/media/image77.wmf
14-Logique/Cours/pandoc/media/image78.wmf
14-Logique/Cours/pandoc/media/image79.png
14-Logique/Cours/pandoc/media/image8.png
14-Logique/Cours/pandoc/media/image80.png
14-Logique/Cours/pandoc/media/image81.png
14-Logique/Cours/pandoc/media/image82.png
14-Logique/Cours/pandoc/media/image83.png
14-Logique/Cours/pandoc/media/image84.png
14-Logique/Cours/pandoc/media/image85.emf
14-Logique/Cours/pandoc/media/image86.png
14-Logique/Cours/pandoc/media/image87.png
14-Logique/Cours/pandoc/media/image88.png
14-Logique/Cours/pandoc/media/image89.png
14-Logique/Cours/pandoc/media/image90.png
14-Logique/Cours/pandoc/media/image91.png
14-Logique/Cours/pandoc/media/image92.png
14-Logique/Cours/pandoc/media/image93.png
14-Logique/Cours/pandoc/media/image94.png
14-Logique/Cours/pandoc/media/image95.jpeg
14-Logique/Cours/pandoc/media/image96.emf
14-Logique/Cours/pandoc/media/image97.emf
14-Logique/Cours/pandoc/media/image98.png
14-Logique/Cours/pandoc/media/image99.png
