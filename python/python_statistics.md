# Statistical Analysis and Model in Python

-----

## Error Propagation

* [`astropy.uncertainty`]()
	- Provides a `Distribution` object to represent statistical distributions in a form that acts as a drop-in replacement for `Quantity` or a regular `numpy.ndarray`. Still work in progress.

* [`uncertainties` - Transparent calculations with uncertainties on the quantities involved](https://github.com/lebigot/uncertainties)
	- The `uncertainties` package is a free, cross-platform program that transparently handles calculations with numbers with uncertainties (like 3.14±0.01). It can also yield the derivatives of any expression.

## Modeling Tool

* [`spotpy` - A Statistical Parameter Optimization Tool](https://github.com/thouska/spotpy)
	- SPOTPY is a Python framework that enables the use of Computational optimization techniques for calibration, uncertainty and sensitivity analysis techniques of almost every (environmental-) model.

* [`BayesianOptimization` - A Python implementation of global optimization with gaussian processes](https://github.com/fmfn/BayesianOptimization)
	- This is a constrained global optimization package built upon bayesian inference and gaussian process, that attempts to find the maximum value of an unknown function in as few iterations as possible.

## Sampling Tools and Bayesian Analysis

* [`emcee` - The Python ensemble sampling toolkit for affine-invariant MCMC](https://github.com/dfm/emcee)
	- By Dan Foreman-Mackey. `emcee` is a stable, well tested Python implementation of the affine-invariant ensemble sampler for Markov chain Monte Carlo (MCMC) proposed by Goodman & Weare (2010).
* [`dynesty` - Dynamic Nested Sampling package for computing Bayesian posteriors and evidences](https://github.com/joshspeagle/dynesty)
	- By [Josh Speagle](https://joshspeagle.github.io/). A Dynamic Nested Sampling package for computing Bayesian posteriors and evidences. Pure Python.
* [`nestle` - Pure Python, MIT-licensed implementation of nested sampling algorithms for evaluating Bayesian evidence](https://github.com/kbarbary/nestle)
	- By [Kyle Barbary](http://kylebarbary.com/)
* [`nnest` - Neural network accelerated nested and MCMC sampling](https://github.com/adammoss/nnest)
	- By Adam Moss. Based on [this paper](https://arxiv.org/abs/1903.10860)

## Gaussian Process

* A full introduction to the theory of Gaussian Processes is available for free online: [Rasmussen & Williams (2006)](http://www.gaussianprocess.org/gpml/).
* [An Astronomer's Introduction to Gaussian Processes](https://astrostatistics.psu.edu/su14/lectures/penn-gp.pdf)
	- Very good introduction by Dan Foreman-Mackey.

* [`sklearn.gaussian_process` - The Gaussian Processes module in `scikit-learn`](https://scikit-learn.org/stable/modules/gaussian_process.html)

* [`GPy` - Gaussian processes framework in python](https://github.com/sheffieldml/gpy)
	- Gaussian processes underpin range of modern machine learning algorithms. In [`GPy`](http://sheffieldml.github.io/GPy/), we've used python to implement a range of machine learning algorithms based on GPs. [Online document is here](https://gpy.readthedocs.io/en/deploy/) 
	- [Jupyter notebooks to introduce `GPy`](https://nbviewer.jupyter.org/github/SheffieldML/notebook/blob/master/GPy/index.ipynb)

* [`gpflow` - Gaussian processes in TensorFlow](https://github.com/GPflow/GPflow)
	- `GPflow` is a package for building Gaussian process models in python, using `TensorFlow`.
	- `GPflow` implements modern Gaussian process inference for composable kernels and likelihoods.
	- `GPflow` uses TensorFlow for running computations, which allows fast execution on GPUs, and uses Python 3.5 or above.
	- [Online document is here](https://gpflow.readthedocs.io/en/develop/)

* [`gpytorch` - A highly efficient and modular implementation of Gaussian Processes in PyTorch](https://github.com/cornellius-gp/gpytorch)
	- `GPyTorch` is a Gaussian process library implemented using `PyTorch`. `GPyTorch` is designed for creating scalable, flexible, and modular Gaussian process models with ease.

* [`george` - Fast and flexible Gaussian Process regression in Python](https://github.com/dfm/george)
	- By Dan Foreman-Mackey. `George` is a fast and flexible Python library for Gaussian Process (GP) Regression.
	- Unlike some other GP implementations, `george` is focused on efficiently evaluating the marginalized likelihood of a dataset under a GP prior, even as this dataset gets Big
	- Example applications:
		* [`ART` - A Reconstruction Tool](https://github.com/tmcclintock/AReconstructionTool)
		* [`everest` - De-trending of K2 Light curves](https://github.com/rodluger/everest)

* [`celerite` - Scalable 1D Gaussian Processes in C++, Python, and Julia](https://github.com/dfm/celerite)
	- By Dan Foreman-Mackey. [Online document is here](https://celerite.readthedocs.io/en/stable/) 
	- Based on [Fast and scalable Gaussian process modeling with applications to astronomical time series](https://arxiv.org/abs/1703.09710)

## Survival Analysis

* Traditionally, [survival analysis](https://en.wikipedia.org/wiki/Survival_analysis) was developed to measure lifespans of individuals. The analysis can be further applied to not just traditional births and deaths, but any duration.
* **Survival function**: the survival function defines the probability the death event has not occured yet at time t, or equivalently, the probability of surviving past time t
* **Hazard curve**: the probability of the death event occurring at time t, given that the death event has not occurred until time t. Hazard function is non-parametric.
* **Kaplan-Meier estimator for survival function**: Survival analysis assumes that upper limits have the same underlying distribution as the data, and the Kaplan-Meier esti- mator further assumes that detections and upper limits are mutually independent

- [`lifelines` - implementation of survival analysis in Python](https://lifelines.readthedocs.io/en/latest/)
	* Handles right-censored data.
	* Example of astrophysical usage: [radio SED of high-z SF galaxies](https://arxiv.org/abs/1812.03392)
