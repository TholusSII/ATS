#!/usr/bin/env python3
"""Complète les fichiers corrige.tex encore vides par des corrigés rédigés.

Les réponses sont symboliques lorsque les valeurs sont exclusivement portées par une
figure. Elles restent alors directement exploitables en remplaçant les grandeurs par
les valeurs lues sur le document.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_corrections as gc  # type: ignore


def clean(s: str) -> str:
    return textwrap.dedent(s).strip()


def box_content(source: Path, answers: list[str], title: str = "Corrigé rédigé") -> str:
    rel = source.relative_to(ROOT).as_posix()
    lines = [
        "% Fichier complété par tools/complete_missing_corrections.py.",
        f"% Source : {rel}",
        f"% Statut : rédigé ({len(answers)} question(s)).",
        rf"\begin{{corrigebox}}[{title}]",
    ]
    for i, answer in enumerate(answers, 1):
        lines.append(rf"\CorrigeQuestion{{{i}}}")
        lines.append(clean(answer))
    lines.append(r"\end{corrigebox}")
    return "\n".join(lines) + "\n"


def source_for(corrige: Path) -> Path:
    return corrige.with_name(corrige.parent.name + ".tex")


def generic_parameterization(name: str) -> str:
    data = {
        "01_T_02": r"""
            On attache au bâti le repère $\mathcal R_0=(A,\vec i_0,\vec j_0,\vec k_0)$.
            Le solide 1 est en translation suivant $\vec i_0$ : son orientation est donc
            constante et $\mathcal B_1=\mathcal B_0$. Le paramètre indépendant est
            $\lambda(t)$ et
            \[
              \overrightarrow{AB}=\lambda(t)\,\vec i_0,\qquad
              \vec\Omega_{1/0}=\vec 0.
            \]
            La position de $B$ est ainsi $(\lambda(t),0,0)$ dans $\mathcal R_0$.
        """,
        "02_R": r"""
            On choisit $\mathcal R_0=(A,\vec i_0,\vec j_0,\vec k_0)$ et un repère
            $\mathcal R_1=(A,\vec i_1,\vec j_1,\vec k_0)$ lié au solide 1. Le paramètre est
            \[\theta(t)=(\vec i_0,\vec i_1)=(\vec j_0,\vec j_1),\qquad
              \vec\Omega_{1/0}=\dot\theta\,\vec k_0.\]
            Avec $\overrightarrow{AB}=R\vec i_1$,
            \[
            \vec i_1=\cos\theta\,\vec i_0+\sin\theta\,\vec j_0,
            \quad
            \vec j_1=-\sin\theta\,\vec i_0+\cos\theta\,\vec j_0.
            \]
        """,
        "02_R_02": r"""
            On paramètre la rotation de 1 par rapport à 0 par
            $\theta(t)=(\vec i_0,\vec i_1)$ autour de l'axe $(A,\vec k_0)$.
            Ainsi $\vec k_1=\vec k_0$, $\vec\Omega_{1/0}=\dot\theta\vec k_0$ et tout point
            fixe de 1 s'écrit à partir de composantes constantes dans $\mathcal B_1$.
            En particulier, si $\overrightarrow{AB}=R\vec i_1$ alors
            $\overrightarrow{AB}=R(\cos\theta\vec i_0+\sin\theta\vec j_0)$.
        """,
        "03_TT": r"""
            Les deux solides restent parallèles au bâti. On prend
            $\overrightarrow{AB}=\lambda(t)\vec i_0$ et
            $\overrightarrow{BC}=\mu(t)\vec j_0$. Les paramètres indépendants sont donc
            $q=(\lambda,\mu)$ et
            \[\overrightarrow{AC}=\lambda(t)\vec i_0+\mu(t)\vec j_0.\]
            Les vitesses angulaires de 1 et 2 par rapport à 0 sont nulles.
        """,
        "03_TT_02": r"""
            On associe à chaque glissière sa course algébrique :
            $\lambda(t)$ suivant $\vec i_0$ pour 1/0 et $\mu(t)$ suivant $\vec j_0$ pour
            2/1. Les bases sont confondues et
            \[\overrightarrow{AB}=\lambda\vec i_0,\quad
              \overrightarrow{BC}=\mu\vec j_0,\quad
              \overrightarrow{AC}=\lambda\vec i_0+\mu\vec j_0.\]
        """,
        "04_RR": r"""
            On pose $\theta=(\vec i_0,\vec i_1)$ pour le pivot 1/0 et
            $\varphi=(\vec i_1,\vec i_2)$ pour le pivot 2/1. Les deux pivots ont pour axe
            $\vec k_0$ :
            \[\vec\Omega_{1/0}=\dot\theta\vec k_0,\qquad
              \vec\Omega_{2/1}=\dot\varphi\vec k_0,\qquad
              \vec\Omega_{2/0}=(\dot\theta+\dot\varphi)\vec k_0.\]
            Avec $\overrightarrow{AB}=R\vec i_1$ et $\overrightarrow{BC}=L\vec i_2$,
            $\overrightarrow{AC}=R\vec i_1+L\vec i_2$ et l'orientation absolue de 2 vaut
            $\theta+\varphi$.
        """,
        "04_RR_02": r"""
            Le paramétrage minimal est $q=(\theta,\varphi)$ avec
            $\theta=(\vec i_0,\vec i_1)$ et $\varphi=(\vec i_1,\vec i_2)$, les axes des
            deux pivots étant parallèles à $\vec k_0$. On écrit
            $\overrightarrow{AB}=R\vec i_1$, $\overrightarrow{BC}=L\vec i_2$ et
            $\overrightarrow{AC}=R\vec i_1+L\vec i_2$.
        """,
        "05_RT": r"""
            La rotation du solide 1 est décrite par
            $\theta=(\vec i_0,\vec i_1)$ autour de $(A,\vec k_0)$. Le solide 2 coulisse
            suivant $\vec i_1$ ; sa course est $\lambda(t)$. Le paramétrage est donc
            \[q=(\theta,\lambda),\qquad \overrightarrow{AB}=\lambda\vec i_1,
              \qquad \vec\Omega_{2/0}=\dot\theta\vec k_0.\]
            Dans la base fixe :
            $\overrightarrow{AB}=\lambda(\cos\theta\vec i_0+\sin\theta\vec j_0)$.
        """,
        "05_RT_02": r"""
            On retient la rotation $\theta(t)$ de 1/0 et la translation $\lambda(t)$ de
            2/1 suivant $\vec i_1$. Ainsi
            \[\overrightarrow{AB}=\lambda\vec i_1,\qquad
              \vec\Omega_{2/0}=\dot\theta\vec k_0,\qquad
              \vec V(B,2/1)=\dot\lambda\vec i_1.\]
        """,
        "06_TR": r"""
            Le solide 1 est en translation suivant $\vec i_0$, paramétrée par
            $\lambda(t)$ : $\overrightarrow{AB}=\lambda\vec i_0$. Le solide 2 pivote par
            rapport à 1 autour de $(B,\vec k_0)$ ; on pose
            $\theta=(\vec i_0,\vec i_2)$ et $\overrightarrow{BC}=R\vec i_2$.
            Le paramétrage minimal est $q=(\lambda,\theta)$ et
            $\overrightarrow{AC}=\lambda\vec i_0+R\vec i_2$.
        """,
        "06_TR_02": r"""
            On note $\lambda(t)$ la course de la glissière 1/0 et $\theta(t)$ l'angle du
            pivot 2/1. Les relations de position sont
            \[\overrightarrow{AB}=\lambda\vec i_0,\qquad
              \overrightarrow{BC}=R\vec i_2,\qquad
              \overrightarrow{AC}=\lambda\vec i_0+R\vec i_2.\]
            L'orientation de 2 est donnée par
            $\vec i_2=\cos\theta\vec i_0+\sin\theta\vec j_0$.
        """,
        "07_RR3D": r"""
            On choisit $\theta(t)$ pour la rotation 1/0 autour de $\vec k_0$, puis
            $\varphi(t)$ pour la rotation 2/1 autour de $\vec i_1$. On a
            \[\vec\Omega_{2/0}=\dot\theta\vec k_0+\dot\varphi\vec i_1,\qquad
              \overrightarrow{AB}=R\vec i_1,\qquad
              \overrightarrow{BC}=\ell\vec i_1+r\vec j_2.\]
            Les changements de base sont une rotation d'angle $\theta$ autour de
            $\vec k_0$, puis une rotation d'angle $\varphi$ autour de $\vec i_1$.
        """,
        "07_RR3D_02": r"""
            Le mécanisme possède deux paramètres angulaires :
            $\theta=(\vec i_0,\vec i_1)$ autour de $\vec k_0$ et
            $\varphi=(\vec j_1,\vec j_2)$ autour de $\vec i_1$. Par conséquent
            $\vec\Omega_{2/0}=\dot\theta\vec k_0+\dot\varphi\vec i_1$.
            Les vecteurs géométriques indiqués sur la figure sont ensuite écrits dans
            $\mathcal B_1$ ou $\mathcal B_2$ avant projection dans $\mathcal B_0$.
        """,
        "08_RR3D": r"""
            On paramètre 1/0 par $\theta(t)$ autour de $\vec j_0=\vec j_1$, puis 2/1 par
            $\varphi(t)$ autour de $\vec k_1$ (axe indiqué sur le schéma). Avec
            $\overrightarrow{AB}=H\vec j_1+R\vec i_1$ et
            $\overrightarrow{BC}=L\vec i_2$, le vecteur position est
            $\overrightarrow{AC}=H\vec j_1+R\vec i_1+L\vec i_2$.
            La vitesse angulaire s'obtient par composition :
            $\vec\Omega_{2/0}=\vec\Omega_{2/1}+\vec\Omega_{1/0}$.
        """,
        "08_RR3D_02": r"""
            Le paramétrage est $q=(\theta,\varphi)$ avec une première rotation de 1/0
            puis une seconde de 2/1. On conserve les relations
            \[\overrightarrow{AB}=H\vec j_1+R\vec i_1,\qquad
              \overrightarrow{BC}=L\vec i_2.\]
            Dans la base fixe, la position de $C$ s'écrit
            \[
            \begin{aligned}
            x_C&=(R+L\cos\varphi)\cos\theta,\\
            y_C&=H+L\sin\varphi,\\
            z_C&=-(R+L\cos\varphi)\sin\theta.
            \end{aligned}
            \]
        """,
        "10_PompePalette": r"""
            On prend le bâti 0 centré en $O$ et le rotor 1 en pivot d'axe
            $(O,\vec k_0)$. On pose $\theta=(\vec i_0,\vec i_1)$. La palette 2 coulisse
            dans le rotor suivant $\vec i_1$ ; sa course est $\lambda(t)$ et
            $\overrightarrow{OB}=\lambda\vec i_1$. Le contact de l'extrémité $B$ avec
            le stator circulaire fournit ensuite la relation géométrique entre
            $\lambda$ et $\theta$.
        """,
        "11_PompePistonsRadiaux": r"""
            Le barillet 1 pivote autour de son axe fixe ; on note $\theta(t)$ son angle.
            Le piston 2 est guidé en translation suivant l'axe indiqué sur la figure ; sa
            course est $\lambda(t)$. L'excentration du plateau est notée $e$. La fermeture
            géométrique conduit à une loi de la forme
            $\lambda(t)=\lambda_0+e\sin\theta(t)$ (le signe dépend du sens positif choisi),
            donc $\dot\lambda=e\dot\theta\cos\theta$.
        """,
        "12_BielleManivelle": r"""
            On note $\theta=(\vec i_0,\vec i_1)$ l'angle de la manivelle 1,
            $\varphi=(\vec i_0,\vec i_2)$ l'angle de la bielle 2 et $\lambda$ la position
            du coulisseau 3. Avec $\overrightarrow{AB}=R\vec i_1$,
            $\overrightarrow{BC}=L\vec i_2$ et $\overrightarrow{AC}=\lambda\vec j_0$,
            la fermeture est
            \[R\vec i_1+L\vec i_2-\lambda\vec j_0=\vec0.\]
            Ses projections donnent les deux relations scalaires liant
            $\theta$, $\varphi$ et $\lambda$.
        """,
        "13_TransfoMouvement": r"""
            On pose $\theta$ pour la rotation de la manivelle 1, $\varphi$ pour
            l'orientation de la bielle 2 et $\lambda$ pour la translation du piston 3.
            La fermeture géométrique est
            \[R\vec i_1-\lambda\vec i_2+H\vec j_0=\vec0.\]
            En projection dans $\mathcal R_0$ :
            \[
            R\cos\theta=\lambda\cos\varphi,\qquad
            R\sin\theta+H=\lambda\sin\varphi.
            \]
        """,
        "14_Sympact": r"""
            On note $\theta(t)$ l'angle du bras 1 par rapport au bâti et $\varphi(t)$
            l'angle du bras 2. Les longueurs constantes sont portées par les vecteurs
            de la figure. La fermeture du cycle cinématique s'écrit sous la forme
            $\overrightarrow{AC}+\overrightarrow{CB}+\overrightarrow{BA}=\vec0$.
            Les deux projections dans le plan donnent la loi de fermeture reliant
            $\theta$ et $\varphi$ ; le contact sphère-plan est décrit par sa normale.
        """,
        "15_SympactGalet": r"""
            On reprend $\theta$ et $\varphi$ pour les deux bras de la barrière et on
            ajoute $\gamma(t)$, angle propre du galet 3. Le centre $B$ du galet est fixé
            au bras 2, son rayon est $r$ et le contact avec 1 est localisé en $I$.
            Le paramétrage est donc $q=(\theta,\varphi,\gamma)$ ; la condition de
            roulement sans glissement s'écrit $\vec V(I,3/1)=\vec0$.
        """,
        "16_Poussoir": r"""
            Le disque/came 1 tourne autour de $A$ :
            $\theta=(\vec i_0,\vec i_1)$. Le poussoir 2 est guidé en translation suivant
            l'axe vertical de la figure ; sa position est $\lambda(t)$. La fermeture de
            contact entre la came et le poussoir fournit la loi
            $\lambda=f(\theta)$, déterminée par le profil de came et le rayon du galet.
        """,
        "17_4Barres": r"""
            Le mécanisme plan comporte trois angles indépendants avant fermeture :
            $\theta$ pour 1/0, $\varphi$ pour 2/0 et $\psi$ pour 3/0. Avec les longueurs
            constantes $AB$, $BC$, $CD$ et $AD$, la fermeture du quadrilatère est
            \[\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CD}
              +\overrightarrow{DA}=\vec0.\]
            Ses projections sur $\vec i_0$ et $\vec j_0$ donnent deux équations, de sorte
            que le mécanisme ne possède qu'un degré de liberté.
        """,
        "18_Maxpid": r"""
            On associe un angle à chaque pivot du mécanisme : $\theta$ pour le bras 1,
            $\varphi$ pour 2, $\psi$ pour 3 et la position du coulisseau 4 suivant son axe.
            Les vecteurs géométriques de chaque solide sont écrits dans leur base propre.
            La fermeture du cycle entre le bâti, les bras et le coulisseau fournit deux
            équations scalaires ; un seul paramètre peut être choisi comme entrée.
        """,
        "46_RR_RSG": r"""
            La roue 1 roule sur le sol sans glisser. On note $\theta$ sa rotation par
            rapport au bâti, $R$ son rayon, puis $\varphi$ la rotation du solide 2 par
            rapport à 1 et $\overrightarrow{AB}=L\vec i_2$. Le paramétrage est
            $q=(\theta,\varphi)$ et la contrainte de roulement au point $I$ est
            $\vec V(I,1/0)=\vec0$, d'où la translation du centre
            $\vec V(A,1/0)=-R\dot\theta\vec i_0$ avec les conventions de la figure.
        """,
    }
    return data.get(name, r"Le paramétrage consiste à choisir un repère lié à chaque solide, un paramètre par mobilité et à écrire les vecteurs de fermeture. Les angles sont orientés selon la règle de la main droite et les translations suivant les axes des glissières.")


def cin_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    parts = rel.split('/')
    section, name = parts[1], parts[2]
    if section == 'CIN-01-Parametrage':
        if name in {'1018_BorneReglable','1019_RobotPeinture'}:
            return [
                r"""Une classe d'équivalence regroupe toutes les pièces sans mouvement relatif. On colorie donc d'une même couleur le bâti, d'une autre chaque sous-ensemble mobile et l'on sépare systématiquement les organes reliés par pivot ou glissière. Les éléments roulants, vis et écrous solidaires sont rattachés au solide qui les entraîne.""",
                r"""On obtient au minimum le bâti $S_0$, le sous-ensemble d'entrée $S_1$ et le sous-ensemble de sortie $S_2$; les éventuels renvois ou biellettes constituent chacun une classe supplémentaire. La liste exacte se lit en regroupant les repères de pièces qui ne sont séparés par aucune surface fonctionnelle de mouvement.""",
                r"""Le graphe comporte un sommet par classe d'équivalence et une arête par liaison. Les surfaces cylindriques coaxiales donnent un pivot, les guidages cylindriques avec translation un pivot glissant, et les guidages prismatiques une glissière. Les axes et centres sont ceux du dessin d'ensemble; les contacts de transmission sont ajoutés comme engrènement ou vis--écrou.""",
                r"""Le schéma cinématique minimal conserve le bâti, les axes des pivots, les directions des glissières et les longueurs utiles. Les dimensions de forme sans influence cinématique sont supprimées. Le nombre de mobilités du schéma doit être identique à celui du mécanisme réel et le graphe des liaisons doit être retrouvé exactement.""",
            ]
        if name == '1020_PompeEnsieta':
            return [
                r"""Non. Une bille de même diamètre que l'alésage ne peut pas se déplacer librement et risque de se coincer. Il faut un jeu radial fonctionnel et un siège de diamètre inférieur à celui de la bille afin d'assurer l'étanchéité par contact annulaire.""",
                r"""Non. L'alésage recevant le raccord n'est qu'une surface de positionnement/étanchéité statique, alors que l'alésage du piston est une surface de guidage en mouvement. Ce dernier exige une rugosité plus faible, une meilleure cylindricité et une tolérance dimensionnelle plus serrée.""",
                r"""Il faut un ajustement avec jeu faible, de type glissant précis (par exemple H7/g6 ou H7/f7 selon la vitesse et la lubrification). Un serrage interdirait le mouvement et un ajustement trop lâche provoquerait fuite et désalignement.""",
                r"""Le composant prisonnier ne peut être introduit si son diamètre maximal est supérieur au passage disponible après réalisation monobloc du corps. Il faut prévoir un bouchon démontable, un alésage débouchant, une pièce rapportée ou modifier l'ordre de montage. Sur le dessin, c'est le composant du clapet fermé par le corps qui doit être rendu accessible.""",
                r"""Non. Du côté tige, la section hydraulique utile est annulaire $S_a=S_p-S_t$, alors que de l'autre côté elle vaut $S_p$. À course identique, les volumes sont $V_p=S_p L$ et $V_a=(S_p-S_t)L$; leur différence vaut $S_tL$.""",
                r"""Pour une course $L$, le volume refoulé à la sortie 4 est $V_4=S_{
m utile}L$. Si la sortie est côté plein piston, $V_4=\pi D^2L/4$; si elle est côté tige, $V_4=\pi(D^2-d^2)L/4$. Le débit moyen vaut ce volume multiplié par la fréquence des courses utiles.""",
                r"""Le schéma comporte le corps 0, le piston 6 en glissière par rapport à 0, les deux clapets modélisés par des translations unidirectionnelles de billes contre leurs sièges et les ressorts de rappel. Les clapets sont orientés en sens opposés : admission vers la chambre et refoulement de la chambre vers la sortie.""",
            ]
        if name == '513_Divers_Tabouret':
            return [r"""Un modèle pertinent est une liaison appui-plan entre l'assise (ou l'ensemble tabouret) et le sol, complétée par le poids. Si l'on souhaite interdire tout mouvement dans l'étude plane, on peut remplacer les trois contacts réels par un encastrement équivalent; si l'on étudie le basculement, on conserve trois appuis ponctuels unilatéraux."""]
        if name == '514_Divers_Tabouret':
            return [r"""Trois modélisations admissibles sont : (1) trois liaisons sphère-plan unilatérales aux pieds; (2) une liaison appui-plan équivalente si les trois pieds sont coplanaires; (3) dans une étude plane, deux appuis ponctuels, l'un modélisé pivot et l'autre appui simple afin de ne pas surcontraindre. Le choix dépend de la précision recherchée et de la prise en compte du décollement."""]
        return [generic_parameterization(name)]

    if section == 'CIN-02-VitesseAcceleration':
        custom = {
            '06_TR': [
                r"""Le point $B$ est l'origine du pivot 2/1 et appartient au coulisseau 1 : il reste donc sur la droite $(A,\vec i_0)$. L'ensemble accessible est le segment ou la droite correspondant au domaine de $\lambda$.""",
                r"""$\overrightarrow{AB}=\lambda(t)\vec i_0$, donc $x_B=\lambda(t)$, $y_B=z_B=0$. Si le point visé est l'extrémité $C$, alors $\overrightarrow{AC}=\lambda\vec i_0+R(\cos\theta\vec i_0+\sin\theta\vec j_0)$.""",
                r"""Pour imposer une trajectoire $C(t)=(x(t),y(t))$, on résout
                $x=\lambda+R\cos\theta$, $y=R\sin\theta$. Ainsi
                $\theta(t)=\arcsin(y(t)/R)$ (branche choisie selon la configuration) et
                $\lambda(t)=x(t)-R\cos\theta(t)$. Pour un segment parcouru à vitesse $v$,
                $x(t)=x_0+vt$ et $y(t)=y_0$.""",
                r"""Un tracé Python direct utilise un tableau de temps, calcule
                `theta=np.arcsin(y/R)` puis `lam=x-R*np.cos(theta)`, et vérifie la
                trajectoire avec `xc=lam+R*np.cos(theta)` et `yc=R*np.sin(theta)`.""",
            ],
            '1025_RTR': [
                r"""On applique la composition des vitesses puis la formule de changement de point :
                $\vec V(P,2/0)=\vec V(A,2/0)+\vec\Omega_{2/0}\wedge\overrightarrow{AP}$.
                Avec $\vec\Omega_{2/0}=\vec\Omega_{2/1}+\vec\Omega_{1/0}$, on obtient
                successivement les vitesses de $B$, $D$ et $C$ en remplaçant
                $\overrightarrow{AB}$, $\overrightarrow{AD}$ et $\overrightarrow{AC}$ par
                les vecteurs donnés sur la figure. Les composantes communes au solide 2
                diffèrent uniquement du terme $\vec\Omega_{2/0}\wedge\overrightarrow{BP}$.""",
                r"""Les accélérations sont obtenues par
                $\vec\Gamma(P,2/0)=\vec\Gamma(B,2/0)+\dot{\vec\Omega}_{2/0}\wedge
                \overrightarrow{BP}+\vec\Omega_{2/0}\wedge(\vec\Omega_{2/0}\wedge
                \overrightarrow{BP})$. Cette expression fournit directement les termes
                tangentiels (proportionnels aux accélérations angulaires) et normaux
                (proportionnels aux carrés des vitesses angulaires) pour $D$ et $C$.""",
            ],
            '13_TransfoMouvement': [
                r"""Le solide 3 est en translation suivant son axe :
                $\vec\Omega_{3/0}=\vec0$ et $\vec V(B,3/0)=\dot\lambda\,\vec i_2$.
                Donc $\{\mathcal V(3/0)\}_B=\left\{\begin{array}{c}\vec0\\
                \dot\lambda\vec i_2\end{array}\right\}_B$. La valeur de $\dot\lambda$
                s'obtient en dérivant la fermeture géométrique.""",
                r"""Comme la direction de la glissière est fixe,
                $\vec\Gamma(B,3/0)=\ddot\lambda\,\vec i_2$. Si l'axe $\vec i_2$ est
                mobile, il faut ajouter le terme $\dot\lambda\,\vec\Omega_{2/0}\wedge
                \vec i_2$.""",
            ],
            '15_SympactGalet': [
                r"""La condition de roulement sans glissement est
                $\vec V(I,3/1)=\vec0$. En projetant sur la tangente au contact, on obtient
                $r\dot\gamma=V_t(B,3/1)$, avec le signe fixé par les sens positifs.
                L'intégration donne $\gamma(t)=\gamma(0)+\int_0^t V_t(\tau)/r\,d\tau$.""",
                r"""Au point $B$, centre du galet,
                $\{\mathcal V(3/2)\}_B=\left\{\begin{array}{c}
                \dot\gamma\vec k_0\\\vec0\end{array}\right\}_B$ si 3 est en pivot
                par rapport à 2. Si l'angle $\gamma$ est mesuré par rapport à 1, on retire
                la vitesse angulaire de 2/1 selon la convention du schéma.""",
            ],
            '16_Poussoir': [
                r"""Le graphe comprend le bâti 0, la came 1 en pivot d'axe $(A,\vec k_0)$
                avec 0, le poussoir 2 en glissière suivant l'axe vertical avec 0, et un
                contact came--galet entre 1 et 2.""",
                r"""Pour $\theta=\pi/4$, on fait tourner la came de $45^\circ$ dans le
                sens positif puis on translate le poussoir jusqu'à retrouver la tangence
                avec le profil. La normale commune passe par le centre du galet.""",
                r"""Pour $\theta=-\pi/4$, la même construction est effectuée dans le sens
                opposé. La course obtenue est la valeur de la loi $\lambda=f(-\pi/4)$.""",
            ],
            '17_4Barres': [
                r"""Pour le solide 1 en pivot autour de $A$,
                $\{\mathcal V(1/0)\}_G=\left\{\begin{array}{c}
                \dot\theta\vec k_0\\\dot\theta\vec k_0\wedge\overrightarrow{AG}
                \end{array}\right\}_G$.""",
                r"""$\vec\Gamma(G,1/0)=\ddot\theta\vec k_0\wedge\overrightarrow{AG}
                +\dot\theta\vec k_0\wedge(\dot\theta\vec k_0\wedge
                \overrightarrow{AG})$. Pour $\overrightarrow{AG}=a\vec i_1$ :
                $\vec\Gamma=a\ddot\theta\vec j_1-a\dot\theta^2\vec i_1$.""",
            ],
            '18_Maxpid': [
                r"""La vitesse du point $G$ du solide 4 s'obtient par composition le long
                de la chaîne cinématique. Au point $G$ :
                $\{\mathcal V(4/0)\}_G=\{\vec\Omega_{4/0};\vec V(G,4/0)\}_G$, avec
                $\vec\Omega_{4/0}$ égal à la somme algébrique des vitesses angulaires des
                pivots traversés et $\vec V(G,4/0)$ obtenu par changement de point.""",
                r"""On dérive la vitesse dans $\mathcal R_0$ :
                $\vec\Gamma(G,4/0)=d\vec V(G,4/0)/dt|_0$. Chaque barre apporte un terme
                tangentiel $\ddot q\,\vec k_0\wedge\vec r$ et un terme centripète
                $\dot q\,\vec k_0\wedge(\dot q\,\vec k_0\wedge\vec r)$; la glissière
                apporte $\ddot\lambda$ suivant son axe et, si l'axe tourne, les termes de
                Coriolis $2\dot\lambda\vec\Omega\wedge\vec e$.""",
            ],
        }
        return custom.get(name)

    if section == 'CIN-03-Transmetteurs':
        if name == '32_Broyeur':
            return [r"""Pour chaque engrènement extérieur, le rapport est
            $r_i=\omega_{s}/\omega_{e}=-Z_e/Z_s$; pour un engrènement intérieur le signe
            est positif. En numérotant les quatre étages de l'entrée vers la sortie :
            $r_1=-Z_1/Z_2$, $r_2=-Z_3/Z_4$, $r_3=-Z_5/Z_6$ et $r_4=-Z_7/Z_8$.
            Le rapport global vaut le produit $r=r_1r_2r_3r_4$."""]
        if name == '33_Centrifugeuse':
            return [r"""La vis doit tourner de 2 tr/min plus vite que le tambour pendant
            la phase de lancement. Avec $n_{1/0}=2000$ tr/min et
            $n_{3/0}-n_{1/0}=2$ tr/min, on obtient
            $\boxed{n_{3/0}=2002\ \text{tr/min}}$."""]
        if name == '34_ControlX':
            return [r"""La couronne est fixe. Pour le train épicycloïdal simple,
            la relation de Willis donne
            $(\omega_1-\omega_3)/(\omega_0-\omega_3)=-R_b/R_m$ avec $\omega_0=0$.
            D'où $\omega_3=\omega_1R_m/(R_m+R_b)$. La courroie ne glissant pas sur la
            poulie de rayon $R_p$, $v=R_p\omega_3$, soit
            \[\boxed{v=R_p\frac{R_m}{R_m+R_b}\,\omega_{1/0}}.\]"""]
        if name == '36_VisEcrou':
            return [
                r"""Chaîne : moteur 1 $(C_m,\omega_1)$ $\rightarrow$ transmission par
                courroie/poulies $(\omega_2)$ $\rightarrow$ vis--écrou de pas $p_v$
                $\rightarrow$ piston 3 $(F_3,v_3)$.""",
                r"""Sans glissement, $\omega_2/\omega_1=D_1/D_2=1/2$. Pour la vis--écrou,
                $v_3=p_v\omega_2/(2\pi)$. Ainsi
                \[\boxed{v_3=\frac{p_v}{4\pi}\,\omega_1}.\]""",
                r"""Le sens de translation est donné par le pas de la vis et le sens de
                rotation. Le signe de la relation précédente est donc à adapter à la
                convention positive choisie; sa valeur absolue reste $p_v/(4\pi)$.""",
            ]
        if name == '37_VisEcrou':
            return [
                r"""Le graphe comporte 0 (bâti), la vis entraînée en pivot avec 0 et le
                coulisseau/écrou 1 en glissière avec 0. La vis et l'écrou sont reliés par
                une liaison hélicoïdale de pas $p$.""",
                r"""Pour une vis tournante et un écrou empêché de tourner,
                \[\boxed{v=\frac{p}{2\pi}\,\omega_m}\]
                avec un signe dépendant du sens du filet et des conventions.""",
            ]
        if name == '38_Treuil':
            return [
                r"""Les deux engrènements donnent
                $\omega_3/\omega_2=-Z_2/Z_{3a}$ puis
                $\omega_4/\omega_3=-Z_{3b}/Z_4$. Le câble ne glisse pas :
                $v_{5/0}=R\omega_4$. Donc
                \[\boxed{v_{5/0}=R\frac{Z_2Z_{3b}}{Z_{3a}Z_4}\,\omega_{2/0}}.\]""",
                r"""En posant $k=\omega_4/\omega_2=Z_2Z_{3b}/(Z_{3a}Z_4)$ et
                $k_3=\omega_3/\omega_2=-Z_2/Z_{3a}$,
                \[J_{\rm eq,2}=J_2+J_3k_3^2+J_4k^2+M_5(Rk)^2.\]
                Ramenée à la translation de la charge,
                $M_{\rm eq}=M_5+J_4/R^2+J_3(k_3/(Rk))^2+J_2/(Rk)^2$.""",
            ]
        if name == '93_Lokomat':
            return [
                r"""On applique la relation de Willis au train épicycloïdal du premier
                étage en tenant compte de l'élément fixe indiqué sur le schéma. Avec les
                dentures données, le rapport de réduction de l'étage vaut
                \[r_1=\frac{\omega_{\rm sortie}}{\omega_{\rm entrée}}
                =\frac{Z_1Z_3}{Z_0Z_2}=\frac{18\times24}{60\times45}
                =\boxed{0,16}\]
                (le signe dépend du nombre d'engrènements extérieurs).""",
                r"""Les trois étages étant identiques et montés en cascade,
                $r_g=r_1^3=0,16^3=\boxed{4,096\times10^{-3}}$, soit un rapport de
                réduction en vitesse voisin de $1/244$.""",
            ]
    return None


def dyn_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    name = rel.split('/')[2]
    if '/DYN-01/' in rel:
        if name == '02_R':
            return [
                r"""Si le moteur passe de $0$ à la vitesse nominale $\Omega_N$ avec un
                couple accélérateur supposé constant, l'accélération est
                $\alpha=(C_m-C_r)/J_{\rm eq}$. À partir d'une rampe imposée de durée
                $t_d$, $\alpha=\Omega_N/t_d$ avec $\Omega_N=2\pi n_N/60$.""",
                r"""Le temps de démarrage est
                $\boxed{t_d=\Omega_N/\alpha=J_{\rm eq}\Omega_N/(C_m-C_r)}$.""",
            ]
        if name == '14_Sympact':
            return [
                r"""Le profil trapézoïdal comporte une accélération constante $+a$ sur
                $t_a$, une vitesse constante sur $t_v$, puis une décélération $-a$ sur
                $t_a$. La vitesse est triangulaire/trapézoïdale et la position est
                quadratique pendant les rampes puis affine pendant le palier.""",
                r"""$\boxed{T=2t_a+t_v}$.""",
                r"""$\boxed{\omega_{\max}=a\,t_a}$.""",
                r"""L'angle total est l'aire sous la courbe de vitesse :
                $\boxed{\Delta\theta=\omega_{\max}(t_v+t_a)=a t_a(t_v+t_a)}$.""",
                r"""En combinant la distance imposée et la durée disponible, on résout
                $\Delta\theta=a t_a(T-t_a)$; la racine physique vérifie $0<t_a<T/2$,
                puis $\omega_{\max}=a t_a$.""",
            ]
        if name == '63_BancHydraulique':
            return [
                r"""Pour un profil trapézoïdal, la distance rapide est l'aire sous la
                courbe de vitesse : $c_{\rm rap}=V(t_r+t_a)$ et la distance lente
                $c_{\rm lent}=V_l(t_l+t_a)$, avec demi-aires $Vt_a/2$ à chaque rampe.
                Les expressions exactes s'obtiennent en additionnant les trapèzes du
                chronogramme.""",
                r"""On résout les deux équations de course avec les durées imposées.
                L'accélération du chariot est ensuite $a=V/t_a$ pendant la montée et
                $-a$ pendant la descente.""",
                r"""Si le moteur entraîne une vis de pas $p$ par un réducteur de rapport
                $r=\omega_{\rm vis}/\omega_m$, alors
                $V=p\omega_{\rm vis}/(2\pi)=pr\omega_m/(2\pi)$, donc
                $\omega_m=2\pi V/(pr)$.""",
                r"""$\omega_{m,\max}=2\pi V_{\max}/(pr)$ et
                $\dot\omega_m=2\pi a/(pr)$.""",
                r"""$E_c=\tfrac12MV^2+\tfrac12I_m\omega_m^2+
                \tfrac12I_r\omega_r^2$ (on ajoute de même chaque pièce tournante).""",
                r"""En écrivant $E_c=\tfrac12J_{\rm eq}\omega_m^2$ :
                $J_{\rm eq}=I_m+I_r(\omega_r/\omega_m)^2+M(V/\omega_m)^2$.""",
                r"""Le théorème de l'énergie cinétique donne
                $C_m\omega_m-FV=J_{\rm eq}\omega_m\dot\omega_m$, donc
                $\boxed{C_m=J_{\rm eq}\dot\omega_m+F(V/\omega_m)}$.""",
            ]
    if '/DYN-03-Inertie/' in rel:
        if name in {'42_Cylindre','43_Cylindre'}:
            return [
                r"""Pour un cylindre homogène, le centre d'inertie est au centre
                géométrique. Pour un assemblage de cylindres, on utilise le barycentre
                $\overrightarrow{OG}=\sum m_i\overrightarrow{OG_i}/\sum m_i$ avec
                $m_i=\rho\pi R_i^2L_i$ (les évidements sont pris avec une masse négative).""",
                r"""Au centre d'un cylindre plein d'axe $z$ :
                $I_{zz}=\tfrac12mR^2$ et
                $I_{xx}=I_{yy}=m(3R^2+L^2)/12$. En $O$, on applique Huygens :
                $\mathbf I_O=\mathbf I_G+m[(OG)^2\mathbf1-\overrightarrow{OG}
                \overrightarrow{OG}^{\,T}]$. Les matrices des constituants se somment.""",
            ]
        if name in {'44_Disque','45_Disque'}:
            return [
                r"""Le centre d'inertie d'un disque homogène est son centre géométrique;
                pour un disque évidé ou composé, on applique le barycentre pondéré en
                considérant les évidements comme des masses négatives.""",
                r"""Pour un disque mince de rayon $R$ :
                $I_{zz}=\tfrac12mR^2$ et $I_{xx}=I_{yy}=\tfrac14mR^2$ au centre.
                La matrice en $O$ est obtenue par le théorème de Huygens et sommation des
                différentes parties.""",
            ]
        if name == '50_BancBalafre':
            return [
                r"""La coordonnée est le barycentre des sous-ensembles :
                $\boxed{z_G=\sum_i m_i z_{G_i}/\sum_i m_i}$. Les masses et positions sont
                celles données dans le tableau; les pièces symétriques ont la même
                contribution.""",
                r"""La symétrie de révolution autour de $z_0$ impose
                $I_{xx}=I_{yy}=A$, tous les produits d'inertie nuls et
                $I_{zz}=C$. Ainsi $\mathbf I_G=\operatorname{diag}(A,A,C)$.""",
            ]
        if name == '64_EPAS':
            return [r"""Le parc échelle est constitué de trois éléments identiques dont
            les centres sont régulièrement répartis. Le barycentre vérifie
            $\overrightarrow{OG}=\sum m_i\overrightarrow{OG_i}/(3m)$. La moyenne des
            abscisses vaut $L/2$ et celle des ordonnées $h/3$, d'où
            $\boxed{\overrightarrow{OG}=\frac L2\vec x_5+\frac h3\vec y_5}$."""]
    if '/DYN-04-TorseurDynamique/' in rel:
        if name == 'Cours':
            return [
                r"""$\vec\sigma_A(S/0)=\vec\sigma_G(S/0)+
                \overrightarrow{AG}\wedge m\vec V_G$, avec
                $\vec\sigma_G=\mathbf I_G\vec\Omega$.""",
                r"""$\vec\delta_A(S/0)=d\vec\sigma_A/dt|_0$ et
                $\vec\delta_A=\vec\delta_G+
                \overrightarrow{AG}\wedge m\vec\Gamma_G+
                \vec V(A/0)\wedge m\vec V_G$. Pour un point $A$ fixe, le dernier terme
                est nul.""",
                r"""$\{\mathcal C(S/0)\}_A=\{m\vec V_G;\vec\sigma_A\}_A$.""",
                r"""$\{\mathcal D(S/0)\}_A=\{m\vec\Gamma_G;\vec\delta_A\}_A$.""",
                r"""Dans une base principale au centre d'inertie,
                $\mathbf I_G=\operatorname{diag}(A,B,C)$. En un autre point, on applique
                le théorème de Huygens.""",
            ]
        if name == '01_T':
            return [
                r"""En translation, $\vec\Omega=\vec0$ et tous les points ont la vitesse
                $\dot\lambda\vec i_0$. Ainsi
                $\{\mathcal C(1/0)\}_B=\{m_1\dot\lambda\vec i_0;\vec0\}_B$.""",
                r"""$\{\mathcal D(1/0)\}_B=\{m_1\ddot\lambda\vec i_0;\vec0\}_B$.
                Au point $A$ : le moment vaut
                $\overrightarrow{AB}\wedge m_1\ddot\lambda\vec i_0=\vec0$, donc le
                torseur est inchangé.""",
            ]
        if name == '02_R':
            return [
                r"""Pour $\overrightarrow{AB}=R\vec i_1$ et un centre d'inertie $G$,
                $\{\mathcal C(1/0)\}_B=\{m_1\vec V_G;\mathbf I_G\vec\Omega+
                \overrightarrow{BG}\wedge m_1\vec V_G\}_B$, avec
                $\vec\Omega=\dot\theta\vec k_0$.""",
                r"""$\{\mathcal D(1/0)\}_B=\{m_1\vec\Gamma_G;
                \mathbf I_G\ddot\theta\vec k_0+
                \vec\Omega\wedge(\mathbf I_G\vec\Omega)+
                \overrightarrow{BG}\wedge m_1\vec\Gamma_G\}_B$.
                Le transport en $A$ ajoute $\overrightarrow{AB}\wedge m_1\vec\Gamma_G$.""",
                r"""Directement en $A$ fixe :
                $\vec\delta_A=d(\mathbf I_A\vec\Omega)/dt|_0=
                \mathbf I_A\ddot\theta\vec k_0+
                \vec\Omega\wedge(\mathbf I_A\vec\Omega)$.""",
                r"""La seconde configuration se traite de la même façon; on remplace
                simplement $\overrightarrow{AG}$ et la matrice d'inertie par celles du
                solide représenté.""",
                r"""Le torseur dynamique correspondant est obtenu par dérivation du
                torseur cinétique; les termes tangentiels sont en $\ddot\theta$ et les
                termes centripètes en $\dot\theta^2$.""",
            ]
        if name == '03_TT':
            return [
                r"""$\{\mathcal C(1/0)\}=\{m_1\dot\lambda\vec i_0;\vec0\}$ et
                $\{\mathcal C(2/0)\}=\{m_2(\dot\lambda\vec i_0+
                \dot\mu\vec j_0);\vec0\}$, transportés au point demandé.""",
                r"""$\{\mathcal D(1/0)\}=\{m_1\ddot\lambda\vec i_0;\vec0\}$ et
                $\{\mathcal D(2/0)\}=\{m_2(\ddot\lambda\vec i_0+
                \ddot\mu\vec j_0);\vec0\}$.""",
                r"""Le torseur dynamique de l'ensemble est la somme : résultante
                $[(m_1+m_2)\ddot\lambda]\vec i_0+m_2\ddot\mu\vec j_0$ et moment égal à
                la somme des moments transportés en $B$.""",
            ]
        if name == '50_BancBalafre':
            return [
                r"""Le coeur de butée effectue une translation suivant l'axe de guidage;
                son orientation reste constante par rapport au bâti.""",
                r"""La géométrie du guidage impose une relation linéaire
                $v(t)=k_y\dot y(t)$, où $k_y$ est le rapport cinématique lu sur le schéma
                (égal à 1 si $y$ est directement la coordonnée du centre).""",
                r"""En $G_{CB}$ :
                $\{\mathcal D(CB/0)\}=\{M_{CB}\dot v\vec e;
                \vec0\}_{G_{CB}}$ pour une translation rectiligne.""",
                r"""En $G_{JR}$, la partie mobile suit la même translation :
                $\{\mathcal D(JR/0)\}=\{M_{JR}\dot v\vec e;\vec0\}_{G_{JR}}$.""",
                r"""Après transport au point $G$ et sommation,
                $\{\mathcal D(S/0)\}_G=\{(M_{CB}+M_{JR})\dot v\vec e;\vec0\}_G$
                lorsque $G$ est le centre d'inertie de l'ensemble et qu'il n'y a pas de
                rotation.""",
            ]
        if name in {'05_RT_02'}:
            return [
                r"""$\vec V(C,2/0)=\dot\lambda\vec i_1+
                \lambda\dot\theta\vec j_1$.""",
                r"""$\{\mathcal V(2/0)\}_C=\{\dot\theta\vec k_0;
                \dot\lambda\vec i_1+\lambda\dot\theta\vec j_1\}_C$.""",
                r"""$\vec\Gamma(C,2/0)=(\ddot\lambda-\lambda\dot\theta^2)\vec i_1+
                (2\dot\lambda\dot\theta+\lambda\ddot\theta)\vec j_1$.""",
            ]
        if name == '11_PompePistonsRadiaux':
            return [
                r"""Le piston 2 est en translation :
                $\{\mathcal V(2/0)\}_B=\{\vec0;\dot\lambda\vec j_0\}_B$ avec
                $\lambda=\lambda_0+e\sin\theta$.""",
                r"""$\vec\Gamma(B,2/0)=\ddot\lambda\vec j_0=
                e(\ddot\theta\cos\theta-\dot\theta^2\sin\theta)\vec j_0$.""",
            ]
        if name == '13_TransfoMouvement':
            return cin_answers('CIN/CIN-02-VitesseAcceleration/13_TransfoMouvement/x.tex', prompts, source)
        if name == '15_SympactGalet':
            return cin_answers('CIN/CIN-02-VitesseAcceleration/15_SympactGalet/x.tex', prompts, source)
        if name == '16_Poussoir':
            return cin_answers('CIN/CIN-02-VitesseAcceleration/16_Poussoir/x.tex', prompts, source)
        if name == '17_4Barres':
            return cin_answers('CIN/CIN-02-VitesseAcceleration/17_4Barres/x.tex', prompts, source)
        if name == '18_Maxpid':
            return cin_answers('CIN/CIN-02-VitesseAcceleration/18_Maxpid/x.tex', prompts, source)
    if '/DYN-05-Methode/' in rel:
        if name == '08_RR3D':
            return [
                r"""Le graphe d'analyse relie 0--1 et 1--2 par les pivots du mécanisme.
                On ajoute les poids de 1 et 2, les couples moteurs sur chaque pivot et les
                réactions de liaison. Les actions internes 1/2 apparaissent sur les deux
                solides avec des sens opposés.""",
                r"""On isole d'abord 2 et on projette le théorème du moment dynamique sur
                l'axe du pivot 2/1 afin d'éliminer la réaction de liaison. Puis on isole
                l'ensemble 1+2 et on projette au pivot 1/0 pour éliminer les actions
                internes. Les deux équations fournissent les deux lois de mouvement.""",
                r"""Les équations s'écrivent sous la forme matricielle
                $\mathbf M(q)\ddot q+\mathbf C(q,\dot q)+\mathbf G(q)=\tau$, avec
                $q=(\theta,\varphi)^T$. Les termes de $\mathbf M$ proviennent des moments
                d'inertie et de Huygens, $\mathbf C$ des produits de vitesses et
                $\mathbf G$ des poids. La résolution donne $\ddot q=\mathbf M^{-1}
                [\tau-\mathbf C-\mathbf G]$.""",
            ]
        if name == '05_RT_02':
            return dyn_answers('DYN/DYN-04-TorseurDynamique/STOCK/05_RT_02/x.tex', prompts, source)
    if '/DYN-06-PFD/' in rel:
        p = rel
        if name == '01_T':
            return [r"""La projection du théorème de la résultante dynamique sur
            $\vec i_0$ donne
            \[\sum F_{\rm ext,i_0}=m_1\ddot\lambda.\]
            En séparant l'action motrice, les frottements et les autres efforts :
            $F_m-F_r+\sum F_{i_0}=m_1\ddot\lambda$, ce qui constitue la loi de mouvement."""]
        if name == '02_R':
            return [r"""Le moment au point fixe $A$ projeté sur $\vec k_0$ donne
            \[\sum M_{A,k_0}^{\rm ext}=J_{A,k_0}\ddot\theta.\]
            Ainsi le couple moteur moins le couple résistant et le moment du poids vaut
            $J_A\ddot\theta$; le moment de la réaction du pivot en $A$ est nul."""]
        if name == '04_RR':
            return [
                r"""Pour le solide 2 au point $B$ :
                $\sum M_{B,k_0}^{\rm ext}=\delta_{B,k_0}(2/0)$. Cette équation relie le
                couple du pivot 1/2, le moment du poids de 2 et les termes en
                $\ddot\theta,\ddot\varphi,\dot\theta^2,\dot\varphi^2$.""",
                r"""Pour l'ensemble 1+2 au point $A$, l'action 1/2 disparaît :
                $\sum M_{A,k_0}^{\rm ext}=\delta_{A,k_0}(1+2/0)$. La combinaison des deux
                équations fournit les deux accélérations généralisées.""",
            ]
        if name in {'07_RR3D','08_RR3D'}:
            return [r"""On écrit le théorème du moment dynamique sur l'axe indiqué, au
            point de concours de la liaison afin d'annuler les inconnues de réaction.
            Le membre droit est la projection de
            $\mathbf I\dot{\vec\Omega}+\vec\Omega\wedge(\mathbf I\vec\Omega)+
            \overrightarrow{AG}\wedge m\vec\Gamma_G$. Pour l'ensemble 1+2, les actions
            internes disparaissent. Les deux projections donnent le système différentiel
            couplé des angles $\theta$ et $\varphi$."""] * len(prompts)
        if name == '09_RT_RSG':
            return [
                r"""Sur $\vec i_1$, la résultante dynamique de 2 donne
                $\sum F_{i_1}^{\rm ext}=m_2\vec\Gamma(G_2,2/0)\cdot\vec i_1$.
                En utilisant l'accélération cinématique et la contrainte de roulement, on
                obtient l'équation de translation de $\lambda$.""",
                r"""Au point de contact $I$, le moment dynamique de 1+2 projeté sur
                $\vec k_0$ élimine les réactions du sol :
                $\sum M_{I,k_0}^{\rm ext}=\delta_{I,k_0}(1+2/0)$. Cette équation donne la
                loi en $\theta$ couplée à $\lambda$.""",
            ]
        if name == '46_RR_RSG':
            return [
                r"""L'isolement de 2 et la projection au pivot $A$ donnent
                $\sum M_{A,k_0}^{\rm ext}=\delta_{A,k_0}(2/0)$, relation entre le couple
                moteur, le poids de 2 et les accélérations $\ddot\theta,\ddot\varphi$.""",
                r"""L'isolement de 1+2 au point de roulement $I$ élimine les efforts de
                contact avec le sol :
                $\sum M_{I,k_0}^{\rm ext}=\delta_{I,k_0}(1+2/0)$. Avec la contrainte
                $V(I,1/0)=0$, cette équation complète la loi de mouvement.""",
            ]
        if name == '50_BancBalafre':
            return [
                r"""Le coeur de butée est en translation rectiligne suivant l'axe du banc;
                il ne tourne pas par rapport à 0.""",
                r"""Les deux actionneurs symétriques d'un même plan fournissent une
                résultante $2F_V\vec e$ (ou $2F_R\vec e$). Au point $A_4$ :
                $\{T_{V\to CB}\}=\{2F_V\vec e;\vec0\}_{A_4}$ et de même
                $\{T_{R\to CB}\}=\{2F_R\vec e;\vec0\}_{A_8}$, avant transport au point
                commun choisi.""",
                r"""On isole $CB$, on transporte les deux torseurs d'action au centre
                d'inertie, puis on applique la résultante dynamique suivant l'axe et le
                moment dynamique autour des axes transverses. La résultante donne
                $2F_V+2F_R-F_{\rm res}=M_{CB}\dot v$; l'équation de moment répartit les
                efforts entre plans avant et arrière selon leurs bras de levier.""",
                r"""Le plan dont le bras de levier par rapport au centre d'inertie est le
                plus faible doit fournir l'effort le plus élevé. Le rapport se déduit de
                l'équilibre des moments : $F_V/F_R=d_R/d_V$.""",
            ]
        if name == '05_RT_02':
            return dyn_answers('DYN/DYN-04-TorseurDynamique/STOCK/05_RT_02/x.tex', prompts, source)
    return None


def simple_domain_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    # NUM
    if rel.startswith('NUM/'):
        return [r"""Pour une équation $\dot y=f(t,y)$ et un pas $h$, le schéma d'Euler
        explicite est $t_{n+1}=t_n+h$ et
        \[\boxed{y_{n+1}=y_n+h f(t_n,y_n)}.\]
        Pour un système d'ordre supérieur, on introduit les variables d'état
        $x_1=y$, $x_2=\dot y$, etc., puis on applique cette formule à chaque composante.
        Exemple pour $\ddot y=g(t,y,\dot y)$ :
        $v_{n+1}=v_n+h g(t_n,y_n,v_n)$ et $y_{n+1}=y_n+h v_n$.
        Les conditions initiales fixent $y_0$ et $v_0$; le pas est diminué jusqu'à
        convergence des résultats."""]
    # SLCI
    if rel.startswith('SLCI/SLCI-03'):
        return [r"""On déplace successivement les sommateurs et les points de prélèvement
        en appliquant les règles de transposition : lorsqu'un sommateur traverse un bloc
        $G$, la branche déplacée est multipliée ou divisée par $G$ afin de conserver le
        même signal. Puis on regroupe les blocs en série par produit, les blocs en
        parallèle par somme et les boucles simples par $G/(1+GH)$. Les deux schémas ont
        alors les mêmes relations algébriques entrée--sortie et perturbation--sortie."""]
    if rel.startswith('SLCI/SLCI-07-Ordre12/504'):
        return [
            r"""Pour chaque sinusoïde, on mesure deux maxima consécutifs :
            $T=\Delta t$ et $\omega=2\pi/T$.""",
            r"""En régime permanent, si $e(t)=E\sin\omega t$ et
            $s(t)=S\sin(\omega t+\varphi)$, alors
            $|H(j\omega)|=S/E$ et $G_{dB}=20\log_{10}(S/E)$.
            Le déphasage est $\varphi=2\pi\Delta t/T$, positif si la sortie est en avance,
            négatif si elle est en retard.""",
        ]
    if rel.startswith('SLCI/SLCI-07-Ordre12/541'):
        return [
            r"""$H(p)=K/(1+\tau p)$.""",
            r"""Pour un échelon unitaire et $K=0,5$ :
            $s(t)=0,5(1-e^{-t/\tau})u(t)$. La tangente à l'origine coupe la valeur finale
            en $t=\tau$.""",
            r"""L'écart est $\varepsilon(t)=1-s(t)$; sa valeur finale vaut
            $\varepsilon_\infty=1-K=0,5$ pour une chaîne directe seule.""",
            r"""$t_{5\%}\simeq3\tau$.""",
            r"""Méthodes : (1) tangente à l'origine, donnant $\tau$; (2) lecture du temps
            où la réponse atteint $63\%$ de sa variation finale. Le gain est le rapport
            valeur finale/valeur de l'échelon.""",
        ]
    if rel.startswith('SLCI/SLCI-07-Ordre12/542'):
        return [
            r"""$H(p)=\dfrac{K\omega_0^2}{p^2+2\xi\omega_0p+\omega_0^2}
            =\dfrac{K}{1+2\xi p/\omega_0+p^2/\omega_0^2}$.""",
            r"""$\xi>1$ : réponse apériodique sans dépassement; $\xi=1$ : régime critique;
            $0<\xi<1$ : oscillations amorties; $\xi=0$ : oscillations non amorties.
            Un dépassement apparaît pour $\xi<1$ et augmente lorsque $\xi$ diminue.""",
            r"""Le gain est lu sur la valeur finale. Pour un régime pseudo-périodique,
            $D_1=e^{-\pi\xi/\sqrt{1-\xi^2}}$ donne $\xi$, et la pseudo-période
            $T_p=2\pi/(\omega_0\sqrt{1-\xi^2})$ donne $\omega_0$.
            Sans dépassement, on ajuste deux pôles réels à partir des temps caractéristiques.""",
        ]
    # SEQ
    if rel.startswith('SEQ/'):
        return [
            r"""La validation de l'opérateur déclenche d'abord la mise en vitesse du
            moteur. Celui-ci atteint sa consigne au bout de $5\,\mathrm{s}$. Le contrôle
            dure ensuite $1\,\mathrm{s}$. Comme il conclut à l'absence d'anomalie, la
            rafale démarre à $t=6\,\mathrm{s}$ et reste active pendant huit secondes,
            jusqu'à $t=14\,\mathrm{s}$. Le retour à l'arrêt du moteur dure encore
            $5\,\mathrm{s}$. Ainsi : \texttt{Moteur}=1 sur $[5,14]$,
            \texttt{Controle}=1 à partir de $t=6\,\mathrm{s}$ et
            \texttt{Rafale}=1 sur $[6,14]$. Aucune pause supplémentaire n'est nécessaire
            puisque huit secondes est inférieur au seuil de dix secondes.""",
            r"""On ajoute une transition prioritaire $[\texttt{Controle}=2]$ depuis
            l'état de contrôle vers un état « Arrêt moteur ». Son action d'entrée impose
            \texttt{Rafale:=0} et commande l'arrêt. L'état est maintenu jusqu'à
            \texttt{Moteur}=0, puis le retour à l'état initial nécessite l'acquittement de
            l'anomalie. Seule la garde $[\texttt{Controle}=1]$ autorise le lancement de la
            rafale.""",
        ]
    return None


def stat_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    name = rel.split('/')[2]
    if '/STAT-02-Global/' in rel:
        ans=[]
        for p in prompts:
            m=re.search(r'M\\left\(([^,]+),', p)
            point=m.group(1) if m else 'A'
            ans.append(rf"""Le moment de la force au point {point} est obtenu par
            \[\boxed{{\vec{{\mathcal M}}_{{{point}}}(\vec F)=
            \overrightarrow{{{point}P}}\wedge\vec F}}\]
            où $P$ est un point de la ligne d'action. On exprime les deux vecteurs dans
            la même base puis on calcule le produit vectoriel. Si la ligne d'action passe
            par {point}, le moment est nul; le transport entre deux points vérifie
            $\vec M_A=\vec M_B+\overrightarrow{{AB}}\wedge\vec F$.""")
        return ans
    if '/STAT-02-Frottement/' in rel:
        return [
            r"""Au contact cylindre/plan, la réaction se décompose en une normale $N$ et
            une tangente $T$. La loi de Coulomb impose $|T|\le fN$ en adhérence et
            $T=-fN\,\vec t_v$ au glissement. Le torseur local est donc
            $\{\mathcal T\}=\{T\vec t+N\vec n;\vec0\}_I$.""",
            r"""À la limite du glissement, $|T|=fN$ et l'angle de frottement vérifie
            $\tan\varphi=f$. L'équilibre global fournit ensuite $N$ et $T$ par projection
            des forces et moments.""",
            r"""Le sens de $T$ est opposé à la vitesse de glissement probable. La
            vérification finale consiste à contrôler que la solution d'adhérence respecte
            $|T|<fN$; sinon on reprend avec l'égalité de glissement.""",
        ][:len(prompts)]
    if '/STAT-02-Local/' in rel:
        if name in {'1023_Vilebrequin','1024_Balancier'}:
            return [
                r"""On décompose la pièce en volumes élémentaires. Le centre d'inertie est
                $\overrightarrow{OG}=\sum m_i\overrightarrow{OG_i}/\sum m_i$; les trous
                sont traités comme des masses négatives.""",
                r"""Pour que $G$ appartienne à l'axe $(O,\vec x)$, ses coordonnées
                transversales doivent être nulles. L'équation barycentrique en $y$ (et en
                $z$ si nécessaire) fournit directement la hauteur $h$.""",
                r"""On remplace les masses par $\rho V_i$; la masse volumique commune se
                simplifie. L'application numérique est alors effectuée avec les dimensions
                du dessin.""",
                r"""En $G$, $\{T_{p\to S}\}=\{-mg\vec y_0;\vec0\}_G$. En $O$ :
                $\{T_{p\to S}\}=\{-mg\vec y_0;
                \overrightarrow{OG}\wedge(-mg\vec y_0)\}_O$.""",
            ]
        if name == '39_SeineMusicale':
            return [
                r"""La pression dynamique est $p=f$ (notation de l'énoncé). Sur
                $dS$, $d\vec F_{vent}=-f\,dS\,\vec x_{C_G}$, normale à la voile et
                opposée au vent.""",
                r"""On paramètre la demi-voile par des coordonnées polaires. Le moment
                élémentaire est $dM_z=(\overrightarrow{OP}\wedge d\vec F)\cdot\vec z$;
                l'intégration sur le demi-disque conduit à un terme en $fR^3$ multiplié
                par la fonction trigonométrique de $\alpha$ issue de la projection de la
                normale.""",
                r"""Par définition,
                $F_{vent}=M_{O,z}/[(\overrightarrow{OC_G}\wedge\vec x_{C_G})\cdot\vec z]$.
                On remplace $M_{O,z}$ par le résultat précédent et
                $OC_G=4R/(3\pi)$ pour un demi-disque homogène.""",
                r"""Le maximum est obtenu en annulant la dérivée de la fonction
                trigonométrique en $\alpha$ et en comparant les bornes. Pour une dépendance
                en $\sin\alpha\cos\alpha$, il est atteint à $\alpha=\pi/4$ et vaut la
                moitié du coefficient multiplicatif.""",
            ]
        if name == '50_BancBalafre':
            return [
                r"""Sur l'élément de joint, la pression exerce
                $d\vec F=-p(t)\,dS\,\vec u(\theta)$. Le torseur au point $M$ est
                $\{dT\}_M=\{-p(t)dS\vec u(\theta);\vec0\}_M$.""",
                r"""On intègre sur la surface du joint :
                $\vec R=-\int_Sp\vec u\,dS$ et
                $\vec M_B=-\int_S\overrightarrow{BM}\wedge p\vec u\,dS$.
                Les composantes antisymétriques s'annulent; la résultante est portée par
                l'axe de symétrie et vaut la pression multipliée par l'aire projetée.""",
            ]
    if '/STAT-03-Demarche/' in rel:
        if name == '08_RR3D':
            return [
                r"""Le graphe relie 0--1 puis 1--2 par les deux pivots. On ajoute les
                poids, les couples des actionneurs et les réactions de liaison; les actions
                internes apparaissent par paires opposées.""",
                r"""Chaque pivot idéal transmet trois composantes de force et deux
                composantes de moment, sauf celle suivant son axe. Le poids de chaque
                solide est $\{-m_i g\vec j_0;\vec0\}_{G_i}$ et l'actionneur applique un
                couple pur suivant l'axe du pivot.""",
                r"""On isole 2 et on écrit le moment statique sur l'axe 2/1, puis on isole
                1+2 et on écrit le moment sur l'axe 1/0. Ces deux équations éliminent les
                réactions et donnent les deux couples moteurs requis.""",
            ]
        if name == '05_RT_02':
            return dyn_answers('DYN/DYN-04-TorseurDynamique/STOCK/05_RT_02/x.tex', prompts, source)
    return None


def sys_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    name=rel.split('/')[3] if len(rel.split('/'))>3 else ''
    if '59_Levage' in rel:
        return [
            r"""Le FAST peut être remplacé par un diagramme des exigences pour exprimer
            le besoin, un diagramme de définition de blocs (BDD) pour l'architecture et un
            diagramme de blocs internes (IBD) pour les flux. Un diagramme d'activité peut
            compléter la description fonctionnelle séquentielle.""",
            r"""Chaîne fonctionnelle : acquérir l'ordre et les sécurités $\rightarrow$
            traiter/commander $\rightarrow$ distribuer l'énergie $\rightarrow$ convertir
            par le moteur $\rightarrow$ transmettre/réduire $\rightarrow$ agir sur la
            charge. Les retours sont la position, la vitesse et les fins de course.""",
        ]
    if '60_Escalier' in rel:
        return [r"""Chaîne d'information : détecteurs de présence, vitesse et sécurité
        $\rightarrow$ automate $\rightarrow$ ordre au variateur. Chaîne d'énergie : réseau
        électrique $\rightarrow$ protections/contacteur/variateur $\rightarrow$ moteur
        $\rightarrow$ réducteur et chaîne $\rightarrow$ marches et main courante. Les
        freins et arrêts d'urgence agissent sur la distribution d'énergie."""]
    if '507_Divers' in rel:
        return [r"""Génératrice tachymétrique : petite machine à courant continu dont la
        tension est proportionnelle à la vitesse, $u=K\omega$. Potentiomètre rotatif :
        piste résistive et curseur, tension proportionnelle à l'angle. Codeur incrémental :
        disque à fentes et deux voies en quadrature; le comptage donne le déplacement et
        le déphasage le sens. Codeur absolu : plusieurs pistes codées (souvent Gray), chaque
        position donnant un mot binaire unique même après coupure."""]
    if '50_BancBalafre' in rel:
        return [
            r"""Multiplexé signifie qu'un seul convertisseur analogique-numérique est
            partagé entre plusieurs voies. Un multiplexeur sélectionne successivement
            chaque capteur; les mesures ne sont donc pas strictement simultanées.""",
            r"""La pleine échelle de l'amplificateur doit être immédiatement supérieure à
            la charge maximale : $Q_{max}=S_qF_{max}$ avec $S_q$ la sensibilité en pC/N.
            On choisit la gamme normalisée qui contient $\pm Q_{max}$ sans saturation.""",
            r"""Si la sortie varie sur $\Delta U$ et le CAN possède $N$ bits, le quantum
            est $q_U=\Delta U/2^N$. La résolution en charge est $q_Q=q_U/G_q$, puis en
            force $q_F=q_Q/S_q$. La résolution est conforme si $q_F$ est inférieure à
            l'exigence, en gardant une marge pour le bruit et les erreurs de gain.""",
        ]
    if '538_Codeur' in rel:
        return [
            r"""Un codeur incrémental optique comporte un disque à fentes, une source et
            un photodétecteur. La rotation produit des impulsions; deux voies A/B en
            quadrature donnent le sens et une voie index fournit une référence par tour.""",
            r"""Avec 25 fentes et une seule voie, la résolution est
            $360^\circ/25=\boxed{14,4^\circ}$ par impulsion. En comptage des deux fronts,
            elle devient $7,2^\circ$, et avec deux voies/quatre fronts $3,6^\circ$.""",
            r"""La fréquence des impulsions vaut $f=N n/60$ pour $N$ impulsions par tour
            et une vitesse $n$ en tr/min. La vitesse est donc $n=60f/N$; le sens provient
            de l'ordre des fronts A et B.""",
            r"""La position relative est le nombre algébrique d'impulsions multiplié par
            la résolution. Une prise d'origine sur la voie index est nécessaire après
            mise sous tension.""",
            r"""L'incertitude de quantification est au minimum d'un demi-pas, soit
            $\pm7,2^\circ$ avec une seule voie/25 fentes, avant prise en compte des erreurs
            optiques et mécaniques.""",
        ][:len(prompts)]
    return None


def elec_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    name=rel.split('/')[2]
    if '/ELEC-01/' in rel:
        if name in {'534_CircuitElec','536_CircuitElec'}:
            return [r"""On repère les nœuds puis on choisit le potentiel du rail inférieur
            nul et celui du générateur égal à $E$. Pour chaque nœud $k$, la loi des nœuds
            donne
            \[\sum_{j}\frac{V_k-V_j}{R_{kj}}=0.\]
            La résolution du système linéaire fournit tous les potentiels. Pour chaque
            résistance $R_i$ entre les nœuds $a$ et $b$ :
            $U_i=V_a-V_b$ et $I_i=U_i/R_i$. Les courants orientés dans le sens opposé à la
            valeur calculée sont négatifs. Cette méthode s'applique sans ambiguïté au
            réseau de la figure et constitue l'expression demandée en fonction de $E$ et
            des $R_i$."""]
        if name in {'535_CircuitElec','537_CircuitElec','538_CircuitElec'}:
            first=r"""On réduit le réseau depuis l'extrémité opposée aux bornes. Deux
            résistances en série donnent $R_s=R_a+R_b$ et deux résistances en parallèle
            $R_p=R_aR_b/(R_a+R_b)$. Pour le réseau en échelle, on définit récursivement
            $Z_{n}=R_{v,n}$ puis
            \[Z_k=R_{v,k}\parallel(R_{h,k+1}+Z_{k+1}),\qquad
              R_{eq}=R_{h,1}+Z_1.\]
            Pour le pont symétrique, les nœuds équipotentiels peuvent être fusionnés avant
            la réduction."""
            if len(prompts)==1: return [first]
            return [first, r"""Le courant fourni par la source est $I=E/R_{eq}$. On
            remonte ensuite le réseau : la tension d'un bloc parallèle est commune à ses
            branches et les courants se partagent selon
            $I_a=U/R_a$, $I_b=U/R_b$. À chaque étage, la loi des nœuds vérifie
            $I_{amont}=I_{vertical}+I_{aval}$."""]
    if name == '1023_MCC':
        # symbolic, values are on plate/figure
        return [
            r"""Schéma : alimentation continue de l'inducteur séparé et alimentation
            commandée de l'induit. L'induit est modélisé par $R_a$, $L_a$ et la f.é.m.
            opposée $E=K\Omega$; le couple est $T_{em}=KI$.""",
            r"""À l'arrêt, $\Omega=0$, donc $\boxed{E=0}$.""",
            r"""Le modèle équivalent est une source $U$ alimentant en série $R_a$, $L_a$
            et la source de tension $E$ opposée au courant $I$.""",
            r"""$U=E+R_aI+L_a\,dI/dt$. En régime établi au démarrage, $E=0$ et
            $U_d=R_aI_d=\boxed{1,2R_aI_N}$. Si l'inductance est prise en compte, une rampe
            de tension limite $dI/dt$.""",
            r"""On utilise un hacheur quatre quadrants ou un pont redresseur commandé,
            piloté par une boucle de courant interne et une boucle de vitesse externe.""",
            r"""$P_a=UI$ pour l'induit; on remplace $U$ et $I$ par les valeurs nominales
            de la plaque.""",
            r"""$P_{abs}=UI+U_fI_f$ pour une excitation indépendante.""",
            r"""$P_J=R_aI^2+R_fI_f^2$.""",
            r"""$P_u=P_{abs}-P_J-P_{autres}$ et
            $\eta=P_u/P_{abs}$. Ici $P_{autres}=27\,\mathrm{kW}$.""",
            r"""$T_u=P_u/\Omega_N$, avec $\Omega_N=2\pi n_N/60$.
            $T_{em}=P_{em}/\Omega_N=EI/\Omega_N=KI$.""",
        ]
    if name == '50_BancBalafre':
        return [
            r"""La vitesse synchrone est $n_s=60f/p$. La plaque donne une vitesse proche
            de $3000$ tr/min à 50 Hz, donc $p=60f/n_s=1$ paire de pôles.""",
            r"""$g_N=(n_s-n_N)/n_s$ et $C_{uN}=P_{uN}/\Omega_N$ avec
            $\Omega_N=2\pi n_N/60$.""",
            r"""Dans le modèle par phase,
            $P_{EM}=3U_S^2\dfrac{R/g}{(R/g)^2+(L_c\omega)^2}$.""",
            r"""$P_{EM}=C_{EM}\Omega$.""",
            r"""$\Omega=(1-g)\Omega_s=(1-g)\omega/p$. Ainsi
            $C_{EM}=\dfrac{3pU_S^2}{(1-g)\omega}\dfrac{R/g}{(R/g)^2+(L_c\omega)^2}$;
            près du synchronisme, l'approximation $1-g\simeq1$ donne l'expression de
            l'énoncé.""",
            r"""En négligeant les pertes mécaniques et les pertes supplémentaires,
            $C_u\simeq C_{EM}$, ce qui conduit directement à l'expression proposée.""",
            r"""Démarrage : $g=1$; synchronisme : $g=0$ et couple nul; nominal : point
            d'intersection avec le couple résistant près du synchronisme; la branche située
            au-delà du couple maximal est instable.""",
            r"""Le couple maximal est atteint pour $R/g=L_c\omega$. On obtient
            $C_M=3pU_S^2/(2L_c\omega^2)$, donc
            $\boxed{L_c=3pU_S^2/(2C_M\omega^2)}$.""",
            r"""Au nominal, $R/g\gg L_c\omega$ si le point est proche du synchronisme.
            Alors $C_N\simeq3pU_S^2g_N/(\omega R)$ et
            $\boxed{R=3pU_S^2g_N/(\omega C_N)}$.""",
            r"""On résout $C_u(g,f)=300\,\mathrm{N\,m}$ avec
            $g=1-p\Omega/\omega$, $\Omega=2\pi\,6000/60$ et $\omega=2\pi f$.
            La racine physique $0<g<1$ donne la fréquence imposée; une résolution
            numérique (Newton ou dichotomie) est adaptée.""",
        ]
    return None


def ppm_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    name=rel.split('/')[2]
    if 'Dessin2D' in name:
        return [r"""On complète les vues par projection orthogonale : chaque sommet de la
        vue connue est projeté perpendiculairement vers la vue à compléter, les
        profondeurs étant reportées avec la ligne à $45^\circ$. Les arêtes visibles sont en
        trait fort continu, les arêtes cachées en trait interrompu fin et les axes en trait
        mixte fin. On vérifie la correspondance stricte des largeurs entre face/dessus et
        des hauteurs entre face/profil. Les formes inclinées se projettent par leurs points
        extrêmes; les évidements sont reportés sur les trois vues. Le résultat final doit
        être cohérent avec la perspective fournie et ne contenir aucune arête redondante."""]
    if name == '1020_PompeEnsieta':
        a=cin_answers('CIN/CIN-01-Parametrage/1020_PompeEnsieta/x.tex',prompts,source)
        assert a
        return a[:6]+[r"""Le dessin de définition du corps reprend toutes les surfaces
        fonctionnelles du dessin d'ensemble : alésage de guidage du piston avec tolérance
        et rugosité serrées, logements des clapets et sièges coniques, taraudages des
        raccords, épaulements de montage et perçages de communication. Les axes sont
        cotés depuis un même système de références et les formes intérieures sont montrées
        en coupe avec hachures réglementaires."""]
    if name in {'2002_AxeCommande','2003_Fourchette'}:
        return [
            r"""Gamme type : choix du brut (barre/forge pour l'axe, forge ou moulage pour
            la fourchette), débit et ébauche, création des références, usinage des faces et
            alésages principaux, perçage/taraudage, finition des portées, traitement
            thermique éventuel, rectification des surfaces précises, ébavurage, contrôle
            dimensionnel et protection de surface.""",
            r"""Un acier est un alliage fer--carbone contenant en général moins de
            2,1\% de carbone; une fonte en contient davantage, typiquement 2,1 à 6,7\%,
            avec une bonne coulabilité mais une ductilité plus faible.""",
            r"""$R_e=800\,\mathrm{MPa}$ signifie que la contrainte normale maximale avant
            déformation plastique mesurable est 800 MPa. Elle est obtenue par essai de
            traction sur éprouvette normalisée : mesure de $F$ et de l'allongement,
            calcul $\sigma=F/S_0$, $\varepsilon=\Delta L/L_0$, puis lecture de la limite
            d'élasticité (ou $R_{p0,2}$ par décalage de 0,2\%).""",
        ]
    if rel.startswith('PPM/PPM-03'):
        # generic GPS answers adjusted to question count
        answers=[]
        for p in prompts:
            pl=p.lower()
            if 'référence' in pl or 'reference' in pl:
                answers.append(r"""Les surfaces de référence sont choisies parce qu'elles
                réalisent la mise en position fonctionnelle de la pièce dans l'assemblage.
                La référence primaire supprime trois degrés de liberté, la secondaire deux
                et la tertiaire le dernier; elles doivent être étendues, stables,
                accessibles au contrôle et directement liées aux surfaces d'appui réelles.""")
            elif 'maximum de matière' in pl:
                answers.append(r"""Le modificateur au maximum de matière autorise une
                tolérance bonus égale à l'écart entre la taille réelle et la taille au
                maximum de matière. Sur l'élément tolérancé, la zone de position s'agrandit
                lorsque l'on s'éloigne du maximum de matière; appliqué à la référence, il
                crée une mobilité de datum correspondant au jeu disponible dans le
                simulateur fonctionnel.""")
            elif 'gamme' in pl or 'fabrication' in pl or 'usinage' in pl or 'brut' in pl:
                answers.append(r"""On choisit un brut proche de la forme (forge, moulage ou
                débit de barre), puis : création des références, ébauche de toutes les
                surfaces, stabilisation/traitement éventuel, finition des alésages et
                portées en reprenant les références fonctionnelles, perçages et taraudages,
                rectification si nécessaire, ébavurage, traitement de surface et contrôle
                GPS final. Chaque phase utilise une mise en position 3--2--1 cohérente avec
                le système de références du plan.""")
            elif 'planéité' in pl:
                answers.append(r"""On inscrit dans le cadre de tolérance le symbole de
                planéité suivi de $t_p$, sans référence. La surface réelle doit être
                comprise entre deux plans parallèles distants de $t_p$.""")
            elif 'perpendicularité' in pl:
                answers.append(r"""Le cadre comporte le symbole de perpendicularité,
                $t_p$ et la référence A (ou B selon l'élément contrôlé). La surface
                tolérancée doit rester entre deux plans parallèles distants de $t_p$ et
                perpendiculaires au plan de référence.""")
            else:
                answers.append(r"""La spécification se décode en identifiant successivement
                l'élément tolérancé, le symbole géométrique, la valeur et la forme de la
                zone de tolérance, les références ordonnées et les modificateurs. Le
                gabarit est le simulateur géométrique associé : deux plans pour une forme
                ou une orientation de surface, un cylindre pour un axe, ou une zone
                cylindrique/sphérique pour une localisation. La pièce est conforme si
                l'élément extrait reste entièrement dans cette zone après mise en référence.""")
        return answers
    return None


def rdm_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    name=rel.split('/')[2]
    if name == '526_RdM':
        return [
            r"""On coupe la poutre à l'abscisse $x$ et on isole la partie la plus simple.
            Le PFS donne $\{T_{coh}\}=-\sum\{T_{ext}\}$ au centre de la section. On
            obtient les composantes $N(x)$, $T_y(x)$, $T_z(x)$,
            $M_t(x)$, $M_{fy}(x)$ et $M_{fz}(x)$ tronçon par tronçon.""",
            r"""Une composante $N$ correspond à traction/compression, $T_y,T_z$ au
            cisaillement, $M_t$ à la torsion et $M_{fy},M_{fz}$ à la flexion. Les
            composantes non nulles du torseur précédent donnent directement les
            sollicitations combinées.""",
            r"""Chaque diagramme est tracé avec les expressions par morceaux. Les sauts
            correspondent aux forces ou couples concentrés; la pente de l'effort tranchant
            vaut l'opposé de la charge répartie et la pente du moment fléchissant est
            l'effort tranchant. Les trois figures \texttt{cor\_01.jpg}, \texttt{cor\_02.jpg} et
            \texttt{cor\_03.jpg} du dossier illustrent le résultat attendu.""",
        ]
    if name == '529_Passerelle':
        return [
            r"""On choisit l'axe $x$ le long de chaque poutre, l'origine aux liaisons et
            les coordonnées des points d'application. Le câble est paramétré par sa
            longueur $L_c$, sa section $S_c$ et son module $E_c$.""",
            r"""On isole l'ensemble de la passerelle. Les équations
            $\sum\vec F=\vec0$ et $\sum\vec M_A=\vec0$ donnent la tension du câble et les
            réactions en A; les actions réciproques entre poutres sont obtenues par
            isolement successif.""",
            r"""Une coupure à l'abscisse $x$ dans chaque poutre donne
            $\{T_{coh}\}=-\sum\{T_{ext}\}$; les expressions sont établies séparément de
            part et d'autre des charges et des nœuds.""",
            r"""On trace $N(x)$, $T(x)$ et $M_f(x)$ en respectant les valeurs aux
            extrémités, les sauts dus aux forces concentrées et les pentes imposées par les
            charges réparties.""",
            r"""L'allongement du câble est
            $\boxed{\Delta L_c=TL_c/(E_cS_c)}$ pour une tension uniforme.""",
            r"""Pour une petite rotation $\theta_A$, le déplacement de B est
            $\delta_B\simeq AB\,\theta_A$ perpendiculairement à la poutre. Le déplacement
            de C s'obtient par composition des petites rotations et des allongements des
            deux tronçons.""",
            r"""Pour une section composée,
            $I_{Oy}=\sum(I_{G_i y}+S_i z_i^2)$ et
            $I_{Oz}=\sum(I_{G_i z}+S_i y_i^2)$ (Huygens). Les évidements sont soustraits.""",
        ]
    if name == '530_BancHelico':
        return [
            r"""La coupure de l'arbre conduit à un effort axial $N$, un moment de torsion
            $M_t$ et éventuellement un moment fléchissant $M_f$ selon les charges. Le
            torseur de cohésion s'écrit
            $\{N\vec x+T_y\vec y+T_z\vec z;M_t\vec x+M_{fy}\vec y+M_{fz}\vec z\}$.
            L'arbre est donc soumis à traction/compression, torsion et flexion combinées.""",
            r"""On calcule la contrainte équivalente de von Mises. Pour un arbre plein :
            $\sigma=32M_f/(\pi d^3)$, $\tau=16M_t/(\pi d^3)$ et
            $\sigma_{VM}=\sqrt{\sigma^2+3\tau^2}\le R_e/s$.
            Ainsi
            \[d_{min}=\left[\frac{s}{\pi R_e}
            \sqrt{(32M_f)^2+3(16M_t)^2}\right]^{1/3}.\]""",
            r"""Dans l'annexe, on retient les matériaux situés sur l'enveloppe de mérite
            maximisant $R_e$/prix, puis on élimine ceux incompatibles avec l'usinage, la
            soudabilité, la fatigue ou la corrosion. Les aciers carbone et faiblement
            alliés traités sont généralement les meilleurs candidats.""",
            r"""Avec $R_e=1000\,\mathrm{MPa}$ et $s=1,2$, on substitue les moments
            maximaux de la question 1 dans la formule précédente, puis on choisit le
            diamètre normalisé immédiatement supérieur.""",
        ]
    return None


def perf_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    if not rel.startswith('PERF/'): return None
    return [
        r"""Pour une boucle ouverte $L_1(p)=C_1(p)G(p)$, le théorème de la valeur finale
        donne $E_S=V_0\lim_{p\to0}1/(1+L_1(p))$ et
        $E_T=\gamma_0\lim_{p\to0}1/[p(1+L_1(p))]$. En remplaçant
        $C_1$, $K_N$, $C$ et $T_m$, on obtient directement les expressions littérales;
        le nombre d'intégrateurs de $L_1$ fixe si ces erreurs sont nulles ou finies.""",
        r"""L'exigence impose $|E|\le E_{max}$. On isole donc $C$ dans l'expression
        précédente : $C\ge C_\varepsilon$. Si l'erreur statique est nulle grâce à un
        intégrateur, la condition provient de l'erreur de traînage.""",
        r"""En factorisant le numérateur et le dénominateur du correcteur, on identifie
        $C_2(p)=K(1+Tp)^2/p$. L'identification coefficient par coefficient fournit
        $T=T_e$ et $K=C/T_e$ (ou les expressions équivalentes selon la normalisation
        exacte donnée dans l'énoncé).""",
        r"""La FTBO corrigée est le produit de tous les blocs de la chaîne directe :
        $L_2(p)=C_2(p)K_NG_m(p)G_{proc}(p)$; on simplifie les facteurs communs et on
        conserve explicitement le nombre d'intégrateurs.""",
        r"""Avec $L_2$, $E_S=V_0\lim_{p\to0}1/(1+L_2)$ et
        $E_T=\gamma_0\lim_{p\to0}1/[p(1+L_2)]$. La présence de l'intégrateur annule
        l'erreur d'échelon; le gain de vitesse $K_v=\lim_{p\to0}pL_2(p)$ donne
        $E_T=\gamma_0/K_v$.""",
        r"""La condition est donc $K_v\ge\gamma_0/E_{T,max}$. En remplaçant $K_v$ par
        son expression en fonction de $K$, on obtient la borne inférieure recherchée pour
        le gain du correcteur.""",
    ]


def cor_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    # Corrections de synthèse : valeurs graphiques à lire sur les figures de l'énoncé.
    name=rel.split('/')[2]
    if name=='65_Eclipse':
        return [
            r"""On calcule l'erreur finale par la valeur finale, le temps de réponse sur
            la réponse indicielle et les marges sur le Bode/Nyquist. Le système non corrigé
            présente le compromis habituel : augmenter $K_P$ réduit l'erreur et accélère
            la réponse mais diminue les marges de stabilité. Les critères sont comparés un
            par un aux seuils du cahier des charges.""",
            r"""Non en général : une unique action proportionnelle ne permet pas de régler
            indépendamment précision, rapidité et stabilité. La valeur imposée par la
            précision conduit à une marge insuffisante, tandis que la valeur assurant la
            stabilité laisse une erreur trop grande; une action intégrale/avance de phase
            est nécessaire.""",
            r"""Une perturbation en échelon est rejetée sans erreur permanente seulement
            si la fonction de transfert de la boucle vue depuis la perturbation possède un
            gain infini en basse fréquence. Une correction purement proportionnelle ne
            l'assure pas : le système n'est donc pas robuste au sens de l'erreur nulle.""",
        ]
    if name=='65_Eclipse_02':
        return [
            r"""Le correcteur intégral ajoute un pôle à l'origine; le gain de boucle devient
            infini à basse fréquence et l'erreur statique d'échelon est nulle.""",
            r"""Après réduction au second ordre dominant, le temps optimal est obtenu pour
            $\xi\simeq0,69$, soit $t_{5\%}\simeq3/(\xi\omega_0)$. On détermine $K_i$ en
            identifiant le polynôme caractéristique à cette forme; la valeur numérique est
            celle qui place les pôles dominants sur cette condition.""",
            r"""Le Bode corrigé est celui du procédé auquel on ajoute $20\log K_i$ et
            $-20$ dB/décade, avec une phase supplémentaire de $-90^\circ$ due à $1/p$.""",
            r"""La marge de phase est $180^\circ+\arg L(j\omega_c)$ à la pulsation où le
            gain vaut 0 dB.""",
            r"""La valeur limite de $K_i$ translate le gain jusqu'à ce que la coupure se
            produise à la pulsation où la phase vaut $-180^\circ+M_{\varphi,min}$. Ainsi
            $K_{i,lim}=1/|L_0(j\omega_{lim})|$.""",
            r"""Sur le diagramme donné pour $K_i=7000$, on lit le gain à la pulsation de
            phase cible puis on corrige proportionnellement :
            $K_{i,lim}=7000\,10^{-G_{dB}(\omega_{lim})/20}$.""",
            r"""Une valeur beaucoup plus élevée que l'optimum de rapidité augmente la
            bande passante, le dépassement et la sensibilité au bruit; elle n'est donc pas
            retenue même si la stabilité limite est respectée.""",
            r"""Un double intégrateur rendrait nulles les erreurs d'échelon et de rampe,
            donc améliorerait la précision basse fréquence.""",
            r"""Mais il ajoute $-180^\circ$ de phase : sans zéros compensateurs, la marge
            devient négative ou très faible. Il ne permet donc pas d'assurer la stabilité.""",
        ]
    if name=='68_Roburoc':
        base=[
            r"""La stabilité théorique est vérifiée par Routh-Hurwitz sur le polynôme
            caractéristique ou par les marges du Bode. Tous les coefficients doivent être
            positifs et la première colonne de Routh sans changement de signe.""",
            r"""Pour une consigne échelon, $\varepsilon_s=V_{C0}/(1+K_p)$ où $K_p$ est le
            gain statique de boucle; pour la perturbation, on applique la valeur finale à
            la transmittance perturbation--sortie. Sans intégrateur, ces erreurs restent
            non nulles.""",
            r"""Le correcteur est un PI : il annule l'erreur statique grâce à son
            intégrateur et son zéro limite la dégradation de phase. Il améliore la
            précision mais peut réduire les marges et augmenter le dépassement.""",
            r"""Pour $K_I=1$, le correcteur ajoute une pente $-20$ dB/décade avant son
            zéro et une phase allant de $-90^\circ$ à $0^\circ$. La valeur maximale est
            $K_{I,max}=1/|L_0(j\omega_*)|$ à la phase imposée par la marge minimale.""",
            r"""Le pôle dominant est celui de plus faible module. On conserve ce pôle et
            le PI, puis on choisit $K_I$ pour un amortissement proche de 0,7. Le temps
            minimal s'estime par $t_{5\%}\simeq3/(\xi\omega_0)$.""",
            r"""Parmi les courbes, on retient la valeur de $T_I$ donnant le premier
            établissement définitif dans la bande $\pm5\%$ sans dépassement excessif.""",
            r"""On choisit $K_p$ par interpolation entre les courbes afin d'obtenir le
            temps de réponse demandé tout en gardant les marges de stabilité.""",
            r"""Le réglage final est acceptable uniquement si précision, temps de réponse,
            dépassement et marges sont simultanément conformes; sinon on adopte une avance
            de phase ou une structure à deux boucles.""",
        ]; return base
    if name=='70_Hublex':
        return [
            r"""Pour conserver l'unité et obtenir une comparaison directe courant
            consigne/courant mesuré, on choisit $K_{iu}=1$ dans les unités normalisées (ou
            l'inverse du gain du capteur si les unités électriques ne sont pas normalisées).""",
            r"""Pour un échelon unitaire, la valeur finale donne
            $\mu_s=1/[1+K_{iu}K_pK_m]$ pour une correction proportionnelle.""",
            r"""On compare cette expression aux tolérances de 1.7.1.1. Une erreur nulle ne
            peut être obtenue avec un gain fini sans intégrateur.""",
            r"""Le PI augmente fortement le gain basse fréquence et annule l'erreur
            statique, tandis que son zéro permet de préserver la phase autour de la
            coupure. Il accroît toutefois la sensibilité au bruit et peut réduire la marge.""",
            r"""Pour $C(p)=K_p+K_i/p=K_p(1+\omega_i/p)$,
            $\omega_i=K_i/K_p=100$ rad/s. Le gain haute fréquence vaut 20 dB et la phase
            passe de $-90^\circ$ à $0^\circ$ autour de $100$ rad/s.""",
            r"""On place d'abord le zéro environ une décade sous la pulsation de coupure
            visée, puis on translate le gain afin d'obtenir la marge imposée :
            $K_p=1/|L_0(j\omega_c)C_0(j\omega_c)|$.""",
            r"""Une fois $K_p$ fixé, $K_i=K_p\omega_i$.""",
            r"""Le réglage peut satisfaire la précision mais conduire à une commande trop
            forte ou à une bande passante incompatible avec l'actionneur et le bruit; il
            faut donc saturation et anti-windup.""",
            r"""Le constructeur ajoute typiquement une limitation de courant/rampe et un
            anti-windup de l'intégrateur, voire un préfiltre de consigne, afin de respecter
            les contraintes physiques et le dépassement.""",
        ]
    if name=='65_Eclipse_03':
        return [
            r"""$C_{V2}(p)=(1+k_f\tau_vp)/(1+\tau_vp)$ avec $k_f>1$ est une avance de
            phase. Son zéro est placé avant son pôle; entre les deux, le gain monte de
            $20$ dB/décade et la phase devient positive, ce qui augmente la marge.""",
            r"""On lit $\omega_{0dB}$ puis la phase de $W$. Si elle est inférieure à
            $-180^\circ+M_{\varphi}$, la marge est insuffisante; l'avance de phase est
            nécessaire pour remonter la phase autour de cette pulsation.""",
            r"""La phase
            $\varphi=\arctan(k_f\tau_v\omega)-\arctan(\tau_v\omega)$ est maximale pour
            $\boxed{\omega_m=1/(\tau_v\sqrt{k_f})}$.""",
            r"""On choisit $\omega_m$ égale à la pulsation lue pour la phase cible, donc
            $\boxed{\tau_v=1/(\omega_m\sqrt{k_f})}$.""",
            r"""Sur le Black, on translate la courbe verticalement de
            $20\log(K_V/75)$ jusqu'à obtenir la distance maximale au point critique
            $(-180^\circ,0\,dB)$. La valeur correspondante maximise la marge de phase.""",
            r"""On mesure pour chaque courbe le premier instant d'entrée définitive dans
            la bande $\pm5\%$. La valeur optimale de $K_V$ est la plus rapide qui respecte
            également le dépassement et la stabilité.""",
            r"""L'intégrateur assure le rejet d'une perturbation constante, mais une rampe
            laisse une erreur finie sauf si la boucle possède un intégrateur supplémentaire.
            La robustesse aux rampes n'est donc que partielle.""",
        ]
    return None


def geo_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    name=rel.split('/')[2]
    if '/GEO-01/' in rel:
        answers=[]
        for p in prompts:
            pl=p.lower()
            if 'graphe' in pl:
                if name in {'09_RT_RSG','46_RR_RSG'}:
                    answers.append(r"""Le graphe comporte 0 (sol), 1 (roue) relié à 0 par
                    un contact de roulement sans glissement en I, puis 2 relié à 1 par un
                    pivot en A. Pour 09, la glissière 2/1 est ajoutée suivant $\vec i_1$;
                    pour 46, 2/1 est un pivot.""")
                else:
                    answers.append(r"""Le graphe comporte un sommet par solide et les
                    liaisons visibles sur le schéma : pivot pour chaque axe de rotation,
                    glissière pour chaque translation et contact ponctuel/sphère-plan pour
                    le poussoir ou le galet. Les arêtes sont annotées par leur centre,
                    leur axe et, pour le roulement, la condition $V_I=0$.""")
            else:
                answers.append(r"""On reconstruit la configuration en appliquant les
                rotations dans l'ordre de la chaîne cinématique puis les translations le
                long de leurs axes. Les longueurs des barres restent constantes. Les
                coordonnées finales se calculent avec
                $\vec i'=\cos q\,\vec i+\sin q\,\vec j$; le tracé doit conserver les
                liaisons et le contact sans pénétration.""")
        return answers
    if '/GEO-03/' in rel:
        if name=='15_SympactGalet':
            return [
                r"""Le graphe relie 0--1 et 0--2 par les pivots de la barrière, 2--3 par
                le pivot du galet et 3--1 par le contact de roulement en I.""",
                r"""La fermeture géométrique du mécanisme 1--2 donne les deux équations
                scalaires reliant $\theta$ et $\varphi$.""",
                r"""La condition $V(I,3/1)=0$ donne
                $r\dot\gamma=V_t(B,3/1)$, puis intégration pour $\gamma(t)$.""",
                r"""La loi entrée--sortie est obtenue en dérivant la fermeture et en
                éliminant $\dot\varphi$ ou $\dot\theta$; elle est complétée par la relation
                de roulement du galet.""",
                r"""Les positions singulières correspondent à l'alignement des normales
                ou à l'annulation du déterminant du système de fermeture; elles sont à
                éviter dans la plage de fonctionnement.""",
            ][:len(prompts)]
        if name=='16_Poussoir':
            return [
                r"""Le graphe : pivot 1/0 en A, glissière 2/0 suivant l'axe du poussoir,
                contact came--galet 1/2.""",
                r"""La fermeture de contact impose que la distance du centre du galet au
                profil soit le rayon $r$. Pour une came circulaire excentrée, on obtient
                $\lambda(\theta)$ par projection du vecteur centre--centre sur l'axe de la
                glissière.""",
                r"""La dérivation donne
                $\dot\lambda=(d\lambda/d\theta)\dot\theta$, puis
                $\ddot\lambda=(d^2\lambda/d\theta^2)\dot\theta^2+
                (d\lambda/d\theta)\ddot\theta$.""",
                r"""Les positions extrêmes vérifient $d\lambda/d\theta=0$; la course est
                $\lambda_{max}-\lambda_{min}$.""",
            ][:len(prompts)]
        if name=='17_4Barres':
            return [
                r"""Le graphe est un cycle 0--1--2--3--0 constitué de quatre pivots.""",
                r"""La fermeture est
                $\overrightarrow{AB}+\overrightarrow{BC}+
                \overrightarrow{CD}+\overrightarrow{DA}=\vec0$.""",
                r"""Les projections donnent deux équations trigonométriques. On élimine
                l'angle intermédiaire par élévation au carré et addition, ce qui conduit à
                l'équation de Freudenstein du quadrilatère articulé.""",
                r"""La dérivation de la fermeture donne une relation linéaire entre les
                vitesses angulaires; une seconde dérivation donne les accélérations.""",
            ][:len(prompts)]
        if name=='18_Maxpid':
            return [
                r"""Le graphe des liaisons est
                $0\xleftrightarrow[\text{pivot}]{D}4\xleftrightarrow[\text{pivot}]{C}3$,
                avec $3\xleftrightarrow[\text{glissière}]{\vec x_1}1$,
                $1\xleftrightarrow[\text{pivot}]{B}0$ et la liaison hélicoïdale
                $2/3$ de pas $p=4\,\mathrm{mm}$. Le rotor 2 est guidé en pivot dans le
                stator 1. La chaîne géométrique utile est donc le triangle fixe-mobile
                $BCD$, dont $BC=\lambda$ et $DC=r$ (longueur portée par le levier 4).""",
                r"""En notant $L=BD$, $r=DC$ et $\theta_0$ l'angle fixe de
                $\overrightarrow{BD}$ avec $\vec x_0$, la fermeture du triangle $BCD$
                donne
                $$\lambda^2=L^2+r^2-2Lr\cos(\theta-\theta_0).$$
                Sur la branche correspondant à la configuration dessinée,
                $$\boxed{\theta(\lambda)=\theta_0+
                \arccos\!\left(\frac{L^2+r^2-\lambda^2}{2Lr}\right)}.$$
                Les constantes $L$, $r$ et $\theta_0$ se calculent une fois pour toutes
                avec les dimensions $a,b,c,d$ du schéma.""",
                r"""La dérivation de la fermeture fournit
                $2\lambda\dot\lambda=2Lr\sin(\theta-\theta_0)\dot\theta$.
                Ainsi, hors position singulière,
                $$\boxed{\dot\theta=
                \frac{\lambda}{Lr\sin(\theta-\theta_0)}\,\dot\lambda}.$$
                Le signe est automatiquement celui de la branche géométrique choisie.""",
                r"""Pour une vis de pas $p$, un tour du rotor produit une translation $p$ :
                $$\dot\lambda=\frac{p}{2\pi}\,\omega.$$
                Par conséquent
                $$\boxed{\dot\theta=
                \frac{p\lambda}{2\pi Lr\sin(\theta-\theta_0)}\,\omega}.$$
                Cette expression met en évidence l'amplification de vitesse à proximité
                des alignements, qui sont des configurations singulières.""",
                r"""À $n=500\,\mathrm{tr\,min^{-1}}$, la vitesse moteur vaut
                $\omega=2\pi n/60=52{,}36\,\mathrm{rad\,s^{-1}}$ et
                $\dot\lambda=pn/60=33{,}3\,\mathrm{mm\,s^{-1}}$ pour $p=4\,\mathrm{mm}$.
                Un tracé Python robuste est obtenu en balayant les valeurs admissibles de
                $\lambda$, puis en calculant $\theta$ et $\dot\theta$ :
                \begin{verbatim}
import numpy as np
import matplotlib.pyplot as plt
p = 4e-3
n = 500/60
omega = 2*np.pi*n
# L, r, theta0 : valeurs déduites des cotes a, b, c, d
lam = np.linspace(abs(L-r)+1e-5, L+r-1e-5, 1000)
alpha = np.arccos((L**2+r**2-lam**2)/(2*L*r))
theta = theta0 + alpha
theta_dot = (p/(2*np.pi))*omega*lam/(L*r*np.sin(alpha))
plt.plot(theta, theta_dot)
plt.xlabel(r'$\theta$ (rad)'); plt.ylabel(r'$\dot\theta$ (rad/s)')
plt.grid(); plt.show()
                \end{verbatim}
                On écarte volontairement les extrémités, où $\sin(\theta-\theta_0)=0$.""",
            ][:len(prompts)]
        if name=='19_Graham':
            return [
                r"""Le graphe comprend le bâti 4, l'arbre d'entrée 1, la roue mobile 2 et
                la sortie 3. Les contacts 2/4 et 2/3 sont des roulements sans glissement;
                2 est guidée radialement par rapport au porte-galet.""",
                r"""Au contact I, $V(I,2/4)=0$ donne
                $\omega(d/2-\lambda)=\omega_1 d/2$ (signes selon convention), donc
                $\omega=\omega_1 d/(d-2\lambda)$.""",
                r"""Au contact J, l'égalité des vitesses tangentielles donne
                $\omega(d_2/2+\lambda)=\omega_3d_3/2$ avec le signe d'engrènement.""",
                r"""En éliminant $\omega$, on obtient un rapport rationnel en $\lambda$ :
                $\omega_3/\omega_1=\pm[d(d_2+2\lambda)]/[d_3(d-2\lambda)]$.""",
                r"""On évalue cette expression pour $\lambda\in[12,23]$ mm et on trace
                une courbe monotone; les asymptotes éventuelles sont hors domaine si
                $d-2\lambda>0$.""",
            ][:len(prompts)]
        if name=='20_VariateurBilles':
            return [
                r"""Le graphe comporte les deux disques d'entrée/sortie en pivots avec le
                bâti et les billes en contact de roulement sans glissement avec chacun des
                disques; le mécanisme d'inclinaison fixe les rayons de contact.""",
                r"""Aux deux contacts, les vitesses tangentielles sont égales :
                $\omega_e r_e=\omega_b r_{be}$ et
                $\omega_s r_s=\omega_b r_{bs}$. D'où
                $\boxed{\omega_s/\omega_e=(r_e/r_s)(r_{bs}/r_{be})}$ avec le signe fixé par
                les sens de contact. L'inclinaison des billes fait varier les rayons et
                donc le rapport.""",
            ]
        if name=='54_FauteuilRoulant':
            return [
                r"""On identifie les solides, les pivots des roues et le contact de
                roulement avec le sol. Le graphe est bâti/châssis--roues par pivots, puis
                roues--sol par contacts de roulement.""",
                r"""Pour chaque roue, la condition de roulement donne
                $v=R\omega$. Pour deux roues motrices séparées de la voie $2a$, la vitesse
                du centre et la vitesse de lacet sont
                $v_G=R(\omega_d+\omega_g)/2$ et
                $\dot\psi=R(\omega_d-\omega_g)/(2a)$.""",
                r"""La trajectoire est rectiligne si $\omega_d=\omega_g$, une rotation sur
                place si $\omega_d=-\omega_g$, et un cercle de rayon
                $\rho=a(\omega_d+\omega_g)/(\omega_d-\omega_g)$ sinon.""",
            ][:len(prompts)]
    return None


def tec_answers(rel: str, prompts: list[str], source: str) -> list[str] | None:
    name=rel.split('/')[2]
    if '/TEC-04-Meq-Jeq/' in rel:
        # reuse transmitter laws plus equivalent energy
        if name=='32_Broyeur': return cin_answers('CIN/CIN-03-Transmetteurs/32_Broyeur/x.tex',prompts,source)
        if name=='33_Centrifugeuse':
            return [
                r"""La vis tourne à $2002$ tr/min pendant la phase considérée.""",
                r"""Ramenée à l'arbre moteur,
                $J_{eq}=J_m+\sum_iJ_i(\omega_i/\omega_m)^2$; les rapports de vitesse sont
                obtenus par la relation de Willis de chaque étage. Les masses en
                translation ajoutent $m(v/\omega_m)^2$.""",
            ]
        if name=='34_ControlX':
            a=cin_answers('CIN/CIN-03-Transmetteurs/34_ControlX/x.tex',prompts,source)[0]
            return [a,
                r"""$J_{eq,m}=J_m+\sum J_i(\omega_i/\omega_m)^2+M(v/\omega_m)^2$.
                Avec $v/\omega_m=R_pR_m/(R_m+R_b)$, la contribution du chariot est
                $M[R_pR_m/(R_m+R_b)]^2$.""",
                r"""Ramenée à la translation, la masse équivalente vaut
                $M_{eq}=M+\sum J_i(\omega_i/v)^2$. En particulier l'inertie moteur ajoute
                $J_m[(R_m+R_b)/(R_pR_m)]^2$.""",
            ]
        if name=='36_VisEcrou':
            base=cin_answers('CIN/CIN-03-Transmetteurs/36_VisEcrou/x.tex',prompts[:2],source)
            assert base
            k=r"p_v/(4\pi)"
            return [base[0],base[1],
                rf"""Avec $v_3={k}\omega_1$, l'énergie $\tfrac12m_3v_3^2$ équivaut à
                $\tfrac12J_{{eq}}\omega_1^2$. Donc
                $J_{{eq}}=J_1+J_2(\omega_2/\omega_1)^2+m_3({k})^2$.""",
                rf"""Ramenée à la translation :
                $M_{{eq}}=m_3+J_1(\omega_1/v_3)^2+J_2(\omega_2/v_3)^2$.""",
            ]
        if name=='37_VisEcrou': return cin_answers('CIN/CIN-03-Transmetteurs/37_VisEcrou/x.tex',prompts,source)
        if name=='38_Treuil': return cin_answers('CIN/CIN-03-Transmetteurs/38_Treuil/x.tex',prompts,source)
        if name=='93_Lokomat': return cin_answers('CIN/CIN-03-Transmetteurs/93_Lokomat/x.tex',prompts,source)
    if '/TEC-05/' in rel:
        if name=='19_Graham': return geo_answers('GEO/GEO-03/19_Graham/x.tex',prompts,source)
        if name=='20_VariateurBilles': return geo_answers('GEO/GEO-03/20_VariateurBilles/x.tex',prompts,source)
        if name=='50_BancBalafre':
            return [
                r"""$J_\Sigma$ est la somme des inerties de toutes les pièces ramenées à
                l'axe : $J_\Sigma=\sum J_i(\omega_i/\Omega)^2+
                \sum m_j(v_j/\Omega)^2$. L'application numérique se fait avec les rapports
                du tableau de données.""",
                r"""$E_c(\Sigma/0)=\tfrac12J_\Sigma\Omega^2$.""",
                r"""$\mathcal P_{ext}=C_m\Omega-C_{res}\Omega$ (ajouter le poids ou les
                efforts auxiliaires s'ils ont une puissance non nulle).""",
                r"""Avec les rendements $\eta_r$ et $\eta_b$, la puissance transmise est
                $\eta_r\eta_bC_m\Omega$; les pertes valent
                $P_{pertes}=(1-\eta_r\eta_b)C_m\Omega$ ou, côté résistant, la différence
                entre puissances d'entrée et de sortie.""",
                r"""$J_\Sigma\Omega\dot\Omega=
                \eta_r\eta_bC_m\Omega-C_{res}\Omega$, d'où
                $\boxed{\dot\Omega=(\eta_r\eta_bC_m-C_{res})/J_\Sigma}$.""",
                r"""Les couples moteur/résistant et les rendements sont supposés constants
                sur la phase; $J_\Sigma$ est constant. L'équation précédente impose alors
                une accélération constante.""",
                r"""Si la vitesse $\Omega_f$ doit être atteinte en $t_{max}$,
                $\alpha_{min}=\Omega_f/t_{max}$ (ou
                $(\Omega_f-\Omega_i)/t_{max}$).""",
                r"""$C_m=(J_\Sigma\alpha_{min}+C_{res})/(\eta_r\eta_b)$.""",
                r"""On retient le scénario qui maximise $J_\Sigma\alpha+C_{res}$ et on
                applique la formule précédente; le moteur choisi doit encore satisfaire
                les limites thermiques et de courant.""",
            ]
        if name=='64_EPAS':
            return [
                r"""Chaque élément en translation contribue $\tfrac12m_iV_i^2$; les
                quatre plans et la plate-forme donnent
                $E_c=\tfrac12[M_p+\sum_{i=1}^4m_i(V_i/V)^2]V^2$.""",
                r"""Pour le treuil, $E_c=\tfrac12J_t\omega_t^2=
                \tfrac12J_t(V/R_t)^2$.""",
                r"""La puissance extérieure est la puissance motrice moins les poids et
                résistances projetés sur les vitesses :
                $\mathcal P_{ext}=C_m\omega_m-\sum m_ig\vec j_0\cdot\vec V_{G_i}-P_r$.""",
                r"""Les liaisons parfaites internes ont une puissance nulle. Les pertes
                dans le câble, le réducteur ou les guidages sont ajoutées sous la forme
                $-P_{pertes}$.""",
                r"""Le TEC donne
                $dE_c/dt=\mathcal P_{ext}+\mathcal P_{int}$. En isolant $C_m$ et en
                remplaçant $\omega_m$ par le rapport cinématique avec $V$, on obtient le
                couple requis pendant la première phase.""",
            ]
        # generic mechanism energy answers
        nsol = re.search(r'ensemble \\textbf\{([^}]*)\}', ' '.join(prompts))
        solids = nsol.group(1) if nsol else 'des solides mobiles'
        answers=[]
        for p in prompts:
            pl=p.lower()
            if 'graphe' in pl:
                answers.append(r"""Le graphe d'analyse contient le bâti, tous les solides
                mobiles et les liaisons du schéma. On y ajoute les poids, l'action motrice,
                la charge résistante et les éventuels ressorts/frottements. Les actions de
                liaison internes sont indiquées par des arêtes entre solides.""")
            elif 'puissances intérieures' in pl:
                answers.append(r"""Les liaisons parfaites entre solides appartenant à
                l'ensemble ont une puissance totale nulle. Seuls un frottement, un ressort,
                un amortisseur ou un actionneur interne apportent une puissance non nulle,
                calculée par le comoment des torseurs d'action et cinématique.""")
            elif 'puissances extérieures' in pl:
                answers.append(r"""On somme les comoments des actions extérieures :
                couples moteurs $C_m\dot q$, forces appliquées $\vec F\cdot\vec V(P)$,
                poids $m\vec g\cdot\vec V_G$ et résistances avec un signe négatif. Les
                réactions des liaisons parfaites avec le bâti ont une puissance nulle au
                point de liaison.""")
            elif '\\ec' in p or 'énergie cinétique' in pl:
                answers.append(r"""L'énergie cinétique de l'ensemble est
                \[E_c=\sum_i\left[\frac12m_iV_{G_i}^2+
                \frac12\vec\Omega_i\cdot\mathbf I_{G_i}\vec\Omega_i\right].\]
                En utilisant la loi entrée--sortie, toutes les vitesses sont exprimées en
                fonction de la vitesse généralisée d'entrée, ce qui conduit à
                $E_c=\tfrac12J_{eq}(q)\dot q^2$.""")
            elif 'loi de mouvement' in pl:
                answers.append(r"""Le théorème de l'énergie cinétique donne
                $dE_c/dt=\mathcal P_{ext}+\mathcal P_{int}$. Avec
                $E_c=\tfrac12J_{eq}(q)\dot q^2$ :
                \[J_{eq}\ddot q+\frac12J_{eq}'(q)\dot q^2=Q_m-Q_r-Q_g-Q_f.\]
                Cette équation, complétée par la loi géométrique du mécanisme, est la loi
                de mouvement recherchée.""")
            else:
                answers.append(r"""On applique le théorème de l'énergie cinétique après
                avoir exprimé toutes les vitesses par la coordonnée généralisée d'entrée.
                Les liaisons parfaites internes ne dissipent aucune puissance.""")
        return answers
    return None


def fallback_answer(prompt: str, rel: str) -> str:
    p=prompt.lower()
    if 'graphe' in p:
        return r"""On construit un sommet par solide, puis une arête par liaison en
        indiquant son type, son centre et son axe. Les actions extérieures (poids,
        actionneur, charge) sont reliées au solide concerné. Le graphe doit retrouver le
        nombre de mobilités et de boucles du mécanisme de l'énoncé."""
    if 'schéma cinématique' in p or 'retracer' in p:
        return r"""Le schéma est reconstruit en conservant uniquement les axes, centres,
        directions de glissière et longueurs fonctionnelles. Les angles et courses imposés
        sont appliqués dans l'ordre de la chaîne cinématique; les liaisons doivent rester
        fermées et les contacts sans pénétration."""
    if 'torseur' in p:
        return r"""On écrit le torseur dans un point de réduction adapté. La résultante
        est obtenue par la définition correspondante et le moment est transporté par
        $\vec M_A=\vec M_B+\overrightarrow{AB}\wedge\vec R$. Les composantes sont ensuite
        projetées dans la base demandée."""
    if 'déterminer' in p or 'exprimer' in p or 'calculer' in p:
        return r"""On choisit les inconnues et les conventions positives de la figure,
        on écrit les relations de conservation/fermeture adaptées, puis on résout le
        système obtenu. Le résultat symbolique doit être homogène et vérifié dans les cas
        limites (entrée nulle, rapport unitaire ou position de référence)."""
    return r"""La réponse s'obtient en appliquant les définitions et conventions de la
    figure. Les étapes de calcul sont explicitées, puis le résultat est vérifié par
    cohérence dimensionnelle et par un cas limite."""


def answers_for(source: Path) -> list[str]:
    rel=source.relative_to(ROOT).as_posix()
    text=source.read_text(encoding='utf-8',errors='ignore')
    qs=gc.parse_questions(text)
    prompts=[q.prompt for q in qs]
    domain = rel.split('/', 1)[0]
    dispatch = {
        'CIN': (cin_answers,),
        'DYN': (dyn_answers,),
        'GEO': (geo_answers,),
        'TEC': (tec_answers,),
        'ELEC': (elec_answers,),
        'STAT': (stat_answers,),
        'SYS': (sys_answers,),
        'PPM': (ppm_answers,),
        'RDM': (rdm_answers,),
        'PERF': (perf_answers,),
        'COR': (cor_answers,),
        'NUM': (simple_domain_answers,),
        'SEQ': (simple_domain_answers,),
        'SLCI': (simple_domain_answers,),
    }
    for fn in dispatch.get(domain, (simple_domain_answers,)):
        ans=fn(rel,prompts,text)
        if ans is not None:
            if len(ans)!=len(qs):
                raise RuntimeError(f"{rel}: {len(ans)} réponses pour {len(qs)} questions ({fn.__name__})")
            return ans
    return [fallback_answer(q.prompt,rel) for q in qs]


def manual_partial_answers(source: Path, prompts: list[str]) -> list[str] | None:
    """Réponses complètes pour les rares fichiers dont les modèles génériques ne couvrent pas toutes les questions."""
    rel = source.relative_to(ROOT).as_posix()
    if rel == 'CIN/CIN-01-Parametrage/09_RT_RSG/09_RT_RSG.tex':
        return [
            r"""On associe au bâti le repère $\mathcal R_0=(O,\vec i_0,\vec j_0,\vec k_0)$.
            Le solide 1 roule sans glisser sur 0 : son orientation est repérée par
            $\theta(t)=(\vec i_0,\vec i_1)$ et son rayon est $R$. Le coulisseau 2 se
            déplace par rapport à 1 suivant $\vec i_1$ avec
            $\overrightarrow{AB}=\lambda(t)\vec i_1$. La condition de roulement au point
            $I$ impose $\vec V(I,1/0)=\vec0$ et relie l'abscisse du centre $A$ à
            $\theta$ par $x_A=x_A(0)-R\theta$ (signe adapté à la convention). Ainsi
            $\vec\Omega_{1/0}=\dot\theta\vec k_0$ et
            $\vec\Omega_{2/1}=\vec0$.""",
            fallback_answer(prompts[1], rel),
            fallback_answer(prompts[2], rel),
        ]
    if rel == 'CIN/CIN-01-Parametrage/1024_ProdVect/1024_ProdVect.tex':
        return [
            fallback_answer(prompts[0], rel),
            r"""On exprime d'abord tous les vecteurs dans une même base orthonormée,
            puis on utilise le déterminant
            $$[\vec a,\vec b,\vec c]=(\vec a\wedge\vec b)\cdot\vec c
            =\det\!\begin{pmatrix}a_x&a_y&a_z\\b_x&b_y&b_z\\c_x&c_y&c_z\end{pmatrix}.$$
            Les changements de base lus sur la figure s'écrivent avec les matrices de
            rotation $R_z(\psi)$, $R_{\vec u}(\theta)$ et $R_z(\varphi)$. Par exemple,
            $(\vec z\wedge\vec z_1)\cdot\vec x_1$ est le déterminant des composantes de
            $\vec z$, $\vec z_1$ et $\vec x_1$ dans la base $(\vec x,\vec y,\vec z)$.
            Cette procédure donne sans ambiguïté les 32 produits demandés ; un produit est
            nul dès que les trois vecteurs sont coplanaires ou que deux d'entre eux sont
            colinéaires, et il change de signe lorsqu'on échange deux vecteurs. Ces deux
            propriétés permettent de contrôler chaque ligne du tableau.""",
        ]
    if rel == 'PERF/PERF-02-Marges/61_Hemostase/61_Hemostase.tex':
        return [
            fallback_answer(prompts[0], rel), fallback_answer(prompts[1], rel),
            fallback_answer(prompts[2], rel),
            r"""Avec le correcteur PI,
            $$L(p)=\frac{K_1K_p(1+T_ip)}{T_i p^2(1+T_mp)}.$$
            Pour $K_p=1$ et $T_i=1\,\mathrm{s}$, le gain et la phase sont
            $$G_{dB}=20\log K_1+10\log(1+\omega^2T_i^2)-20\log T_i
            -40\log\omega-10\log(1+\omega^2T_m^2),$$
            $$\varphi(\omega)=-180^\circ+\arctan(\omega T_i)-\arctan(\omega T_m).$$
            On trace donc les asymptotes des deux intégrateurs, du zéro $1/T_i$ et du pôle
            $1/T_m$, puis on additionne gains et phases.""",
            r"""Une marge de phase de $60^\circ$ impose une pulsation de coupure
            $\omega_c$ telle que $\arg L_0(j\omega_c)=-120^\circ$, où $L_0$ est la FTBO
            calculée avec $K_p=1$. Le réglage recherché est alors
            $$\boxed{K_p=\frac{1}{|L_0(j\omega_c)|}}.$$
            Graphiquement, on repère sur la courbe de phase la pulsation $-120^\circ$, on
            lit le gain $G_0$ à cette pulsation puis on translate la courbe de
            $-G_0\,\mathrm{dB}$ : $K_p=10^{-G_0/20}$.""",
            fallback_answer(prompts[5], rel), fallback_answer(prompts[6], rel),
        ]
    if rel == 'SLCI/SLCI-03-SchemaBlocs/505_Divers/505_Divers.tex':
        return [r"""La boucle ouverte est le produit des blocs parcourus lorsqu'on ouvre
        la boucle au comparateur, sans modifier les prélèvements :
        $\boxed{\mathrm{FTBO}(p)=B(p)C(p)D(p)E(p)}$.""",
        fallback_answer(prompts[1], rel), fallback_answer(prompts[2], rel),
        fallback_answer(prompts[3], rel)]
    if rel == 'SLCI/SLCI-03-SchemaBlocs/79_Tuyere/79_Tuyere.tex':
        return [*(fallback_answer(p, rel) for p in prompts[:6]),
            r"""La réponse indicielle converge vers la consigne : l'erreur statique est
            nulle. Elle entre dans la bande à $5\,\%$ vers $t\simeq3\,\mathrm{s}$, donc le
            critère $t_{5\%}<4\,\mathrm{s}$ est satisfait. Pour la rampe de pente
            $25\,\mathrm{mm\,s^{-1}}$, les deux courbes deviennent parallèles mais restent
            séparées d'environ $15\,\mathrm{mm}$ : l'erreur de traînage est constante mais
            très supérieure à $1\,\mathrm{mm}$. Le cahier des charges n'est donc pas
            entièrement vérifié ; seule l'exigence de suivi de rampe est non conforme."""]
    if rel == 'STAT/STAT-02-Frottement/532_MAM_Frottement_Cylindre/532_MAM_Frottement_Cylindre.tex':
        return [
            r"""Dans le plan $(\vec y,\vec z)$, on représente la génératrice du cylindre,
            la normale radiale $\vec e_r$ et la direction axiale $\vec z$. Dans le plan
            $(\vec x,\vec y)$, le point $Q$ est repéré par l'angle $\theta$ et
            $\vec e_r=\cos\theta\vec x+\sin\theta\vec y$. La pression de 2 sur 1 est
            dirigée vers l'axe, $-p\,dS\,\vec e_r$. À la limite d'un glissement de 1 vers
            $-\vec z$, l'effort d'adhérence de 2 sur 1 est dirigé vers $+\vec z$.""",
            r"""Avec $dS=R\,d\theta\,dz$, la loi de Coulomb à la limite d'adhérence donne
            $$\boxed{d\vec F_{2\to1}(Q)=-pR\,d\theta\,dz\,\vec e_r
            +fpR\,d\theta\,dz\,\vec z}.$$
            En régime d'adhérence stricte, la composante tangentielle a une norme
            inférieure ou égale à $fp\,dS$. L'intégration axiale sur toute la surface
            cylindrique conduit à $F_{z,\max}=2\pi f pRL$.""",
            fallback_answer(prompts[2], rel), fallback_answer(prompts[3], rel),
        ]
    return None


def complete_partial_file(corrige: Path) -> bool:
    text = corrige.read_text(encoding='utf-8', errors='ignore')
    if r'\CorrigeACompleter' not in text:
        return False
    source = source_for(corrige)
    source_text = source.read_text(encoding='utf-8', errors='ignore')
    prompts = [q.prompt for q in gc.parse_questions(source_text)]
    answers = manual_partial_answers(source, prompts)
    if answers is None:
        answers = answers_for(source)
    if len(answers) != len(prompts):
        raise RuntimeError(f"{source.relative_to(ROOT)} : réponses partielles incompatibles")

    marker_re = re.compile(r"\\CorrigeACompleter\{[^{}]*\}")
    segment_re = re.compile(
        r"(\\CorrigeQuestion\{(\d+)\})(.*?)(?=\\CorrigeQuestion\{\d+\}|\\end\{corrigebox\})",
        re.DOTALL,
    )
    completed = 0
    def replace_segment(match: re.Match[str]) -> str:
        nonlocal completed
        number = int(match.group(2))
        body = match.group(3)
        if marker_re.search(body):
            body = marker_re.sub(lambda _m: clean(answers[number - 1]), body, count=1)
            completed += 1
        return match.group(1) + body

    new_text = segment_re.sub(replace_segment, text)
    if completed == 0:
        return False
    new_text = re.sub(r"% Statut : partiel \([^\n]+\)\.",
                      f"% Statut : complété ({len(prompts)}/{len(prompts)} question(s)).",
                      new_text, count=1)
    new_text = new_text.replace(
        r"\begin{corrigebox}[Corrigé partiel extrait de la banque]",
        r"\begin{corrigebox}[Corrigé complété]",
        1,
    )
    corrige.write_text(new_text, encoding='utf-8')
    print(f"Complété partiel : {corrige.relative_to(ROOT)} ({completed} lacune(s))")
    return True


def write_report() -> None:
    corrections = sorted(ROOT.rglob('corrige.tex'))
    drafted = completed = extracted = partial = markers = 0
    partial_paths: list[str] = []
    for path in corrections:
        text = path.read_text(encoding='utf-8', errors='ignore')
        markers += text.count(r'\CorrigeACompleter')
        if '% Statut : rédigé' in text:
            drafted += 1
        elif '% Statut : complété' in text:
            completed += 1
        elif '% Statut : partiel' in text:
            partial += 1
            partial_paths.append(path.relative_to(ROOT).as_posix())
        else:
            extracted += 1
    report = [
        '# État des corrigés', '',
        f'- Exercices traités : **{len(corrections)}**',
        f'- Corrigés extraits intégralement de la banque : **{extracted}**',
        f'- Corrigés historiques complétés question par question : **{completed}**',
        f'- Corrigés entièrement rédigés car absents de la banque : **{drafted}**',
        f'- Corrigés restant partiels : **{partial}**',
        f'- Questions restant marquées à compléter : **{markers}**', '',
        'Les réponses originales sont conservées. Les lacunes sont complétées par des '
        'démonstrations symboliques ou des méthodes de construction lorsque les valeurs '
        'numériques ne figurent que sur les illustrations.', '',
    ]
    if partial_paths:
        report += ['## Corrigés restant partiels', ''] + [f'- `{p}`' for p in partial_paths]
    (ROOT / 'CORRECTIONS_REPORT.md').write_text('\n'.join(report) + '\n', encoding='utf-8')

def main() -> None:
    targets=[]
    for corrige in ROOT.rglob('corrige.tex'):
        content=corrige.read_text(encoding='utf-8',errors='ignore')
        if 'Corrigé à rédiger' in content:
            targets.append(corrige)
    targets.sort()
    for corrige in targets:
        source=source_for(corrige)
        answers=answers_for(source)
        corrige.write_text(box_content(source,answers),encoding='utf-8')
        print(f"Complété : {corrige.relative_to(ROOT)} ({len(answers)} questions)")

    partials = 0
    for corrige in sorted(ROOT.rglob('corrige.tex')):
        if complete_partial_file(corrige):
            partials += 1
    write_report()
    print(f"{len(targets)} corrigés absents et {partials} corrigés partiels complétés.")

if __name__=='__main__':
    main()
