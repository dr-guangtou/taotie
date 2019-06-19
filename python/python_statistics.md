# Statistical Analysis and Model in Python

-----

## Modeling Tool

* [spotpy - A Statistical Parameter Optimization Tool](https://github.com/thouska/spotpy)
	- SPOTPY is a Python framework that enables the use of Computational optimization techniques for calibration, uncertainty and sensitivity analysis techniques of almost every (environmental-) model.

## Sampling Tools and Bayesian Analysis

* [emcee - The Python ensemble sampling toolkit for affine-invariant MCMC](https://github.com/dfm/emcee)
	- By Dan Foreman-Mackey. `emcee` is a stable, well tested Python implementation of the affine-invariant ensemble sampler for Markov chain Monte Carlo (MCMC) proposed by Goodman & Weare (2010).
* [dynesty - Dynamic Nested Sampling package for computing Bayesian posteriors and evidences](https://github.com/joshspeagle/dynesty)
	- By [Josh Speagle](https://joshspeagle.github.io/). A Dynamic Nested Sampling package for computing Bayesian posteriors and evidences. Pure Python.
* [nestle - Pure Python, MIT-licensed implementation of nested sampling algorithms for evaluating Bayesian evidence](https://github.com/kbarbary/nestle)
	- By [Kyle Barbary](http://kylebarbary.com/)
* [nnest - Neural network accelerated nested and MCMC sampling](https://github.com/adammoss/nnest)
	- By Adam Moss. Based on [this paper](https://arxiv.org/abs/1903.10860)

## Survival Analysis

* Traditionally, [survival analysis](https://en.wikipedia.org/wiki/Survival_analysis) was developed to measure lifespans of individuals. The analysis can be further applied to not just traditional births and deaths, but any duration.
* **Survival function**: the survival function defines the probability the death event has not occured yet at time t, or equivalently, the probability of surviving past time t
* **Hazard curve**: the probability of the death event occurring at time t, given that the death event has not occurred until time t. Hazard function is non-parametric.
* **Kaplan-Meier estimator for survival function**: Survival analysis assumes that upper limits have the same underlying distribution as the data, and the Kaplan-Meier esti- mator further assumes that detections and upper limits are mutually independent

- [lifelines - implementation of survival analysis in Python](https://lifelines.readthedocs.io/en/latest/)
	* Handles right-censored data.
	* Example of astrophysical usage: [radio SED of high-z SF galaxies](https://arxiv.org/abs/1812.03392)
