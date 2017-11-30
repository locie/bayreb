---
title: "Contexte et objectifs du projet BAYREB"
summary: "Le projet ANR BAYREB vise à proposer une méthode de diagnostic énergétique des bâtiments avant leur réhabilitation"
permalink: objectifs.html
keywords: bayreb, anr
sidebar: sidebar_fr
topnav: topnav_fr
toc: true
---

## Enjeux

Le plus important gisement d’économies d’énergies dans le secteur du bâtiment se trouve dans
la rénovation de l’existant. En conséquence, de nombreux travaux sont dédiés à la recherche de
moyens d’encourager la décision. Une garantie de performance après rénovation peut constituer
une incitation intéressante, mais est difficile à réaliser en pratique. Une condition nécessaire
pour une rénovation rentable est de proposer des solutions adaptées à chaque cas. Cela
nécessite la réalisation d’un diagnostic préalable, permettant d’identifier les faiblesses de chaque
bâtiment : par exemple en quantifiant la part de consommation d’énergie due aux infiltrations
d’air, au transfert par l’enveloppe, par un système de chauffage peu efficace... Pour un tel
diagnostic détaillé, on peut recourir aux méthodes inverses qui permettraient de construire une
représentation réaliste d’un bâtiment sur la base de mesures in situ.

## Objectifs

Le but du projet BAYREB est d'utiliser des mesures réalisées dans un bâtiment (température, humidité, $$CO_2$$) pour acquérir la connaissance justifiant du choix de la solution de réhabilitation qui lui sera la plus adaptée. La caractérisation des propriétés de l'enveloppe via une instrumentation in situ est déjà proposée par les méthodes de co-heating et celles qui en sont inspirées (QUB, ISABELE). Ces méthodes ne sont cependant par applicables au diagnostic pré-rénovation car :

* Leur protocole expérimental n'est pas réalisable dans des locaux occupés.
* Leurs résultats sont trop agrégés pour évaluer les effets de différentes solutions de rénovation.

Le défi du projet BAYREB est donc double. Premièrement, le comportement du bâtiment doit être suivi dans ses conditions d'utilisation normales, sans conditions aux limites imposées, et mesurées avec des capteurs de type et de précision limitées. Cela entraîne potentiellement de fortes incertitudes de mesure et des jeux de données moins riches. Deuxièmement, cette mesure doit permettre de **désagréger** les différentes sources de déperditions thermiques dans un modèle du bâtiment, afin de permettre la décision de rénovation. Le modèle calibré par le problème inverse de caractérisation in situ doit donc obéir à un niveau de détail suffisant.

## Positionnement

En raison des défis énoncés ci-dessus, le projet BAYREB met l'accent sur la prise en compte de toutes les possibles sources d'erreur dans la résolution du problème inverse : erreurs de mesure, erreurs d'hypothèse des modèles et de résolution du problème direct. Le projet repose sur le choix spécifique du cadre des statistiques Bayésiennes pour traduire toutes ces incertitudes dans les estimations de paramètres.

Si la méthode est maîtrisée, les intervalles de confiance d'un paramètre traduisent alors la meilleure connaissance du bâtiment que la mesure peut en offrir : une propriété ne sera pas déclarée correctement estimée si les mesures sont insuffisantes pour cela.
