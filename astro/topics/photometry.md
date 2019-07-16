# Photometric Analysis of Astronomical Targets

## General Tools

### Source Extraction and Deblender

* [__photutils__ - Affiliated package for image photometry utilities](https://github.com/astropy/photutils)
    * General Python package. Not the fastest one and is still growing.
* [__sep__ - Python library for Source Extraction and Photometry](https://github.com/kbarbary/sep/blob/v1.0.x/docs/index.rst)
    * __SEP__ makes the core algorithms of Source Extractor available as a library of stand-alone functions and classes.
* [__SExtractor__](http://www.astromatic.net/software/sextractor)
    * It is very good software, just remember never call it __sex__, just don't.
    * The best document: [Don't Panic](http://mensa.ast.uct.ac.za/~holwerda/SE/Welcome.html) by Benne Holwerda.
* [__multiprofit__ - Multi-object/band source modelling/galaxy fitting code](https://github.com/lsst-dm/multiprofit)
    - By Dan Taranu. Still under-development.
* [The __Tractor__: measuring astronomical sources via probabilistic inference](https://github.com/dstndstn/tractor)
    * By Dustin Lang and David Hogg.  Used by DECaLS, Probabilistic astronomical source detection & measurement.
* [__ngmix__ - Gaussian mixtures and image processing implemented in python](https://github.com/esheldon/ngmix)
    * By Erin Sheldon. Gaussian mixture models and other code for working with for 2d images, implemented in python. Used by DES data analysis.

### Probabilistic Cataloging

* [__PCAT__ - A transdimensional, hierarchical, Bayesian framework to sample from a metamodel](https://github.com/tdaylan/pcat)
    * Based on the work by [Daylan et al. 2016](https://ui.adsabs.harvard.edu/abs/2017ApJ...839....4D/abstract); the application on crowded field photometry can be found in [Portillo et al. 2018](https://ui.adsabs.harvard.edu/abs/2017AJ....154..132P/abstract)

* [__multiband_pcat__ - A transdimensional, Bayesian sampler using hierarchical modeling to catalog point sources in multiple passbands](https://github.com/RichardFeder/multiband_pcat)
    * Based on the work by [Feder et al. 2019](https://ui.adsabs.harvard.edu/abs/2019arXiv190704929F/abstract). Now only works for point sources.

#### For Low Surface Brightness or Extremely Faint Targets

* [__MTObjects__ - a tool for detecting sources in astronomical images](https://github.com/CarolineHaigh/mtobjects)
    * Working progress, based on the __C__ code by Paul Teeninga's 2015 work: [Improved detection of faint extended astronomical objects through statistical attribute filtering](http://fse.studenttheses.ub.rug.nl/12972/1/INF-BA-2015-P.D.Teeninga.pdf)

* [__DeepScan__ - source extraction tool designed to identify very low surface brightness features in large astronomical data](https://github.com/danjampro/DeepScan)
    * Based on the work by [Prole et al. 2018: Automated detectionof very low surface brightness galaxiesin the Virgo cluster](https://academic.oup.com/mnras/article-abstract/478/1/667/4980941?redirectedFrom=fulltext)

#### Multiband Deblending and Force Photometry
* [ProFound - source finding and extraction in R](https://github.com/asgr/ProFound)
* [scarlet - Source separation in multi-band images by Constrained Matrix Factorization](https://github.com/fred3m/scarlet)
    - By Fred Moolekamp and Peter Melchior. It performs source separation (aka "deblending") on multi-band images. Still under-development.
* [LAMBDAR: Lambda Adaptive Multi-Band Deblending Algorithm in R](https://github.com/AngusWright/LAMBDAR)

### Image Simulation

* [Balrog - DES image simulation software: We dug too deeply and too greedily](https://github.com/emhuff/Balrog)
    - Application in DES: [No galaxy left behind](https://arxiv.org/abs/1507.08336)
    - [__Balrog__ run in DES Y3](https://cdcvs.fnal.gov/redmine/projects/des/wiki/des_balrog_y3)
* [Synpipe - Synthetic Object Pipeline for the LSST pipeline](https://github.com/lsst/synpipe)
    - Synpipe provides tasks which make use of the LSST fake object pipeline to insert realistic galaxies and stars. It also includes scripts to analyze the results of data which has been processed with fake objects inserted.
* [Obiwan - Monte Carlo method for adding fake galaxies to Legacy Survey imaging data](https://obiwan.readthedocs.io/en/latest/)

## Galaxies or Extended Objects

### Tools

* [GalSim - The modular galaxy image simulation toolkit](https://github.com/GalSim-developers/GalSim)
    - __GalSim__ is open-source software for simulating images of astronomical objects (stars, galaxies) in a variety of ways.
    - __GalSim__ paper can be found [here](http://adsabs.harvard.edu/abs/2015A%26C....10..121R)

### 1-D Galaxy Profile Extraction

* [__stsdas.analysis.isophote__ - fits elliptical isophotes to galaxy images](http://stsdas.stsci.edu/cgi-bin/gethelp.cgi?ellipse)
    - The OG.
* [__photutils.isophote__ - Python version of the __ellipse__ code](https://github.com/astropy/photutils/tree/master/photutils/isophote)
    - Not as fast as the __IRAF__ version, but it is useful. Document is [here](https://photutils.readthedocs.io/en/stable/isophote.html)
* [ARCHANGEL: Galaxy Photometry System](http://abyss.uoregon.edu/~js/archangel/)
    - By James Schombert. Used by several projects including [SPARC](http://astroweb.cwru.edu/SPARC/). [Paper is here](https://arxiv.org/abs/astro-ph/0703646)

### 2-D Galaxy Modeling

* [Imfit: Fast, Flexible Multi-component Fitting of Galaxy Images](https://www.mpe.mpg.de/~erwin/code/imfit/)
    - By Peter Erwin. Imfit is a program for fitting astronomical images -- especially images of galaxies, though it can in principle be used for fitting other sources
    - This is today's first choice.
    - [pymfit](https://github.com/johnnygreco/pymfit) by Johnny Greco to use __imfit__ in Python.
* [Galfit - Detailed Structural Decomposition of Galaxy Images](https://users.obs.carnegiescience.edu/peng/work/galfit/galfit.html)
    - By Chien Peng. Still the most flexible code. But it has not been maintained recently.
    - [Top 10 Rules of Thumb for Galaxy Fitting](https://users.obs.carnegiescience.edu/peng/work/galfit/TOP10.html): this is good advice for fitting galaxies in general.
* [ProFit - Profile Fitting Code in R](https://github.com/ICRAR/ProFit)
    - ProFit is a Bayesian galaxy fitting tool that uses a fast C++ image generation library and a flexible interface to a large number of likelihood samplers.
    - [libprofit - a low-level C++ library that produces images based on different luminosity profiles](https://github.com/ICRAR/libprofit). Document is [here](https://libprofit.readthedocs.io/en/latest/)
    - [pyprofit - a python wrapper for libprofit](https://github.com/ICRAR/pyprofit)
        * This only provides the tool to generate 2-D galaxy model with PSF convolution. You need to setup your own optimazation structue for fitting.
* [lenstronomy - software package for lens model reconstruction of imaging data](https://github.com/sibirrer/lenstronomy)
    - By [Simon Birrer](http://www.astro.ucla.edu/~sibirrer/). __lenstronomy__ is a multi-purpose package to model strong gravitational lenses. The software package is presented in Birrer & Amara 2018 and is based on Birrer et al 2015.
    - It can also be used to fit galaxies like __Galfit__. See [example here](https://github.com/sibirrer/lenstronomy_extensions/blob/master/lenstronomy_extensions/Notebooks/galfitting.ipynb)

## Stellar or PSF Photometry

* [DAOPHOT - Stellar Photometry Package](http://www.star.bris.ac.uk/~mbt/daophot/)
    - DAOPHOT is a package for stellar photomoetry designed to deal with crowded fields.
* [DOLPHOT - stellar photometry package that was adapted from HSTphot for general use](http://americano.dolphinsim.com/dolphot/)
    - By Andrew Dolphin and Raytheon Company. PSF photometry for HSC. Now supports WFIRST too.
    - [pydolphot - python wrappers for DOLPHOT](https://github.com/dweisz/pydolphot) by Dan Weisz.
* [__photutils.psf__ - PSF photometry in Python](https://photutils.readthedocs.io/en/stable/psf.html)
    - Provides Python approaches to do __DAOPhot__ or __IRAF__ style PSF photometry.

### Useful papers

* [Photometric Biases in Modern Surveys by Portillo, Speagle, & Finkbeiner 2019](https://arxiv.org/pdf/1902.02374.pdf)
    - Reveals a bias in modern PSF photometry: We show these ML estimators systematically overestimate the flux as a function of the signal-to-noise ratio (SNR) and the number of model parameters involved in the fit.
    - [phot-bias - Biases in Maximum-Likelihood Photometry](https://github.com/joshspeagle/phot_bias)
