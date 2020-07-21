---
layout: home
title: BAYREB project
subtitle: Bayesian inference for building energy performance assessment
---

The BAYREB project belongs to the general field of the energy refurbishment of buildings. It aims at providing decision makers and renovation experts with decision support tools for the renovation process regarding energy efficiency. The project is part of a workflow based on stochastic methods that will support the decision process in a twofold manner:
* Using in situ sensor measurements, aided with Bayesian inference and a prior model of the building, to evaluate its real energy performance, diagnose envelope properties and eventual pathologies, while providing confidence intervals for all inferred data;
* Using the acquired knowledge of the true state of the building, and its uncertainty, as a basis for the elaboration of optimal renovation solutions.


All results of the project have been summarised in [a single report available here](/docs/bayreb_main_report.pdf). More detail regarding specific points have been published in papers, referred below.

## Background literature review on inverse problems and how to solve them

[Main reference available here](http://srouchier.github.io/files/2018-enb-review.pdf)

First, a state of the art of the common practices in building energy performance assessment
was attempted. **Chapter 1** of the monograph, and the paper referred above, reviewed some existing practices for estimating energy performance
indicators from in-situ measurements, and showed that most of them are not applicable in occupied
buildings. The project was indeed motivated by the need for a method that would yield interpretable
performance indicators from a monitored building in normal operating conditions, in order to
provide incentive for refurbishment. Ideally, these indicators should disaggregate the building
performance into separate heat loss terms (transmission through the envelope, windows, thermal
bridges, heat loss from air infiltration...) as to prioritize energy conservation measures. **Chapter 2** then
formalizes the problem and presents the mathematical and numerical tools that were used in the
project. Some elements of model calibration and statistical learning are presented. We especially
emphasize the necessary steps for proper model specification, and for model checking and validation
once optimal parameters have been estimated. A special focus is then made on linear stochastic
state-space models, a category of models used to learn from time-series energy and temperature
readings. The popular RC models belong to this category. All steps of the solving process are
described: model specification, discretization, Kalman filtering, and parameter estimation with
Maximum Likelihood Estimation or Markov Chain Monte Carlo.

## Identifiability, interpretability... testing the limits of building energy performance assessment

Main reference: Sarah Juricic's Ph.D. thesis (link available soon)

The second main part of the report, and the first essential contribution of the project to the state of
the art, is the question of parameter interpretability. Once a numerical model has been trained by
fitting its parameters so that its output best matches observed data, we want to ensure that these
parameters may be interpreted as representative of real physical properties. This question goes
beyond the concept of model identifiability, which asks whether model parameters may be uniquely
estimated from data: we wish to know about physical meaning. **Chapter 3** describes the methodology
of interpretability assessment. It is based on a numerical benchmark: a simulated building in which
all envelope properties (insulation thickness, air change rate, transmission of glazing...) may be
changed. The question is whether variations of the properties of the reference building result in
variations of the expected performance indicators estimated from reduced-order models, and only
the expected indicators. Through sensitivity analysis, we can find the origin of the variance of
estimated parameters, and point out the phenomena that were not appropriately explained by the
reduced-order models. Two applications of the numerical benchmark were then proposed: finding
the minimal monitoring duration so that estimates of the global heat loss coefficient are robust
regarding variable weather conditions; finding whether a minimal set of measurements is enough to
disaggregate heat loss from air infiltration and envelope transmission. Chap. 3 is thus a theoretical
study of the limitations and potential of building energy performance assessment based on in-situ
measurements.

In a nutshell, this part of the work aimed at establishing to what extent stochastic RC models
were able to estimate the thermal performance of a building envelope from weather, indoor
temperatures and heating power designed as to not disturb occupants. The overall thermal resistance
can be robustly estimated from minimally 11 days training data and achieves very satisfactory
interpretability. Finer decomposition of the heat losses has however not been found possible from
poorly informative data. Finally, regardless of the conditions of data collection, the good practice
workflow for meaningful calibration remains valid and in any case necessary for any thermal
characterisation.

## Case studies

Finally, **Chapter 4** illustrates the methods proposed by the project by showing a collection of
independent practical applications. Several methods are illustrated, each of which aims to answer a
question related to building energy performance assessment:
* The energy signature method is used on commercial buildings data. Although this method
is very simple and relies on strong assumptions, it allows a coarse decomposition of energy
use and a comparison of performance before and after energy conservation measures were
applied. [Click here](https://buildingenergygeeks.org/epa_es.html) for a notebook of this case study.
* Ordinary linear regression demonstrates how to easily identify which phenomena have a
significant impact on the energy balance of a building, and which measurements do not need
to be taken into account. [Click here](https://buildingenergygeeks.org/epa_lr.html) for a notebook of this case study.
* Then, the main methodology of the project is demonstrated: using a state-space model,
i.e. a resistor-capacitor network written in stochastic form, to analyse time-series readings
of energy use and temperatures, and estimate physical properties of the building envelope.
The methodology comes with criteria for model checking and validation, which allow some
confidence in the interpretation of results. [Click here](https://buildingenergygeeks.org/ssm_overview.html) for a series of notebooks of this methodology.
* These physically-based state-space model structures can be extended in a hybrid form
called latend force models. LFMs are a state-space model including an uncertain influence
modelled by a temporal Gaussian Process: this is a way to include unobserved phenomena
that may have an impact on the model output, and thus improve its predictive accuracy. GPs
are however non-parametric models that are difficult to relate to physical concepts: the result
is that the estimated parameters of an LFM may not be physically interpretable.
* Online parameter estimation with the Sequential Monte Carlo algorithm is then explained. A
similar RC model structure as in the previous sections is trained sequentially: its parameters
are updated with every new data point, so that the evolution of their posterior distribution can
be seen as a function of the available data. [Click here](http://srouchier.github.io/files/2019-enb-online.pdf) for a paper with further detail.
* Finally, an attempt is made at decomposing the global heat loss coefficient of the
envelope into a heat transfer coefficient, and a separate term for heat loss related to air
infiltration. The method uses more diversified data, such as wind speed and direction and indoor CO2 concentration measurements, in order to
estimate infiltration air flow and the induced heat loss. While results come with a very high
uncertainty, this is considered a promising prospect of the work.
