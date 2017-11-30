---
title: "Méthodologie"
summary: "Les étapes du travail réalisé pour répondre aux objectifs du projet"
permalink: methodologie.html
keywords: bayreb, anr
sidebar: sidebar_fr
topnav: topnav_fr
toc: true
---

Afin de remplir ses [objectifs](projet.html), le projet doit aborder les verrous scientifiques et techniques suivants. Les résultats seront présentés sur ce site web selon la même structure.

## Identifiabilité des modèles de bâtiments

Le projet met particulièrement l'accent sur l'**identifiabilité** des paramètres, la **richesse d'information** contenue dans la mesure.

L'identifiabilité est la faisabilité de l'estimation d'un paramètre de modèle, sur la base d'une série de mesures données. Une condition nécessaire pour l'identifiabilité est que la structure même du modèle permette cette estimation : on parle d'identifiabilité structurelle. Ensuite, il est nécessaire que les mesures servant à l'apprentissage soient assez riches et informatives : on parle d'identifiabilité pratique.

Le projet BAYREB a besoin de structures de modèles permettant la désagrégation des consommations d'un bâtiment en vue de sa réhabilitation, mais qui doivent être suffisamment simplifiés pour permettre l'identifiabilité de leurs paramètres. Concilier ces deux exigences contradictoires est le principal défi du projet.

[Lien vers la page des résultats](identifiabilite.html)

## Modélisation stochastique

Dans la plupart des cas, les problèmes d'estimation de paramètres sont résolus sous l’hypothèse d’un modèle non biaisé, c’est-à-dire qu’on suppose capable de reproduire fidèlement la réalité. Cette hypothèse est toujours fausse, particulièrement pour les modèles RC très simples utilisés par les inverseurs. La prise en compte des (nombreuses) erreurs et approximations de modélisation est indispensable à la légitimité des modèles calibrés et à l’interprétabilité de leurs paramètres. Un des moyens possibles pour inclure ces erreurs dans la formulation du problème est l’utilisation d’équations différentielles stochastiques, résolues via un filtre de Kalman et l'algorithme d'inférence Bayésienne MCMC.

[Lien vers la page des résultats](stochastique.html)

## Caractérisation en temps réel

L'estimation de paramètres est une opération généralement "hors-ligne" : un modèle est calibré sur la base d'une série complète de données servant d'apprentissage. En conséquence, il peut être difficile d'identifier précisément quelle partie de la séquence expérimentale a apporté la plus grande richesse d'information au modèle.

Une alternative à l'estimation hors-ligne est la caractérisation en temps réel : chaque paramètre est décrit par une fonction de probabilité qui est mise à jour à chaque fois qu'un nouveau point de mesure est disponible. Cela permet de tirer les enseignements de l'expérience pendant qu'elle a lieu, donc de constater précisément quels phénomènes influent sur les estimateurs. Par ce moyen, on peut également imaginer interrompre la mesure dès que l'apprentissage est jugé satisfaisant.

[Lien vers la page des résultats](tempsreel.html)

## Réseau de capteurs sans fils

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
