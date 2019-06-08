# Statistical Analysis and Model in Python

-----

## Modeling Tool 

* [spotpy - A Statistical Parameter Optimization Tool](https://github.com/thouska/spotpy)
	- SPOTPY is a Python framework that enables the use of Computational optimization techniques for calibration, uncertainty and sensitivity analysis techniques of almost every (environmental-) model.

----

## Survival Analysis

* Traditionally, [survival analysis](https://en.wikipedia.org/wiki/Survival_analysis) was developed to measure lifespans of individuals. The analysis can be further applied to not just traditional births and deaths, but any duration.
* **Survival function**: the survival function defines the probability the death event has not occured yet at time t, or equivalently, the probability of surviving past time t
* **Hazard curve**: the probability of the death event occurring at time t, given that the death event has not occurred until time t. Hazard function is non-parametric.
* **Kaplan-Meier estimator for survival function**: Survival analysis assumes that upper limits have the same underlying distribution as the data, and the Kaplan-Meier esti- mator further assumes that detections and upper limits are mutually independent

- [lifelines - implementation of survival analysis in Python](https://lifelines.readthedocs.io/en/latest/)
	* Handles right-censored data.
	* Example of astrophysical usage: [radio SED of high-z SF galaxies](https://arxiv.org/abs/1812.03392)
