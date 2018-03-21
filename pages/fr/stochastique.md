---
title: "Modélisation stochastique"
summary: "Comment prendre en compte les erreurs de mesure et de modélisation en résolvant l'estimation de paramètres"
permalink: stochastique.html
keywords: bayreb, anr
sidebar: sidebar_fr
topnav: topnav_fr
toc: true
---

Dans la plupart des cas, le problème inverse de caractérisation par mesures in situ est réalisé sous l’hypothèse d’un modèle non biaisé, c’est-à-dire qu’on suppose capable de reproduire fidèlement la réalité. Cette hypothèse est toujours fausse, particulièrement pour les modèles RC très simples utilisés par les inverseurs. La prise en compte des (nombreuses) erreurs et approximations de modélisation est indispensable à la légitimité des modèles calibrés et à l’interprétabilité de leurs paramètres.

Une solution possible à ce problème est l'utilisation de modèles stochastiques. Ceux-ci permettent d'inclure un terme d'erreur de système représentant les approximations du modèle par rapport à la réalité : on a alors affaire à des équations différentielles stochastiques (SDE). D'après la littérature, les modèles stochastiques permettent des résultats plus reproductibles, plus prudents et plus réalistes vis-à-vis de l'information réellement contenue dans la mesure.

Dans le cadre du projet BAYREB a été réalisée une étude quantifiant cet effet, par rapport à la modélisation déterministe standard. On y a constaté que l’utilisation d’un modèle stochastique augmente considérablement l'incertitude sur les valeurs estimées des caractéristiques du bâtiment, mais que cette estimation est par conséquent plus robuste et plus fiable.

<img src="images/fig_hlc_det.png" style="width: 600px;">

<img src="images/fig_hlc_sto.png" style="width: 600px;">

Ce travail a donné lieu à un article publié dans la revue *Building and Environment*:

[Rouchier S, Rabouille M, Oberlé P (2018) Calibration of simplified building energy models for parameter estimation and forecasting: stochastic versus deterministic modelling. Building and Environment, vol. 134, p. 181-190](https://www.sciencedirect.com/science/article/pii/S036013231830115X)
