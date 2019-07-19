Observational and Theoretical Cosmology
=======================================

Cosmology Parameters and Model Optimization
-------------------------------------------

-  `CCL - DESC Core Cosmology Library: cosmology routines with validated
   numerical accuracy <https://github.com/LSSTDESC/CCL>`__

   -  On top of **CCL**, there is **firecrown**:
   -  `firecrown: the “c” is for
      “cosmology” <https://github.com/LSSTDESC/firecrown>`__

-  `CosmoMC - MCMC parameter sampling
   code <https://github.com/cmbant/CosmoMC>`__

   -  **CosmoMC** is a Fortran 2008 Markov-Chain Monte-Carlo (MCMC)
      engine for exploring cosmological parameter space, together with
      Fortran and python code for analysing Monte-Carlo samples and
      importance sampling (plus a suite of scripts for building grids of
      runs, plotting and presenting results).

-  `CosmoHammer - Cosmological parameter estimation with the MCMC
   Hammer <https://github.com/cosmo-ethz/CosmoHammer>`__

   -  A paper describing the software can be `found
      here <https://arxiv.org/abs/1212.1721>`__

-  `Cobaya - Code for Bayesian Analysis in
   Cosmology <https://github.com/CobayaSampler/cobaya>`__

   -  **Cobaya** is a framework for sampling and statistical modelling:
      it allows you to explore an arbitrary prior or posterior using a
      range of Monte Carlo samplers (including the advanced MCMC sampler
      from **CosmoMC**, and the advanced nested sampler **PolyChord**).

-  `MontePython - The Monte Carlo code for class in
   Python <https://baudren.github.io/montepython.html>`__

   -  **MontePython** is a Monte Carlo code for Cosmological Parameter
      extraction. It contains likelihood codes of most recent
      experiments, and interfaces with the Boltzmann code **Class** for
      computing the cosmological observables.

Supernova related
-----------------

-  `sncosmo - Python library for supernova
   cosmology <https://github.com/sncosmo/sncosmo>`__

   -  **SNCosmo** is a Python library for supernova cosmology analysis.
      It aims to make such analysis both as flexible and clear as
      possible. `Online document is
      here <https://sncosmo.readthedocs.io/en/v2.0.x/>`__
   -  `sndatasets - Download and normalize published supernova
      photometric data <https://github.com/sncosmo/sndatasets>`__

CMB related
-----------

-  `CAMB - Code for Anisotropies in the Microwave
   Background <https://github.com/cmbant/CAMB>`__

   -  **CAMB** is a cosmology code for calculating cosmological
      observables, including CMB, lensing, source count and 21cm angular
      power spectra, matter power spectra, transfer functions and
      background evolution

-  `CLassylss - a lightweight Python binding of the CLASS CMB Boltzmann
   code <https://github.com/nickhand/classylss>`__

   -  A very nice gateway to **CLASS**

-  `CLASS - Cosmic Linear Anisotropy Solving
   System <http://class-code.net/>`__

   -  The purpose of **CLASS** is to simulate the evolution of linear
      perturbations in the universe and to compute CMB and large scale
      structure observables.
   -  A public repository is available on
      `github <https://github.com/lesgourg/class_public>`__

Correlation Functions
---------------------

-  `Corrfunc - Blazing fast correlation functions on the
   CPU <https://github.com/manodeep/Corrfunc>`__

-  `TreeCorr - Code for efficiently computing 2-point and 3-point
   correlation functions <https://github.com/rmjarvis/TreeCorr>`__

   -  It can compute correlations of regular number counts, weak lensing
      shears, or scalar quantities such as convergence or CMB
      temperature fluctutations.

Weak Lensing
------------

-  Both **corrfunc** and **treecorr** can be used for shear-shear or
   galaxy-shear analysis
-  `LensTools - collects together a suite of widely used analysis tools
   in Weak Gravitational
   Lensing <https://github.com/apetri/LensTools>`__
-  `DESWL - A collection of scripts and software related to DES weak
   lensing analysis <https://github.com/rmjarvis/DESWL>`__

   -  By Marc Jarvis

Cluster Lensing
~~~~~~~~~~~~~~~

-  `cluster-lensing - Galaxy Cluster and Weak Lensing
   Tools <https://github.com/jesford/cluster-lensing>`__

   -  By Jes Ford. `Paper can be found
      here <https://iopscience.iop.org/article/10.3847/1538-3881/152/6/228/meta>`__

-  `cluster_toolkit - Tools for analyzing galaxy
   clusters <https://github.com/tmcclintock/cluster_toolkit>`__

   -  by `Tom McClintock <https://tmcclintock.github.io/>`__. Contains
      routines used in the Dark Energy Survey Year 1 stacked cluster
      weak lensing analysis.

IGM Related (e.g. Lya Forrest)
------------------------------

-  `IGMHUB - IGM analysis tools <https://igmhub.github.io/>`__

   -  `baofit - Fits cosmological data to measure baryon acoustic
      oscillations <https://github.com/igmhub/baofit>`__

      -  **baofit** is a software package for analyzing cosmological
         correlation functions to estimate parameters related to baryon
         acoustic oscillations and redshift-space distortions

Dark Matter Halos
-----------------

-  `Halotools - Python package for studying large scale structure,
   cosmology, and galaxy evolution using N-body simulations and halo
   models <https://github.com/astropy/halotools>`__

   -  **Halotools** is a specialized python package for building and
      testing models of the galaxy-halo connection, and analyzing
      catalogs of dark matter halos.

-  `Colossus - a python toolkit for calculations pertaining to
   cosmology, the large-scale structure of the universe, and the
   properties of dark matter
   halos <http://www.benediktdiemer.com/code/colossus/>`__

-  `COMMAH - COncentration-Mass relation and Mass Accretion
   History <https://correacamila.com/code/commah/>`__

   -  By Camila Correa; calculates dark matter halo concentrations as a
      function of halo mass and redshift. The `source code is available
      on Github <https://github.com/astroduff/commah>`__
   -  Based on the works of `Correa et
      al. 2015a <https://arxiv.org/abs/1409.5228>`__; `Correa et
      al. 2015c <https://arxiv.org/abs/1502.00391>`__

Emulators:
----------

-  Increasingly popular way to study cosmology based on a limit set of
   N-body simulations.

Key Technique
~~~~~~~~~~~~~

-  A suite of N-body cosmology simulations

   -  2nd order Lagrangian perturbation theory (2LPT) initial conditions

      -  e.g. by `2LPTIC <http://cosmo.nyu.edu/roman/2LPT/>`__ or on
         Github `here <https://github.com/manodeep/2LPTic>`__

   -  Input power spectrum. e.g. by `CAMB: Code for Anisotropies in the
      Microwave Background <https://camb.info>`__

-  Sampling the cosmological parameters:

   -  Latin Hypercube Designs (LHDs)
   -  `Maximin-distance “sliced” LHD
      (SLHD) <https://www.asc.ohio-state.edu/statistics/comp_exp/jour.club/optimal_sliced_lhd_ba2015.pdf>`__

      -  `A Python
         implementation <https://pythonhosted.org/pyDOE/index.html>`__
      -  `SMT - Surrogate Modeling
         Toolbox <https://smt.readthedocs.io/en/latest/index.html>`__
      -  `Another Python version <https://github.com/sahilm89/lhsmdu>`__

-  Principle Component Analysis (PCA)

   -  e.g. `empca <https://github.com/sbailey/empca>`__ by Stephen
      Bailey

-  Gaussian process emulator

   -  e.g. `george <http://dfm.io/george/current/>`__ by Dan
      Foreman-Mackey

Available Emulators
~~~~~~~~~~~~~~~~~~~

-  `Aemulus Project led by
   Stanford <https://aemulusproject.github.io>`__

   -  The basic structure of the code:
      `Aemulator <https://github.com/AemulusProject/Aemulator>`__
   -  Emulator of `halo mass
      function <https://github.com/AemulusProject/hmf_emulator>`__ and
      `halo bias <https://github.com/AemulusProject/bias_emulator>`__
   -  `The Aemulus Project I: Numerical Simulations for Precision
      Cosmology <https://arxiv.org/abs/1804.05865>`__
   -  `The Aemulus Project II: Emulating the Halo Mass
      Function <https://arxiv.org/abs/1804.05866>`__
   -  `The Aemulus Project III: Emulation of the Galaxy Correlation
      Function <https://arxiv.org/abs/1804.05867>`__
   -  Documents for `data release
      1 <https://aemulus-data.readthedocs.io/en/latest/>`__

-  `CosmicEmu led by
   ANL <http://www.hep.anl.gov/cosmology/CosmicEmu/emu.html>`__

   -  Code can be found `here <https://github.com/lanl/CosmicEmu>`__
   -  **CosmicEmu** produces predictions for the matter power spectrum
      based on eight cosmological parametersand redshift.
   -  Based on the `Mira-Titan
      simulations <https://arxiv.org/abs/1508.02654>`__
   -  Also related to the Coyote Universe emulator: `Paper
      I <https://arxiv.org/abs/0812.1052>`__, `Paper
      II <https://arxiv.org/abs/0902.0429>`__, `Paper
      III <https://arxiv.org/abs/0912.4490>`__, and
      `Extended <https://arxiv.org/abs/1304.7849>`__
   -  Paper about the `emulated
      power-spectrum <https://arxiv.org/abs/1311.6444>`__
   -  Paper about the `emulated halo mass-concentration
      relation <https://arxiv.org/abs/1210.1576>`__

-  ACME Emulator led by OSU

   -  Paper by Ben Wibking: `Emulating galaxy clustering and
      galaxy-galaxy lensing into the deeply nonlinear
      regime <http://adsabs.harvard.edu/doi/10.1093/mnras/sty2258>`__
   -  Use the `AbacusCosmos suite of
      simulations <https://lgarrison.github.io/AbacusCosmos/>`__

      -  The code used for the simulation is
         `here <https://github.com/lgarrison/AbacusCosmos>`__
      -  The `AbacusCosmos description
         paper <https://arxiv.org/abs/1712.05768>`__

-  Dark Emulator led by IPMU

   -  Based on the Dark Quest suite of simulations.
   -  `Dark Quest. I. Fast and Accurate Emulation of Halo Clustering
      Statistics and Its Application to Galaxy
      Clustering <http://adsabs.harvard.edu/abs/2018arXiv181109504N>`__
