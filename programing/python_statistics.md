# Statistical Analysis and Model in Python

## Error Propagation

* [__astropy.uncertainty__](http://docs.astropy.org/en/stable/uncertainty/)
	- Provides a __Distribution__ object to represent statistical distributions in a form that acts as a drop-in replacement for __Quantity__ or a regular __numpy.ndarray__. Still work in progress.

* [__uncertainties__ - Transparent calculations with uncertainties on the quantities involved](https://github.com/lebigot/uncertainties)
	- The __uncertainties__ package is a free, cross-platform program that transparently handles calculations with numbers with uncertainties (like 3.14±0.01). It can also yield the derivatives of any expression.

## Modeling Tool

* [__spotpy__ - A Statistical Parameter Optimization Tool](https://github.com/thouska/spotpy)
	- SPOTPY is a Python framework that enables the use of Computational optimization techniques for calibration, uncertainty and sensitivity analysis techniques of almost every (environmental-) model.

* [__BayesianOptimization__ - A Python implementation of global optimization with gaussian processes](https://github.com/fmfn/BayesianOptimization)
	- This is a constrained global optimization package built upon bayesian inference and gaussian process, that attempts to find the maximum value of an unknown function in as few iterations as possible.

## Sampling Tools and Bayesian Analysis

* [__emcee__ - The Python ensemble sampling toolkit for affine-invariant MCMC](https://github.com/dfm/emcee)
	- By Dan Foreman-Mackey. __emcee__ is a stable, well tested Python implementation of the affine-invariant ensemble sampler for Markov chain Monte Carlo (MCMC) proposed by Goodman & Weare (2010).

* [__dynesty__ - Dynamic Nested Sampling package for computing Bayesian posteriors and evidences](https://github.com/joshspeagle/dynesty)
	- By [Josh Speagle](https://joshspeagle.github.io/). A Dynamic Nested Sampling package for computing Bayesian posteriors and evidences. Pure Python.

* [__nestle__ - Pure Python, MIT-licensed implementation of nested sampling algorithms for evaluating Bayesian evidence](https://github.com/kbarbary/nestle)
	- By [Kyle Barbary](http://kylebarbary.com/)

* [__nnest__ - Neural network accelerated nested and MCMC sampling](https://github.com/adammoss/nnest)
	- By Adam Moss. Based on [this paper](https://arxiv.org/abs/1903.10860)

* [__sampyl__ - MCMC samplers for Bayesian estimation in Python, including Metropolis-Hastings, NUTS, and Slice](https://github.com/mcleonard/sampyl)
	- __Sampyl__ is a package for sampling from probability distributions using MCMC methods. Similar to __PyMC3__ using theano to compute gradients, Sampyl uses autograd to compute gradients.

* [__PyMC3__ - Probabilistic Programming in Python: Bayesian Modeling and Probabilistic Machine Learning with Theano](https://github.com/pymc-devs/pymc3)
	- __PyMC3__ is a Python package for Bayesian statistical modeling and Probabilistic Machine Learning focusing on advanced Markov chain Monte Carlo (MCMC) and variational inference (VI) algorithms. Its flexibility and extensibility make it applicable to a large suite of problems.
	- [Getting started with PyMC3](https://docs.pymc.io/notebooks/getting_started) and the [Example Notebooks](https://docs.pymc.io/nb_examples/index.html) are good places to get started.
* [__PyMC4__ - A high-level probabilistic programming interface for TensorFlow Probability](https://github.com/pymc-devs/pymc4)

## Gaussian Process

* A full introduction to the theory of Gaussian Processes is available for free online: [Rasmussen & Williams (2006)](http://www.gaussianprocess.org/gpml/).
* [An Astronomer's Introduction to Gaussian Processes](https://astrostatistics.psu.edu/su14/lectures/penn-gp.pdf)
	- Very good introduction by Dan Foreman-Mackey.

* [__sklearn.gaussian_process__ - The Gaussian Processes module in __scikit-learn__](https://scikit-learn.org/stable/modules/gaussian_process.html)

* [__GPy__ - Gaussian processes framework in python](https://github.com/sheffieldml/gpy)
	- Gaussian processes underpin range of modern machine learning algorithms. In [__GPy__](http://sheffieldml.github.io/GPy/), we've used python to implement a range of machine learning algorithms based on GPs. [Online document is here](https://gpy.readthedocs.io/en/deploy/) 
	- [Jupyter notebooks to introduce __GPy__](https://nbviewer.jupyter.org/github/SheffieldML/notebook/blob/master/GPy/index.ipynb)

* [__gpflow__ - Gaussian processes in TensorFlow](https://github.com/GPflow/GPflow)
	- __GPflow__ is a package for building Gaussian process models in python, using __TensorFlow__.
	- __GPflow__ implements modern Gaussian process inference for composable kernels and likelihoods.
	- __GPflow__ uses TensorFlow for running computations, which allows fast execution on GPUs, and uses Python 3.5 or above.
	- [Online document is here](https://gpflow.readthedocs.io/en/develop/)

* [__gpytorch__ - A highly efficient and modular implementation of Gaussian Processes in PyTorch](https://github.com/cornellius-gp/gpytorch)
	- __GPyTorch__ is a Gaussian process library implemented using __PyTorch__. __GPyTorch__ is designed for creating scalable, flexible, and modular Gaussian process models with ease.

* [__george__ - Fast and flexible Gaussian Process regression in Python](https://github.com/dfm/george)
	- By Dan Foreman-Mackey. __George__ is a fast and flexible Python library for Gaussian Process (GP) Regression.
	- Unlike some other GP implementations, __george__ is focused on efficiently evaluating the marginalized likelihood of a dataset under a GP prior, even as this dataset gets Big
	- Example applications:
		* [__ART__ - A Reconstruction Tool](https://github.com/tmcclintock/AReconstructionTool)
		* [__everest__ - De-trending of K2 Light curves](https://github.com/rodluger/everest)

* [__celerite__ - Scalable 1D Gaussian Processes in C++, Python, and Julia](https://github.com/dfm/celerite)
	- By Dan Foreman-Mackey. [Online document is here](https://celerite.readthedocs.io/en/stable/) 
	- Based on [Fast and scalable Gaussian process modeling with applications to astronomical time series](https://arxiv.org/abs/1703.09710)

## Survival Analysis

* Traditionally, [survival analysis](https://en.wikipedia.org/wiki/Survival_analysis) was developed to measure lifespans of individuals. The analysis can be further applied to not just traditional births and deaths, but any duration.
* **Survival function**: the survival function defines the probability the death event has not occured yet at time t, or equivalently, the probability of surviving past time t
* **Hazard curve**: the probability of the death event occurring at time t, given that the death event has not occurred until time t. Hazard function is non-parametric.
* **Kaplan-Meier estimator for survival function**: Survival analysis assumes that upper limits have the same underlying distribution as the data, and the Kaplan-Meier esti- mator further assumes that detections and upper limits are mutually independent

- [__lifelines__ - implementation of survival analysis in Python](https://lifelines.readthedocs.io/en/latest/)
	* Handles right-censored data.
	* Example of astrophysical usage: [radio SED of high-z SF galaxies](https://arxiv.org/abs/1812.03392)
