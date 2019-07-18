# Observational and Theoretical Cosmology

## Cosmology Parameters and Model Optimization

* [__CCL__ - DESC Core Cosmology Library: cosmology routines with validated numerical accuracy](https://github.com/LSSTDESC/CCL)
	- On top of __CCL__, there is __firecrown__:
	- [firecrown: the "c" is for "cosmology"](https://github.com/LSSTDESC/firecrown)
* [__CosmoMC__ - MCMC parameter sampling code](https://github.com/cmbant/CosmoMC)
	- __CosmoMC__ is a Fortran 2008 Markov-Chain Monte-Carlo (MCMC) engine for exploring cosmological parameter space, together with Fortran and python code for analysing Monte-Carlo samples and importance sampling (plus a suite of scripts for building grids of runs, plotting and presenting results).
* [__CosmoHammer__ - Cosmological parameter estimation with the MCMC Hammer](https://github.com/cosmo-ethz/CosmoHammer)
	- A paper describing the software can be [found here](https://arxiv.org/abs/1212.1721)

* [__Cobaya__ - Code for Bayesian Analysis in Cosmology](https://github.com/CobayaSampler/cobaya)
	- __Cobaya__ is a framework for sampling and statistical modelling: it allows you to explore an arbitrary prior or posterior using a range of Monte Carlo samplers (including the advanced MCMC sampler from __CosmoMC__, and the advanced nested sampler __PolyChord__).

* [__MontePython__ - The Monte Carlo code for class in Python](https://baudren.github.io/montepython.html)
	- __MontePython__ is a Monte Carlo code for Cosmological Parameter extraction. It contains likelihood codes of most recent experiments, and interfaces with the Boltzmann code __Class__ for computing the cosmological observables.

## Supernova related

* [__sncosmo__ - Python library for supernova cosmology](https://github.com/sncosmo/sncosmo)
	- __SNCosmo__ is a Python library for supernova cosmology analysis. It aims to make such analysis both as flexible and clear as possible. [Online document is here](https://sncosmo.readthedocs.io/en/v2.0.x/)
	- [__sndatasets__ - Download and normalize published supernova photometric data](https://github.com/sncosmo/sndatasets)

## CMB related

* [__CAMB__ - Code for Anisotropies in the Microwave Background](https://github.com/cmbant/CAMB)
	- __CAMB__ is a cosmology code for calculating cosmological observables, including CMB, lensing, source count and 21cm angular power spectra, matter power spectra, transfer functions and background evolution

* [__CLassylss__ - a lightweight Python binding of the CLASS CMB Boltzmann code](https://github.com/nickhand/classylss)
	- A very nice gateway to __CLASS__

* [__CLASS__ - Cosmic Linear Anisotropy Solving System](http://class-code.net/)
	- The purpose of __CLASS__ is to simulate the evolution of linear perturbations in the universe and to compute CMB and large scale structure observables.
	- A public repository is available on [github](https://github.com/lesgourg/class_public)

## Correlation Functions

* [__Corrfunc__ - Blazing fast correlation functions on the CPU](https://github.com/manodeep/Corrfunc)

* [__TreeCorr__ - Code for efficiently computing 2-point and 3-point correlation functions](https://github.com/rmjarvis/TreeCorr)
	- It can compute correlations of regular number counts, weak lensing shears, or scalar quantities such as convergence or CMB temperature fluctutations.

## Weak Lensing

* Both __corrfunc__ and __treecorr__ can be used for shear-shear or galaxy-shear analysis
* [__LensTools__ - collects together a suite of widely used analysis tools in Weak Gravitational Lensing](https://github.com/apetri/LensTools)
* [__DESWL__ - A collection of scripts and software related to DES weak lensing analysis](https://github.com/rmjarvis/DESWL)
	- By Marc Jarvis

### Cluster Lensing

* [__cluster-lensing__ - Galaxy Cluster and Weak Lensing Tools](https://github.com/jesford/cluster-lensing)
	- By Jes Ford.  [Paper can be found here](https://iopscience.iop.org/article/10.3847/1538-3881/152/6/228/meta)

* [__cluster_toolkit__ - Tools for analyzing galaxy clusters](https://github.com/tmcclintock/cluster_toolkit)
	- by [Tom McClintock](https://tmcclintock.github.io/). Contains routines used in the Dark Energy Survey Year 1 stacked cluster weak lensing analysis.


## IGM Related (e.g. Lya Forrest)

* [__IGMHUB__ - IGM analysis tools](https://igmhub.github.io/)
	* [__baofit__ - Fits cosmological data to measure baryon acoustic oscillations](https://github.com/igmhub/baofit)
		- __baofit__ is a software package for analyzing cosmological correlation functions to estimate parameters related to baryon acoustic oscillations and redshift-space distortions

## Dark Matter Halos

* [__Halotools__ - Python package for studying large scale structure, cosmology, and galaxy evolution using N-body simulations and halo models](https://github.com/astropy/halotools)
	- __Halotools__ is a specialized python package for building and testing models of the galaxy-halo connection, and analyzing catalogs of dark matter halos.

* [__Colossus__ - a python toolkit for calculations pertaining to cosmology, the large-scale structure of the universe, and the properties of dark matter halos](http://www.benediktdiemer.com/code/colossus/)

* [__COMMAH__ - COncentration-Mass relation and Mass Accretion History](https://correacamila.com/code/commah/)
	- By Camila Correa; calculates dark matter halo concentrations as a function of halo mass and redshift. The [source code is available on Github](https://github.com/astroduff/commah)
	- Based on the works of [Correa et al. 2015a](https://arxiv.org/abs/1409.5228); [Correa et al. 2015c](https://arxiv.org/abs/1502.00391)

## Emulators:

* Increasingly popular way to study cosmology based on a limit set of N-body simulations.

### Key Technique

* A suite of N-body cosmology simulations
	- 2nd order Lagrangian perturbation theory (2LPT) initial conditions
		* e.g. by [__2LPTIC__](http://cosmo.nyu.edu/roman/2LPT/) or on Github [here](https://github.com/manodeep/2LPTic)
	- Input power spectrum. e.g. by [CAMB: Code for Anisotropies in the Microwave Background](https://camb.info)

* Sampling the cosmological parameters:
	- Latin Hypercube Designs (LHDs)
	- [Maximin-distance “sliced” LHD (SLHD)](https://www.asc.ohio-state.edu/statistics/comp_exp/jour.club/optimal_sliced_lhd_ba2015.pdf)
    	- [A Python implementation](https://pythonhosted.org/pyDOE/index.html)
    	- [__SMT__ - Surrogate Modeling Toolbox](https://smt.readthedocs.io/en/latest/index.html)
    	- [Another Python version](https://github.com/sahilm89/lhsmdu)

* Principle Component Analysis (PCA)
	- e.g. [__empca__](https://github.com/sbailey/empca) by Stephen Bailey

* Gaussian process emulator
	- e.g. [__george__](http://dfm.io/george/current/) by Dan Foreman-Mackey

### Available Emulators

- [Aemulus Project led by Stanford](https://aemulusproject.github.io)
	* The basic structure of the code: [Aemulator](https://github.com/AemulusProject/Aemulator)
	* Emulator of [halo mass function](https://github.com/AemulusProject/hmf_emulator) and [halo bias](https://github.com/AemulusProject/bias_emulator)
	* [The Aemulus Project I: Numerical Simulations for Precision Cosmology](https://arxiv.org/abs/1804.05865)
	* [The Aemulus Project II: Emulating the Halo Mass Function](https://arxiv.org/abs/1804.05866)
	* [The Aemulus Project III: Emulation of the Galaxy Correlation Function](https://arxiv.org/abs/1804.05867)
	* Documents for [data release 1](https://aemulus-data.readthedocs.io/en/latest/)

- [CosmicEmu led by ANL](http://www.hep.anl.gov/cosmology/CosmicEmu/emu.html)
	* Code can be found [here](https://github.com/lanl/CosmicEmu)
	* __CosmicEmu__ produces predictions for the matter power spectrum based on eight cosmological parametersand redshift.
	* Based on the [Mira-Titan simulations](https://arxiv.org/abs/1508.02654)
	* Also related to the Coyote Universe emulator: [Paper I](https://arxiv.org/abs/0812.1052), [Paper II](https://arxiv.org/abs/0902.0429), [Paper III](https://arxiv.org/abs/0912.4490), and [Extended](https://arxiv.org/abs/1304.7849)
	* Paper about the [emulated power-spectrum](https://arxiv.org/abs/1311.6444)
	* Paper about the [emulated halo mass-concentration relation](https://arxiv.org/abs/1210.1576)

- ACME Emulator led by OSU
	* Paper by Ben Wibking: [Emulating galaxy clustering and galaxy-galaxy lensing into the deeply nonlinear regime](http://adsabs.harvard.edu/doi/10.1093/mnras/sty2258)
	* Use the [AbacusCosmos suite of simulations](https://lgarrison.github.io/AbacusCosmos/)
		- The code used for the simulation is [here](https://github.com/lgarrison/AbacusCosmos)
		- The [AbacusCosmos description paper](https://arxiv.org/abs/1712.05768)

- Dark Emulator led by IPMU
	* Based on the Dark Quest suite of simulations.
	* [Dark Quest. I. Fast and Accurate Emulation of Halo Clustering Statistics and Its Application to Galaxy Clustering](http://adsabs.harvard.edu/abs/2018arXiv181109504N)

