![](13-MAS-MS/Cours/pandoc/media/image1.png){width="8.494444444444444in"
height="4.148611111111111in"}

![](13-MAS-MS/Cours/pandoc/media/image3.emf){width="3.075in"
height="3.0235783027121608in"}

Cycle 7 : Analyser, Modéliser, Expérimenter et Résoudre la distribution
et la conversion d\'énergie en alternatif

**Machine Asynchrone (MAS), Machine Synchrone (MS), Onduleur triphasé**

Thomas Lusseau

Lycée Robert Doisneau - ATS

# **Table des matières** {#table-des-matières .TOC-Heading .unnumbered}

[1. Distribution en triphasé -- Utilisation des complexes
[6](#distribution-en-triphasé-utilisation-des-complexes)](#distribution-en-triphasé-utilisation-des-complexes)

[1.1. Tensions simple et composée
[6](#tensions-simple-et-composée)](#tensions-simple-et-composée)

[1.2. Représentation vectorielle d'un signal sinusoïdal
[7](#représentation-vectorielle-dun-signal-sinusoïdal)](#représentation-vectorielle-dun-signal-sinusoïdal)

[1.3. Puissance réactive [9](#puissance-réactive)](#puissance-réactive)

[2. Onduleur triphasé [11](#onduleur-triphasé)](#onduleur-triphasé)

[3. GENERALITES SUR LES MACHINES ALTERNATIVES
[16](#generalites-sur-les-machines-alternatives)](#generalites-sur-les-machines-alternatives)

[3.1. Constitution d'une machine triphasée
[16](#px-stator_and_rotor_by_zureksconstitution-dune-machine-triphasée)](#px-stator_and_rotor_by_zureksconstitution-dune-machine-triphasée)

[3.2. Création du champ tournant
[16](#création-du-champ-tournant)](#création-du-champ-tournant)

[3.3. Vitesse de synchronisme [18](#_Toc128747961)](#_Toc128747961)

[3.4. Plaque signalétique et plaque à bornes
[20](#_Toc128747962)](#_Toc128747962)

[3.5. Couplages étoile (Y) / triangle ($\mathbf{\Delta}$)
[20](#couplages-étoile-y-triangle-mathbfdelta)](#couplages-étoile-y-triangle-mathbfdelta)

[3.6. Puissances en triphasé équilibré
[22](#puissances-en-triphasé-équilibré)](#puissances-en-triphasé-équilibré)

[3.7. Couple Thermique Equivalent (C~th~)
[23](#couple-thermique-equivalent-cth)](#couple-thermique-equivalent-cth)

[4. Machine Asynchrone (MAS)
[25](#machine-asynchrone-mas)](#machine-asynchrone-mas)

[4.1. Glissement [25](#glissement)](#glissement)

[4.2. Schéma monophasé équivalent
[25](#schéma-monophasé-équivalent)](#schéma-monophasé-équivalent)

[4.3. Bilan de puissance et rendement
[26](#_Toc128747969)](#_Toc128747969)

[4.4. Couple électromagnétique
[29](#couple-électromagnétique)](#couple-électromagnétique)

[4.5. Variation de vitesse d'une MAS
[31](#variation-de-vitesse-dune-mas)](#variation-de-vitesse-dune-mas)

[4.6. Commande V/f = cte : [32](#commande-vf-cte)](#commande-vf-cte)

[5. MACHINE SYNCHRONE [36](#machine-synchrone)](#machine-synchrone)

[5.1. Domaines d'emploi [36](#domaines-demploi)](#domaines-demploi)

[5.2. Modèle simplifié pour un enroulement ou phase
[37](#modèle-simplifié-pour-un-enroulement-ou-phase)](#modèle-simplifié-pour-un-enroulement-ou-phase)

[5.3. Diagramme de Behn-Eschenburg
[37](#diagramme-de-behn-eschenburg)](#diagramme-de-behn-eschenburg)

[5.1. Diagramme de Behn-Eschenburg simplifié
[38](#diagramme-de-behn-eschenburg-simplifié)](#diagramme-de-behn-eschenburg-simplifié)

[5.2. Relations de base [38](#relations-de-base)](#relations-de-base)

[5.3. Couple électromagnétique
[38](#couple-électromagnétique-1)](#couple-électromagnétique-1)

[5.4. Angle géométrique θ
[42](#angle-géométrique-θ)](#angle-géométrique-θ)

[5.5. Bilan de puissances
[42](#bilan-de-puissances)](#bilan-de-puissances)

[5.6. Variation de vitesse de la MS
[43](#variation-de-vitesse-de-la-ms)](#variation-de-vitesse-de-la-ms)

[5.7. Moteur Brushless ou MS autopilotée
[43](#moteur-brushless-ou-ms-autopilotée)](#moteur-brushless-ou-ms-autopilotée)

[6. Sources [45](#sources)](#sources)

[7. Exercices du chapitre [46](#_Toc128747985)](#_Toc128747985)

Donner les démarches et outils nécessaires à l'étude des machines
alternatives.

**Je connais :**

+-------------------------------------------------------------------+---+
| -   La relation entre tension simple et tension composée ainsi    | ⃝  |
|     que leurs définitions                                         |   |
+===================================================================+===+
| -   La définition d'un système triphasé équilibré                 | ⃝  |
+-------------------------------------------------------------------+---+
| -   Les représentations vectorielles et complexe d'une grandeur   | ⃝  |
|     sinusoïdale                                                   |   |
+-------------------------------------------------------------------+---+
| -   Les impédances et admittances pour les dipôles de base (R, L, | ⃝  |
|     C)                                                            |   |
+-------------------------------------------------------------------+---+
| -   Les différents couplages pour une MAS (étoile, triangle)      | ⃝  |
+-------------------------------------------------------------------+---+
| -   Les différents couplages pour une MAS (étoile, triangle)      | ⃝  |
+-------------------------------------------------------------------+---+
| -   Les définitions des puissances active, réactive et apparente  | ⃝  |
|     en triphasé et le théorème de Boucherot                       |   |
+-------------------------------------------------------------------+---+
| -   Les relations fondamentales de la MAS (vitesse de             | ⃝  |
|     synchronisme, glissement,...)                                 |   |
+-------------------------------------------------------------------+---+
| -   Le bilan de puissance de la MAS et les relations des          | ⃝  |
|     différentes puissances                                        |   |
+-------------------------------------------------------------------+---+
| -   La méthode pour déterminer l'expression du couple             | ⃝  |
|     électromagnétique à partir du schéma équivalent               |   |
+-------------------------------------------------------------------+---+
| -   Les différents moyens permettant de faire varier la vitesse   | ⃝  |
|     d'une MAS                                                     |   |
+-------------------------------------------------------------------+---+
| -   Le schéma équivalent monophasé de Behn-Eschenburg pour la MS  | ⃝  |
+-------------------------------------------------------------------+---+
| -   La méthode pour tracer les diagrammes vectoriels et           | ⃝  |
|     déterminer les différentes grandeurs du schéma de             |   |
|     Behn-Eschenburg                                               |   |
+-------------------------------------------------------------------+---+
| -   Les relations fondamentales de la MS                          | ⃝  |
+-------------------------------------------------------------------+---+
| -   La méthode pour déterminer l'expression du couple             | ⃝  |
|     électromagnétique de la MS                                    |   |
+-------------------------------------------------------------------+---+
| -   Le bilan de puissance de la MS                                | ⃝  |
+-------------------------------------------------------------------+---+
| -   Le principe de l'autopilotage pour la MS                      | ⃝  |
+-------------------------------------------------------------------+---+

**Je sais :**

+-------------------------------------------------------------------+---+
| -   Déterminer la tension simple d'un réseau à partir de sa       | ⃝  |
|     > tension composée                                            |   |
+===================================================================+===+
| -   Faire une addition ou soustraction de deux grandeurs          | ⃝  |
|     > sinusoïdales à partir de la représentation vectorielle et   |   |
|     > complexe                                                    |   |
+-------------------------------------------------------------------+---+
| -   Déterminer les impédances équivalentes de n'importe quelle    | ⃝  |
|     > association d'impédances (série, parallèle)                 |   |
+-------------------------------------------------------------------+---+
| -   Déterminer le couplage d'une MAS à partir de sa tension aux   | ⃝  |
|     > bornes d'un enroulement et du réseau utilisé                |   |
+-------------------------------------------------------------------+---+
| -   Déterminer les puissances active, réactive et apparente       | ⃝  |
+-------------------------------------------------------------------+---+
| -   Déterminer la vitesse de synchronisme, le nombre de paires de | ⃝  |
|     > pôles à partir de la fréquence d'alimentation               |   |
+-------------------------------------------------------------------+---+
| -   Déterminer le rendement d'une MAS, pour un point de           | ⃝  |
|     > fonctionnement donné                                        |   |
+-------------------------------------------------------------------+---+
| -   Déterminer l'expression du couple électromagnétique et sa     | ⃝  |
|     valeur maximale                                               |   |
+-------------------------------------------------------------------+---+
| -   Représenter les caractéristiques utiles de la MAS lors d'une  | ⃝  |
|     > variation de vitesse de type U/f=cte                        |   |
+-------------------------------------------------------------------+---+
| -   Déterminer la vitesse de synchronisme, le nombre de paires de | ⃝  |
|     > pôles à partir de la fréquence d'alimentation               |   |
+-------------------------------------------------------------------+---+
| -   Déterminer l'expression du couple électromagnétique et sa     | ⃝  |
|     valeur maximale                                               |   |
+-------------------------------------------------------------------+---+
| -   Tracer les diagrammes vectoriels et déterminer les            | ⃝  |
|     > différentes grandeurs du schéma de Behn-Eschenburg          |   |
+-------------------------------------------------------------------+---+

## ![](13-MAS-MS/Cours/pandoc/media/image5.png){width="2.848611111111111in" height="1.913888888888889in"}Distribution en triphasé -- Utilisation des complexes

### Tensions simple et composée

Une installation **triphasée** comporte **3 fils** de ligne identiques
appelés **phases** et parfois un quatrième fil appelé **neutre**.

![](13-MAS-MS/Cours/pandoc/media/image6.png){width="2.839583333333333in"
height="1.0416666666666667in"}

Un système triphasé équilibré de tension (ou de courants) est formé de
trois grandeurs sinusoïdales de **même valeur efficace V**, de **même
fréquence f = ω÷2π**et **déphasées de 120°**les unes par rapport aux
autres.

Le système de tensions triphasé le plus utilisé est le **système
direct** dont les expressions temporelles sont :

> $v_{1}(t) = V\sqrt{2}\sin(\omega t)$
> $v_{2}(t) = V\sqrt{2}\sin\left( \omega t - \frac{2\pi}{3} \right)$
> $v_{3}(t) = V\sqrt{2}\sin\left( \omega t - \frac{4\pi}{3} \right)$

![](13-MAS-MS/Cours/pandoc/media/image7.png){width="2.838888888888889in"
height="2.7631944444444443in"}Un système triphasé est **équilibré**
si:v~1~+v~2~+v~3~ =0

La **tension simple** v~i~ est la différence de potentiel entre la
**phase i et le neutre**. Sa valeur efficace est notée V.

La **tension composée**u~ij~ = v~i~-v~j~ est la différence de potentiel
entre la **phase i et la phase j**. Sa valeur efficace est notée U.

![](13-MAS-MS/Cours/pandoc/media/image8.wmf)

Lorsqu'on parle de réseau triphasé 400 V, c'est la tension composée qui
est donnée. La tension simple est donc de 230 V.

![](13-MAS-MS/Cours/pandoc/media/image9.png){width="2.9055161854768152in"
height="1.0660378390201224in"}

###  {#section .unnumbered}

### Représentation vectorielle d'un signal sinusoïdal

Une **fonction sinusoïdale** peut être représentée par un **vecteur,
tournant à la vitesse** $\mathbf{\omega}$, dans le plan complexe et dont
la **norme est l'amplitude crête Ŝ**.

![](13-MAS-MS/Cours/pandoc/media/image10.jpeg){width="3.688678915135608in"
height="1.4651367016622923in"}![](13-MAS-MS/Cours/pandoc/media/image11.png){width="3.579861111111111in"
height="3.4618055555555554in"}Les vecteurs représentant une grandeur
sinusoïdale sont tous représentés au même instant comme si on avait pris
une photo. On les **représente donc tous à t = 0**.

![](13-MAS-MS/Cours/pandoc/media/image12.png){width="3.05625in"
height="1.2826388888888889in"}

Tous les vecteurs seront représentés à partir d'une grandeur qui sera
prise **comme référence (ou origine des phases) et à partir de laquelle
seront définis les déphasages.**

![](13-MAS-MS/Cours/pandoc/media/image13.png){width="2.075in"
height="1.4777777777777779in"}La **représentation de Fresnel** utilise
la **valeur efficace S** plutôt que l'amplitude (Ŝ = S.√2) car elle est
facilement **mesurable** (multimètre RMS ou ferromagnétique).

Tous les vecteurs seront représentés à partir d'une grandeur qui sera
prise **comme référence (ou origine des phases).**

![](13-MAS-MS/Cours/pandoc/media/image14.png){width="2.6131944444444444in"
height="2.098611111111111in"}Le diagramme de Fresnel utilise en fait
l'amplitude complexe [S]{.underline} de s(t) dans un vecteur de **norme
S qui représente la valeur efficace de s(t) et est déphasé d'un angle**
$\mathbf{\varphi\ }$.

La représentation de Fresnel permet de réaliser simplement la somme de
fonction sinusoïdale, par construction géométrique. Il suffit alors de
remplacer chaque signal par son vecteur de Fresnel équivalent et de
réaliser une somme vectorielle.

Dans un système triphasé, la tension v~1~ est prise comme référence.

+--------+-------------------------------------------------------------+
| > ![   | **Représentation de Fresnel**                               |
| ](13-M |                                                             |
| AS-MS/ | **Représenter** $\mathbf{V}_{\mathbf{1}}$**,**              |
| Cours/ | $\mathbf{V}_{\mathbf{2}}$ **et** $\mathbf{V}_{\mathbf{3}}$  |
| pandoc | **en prenant** $\mathbf{V}_{\mathbf{1}}$ **comme origine    |
| /media | des phases.**                                               |
| /image |                                                             |
| 15.png | **Construire** $\mathbf{U}_{\mathbf{31}}$ **puis donner son |
| ){widt | expression temporelle**                                     |
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

### Puissance réactive

Nous le verrons plus tard dans le cours mais la machine synchrone peut
se comporter comme un récepteur inductif ou capacitif suivant
l'excitation de la machine. Lorsque le comportement est capacitif, la
machine synchrone fournit de la puissance réactive et porte le nom de
compensateur synchrone. Cela été recherché il y a quelques années pour
améliorer le facteur de puissance d'une installation électrique. Cette
détermination de puissance réactive est donc parfois importante.

Il faut retenir :

+----------------------+----------------------+-----------------------+
| **Comportement       | **Comportement       | **Comportement        |
| réisistif**          | inductif**           | capacitif**           |
|                      |                      |                       |
| **(**$\m             | **(**$\mathbf{0      | **(**$\mathbf         |
| athbf{\varphi = 0)}$ |  < \varphi \leq}\fra | {-}\frac{\mathbf{\ \p |
|                      | c{\mathbf{\ \pi}}{\m | i}}{\mathbf{2}}\mathb |
|                      | athbf{2}}\mathbf{)}$ | f{\leq \varphi < 0)}$ |
+======================+======================+=======================+
| Q = 0                | Q \> 0               | Q \< 0                |
+----------------------+----------------------+-----------------------+

Et quelques petites méthodes rapides pour déterminer les puissances
réactives pour les dipôles de base.

  --------------------------------------------------------------------------------------------------------------------------------------
  **Résistance R**                   **Inductance L**                                **Condensateur C**
  ---------------------------------- ----------------------------------------------- ---------------------------------------------------
  $$P = RI^{2} = \frac{U^{2}}{R}$$   $$P = 0$$                                       $$P = 0$$

  $$Q = 0$$                          $$Q = L\omega I^{2} = \frac{U^{2}}{L\omega}$$   $$Q = - C\omega U^{2} = - \frac{I^{2}}{C\omega}$$
  --------------------------------------------------------------------------------------------------------------------------------------

+--------+-------------------------------------------------------------+
| > ![   | **Puissances en triphasé**                                  |
| ](13-M |                                                             |
| AS-MS/ | ![](13-MAS-MS/Cours/pandoc/media/image16.emf)               |
| Cours/ |                                                             |
| pandoc | Un réseau triphasé 230 V - 400 V - 50 Hz alimente un        |
| /media | récepteur triphasé (R = 20 $\Omega$ et L = 1 H) tel que :   |
| /image |                                                             |
| 15.png | **Déterminer :**                                            |
| ){widt |                                                             |
| h="0.6 | **- [Z]{.underline} puis Z :**                              |
| 262696 |                                                             |
| 850393 | **- I :**                                                   |
| 701in" |                                                             |
| >      | **- P :**                                                   |
| height |                                                             |
| ="0.65 | **- Q :**                                                   |
| 083333 |                                                             |
| 333333 | **- S :**                                                   |
| 34in"} |                                                             |
|        | **- cos** $\mathbf{\varphi}$** :**                          |
+========+=============================================================+
+--------+-------------------------------------------------------------+

## Onduleur triphasé

Que ce soit pour la MAS ou la MS, il est nécessaire d'agir sur la
fréquence d'alimentation. Pour cela, un **onduleur triphasé** est
utilisé (association de 3 « bras de ponts »). Il permet de recréer **un
système triphasé à partir d'une tension continue (appelée aussi « bus
continu ») issue d'une batterie ou à la sortie d'un redresseur**.

La structure est donnée ci-dessous. La charge, modélisée ici par des
sources de courants, est le stator d'une MS ou MAS. L'allure de la
tension $v_{c}$ et de son fondamental sont représentés pour la loi de
commande MLI classique.

![](13-MAS-MS/Cours/pandoc/media/image17.png){width="3.729861111111111in"
height="2.3125in"}![](13-MAS-MS/Cours/pandoc/media/image18.png){width="4.4375in"
height="2.8020833333333335in"}

![](13-MAS-MS/Cours/pandoc/media/image19.png){width="3.8833333333333333in"
height="2.0416666666666665in"}

![](13-MAS-MS/Cours/pandoc/media/image20.gif){width="4.75in"
height="1.9649070428696414in"}

Cette loi de commande particulière se fait donc avec une génération
d'harmonique, qu'une MLI adaptée (sinus-triangle, calculée, vectorielle)
permet de limiter en éliminant les harmoniques de basses fréquences.
Cela peut être noté sur l'allure du courant $i_{c}$ représenté
ci-dessus, et qui est quasiment sinusoïdal. La machine joue un rôle de
filtre passe-bas.

L'intérêt de cette loi de commande est au niveau spectral, si on compare
avec une loi de commande qui génère un signal carré et permet de
supprimer les harmoniques de rang 3, 5, 7, 9 qui sont les plus
contraignants. Les premiers harmoniques avec la MLI précédente sont
centrés autour de la fréquence de porteuse.

![](13-MAS-MS/Cours/pandoc/media/image21.png){width="3.2291666666666665in"
height="2.6998829833770777in"}

Exemple de MLI sinus-triangle :

![](13-MAS-MS/Cours/pandoc/media/image22.png){width="2.9166666666666665in"
height="2.063008530183727in"}

![](13-MAS-MS/Cours/pandoc/media/image23.png){width="4.777656386701662in"
height="2.597471566054243in"}

On voit que le courant est quasiment sinusoïdal, dû au fait que le
moteur agit comme un filtre. La puissance active n'est d'ailleurs
transportée que par le fondamental.

+--------+-------------------------------------------------------------+
| > ![   | **Onduleur**                                                |
| ](13-M |                                                             |
| AS-MS/ | La structure de l'onduleur d'une machine synchrone ainsi    |
| Cours/ | que la tension v~AN~ et l'intensité i~a~ du courant absorbé |
| pandoc | dans la phase « a » pour le point de fonctionnement étudié  |
| /media | (sur une période entière) sont données ci-dessous :         |
| /image |                                                             |
| 15.png | ![](13-MAS-MS/C                                             |
| ){widt | ours/pandoc/media/image24.emf){width="2.8506944444444446in" |
| h="0.6 | height="1.5791666666666666in"}                              |
| 262696 |                                                             |
| 850393 | ![](13-MAS-MS/                                              |
| 701in" | Cours/pandoc/media/image26.emf){width="4.331944444444445in" |
| >      | height="2.327777777777778in"}                               |
| height |                                                             |
| ="0.65 | [Etude de l'onduleur]{.underline}                           |
| 083333 |                                                             |
| 333333 | **Entourer en rouge un bras d'onduleur.**                   |
| 34in"} |                                                             |
|        | **Expliquer pourquoi il est nécessaire d'avoir une commande |
|        | complémentaire pour chaque bras de l'onduleur. Justifier    |
|        | votre réponse.**                                            |
|        |                                                             |
|        | [Etude harmonique]{.underline}                              |
|        |                                                             |
|        | ![](13-MAS-MS/C                                             |
|        | ours/pandoc/media/image27.emf){width="3.5527777777777776in" |
|        | height="2.198611111111111in"}Le spectre d'amplitude est     |
|        | donné ci-contre.                                            |
|        |                                                             |
|        | **Quelle est la fréquence du signal v~AN~ ?**               |
|        |                                                             |
|        | **Quelle est la fréquence de son fondamental v~AN1~ ?**     |
|        |                                                             |
|        | **Déterminer la valeur efficace du fondamental de la        |
|        | tension, notée V~AN1~ ?**                                   |
|        |                                                             |
|        | **Quels sont la fréquence et le rang du premier harmonique  |
|        | non nul de rang strictement supérieur à 1 ?**               |
|        |                                                             |
|        | **Expliquer qualitativement pourquoi on peut considérer que |
|        | le courant absorbé par le moteur est sinusoïdal bien que la |
|        | tension ne le soit pas.**                                   |
|        |                                                             |
|        | [Considérations énergétiques]{.underline}                   |
|        |                                                             |
|        | **Représenter sur les courbes l'allure du fondamental       |
|        | v~AN1~ de la tension v~AN~, en le positionnant correctement |
|        | en phase et en amplitude.**                                 |
|        |                                                             |
|        | **Déterminer la valeur efficace du courant i~a~, notée I~a~ |
|        | (voir courbe).**                                            |
|        |                                                             |
|        | **Déterminer le déphasage** $\mathbf{\varphi}_{\mathbf{1}}$ |
|        | **entre le courant i~a~ et le fondamental de la tension     |
|        | v~AN~.**                                                    |
|        |                                                             |
|        | **Déterminer la puissance active P absorbée par la machine  |
|        | triphasé en fonction des notations précédentes. Effectuer   |
|        | l'application numérique.**                                  |
|        |                                                             |
|        | **Déterminer la puissance réactive Q absorbée par la        |
|        | machine triphasée en fonction des notations précédentes.    |
|        | Effectuer l'application numérique.**                        |
|        |                                                             |
|        | **Peut-on calculer la puissance apparente S ? Quelle donnée |
|        | manque-t-il ?**                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

## GENERALITES SUR LES MACHINES ALTERNATIVES

### ![800px-Stator_and_rotor_by_Zureks](13-MAS-MS/Cours/pandoc/media/image28.jpeg){width="2.042361111111111in" height="1.4472222222222222in"}Constitution d'une machine triphasée

La machine triphasée (MAS ou MS), comme toute machine tournante, est
constituée :

-   D'un **stator :** c'est la partie fixe et qui comporte 3 bobinages
    > (ou enroulements) alimentés en triphasé.

-   D'un **rotor :** c'est la partie tournante qui peut comporter soit
    > des bobinages soit une cage d'écureuil pour une MAS, soit un
    > aimant permanent ou un rotor bobiné pour une MS.

-   D'une plaque à bornes : fixée sur la carcasse, elle comporte un
    > ensemble de 6 bornes permettant de connecter les bobines
    > statoriques à l'alimentation électrique en effectuant le couplage
    > voulu.

-   D'une plaque d'identification (ou plaque signalétique) : fixée sur
    > la carcasse, elle représente la fiche d'identité de la machine.

### Création du champ tournant

Le principe de fonctionnement repose sur la création d'un **champ
magnétique statorique tournant**.

![](13-MAS-MS/Cours/pandoc/media/image29.emf){width="3.0166666666666666in"
height="2.245567585301837in"}Le stator est constitué de **trois bobines
décalées dans l'espace de 120° et alimentées par un système triphasé**.

Dans l'expérience suivante, le stator est constitué de trois bobines
décalées dans l'espace de 120°. Ces bobines sont alimentées par un
système triphasé à fréquence variable obtenu à partir d'un onduleur
triphasé de tensions.

![](13-MAS-MS/Cours/pandoc/media/image30.png){width="3.5416666666666665in"
height="1.5166666666666666in"}

**Champ magnétique pour un enroulement**

![](13-MAS-MS/Cours/pandoc/media/image32.png){width="3.709722222222222in"
height="3.5520833333333335in"}![](13-MAS-MS/Cours/pandoc/media/image33.png){width="3.191666666666667in"
height="1.825in"}

**Théorème de Leblanc :**

Un *courant sinusoïdal* parcourant une *bobine fixe* (à répartition
radiale sinusoïdale de courant), peut être remplacé par *deux inducteurs
constants* (à répartition radiale sinusoïdale de champ) qui *tournent en
sens inverse l\'un de l\'autre à vitesse constanteΩ=ω/p*, se croisant
sur l\'axe de la bobine quand le courant dans celle-ci est maximum, et
d\'amplitude *Φ=Φ~M~/2*.

**Théorème de Ferraris :**

Un *système de courants triphasés équilibrés* parcourant un système de
*bobines* (à répartition radiale sinusoïdale de courant) *décalées de
120°* l\'une de l\'autre, peut être remplacé par un *inducteur constant
unique* (à répartition radiale sinusoïdale de champ) tournant à vitesse
constante *Ω=ω/p* et d\'amplitude *Φ=3Φ~M~/2*.

Pour **une MS**, le rotor tournera à la vitesse du champ tournant, aussi
appelée vitesse de synchronisme.

Pour **une MAS**, les **bobinages rotoriques étant en court-circuit**,
des courants **induits** sont produits. Ces courants vont à leur tour
produire un champ magnétique induit qui va **s'opposer à la cause qui
lui a donné naissance**. Cela se traduit concrètement par un **phénomène
de poursuite du rotor** vis à vis du champ tournant sans qu'il n'arrive
jamais à le rattraper. Tant que le rotor a une fréquence de rotation
différente que celle du champ inducteur, chaque point de rotor « voit »
une variation de champ. Les conducteurs rotoriques produisent donc une
f.é.m. qui, dans le circuit fermé, va donner naissance à des courants
induits.

Le rotor suit donc ce champ magnétique tournant, en tournant à une
**vitesse toujours différente** de celle du champ tournant → **machine
asynchrone**.

### Vitesse de synchronisme

Les enroulements statoriques **alimentés par des courants triphasés de
pulsation ω** créent un **champ magnétique statorique tournant à la
vitesse** $\mathbf{\Omega}_{\mathbf{s}}$ (théorème de Ferraris). Cette
vitesse est appelée **vitesse de synchronisme** et dépend de la
pulsation $\omega$ d'alimentation des courants statoriques et du nombre
de paires de pôles des enroulements statoriques.

![](13-MAS-MS/Cours/pandoc/media/image34.wmf)
![](13-MAS-MS/Cours/pandoc/media/image35.wmf) ou
![](13-MAS-MS/Cours/pandoc/media/image36.wmf)

$\Omega_{s}$ : vitesse de rotation du **champ tournant**(rad/s)

n~s~ : vitesse de rotation du **champ tournant**(tr/s) ou Ns (tr/min)

p : nombre de **paires de pôles** des enroulements statoriques.

f, $\omega$ : **fréquence et pulsation des courants statoriques**

![](13-MAS-MS/Cours/pandoc/media/image30.png){width="4.575in"
height="1.8833333333333333in"}

+--------+-------------------------------------------------------------+
| > ![   | **Pôles et vitesse de synchronisme**                        |
| ](13-M |                                                             |
| AS-MS/ | **Donner la vitesse de synchronisme d'une machine           |
| Cours/ | tétrapolaire alimentée avec une fréquence de 50Hz.**        |
| pandoc |                                                             |
| /media | **Donner la vitesse de synchronisme d'une machine bipolaire |
| /image | alimentée avec une fréquence de 100Hz.**                    |
| 15.png |                                                             |
| ){widt | **Donner le nombre de paires de pôles d'une machine         |
| h="0.6 | synchrone dont le rotor a vitesse de 2400 tr/min et         |
| 262696 | alimentée avec une fréquence de 80Hz.**                     |
| 850393 |                                                             |
| 701in" | **Donner le nombre de paires de pôles d'une machine         |
| >      | asynchrone dont le rotor a vitesse de 950 tr/min et         |
| height | alimentée avec une fréquence de 50Hz.**                     |
| ="0.65 |                                                             |
| 083333 |                                                             |
| 333333 |                                                             |
| 34in"} |                                                             |
+========+=============================================================+
+--------+-------------------------------------------------------------+

### Plaque signalétique et plaque à bornes

![](13-MAS-MS/Cours/pandoc/media/image37.emf){width="7.0875in"
height="2.7936734470691165in"}

C'est la carte d'identité de la machine, on y retrouve entre autres :

**2 :** L'indice de protection IP sur deux chiffres

1^er^ chiffre : protection contre la pénétration des corps solides

2è^me^ chiffre : protection contre la pénétration des corps liquides

**5 :** Les caractéristiques d'alimentation électrique (ex : 230/400V
9/5,2A 50Hz). Le MAS accepte en général une variation de plus ou moins
10% autour de ces valeurs nominales.

**6 :** La puissance utile (on indique toujours ce type de puissance,
sauf dans le cas d'une pompe où la puissance absorbée est indiquée) ⇒
puissance mécanique (ex : 2,2kW - 3ch)

RAPPEL : 1 ch = 736 W en Europe (attention, le cheval britannique est
différent car issu du système impérial : 1HP=746W)

### Couplages étoile (Y) / triangle ($\mathbf{\Delta}$) {#couplages-étoile-y-triangle-mathbfdelta .Etude-de-cas}

Le stator d'une machine asynchrone comporte trois enroulements
identiques qui peuvent être raccordés au réseau triphasé (ou couplés) de
deux manières différentes :

-   Couplage **étoile**

-   Couplage **triangle**

Le choix du couplage dépend de la machine utilisée et du réseau auquel
elle est raccordée.

+----------------------------------+-----------------------------------+
| **[Couplage étoile               | **[Couplage triangle              |
| (Y) :]{.underline}**             | (∆) :]{.underline}**              |
|                                  |                                   |
| La tension aux bornes d'un       | La tension aux bornes d'un        |
| enroulement est la **tension     | enroulement est la **tension      |
| simple** (exemple 230 V).        | composée** (exemple 400 V).       |
|                                  |                                   |
| ![](13-MAS                       | ![](13-                           |
| -MS/Cours/pandoc/media/image38.p | MAS-MS/Cours/pandoc/media/image39 |
| ng){width="2.6791666666666667in" | .png){width="2.702777777777778in" |
| height="0.96875in"}              | height="0.975in"}                 |
|                                  |                                   |
| En couplage étoile, chaque       | En couplage triangle, chaque      |
| enroulement de la MAS voit la    | enroulement de la MAS voit la     |
| tension simple et est parcouru   | tension composée et est parcouru  |
| par le courant de ligne I.       | par un courant                    |
|                                  | $J = \frac{I}{\sqrt{3}}$          |
+==================================+===================================+
+----------------------------------+-----------------------------------+

Le choix du couplage dépend :

-   Des tensions du réseau

-   Des indications portées sur la plaque signalétique qui donne les
    > conditions normales de fonctionnement (dites aussi nominales)

L'utilisateur choisit le couplage qui convient par l'intermédiaire de la
plaque à borne du moteur, qui comporte six bornes auxquelles sont
reliées les entrées et les sorties des trois enroulements

> ![](13-MAS-MS/Cours/pandoc/media/image40.emf){width="1.5798600174978128in"
> height="1.0283016185476817in"}![](13-MAS-MS/Cours/pandoc/media/image41.png){width="2.745282152230971in"
> height="1.2427504374453193in"}

[Normalisation des bornes :]{.underline} Entrées U1, V1 et W1, Sorties
U2, V2 et W2

[Détermination du couplage :]{.underline}

![](13-MAS-MS/Cours/pandoc/media/image42.jpeg){width="1.8770833333333334in"
height="1.2361111111111112in"}Sur la plaque à bornes d'une MAS, la plus
petite des tensions indiquées est la tension efficace nominale aux
bornes d'un enroulement.

  ----------------------------------------------------------------------------------------
                              **Réseau**                                  
  ------------ -------------- --------------------- --------------------- ----------------
                              **133/230V**          **230/400V**          **400/690V**

  **Moteur**   **133/230V**   **Y**                 **impossible**        **impossible**

               **230/400V**   $$\mathbf{\Delta}$$   **Y**                 **impossible**

               **400/690V**   **impossible**        $$\mathbf{\Delta}$$   **Y**
  ----------------------------------------------------------------------------------------

Si la plus grande tension de la plaque signalétique du moteur correspond
à la tension entre phases du réseau (tension composée), on choisit le
couplage étoile Y.

On peut retenir « tensions (réseau et nominale du moteur) égales ⇒
couplage étoile »

Si la plus petite tension de la plaque signalétique du moteur correspond
à la tension entre phases du réseau (tension composée), on choisit le
couplage triangle ∆.

On peut retenir « plus petite tension moteur = plus grande tension
réseau⇒ couplage triangle »

![](13-MAS-MS/Cours/pandoc/media/image30.png){width="4.575in"
height="1.8833333333333333in"}

+--------+-------------------------------------------------------------+
| > ![   | **Couplage**                                                |
| ](13-M |                                                             |
| AS-MS/ | **Les tensions indiquées sur la plaque signalétique d\'un   |
| Cours/ | moteur triphasé sont : 400 V / 690 V 50 Hz**                |
| pandoc |                                                             |
| /media | **\                                                         |
| /image | Quel doit être le couplage du moteur sur un réseau triphasé |
| 15.png | 230 V / 400 V ?**                                           |
| ){widt |                                                             |
| h="0.6 | **\                                                         |
| 262696 | Et sur un réseau triphasé 400 V / 690 V**                   |
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

### Puissances en triphasé équilibré

Un récepteur triphasé équilibré peut être considéré comme l'association
de 3 récepteurs monophasés identique. L'expression des puissances
active, réactive et apparente sont :

> ![](13-MAS-MS/Cours/pandoc/media/image43.wmf)
> ![](13-MAS-MS/Cours/pandoc/media/image44.wmf)
> ![](13-MAS-MS/Cours/pandoc/media/image45.wmf)

![](13-MAS-MS/Cours/pandoc/media/image46.wmf)**Théorème de Boucherot :**

Si un réseau électrique a toutes les grandeurs sinusoïdales de même
fréquence, la puissance active (respectivement réactive) totale fournie
par le réseau est égale à la somme algébrique des puissances actives
(respectivement réactives) consommée par chaque dipôle du réseau.

![](13-MAS-MS/Cours/pandoc/media/image47.wmf)**Facteur de puissance
f~p~ :**

Le facteur de puissance est un paramètre qui rend compte de
l\'efficacité qu\'a un dipôle pour consommer de la puissance lorsqu\'il
est traversé par un courant.

### Couple Thermique Equivalent (C~th~)

Lorsque le moteur piloté par un variateur développe un couple moteur qui
évolue dans le temps de façon cyclique, la détermination du couple
nominal du moteur (celui qui conditionne sa capacité et son prix) se
fait avec la notion de **couple thermique équivalent**.

C\'est l\'échauffement qui limite la capacité d\'un moteur à délivrer un
couple 24h/24 plus élevé que son couple nominal. Pour un couple moteur
égal au couple nominal et développé en permanence, l\'équilibre
thermique de la machine est assuré. Si le couple délivré est supérieur à
la valeur nominale l\'échauffement augmente, si le couple délivré est
inférieur à la valeur nominale, l\'échauffement diminue. On cherche donc
à déterminer pour un couple qui évolue dans le temps la valeur du couple
qui, développé en permanence (donc sans évolution dans le temps),
produirait le même échauffement. Ce couple se nomme couple thermique
équivalent C~th~.

On définit le couple thermique équivalent comme la relation
$C_{th}^{2} = \frac{1}{T}.\int_{0}^{T}{C_{i}^{2}(t).dt}$

En pratique, pour des valeurs constantes de C~i~, on utilisera
$C_{th}^{2} = \frac{1}{T}.\sum_{i}^{}\left( C_{i}^{2} \times t_{i} \right)$

Pour dimensionner un moteur fonctionnant en régime cyclique, on doit
tenir compte du couple dit « thermique équivalent ». Celui-ci doit être
**inférieur ou égal au couple nominal donné par le constructeur**.

+--------+-------------------------------------------------------------+
| > ![   | **Cth**                                                     |
| ](13-M |                                                             |
| AS-MS/ | **Calculer le couple thermique équivalent du moteur à       |
| Cours/ | partir du chronogramme suivant.**                           |
| pandoc |                                                             |
| /media | $C_{th}^{2} = \frac{1}{T}\int_{0}^{T}{C_{M}^{2}(t).dt}$avec |
| /image | T = 0,2 s (5 périodes pour 1 seconde)                       |
| 15.png |                                                             |
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
| > ![   | **Cth**                                                     |
| ](13-M |                                                             |
| AS-MS/ | **Calculer le couple thermique équivalent du moteur à       |
| Cours/ | partir du chronogramme suivant.**                           |
| pandoc |                                                             |
| /media | > ![](13-MAS-MS/C                                           |
| /image | ours/pandoc/media/image48.png){width="5.5214665354330705in" |
| 15.png | > height="3.336052055993001in"}                             |
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

## Machine Asynchrone (MAS)

### Glissement

Une des différences entre la MAS et la MS est l'existence d'un
glissement pour la MAS. Le glissement traduit le fait que dans une MAS,
le rotor ne tourne pas à la vitesse du champ tournant $\Omega_{s}$.
(contrairement à la MS).

Le champ tournant statorique balaie le bobinage rotorique et y induit
des forces électromotrices (loi de Lenz). Les bobinages rotoriques étant
en court-circuit, des courants induits sont produits. L'action du champ
tournant sur ces courants créé un couple électromagnétique.

Le **rotor** de la MAS **tourne à une vitesse angulaire**
$\mathbf{\Omega}\mathbf{\ }$**inférieure**à la vitesse angulaire du
**champ tournant statorique** $\mathbf{\Omega}_{\mathbf{s}}$.

Si le rotor tourne à la vitesse du champ tournant, il ne « voit » plus
de variation de flux et il n'y a plus de fém induite et donc de couple.

Le **glissement** caractérise la diminution relative de vitesse de
rotation. Il est souvent exprimé en % et dépend du point de
fonctionnement de la machine.

![](13-MAS-MS/Cours/pandoc/media/image49.wmf)

Le glissement doit être le plus faible possible (plus il sera grand,
plus les pertes Joule rotoriques seront grandes).

La fréquence des courants rotoriques induits est fonction du
glissement : ![](13-MAS-MS/Cours/pandoc/media/image50.wmf)
![](13-MAS-MS/Cours/pandoc/media/image51.wmf)

> f, $\omega$ : fréquence et pulsation des courants statoriques
>
> f~R~, $\omega_{R}$ : fréquence et pulsation des courants rotoriques
>
> ![](13-MAS-MS/Cours/pandoc/media/image30.png){width="4.575in"
> height="1.8833333333333333in"}

### Schéma monophasé équivalent

Le schéma équivalent monophasé est une **représentation mathématique**
du fonctionnement en **régime permanent** de la MAS alimentée par un
**réseau à tension et fréquence constante**.

![](13-MAS-MS/Cours/pandoc/media/image52.png){width="3.546527777777778in"
height="2.0in"}La résistance R/g n'a aucune signification physique et
permet uniquement de représenter la puissance transmise du stator au
rotor (P~TR~).

V~1~ : tension efficace aux bornes d'une phase du stator

I~1~ : courant efficace dans une phase du stator

R~1~: résistance d'une phase du stator

R~f~: résistance modélisant les pertes ferromagnétiques

X~0~ : réactance de magnétisation= L~0~ω

X~1~ : réactance de fuites au stator= L~1~ω

X : réactance de fuite au rotor ramenée au stator= Lω

R : résistance d'une phase du rotor ramenée au stator

g : glissement

La puissance **P~TR~** transmise du stator au rotor vaut
$\boxed{P_{TR} = 3.\frac{R}{g}I_{1}'^{2}}$.I'~1~ représente la valeur
efficace du courant [I']{.underline}~1~.

Les pertes fer au stator **P~fs\ ~**valent
$\boxed{P_{fs} = 3.\frac{V_{1}^{2}}{R_{f}}}$. V~1~ représente la valeur
efficace de la tension [V]{.underline}~1~.

### Bilan de puissance et rendement

![](13-MAS-MS/Cours/pandoc/media/image53.png){width="7.068787182852144in"
height="3.878063210848644in"}

+--------+-------------------------------------------------------------+
| > ![   | **Etude d'une MAS**                                         |
| ](13-M |                                                             |
| AS-MS/ | La plaque signalétique de la machine porte les indications  |
| Cours/ | suivantes :                                                 |
| pandoc |                                                             |
| /media | 230 V / 400 V - 50 Hz - 15 kW - 1 440 tr.min^-1^            |
| /image |                                                             |
| 15.png | La machine est alimentée par un système triphasé équilibré  |
| ){widt | de tensions sinusoïdales de fréquence f ; on note V la      |
| h="0.6 | valeur efficace des tensions simples et g le glissement.    |
| 262696 |                                                             |
| 850393 | Dans tout le problème, on néglige les résistances et        |
| 701in" | inductances de fuite statoriques, les pertes fer et les     |
| >      | pertes mécaniques.                                          |
| height |                                                             |
| ="0.65 | Sous alimentation nominale, on a obtenu :                   |
| 083333 |                                                             |
| 333333 | \- à vide, un courant de ligne d\'intensité 6 A.            |
| 34in"} |                                                             |
|        | \- à charge nominale, un courant de ligne d\'intensité 19,4 |
|        | A, une puissance absorbée de 11 kW et une fréquence de      |
|        | rotation de 1 440 tr/min.                                   |
|        |                                                             |
|        | La machine asynchrone est alimentée sous 220 V/380 V, 50    |
|        | Hz.                                                         |
|        |                                                             |
|        | **Donner le nombre p de paires de pôles de la machine.**    |
|        |                                                             |
|        | **Déterminer pour le fonctionnement à charge nominale :**   |
|        |                                                             |
|        | \- le glissement g :                                        |
|        |                                                             |
|        | \- la puissance réactive absorbée :                         |
|        |                                                             |
|        | \- le moment du couple nominal C~n~ :                       |
|        |                                                             |
|        | \- les pertes rotoriques par effet Joule :                  |
|        |                                                             |
|        | **Le schéma équivalent est donné ci-contre, rappeler la     |
|        | signification physique de :**                               |
|        |                                                             |
|        | ![](13-MAS-MS/C                                             |
|        | ours/pandoc/media/image54.png){width="1.7201388888888889in" |
|        | height="1.086111111111111in"}                               |
|        |                                                             |
|        | -   L :                                                     |
|        |                                                             |
|        | -   R :                                                     |
|        |                                                             |
|        | -   l :                                                     |
|        |                                                             |
|        | **Montrer que les éléments du schéma équivalent par phase   |
|        | ont pour valeurs : L = 117 mH l = 9,4 mH r = 0,5 Ω.**       |
+========+=============================================================+
+--------+-------------------------------------------------------------+

### ![](13-MAS-MS/Cours/pandoc/media/image55.png){width="2.563888888888889in" height="2.09375in"}Couple électromagnétique

Dans la pratique, le schéma monophasé précédent est simplifié en
négligeant la chute de tension aux bornes de R~1~ et X~1~. Le schéma
équivalent simplifié est alors le suivant :

Les grandeurs étant sinusoïdales on utilise la représentation complexe.

[Z]{.underline}~1~ est l'impédance équivalente à X et R/g en série

${\overset{\underbar{}}{Z}}_{1} = \frac{{\overset{\underbar{}}{V}}_{1}}{{\underline{I'}}_{1}} = \frac{R}{g} + jX$
$\Rightarrow \left| {\overset{\underbar{}}{Z}}_{1} \right| = \frac{V_{1}}{I'_{1}} = \sqrt{\left( \frac{R}{g} \right)^{2} + X^{2}} \Rightarrow I'_{1} = \frac{V_{1}}{\sqrt{\left( \frac{R}{g} \right)^{2} + X^{2}}}$

$P_{TR} = 3.\frac{R}{g}I_{1}'^{2} = C_{em}.\Omega_{s}$ et
$\Omega_{s} = \frac{\omega}{p}$

$$\Rightarrow \boxed{C_{em} = \frac{p}{\omega}\frac{3{V_{1}}^{2}\frac{R}{g}}{\left( \frac{R}{g} \right)^{2} + X^{2}} = \frac{3{V_{1}}^{2}}{\Omega_{s}}\frac{Rg}{R^{2} + (Xg)^{2}}}$$

Représentation graphique :

![](13-MAS-MS/Cours/pandoc/media/image56.png){width="3.6041666666666665in"
height="1.7826388888888889in"}![](13-MAS-MS/Cours/pandoc/media/image57.png){width="3.2104297900262466in"
height="2.263888888888889in"}

##### Recherche du couple maximal {#recherche-du-couple-maximal .unnumbered}

Le couple est maximal lorsque le glissement g vaut une valeur
$\boxed{g_{M} = \frac{R}{X}}$. Le couple est maximal et vaut alors
$C_{em\ max} = C_{M} = \frac{3{V_{1}}^{2}}{\Omega_{s}}\frac{1}{2X}$

Au démarrage on a g = 1, donc le couple de démarrage s'exprime par
$C_{D} = \frac{3{V_{1}}^{2}}{\Omega_{s}}\frac{R}{R^{2} + X^{2}}$

Au voisinage du synchronisme, on a g \<\<g~M~, on a alors
$C_{em} \approx \frac{3{V_{1}}^{2}}{\Omega_{s}}\frac{g}{R}$

![](13-MAS-MS/Cours/pandoc/media/image30.png){width="4.575in"
height="1.8833333333333333in"}

+--------+-------------------------------------------------------------+
| > ![   | **Etude d'une MAS**                                         |
| ](13-M |                                                             |
| AS-MS/ | ![](13-MAS-MS/C                                             |
| Cours/ | ours/pandoc/media/image54.png){width="1.7201388888888889in" |
| pandoc | height="1.086111111111111in"}                               |
| /media |                                                             |
| /image | Le schéma équivalent monophasé d'une MAS est donné          |
| 15.png | ci-contre.                                                  |
| ){widt |                                                             |
| h="0.6 | **Montrer que le moment C du couple de la machine peut      |
| 262696 | s\'écrire :**                                               |
| 850393 |                                                             |
| 701in" | $C = \frac{\text{3p}\text{V}^{2}}{\omega} \t                |
| >      | imes \frac{\frac{r}{g}}{(\frac{r}{g})^{2} + (l\omega)^{2}}$ |
| height |                                                             |
| ="0.65 | **Pour quelle valeur de glissement g~max~, le moment du     |
| 083333 | couple est-il maximal ?**                                   |
| 333333 |                                                             |
| 34in"} | **Donner la valeur de ce maximum Cmax et la fréquence de    |
|        | rotation correspondante en tr/min.**                        |
|        |                                                             |
|        | **Tracer l\'allure du graphe donnant le moment du couple C  |
|        | en fonction de la fréquence de rotation de 0 à 3000 tr/min  |
|        | sachant que la vitesse de synchronisme est de 1500 tr/min.  |
|        | Préciser le type de fonctionnement suivant la fréquence de  |
|        | rotation.**                                                 |
+========+=============================================================+
+--------+-------------------------------------------------------------+

### Variation de vitesse d'une MAS

La vitesse du rotor Ω d'une machine asynchrone est égale à
$\frac{\omega}{p}.(1 - g)$.

Pour faire varier la vitesse, on peut :
$g = \frac{\Omega_{s} - \Omega}{\Omega_{s}} \Rightarrow g.\Omega_{s} = \Omega_{s} - \Omega \Rightarrow \Omega = \Omega_{s}.(1 - g) = \frac{\omega}{p}.(1 - g)$

-   Agir sur le **glissement g** (avec la tension d'alimentation)

-   Agir sur la **fréquence d'alimentation f**

-   Agir que le **nombre de paires de pôles p**

Les méthodes qui n'agissent que sur un seul de ces paramètres ne
permettent que de régler la vitesse au détriment du couple et/ou ne
permettent pas un réglage continu de la vitesse.

### ![](13-MAS-MS/Cours/pandoc/media/image58.png){width="3.50625in" height="2.7069444444444444in"}Commande V/f = cte :

Une des méthodes les plus utilisée aujourd'hui est la **commande
V/f=cte** qui permet d'avoir le couple maximal disponible sur toute la
gamme de vitesse.

Pour réaliser cette commande, un onduleur de tension est utilisé afin de
pouvoir faire varier la fréquence et donc la vitesse de synchronisme.

Lorsqu'on fait varier ce rapport V/f, la caractéristique couple/vitesse
« translate ».

![](13-MAS-MS/Cours/pandoc/media/image59.png){width="3.2325995188101486in"
height="1.641509186351706in"}

En effet, le couple s'écrit dans la zone utile
$C_{em} = - \frac{3p}{4\pi^{2}R}\left( \frac{{V_{1}}^{2}}{f} \right)^{2}\Omega + \frac{3p}{2\pi R}\frac{{V_{1}}^{2}}{f}$

+--------+-------------------------------------------------------------+
| > ![   | **Etude d'une MAS**                                         |
| ](13-M |                                                             |
| AS-MS/ | La plaque signalétique de la machine porte les indications  |
| Cours/ | suivantes :                                                 |
| pandoc |                                                             |
| /media | 230 V / 400 V - 50 Hz - 15 kW - 1 440 tr.min^-1^            |
| /image |                                                             |
| 15.png | La machine est alimentée par un système triphasé équilibré  |
| ){widt | de tensions sinusoïdales de fréquence f ; on note V la      |
| h="0.6 | valeur efficace des tensions simples et g le glissement.    |
| 262696 |                                                             |
| 850393 | On néglige toute saturation magnétique ainsi que les        |
| 701in" | résistances et inductances de fuite statoriques.            |
| >      |                                                             |
| height | **Donner le nombre p de paires de pôles de la machine.**    |
| ="0.65 |                                                             |
| 083333 | +------------------------------------+------------------+   |
| 333333 | | Le schéma équivalent par phase,    | ![](13-MAS-M     |   |
| 34in"} | | entre phase et neutre ; il est     | S/Cours/pandoc/m |   |
|        | | utilisable quelle que soit la      | edia/image60.jpe |   |
|        | | valeur de la tension V.            | g){width="2.0in" |   |
|        | |                                    | height="1.3569   |   |
|        | | On a effectué sur la machine les   | 444444444445in"} |   |
|        | | essais suivants à la fréquence     |                  |   |
|        | | f = 50 Hz :                        |                  |   |
|        | |                                    |                  |   |
|        | | \- **Essai n° 1** : la machine est |                  |   |
|        | | entraînée à la vitesse de          |                  |   |
|        | | synchronisme ; sous tension        |                  |   |
|        | | V = 230 V, le courant de ligne a   |                  |   |
|        | | pour intensité efficace            |                  |   |
|        | | I~0~ = 9,5 A et la puissance       |                  |   |
|        | | absorbée est P~0~ = 630 W.         |                  |   |
|        | |                                    |                  |   |
|        | | \- **Essai n° 2** : le rotor de la |                  |   |
|        | | machine est bloqué ; sous tension  |                  |   |
|        | | V~cc~ = 50 V, le courant de ligne  |                  |   |
|        | | a pour intensité efficace          |                  |   |
|        | | I~cc~ = 30 A et la puissance       |                  |   |
|        | | absorbée est P~cc~ = 830 W.        |                  |   |
|        | +------------------------------------+------------------+   |
|        |                                                             |
|        | **Donner la signification des différents éléments du schéma |
|        | équivalent.**                                               |
|        |                                                             |
|        | **En utilisant l\'essai n° 1, déterminer les valeurs des    |
|        | éléments R et L.**                                          |
|        |                                                             |
|        | **Dans l\'essai n°2 :**                                     |
|        |                                                             |
|        | **- Calculer la puissance active consommée par R et la      |
|        | puissance réactive absorbée par L.**                        |
|        |                                                             |
|        | **- En déduire les puissances actives et réactives          |
|        | absorbées par r et l puis les valeurs des éléments r et     |
|        | l.**                                                        |
|        |                                                             |
|        | **Donner l\'expression littérale de l\'intensité efficace   |
|        | I~2~ du courant dans la résistance r/g. En donner une       |
|        | expression approchée si (gl**$\mathbf{\omega}$**)^2^ est    |
|        | négligeable devant r^2^.**                                  |
|        |                                                             |
|        | **Donner l\'expression approchée du moment Ce du couple     |
|        | électromagnétique si (gl**$\mathbf{\omega}$**)^2^           |
|        | \<\< r^2^.**                                                |
|        |                                                             |
|        | **Exprimer le glissement g en fonction de la vitesse de     |
|        | rotation N de la machine et de sa fréquence de synchronisme |
|        | Ns.**                                                       |
|        |                                                             |
|        | **En déduire que l\'expression approchée du moment Ce du    |
|        | couple électromagnétique peut s\'écrire :**                 |
|        |                                                             |
|        | ![](13-MAS-MS/Cours/pandoc/media/image61.wmf)               |
|        |                                                             |
|        | Vérifier que $A \approx 0,094$ si C~e~ est exprimé en N.m,  |
|        | V en volts, f en Hz ,  N~s~ et N en tr.min^-1^.             |
|        |                                                             |
|        | **Tracer l'allure de la caractéristique approchée Ce = f(N) |
|        | si V = 230 V et f = 50 Hz pour**                            |
|        | $\mathbf{0 < N < 2}\mathbf{N}_{\mathbf{S}}$**. Tracer sur   |
|        | cette courbe, l'allure de la caractéristique réelle.        |
|        | Indiquer les différents modes de fonctionnement. Que se     |
|        | passe-t-il, si on maintient V/f = cte ?**                   |
+========+=============================================================+
+--------+-------------------------------------------------------------+

## MACHINE SYNCHRONE

Une machine synchrone (MS) est un convertisseur électromécanique
réversible. Elle peut fonctionner soit en génératrice (on la nomme alors
**alternateur**), soit en moteur.

Le champ tournant statorique est créé de la même façon que dans la
machine asynchrone. Un ensemble d'enroulements alimentés en triphasé qui
crée un champ tournant unique à $\omega_{s}$. Au rotor, on place des
aimants (ou des enroulements) dont le champ magnétique va s'accrocher
sur le champ tournant statorique.

Le rotor du moteur **synchrone** tourne à **la même vitesse** que le
champ tournant statorique, **quelle que soit la charge et la tension
d'alimentation**.

### Domaines d'emploi

**Petites puissances (de 1 W à 100 W environ) :**

Entraînement de programmateurs horaires, ventilateurs sur
micro-ordinateurs, enregistrement et reproduction audio-vidéo, modélisme
(auto, trains et engins volants)

Instrumentation médicale, micro mécanismes automobile, modélisme, mini
drone...

**Moyennes puissances (de 100 W à 100 kW environ) :**

Machines d'usinage numérique (UGV), commande de mécanismes (aéronautique
et espace...)

Alternateur automobile classique (1 à 3 kW), entraînement direct du
tambour des lave-linge modernes...

Motorisation de véhicules électriques ou hybrides (vélo à assistance
électrique, scooter, Prius Toyota...)

**Fortes puissances (de 100 kW à 1,5 GW environ) :**

Motorisation ferroviaire (TGV atlantique à rotor bobiné 800 kW, 1100kg /
TGV sud-est à rotor aimants 722kW, 720kg, 4570tr/min maxi), entrainement
d'hélices de bateaux

Production d'énergie électrique, alternateur de centrale nucléaire (900
MW à 1300 MW, 1500 tr/min) ou hydraulique (480 MW, 107 tr/min), éolienne
(5 MW)

Industrie : compresseur, centrifugeuse, mélangeuse...

+------------------------+--------------------+------------------------+
| ![](13-MAS-MS/Cou      | ![                 | ![](13-M               |
| rs/pandoc/media/image6 | ](13-MAS-MS/Cours/ | AS-MS/Cours/pandoc/med |
| 2.emf){width="2.275in" | pandoc/media/image | ia/image64.emf){width= |
| height="               | 63.emf){width="1.3 | "1.5993055555555555in" |
| 0.9861111111111112in"} | 229166666666667in" | height="               |
|                        | height="1.16       | 1.1979166666666667in"} |
|                        | 04166666666667in"} |                        |
+========================+====================+========================+
| +-------------------+  | **Usinage à grande | **Paquebot de          |
| | **AR.Drone PARROT |  | vitesse (UGV)**    | croisière Star         |
| | quadrirotor**     |  |                    | Princess**             |
| |                   |  | Vitesse de coupe   |                        |
| | Moteur brushless  |  | de 1000 m/min dans | Propulseur «POD» avec  |
| | spécialement      |  | l'acier, 10 fois   | moteur intégré dans    |
| | conçu et sa carte |  | la vitesse         | une nacelle orientable |
| | de contrôle.      |  | d'usinage          | fixée sous la coque,   |
| |                   |  | traditionnelle.    | entraînant une hélice  |
| | P~u~ = 15 W, N    |  |                    | à pas fixe et vitesse  |
| | variable de 10350 |  | Moteur de broche   | variable.              |
| | à 41400 tr/min    |  | UGV :              |                        |
| |                   |  |                    | P~umax~ = 14 MW à f =  |
| | N = 28000 tr/min  |  | P~u~ = 2 kW, N =   | 29Hz ; 24 pôles        |
| | en vol stabilisé, |  | 40000 tr/min       |                        |
| | soit 3300 tr/min  |  |                    |                        |
| | pour les hélices  |  |                    |                        |
| |                   |  |                    |                        |
| | Contrôle par      |  |                    |                        |
| | microcontrôleur   |  |                    |                        |
| | basse             |  |                    |                        |
| | consommation      |  |                    |                        |
| | 8bits.            |  |                    |                        |
| +-------------------+  |                    |                        |
+------------------------+--------------------+------------------------+

### Modèle simplifié pour un enroulement ou phase

Le schéma monophasé équivalent peut représenter l'alternateur en
convention générateur ou le moteur en convention récepteur. Ce modèle
est réduit à un **circuit R, L, E série** :

-   **E** est la fem développée par la rotation du rotor aux bornes d'un
    > enroulement. Elle est directement proportionnelle à la vitesse et
    > au flux φ sous un pôle qui dépend de l'excitation magnétique
    > fournie par l'inducteur tournant

-   **V** la tension simple aux bornes de l'enroulement et **I** le
    > courant le traversant

-   **R~s~** est la résistance d'un enroulement

-   **L~s~** est l'inductance synchrone\*. On pose également **X~s~ =
    > L~s~ω**= réactance de l'enroulement

*\*Il s'agit d'une inductance qui tient compte du couplage magnétique
entre les trois enroulements et le rotor. Elle est valable seulement en
régime établi et pour les machines à pôles lisses, d'où une des
principales limites du modèle...*

+----------------------------------+-----------------------------------+
| Convention récepteur (moteur)    | Convention générateur             |
|                                  | (alternateur)                     |
+==================================+===================================+
|                                  |                                   |
+----------------------------------+-----------------------------------+
| Couplage électromagnétique en    |                                   |
| tension :                        |                                   |
| ![](13-MAS-MS                    |                                   |
| /Cours/pandoc/media/image65.wmf) |                                   |
+----------------------------------+-----------------------------------+
| Loi des mailles électrique       |                                   |
+----------------------------------+-----------------------------------+
| ![](13-MAS-MS                    | ![](13-MAS-M                      |
| /Cours/pandoc/media/image66.wmf) | S/Cours/pandoc/media/image67.wmf) |
+----------------------------------+-----------------------------------+
| Puissance électrique active (W)  |                                   |
| appelée ou fournie par la        |                                   |
| machine :                        |                                   |
| ![](13-MAS-MS                    |                                   |
| /Cours/pandoc/media/image68.wmf) |                                   |
+----------------------------------+-----------------------------------+
| Puissance électromagnétique      |                                   |
| (W) :                            |                                   |
| ![](13-MAS-MS                    |                                   |
| /Cours/pandoc/media/image69.wmf) |                                   |
|                                  |                                   |
| Couple électromagnétique C~em~   |                                   |
+----------------------------------+-----------------------------------+

### Diagramme de Behn-Eschenburg

Le diagramme de **Behn-Eschenburg** est le diagramme de Fresnel
correspondant à la loi des mailles électrique :

  -----------------------------------------------------------------------
  Convention récepteur (moteur)      Convention générateur (alternateur)
  ---------------------------------- ------------------------------------
                                     

  -----------------------------------------------------------------------

-   **ϕ est le déphasage entre le courant [I]{.underline} et la tension
    > [V]{.underline}**

-   **δ** est l'angle interne, il correspond à l'angle entre
    > [E]{.underline} et [V]{.underline}

-   **ψ est le déphasage entre le courant [I]{.underline} et la fem
    > [E]{.underline}**

### Diagramme de Behn-Eschenburg simplifié

Dans le tracé du diagramme, la chute de tension dans la résistance
**R~s~** est largement exagérée pour permettre une bonne lisibilité.
Dans la réalité, cette résistance est souvent négligée.

Le courant **[I]{.underline}** est placé à l'origine des angles. La
résistance **R~s~** est négligée. Le diagramme de Behn-Eschenburg se
simplifie alors ainsi :

  -----------------------------------------------------------------------
  Convention récepteur (moteur)      Convention générateur (alternateur)
  ---------------------------------- ------------------------------------
                                     

  -----------------------------------------------------------------------

Ainsi le comportement de la machine peut être **inductif** (courant en
retard) ou **capacitif** (courant en avance) suivant l'excitation de la
machine qui règle la valeur de la fém E.

Quand E est supérieur à V, on dit que la machine est surexcitée.

L'angle ψ entre le courant I et la fém E dans l'enroulement est
essentiel pour l'expression du couple de la machine et son contrôle.

### Relations de base

Les équations fondamentales à connaître pour la machine synchrone sont
donc :

> ![](13-MAS-MS/Cours/pandoc/media/image70.wmf)

### Couple électromagnétique

On détermine le couple électromagnétique à partir de la puissance
électromagnétique :

> ![](13-MAS-MS/Cours/pandoc/media/image71.wmf)

On voit donc qu'à excitation constante, la fém E étant proportionnelle à
la vitesse Ω~s~

En instantané, la loi de Faraday donne e = $\frac{d\varphi}{dt}$, soit
en sinusoïdal E = ω.φ = p.Ω~s~.φ = K~e~.Ω~s~

> ![](13-MAS-MS/Cours/pandoc/media/image72.wmf) avec K~c~ = 3.K~e~

On retrouve une expression de couple comparable à celui d'une MCC mais
dépendant de l'angle ψ.

##### Autre expression du couple électromagnétique {#autre-expression-du-couple-électromagnétique .unnumbered}

Dans le diagramme vectoriel (résistance d'un enroulement négligée), on
remarque que E.cosψ = V.cosϕ, ce qui donne les relations P~em~ =
3.V.I.cosϕ et
$C_{em} = \frac{P_{em}}{\mathrm{\Omega}_{s}} = \frac{3.V.I.cos\phi}{\mathrm{\Omega}_{s}}$

+--------+-------------------------------------------------------------+
| > ![   | **Etude d'une MS**                                          |
| ](13-M |                                                             |
| AS-MS/ | Le moteur synchrone est à aimants permanents et possède 8   |
| Cours/ | pôles (p = 4). Les enroulements du stator sont couplés en   |
| pandoc | étoile. L'intensité efficace nominale du courant dans un    |
| /media | enroulement est I~N~ = 155 A. Afin de simplifier l'étude,   |
| /image | les pertes mécaniques ainsi que les pertes fer du moteur    |
| 15.png | synchrone seront négligées.                                 |
| ){widt |                                                             |
| h="0.6 | La machine est étudiée en convention récepteur. Le modèle   |
| 262696 | équivalent à une phase de l'induit est représenté           |
| 850393 | ci-dessous. Les tensions et courants sont supposés          |
| 701in" | sinusoïdaux de pulsation ω = 2πf.                           |
| >      |                                                             |
| height | Afin de déterminer les paramètres du modèle, divers essais  |
| ="0.65 | ont été effectués :                                         |
| 083333 |                                                             |
| 333333 | -   Essai n°1 : on a mesuré la résistance entre deux        |
| 34in"} |     > phases : r = 0,06 Ω.                                  |
|        |                                                             |
|        | -   Essai n°2 : sur un banc d'essais, on a entraîné la      |
|        |     > machine synchrone à vide par l'intermédiaire d'un     |
|        |     > moteur auxiliaire à la vitesse N = 1500 tr/min. On a  |
|        |     > mesuré la tension simple aux bornes d'une phase : 37  |
|        |     > V.                                                    |
|        |                                                             |
|        | -   Essai n°3 : avec une alimentation électrique            |
|        |     > appropriée, on a effectué un essai de la machine en   |
|        |     > moteur à 1500 tr/min pour lequel ψ = 0°, I = I~max~ = |
|        |     > 185 A et V = 49 V.                                    |
|        |                                                             |
|        | -                                                           |
|        |                                                             |
|        | **Déterminer la fréquence des tensions statoriques si N =   |
|        | 1500 tr/min.**                                              |
|        |                                                             |
|        | **Essai n°1. Déterminer la valeur de la résistance R d'un   |
|        | enroulement.**                                              |
|        |                                                             |
|        | **Essai n°2. On pose E = K.Ω (Ω en rad/s). Déterminer K.**  |
|        |                                                             |
|        | **La résistance R n'est pas négligée**                      |
|        |                                                             |
|        | **A partir du modèle électrique équivalent, écrire la       |
|        | relation entre [V]{.underline}, [E]{.underline} et          |
|        | [I]{.underline}.**                                          |
|        |                                                             |
|        | **Tracer le diagramme vectoriel de cette relation relatif à |
|        | l'essai n°3. On prendra E comme origine des phases.**       |
|        |                                                             |
|        | **En déduire que L = 0,21mH.**                              |
|        |                                                             |
|        | **La résistance R est négligée.** Pour N = 5000 tr/min, ψ = |
|        | -59° et I = I~N~ = 155 A :                                  |
|        |                                                             |
|        | **Déterminer f puis ω.**                                    |
|        |                                                             |
|        | **En déduire E = K.Ω et LωI.**                              |
|        |                                                             |
|        | **Tracer le diagramme vectoriel. On prendra E comme origine |
|        | des phases. En déduire la valeur de V et celle de ϕ.**      |
+========+=============================================================+
+--------+-------------------------------------------------------------+

### Angle géométrique θ

L'angle ψ est complémentaire de l'angle géométrique θ
$(\theta + \psi = \frac{\pi}{2}\ )$ entre l'axe du champ polaire et
celui du champ tournant puisque la fem E est en avance de
$\frac{\pi}{2}$ sur le champ (loi de Faraday). Ainsi sinθ = cosψ

Par conséquent, **l'angle θ représente l'état de charge de la machine ou
le couple résistant. Il est nul pour une machine à vide et ne peut pas
dépasser 90°, sinon il y a décrochage**. **La limite de décrochage est
donc pour** $\mathbf{\psi}\mathbf{\leq 0.}$

### Bilan de puissances

Les pertes de la **machine synchrone triphasée** sont :

-   Des **pertes joules au stator (induit)** **P~JS~ = 3.R~s~.I²**

(R~S~ résistance d'un enroulement statorique et I courant dans un
enroulement en branchement étoile)

-   Des **pertes mécaniques** **P~m~**

Frottements mécaniques fonction essentiellement de la vitesse de
rotation pour les machines usuelles ou du carré de la vitesse à cause
des effets aérodynamiques pour les machines ayant une vitesse élevée par
exemple broche UGV à N~S~ = 20 000 tr/min

-   Des **pertes fer ou magnétiques** **P~fe~**

On regroupe parfois les pertes mécaniques et fer sous le nom de **pertes
collectives** P~c~ = P~m~ + P~fe~

-   Des **pertes d'excitation** **P~e~ = R~e~.I~e~² = U~e~.I~e~**

Si l'inducteur de résistance R~e~ est bobiné

  -----------------------------------------------------------------------------------
  Convention récepteur (moteur)                   Convention générateur (alternateur)
  ----------------------------------------------- -----------------------------------
                                                  

  Rendement                                       
  ![](13-MAS-MS/Cours/pandoc/media/image73.wmf)   
  -----------------------------------------------------------------------------------

On trouve aussi la notation P~totale~ = P~a~ = P~u~ + P~J~ + P~c~

##### Expression du couple {#expression-du-couple .unnumbered}

Si l'on néglige toutes les pertes, on peut écrire puissance mécanique =
puissance électrique

Soit C~u~.Ω~s~ = 3.V.I.cosϕ = 3.E.I.cosψ = 3.K~e~.Ω~s~.I.cosψ d'où C~u~
= 3.K~e~.I.cosψ = 3.K~e~.I.sinθ avec K~e~ = p.φ

Le couple du moteur synchrone est maximum quand l'angle θ vaut π/2

##### Risque de décrochage {#risque-de-décrochage .unnumbered}

L'angle δ représente l'angle de décalage mécanique entre le rotor et le
champ statorique lors d'un fonctionnement moteur. Si cet angle dépasse
90°, le moteur rentre dans une phase instable où le rotor « décroche »
de l'attraction du champ tournant.

**La conséquence est que le moteur s'arrête et qu'il faut le
redémarrer**. Toutes les commandes qui permettent de faire fonctionner
les moteurs synchrones à vitesse variable permettent en réalité
d'asservir la position du champ tournant pour que l'angle mécanique
reste à une valeur toujours inférieure à 90°. On parle alors de
« machine synchrone auto-pilotée » ou de « moteur à courant continu sans
balais » ou « brushless ».

### Variation de vitesse de la MS

Dans le cas le plus général, le contrôle de la machine synchrone peut se
faire en agissant sur 3 paramètres :

-   La fem **E** par le courant d'excitation **I~e~** si la machine est
    > à inducteur bobiné, en agissant sur la valeur du flux φ sous un
    > pôle. Ceci est impossible si la machine est à aimants permanents.

-   Le courant **I** dans les phases lorsque la machine est associée à
    > un convertisseur de puissance avec contrôle de courant (capteur à
    > effet Hall nécessaire).

-   L'angle **ψ** lorsque la position du rotor est contrôlée par capteur
    > angulaire (fourche optique, codeur incrémental, synchro-résolver).
    > L'alimentation des 3 phases est alors coordonnée à l'information
    > de ce capteur (pilotage des interrupteurs d'un onduleur). Il
    > s'agit alors d'un **autopilotage.**

Un pilotage complet donne lieu à un ensemble dit « brushless »
(traduction mot à mot « sans balais »), par comparaison à la fonction
réalisée par l'ensemble collecteur + balais d'une MCC.

### ![](13-MAS-MS/Cours/pandoc/media/image74.emf)Moteur Brushless ou MS autopilotée

L'organisation de la commande de la machine synchrone autopilotée est
présentée ci-contre. La commande permet d'imposer l'amplitude du courant
**I~ref~** et l'angle d'autopilotage **ψ~ref~**.

Afin de maximiser le couple, l'angle d'autopilotage est maintenu à 0
\[$\pi\rbrack$ grâce aux capteurs et aux asservissements.

+--------+-------------------------------------------------------------+
| > ![   | **Unité de vissage**                                        |
| ](13-M |                                                             |
| AS-MS/ | La machine est modélisée par le modèle de Behn-Eschenburg,  |
| Cours/ | la résistance de chaque phase est négligée. La figure       |
| pandoc | ci-contre présente le schéma équivalent par phase de la     |
| /media | machine, ainsi que les conventions utilisées.               |
| /image |                                                             |
| 15.png | Les pertes fer et mécaniques sont supposées négligeables.   |
| ){widt | L'étude est faite en régime établi.                         |
| h="0.6 |                                                             |
| 262696 | $\varphi$ : Déphasage entre le courant i~i~ et la tension   |
| 850393 | v~i~                                                        |
| 701in" |                                                             |
| >      | ψ : Déphasage entre la fém. **e~i~** et le courant **i~i~** |
| height |                                                             |
| ="0.65 | Le constructeur donne :                                     |
| 083333 |                                                             |
| 333333 | -   le nombre de paires de pôles : p = 3 ;                  |
| 34in"} |                                                             |
|        | -   l'inductance cyclique : L = 7,5 mH ;                    |
|        |                                                             |
|        | -   la constante de                                         |
|        |     fem (![](13-MAS-MS/Cours/pandoc/media/image75.wmf)) : K |
|        |     = 0,13 V/(rad/s).                                       |
|        |                                                             |
|        | **Calculer la pulsation** $\mathbf{\omega}$ **et la         |
|        | fréquence f des grandeurs statoriques si la machine tourne  |
|        | à 3600 tr/min.**                                            |
|        |                                                             |
|        | **Montrer que le couple fourni par la machine peut se       |
|        | mettre sous la forme**                                      |
|        | $\mathbf{C}\mathbf{=}\mathbf{K}_{\mathbf{c}}\               |
|        | mathbf{.}\mathbf{I}\mathbf{.}\mathbf{\cos}\mathbf{\psi}$**. |
|        | Déterminer** $\mathbf{K}_{\mathbf{c}}$**.**                 |
|        |                                                             |
|        | **Pour un couple et une vitesse donnée, quel angle          |
|        | d'autopilotage ψ permet de minimiser les courants dans les  |
|        | bobinages de la machine en fonctionnement frein puis moteur |
|        | ?**                                                         |
|        |                                                             |
|        | **Calculer la puissance absorbée par la machine. Quelle est |
|        | la condition sur** $\mathbf{\varphi}$ **pour obtenir un     |
|        | fonctionnement moteur puis frein ?**                        |
|        |                                                             |
|        | **Tracer l'allure des diagrammes vectoriels de Behn         |
|        | Eschenburg en fonctionnement moteur puis en fonctionnement  |
|        | frein. On prendra la phase de E comme origine et on         |
|        | supposera que**                                             |
|        | $                                                           |
|        | \left| \mathbf{\cos}\mathbf{\psi} \right|\mathbf{= 1}$**.** |
|        |                                                             |
|        | **Pour le fonctionnement moteur et pour N = 3 000 tr/min et |
|        | I = 6,7 A, déterminer :**                                   |
|        |                                                             |
|        | **- le facteur de                                           |
|        | p                                                           |
|        | uissance cos**$\mathbf{\ }\mathbf{\varphi}\mathbf{\ }$**;** |
|        |                                                             |
|        | **- la tension simple efficace V,**                         |
|        |                                                             |
|        | **- le couple C.**                                          |
+========+=============================================================+
+--------+-------------------------------------------------------------+

## Sources

Ce cours a été élaboré à l'aide de nombreuses ressources provenant de
différents collègues de l'UPSTI.\

## Exercices du chapitre

![](13-MAS-MS/Cours/pandoc/media/image76.png){width="5.466666666666667in"
height="8.373527996500437in"}

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"}
![](13-MAS-MS/Cours/pandoc/media/image78.png){width="0.8905686789151356in"
height="0.5566043307086614in"}**BANC BALAFRE**

*([Source]{.underline} : ATS 2019)*

**Mise en situation**

![](13-MAS-MS/Cours/pandoc/media/image79.png){width="2.3680555555555554in"
height="1.3208333333333333in"}Le banc BALAFRE (BAnc d\'essais à LAmes
Fluides à haut REynolds) est un banc d\'essai destiné à
l\'identification du comportement des étanchéités du type joint
annulaire. Il est dimensionné pour l\'étude de joints utilisés dans des
turbomachines que l\'on trouve dans les domaines du spatial et de
l\'énergie.

Le banc BALAFRE a été développé par la société CSTM (Conception de
Systèmes et Technologie Mécanique) en collaboration avec l\'institut
Pprime de l\'université de Poitiers.

**[Principe de fonctionnement du banc :]{.underline}**

Le joint que l\'on souhaite caractériser est monté sur les pièces joint
(rotor) et joint (stator). Pour obtenir un comportement représentatif du
fonctionnement réel du joint, on injecte de l\'eau sous-pression à
l\'entrée du banc. Cette eau circule entre le stator et le rotor, en
formant un film liquide. Le comportement dynamique de ce film liquide
dépend des propriétés du joint. C\'est ce comportement (exprimé sous la
forme de matrices de raideur, d\'amortissement et de masse) que l\'on
cherche à caractériser.

Pour effectuer cette identification, il est donc nécessaire :

-   d\'entraîner le rotor en rotation

-   de provoquer une perturbation du film liquide.

Un moteur asynchrone triphasé Leroy Sommer PLS- 280-MP est utilisé pour
entraîner le rotor. Pendant un essai, le rotor doit avoir une vitesse
stabilisée à 6000 tr.min^-1^.

La perturbation du film liquide est générée par huit actionneurs
piézoélectriques et transmise au cœur de butée double.

![](13-MAS-MS/Cours/pandoc/media/image80.png){width="5.702321741032371in"
height="3.245138888888889in"}

**[Données et hypothèses :]{.underline}**

-   Le couple résistant exercé par le film d\'eau sur le joint (rotor) à
    > 6000 tr.min^-1^ est estimé à C~res~ = 300 N.m

-   La vitesse cible N~c~ (vitesse de rotation du rotor de joint) doit
    > pouvoir être réglée à une valeur choisie entre 5000 et 7000
    > tr.min^-1^

-   La mise en rotation doit se faire à accélération constante pendant
    > une durée n\'excédant par T~acc~ = 5 s

-   Le réseau d\'alimentation électrique fournit une tension 230/ 400 V
    > en 50 Hz

-   La plaque signalétique du moteur est reproduite ci-contre

-   Les pertes Joules statoriques, les pertes fer et les pertes
    > mécaniques dans le moteur sont négligées

![](13-MAS-MS/Cours/pandoc/media/image81.png){width="3.1368055555555556in"
height="2.1034722222222224in"}

**Modélisation de la motorisation**

**1.** En utilisant les informations de la plaque signalétique,
**déterminer** :

-   Le couplage du moteur et la valeur nominale de la tension U~s~,
    > définie sur le schéma électrique équivalent

-   Le nombre de paires de pôles p

-   Le glissement nominal g~N~

-   Le couple utile nominal C~uN~

On donne sur la figure ci-contre le modèle équivalent ramené au stator
d'une phase du moteur. L~0~ représente l\'inductance de magnétisation et
L~c~ l\'inductance des fuites totales d\'une phase (rotorique ramenée au
stator et stator). On note g le glissement.

On rappelle que la puissance dissipée dans la résistance $\frac{R}{g}$
correspond à la puissance transmise du stator au rotor. Cette puissance
peut être décomposée en une résistance R correspondant aux pertes Joule
dans le rotor en série avec une résistance $\frac{R(1 - g)}{g}$
correspondant à la puissance électromécanique fournie au rotor.

**2.** **Exprimer** le couple électromagnétique C~EM~ en fonction de
$U_{s}^{2}$, ω (pulsation d'alimentation du moteur), g, R, L~c~ et p.
**En déduire** que l'expression du couple utile disponible sur l'arbre
moteur est
$C_{u} = \frac{3pU_{s}^{2}}{\omega}.\frac{\frac{R}{g}}{\left( \frac{R}{g} \right)^{2} + \left( L_{c}\omega \right)^{2}}$

![](13-MAS-MS/Cours/pandoc/media/image82.png){width="2.877083333333333in"
height="2.2069444444444444in"}À l\'aide de cette équation, on obtient
l\'allure de la courbe de couple en fonction de la vitesse de rotation N
de l\'arbre moteur.

**3.** À l\'aide des points A, B, Cet D, **identifier** sur cette
courbe :

-   Le point de fonctionnement nominal

-   Le démarrage du moteur

-   Le point de synchronisme

-   La zone de fonctionnement instable du moteur

**4.** **Déterminer** l'expression du couple utile maximal C~M~ pour une
valeur du glissement g~M~.

Le constructeur précise le rapport du couple maximal sur le couple
nominal $\frac{C_{M}}{C_{N}} = 3,5$.

**5.** **En déduire** l\'expression de L~c~ en fonction de p, U~s~, C~M~
et ω. **Faire** l\'application numérique.

**6.** Que peut-on dire de $\frac{R}{g}$ par rapport à L~c~ω au
voisinage du point de fonctionnement nominal ? **En déduire**
l\'expression de R en fonction du couple nominal C~N~, du glissement
nominal g~N~, de p, U~s~ et de ω. **Faire** l'application numérique.

Le variateur utilisé pour la commande du moteur fonctionne en
$\frac{U_{s}}{f}$ constant. À l\'aide des valeurs calculées
précédemment, on a tracé les courbes de couple utile en fonction de la
vitesse de rotation pour différentes valeurs de fréquence de commande.

![](13-MAS-MS/Cours/pandoc/media/image83.png){width="2.9339621609798776in"
height="2.17961176727909in"}
![](13-MAS-MS/Cours/pandoc/media/image84.png){width="2.9339621609798776in"
height="2.323953412073491in"}

Courbe complète Zoom sur la partie utile

Évolution du couple utile en fonction de la vitesse de rotation pour des
fréquences de commande de 90 à 110 Hz

**7.** À l'aide de ces courbes, **déterminer** quelle fréquence doit
être imposée par le variateur pour maintenir une vitesse de 6000
tr.min^-1^ en présence d\'un couple résistant correspondant au couple
C~res~ défini par le cahier des charges.

![](13-MAS-MS/Cours/pandoc/media/image85.png){width="0.6415091863517061in"
height="0.6363768591426072in"}**PANNEAUX DÉROULANTS**

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source :]{.underline} Concours ATS
2011)*

**Mise en situation**

![Senior](13-MAS-MS/Cours/pandoc/media/image86.jpeg){width="1.6194444444444445in"
height="2.7291666666666665in"}Le panneau publicitaire déroulant,
appartenant à la catégorie des MUPI (Mobilier Urbain Pour
l'Information), est un objet installé dans l'espace public. C'est un
media de masse qui permet de toucher le consommateur sur son lieu de
vie. La société JC DECAUX qui installe des mobiliers urbains fixes s'est
intéressée depuis longtemps à pouvoir toucher un maximum de personnes
grâce à l'utilisation de ces panneaux.

En effet, on a longtemps utilisé des panneaux fixes mais les études
réalisées par JC Decaux Wordlink ont permis d'analyser les effets
publicitaires de l'introduction du mouvement dans la communication
extérieure.

Cette étude, appelée Sutton démontre qu'un panneau en mouvement augmente
le contact visuel avec le panneau de 37%. Ceci signifie que 90% du
trafic aura au moins un contact visuel avec le site durant son passage.
Lorsque le panneau est déroulant, plus de deux-tiers de personnes
mémorisent la campagne. C'est pourquoi JC DECAUX a été amené à
développer ce type de panneau déroulant. L'expérience de JC DECAUX dans
ce domaine date de plus de trente ans puisque le premier brevet
concernant ce type de panneau a été déposé en décembre 1977.

Le système étudié est le système de panneau type sénior de 8m² qui
équipe de nombreuses villes dont Paris. Ce panneau permet de faire
défiler successivement dans un sens puis dans l'autre jusqu'à 7 affiches
avec un temps d'exposition constant pour chaque affiche.

Le format des affiches rétro éclairées est d'environ 8m².Les affiches
sont de dimensions 3200 x 2300mm (largeur x hauteur) avec une surface
visible de 3060 x 2230mm.Le dispositif est constitué de deux rouleaux
(longueur 3200mm et ∅ 140mm).Le défilement s'effectue à la vitesse de
1m/s avec une rampe d'accélération et de décélération de chacune 1
seconde. Le cycle de défilement pour 4 affiches est le suivant :

Le temps d'exposition est programmable à distance via un module GSM
(Wacom) relié à un automate programmable (Siemens). Ce temps
d'exposition est modifiable suivant les termes du contrat avec
l'annonceur.

Les affiches étant changées tous les 15 jours, il faut faciliter leur
mise en place. Pour cela, elles sont disposées en bandeau et placées sur
le rouleau du haut lors de leur installation. La première est une amorce
fixée au rouleau du haut avec un adhésif puis elles sont reliées les
unes aux autres par un système de zip. La dernière est une amorce qui
est également fixée au rouleau du bas par un adhésif. Cet ensemble
constitue un bandeau.

Dans la solution actuelle, l'entraînement se fait par deux moteurs
asynchrones identiques commandés par deux variateurs scalaires.
L'ensemble est géré par l'automate programmable.

**Réglage de la vitesse du moteur asynchrone**

Le moteur asynchrone est commandé par un variateur de type U/f constant.
La vitesse nominale de défilement d'un affiche est de 1m.s^-1^. Le
moteur utilisé est un motoréducteur réfW10DT56L4.

[Objectif de l'étude :]{.underline}

**Vérifier** le dimensionnement du moteur asynchrone et **régler** la
fréquence du variateur afin de répondre au mieux au cahier des charges.

Dans cette étude, on s'intéressera au fonctionnement à vitesse
constante. On notera :

-   Ω : la vitesse angulaire exprimée en rad/s

-   N : la fréquence de rotation exprimée en tr/min

Compte tenu de la tension dans l'affiche, on obtient un couple moteur
C~m~ = 0,28 Nm à une vitesse angulaire Ω~m~ = 139 rad.s^-1^.

**1. Déterminer** la puissance **P~m~** nécessaire en régime permanent.

Les caractéristiques du moteur lorsqu'il est alimenté sur un réseau 50
Hz sont les suivantes :

P~N~ : puissance nominale sur l'arbre du moteur 120 W

N~N~ : vitesse nominale en sortie d'arbre 1300 tr.min^-1^

I~N~ : courant nominal à vitesse nominale 0,8 A

cosϕ : facteur de puissance 0,68

I~D~/I~N~ : courant au démarrage/courant nominal 2,6

C~N~ : couple nominal 0,88 Nm

C~max~/C~N~ : couple maximal/couple nominal 1,9

**2.** A partir des caractéristiques du moteur et de la réponse à la
question précédente, **montrer** que le moteur est largement
surdimensionné.

**3. Donner** l'expression de **g** en fonction de la vitesse angulaire
**Ω~m~** et la vitesse de synchronisme **Ω~s~**.

**4. Donner** l'expression de **Ω~s~** en fonction de **ω** (pulsation
du réseau) et de **p** (nombre de paires de pôles) puis **déterminer
p**, **Ω~s~** et **N~s~** lorsque le moteur est alimenté par un réseau
triphasé à une fréquence de 50 Hz.

**5.** A partir des données du constructeur, **déduire** la valeur du
glissement au point de fonctionnement nominal **g~N~**.

On rappelle que l'expression du couple électromagnétique pour un moteur
asynchrone est :

+-----------------------------+----------------------------------------+
| $$C_{m1} =                  | C~max~ : couple maximal du moteur      |
| \frac{2.C_{\max}}{\frac{g_{ |                                        |
| 0}}{g} + \frac{g}{g_{0}}}$$ | g : glissement                         |
|                             |                                        |
|                             | g~0~ : glissement pour le couple       |
|                             | C~max~                                 |
+=============================+========================================+
+-----------------------------+----------------------------------------+

**6. Calculer** la valeur**g~0~** à partir de l'expression du couple
moteur**C~m1~**.

**7. Tracer** l'allure de la caractéristique **C~m~** en fonction de
**g** (pour 0 \< g \< 1) en indiquant les valeurs numériques de C~N~,
g~N~, C~max~ et g~0~ sur la courbe. **Préciser** la zone de
fonctionnement stable du moteur.

En réalité, le rendement de la transmission n'est pas égal à 1. En
conséquence, la valeur du couple électromagnétique en fonctionnement
normal est C~maff~ = 0,3 Nm.

**8.** Le système fonctionnant à une valeur de couple C~m1~ = C~maff~
donc inférieure à C~N~, **montrer** que l'expression du couple moteur
peut se mettre sous la forme$C_{m1} = 2.\frac{g}{g_{0}}.C_{\max}$ et
**en déduire** la valeur du glissement **g~aff~** pour le couple
**C~maff~**.

**9. Montrer** que l'expression du couple peut s'exprimer par C~m1~ =
λ.(Ω~s~ - Ω~m~). **Préciser** l'expression de λ.

On sait que dans le modèle équivalent du moteur asynchrone on a :

+----------------------------------+-------+--------------------------+
| $$C_{\max} =                     | et    | $$g_{0} = \fr            |
| \frac{3pV^{2}}{2L_{2}\omega ²}$$ |       | ac{R_{2}}{L_{2}\omega}$$ |
+==================================+=======+==========================+
| V : la tension simple aux bornes |       |                          |
| d'un enroulement                 |       |                          |
|                                  |       |                          |
| L~2~ : l'inductance secondaire   |       |                          |
| ramenée au primaire              |       |                          |
|                                  |       |                          |
| R~2~ : la résistance rotorique   |       |                          |
| secondaire ramenée au primaire   |       |                          |
+----------------------------------+-------+--------------------------+

**10. Justifier** que λ est constant lorsque l'on commande le moteur
avec un variateur de vitesse à V/f constant.

Dans la suite du problème, on prendra λ = 0,0453 N.m.s.rad^-1^.

**11.** Sachant que le moteur doit tourner à la vitesse Ω~m~ = 139
rad.s^-1^ avec un couple C~maff~ = 0,3 Nm pour respecter le cahier des
charges, quelle devra être la vitesse de synchronisme **Ω~s~** ? **En
déduire** la valeur de la fréquence f~v~ à programmer dans le variateur
de vitesse du moteur pour respecter le cahier des charges.

**[\
]{.underline}**

![](13-MAS-MS/Cours/pandoc/media/image87.png){width="0.6536603237095363in"
height="0.5394728783902012in"}**ÉTUDE DE L'ENTRAÎNEMENT DE LA BROCHE
D'UN CENTRE D'USINAGE**

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source :]{.underline} Concours CCP TSI
2002)*

**Mise en situation**

![C:\\FICHIERS\\Archivage\\Doisneau\\Matériels\\Pôle
Prod\\C300H\\Photos\\C300H.jpg](13-MAS-MS/Cours/pandoc/media/image88.jpeg){width="1.95in"
height="2.216666666666667in"}Le système, objet de ce problème, est un
centre d\'usinage horizontal (cf. photo) palettisé, à commande numérique
quatre axes (X, Y, Z et B).

Ce centre d\'usinage, de conception moderne, a été développé afin
d\'assurer une très haute précision et des performances élevées. Le
bâti, en béton de synthèse précontraint, est renforcé de fibres et
matériaux spéciaux. Il apporte à cette machine d\'excellentes
caractéristiques d\'amortissement des vibrations.

Les guidages sont assurés par des glissières sur rails prismatiques et
cages à aiguilles. Le tout offre un ensemble sans jeu, compact, rigide
et graissé à vie.

L\'entraînement de la table en X et Z et de la broche en Y est assuré
par des moteurs asynchrones triphasés et des systèmes vis / écrou à
billes de précision. Le contrôle de position est assuré par des codeurs
incrémentaux. Le travail qui suit concerne l\'étude de l'alimentation du
moteur dela broche.

> Présentation de la chaîne de conversion de l'énergie

u~T~(t) = Û~T~.sinωt = U~T~.√2.sinωt soit u~T~(θ) = Û~T~.sinθ =
U~T~.√2.sinθ en posant θ = ωt

En sortie du redresseur (redresseur monophasé non commandé), le rôle du
filtre est de :

> Lisser le courant fourni par le redresseur
>
> Fournir une tension parfaitement continue à l'onduleur de tension

**Etude de la charge mécanique**

[Objectif de l'étude :]{.underline}

**Déterminer** les caractéristiques de la machine pour son
fonctionnement nominal et les limites de fonctionnement de l'ensemble
machine+charge

Le moteur utilisé a les caractéristiques suivantes pour une alimentation
à 50 Hz :

  ----------- ---------- ------------ ------------- ----------- -----------
  P~N~        C~N~       n~N~         I~N~          C~d~        C~max~

  \[kW\]      \[Nm\]     \[tr/min\]   \[A\]         C~N~        \[Nm\]

  **5,35**    **35**     **1460**     **9,5**       **2,4**     **89,3**
  ----------- ---------- ------------ ------------- ----------- -----------

P~N~: puissance nominale C~N~ : couple nominal n~N~: vitesse nominale du
rotor

I~N~: courant nominal C~d~/C~N~: rapport entre le couple de démarrage et
C~N~ C~max~: couple maximal

Toutes les pertes de la machine sont négligées, exceptées les pertes
Joules rotoriques.

**7.** A partir des données constructeur dans le cas où la machine est
alimentée par le réseau industriel **230 V / 400 V** et pour une
utilisation au point nominal de la machine, **déterminer** les grandeurs
suivantes :

-   Le nombre de paires de pôles **p** de la machine

-   La fréquence de rotation **N~s~**, exprimée en tr/min du champ
    > statorique

-   Le glissement nominal **g~N~**

-   La puissance transmise au rotor **P~tr~**

-   Les pertes Joules rotoriques **P~jr~**

-   Le rendement **η**du moteur

-   Le facteur de puissance **cos ϕ**

Dans le plan couple-vitesse, le lieu de fonctionnement autorisé pour la
machine d'entraînement est limité par les caractéristiques suivantes :

-   De 0 à 1500 tr/min : C~motMAX~ = 35 Nm

-   De 1500 tr/min à 6000 tr/min : P~uMAX~ = C~motMAX~Ω = 5,35 kW

avec Ω vitesse de rotation mécanique en rad/s.

Entre la machine d'entraînement et la charge mécanique, il y a une boite
de vitesse, que l'on considèrera sans pertes, qui comporte deux rapports
de réduction. Le couple résistant de la charge mécanique ramené au
niveau du moteur d'entraînement peut s'exprimer par :

-   C~res~ = C~01~+k~1~Ω pour le premier rapport de réduction (pour 0 ≤
    > N ≤ 1000 tr/min)

-   C~res~ = C~02~+k~2~Ω pour le second rapport de réduction (pour N \>
    > 1000 tr/min)

avec C~01~ = 12 Nm, k~1~ = 0,15 Nm/rad.s^-1^, C~02~ = 1 Nm et k~2~ =
0,0125 Nm/rad.s^-1^.

**8. Tracer** dans le plan couple-vitesse, **C(Ω)**, le lieu de
fonctionnement autorisé pour le moteur d'entraînement et les
caractéristiques de la charge.

**9.** A partir du graphe précédent, à Ω = 0 rad/s, **indiquer** la
valeur maximale que peut prendre le couple accélérateur (C~acc~ =
C~mot~ - C~res~).

**10a. Indiquer** le point de fonctionnement atteint avec le premier
rapport de réduction.

**10b.** Lorsque la vitesse atteint 1000 tr/min, on enclenche le second
rapport de réduction. **Donner** alors la valeur du couple accélérateur
**C~acc~** et le point de fonctionnement qui peut être atteint.

**Etude de la machine asynchrone et de l'onduleur de tension**

[Objectifs de l'étude :]{.underline}

**Déterminer** le couple accélérateur maximal possible avec
l'association onduleur+MAS et la commande scalaire de type U/f = cte
utilisée.

**Déterminer** la fréquence d'alimentation permettant d'obtenir le
couple accélérateur maximal possible au démarrage

Afin de faire varier la fréquence de rotation de la broche, l'onduleur
de tension permet de délivrer à la machine asynchrone des tensions
alternatives sinusoïdales de fréquence et d'amplitude variables.

On note **v~1~(t)**, **v~2~(t)** et **v~3~(t)** les tensions simples
appliquées aux bornes de chaque phase de la machine asynchrone.

avec : ![](13-MAS-MS/Cours/pandoc/media/image90.wmf), **U~C~** étant la
tension constante en entrée de l'onduleur de tension, U~c~ = 650V

**k** est un paramètre de commande : k ∈ \[0;1\]

ω = 2πf où **f** est la fréquence des tensions en sortie de l'onduleur

On désire maintenir constant le rapport de l'amplitude de la tension sur
la fréquence. Pour une fréquence de 50 Hz, la tension efficace entre
phases, notée **U**, atteint la valeur limite de 400 V. La tension
simple a une valeur efficace notée V~eff~ = 230V. La commande utilisée
pour l'onduleur est de type U/f = cte.

**11. Tracer** la courbe donnant le coefficient **k** en fonction de la
fréquence et ceci pour une fréquence **f** comprise entre **0** et **80
Hz**.

On donne le schéma simplifié équivalent d'une phase de la machine
asynchrone ci-contre.

[Application numérique :]{.underline}

V~eff~ = 230 V ; ω = 2πf rad/s ; p = 2 ; L~m~ = 180 mH ; L~f~ = 18 mH ;
R = 0,77 Ω

**12.** En calculant la puissance électromagnétique dissipée dans la
résistance **R/g**, **donner** l'expression du couple électromagnétique
**C~em~**.

**13. Donner** l'expression du couple électromagnétique maximal puis
**calculer** sa valeur numérique pour f = 50 Hz.

Sur le document réponse ont été représentées quatre caractéristiques
\"couple électromagnétique en fonction de la vitesse de rotation\" de la
machine asynchrone alimentée par l'onduleur de tension.

**14.** Pour chaque caractéristique, **déterminer** graphiquement la
vitesse de synchronisme (exprimée en tr/min), le couple maximum et en
déduire la fréquence et la valeur efficace des tensions appliquées. Les
résultats seront présentés dans un tableau.

**15.** Sachant que le couple résistant est constant et a une valeur de
35 Nm, **déterminer** graphiquement pour chaque caractéristique, le
point de fonctionnement mécanique (couple et vitesse) et en déduire le
point de fonctionnement électrique\* (valeurs efficaces des tensions
simples et des courants de ligne). On présentera les résultats dans un
tableau.

*\* On pourra établir l'expression de l'impédance complexe.*

**16 .**A Ω = 0, **indiquer** le couple accélérateur maximum que l'on
peut obtenir. **En déduire** la fréquence f d'alimentation.

**\
**

**DOCUMENT RÉPONSE**

**[\
]{.underline}**

![4029](13-MAS-MS/Cours/pandoc/media/image91.jpeg){width="0.46875in"
height="0.625in"}**MAISON HANTEE**

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source]{.underline} : ATS 2009)*

**Mise en situation**

Vieilles pierres, couloirs sans fin et pièges maléfiques \... il faut
avoir le cœur bien accroché pour s\'aventurer dans ces lieux \... Cette
installation est composée de seize véhicules indépendants roulant sur
une piste béton de 192 mètres. Cette piste reçoit en son centre un rail
de guidage qui fixe la trajectoire des véhicules.

![](13-MAS-MS/Cours/pandoc/media/image92.png){width="2.8493055555555555in"
height="2.2618055555555556in"}Chaque voiture peut recevoir deux
personnes au maximum. Les passagers ne conduisent pas, ils sont
uniquement spectateurs. Ils sont assis sur une nacelle tournante, libre
en rotation. Un système de contrepoids placé sous l\'assise, ainsi que
l\'inclinaison de la piste, permettent une bonne orientation des
visiteurs devant les scènes du décor.

Une voie de garage peut contenir sept véhicules permettant ainsi le
délestage de la piste pour adapter le nombre de véhicules à la
fréquentation.

Un opérateur proche du quai d\'embarquement a en charge l\'exploitation,
il doit gérer les flux des départs, contrôler les débarquements et
surveiller l\'évolution sur la piste.

**[Données :]{.underline}**

-   Vitesse du véhicule : V~C~ = 1 à 1,3 m/s = V~M~

-   Variation de vitesse maximale tolérée : 10%

-   Pente maximale en montée : 6% ; en descente : 7%

-   Tension d'alimentation : U~1~, réseau EDF (250 V, 50 Hz)

L\'analyse de l\'activité du service maintenance fait ressortir les
points suivants :

-   Changements fréquents des pare-chocs dus aux collisions entre
    véhicules

-   Remplacement des moteurs (6 moteurs par saison)

    **Étude de l'alimentation de la MAS**

![](13-MAS-MS/Cours/pandoc/media/image93.jpeg){width="4.663888888888889in"
height="2.8673611111111112in"}La solution initiale utilisant une machine
à courant continu pour chaque véhicule n\'a pas été retenue par le
service maintenance qui a préféré la remplacer par un moteur asynchrone
triphasé associé à un variateur de vitesse (convertisseur de fréquence).
La raison essentielle de ce choix est la maintenance réduite de ce type
de moteur par rapport au moteur à courant continu (pas d\'usure de
balais, pas de court-circuit dû à la présence de poussière de carbone
dans les moteurs).

Schéma de principe de l\'installation

L\'alimentation des véhicules se fait en 230 V, 50 Hz, chaque véhicule
est équipé d\'un automate programmable industriel, tous les automates
sont en liaison avec un automate maître fixe situé dans la station par
un réseau modbus.

Les moteurs asynchrones triphasés SEW modèle DV 100 M4 sont alimentés
par des variateurs de vitesse, l\'entrée de consigne de ces variateurs
est fournie par une sortie analogique de l\'automate. La transmission
mécanique est dimensionnée de manière à ce que la vitesse de translation
du chariot soit de 1,3 m/s lorsque le moteur tourne à n = 1400 tr/min,
le couple utile à la sortie du moteur est compris entre **10 Nm** et
**-4 Nm**.

L\'expression du couple électromagnétique du moteur asynchrone en
fonction du glissement déduite des propriétés du schéma équivalent
monophasé est de la forme :
$C_{em} = \frac{3U^{2}}{\Omega_{S}}.\frac{R_{2}.g}{R_{2}^{2} + X_{2}^{2}.g^{2}}$

Avec : C~em~ : couple électromagnétique

> U : valeur efficace de la tension composée
>
> Ω~S~ : vitesse angulaire de rotation du champ tournant
>
> R~2~ : résistance d\'une phase du rotor, ramenée au stator
>
> X~2~ : réactance d\'une phase du rotor ramenée au stator avec X~2~ =
> L~2~ω ; ω = 2πf où f est la fréquence des courants statoriques
>
> $g = \frac{\Omega_{S} - \omega_{m}}{\Omega_{S}}$ : glissement
>
> ω~m~ : vitesse angulaire de rotation du rotor du moteur

Le moteur est connecté en triangle.

Le couple de pertes est négligé : C~em~ = C~u~ (couple utile).

![](13-MAS-MS/Cours/pandoc/media/image94.jpeg){width="3.01875in"
height="2.441666666666667in"}Dans la zone de fonctionnement du moteur,
la caractéristique C~em~ = f(g) peut être modélisée par une droite
paramétrée par Ω~S~. Il convient de déterminer l\'équation de cette
droite.

Figure 1: Caractéristique C~em~=f(g)

La caractéristique C~em~ = f(g) passe par un maximum C~M~ pour une
valeur g~M~ du glissement (voir figure ci-contre).

**1.** En utilisant les propriétés de la dérivée, **déterminer**
l\'expression de g~M~ en fonction de R~2~ et X~2~.

**2. Donner** l\'expression de C~M~ en fonction de U, Ω~S~ et X~2~.

**3. Montrer** que C~em~ peut se mettre sous la forme :

> $$C_{em} = 2.C_{M}.\frac{x}{1 + x^{2}}\ avec\ x = \frac{g}{g_{M}}$$

Le moteur utilisé a les caractéristiques suivantes pour une alimentation
à 50 Hz :

+----------+------+------+------+------+------+------+------+------+
| Type     | P~N~ | M~N~ | n~N~ | I~N~ | cosϕ | l    | J~   | M~   |
| moteur   |      |      |      |      |      | ~A~/ | Mot~ | max~ |
|          | (kW) | (Nm) | (tr/ | \    |      | l~N~ |      |      |
| 380-415  |      |      | min) | (A\) |      |      | (    | (Nm) |
| V        |      |      |      |      |      |      | kg.m |      |
|          |      |      |      |      |      |      | ^2^) |      |
+----------+------+------+------+------+------+------+------+------+
| DV 100   | 2,2  | 15   | 1410 | 4,9  | 0,83 | 5,9  | 53   | 40   |
| M4       |      |      |      |      |      |      |      |      |
+----------+------+------+------+------+------+------+------+------+

> P~N~: puissance nominale cosϕ : facteur de puissance
>
> M~N~ : couple nominal l~A~/l~N~ : rapport entre le courant de
> démarrage et I~N~
>
> n~N~: vitesse nominale du rotor J~mot~ : inertie du moteur
>
> I~N~: courant nominal M~max~ : couple maximal

**4. Exprimer** la vitesse angulaire de rotation du champ tournant Ω~S~
en fonction de la fréquence f des courants statoriques et du nombre de
paires de pôles p.

**5.** En utilisant les caractéristiques du moteur et en considérant
qu\'en fonctionnement nominal le glissement est faible, **déterminer**
le nombre de paires de pôles p du moteur asynchrone.

**6.** En utilisant le résultat de la question **3** et les
caractéristiques du moteur, **calculer** la valeur de g~M~ sachant que x
est inférieur à 1.

Les résultats précédents permettent d\'obtenir une expression linéarisée
de la caractéristique de couple C~em~ = f(g) autour de la vitesse de
synchronisme. L\'expression de C~em~ devient alors C~em~ = 1,65×Ω~s~×g.

Nous allons déterminer la fréquence de la tension d\'alimentation pour
que le chariot se déplace à 1,3 m/s, lorsque le couple moteur est de 10
Nm.

**7. Donner** l\'expression de C~em~ en fonction de f, p et ω~m~
(vitesse angulaire de rotation du rotor en rad/s).

**8. Calculer** la fréquence f des courants d\'alimentation du moteur
pour que le chariot se déplace à 1,3 m/s lorsque le couple moteur est de
10 Nm.

Le couple pouvant devenir négatif, la structure du convertisseur doit
permettre cette inversion. Il faut d\'abord s\'assurer de la
réversibilité du système utilisé.

![](13-MAS-MS/Cours/pandoc/media/image95.png){width="5.0in"
height="1.2169805336832895in"}

Schéma de principe du convertisseur de fréquence

Les transistors sont considérés comme des interrupteurs commandés et le
dispositif de commande n\'est pas représenté.

**9.** Le schéma de principe du convertisseur de fréquence est
représenté sur la figure ci-dessus. **Conclure** en explicitant la
réponse sur la réversibilité demandée.

Le cahier des charges impose une variation de vitesse maximale tolérée
de 10%. Nous allons vérifier ce critère d\'appréciation sur cette
nouvelle solution.

**10.** La fréquence des courants d\'alimentation étant celle calculée à
la question **8**, **calculer** la vitesse de rotation du moteur lorsque
le couple passe à -4 Nm.

**11.** En considérant les variations extrêmes de la vitesse en fonction
des variations du couple, **conclure** quant à la nécessité de réguler
la vitesse.

**12. Conclure** quant aux avantages et aux inconvénients de
l\'utilisation des moteurs asynchrones.

**[\
]{.underline}**

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![](13-MAS-MS/Cours/pandoc/media/image96.png){width="0.7502963692038496in"
height="0.726415135608049in"}

**TELESIEGE DEBRAYABLE 6 PLACES**

*([Source :]{.underline} CCP TSI 2016)*

**Mise en situation**

L'étude proposée dans cet exercice porte sur les moteurs de secours du
télésiège débrayable 6 places (TSD6) « Biollay », mis en activité
récemment au sein de la station de Courchevel. Il a été conçu par la
société Poma.

![C:\\Users\\Benoit\\Documents\\CPGE\\Concours_TSI\\Sujets_écrit\\Sujet_écrit_2015\\Ressources\\538055_469097636460151_1077262434_n.jpg](13-MAS-MS/Cours/pandoc/media/image97.jpeg){width="5.131944444444445in"
height="2.3833333333333333in"}

[Extrait du cahier des charges :]{.underline}

  -----------------------------------------------------------------------
  Vitesse du câble en marche secours              de 0,8 m.s^-1^ à 1,8
                                                  m.s^-1^
  ----------------------------------------------- -----------------------
  Nombre de moteurs en marche secours normal      2

  Nombre de moteurs en marche secours dégradé     1
  -----------------------------------------------------------------------

[Grandeurs et valeurs numériques :]{.underline}

  -----------------------------------------------------------------------
  **Eléments**           **Caractéristiques et notations**
  ---------------------- ------------------------------------------------
  2 Moteurs de secours   Couple d'un seul moteur de secours : C~ms~
  asynchrones triphasés  
  SIEMENS 75 kW de       
  référence              
  1LE1501-2DA03-4AA4     

                         Vitesse de rotation : ω~ms~

                         Puissance utile : P~u~ = 75 kW

                         Tension nominale : U = 400 V

                         Courant nominal : I = 133 A

                         Fréquence : f = 50 Hz

                         Vitesse de rotation nominale : N~n~ = 2 978
                         tours/min

                         Rendement : η = 93,8 %

                         Facteur de puissance : cosϕ = 0,87

  2 Réducteurs par       Rapport de réduction primaire : r~1~ =
  moteur de secours      ω~ms~/ω~pignon~ = 32,7

                         Réduction secondaire : r~2~ ; couronne :
                         Z~c~$\ $= 220 et pignon : Z~p~$\ $= 16

                         Rendement des deux réducteurs : η = 1

  Poulie motrice         Rayon : R~p~ = 2,45 m
  -----------------------------------------------------------------------

**Couple moteur nécessaire**

[Objectif :]{.underline} **Déterminer** le couple des moteurs de secours
nécessaire à l'évacuation des skieurs.

Lors d'un dysfonctionnement de la motorisation principale ou lors d'une
coupure électrique, les deux moteurs électriques de secours prennent le
relais et permettent d'évacuer les skieurs. Il est alors nécessaire de
désaccoupler le réducteur principal de la poulie motrice. En cas de
secours, deux moteurs électriques asynchrones sont donc utilisés. La
puissance de chaque moteur est transmise à un premier réducteur de
rapport de réduction r~1~, puis transmise à un ensemble pignon-couronne,
la couronne étant solidaire de la poulie motrice. Ceci est illustré sur
la figure ci-contre. Le nombre de dents de la couronne est noté Z~c~ et
le nombre de dents du pignon est noté Z~p~.

[Hypothèses]{.underline}

On considérera les cas limites de fonctionnement :

-   Au début de l'évacuation à la montée, 100 % des sièges sont pleins,
    > entrainant une tension du câble T~B~ = 337 000 N

-   A la fin de l'évacuation à la montée, 100 % des sièges sont vides
    > entrainant une tension du câble T~B~ = 282 000 N

Du début à la fin de l'évacuation, les sièges à la descente sont vides
entrainant une tension du câble T~A~ = 260 000 N

On considérera que l'on se place en régime établi et que les liaisons
sont parfaites.

**1. Donner** l'expression de C~ms~ en fonction de T~B~, T~A~ et des
différentes caractéristiques introduites dans la Mise en situation.
**Faire** l'application numérique de C~ms~ au début de l'évacuation et à
la fin de l'évacuation.

Pour la suite, on prendra les valeurs suivantes :

-   C~ms~$\ $= 210 N.m au début de l'évacuation

-   C~ms~$\ $= 60 N.m à la fin de l'évacuation

    **Validation des moteurs de secours**

[Objectif :]{.underline} **Valider** la solution retenue. Les moteurs
doivent assurer la marche de secours avec une vitesse du câble comprise
entre 0,8 m.s^-1^ et 1,8 m.s^-1^ en marche avant ou arrière. Dans le cas
d'une défaillance d'un des moteurs de secours, l'autre pourra assurer le
fonctionnement.

La solution choisie par la société Poma est le moteur asynchrone
triphasé SIEMENS 75 kW de référence 1LE1501-2DA03-4AA4. Les
caractéristiques données par le constructeur sont regroupées dans la
Mise en situation.

**2.** Pour une utilisation au point de fonctionnement nominal de la
machine, **déterminer** les grandeurs suivantes :

-   ![](13-MAS-MS/Cours/pandoc/media/image98.png){width="2.986111111111111in"
    > height="1.8541666666666667in"}La fréquence de rotation N~S~,
    > exprimée en tours par minute du champ tournant statorique

-   Le nombre de paires de pôles p de la machine

-   Le glissement nominal g~n~.

Le choix d'un moteur ne peut être validé que si celui-ci peut assurer le
fonctionnement dans le cas d'un mode dégradé (un seul moteur
fonctionnant).

Pour cela, des essais à vide et à rotor bloqué, donnés par le
constructeur, ont permis d'établir le modèle équivalent d'une phase du
moteur asynchrone.

> V~1~ = 230 V R'~2~ = 10,5 mΩ X'~2~ = 0,23 Ω X~0~ = 4,76 Ω

Modèle équivalent d'une phase du moteur asynchrone

**3. Déterminer** l'expression de la valeur efficace du courant I'~2~ en
fonction de V~1~, X'~2~, R'~2~ et g.

Pour la suite, on négligera les pertes mécaniques du rotor, donc le
couple mécanique utile sera égal au couple électromagnétique.

**4a. Déterminer** les expressions de la puissance transmise au rotor
P~tr~ et de la puissance mécanique P~méca~ en fonction de V~1~, X'~2~,
R'~2~ et g.

**4b.** **Montrer** que le couple électromagnétique développé par la
machine peut se mettre sous la forme :

$C_{ms} = \frac{3.p.V_{1}^{2}}{\omega}.\frac{\frac{R_{2}^{'}}{g}}{\left( \frac{R_{2}^{'}}{g} \right)^{2} + \left( X_{2}^{'} \right)^{2}}$
avec ω = 2.π.f

**4c. Déterminer** le glissement g~M~$\ $ tel que le couple
électromagnétique C~ms~ soit maximal en fonction de R'~2~ et de X'~2~.
Faire l'application numérique.

Pour la suite, on prendra g~M~ = 0,046.

[Fonctionnement « dégradé » de la marche de secours]{.underline}

Remarque : Les glissements aux points de fonctionnement stables sont
[inférieurs]{.underline} au glissement g~M~.

**5a.** **Déterminer** les glissements g'~1~ $\ $et g'~2~ pour des
couples moteurs respectifs C'~ms1~ = 420 Nm (début d'évacuation) et
C'~ms2~ = 120 N.m (fin d'évacuation).

**5b. En déduire** les vitesses de translation en début et en fin
d'évacuation.

[Conclusion]{.underline}

**6.** À partir des résultats obtenus aux questions précédentes,
**valider** le choix du moteur de secours retenu.

**[\
]{.underline}**

![](13-MAS-MS/Cours/pandoc/media/image99.png){width="0.9970406824146981in"
height="0.726415135608049in"}

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**VEHICULE AUTO GUIDÉ**

*([Source :]{.underline} ATS 2014)*

**Mise en situation**

Le VAG est un véhicule autonome à guidage laser. Il est utilisé en
milieu hospitalier pour le transport de déchets, plateaux repas, linges
dans les parties non accessibles au public. Seules des personnes
autorisées peuvent y pénétrer. On peut donc considérer qu'il s'agit de
zones propres.

L'étude proposée porte sur le respect des conditions de sécurité pour la
circulation des chariots à proximité du personnel de l'hôpital.

L'avancement du VAG est assuré par un moteur-roue **1**. L'arbre **7**
est l'arbre moteur (le moteur n'est pas représenté). L'énergie mécanique
est transmise à la roue **1** par l'intermédiaire d'un train
d'engrenages.

![](13-MAS-MS/Cours/pandoc/media/image100.png)

Dans le mouvement de translation rectiligne du chariot, le point A lié
au carter **5**, a pour vitesse
![](13-MAS-MS/Cours/pandoc/media/image101.wmf). Le roulement de la roue
sur le sol **0** se fait sans glissement.

Avec r rayon de la roue d'entraînement, r~1~ le rapport de réduction
entre le moteur et la roue, ω~7/6~ la vitesse de rotation du rotor en
rd·s^-1^, la vitesse du chariot a pour expression :

> ![](13-MAS-MS/Cours/pandoc/media/image102.wmf) avec r = 105 mm et
> ![](13-MAS-MS/Cours/pandoc/media/image103.wmf)

La plage de vitesse stabilisée en ligne droite du VAG, V~A,5/0~, doit
être ajustable entre 0,1 et 1,2 m·s^-1^.

[Données utiles :]{.underline}

La tension continue issue du pack de batterie est de 24 V.

Le moteur est piloté par un variateur de vitesse non étudié ici.

Le moteur est de type asynchrone triphasé couplé par construction en
étoile et de caractéristiques nominales suivantes (lecture de la plaque
signalétique) :

  -----------------------------------------------------------------------
  Fréquence nominale d'alimentation du     Tension efficace entre phases
  stator f~s~ = 110 Hz                     U~n~ = 14,5 V
  ---------------------------------------- ------------------------------
  Vitesse nominale en charge N~n~ = 3100   Puissance utile mécanique P~u~
  tr·min^-1^                               = 850 W

  Facteur de puissance à charge nominale   Rendement nominal η~n~ = 0,76
  F~p~ = cosφ = 0,79                       
  -----------------------------------------------------------------------

[Remarques :]{.underline}

Pour l'étude réalisée (déplacement en ligne droite), le système
d'orientation est immobile

On posera N = ω~7/6~ × $\frac{30}{\pi}$

**Détermination de la loi entrée sortie entre le variateur et la roue**

A partir des indications et caractéristiques du moteur

**1. Donner** la relation liant la vitesse de synchronisme N~s~ en
tr·min^-1^ et la fréquence f en Hz de l'alimentation. On notera p le
nombre de paires de pôles.

**2. Introduire** le glissement g et **exprimer** la relation liant N~s~
et la vitesse du rotor N**.** **En déduire** en justifiant par une
hypothèse simplificatrice, le nombre de paires de pôles p du moteur et
la vitesse de synchronisme N~s~.

**3. Exprimer** puis **calculer** le glissement nominal du moteur g~n~
en % et son couple nominal C~n~ en Nm.

**4. Etablir** la relation entre la vitesse du rotor du moteur ω~7/6~ en
rd·s^-1^, la fréquence f des tensions de sortie du variateur et le
glissement g. **Déduire** alors la relation entre la vitesse du chariot
V~A,5/0~, la fréquence f et le glissement g.

**5.** En admettant pour le moteur en charge un glissement constant g =
6%, **exprimer** la vitesse du chariot sous la forme V~A,5/0~ = K·f et
**déterminer** l'expression de K et sa valeur numérique. **Déduire** la
plage de fréquence f nécessaire pour que la vitesse V~A,5/0~ du VAG
respecte la plage de vitesse fixée plus haut.

La vitesse maximale du moteur est fixée à +2620 tr·min^-1^.

**6. Utiliser** l'annexe variateur « Entrée numérique de contrôle de la
vitesse » et **donner** en justifiant, la valeur numérique décimale à
programmer pour obtenir cette vitesse, puis sous forme binaire les deux
octets Byte 0 et Byte 1.

Le couple d'un moteur asynchrone est admis constant si le rapport U/f
est également constant. On utilisera le rapport U/f du point nominal.

**7. Déduire** numériquement la plage de la tension efficace U entre
phases nécessaire pour maintenir le couple du moteur constant pour la
plage de vitesse considérée. **Vérifier** sa compatibilité avec la
source de tension continue disponible.

**ANNEXE : Variateur de roue**

+-----------------------------------+----------------------------------+
| **Variateur : caractéristiques de |                                  |
| puissance**                       |                                  |
+===================================+==================================+
| ![](13-M                          |                                  |
| AS-MS/Cours/pandoc/media/image104 |                                  |
| .png){width="6.561805555555556in" |                                  |
| height="1.90625in"}               |                                  |
+-----------------------------------+----------------------------------+
| Housing : *Boitier*               | Nominal output current :         |
|                                   | *Courant de sortie nominal*      |
| Nominal battery voltage :         |                                  |
| *Tension nominale de la batterie* | Maximum output current :         |
|                                   | *Courant de sortie maximal*      |
| Input voltage range permanent :   |                                  |
| *Plage de tension d'entrée        | Output voltage : *Tension de     |
| permanente*                       | sortie*                          |
|                                   |                                  |
| Short time : *Temps court \< 30s* |                                  |
+-----------------------------------+----------------------------------+
| **Variateur : Paramètres des      |                                  |
| rampes d'accélération et de       |                                  |
| décélération**                    |                                  |
+-----------------------------------+----------------------------------+
| ![](13-M                          |                                  |
| AS-MS/Cours/pandoc/media/image105 |                                  |
| .png){width="6.311805555555556in" |                                  |
| height="1.6354166666666667in"}    |                                  |
+-----------------------------------+----------------------------------+
| Par.no. : *Numéro du paramètre à  | The parameter sets the ramp      |
| programmer*                       | slope for speed acceleration     |
|                                   | (increasing numéric rpm) :       |
| Name : *Nom du paramètre*         |                                  |
|                                   | *Le paramètre définit la pente   |
| Range : *Plage de réglage*        | de la rampe d\'accélération de   |
|                                   | vitesse (augmentation numérique  |
| Units : *Unités*                  | de la vitesse en tr.min^-1^ pour |
|                                   | une seconde)*                    |
| Default : *Valeur programmée par  |                                  |
| défaut*                           | The parameter sets the ramp      |
|                                   | slope for speed deceleration     |
| Acceleration ramp : *Rampe        | (decreasing numéric rpm) :       |
| d'accélération*                   |                                  |
|                                   | *Le paramètre définit la pente   |
| Deceleration ramp : *Rampe de     | de la rampe de décélération de   |
| décélération*                     | vitesse (diminution numérique de |
|                                   | la vitesse en tr.min^-1^ pour    |
| Rpm/s : *en tour par minute /     | une seconde)*                    |
| seconde (pour l'accélération et   |                                  |
| la décélération)*                 |                                  |
+-----------------------------------+----------------------------------+
| **Variateur : Entrée numérique de |                                  |
| contrôle de la vitesse**          |                                  |
+-----------------------------------+----------------------------------+
| ![](13-M                          |                                  |
| AS-MS/Cours/pandoc/media/image106 |                                  |
| .png){width="7.009722222222222in" |                                  |
| height="0.875in"}                 |                                  |
+-----------------------------------+----------------------------------+
| Byte : *Octet*                    | Scale : *Echelle*                |
|                                   |                                  |
| Low : *Partie basse*              | L'incrément de vitesse vaut 0,25 |
|                                   | ou 1/4 tour.min^-1^              |
| High : *Partie haute*             |                                  |
|                                   | Range / Setting :                |
| Data : *Donnée*                   |                                  |
|                                   | *Plage numérique programmable /  |
| Set speed command : *Définit la   | Variation de vitesse             |
| commande en vitesse*              | correspondante en tr.min^-1^*    |
|                                   |                                  |
| [La vitesse est donc définie par  | [Le point est pour la plage le   |
| un mot de 16 bits incluant le bit | séparateur des                   |
| de signe à gauche]{.underline}    | milliers]{.underline}            |
+-----------------------------------+----------------------------------+

**[\
]{.underline}**

**DEPOSE BAGAGE AUTOMATIQUE**

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source]{.underline} : Centrale-Supélec
TSI 2018)*

**Mise en situation**

![](13-MAS-MS/Cours/pandoc/media/image107.emf){width="2.8673611111111112in"
height="1.8097222222222222in"}![](13-MAS-MS/Cours/pandoc/media/image108.emf){width="2.848611111111111in"
height="2.0027777777777778in"}[Présentation du système]{.underline}

Depuis déjà plusieurs années, le processus d'enregistrement des
passagers dans les aéroports est en train de vivre une mutation en
évoluant de la « banque d'enregistrement » classique vers une idée de «
dépose bagages » automatisée.

Le système de DBA permet au passager de déposer un bagage en toute
autonomie.

[Problématique]{.underline}

La chaine d'énergie du basculeur est notamment constituée d'une machine
asynchrone (MAS) triphasée alimentée par un variateur de vitesse
connecté au réseau triphasé 230 V / 400 V. La machine asynchrone
entraine l'ensemble bielle-manivelle du basculeur via un réducteur de
rapport de réduction k = $\frac{1}{107,7}$

Compte tenu du glissement dépendant du couple résistant imposé par la
charge, la vitesse de rotation de l'arbre de la machine asynchrone en
régime établi est différente de sa vitesse de synchronisme. Cette
dernière est directement liée à la valeur de réglage du paramètre
fréquence du variateur (noté F~par~).

Les rampes d'accélération et de décélération ne sont pas traitées.

[Objectif]{.underline}

Déterminer la fréquence F~par~ en utilisant la partie utile de la
caractéristique couple-vitesse de la MAS et l'expression du couple
résistant.

**Paramètres du schéma équivalent d'un enroulement statorique de la
MAS**

[Objectif :]{.underline} Proposer un modèle de la MAS et en déterminer
les paramètres.

Le fabricant de la machine asynchrone qui entraîne le basculeur donne
les informations suivantes sur sa plaque signalétique :

  ------------- ------------- --------------- ---------------- ---------- ------------------------------------------------------------- ----------------------------------------------------------------
  **Puissance   **Moteur      **Fréquence**   **Vitesse        **Couple   $$\frac{\mathbf{C}_{\mathbf{d}}}{\mathbf{C}_{\mathbf{n}}}$$   $$\frac{\mathbf{C}_{\mathbf{\max}}}{\mathbf{C}_{\mathbf{n}}}$$
  utile**       bitension**                   nominale**       nominal                                                                  
                                                               C~n~**                                                                   

  730 W         230/400 V     50 Hz           1 430 tr·min⁻¹   4,9 N·m    1,16                                                          2,6
  ------------- ------------- --------------- ---------------- ---------- ------------------------------------------------------------- ----------------------------------------------------------------

C~d~ est le couple de démarrage (ω~mot~ = 0)

C~max~ est le couple maximal

Le schéma équivalent retenu pour un enroulement statorique est
représenté ci-contre.

On note :

-   R (Ω) la résistance rotorique ramenée au stator

-   X = L·ω (Ω) la réactance de fuite rotorique ramenée au stator

-   L (H) l'inductance de fuite rotorique ramenée au stator

-   V (V) la tension aux bornes d'un enroulement statorique

-   I (A) l'intensité du courant parcourant un enroulement statorique

-   $g = \frac{\Omega_{s} - \Omega}{\Omega_{s}} = \frac{N_{s} - N}{N_{s}}$
    > le glissement

-   $\Omega_{s} = \frac{\omega}{p}$ (rad⋅s⁻¹) et N~s~ (tr⋅min^-1^) la
    > vitesse de synchronisme

-   Ω = ω~mot~ (rad⋅s⁻¹) et N (tr⋅min^-1^) la vitesse de l'arbre de la
    > MAS

-   ω = 2πf (rad⋅s^-1^) la pulsation des tensions et courants
    > statoriques

-   p le nombre de paires de pôles de la MAS

-   f (Hz) la fréquence des tensions et courants statoriques

Hypothèse simplificatrice : Seules les pertes par effet Joule rotoriques
seront prises en compte.

**1. Indiquer** la valeur efficace de la tension V aux bornes d'un
enroulement statorique pour un fonctionnement nominal de la MAS. **En
déduire** son couplage si elle était connectée directement au réseau 230
V / 400 V. **Justifier** votre réponse.

Par la suite, on conservera ce couplage lorsque la MAS sera alimentée
par le variateur de vitesse.

**2. Déterminer** le nombre de paires de pôles p de la MAS.
**Expliquer** la démarche. **En déduire** la valeur numérique de la
vitesse de synchronisme.

On désire déterminer la caractéristique couple/glissement de la MAS.

**3. Montrer** que l'expression du couple moteur C~m~ en fonction du
glissement peut s'écrire ainsi :
$C_{m} = \frac{3V^{2}}{\Omega_{s}} \cdot \frac{\frac{R}{g}}{{(\frac{R}{g})}^{2} + X^{2}}$

Pour arriver au résultat, exprimer la puissance transmise au rotor P~tr~
en fonction de V, R, X et g en exploitant le schéma équivalent
précédent. Les pertes mécaniques étant négligées, le couple
électromagnétique C~em~ est égal au couple moteur (ou couple utile)
C~m~. **Établir** ensuite la relation entre P~tr~, Ω~s~ et C~m~ puis
conclure.

**4.** La fonction C~m~(g) présente des extrema. **Déterminer** les
expressions littérales de g~max~ (glissement pour lequel C~m~(g~max~) =
C~max~) et de C~max~ en fonction de V, Ω~s~, R et X.

**5.** Connaissant le rapport $\frac{C_{\max}}{C_{n}}$, **déterminer**
la valeur numérique de l'inductance de fuite rotorique ramenée au stator
L.

**6.** Que vaut le glissement au démarrage ? **En déduire** l'expression
littérale du couple de démarrage C~d~.

**7.** Connaissant le rapport $\frac{C_{d}}{C_{n}}$, **déterminer** la
valeur numérique de la résistance rotorique ramenée au stator R. La
résolution admet deux solutions, on retiendra pour la suite la plus
petite des deux valeurs de R, qui contribue à un meilleur rendement de
la MAS.

**Expression du couple résistant C~r~(ω~mot~) exercé sur l'arbre
moteur**

[Objectif :]{.underline} Déterminer une expression du couple résistant
exercé par le mécanisme sur l'arbre de la MAS.

Pour la suite du problème, on s'intéressera uniquement à l'intervalle de
temps t ∈ \[0; 4 s\].

![](13-MAS-MS/Cours/pandoc/media/image109.png){width="5.35505249343832in"
height="3.3773589238845143in"}

**8.** Le couple résistant peut être assimilé à un couple de frottement
visqueux tel que C~r~ = K~r~×ω~mot~. **Déterminer** numériquement la
valeur de K~r~.

**Valeur de réglage du paramètre fréquence du variateur (F~par~)**

[Objectif :]{.underline} Déterminer la valeur de réglage du paramètre
fréquence par une résolution simplifiée.

La résolution rapide consiste à utiliser la partie utile de la
caractéristique couple-vitesse de la MAS dont l'expression en fonction
du glissement g est la suivante :
$C_{m} = \frac{p}{\omega} \cdot \frac{3V²}{R} \cdot g$

**9. Appliquer** le principe fondamental de la dynamique à l'arbre de la
MAS pour établir la relation entre C~m~(t), C~r~(t), ω~mot~(t) et J~e~
(J~e~ ; moment d'inertie équivalent rapporté sur l'arbre moteur).
**Montrer** qu'en régime permanent (à vitesse constante) C~m~(t) =
C~r~(t).

**10. Exprimer** le glissement g en fonction de f, ω~mot~ et p

**11.** Le variateur de vitesse fonctionne à $\frac{V}{f}$ constant. À
l'aide des expressions précédentes, **déterminer** la valeur numérique
de la pulsation ω des tensions et courants statoriques de la MAS pour
que son arbre tourne à 135,3 rad⋅s^1^ en régime établi. **En déduire**
la valeur de réglage du paramètre fréquence du variateur (F~par~). Pour
l'application numérique, on prendra R = 9,3 Ω.

[\
]{.underline}

[Objectif :]{.underline} Déterminer la valeur de réglage du paramètre
fréquence par une résolution numérique.

La résolution numérique consiste à utiliser un programme écrit en
langage Python qui va permettre de minimiser la fonction f = C~m~(t) --
C~r~(t) et de tracer sur un même graphe les fonctions C~m~(ω~mot~) et
C~r~(ω~mot~), reproduite ci-dessous.

![](13-MAS-MS/Cours/pandoc/media/image110.png){width="5.151808836395451in"
height="2.773584864391951in"}

![](13-MAS-MS/Cours/pandoc/media/image110.png){width="5.198113517060367in"
height="3.301887576552931in"}

**12.** À l'aide de l'expression de C~max~, **justifier** l'intérêt de
ce type de commande lorsque la fréquence f varie. **Calculer** pour le
point nominal de fonctionnement donné sur la plaque signalétique de la
MAS le coefficient $K_{f} = \frac{V}{f}$.

**13. Exprimer** le couple C~m~ en fonction de K~f~, p, R, L et D~ω~ =
2πf -pω~mot~.

**14.** En exploitant les courbes du générées par le programme,
**indiquer** la valeur de F~par~ qu'afficherait le programme.

**15. Évaluer** les écarts entre les valeurs du paramètre de fréquence
F~par~ obtenues par la méthode de résolution simplifiée et la méthode de
résolution numérique

**[\
]{.underline}**

![](13-MAS-MS/Cours/pandoc/media/image111.png){width="0.9298108048993876in"
height="0.726415135608049in"}

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"}**DEBOURREUSE DE NOYAUX DE FONDERIE**

*([Source :]{.underline} Centrale Supélec TSI 2009)*

**Mise en situation**

L'entreprise Montupet conçoit, réalise, et produit des culasses pour des
moteurs thermiques destinées à équiper les véhicules des grands
constructeurs automobiles européens. La culasse compose la partie haute
du moteur, elle permettra d'assurer la distribution dans les différents
cylindres du mélange air et combustible servant pour la combustion. Les
culasses sont réalisées par la technique de fonderie en coquille avec
coulée de l'alliage d'aluminium par gravité.

![](13-MAS-MS/Cours/pandoc/media/image112.emf){width="4.631944444444445in"
height="3.310416666666667in"}Des cavités intérieures réalisées dans la
culasse permettent le passage du mélange de combustion et du liquide de
refroidissement. La technique de réalisation par fonderie utilisée ici
impose l'utilisation d'une coquille en acier, possédant l'empreinte des
formes extérieures de la culasse, dans laquelle on positionnera des
noyaux en sable pour la réalisation des cavités intérieures.

Pour réaliser la réduction des mottes de noyaux en sable et leur
évacuation, de très fortes accélérations sont transmises aux culasses
par l'intermédiaire de deux moteurs à balourd (un par culasse provoquant
des vibrations indépendantes) liés au support (voir ci-contre). Il est
nécessaire de transmettre des accélérations minimales de l'ordre de **16
m.s^-2^** à une fréquence comprise entre **20 et 25 Hz**, pour que les
mottes de sable se désagrègent en grains de sable et puissent être mises
en mouvement pour sortir des cavités de la culasse.

La présence de deux moteurs permettra d'obtenir une accélération dans le
plan horizontal (x,y). Celle-ci sera transmise à l'ensemble mis en
mouvement. L'accélération subie par la culasse est issue des effets dus
à l'accélération centrifuge imposés par chacun des 2 moteurs à balourd.

Ces actions dynamiques représentent la résultante dynamique générée par
la présence des balourds tournant liés au rotor des moteurs. On
considère que l'accélération générée est liée directement à la valeur de
l'action dynamique imposée par le moteur.

La masse de l'ensemble (2 moteurs, le support, 2 culasses, 4 marteaux et
des composants annexes) mis en mouvement par les 2 moteurs à balourd est
de **4940 kg**.

Les caractéristiques techniques des moteurs à balourd sont données sur
en annexe. Un seul variateur de vitesse alimente les deux moteurs à
balourds. Ces derniers sont du type moteur asynchrone triphasé tétra
polaire.

Le rendement des machines asynchrones est de 80%.

**1.** Justifier l'utilisation des moteurs à balourds. Justifier
l'utilisation de moteurs asynchrones triphasés pour les moteurs à
balourds.

**2.** Calculer la valeur de l'action dynamique nécessaire que chaque
moteur à balourd doit générer sur la culasse pour répondre au cahier des
charges.

**3.** À partir de la documentation fournie en annexe, déterminer le
moteur à balourd qui répond au mieux aux critères du cahier des charges.
Justifier par un simple bilan de puissance le choix d'un variateur de
puissance de **20 kW**.

La cadence de production impose que 2 culasses soient traitées en 90
secondes. La durée pendant laquelle les moteurs à balourd génèrent des
accélérations est de **60 secondes**.

Par conséquent, les phases d'accélération et de décélération des
machines asynchrones sont primordiales. On ne s'intéressera ici qu'aux
phases de décélération, car elles conditionnent la phase de libération
des culasses du support.

On se propose dans un premier temps de vérifier la nécessité d'un
dispositif de freinage. Dans un second temps, on analysera 2 modes de
freinage, et un choix sur un critère énergétique sera fait. Enfin, dans
l'objectif de justifier le choix d'une résistance de freinage et de
quantifier l'énergie à dissiper lors des phases de freinage, il sera
nécessaire de déterminer les différents paramètres électriques des
moteurs à balourds.

**Nécessité d'un dispositif de freinage**

On se propose dans cette partie de vérifier la nécessité d'un dispositif
de freinage. La phase de freinage débute à l'instant où l'alimentation
des machines asynchrones est coupée.

On suppose que le moment d'inertie ramené sur l'arbre du moteur vaut **J
= 0,33 kg.m^2^**, et que le couple résistant est uniquement dû aux
frottements visqueux de coefficient estimé à **f = 5.10^-2^ N.m.s**. Le
couple de frottement sec sera négligé.

**4.** Appliquer le théorème du moment dynamique à l'arbre du moteur
durant une phase de freinage et en déduire une équation différentielle
liant J, Ω et f.

**5.** Résoudre cette équation différentielle, en prenant pour origine
des temps, l'instant où l'on coupe l'alimentation des machines
asynchrones. La vitesse de rotation initiale est prise égale à **1440
tr.min^-1^**.

**6.** En déduire le temps nécessaire aux moteurs asynchrones pour
s'arrêter. Le couple de frottement sec ayant été négligé, on considèrera
que l'arrêt est obtenu lorsque la vitesse calculée atteint 1% de la
vitesse initiale. Conclure sur la nécessité d'un dispositif de freinage.

**Expression du couple électromagnétique fourni par une MAS et
détermination des paramètres**

Les caractéristiques nominales des machines asynchrones triphasées
sont :

-   Puissance nominale **P~n~ = 7,75 kW**

-   Courant nominal **I~n~ = 13 A**

-   Tension d'alimentation **230/400 V**

-   Fréquence statorique **f~s~ = 50 Hz**

-   Vitesse de rotation nominale **N~n~ = 1440 tr.min^-1^**

-   Couplage étoile

-   Les tensions et les courants sont considérés alternatifs
    > parfaitement sinusoïdaux

![](13-MAS-MS/Cours/pandoc/media/image113.emf){width="2.6222222222222222in"
height="1.4256944444444444in"}On se propose tout d'abord de déterminer
l'expression du couple électromagnétique fourni par une machine
asynchrone en fonction des paramètres électriques et mécaniques de
celle-ci. Le modèle équivalent d'une phase d'une machine asynchrone
triphasée équilibrée est donné ci-contre.

On notera **L** l'inductance magnétisante, **ℓ~fr~** l'inductance de
fuite ramenée au stator, **R~r~** la résistance rotorique ramenée au
stator et **g** le glissement. De plus, **Ω~s~** représente la vitesse
angulaire du champ tournant statorique exprimée en rad.s^-1^, et
**ω~s~** la pulsation des grandeurs électriques statoriques en
rad.s^-1^.

**\
**

**7.** Déterminer le nombre de paires de pôles **p** des machines
asynchrones.

**8.** Déterminer l'expression de la puissance transmise au rotor pour
une machine asynchrone en fonction de ℓ~fr~, R~r~, g, ω~s~ et V~s~.

**9.** En déduire l'expression du couple électromagnétique **C** fourni
par une machine asynchrone en fonction de ℓ~fr~, R~r~, g, p, Ω~s~ et
V~s~.

Afin de caractériser les machines asynchrones triphasées, il est
nécessaire d'identifier les différents paramètres du modèle monophasé.
Pour cela, deux essais ont été réalisés :

-   1^er^ essai : Essai à la vitesse angulaire de synchronisme Ω~s~ sous
    > une tension entre Phase et Neutre de **230 V** à la fréquence de
    > **50 Hz**. La puissance réactive absorbée par une machine
    > asynchrone triphasée vaut **800 VAR**.

-   2^nd^ essai : Essai à rotor calé (= 0) sous tension réduite. Une
    > machine asynchrone triphasée est alimentée par une source de
    > tension triphasée délivrant une tension simple de valeur efficace
    > prise égale à **V~cc~ = 76 V**, la valeur efficace du courant
    > absorbé par phase est **I~cc~** et vaut **13 A**. Dans ces
    > conditions, une machine asynchrone triphasée absorbe une puissance
    > active **P~cc~ = 350 W**.

**10.** Avec l'essai 1 :

-   Quelle est la valeur du glissement pour cet essai ?

-   Après avoir exprimé la puissance réactive absorbée par la machine
    > asynchrone pour l'essai 1, déterminer la valeur de l'inductance
    > magnétisante **L**.

**11.** Avec l'essai 2 :

-   Justifier que l'essai à rotor bloqué soit réalisé sous tension
    > réduite.

-   Quelle est la valeur du glissement pour cet essai ?

-   Déterminer la valeur efficace du courant **I~r~**.

-   Déterminer les valeurs de la résistance **R~r~** et de l'inductance
    > de fuite **ℓ~fr~**.

Pour la suite du sujet, on prendra **R~r~ = 730 mΩ** ; **L = 630 mH** et
**ℓ~fr~ = 20 mH**.

**12.** Déterminer l'expression numérique du couple électromagnétique
**C** en fonction du glissement g pour **f~s~ =50Hz**. En déduire la
valeur du couple maximum et la valeur du glissement pour laquelle on
l'atteint.

**13.** Tracer l'allure de la courbe du couple électromagnétique **C**
en fonction du glissement g pour g∈\[-1;1\].

**14.** Préciser les modes de fonctionnement (moteur ou frein) de la
machine asynchrone triphasée en fonction de la valeur du glissement g.

**ANNEXE : Documentation technique des moteurs à balourd**

![](13-MAS-MS/Cours/pandoc/media/image114.png){width="6.755905511811024in"
height="6.826771653543307in"}

![](13-MAS-MS/Cours/pandoc/media/image115.png){width="6.755905511811024in"
height="2.3858267716535435in"}

**[\
]{.underline}**

![](13-MAS-MS/Cours/pandoc/media/image116.png){width="0.6582305336832895in"
height="0.867924321959755in"}**TRAMWAY DE STRASBOURG**

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source :]{.underline} Concours 3ème
année ENS Cachan 2002)*

**Mise en situation**

![](13-MAS-MS/Cours/pandoc/media/image117.jpeg){width="2.363888888888889in"
height="1.5958333333333334in"}Une rame de tramway de Strasbourg se
compose de quatre bogies dont trois sont moteurs. Un bogie moteur est
composé de quatre roues entraînées chacune par un moteur asynchrone
triphasé par l'intermédiaire d'un réducteur. Une rame de tramway est
donc motorisée par douze moteurs asynchrones.

**[Principe de traction]{.underline}**

Le schéma de traction retenu pour le Tramway de Strasbourg est donné
ci-dessous. Chaque onduleur de traction alimente deux des quatre
machines asynchrones placées sur chaque bogie. Cette commande
indépendante des roues situées à droite et à gauche du bogie permet
d\'améliorer les passages en courbe.

Le conducteur, par l'intermédiaire d'une manette, peut moduler l'effort
de traction à appliquer à la rame de tramway. Ceci revient à moduler le
couple électromagnétique des moteurs. Le constructeur a choisi
d'implanter une commande permettant d'imposer le couple
électromagnétique instantané sur l'arbre des moteurs.

![](13-MAS-MS/Cours/pandoc/media/image118.png){width="6.458295056867891in"
height="3.83781605424322in"}

**[Caractéristiques nominales du moteur]{.underline}**

Il s\'agit d\'un moteur asynchrone triphasé à rotor à cage dont les
enroulements statoriques sont couplés en étoile.

-   Tension nominale entre phases : U~N~ = 585 V

-   Fréquence statorique nominale : f~N~ = 88 Hz

-   Intensité nominale du courant statorique : l~N~ = 35,4 A

-   Facteur de puissance nominal : cos ϕ~N~ = 0,732

-   Fréquence nominale de synchronisme : N~s~ = 2640 tr.min^-1^

-   Fréquence nominale de rotation du rotor : N~N~ = 2610 tr.min^-1^

Dans ce qui suit, on néglige : Les résistances et inductances de fuites
statoriques

Les pertes dans le fer

Les pertes mécaniques

**Etude du fonctionnement nominal du moteur**

**1.** Déterminer le nombre p de paires de pôles du moteur.

**2.** Calculer le glissement g~N~.

**3.** Calculer la puissance électrique P~N~ absorbée par le moteur et
préciser la valeur de la puissance électromagnétique P~TrN~ transmise au
rotor.

**4.** Calculer le couple électromagnétique C~N~.

**5.** Exprimer les pertes par effet Joule au rotor P~Jr~ en fonction de
P~Tr~. Calculer P~JrN~.

**6.** Calculer la puissance utile P~UN~ développée par le moteur.

**Fonctionnement dans les quatre quadrants**

![](13-MAS-MS/Cours/pandoc/media/image119.png){width="2.582638888888889in"
height="1.511111111111111in"}L\'association du convertisseur et de la
motorisation doit permettre le fonctionnement de la machine asynchrone
dans les 4 quadrants mécaniques c\'est-à-dire pour le Tramway de
Strasbourg, la circulation dans les deux sens de marche et le freinage
électrique. Les tensions alimentant la machine asynchrone sont
sinusoïdales triphasées (v~AN~, v~BN~ et v~CN~) et que le modèle
équivalent par phase de la machine peut être assimilé au schéma
simplifié ci-dessous.

-   R/g est la résistance modélisant le transfert de puissance active au
    > rotor

-   L~M~ est l'inductance magnétisante

-   L~t~ est l'inductance totale de fuites vue du stator

-   g est le glissement

-   v est une tension simple du réseau d'alimentation de valeur efficace
    > V (v = v~xN~ avec x = A, B ou C)

-   i est l'intensité en ligne.

On donne : R = 0,138 Ω L~t~ = 2,38 mH L~M~ = 26,55 mH.

![](13-MAS-MS/Cours/pandoc/media/image120.wmf)**7.** Déterminer
l\'expression du couple électromagnétique C en fonction de V, L~t~, R,
g, p et ω (pulsation des grandeurs statoriques). Mettre le résultat sous
la forme ci-contre en précisant les expressions de A et de g~0~.

On prendra pour les applications numériques suivantes : V = 338 V et f =
88 Hz.

**8.** Pour quelle valeur de g, le couple est-il maximal ? Déterminer
alors le couple maximal C~MAX~. Effectuer les applications numériques.

**9.** Tracer la caractéristique C(N) d'un moteur de traction pour 0 \<
N \< 2N~s~ avec N en tr/min. Préciser les points remarquables, la partie
stable de la caractéristique ainsi que les plages de fonctionnement en
moteur et en génératrice.

**10.** En précisant l'hypothèse faite, montrer que la caractéristique
de couple peut se mettre sous la forme C ≈ K.g avec K = 8972 Nm.
Représenter cette caractéristique approchée sur le graphe précédent.

**11.** En utilisant le résultat de la question précédente, calculer le
glissement puis la vitesse de rotation du moteur N (en tr/min) pour C =
90 Nm puis pour C = -90 Nm.

**12.** On souhaite inverser le sens de rotation des moteurs de traction
pour effectuer une marche arrière. Comment procède-t-on ?

**13.** Représenter, sur le document réponse, les tensions v~BN~ et
v~CN~ nécessaires pour aller dans les différents quadrants de
fonctionnement du moteur. Les conventions sont données pour le
quadrant 1. Préciser pour chaque quadrant le type de fonctionnement de
la machine.

**14.** Montrer que l\'expression du déphasageϕ de v par rapport à i est
donnée par :

> ![](13-MAS-MS/Cours/pandoc/media/image121.wmf)

**15.** En déduire les valeurs de ϕ pour C = 90 Nm puis pour C = -90 Nm.
Commenter les résultats obtenus.

**16.** Compléter le document réponse en représentant les courants i~A~,
i~B~, i~C~ dans chacun des 4 quadrants mécaniques permettant d'obtenir
un couple en valeur absolue de 90 Nm.

**DOCUMENT RÉPONSE**

![](13-MAS-MS/Cours/pandoc/media/image123.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image124.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image125.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image123.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image124.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image125.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image123.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image124.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image125.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image123.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image126.png){width="7.45625in"
height="9.42361111111111in"}![](13-MAS-MS/Cours/pandoc/media/image127.png){width="7.45625in"
height="9.42361111111111in"}

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"}

**TABLE DE RADIOLOGIE D²RS**

*([Source]{.underline} : ATS 2018)*

**Mise en situation**

[Présentation du système]{.underline}

La table de radiologie D²RS (Digital Dynamic Remote System) conçue et
commercialisée par STEPHANIX répond aux fonctions suivantes :

-   supporter et positionner le patient ainsi que le système d'imagerie

-   intégrer de nouveaux critères d'innovation :

```{=html}
<!-- -->
```
-   dernière génération de capteur plan dynamique

-   positionnement automatique en fonction du protocole sélectionné

```{=html}
<!-- -->
```
-   réaliser des tomosynthèses\* (pseudo 3D, protocole de détection
    > précoce de certains cancers) grâce à l'interpolation de 2 axes en
    > mouvement.

![](13-MAS-MS/Cours/pandoc/media/image128.emf){width="4.319608486439195in"
height="3.5283016185476814in"}

\*La tomosynthèse est une technique d'imagerie radiologique ancienne et
tombée en désuétude qui redevient d'actualité grâce au développement des
technologies numériques de traitement d'images radiologiques. À partir
d'une table radiologique classique, elle permet dorénavant une
acquisition volumique (dite pseudo-3D) de la zone observée.

[Problématique]{.underline}

Lorsque le manipulateur radio agit sur le mouvement de chariotage pour
positionner précisément la source de rayons X et cibler la zone à
radiographier pour une tomosynthèse, des instabilités apparaissent à
basse vitesse et perturbent son réglage.

**Détermination des grandeurs nominales de la machine**

[Hypothèses :]{.underline}

La table de radiographie D²RS est alimentée par le réseau triphasé 400 V
/ 50 Hz. Toutes les pertes de la machine asynchrone sont négligées à
l'exception des pertes joules au rotor et des pertes mécaniques.

**1. Prendre** connaissance de la plaque signalétique en annexe.
**Déterminer** alors pour cette machine :

-   le couplage des enroulements

-   le nombre de paires de pôles p

-   le glissement nominal g~n~

-   la puissance active absorbée nominale P~ab~

-   les pertes joules rotoriques P~jr~

-   les pertes mécaniques P~pm~

-   le rendement nominal η~n~

[Modèle équivalent par phase de la machine asynchrone :]{.underline}

Réactance de magnétisation X~m~ = L~m~.ω

Réactance de fuite d'une phase rotor ramenée au stator X~2~ = L~2~.ω

Résistance d'une phase rotor ramenée au stator R~2~

Glissement g

Pulsation des courants statoriques ω

Deux essais ont été effectués pour déterminer les valeurs numériques des
paramètres :

+-------------------------------+--------------------------------------+
| Essai à vide                  |                                      |
+===============================+======================================+
| Conditions de l'essai         | Mesures                              |
+-------------------------------+--------------------------------------+
| Machine désaccouplée          | Puissance réactive absorbée Q~0~ =   |
|                               | 1322 VAR                             |
| Tension d'alimentation V~10~  |                                      |
| = 230 V                       |                                      |
|                               |                                      |
| Fréquence f = 50 Hz           |                                      |
+-------------------------------+--------------------------------------+

+-------------------------------+--------------------------------------+
| Essai à rotor bloqué          |                                      |
+===============================+======================================+
| Conditions de l'essai         | Mesures                              |
+-------------------------------+--------------------------------------+
| Machine avec rotor bloqué     | Puissance apparente absorbée S~rb~ = |
|                               | 245 VA                               |
| Tension d'alimentation V~1rb~ |                                      |
| = 15 V                        | Intensité du courant I~2rb~ = 2,49 A |
|                               |                                      |
| Fréquence f = 50 Hz           | Facteur de puissance f~p~ = 0,69     |
+-------------------------------+--------------------------------------+

**2. Faire** une hypothèse sur la valeur du glissement dans l'essai à
vide et **représenter** le schéma simplifié du modèle équivalent par
phase. **Exprimer** la puissance réactive Q~0~ en fonction des éléments
du schéma et **en déduire** la valeur numérique de l'inductance de
magnétisation L~m~.

**3. Faire** une hypothèse sur la valeur du glissement dans l'essai à
rotor bloqué et **représenter** le schéma simplifié du modèle équivalent
par phase**. Exprimer** les puissances active P~rb~ et réactive Q~rb~ en
fonction des éléments du schéma. **En déduire** les valeurs numériques
de la résistance rotorique R~2~ et de l'inductance de fuite rotorique
L~2~.

Les valeurs numériques retenues pour la suite du problème sont :

> Inductance de magnétisation L~m~ = 0,382 H
>
> Inductance de fuite d'une phase rotor ramenée au stator L~2~ = 29,4 mH
>
> Résistance d'une phase rotor ramenée au stator R~2~ = 9,08 Ω

**4. Indiquer** le paramètre de l'alimentation sur lequel on peut agir
pour faire varier la vitesse de la machine.

**5. Montrer** que le couple électromagnétique de la machine peut se
mettre sous la forme $C_{em} = K.\frac{x}{(x^{2} + X_{2}^{2})}\ $ et
**exprimer** les paramètres K et x. **Valider** le modèle par le calcul
du couple nominal de la machine. Puis **montrer** que C~em~ est maximum
pour $g = g_{\max} = \frac{R_{2}}{X_{2}}$. **En déduire** l'expression
de C~max~ en fonction de L~2~, V~1~, p et f.

**6. Justifier** qualitativement le choix d'une commande scalaire en
$\frac{V_{1}}{f}$ pour une machine asynchrone associée à un onduleur de
tension (ou de courant).

**Etude de la commande scalaire**

Le couple dans une machine asynchrone est directement proportionnel au
carré du flux créé par l'inductance magnétisante L~m~. Les performances
optimales sont obtenues si le flux, donc le courant magnétisant
[I]{.underline}~m~, est maintenu constant sur toute la plage de vitesse.

**7. Exprimer** la valeur efficace du courant magnétisant I~m~ en
fonction de V~1~, L~m~ et f, puis **justifier** le choix d'une commande
scalaire.

Un modèle plus complet de la machine asynchrone est proposé ci-dessous.

Réactance de magnétisation X~m~ = L~m~.ω

Réactance de fuite d'une phase rotor ramenée au stator X~2~ = L~2~.ω

Résistance d'une phase rotor ramenée au stator R~2~

Réactance de fuite d'une phase stator X~1~ = L~1~.ω

Résistance d'une phase stator R~1~

Les paramètres de l'enroulement stator ont fait l'objet d'une mesure. On
a relevé R~1~ = 0,85 Ωet L~1~ = 3,24 mH.

**8. Calculer** la chute de tension statorique au point nominal.

Par simulation du modèle complet par phase, deux courbes ont été
obtenues : le courant magnétisant I~m~(A) à la figure de gauche et la
chute de tension ∆u (% de V~1~) à la figure de droite, en fonction de la
fréquence d'alimentation f (Hz).

![](13-MAS-MS/Cours/pandoc/media/image130.png){width="3.584905949256343in"
height="1.903713910761155in"}![](13-MAS-MS/Cours/pandoc/media/image131.png){width="3.645307305336833in"
height="1.9192530621172355in"}

**9. Commenter** les courbes obtenues par simulation et **conclure** sur
les limites de la commande scalaire. **Proposer** une autre stratégie de
commande qui réponde à la problématique.

[Plaque signalétique du moteur :]{.underline}

  --------------------------------------------------------------------------------------------------------------------------------------------------
  ![](13-MAS-MS/Cours/pandoc/media/image132.emf){width="0.7716535433070866in"                                                               
  height="0.49606299212598426in"}                                                                                                           
  ![](13-MAS-MS/Cours/pandoc/media/image133.emf){width="2.132075678040245in"                                                                
  height="0.49730424321959754in"}                                                                                                           
  ![](13-MAS-MS/Cours/pandoc/media/image134.emf){width="0.7716535433070866in"                                                               
  height="0.49606299212598426in"}                                                                                                           
  ----------------------------------------------------------------------------- --------------------- ------- ------------ ------- -------- --------
  3∼ Mot                                                                        M 2SB 4 FD            Cod     8G360209CV                    

  No                                                                            F-01-13 / 6771243     S 1     IMB          5       14.5     kg

                                                                                                                                            

  kW                                                                            1.1 / 50 Hz                                                 

                                                                                                                                            

  Hz                                                                            V (+/- 10%)           A                    min-1   cosɸ     

  50                                                                            230 / 400 D/Y         4.7 /                1400    0.78     
                                                                                                      2.7                                   

                                                                                                                                            
  --------------------------------------------------------------------------------------------------------------------------------------------------

[Extrait du catalogue moteur Bonfiglioli :]{.underline}

![](13-MAS-MS/Cours/pandoc/media/image135.emf){width="7.26415135608049in"
height="3.8741655730533684in"}

Avec : M~a~ couple d'accélération moyen (Nm)

M~n~ couple nominal (Nm)

M~s~ couple de démarrage (Nm)

![](13-MAS-MS/Cours/pandoc/media/image136.jpeg){width="0.46539916885389326in"
height="0.625in"}**EOLIENNE**

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source]{.underline} : CAPET SII 2010)*

**Mise en situation**

Cette installation est implantée dans un camping situé en bordure de
l'étang de Thau sur la commune de Mèze (Hérault, 34).

Le propriétaire qui souhaite afficher une démarche respectueuse de
l'environnement et réduire sa facture énergétique a exprimé les
contraintes suivantes :

-   Un minimum de nuisances sonores pour les campeurs et le propriétaire

-   Une installation capable de couvrir au minimum la totalité de la
    > facture énergétique pour le logement privé, soit une puissance
    > minimale de 5 kW lors du fonctionnement à la fréquence de rotation
    > nominale.

Les conditions météorologiques retenues sont :

-   Vent local moyen de 10 m/s du secteur EST avec des maximas pouvant
    > atteindre 27 m/s

-   Altitude : niveau de la mer.

Le propriétaire du camping a contacté la société TRAVERE Industries pour
réaliser son projet d'implantation d\'éolienne.

**Schéma de l'installation proposée par la société TRAVERE Industries
SAS**

Un ensemble redresseur / convertisseur met en forme l'énergie électrique
délivrée par l'éolienne pour la renvoyer au réseau électrique BT (Basse
Tension). Un compteur d'énergie à courbe de charge calcule l'énergie
consommée et l'énergie renvoyée vers le réseau EDF. L'installation
électrique du propriétaire est reliée au réseau électrique BT en
monophasé.

**Vérification de la puissance générée**

Le schéma équivalent monophasé pour une phase de la génératrice est
représenté ci-dessous.

Pour une vitesse nominale de 240 tr/min la génératrice débite un courant
I de 8,38 A avec un déphasage ϕ entre I et V~1~ de 18°. La f.é.m.
[E]{.underline} est alors une tension sinusoïdale de fréquence f = 48
Hz, et de valeur efficace E = 311 V.

**1. Donner** l'expression de [V]{.underline}~1~ en fonction de
[I]{.underline}, [E]{.underline}, r~1~, ω, et L~1~.

**2. Déterminer** graphiquement, sur le graphique ci-après, la valeur
efficace de la tension [V]{.underline}~1~.

**3. Calculer** la puissance active P~gén~ fournie par la génératrice
pour le fonctionnement nominal. **En déduire** s'il est possible de
couvrir les besoins énergétiques du site de Mèze avec l'installation
proposée.

**4. Conclure**, en indiquant le rendement de la génératrice pour le
fonctionnement nominal de l'éolienne TA6-5500 sachant que la puissance
mécanique récupérée est de 6,1 kW.

  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  

                                                                                                  
  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![](13-MAS-MS/Cours/pandoc/media/image137.png){width="0.9433967629046369in"
height="0.6104341644794401in"}**MLPS : Système automatisé de
conditionnement de cartons**

*([Source]{.underline} : ATS 2016)*

![](13-MAS-MS/Cours/pandoc/media/image138.png){width="2.6506944444444445in"
height="2.620138888888889in"}**Mise en situation**

Le système MPLS (pour Multi Level Packaging System) permet d\'agencer
les cartons sur la palette. Ses principaux éléments constitutifs sont :

-   Une **unité en U,** composée d\'un axe numérique et d'un préhenseur
    > à ventouses, permet la saisie, l\'élévation, la translation, la
    > descente et la dépose d\'un carton à une position précise sur la
    > palette.

-   Une **table élévatrice** permet de descendre la palette de la
    > hauteur d\'un carton quand une couche est terminée.

-   Un **plateau indexeur** permet de faire tourner la palette par pas
    > de 90° dans le sens horaire et en fonction des besoins du cycle.

La production du couple mécanique nécessaire à l\'entraînement du
préhenseur est assurée par un ensemble moteur synchrone et onduleur de
tension à commande MLI.

![](13-MAS-MS/Cours/pandoc/media/image139.png){width="5.301388888888889in"
height="4.0in"}La machine synchrone est alimentée depuis le réseau EDF
230V/50Hz par la chaîne d\'énergie dont le schéma de principe est
représenté ci-dessous :

Le rôle de l\'ensemble redresseur à diodes D1 à D4 et filtre Lf / Cf est
de convertir le réseau sinusoïdal d\'EDF en une source de tension U~0~
que l\'on supposera continue.

Le rôle de l\'ensemble convertisseur à trois cellules de commutation
(K1/K4 ; K3/K6 ; K5/K2) est de convertir la source de tension continue
U~0~ en une source de tension triphasée à fréquence réglable et à
amplitude du fondamental également réglable.

Les caractéristiques de fréquence et d\'amplitude du fondamental sont
obtenues par le choix d\'un chronogramme approprié des trois fonctions
de modulation fm1, fm2, fm3 dont les valeurs 0 et/ou 1 sont
\"calculées\" par le régulateur de vitesse.

*Chaîne d'énergie*

**[Hothèses :]{.underline}**

> • Le couple électromagnétique C~em~(t) est confondu avec le couple
> mécanique C~m~(t)
>
> • La puissance électromagnétique P~em~(t) est confondue avec la
> puissance mécanique P~m~(t)
>
> Une étude énergétique a permis de tracer le graphe de la puissance
> mécanique P~m~(t) fournie par la machine synchrone.
>
> **1.**Entre les instants t~0~ et τ~2~, puis entre les instants τ~2~ et
> t~i~, **préciser** le mode de fonctionnement redresseur / onduleur du
> convertisseur statique raccordé à la machine synchrone ainsi que le
> mode de fonctionnement moteur / génératrice de cette machine.
> **Justifier** votre réponse.
>
> **2. Justifier** la présence du module de freinage (voir chaîne
> d'énergie) constitué de la résistance Rf et de l\'interrupteur Kf.
> Quel est l\'état ouvert / fermé de l\'interrupteur statique Kf entre
> les instants t~0~ et t~i~ ?

**[Objectif :]{.underline}**Vérifier que l\'alimentation de la machine
par l\'onduleur permet d\'atteindre la vitesse de translation du
préhenseur **V = 0,86 m.s^-1^**

**[Hypothèse et notations :]{.underline}** Le stator de la machine est
supposé sans pertes magnétiques

  -----------------------------------------------------------------------
  Poulie motrice                       Diamètre D = 100 mm
  ------------------------------------ ----------------------------------
  Rapport de réduction du réducteur    r = 1/11,83

  Couplage du stator                   Etoile

  Fem à vide entre phases (valeur      56V à 1000tr.mn^-1^
  efficace)                            

  *Données constructeurs*              
  -----------------------------------------------------------------------

-   ω~s~ la pulsation des grandeurs électriques (rad.s^-1^)

-   6, le nombre de pôles

-   Ω~s~ la vitesse angulaire du champ tournant statorique

-   R~s~= 3,91 Ω, la résistance par phase

-   L~c~= 8,8 mH, l\'inductance cyclique par phase

-   [V]{.underline}~s~, [I]{.underline}~s~, [E]{.underline} l\'amplitude
    > complexe de la tension, du courant, de la fcem par phase

-   k~e~ le coefficient, positif, de fcem avec E = k~e~.Ω~m~

-   $\varphi = ({\overrightarrow{I}}_{s},\ {\overrightarrow{V}}_{s})$ le
    > déphasage du courant ${\overrightarrow{I}}_{s}$ sur la tension
    > ${\overrightarrow{V}}_{s}$

-   $\psi = ({\overrightarrow{I}}_{s},\ \overrightarrow{E})$ le
    > déphasage du courant ${\overrightarrow{I}}_{s}$ sur la tension
    > $\overrightarrow{E}$

Le mouvement de translation du préhenseur est obtenu à partir d\'un
motoréducteur et d\'un système poulie-courroie.

**3. Déterminer** la vitesse de rotation de la poulie Ω~p~, puis celle
du moteur Ω~m~.

**Pour les questions Q4 à Q7, nous ferons l\'hypothèse que R~s~ = 0**,
conformément au schéma équivalent monophasé.

**4. Exprimer** la puissance électromagnétique P~em~ transmise par le
stator triphasé au rotor en fonction de E, I~s~, ψ.

**5.** La fonction d\'autopilotage de la pulsation de l\'alimentation du
stator à la position du rotor garantit l\'égalitéΩ~s~ = Ω~m~.
**Montrer** que l\'expression du couple électromagnétique C~em~ peut
s\'écrire C~em~ = k~c~.I~s~.cosψ. **Exprimer** le coefficient de couple
k~c~ en fonction de k~e~.

**6.** Pourquoi les valeurs particulières ψ = 0 et ψ = π sont-elles
optimales pour le dimensionnement de la machine ?

**7.** Pour ψ = 0, **calculer** pour le régime permanent (vitesse V) :

-   La valeur efficace de la fcem E par phase

-   La valeur efficace du courant I~s~ par phase

-   La fréquence f~S~ des grandeurs électriques

-   La valeur efficace de la tension V~s~ par phase.

**8. Reprendre** le calcul de la tension V~s~ dans les mêmes conditions
de fonctionnement mais **en considérant la résistance par phase R~s~ du
stator**. **Conclure** quant à la validité de l\'hypothèse R~s~= 0 lors
du régime permanent.

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"}![](13-MAS-MS/Cours/pandoc/media/image140.emf){width="0.8295811461067366in"
height="0.59375in"}**SYSTEME SEAREV : Récupération de l'énergie de la
houle marine**

*[Source]{.underline} : Centrale Supélec TSI 2011*

**Mise en situation**

![](13-MAS-MS/Cours/pandoc/media/image141.emf){width="3.0729166666666665in"
height="1.6909722222222223in"}Les ressources en énergie fossile baissent
inexorablement, et les scientifiques sont à la recherche de solutions de
remplacement durables. La consommation annuelle d'énergie mondiale est
de 140.10^12^kWh ce qui représente environ 1/8000^ème^ de l'énergie
solaire arrivant sur terre. La production mondiale d'électricité
représente quant à elle 17.10^12^kWh.

L'énergie solaire est à l'origine de la formation de la houle qui
représente une énergie nette disponible évaluée entre 140 et 700 TWh/an
d'après le WEC (World Energycouncil), soit 1 à 5% de la demande mondiale
en électricité. La puissance moyenne par mètre de front de vague se
situe entre 10 et 100kW/m. Même si cette ressource reste limitée face à
la demande globale en énergie, elle n'en reste pas moins exploitable,
particulièrement en France où la façade maritime est l'une des plus
importante d'Europe. C'est pourquoi les laboratoires de recherche de
l'École Centrale de Nantes, et de l'École Normale Supérieure de Rennes
travaillent actuellement au développement d'un prototype de
houlogénératrice (projet SEAREV).

  -----------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](13-MAS-MS/Cours/pandoc/media/image142.emf){width="1.3065332458442696in"   ![](13-MAS-MS/Cours/pandoc/media/image140.emf){width="2.4175470253718285in"
  height="1.728543307086614in"}                                                 height="1.7305161854768154in"}
  ----------------------------------------------------------------------------- -----------------------------------------------------------------------------
  *Figure 2: Prototype SEAREV Centrale Nantes*                                  *Figure 3: Image de synthèse système SEAREV*

  -----------------------------------------------------------------------------------------------------------------------------------------------------------

Il s'agit d'un flotteur ancré au large dans lequel est placé un pendule
constituant le rotor d'une génératrice synchrone. L'énergie produite est
adaptée afin d'être acheminée à la côte et injectée sur le réseau de
transport ***EDF***.

**Description**

La surface de l'eau est modélisée par une sinusoïde fonction de l'espace
et du temps. On fait l'hypothèse forte que l'orientation du flotteur
suit la tangente à la surface de l'eau, ce qui induit un mouvement de
tangage.

*Figure 4 : Modélisation de la houle*

Le houlogénérateur est constitué d'un flotteur **[1]{.underline}** et
d'un pendule **[2]{.underline}** évoluant par rapport à la Terre
**[0]{.underline}**. Les deux solides **[1]{.underline}** et
**[2]{.underline}** sont en liaison pivot d'axe. La génératrice
synchrone placée sur l'axe de liaison permet de récupérer une partie de
l'énergie des vagues.

***Paramétrage ***

La figure 4 représente le schéma équivalent monophasé de la génératrice
synchrone débitant sur le convertisseur alternatif-continu modélisé
comme une source de tension idéale.

On suppose que les courants et les tensions sont parfaitement
sinusoïdaux de pulsation **ω**. On appelle **[V]{.underline}~S~** la
représentation complexe de **v~S~(t)**, force électromotrice de la
génératrice synchrone, **[V]{.underline}~R~** la représentation complexe
de **v~R~(t)**, tension simple d'entrée du convertisseur
alternatif-continu et **[I]{.underline}**la représentation complexe de
**i(t)**, le courant statorique. La tension v~S~(t) est prise comme
référence. On appelle **δ** l'avance de phase de v~R~(t) par rapport à
v~S~(t) et **ψ** l'avance de phase de i(t) par rapport à v~S~(t). Enfin
**X** = ℓ~S~.ω est la réactance de la génératrice. On donne ℓ~S~= 35 mH.
La génératrice est constituée de **p~M~** paires de pôles, avec p~M~=
120.

**Contrôle du transfert d'énergie**

**[Objectifs :]{.underline}**

-   Montrer que la structure de conversion permet d'ajuster le réglage
    > de la puissance électrique produite par la génératrice à sa valeur
    > optimale

-   Déterminer les valeurs des paramètres de commande pour une puissance
    > moyenne maximale de 400 kW correspondant à la houle optimale.

**1. Écrire** la relation liant [V]{.underline}~S~, [V]{.underline}~R~
et [I]{.underline} en fonction des éléments du circuit. **Tracer**
l'allure de cette relation dans le plan complexe. **Faire apparaître**
sur la figure les angles ψ et δ.

**2. Exprimer** la puissance active (électromagnétique) P~S~ fournie par
la génératrice synchrone. **En déduire** l'expression de P~S~ en
fonction de V~S~, V~R~, X et δ. V~S~ et V~R~ sont respectivement la
valeur efficace de v~S~(t) et de v~R~(t). (on pourra faire une
projection sur l'axe vertical)

**3. Exprimer** la puissance réactive Q~S~ fournie par la génératrice
synchrone. **En déduire** l'expression de Q~S~ en fonction de V~S~,
V~R~, X et δ. (projection sur l'axe $\overrightarrow{V_{S}}$)

**4.** En fonctionnement normal, l'angle δ reste petit. **Donner** dans
ces conditions l'expression approchée de P~S~ et de Q~S~.

**5.** En vous appuyant sur les résultats des questions précédentes,
**indiquer** sur quels paramètres du système on peut agir pour régler le
transfert d'énergie de la source vers la charge.

Le générateur étant pourvu d'aimant permanent, il n'est pas nécessaire
de produire un courant magnétisant statorique. On peut donc imposer Q~S~
= 0. On prendra les expressions suivantes :

$$P_{S} = 3.V_{S}.\frac{V_{R}.\delta}{X}\ et\ Q_{S} = 3.V_{S}.\frac{V_{S} - V_{R}}{X}$$

**6. En déduire** l'expression de V~R~, puis de δ en fonction de P~S~ et
des éléments du circuit.

**7.** Le couple résistant appliqué par la génératrice au pendule
s'écrit C~r~ = -λ.$\dot{\theta}$. **Exprimer** la puissance moyenne P~S~
en fonction de $\dot{\theta}$ et λ.

**8.** La constante de force électromotrice K~u~ de la génératrice est
définie par V~S~= K~u~.$\dot{\theta}$, et X = ℓ~s~.p~M~.$\dot{\theta}$.
**En déduire** l'expression de δen fonction de K~u~, ℓ~S~,
$\dot{\theta}$, p~M~ et λ.

On donne $\dot{\theta}$~max~ = 0,25 rad s^−1^ et λ = 0,63.10^7^ N·m·s.
Par ailleurs, lorsque $\dot{\theta}$= $\dot{\theta}$~max~, V~S~= 400 V.

Application numérique : en déduire la plage de variation de δ.

**9.** L'arbre du générateur est équipé d'un capteur de position
angulaire et de vitesse angulaire. On dispose également d'un capteur de
courant dans chaque phase du stator. **Conclure** sur la possibilité de
contrôler la puissance active convertie par la génératrice.

**10.** Compléter le bilan de puissance de la génératrice synchrone.

![](13-MAS-MS/Cours/pandoc/media/image143.png){width="0.965411198600175in"
height="0.5792454068241469in"}

**BOURREUSE -- NIVELEUSE -- DRESSEUSE**

![](13-MAS-MS/Cours/pandoc/media/image77.png){width="1.3555555555555556in"
height="0.3888888888888889in"} *([Source :]{.underline} ATS 2020)*

**Mise en situation**

La motorisation de la bourreuse doit permettre son fonctionnement en
mode circulation et en mode travail. Ces deux modes de fonctionnement
sont cependant radicalement différents :

> --- en mode circulation, le moteur travaille principalement en régime
> stabilisé et sous forte puissance ;
>
> --- en mode travail, la puissance demandée au moteur est plus faible
> et le régime de fonctionnement du moteur change sans cesse.

Pour qu'elle puisse tracter un convoi de 100 tonnes à la vitesse de 100
km/h (cas d'utilisation le plus énergivore), la bourreuse est pourvue
d'un moteur à combustion interne dont la puissance nominale est de 486
kW. En mode travail, la puissance requise pour le fonctionnement de
l'engin est significativement plus faible. Il en résulte qu'en mode
travail, la motorisation de la bourreuse n'est pas exploitée de manière
optimale.

[Solution envisagée.]{.smallcaps} Afin de réduire la consommation
énergétique de la bourreuse en mode travail, il est envisagé d'en
électrifier le fonctionnement. Chacun des trois essieux de la bourreuse
sera donc pourvu d'une machine électrique. Cette évolution permettra
également de réduire les émissions sonores et le niveau de vibration de
la bourreuse en mode travail, améliorant ainsi le confort et la sécurité
des personnels opérant sur ou à proximité de l'engin.

**Dimensionnement des modulateurs**

Afin de minimiser les modifications de la bourreuse introduites par
l'électrification de sa traction, les machines électriques sont
installées à la place des moteurs hydrauliques utilisés actuellement
pour la traction en mode travail (figure 1). Les réducteurs situés en
aval de ces moteurs sont également remplacés afin d'adapter la chaîne
d'énergie à sa nouvelle motorisation.

![](13-MAS-MS/Cours/pandoc/media/image144.png){width="7.33458552055993in"
height="2.2075503062117234in"}

Figure 1 -- Vue d'un essieu, de sa boîte de vitesse et de la
motorisation hydraulique

[Caractéristiques des machines]{.smallcaps}. Les machines utilisées pour
la traction de la bourreuse en mode travail sont des machines synchrones
triphasées à aimants permanents. Chacune de ces trois machines est
alimentée par un onduleur de courant. Les données constructeur relatives
à ces machines sont données dans le tableau page suivante.

  -----------------------------------------------------------------------
  Grandeur                                       Symbole    Valeur
  ---------------------------------------------- ---------- -------------
  Nombre de phases                                          3

  Couplage                                                  étoile

  Nombres de paires de pôles                     p          4

  Fréquence électrique nominale                  f~n~       120 Hz

  Puissance nominale                             P~n~       23 kW

  Vitesse nominale                               N~n~       1800 tr/min

  Tension de couplage nominale                   U~n~       400 V

  Intensité nominale                             I~n~       42,90 A

  Couple nominal                                 C~n~       122 N·m

  Rendement au point de fonctionnement nominal   η~n~       0,94

  Intensité maximale                             I~Max~     62,21 A

  Couple maximal                                 C~Max~     164,7 N·m
  -----------------------------------------------------------------------

**[Modélisation et détermination des paramètres des
machines]{.underline}**

Les trois machines étant identiques et sollicitées de la même manière,
l'étude se focalise sur une seule machine.

[Modèle électrique]{.smallcaps}. On utilise le modèle de Behn-Eschenburg
pour estimer les grandeurs électriques nécessaires au fonctionnement de
la machine. Ce modèle et les notations associées sont rappelés figure 2.
Le système de tension triphasé est supposé équilibré et une seule phase
de la machine est considérée. La résistance d'induit R et l'inductance L
sont supposés constants quel que soit le point de fonctionnement de la
machine.

[Dissipations de puissance]{.smallcaps}. Les seules dissipations de
puissance considérées dans la machine sont les pertes cuivre modélisées
par la résistance d'induit R. Les pertes magnétiques et mécaniques sont
négligées.

  -------------------------------------------------------------------------------
                    Définition
  ----------------- -------------------------------------------------------------
  ω                 Pulsation électrique en rad/s

  [V]{.underline}   Tension d'alimentation d'une phase

  [I]{.underline}   Courant absorbé par phase

  R                 Résistance d'induit

  X                 Réactance cyclique (X = L·ω)

  [E]{.underline}   force électromotrice (fem) induite
  -------------------------------------------------------------------------------

Figure 2 -- Modèle électrique d'une phase d'une machine, paramètres et
diagramme vectoriel associés

**1.** À partir des données constructeur, **exprimer** et **calculer**
pour le point de fonctionnement nominal :

> --- la valeur efficace V~n~ de la tension d'alimentation
> [V]{.underline} d'une phase de la machine,
>
> --- la puissance mécanique P~m~ délivrée par la machine,
>
> --- la puissance électrique active P~abs~ qu'elle absorbe.

**2. Déduire** de la question précédente :

> --- le facteur de puissance de la machine à son point de
> fonctionnement nominal : cos(ϕ~n~),
>
> --- la résistance R d'une phase d'induit.

**3. Calculer** la valeur de la puissance réactive Q~abs~ absorbée par
la machine à son point de fonctionnement nominal.

[Hypothèse sur l'angle]{.smallcaps} Ψ. On suppose pour les deux
questions suivantes que la fem [E]{.underline} est en phase avec le
courant [I]{.underline}, c'est à dire que Ψ = 0.

**4. Exprimer** la puissance réactive Q~abs~ absorbée par la machine en
fonction notamment de la réactance cyclique X. **En déduire** la valeur
de l'inductance cyclique L.

[Constante de couplage]{.smallcaps}. La valeur efficace de la fem E est
proportionnelle à la vitesse de rotation Ω~m~ de la machine :
E = K·Ω~m~.

**5. Déterminer** l'expression de la constante de couplage K et donner
sa valeur dans les unités du système international.

**[Grandeurs électriques maximales en entrée de la
machine]{.underline}**

[Couple délivré par la machine]{.smallcaps}. On admet que le couple C~m~
délivré par une machine synchrone à aimants peut, dans le cadre des
hypothèses de l'étude, s'exprimer par la relation suivante (les
notations de la figure 2 sont conservées) :

C~m~ = 3·K·cos(Ψ)·I

[Points de fonctionnement visés]{.smallcaps}. La détermination des
grandeurs électriques maximales en entrée de la machine passe par
l'étude de deux points de fonctionnement particuliers : le décollage et
la fin de la phase d'accélération.

> --- Au décollage de la bourreuse (mise en marche à partir de la
> vitesse nulle), les phénomènes d'adhérence imposent d'appliquer un
> effort de traction plus important que lorsque la bourreuse est en
> mouvement. Ce point de fonctionnement impose le courant maximal
> absorbé par la machine. Lors du décollage de la bourreuse, la machine
> délivre un couple C~mdec~ = 140 N·m.
>
> --- À la fin de la phase d'accélération, la machine délivre un couple
> C~mfa~ = 115 N·m et tourne à la vitesse N~fa~ = 1700 tr/min.

[Paramètres électriques de la machine]{.smallcaps}. Il est rappelé que
le modèle électrique de la machine est donné figure 2. Quels que soient
les résultats trouvés précédemment, on utilisera les valeurs suivantes
dans la suite de cette étude :

R = 0,27 Ω ; L = 4,1 mH ; K = 0,95 V·s/rad

[Pilotage de la machine]{.smallcaps}. L'onduleur qui alimente la machine
est asservi pour maintenir l'angle Ψ (angle d'autopilotage) à 0.

**6. Expliquer** l'intérêt de maintenir l'angle Ψ à 0.

**7.** En supposant Ψ = 0, **calculer** le courant efficace I~dec~
absorbé par la machine lors du décollage de la bourreuse.

**8.** En supposant Ψ = 0, **calculer** le courant efficace I~fa~
absorbé par la machine et la tension efficace V~fa~ aux bornes d'une de
ses phases à la fin de la phase d'accélération.

![](13-MAS-MS/Cours/pandoc/media/image145.png){width="7.245246062992126in"
height="1.5014063867016623in"}

![](13-MAS-MS/Cours/pandoc/media/image146.png){width="7.118994969378828in"
height="3.0385804899387576in"}

![](13-MAS-MS/Cours/pandoc/media/image147.png){width="7.2182939632545935in"
height="3.7260148731408576in"}

![](13-MAS-MS/Cours/pandoc/media/image148.png){width="7.165909886264217in"
height="3.232224409448819in"}

![](13-MAS-MS/Cours/pandoc/media/image149.png){width="7.2349311023622045in"
height="4.978365048118985in"}

![](13-MAS-MS/Cours/pandoc/media/image150.png){width="7.194997812773403in"
height="4.935843175853019in"}

![](13-MAS-MS/Cours/pandoc/media/image151.png){width="7.351654636920385in"
height="5.108452537182852in"}

![](13-MAS-MS/Cours/pandoc/media/image152.png){width="7.307403762029746in"
height="4.868077427821523in"}

![](13-MAS-MS/Cours/pandoc/media/image153.png){width="7.0836636045494314in"
height="4.961538713910761in"}

![](13-MAS-MS/Cours/pandoc/media/image154.png){width="7.111826334208224in"
height="3.2675951443569553in"}

![](13-MAS-MS/Cours/pandoc/media/image155.png){width="7.3271544181977255in"
height="5.178631889763779in"}

![](13-MAS-MS/Cours/pandoc/media/image156.emf){width="6.827083333333333in"
height="4.551388888888889in"}

![](13-MAS-MS/Cours/pandoc/media/image157.emf){width="7.268055555555556in"
height="4.229166666666667in"}

![](13-MAS-MS/Cours/pandoc/media/image158.emf){width="7.268055555555556in"
height="3.2333333333333334in"}

![](13-MAS-MS/Cours/pandoc/media/image159.emf){width="7.268055555555556in"
height="4.3277777777777775in"}

![](13-MAS-MS/Cours/pandoc/media/image160.emf){width="7.268055555555556in"
height="3.8652777777777776in"}

![](13-MAS-MS/Cours/pandoc/media/image161.emf){width="7.268055555555556in"
height="4.6722222222222225in"}![](13-MAS-MS/Cours/pandoc/media/image162.emf){width="7.268055555555556in"
height="1.3173611111111112in"}

---
## Inventaire des images
13-MAS-MS/Cours/pandoc/media/image1.png
13-MAS-MS/Cours/pandoc/media/image10.jpeg
13-MAS-MS/Cours/pandoc/media/image100.png
13-MAS-MS/Cours/pandoc/media/image101.wmf
13-MAS-MS/Cours/pandoc/media/image102.wmf
13-MAS-MS/Cours/pandoc/media/image103.wmf
13-MAS-MS/Cours/pandoc/media/image104.png
13-MAS-MS/Cours/pandoc/media/image105.png
13-MAS-MS/Cours/pandoc/media/image106.png
13-MAS-MS/Cours/pandoc/media/image107.emf
13-MAS-MS/Cours/pandoc/media/image108.emf
13-MAS-MS/Cours/pandoc/media/image109.png
13-MAS-MS/Cours/pandoc/media/image11.png
13-MAS-MS/Cours/pandoc/media/image110.png
13-MAS-MS/Cours/pandoc/media/image111.png
13-MAS-MS/Cours/pandoc/media/image112.emf
13-MAS-MS/Cours/pandoc/media/image113.emf
13-MAS-MS/Cours/pandoc/media/image114.png
13-MAS-MS/Cours/pandoc/media/image115.png
13-MAS-MS/Cours/pandoc/media/image116.png
13-MAS-MS/Cours/pandoc/media/image117.jpeg
13-MAS-MS/Cours/pandoc/media/image118.png
13-MAS-MS/Cours/pandoc/media/image119.png
13-MAS-MS/Cours/pandoc/media/image12.png
13-MAS-MS/Cours/pandoc/media/image120.wmf
13-MAS-MS/Cours/pandoc/media/image121.wmf
13-MAS-MS/Cours/pandoc/media/image123.png
13-MAS-MS/Cours/pandoc/media/image124.png
13-MAS-MS/Cours/pandoc/media/image125.png
13-MAS-MS/Cours/pandoc/media/image126.png
13-MAS-MS/Cours/pandoc/media/image127.png
13-MAS-MS/Cours/pandoc/media/image128.emf
13-MAS-MS/Cours/pandoc/media/image13.png
13-MAS-MS/Cours/pandoc/media/image130.png
13-MAS-MS/Cours/pandoc/media/image131.png
13-MAS-MS/Cours/pandoc/media/image132.emf
13-MAS-MS/Cours/pandoc/media/image133.emf
13-MAS-MS/Cours/pandoc/media/image134.emf
13-MAS-MS/Cours/pandoc/media/image135.emf
13-MAS-MS/Cours/pandoc/media/image136.jpeg
13-MAS-MS/Cours/pandoc/media/image137.png
13-MAS-MS/Cours/pandoc/media/image138.png
13-MAS-MS/Cours/pandoc/media/image139.png
13-MAS-MS/Cours/pandoc/media/image14.png
13-MAS-MS/Cours/pandoc/media/image140.emf
13-MAS-MS/Cours/pandoc/media/image141.emf
13-MAS-MS/Cours/pandoc/media/image142.emf
13-MAS-MS/Cours/pandoc/media/image143.png
13-MAS-MS/Cours/pandoc/media/image144.png
13-MAS-MS/Cours/pandoc/media/image145.png
13-MAS-MS/Cours/pandoc/media/image146.png
13-MAS-MS/Cours/pandoc/media/image147.png
13-MAS-MS/Cours/pandoc/media/image148.png
13-MAS-MS/Cours/pandoc/media/image149.png
13-MAS-MS/Cours/pandoc/media/image15.png
13-MAS-MS/Cours/pandoc/media/image150.png
13-MAS-MS/Cours/pandoc/media/image151.png
13-MAS-MS/Cours/pandoc/media/image152.png
13-MAS-MS/Cours/pandoc/media/image153.png
13-MAS-MS/Cours/pandoc/media/image154.png
13-MAS-MS/Cours/pandoc/media/image155.png
13-MAS-MS/Cours/pandoc/media/image156.emf
13-MAS-MS/Cours/pandoc/media/image157.emf
13-MAS-MS/Cours/pandoc/media/image158.emf
13-MAS-MS/Cours/pandoc/media/image159.emf
13-MAS-MS/Cours/pandoc/media/image16.emf
13-MAS-MS/Cours/pandoc/media/image160.emf
13-MAS-MS/Cours/pandoc/media/image161.emf
13-MAS-MS/Cours/pandoc/media/image162.emf
13-MAS-MS/Cours/pandoc/media/image17.png
13-MAS-MS/Cours/pandoc/media/image18.png
13-MAS-MS/Cours/pandoc/media/image19.png
13-MAS-MS/Cours/pandoc/media/image20.gif
13-MAS-MS/Cours/pandoc/media/image21.png
13-MAS-MS/Cours/pandoc/media/image22.png
13-MAS-MS/Cours/pandoc/media/image23.png
13-MAS-MS/Cours/pandoc/media/image24.emf
13-MAS-MS/Cours/pandoc/media/image26.emf
13-MAS-MS/Cours/pandoc/media/image27.emf
13-MAS-MS/Cours/pandoc/media/image28.jpeg
13-MAS-MS/Cours/pandoc/media/image29.emf
13-MAS-MS/Cours/pandoc/media/image3.emf
13-MAS-MS/Cours/pandoc/media/image30.png
13-MAS-MS/Cours/pandoc/media/image32.png
13-MAS-MS/Cours/pandoc/media/image33.png
13-MAS-MS/Cours/pandoc/media/image34.wmf
13-MAS-MS/Cours/pandoc/media/image35.wmf
13-MAS-MS/Cours/pandoc/media/image36.wmf
13-MAS-MS/Cours/pandoc/media/image37.emf
13-MAS-MS/Cours/pandoc/media/image38.png
13-MAS-MS/Cours/pandoc/media/image39.png
13-MAS-MS/Cours/pandoc/media/image40.emf
13-MAS-MS/Cours/pandoc/media/image41.png
13-MAS-MS/Cours/pandoc/media/image42.jpeg
13-MAS-MS/Cours/pandoc/media/image43.wmf
13-MAS-MS/Cours/pandoc/media/image44.wmf
13-MAS-MS/Cours/pandoc/media/image45.wmf
13-MAS-MS/Cours/pandoc/media/image46.wmf
13-MAS-MS/Cours/pandoc/media/image47.wmf
13-MAS-MS/Cours/pandoc/media/image48.png
13-MAS-MS/Cours/pandoc/media/image49.wmf
13-MAS-MS/Cours/pandoc/media/image5.png
13-MAS-MS/Cours/pandoc/media/image50.wmf
13-MAS-MS/Cours/pandoc/media/image51.wmf
13-MAS-MS/Cours/pandoc/media/image52.png
13-MAS-MS/Cours/pandoc/media/image53.png
13-MAS-MS/Cours/pandoc/media/image54.png
13-MAS-MS/Cours/pandoc/media/image55.png
13-MAS-MS/Cours/pandoc/media/image56.png
13-MAS-MS/Cours/pandoc/media/image57.png
13-MAS-MS/Cours/pandoc/media/image58.png
13-MAS-MS/Cours/pandoc/media/image59.png
13-MAS-MS/Cours/pandoc/media/image6.png
13-MAS-MS/Cours/pandoc/media/image60.jpeg
13-MAS-MS/Cours/pandoc/media/image61.wmf
13-MAS-MS/Cours/pandoc/media/image62.emf
13-MAS-MS/Cours/pandoc/media/image63.emf
13-MAS-MS/Cours/pandoc/media/image64.emf
13-MAS-MS/Cours/pandoc/media/image65.wmf
13-MAS-MS/Cours/pandoc/media/image66.wmf
13-MAS-MS/Cours/pandoc/media/image67.wmf
13-MAS-MS/Cours/pandoc/media/image68.wmf
13-MAS-MS/Cours/pandoc/media/image69.wmf
13-MAS-MS/Cours/pandoc/media/image7.png
13-MAS-MS/Cours/pandoc/media/image70.wmf
13-MAS-MS/Cours/pandoc/media/image71.wmf
13-MAS-MS/Cours/pandoc/media/image72.wmf
13-MAS-MS/Cours/pandoc/media/image73.wmf
13-MAS-MS/Cours/pandoc/media/image74.emf
13-MAS-MS/Cours/pandoc/media/image75.wmf
13-MAS-MS/Cours/pandoc/media/image76.png
13-MAS-MS/Cours/pandoc/media/image77.png
13-MAS-MS/Cours/pandoc/media/image78.png
13-MAS-MS/Cours/pandoc/media/image79.png
13-MAS-MS/Cours/pandoc/media/image8.wmf
13-MAS-MS/Cours/pandoc/media/image80.png
13-MAS-MS/Cours/pandoc/media/image81.png
13-MAS-MS/Cours/pandoc/media/image82.png
13-MAS-MS/Cours/pandoc/media/image83.png
13-MAS-MS/Cours/pandoc/media/image84.png
13-MAS-MS/Cours/pandoc/media/image85.png
13-MAS-MS/Cours/pandoc/media/image86.jpeg
13-MAS-MS/Cours/pandoc/media/image87.png
13-MAS-MS/Cours/pandoc/media/image88.jpeg
13-MAS-MS/Cours/pandoc/media/image9.png
13-MAS-MS/Cours/pandoc/media/image90.wmf
13-MAS-MS/Cours/pandoc/media/image91.jpeg
13-MAS-MS/Cours/pandoc/media/image92.png
13-MAS-MS/Cours/pandoc/media/image93.jpeg
13-MAS-MS/Cours/pandoc/media/image94.jpeg
13-MAS-MS/Cours/pandoc/media/image95.png
13-MAS-MS/Cours/pandoc/media/image96.png
13-MAS-MS/Cours/pandoc/media/image97.jpeg
13-MAS-MS/Cours/pandoc/media/image98.png
13-MAS-MS/Cours/pandoc/media/image99.png
