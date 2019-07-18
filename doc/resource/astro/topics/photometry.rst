Photometric Analysis of Astronomical Targets
============================================

General Tools
-------------

Source Extraction and Deblender
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `photutils - Affiliated package for image photometry
   utilities <https://github.com/astropy/photutils>`__

   -  General Python package. Not the fastest one and is still growing.

-  `sep - Python library for Source Extraction and
   Photometry <https://github.com/kbarbary/sep/blob/v1.0.x/docs/index.rst>`__

   -  **SEP** makes the core algorithms of Source Extractor available as
      a library of stand-alone functions and classes.

-  `SExtractor <http://www.astromatic.net/software/sextractor>`__

   -  It is very good software, just remember never call it **sex**,
      just don’t.
   -  The best document: `Don’t
      Panic <http://mensa.ast.uct.ac.za/~holwerda/SE/Welcome.html>`__ by
      Benne Holwerda.

-  `multiprofit - Multi-object/band source modelling/galaxy fitting
   code <https://github.com/lsst-dm/multiprofit>`__

   -  By Dan Taranu. Still under-development.

-  `The Tractor: measuring astronomical sources via probabilistic
   inference <https://github.com/dstndstn/tractor>`__

   -  By Dustin Lang and David Hogg. Used by DECaLS, Probabilistic
      astronomical source detection & measurement.

-  `ngmix - Gaussian mixtures and image processing implemented in
   python <https://github.com/esheldon/ngmix>`__

   -  By Erin Sheldon. Gaussian mixture models and other code for
      working with for 2d images, implemented in python. Used by DES
      data analysis.

Probabilistic Cataloging
~~~~~~~~~~~~~~~~~~~~~~~~

-  `PCAT - A transdimensional, hierarchical, Bayesian framework to
   sample from a metamodel <https://github.com/tdaylan/pcat>`__

   -  Based on the work by `Daylan et
      al. 2016 <https://ui.adsabs.harvard.edu/abs/2017ApJ...839....4D/abstract>`__;
      the application on crowded field photometry can be found in
      `Portillo et
      al. 2018 <https://ui.adsabs.harvard.edu/abs/2017AJ....154..132P/abstract>`__

-  `multiband_pcat - A transdimensional, Bayesian sampler using
   hierarchical modeling to catalog point sources in multiple
   passbands <https://github.com/RichardFeder/multiband_pcat>`__

   -  Based on the work by `Feder et
      al. 2019 <https://ui.adsabs.harvard.edu/abs/2019arXiv190704929F/abstract>`__.
      Now only works for point sources.

For Low Surface Brightness or Extremely Faint Targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `MTObjects - a tool for detecting sources in astronomical
   images <https://github.com/CarolineHaigh/mtobjects>`__

   -  Working progress, based on the **C** code by Paul Teeninga’s 2015
      work: `Improved detection of faint extended astronomical objects
      through statistical attribute
      filtering <http://fse.studenttheses.ub.rug.nl/12972/1/INF-BA-2015-P.D.Teeninga.pdf>`__

-  `DeepScan - source extraction tool designed to identify very low
   surface brightness features in large astronomical
   data <https://github.com/danjampro/DeepScan>`__

   -  Based on the work by `Prole et al. 2018: Automated detectionof
      very low surface brightness galaxiesin the Virgo
      cluster <https://academic.oup.com/mnras/article-abstract/478/1/667/4980941?redirectedFrom=fulltext>`__

Multiband Deblending and Force Photometry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `ProFound - source finding and extraction in
   R <https://github.com/asgr/ProFound>`__
-  `scarlet - Source separation in multi-band images by Constrained
   Matrix Factorization <https://github.com/fred3m/scarlet>`__

   -  By Fred Moolekamp and Peter Melchior. It performs source
      separation (aka “deblending”) on multi-band images. Still
      under-development.

-  `LAMBDAR: Lambda Adaptive Multi-Band Deblending Algorithm in
   R <https://github.com/AngusWright/LAMBDAR>`__

Image Simulation
~~~~~~~~~~~~~~~~

-  `Balrog - DES image simulation software: We dug too deeply and too
   greedily <https://github.com/emhuff/Balrog>`__

   -  Application in DES: `No galaxy left
      behind <https://arxiv.org/abs/1507.08336>`__
   -  `Balrog run in DES
      Y3 <https://cdcvs.fnal.gov/redmine/projects/des/wiki/des_balrog_y3>`__

-  `Synpipe - Synthetic Object Pipeline for the LSST
   pipeline <https://github.com/lsst/synpipe>`__

   -  Synpipe provides tasks which make use of the LSST fake object
      pipeline to insert realistic galaxies and stars. It also includes
      scripts to analyze the results of data which has been processed
      with fake objects inserted.

-  `Obiwan - Monte Carlo method for adding fake galaxies to Legacy
   Survey imaging data <https://obiwan.readthedocs.io/en/latest/>`__

Galaxies or Extended Objects
----------------------------

Tools
~~~~~

-  `GalSim - The modular galaxy image simulation
   toolkit <https://github.com/GalSim-developers/GalSim>`__

   -  **GalSim** is open-source software for simulating images of
      astronomical objects (stars, galaxies) in a variety of ways.
   -  **GalSim** paper can be found
      `here <http://adsabs.harvard.edu/abs/2015A%26C....10..121R>`__

1-D Galaxy Profile Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `stsdas.analysis.isophote - fits elliptical isophotes to galaxy
   images <http://stsdas.stsci.edu/cgi-bin/gethelp.cgi?ellipse>`__

   -  The OG.

-  `photutils.isophote - Python version of the ellipse
   code <https://github.com/astropy/photutils/tree/master/photutils/isophote>`__

   -  Not as fast as the **IRAF** version, but it is useful. Document is
      `here <https://photutils.readthedocs.io/en/stable/isophote.html>`__

-  `ARCHANGEL: Galaxy Photometry
   System <http://abyss.uoregon.edu/~js/archangel/>`__

   -  By James Schombert. Used by several projects including
      `SPARC <http://astroweb.cwru.edu/SPARC/>`__. `Paper is
      here <https://arxiv.org/abs/astro-ph/0703646>`__

2-D Galaxy Modeling
~~~~~~~~~~~~~~~~~~~

-  `Imfit: Fast, Flexible Multi-component Fitting of Galaxy
   Images <https://www.mpe.mpg.de/~erwin/code/imfit/>`__

   -  By Peter Erwin. Imfit is a program for fitting astronomical images
      – especially images of galaxies, though it can in principle be
      used for fitting other sources
   -  This is today’s first choice.
   -  `pymfit <https://github.com/johnnygreco/pymfit>`__ by Johnny Greco
      to use **imfit** in Python.

-  `Galfit - Detailed Structural Decomposition of Galaxy
   Images <https://users.obs.carnegiescience.edu/peng/work/galfit/galfit.html>`__

   -  By Chien Peng. Still the most flexible code. But it has not been
      maintained recently.
   -  `Top 10 Rules of Thumb for Galaxy
      Fitting <https://users.obs.carnegiescience.edu/peng/work/galfit/TOP10.html>`__:
      this is good advice for fitting galaxies in general.

-  `ProFit - Profile Fitting Code in
   R <https://github.com/ICRAR/ProFit>`__

   -  ProFit is a Bayesian galaxy fitting tool that uses a fast C++
      image generation library and a flexible interface to a large
      number of likelihood samplers.
   -  `libprofit - a low-level C++ library that produces images based on
      different luminosity
      profiles <https://github.com/ICRAR/libprofit>`__. Document is
      `here <https://libprofit.readthedocs.io/en/latest/>`__
   -  `pyprofit - a python wrapper for
      libprofit <https://github.com/ICRAR/pyprofit>`__

      -  This only provides the tool to generate 2-D galaxy model with
         PSF convolution. You need to setup your own optimazation
         structue for fitting.

-  `lenstronomy - software package for lens model reconstruction of
   imaging data <https://github.com/sibirrer/lenstronomy>`__

   -  By `Simon Birrer <http://www.astro.ucla.edu/~sibirrer/>`__.
      **lenstronomy** is a multi-purpose package to model strong
      gravitational lenses. The software package is presented in Birrer
      & Amara 2018 and is based on Birrer et al 2015.
   -  It can also be used to fit galaxies like **Galfit**. See `example
      here <https://github.com/sibirrer/lenstronomy_extensions/blob/master/lenstronomy_extensions/Notebooks/galfitting.ipynb>`__

Stellar or PSF Photometry
-------------------------

-  `DAOPHOT - Stellar Photometry
   Package <http://www.star.bris.ac.uk/~mbt/daophot/>`__

   -  DAOPHOT is a package for stellar photomoetry designed to deal with
      crowded fields.

-  `DOLPHOT - stellar photometry package that was adapted from HSTphot
   for general use <http://americano.dolphinsim.com/dolphot/>`__

   -  By Andrew Dolphin and Raytheon Company. PSF photometry for HSC.
      Now supports WFIRST too.
   -  `pydolphot - python wrappers for
      DOLPHOT <https://github.com/dweisz/pydolphot>`__ by Dan Weisz.

-  `photutils.psf - PSF photometry in
   Python <https://photutils.readthedocs.io/en/stable/psf.html>`__

   -  Provides Python approaches to do **DAOPhot** or **IRAF** style PSF
      photometry.

Useful papers
~~~~~~~~~~~~~

-  `Photometric Biases in Modern Surveys by Portillo, Speagle, &
   Finkbeiner 2019 <https://arxiv.org/pdf/1902.02374.pdf>`__

   -  Reveals a bias in modern PSF photometry: We show these ML
      estimators systematically overestimate the flux as a function of
      the signal-to-noise ratio (SNR) and the number of model parameters
      involved in the fit.
   -  `phot-bias - Biases in Maximum-Likelihood
      Photometry <https://github.com/joshspeagle/phot_bias>`__
