# Arborescence des 468 exercices

Ce document liste uniquement les dossiers d'exercices, sans détailler les images, le fichier source et le corrigé contenus dans chaque dossier.

## Comment m'indiquer les modifications

Tu peux me renvoyer une ou plusieurs lignes sous cette forme :

```text
"02-Modélisation des mécanismes/CIN/CIN-01/.../NomExercice" -> "03-Lois entrée sortie/Transmetteurs/NomExercice"
```

Cette syntaxe permet à la fois de déplacer et de renommer un dossier. Le chemin à droite est toujours le chemin final souhaité.

Pour déplacer plusieurs exercices dans le même dossier, indique une ligne par exercice. Pour déplacer un dossier intermédiaire complet, indique le chemin de ce dossier : tous ses sous-dossiers suivront.

Tu peux aussi remplir la colonne `nouveau_chemin` du fichier `RECLASSEMENT_EXERCICES.csv` et me renvoyer seulement les lignes modifiées.

## Arborescence actuelle

```text
├── 01-Ingénierie système
│   ├── A_Integrer
│   │   └── DDS_01
│   │       └── 011_IS
│   └── SYS
│       └── SYS-01
│           ├── SYS-01-ChaineFonctionnelle
│           │   ├── 58_Oz440
│           │   ├── 59_Levage
│           │   └── 60_Escalier
│           ├── SYS-01-ChainePuissance
│           │   ├── 1100_Pneumatique
│           │   ├── 80_Clever
│           │   ├── 88_Suspension
│           │   ├── 89_Bouee
│           │   └── 90_Pilote
│           └── SYS-01_ChaineInfo
│               ├── 507_Divers
│               ├── 50_BancBalafre
│               └── 538_Codeur
├── 02-Modélisation des mécanismes
│   ├── A_Integrer
│   │   ├── DDS_01
│   │   │   └── 020_QCM_Liaisons
│   │   ├── DDS_02
│   │   │   ├── 024_ProduitVectoriel
│   │   │   ├── 036_Cinematique_Schema
│   │   │   └── 042_Chs_Leq
│   │   ├── DDS_03
│   │   │   ├── 043_Geometrie
│   │   │   ├── 045_DerivationVectorielle
│   │   │   ├── 050_Geometrie
│   │   │   └── 057_Geometrie
│   │   ├── DDS_04
│   │   │   ├── 066_Modelisation_Geometrie
│   │   │   ├── 076_Geometrie
│   │   │   └── 079_Geometrie_Verin
│   │   └── DDS_05
│   │       └── 088_Geometrie
│   ├── B2_ProposerModele
│   │   └── B2_16_Hyperstatisme
│   │       ├── 69_TrainA350
│   │       ├── 71_Robovolc_02
│   │       ├── 72_Tripteor
│   │       ├── 81_Piaggio
│   │       ├── 82_MAV
│   │       ├── 83_Roburoc
│   │       └── 84_Nacelle
│   ├── CIN
│   │   └── CIN-01-Parametrage
│   │       ├── 01_T
│   │       ├── 01_T_02
│   │       ├── 02_R
│   │       ├── 02_R_02
│   │       ├── 03_TT
│   │       ├── 03_TT_02
│   │       ├── 04_RR
│   │       ├── 04_RR_02
│   │       ├── 05_RT
│   │       ├── 05_RT_02
│   │       ├── 06_TR
│   │       ├── 06_TR_02
│   │       ├── 07_RR3D
│   │       ├── 07_RR3D_02
│   │       ├── 08_RR3D
│   │       ├── 08_RR3D_02
│   │       ├── 09_RT_RSG
│   │       ├── 1018_BorneReglable
│   │       ├── 1019_RobotPeinture
│   │       ├── 1020_PompeEnsieta
│   │       ├── 1024_ProdVect
│   │       ├── 10_PompePalette
│   │       ├── 11_PompePistonsRadiaux
│   │       ├── 12_BielleManivelle
│   │       ├── 13_TransfoMouvement
│   │       ├── 14_Sympact
│   │       ├── 15_SympactGalet
│   │       ├── 16_Poussoir
│   │       ├── 17_4Barres
│   │       ├── 18_Maxpid
│   │       ├── 46_RR_RSG
│   │       ├── 513_Divers_Tabouret
│   │       └── 514_Divers_Tabouret
│   ├── GEO
│   │   ├── GEO-01
│   │   │   ├── 01_T
│   │   │   ├── 02_R
│   │   │   ├── 03_TT
│   │   │   ├── 04_RR
│   │   │   ├── 05_RT
│   │   │   ├── 06_TR
│   │   │   ├── 07_RR3D
│   │   │   ├── 08_RR3D
│   │   │   ├── 09_RT_RSG
│   │   │   ├── 10_PompePalette
│   │   │   ├── 11_PompePistonsRadiaux
│   │   │   ├── 12_BielleManivelle
│   │   │   ├── 13_TransfoMouvement
│   │   │   ├── 14_Sympact
│   │   │   ├── 15_SympactGalet
│   │   │   ├── 16_Poussoir
│   │   │   ├── 17_4Barres
│   │   │   ├── 18_Maxpid
│   │   │   └── 46_RR_RSG
│   │   └── GEO-03
│   │       ├── 10_PompePalette
│   │       ├── 11_PompePistonsRadiaux
│   │       ├── 12_BielleManivelle
│   │       ├── 13_TransfoMouvement
│   │       ├── 14_Sympact
│   │       ├── 15_SympactGalet
│   │       ├── 16_Poussoir
│   │       ├── 17_4Barres
│   │       ├── 18_Maxpid
│   │       ├── 19_Graham
│   │       ├── 20_VariateurBilles
│   │       ├── 54_FauteuilRoulant
│   │       └── 64_EPAS
│   └── PPM
│       ├── PPM-01
│       │   ├── 1000_Dessin2D
│       │   ├── 1001_Dessin2D
│       │   ├── 1002_Dessin2D
│       │   ├── 1003_Dessin2D
│       │   ├── 1004_Dessin2D
│       │   ├── 1005_Dessin2D
│       │   ├── 1006_Dessin2D
│       │   ├── 1007_Dessin2D
│       │   ├── 1008_Dessin2D
│       │   ├── 1009_Dessin2D
│       │   ├── 1010_Dessin2D
│       │   ├── 1011_Dessin2D
│       │   ├── 1012_Dessin2D
│       │   ├── 1013_Dessin2D
│       │   ├── 1014_Dessin2D
│       │   ├── 1015_Dessin2D
│       │   ├── 1016_Dessin2D
│       │   ├── 1017_Dessin2D
│       │   └── 1020_PompeEnsieta
│       ├── PPM-02
│       │   ├── 1000_Dessin2D
│       │   ├── 2001_BoitierDifferentiel
│       │   ├── 2002_AxeCommande
│       │   ├── 2003_Fourchette
│       │   └── 2004_Secateur
│       └── PPM-03
│           ├── 74_Chariot
│           ├── 75_TrainA380
│           ├── 76_FixationSki
│           ├── 85_FauteuilBateau
│           ├── 86_Moyeu
│           └── 87_Nacelle
├── 03-Lois entrée sortie
│   └── CIN
│       └── CIN-03-Transmetteurs
│           ├── 21_TrainSimple
│           ├── 22_TrainSimple
│           ├── 23_TrainSimple
│           ├── 24_TrainSimple
│           ├── 25_Cheville
│           ├── 26_RoueMotrice
│           ├── 27_TrainEpi
│           ├── 28_TrainEpi
│           ├── 29_TrainEpi
│           ├── 30_TrainEpi
│           ├── 31_Redex
│           ├── 32_Broyeur
│           ├── 33_Centrifugeuse
│           ├── 34_ControlX
│           ├── 35_Vario
│           ├── 36_VisEcrou
│           ├── 37_VisEcrou
│           ├── 38_Treuil
│           ├── 91_PorteAvion
│           ├── 92_Colossus
│           ├── 93_Lokomat
│           └── 94_Taurus
├── 04-Cinématique
│   ├── A_Integrer
│   │   ├── DDS_02
│   │   │   ├── 027_Cinematique
│   │   │   └── 033_Cinematique
│   │   ├── DDS_03
│   │   │   ├── 051_Cinematique
│   │   │   ├── 053_SchemaCinematique
│   │   │   ├── 055_SchemaCinematique
│   │   │   └── 056_SchemaCinematique
│   │   ├── DDS_04
│   │   │   ├── 070_Cinematique
│   │   │   └── 082_Cinematique_TrainEpi
│   │   └── DDS_05
│   │       ├── 085_SchemasCinematique
│   │       └── 087_SchemasCinematique
│   └── CIN
│       └── CIN-02-VitesseAcceleration
│           ├── 01_T
│           ├── 01_T_02
│           ├── 02_R
│           ├── 02_R_02
│           ├── 03_TT
│           ├── 03_TT_02
│           ├── 04_RR
│           ├── 04_RR_02
│           ├── 05_RT
│           ├── 05_RT_02
│           ├── 06_TR
│           ├── 06_TR_02
│           ├── 07_RR3D
│           ├── 07_RR3D_02
│           ├── 08_RR3D
│           ├── 08_RR3D_02
│           ├── 09_RT_RSG
│           ├── 1025_RTR
│           ├── 10_PompePalette
│           ├── 11_PompePistonsRadiaux
│           ├── 12_BielleManivelle
│           ├── 13_TransfoMouvement
│           ├── 14_Sympact
│           ├── 15_SympactGalet
│           ├── 16_Poussoir
│           ├── 17_4Barres
│           ├── 18_Maxpid
│           └── 46_RR_RSG
├── 05-Modélisation Systèmes Asservis
│   ├── A_Integrer
│   │   ├── DDS_01
│   │   │   ├── 002_FTBF_Canonique
│   │   │   ├── 003_ValeurFinale
│   │   │   ├── 004_IdentificationTemporelle
│   │   │   ├── 007_FTBO
│   │   │   ├── 008_Bode
│   │   │   ├── 009_IdentificationBode
│   │   │   ├── 012_Bode
│   │   │   └── 013_FTBO
│   │   ├── DDS_02
│   │   │   ├── 023_Calcul_Complexes
│   │   │   └── 029_SLCI_Stabilite
│   │   ├── DDS_03
│   │   │   ├── 044_SLCI_Calculs
│   │   │   ├── 046_SLCI_Blocs
│   │   │   ├── 049_SLCI_Bode_Retard
│   │   │   ├── 052_SLCI_Demo
│   │   │   └── 060_Bode
│   │   └── DDS_04
│   │       ├── 065_SLCI_Modelisation
│   │       ├── 068_Modelisation
│   │       ├── 069_SLCI_Calcul
│   │       ├── 073_SLCI_Retard
│   │       ├── 075_SLCI_SchemaBlocs
│   │       └── 081_SLCI_Numerique
│   └── SLCI
│       ├── SLCI-02-FT
│       │   └── 51_MCC
│       ├── SLCI-03-SchemaBlocs
│       │   ├── 39_SeineMusicale
│       │   ├── 47_SysReeduc
│       │   ├── 48_Quille
│       │   ├── 500_Divers
│       │   ├── 505_Divers
│       │   ├── 512_Divers
│       │   ├── 51_MCC
│       │   ├── 52_Verin
│       │   ├── 53_BancEpreuveHydraulique
│       │   ├── 71_Robovolc
│       │   ├── 77_ProtheseTibia
│       │   ├── 78_RobotDaVinci
│       │   ├── 79_Tuyere
│       │   ├── 80_Clever
│       │   └── 96_Stabilisateur
│       ├── SLCI-07-Ordre12
│       │   ├── 502_Divers
│       │   ├── 503_Divers
│       │   ├── 504_Divers
│       │   ├── 506_Divers
│       │   ├── 541_Cours
│       │   └── 542_Cours
│       └── SLCI-11-DiagrammeBode
│           ├── 510_01_Divers
│           ├── 510_02_Divers
│           ├── 510_03_Divers
│           ├── 510_04_Divers
│           ├── 510_05_Divers
│           └── 511_Divers
├── 06-Correction des Systèmes asservis
│   ├── A_Integrer
│   │   ├── DDS_02
│   │   │   ├── 022_Stabilite
│   │   │   ├── 025_MargesGraphiques
│   │   │   ├── 026_QCM_PerfSLCI
│   │   │   ├── 030_Correcteur_PI
│   │   │   ├── 031_Correcteur_P
│   │   │   ├── 034_SLCI_Rapidite
│   │   │   └── 035_SLCI_Rapidite
│   │   ├── DDS_04
│   │   │   ├── 072_SLCI_PI
│   │   │   ├── 077_SLCI_PI
│   │   │   ├── 080_CorrecteurP
│   │   │   ├── 083_SchemaBlocs_FT
│   │   │   └── 084_SLCI_P
│   │   └── DDS_05
│   │       └── 086_Correcteur_Clever
│   ├── COR
│   │   ├── COR-02-P
│   │   │   └── 65_Eclipse
│   │   ├── COR-03-PI
│   │   │   ├── 64_EPAS
│   │   │   ├── 65_Eclipse_02
│   │   │   ├── 66_Micromanipulateur
│   │   │   ├── 67_PompeTurbo
│   │   │   ├── 68_Roburoc
│   │   │   └── 70_Hublex
│   │   └── COR-04-AP
│   │       └── 65_Eclipse_03
│   └── PERF
│       ├── PERF-02-Marges
│       │   ├── 61_Hemostase
│       │   ├── 62_Palettisation
│       │   ├── 63_BancHydraulique
│       │   └── 64_EPAS
│       ├── PERF-05-Precistion-TVF
│       │   ├── 501_Divers
│       │   └── 509_Divers
│       └── PERF-06-Precision
│           ├── 63_BancHydraulique
│           ├── 64_EPAS
│           └── 73_Bassin
├── 07-Électronique
│   └── ELEC
│       ├── ELEC-01
│       │   ├── 534_CircuitElec
│       │   ├── 535_CircuitElec
│       │   ├── 536_CircuitElec
│       │   ├── 537_CircuitElec
│       │   └── 538_CircuitElec
│       └── ELEC-05-MA
│           └── 50_BancBalafre
├── 08-Électromécanique
│   └── A_Integrer
│       └── DDS_04
│           └── 078_Modelisation
├── 09-MCC
│   ├── A_Integrer
│   │   └── DDS_04
│   │       └── 067_Modelisation_SchemaBlocs
│   └── ELEC
│       └── ELEC-04-MCC
│           └── 1023_MCC
├── 11-Actions Mécaniques
│   ├── A_Integrer
│   │   ├── DDS_01
│   │   │   ├── 016_PFS
│   │   │   └── 021_QCM_PFS
│   │   ├── DDS_02
│   │   │   ├── 032_Statiques_AM
│   │   │   └── 041_Statique_PFS
│   │   ├── DDS_03
│   │   │   ├── 048_PFS
│   │   │   └── 058_PFS
│   │   ├── DDS_04
│   │   │   └── 071_PFS
│   │   ├── DDS_05
│   │   │   ├── 089_PFD_RobotChirurgical
│   │   │   ├── 090_Inertie
│   │   │   ├── 092_TorseursDyn_Orthese
│   │   │   ├── 093_PFD
│   │   │   ├── 095_Stat
│   │   │   └── 096_Stat
│   │   └── DDS_Reserve
│   │       ├── 982_TEC
│   │       ├── 985_Hyperstatisme
│   │       └── 999_TEC_Clever
│   ├── C2_MettreEnOeuvreDemarche
│   │   └── C2_07_PFS
│   │       ├── 515_Divers_Potence
│   │       └── 56_RobotAvion
│   ├── DYN
│   │   ├── DYN-01
│   │   │   ├── 01_T
│   │   │   ├── 02_R
│   │   │   ├── 14_Sympact
│   │   │   ├── 61_Hemostase
│   │   │   ├── 61_Hemostase_02
│   │   │   └── 63_BancHydraulique
│   │   ├── DYN-03-Inertie
│   │   │   ├── 1026_Pale
│   │   │   ├── 40_Parallelepipede
│   │   │   ├── 41_Parallelepipede
│   │   │   ├── 42_Cylindre
│   │   │   ├── 43_Cylindre
│   │   │   ├── 44_Disque
│   │   │   ├── 45_Disque
│   │   │   ├── 50_BancBalafre
│   │   │   ├── 64_EPAS
│   │   │   └── 65_Eclipse
│   │   ├── DYN-04-TorseurDynamique
│   │   │   ├── 01_T
│   │   │   ├── 01_T_02
│   │   │   ├── 02_R
│   │   │   ├── 03_TT
│   │   │   ├── 04_RR
│   │   │   ├── 05_RT
│   │   │   ├── 06_TR
│   │   │   ├── 07_RR3D
│   │   │   ├── 08_RR3D
│   │   │   ├── 09_RT_RSG
│   │   │   ├── 1025_RTR
│   │   │   ├── 46_RR_RSG
│   │   │   ├── 50_BancBalafre
│   │   │   ├── 64_EPAS
│   │   │   ├── Cours
│   │   │   └── STOCK
│   │   │       ├── 02_R_02
│   │   │       ├── 03_TT_02
│   │   │       ├── 04_RR_02
│   │   │       ├── 05_RT_02
│   │   │       ├── 06_TR_02
│   │   │       ├── 07_RR3D_02
│   │   │       ├── 08_RR3D_02
│   │   │       ├── 10_PompePalette
│   │   │       ├── 11_PompePistonsRadiaux
│   │   │       ├── 12_BielleManivelle
│   │   │       ├── 13_TransfoMouvement
│   │   │       ├── 14_Sympact
│   │   │       ├── 15_SympactGalet
│   │   │       ├── 16_Poussoir
│   │   │       ├── 17_4Barres
│   │   │       └── 18_Maxpid
│   │   ├── DYN-05-Methode
│   │   │   ├── 01_T
│   │   │   ├── 02_R
│   │   │   ├── 03_TT
│   │   │   ├── 04_RR
│   │   │   ├── 05_RT
│   │   │   ├── 06_TR
│   │   │   ├── 07_RR3D
│   │   │   ├── 08_RR3D
│   │   │   ├── 09_RT_RSG
│   │   │   ├── 46_RR_RSG
│   │   │   └── STOCK
│   │   │       ├── 01_T_02
│   │   │       ├── 02_R_02
│   │   │       ├── 03_TT_02
│   │   │       ├── 04_RR_02
│   │   │       ├── 05_RT_02
│   │   │       ├── 06_TR_02
│   │   │       ├── 07_RR3D_02
│   │   │       └── 08_RR3D_02
│   │   └── DYN-06-PFD
│   │       ├── 01_T
│   │       ├── 02_R
│   │       ├── 03_TT
│   │       ├── 04_RR
│   │       ├── 05_RT
│   │       ├── 06_TR
│   │       ├── 07_RR3D
│   │       ├── 08_RR3D
│   │       ├── 09_RT_RSG
│   │       ├── 46_RR_RSG
│   │       ├── 50_BancBalafre
│   │       └── STOCK
│   │           ├── 01_T_02
│   │           ├── 02_R_02
│   │           ├── 03_TT_02
│   │           ├── 04_RR_02
│   │           ├── 05_RT_02
│   │           ├── 06_TR_02
│   │           ├── 07_RR3D_02
│   │           └── 08_RR3D_02
│   ├── STAT
│   │   ├── STAT-02-Frottement
│   │   │   ├── 532_MAM_Frottement_Cylindre
│   │   │   └── 533_MAM_Frottement_Cylindre
│   │   ├── STAT-02-Global
│   │   │   ├── 516_MAM
│   │   │   ├── 517_MAM
│   │   │   ├── 518_MAM
│   │   │   ├── 519_MAM
│   │   │   ├── 520_MAM
│   │   │   └── 521_MAM
│   │   ├── STAT-02-Local
│   │   │   ├── 1023_Vilebrequin
│   │   │   ├── 1024_Balancier
│   │   │   ├── 1025_Palier
│   │   │   ├── 39_SeineMusicale
│   │   │   └── 50_BancBalafre
│   │   └── STAT-03-Demarche
│   │       ├── 01_T
│   │       ├── 02_R
│   │       ├── 03_TT
│   │       ├── 04_RR
│   │       ├── 05_RT
│   │       ├── 06_TR
│   │       ├── 07_RR3D
│   │       ├── 08_RR3D
│   │       ├── 14_Sympact
│   │       ├── 55_Suspension
│   │       ├── 57_PeseCamion
│   │       ├── 95_ChasseNeige
│   │       └── STOCK
│   │           ├── 01_T_02
│   │           ├── 02_R_02
│   │           ├── 03_TT_02
│   │           ├── 04_RR_02
│   │           ├── 05_RT_02
│   │           ├── 06_TR_02
│   │           ├── 07_RR3D_02
│   │           ├── 08_RR3D_02
│   │           └── 09_RT_RSG
│   └── TEC
│       ├── TEC-04-Meq-Jeq
│       │   ├── 21_TrainSimple
│       │   ├── 22_TrainSimple
│       │   ├── 23_TrainSimple
│       │   ├── 24_TrainSimple
│       │   ├── 25_Cheville
│       │   ├── 26_RoueMotrice
│       │   ├── 27_TrainEpi
│       │   ├── 28_TrainEpi
│       │   ├── 29_TrainEpi
│       │   ├── 30_TrainEpi
│       │   ├── 31_Redex
│       │   ├── 32_Broyeur
│       │   ├── 33_Centrifugeuse
│       │   ├── 34_ControlX
│       │   ├── 35_Vario
│       │   ├── 36_VisEcrou
│       │   ├── 37_VisEcrou
│       │   ├── 38_Treuil
│       │   ├── 91_PorteAvion
│       │   ├── 92_Colossus
│       │   ├── 93_Lokomat
│       │   └── 94_Taurus
│       └── TEC-05
│           ├── 10_PompePalette
│           ├── 11_PompePistonsRadiaux
│           ├── 12_BielleManivelle
│           ├── 13_TransfoMouvement
│           ├── 14_Sympact
│           ├── 15_SympactGalet
│           ├── 16_Poussoir
│           ├── 17_4Barres
│           ├── 18_Maxpid
│           ├── 19_Graham
│           ├── 20_VariateurBilles
│           ├── 49_ElevateurBateaux
│           ├── 50_BancBalafre
│           └── 64_EPAS
├── 12-RDM
│   └── RDM
│       ├── RDM-01-Cohesion
│       │   ├── 522_RdM
│       │   ├── 523_RdM
│       │   ├── 524_RdM
│       │   ├── 525_RdM
│       │   ├── 526_RdM
│       │   ├── 527_RdM
│       │   ├── 528_BrocheFraisage
│       │   ├── 529_Passerelle
│       │   └── 530_BancHelico
│       ├── RDM-02-Traction
│       │   └── 539_Cours_RDM
│       ├── RDM-03-Torsion
│       │   └── 539_Cours_RDM
│       ├── RDM-04-Flexion
│       │   └── 539_Cours_RDM
│       └── RDM-05-Deformation
│           ├── 531_RdM
│           ├── 532_RdM
│           ├── 540_RdM
│           ├── 541_RdM
│           └── 542_RdM
├── 14-Logique
│   ├── A_Integrer
│   │   └── DDS_03
│   │       └── 059_STM
│   └── SEQ
│       └── SEQ-03
│           └── 50_BancBalafre
└── 15-Outils numériques
    └── NUM
        └── NUM-03
            ├── 1021_Euler
            ├── 1022_Euler
            └── 1023_Euler
```
