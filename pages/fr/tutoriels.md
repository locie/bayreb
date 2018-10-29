---
title: "Tutoriels"
summary: "Exemples de code pour appliquer les méthodes du projet"
permalink: tutoriels.html
keywords: bayreb, anr
sidebar: sidebar_fr
topnav: topnav_fr
toc: true
---

Afin de rendre accessibles et reproductibles les avancées du projet BAYREB, des extraits de code Python utilisés dans chacune de ses parties sont fournies ici sous la forme de notebooks Jupyter. Vous pouvez les visualiser en ligne, ou en télécharger le code à partir du [dépôt Github](https://github.com/locie/bayreb) lié à cette page.

## Introduction aux problèmes inverses en transferts thermiques

Trois tutoriels qui ont été réalisés en marge du projet BAYREB, en guise d'introduction aux problèmes inverses.

* [Identification de la conductivité thermique d'un mur par inférence Bayésienne](https://nbviewer.jupyter.org/github/locie/bayreb/blob/master/Notebooks/01_HeatConductivity/Notebook_HeatConductivity.ipynb). Cet exercice offre une introduction à la librairie PyMC qui est beaucoup utilisée dans le reste du projet.
* [Conduction thermique inverse: reconstruire un flux de chaleur à partir d'une mesure de température](https://nbviewer.jupyter.org/github/locie/bayreb/blob/master/Notebooks/02_HeatFlow/Notebook_HeatFlow.ipynb). C'est un problème standard d'inversion, où on cherche à reconstruire une fonction évoluant dans le temps dans un problème inverse mal posé.
* [Transferts d'humidité: identifier les propriétés hygriques d'une éprouvette en mesurant sa masse et son humidité relative](https://nbviewer.jupyter.org/github/locie/bayreb/blob/master/Notebooks/03_MoistureTransfer/Notebook_MoistureTransfer.ipynb)


## Identification d'un modèle 2R2C déterministe

Deux tutoriels qui viennent en support de [l'article *review* publié dans Energy and Buildings](https://www.sciencedirect.com/science/article/pii/S0378778817317942)

* [Least-square estimation](https://nbviewer.jupyter.org/github/locie/bayreb/blob/master/Notebooks/04_2R2C_LSE/2R2C%20model%20parameter%20estimation.ipynb): exemple très simple montrant comment identifier un modèle RC avec des données de mesure en bâtiment.
* [Sensitivity analysis and likelihood-based confidence regions](https://nbviewer.jupyter.org/github/locie/bayreb/blob/master/Notebooks/04_2R2C_LSE/2R2C%20model%20sensitivity%20and%20identifiability.ipynb): quelques exemples de l'estimation de l'identifiabilité pratique des modèles RC.

## Identification d'un modèle 2R2C stochastique avec MCMC et un filtre de Kalman

Ce tutoriel montre le code utilisé pour illustrer l'importance de l'erreur de modélisation dans l'estimation de paramètres. L'article qui décrit la méthodologie en détail est [téléchargeable ici](https://hal.archives-ouvertes.fr/hal-01739625).

* [RC model calibration: stochastic versus deterministic modelling](https://nbviewer.jupyter.org/github/locie/bayreb/blob/master/Notebooks/05_2R2C_stochastic/Stochastic%20RC%20model.ipynb)

## Estimation de paramètres en temps réel

Cette section sera bientôt renseignée.
