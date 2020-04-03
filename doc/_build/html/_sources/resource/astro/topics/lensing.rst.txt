All about Lensing: Strong, Weak, and Micro
==========================================

Strong Lensing
--------------

Modeling
~~~~~~~~

-  `PyAutoLens - Automated Strong Gravitational Lens
   Modeling <https://github.com/Jammy2211/PyAutoLens>`__

   -  From James Nightingale. Based on `Adaptive Semi-linear Inversion
      of Strong Gravitational Lens
      Imaging <https://arxiv.org/abs/1412.7436>`__ and `AutoLens:
      Automated Modeling of a Strong Lens’s Light, Mass and
      Source <https://arxiv.org/abs/1708.07377>`__

-  `lenstronomy - Software package for lens model reconstruction of
   imaging data <https://github.com/sibirrer/lenstronomy>`__

   -  By Simon Birrer. **lenstronomy** is a multi-purpose package to
      model strong gravitational lenses.
   -  Based on `Lenstronomy: multi-purpose gravitational lens modelling
      software package <https://arxiv.org/abs/1803.09746v1>`__

-  `vislens - Module for modeling gravitational lensing systems in which
   the data are not images but interferometric
   visibilities <https://github.com/jspilker/visilens>`__

   -  **Visilens** is a python module for modeling gravitational lensing
      systems observed by a radio/mm interferometer like ALMA or ATCA.

Weak Lensing
------------

-  Some of the tools overlap with the cosmology tools section.

-  `LensTools - Useful computing tools for Weak Lensing
   analyses <https://github.com/apetri/LensTools>`__

   -  This python add-on will handle basically every operation you will
      need to perform on Weak Lensing survey data; the distribution
      includes a range of tools in image analysis, statistical
      processing and numerical theory predictions and supports
      multiprocessing using the mpi4py module.
   -  Full document can be found
      `here <https://lenstools.readthedocs.io/en/latest/>`__

-  `TreeCorr <Code%20for%20efficiently%20computing%202-point%20and%203-point%20correlation%20functions>`__

   -  By Mark Jarvis. **TreeCorr** is actually a very general tool for
      correlation function. Can be used for number counts, cosmic shear,
      galaxy-galaxy lensing, and other cosmological applications.

-  `swot - Super W of Theta <https://jeancoupon.com/swot>`__

   -  SWOT is a code to compute two-point statistics for very large data
      sets, based on “divide and conquer” algorithms. `Github repo is
      here <https://github.com/jcoupon/swot>`__
   -  Is a great tool to do galaxy-galaxy lensing.

Shear Measurement
~~~~~~~~~~~~~~~~~

-  Galaxy shape measurement with corrections for PSF and other
   systematics. Different lensing surveys often choose different codes
   or algorithms to calculate shear.

-  `GREAT3 - The third GRavitational lEnsing Accuracy Testing
   challenge <http://great3challenge.info/>`__

   -  **GREAT3** is a blind data analysis competition held by the
      world-wide weak lensing community to test weak lensing measurement
      algorithms.
   -  Details about the challenge can be found in the `The Third
      Gravitational Lensing Accuracy Testing (GREAT3) Challenge
      Handbook <https://arxiv.org/abs/1308.4982>`__
   -  Summary of the challenge can be found in the `final GREAT3
      conference <http://www.great3challenge.info/?q=finalmeeting>`__
   -  `Public repository for the code can be found on
      GitHub <https://github.com/barnabytprowe/great3-public>`__

-  `ngmix - Gaussian mixtures and image processing implemented in
   python <https://github.com/esheldon/ngmix>`__

   -  By Erin Sheldon. Gaussian mixture models and other code for
      working with for 2d images, implemented in python.
   -  **ngmix** is adopted by the dark energy survey (DES) as one of the
      shear measurement tools. Examples of running **ngmix** on DES MEDS
      files can be found
      `here <https://github.com/esheldon/gmix_meds>`__

-  `im3shape - galaxy shape measurement
   code <https://bitbucket.org/joezuntz/im3shape-git/src/master/>`__

   -  By Joe Zuntz. **Im3shape** measures the shapes of galaxies in
      astronomical survey images, taking into account that they have
      been distorted by a point-spread function.
   -  **Im3shape** is adopted by the dark energy survey (DES) as one of
      the shear measurement tools. Please also see `Zuntz et
      al. 2013 <https://arxiv.org/abs/1302.0183>`__

-  `meas_extensions_shapeHSM : HSM shape
   measurement <https://github.com/lsst/meas_extensions_shapeHSM>`__

   -  Used by the LSST Data Management.

Cosmic Shears Analysis
~~~~~~~~~~~~~~~~~~~~~~

-  `Weak gravitational lensing CFHTLens
   analysis <https://github.com/apetri/CFHTLens_analysis>`__

-  `Public repository for the Monte Python likelihood module for the
   KiDS-450 cosmic shear correlation
   functions <https://github.com/fkoehlin/kids450_cf_likelihood_public>`__

   -  This repository contains the likelihood module for the KiDS-450
      correlation function measurements from `Hildebrandt et
      al. 2017 <https://arxiv.org/abs/1606.05338>`__
   -  Also the `public repository for the Monte Python likelihood module
      for the KiDS+VIKING-450 (KV450) cosmic shear correlation
      functions <https://github.com/fkoehlin/kv450_cf_likelihood_public>`__

Galaxy-Galaxy Lensing Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `xshear - Measure the tangential shear around a set of
   lenses <https://github.com/esheldon/xshear>`__

   -  By Erin Sheldon. Measure the tangential shear around a set of
      lenses. This technique is also known as cross-correlation shear,
      hence the name xshear.

-  `xpipe - Weak lensing measurement pipeline for wide area
   surveys <https://github.com/vargatn/xpipe>`__

   -  By Tamás Norbert Varga. **xpipe** is a python package created to
      automate work with measuring and calibrating weak lensing shear
      and mass profiles in wide area lensing surveys such as DES

-  `dsigma - Pure-python galaxy-galaxy lensing framework for the HSC
   survey <https://github.com/dr-guangtou/dsigma>`__

   -  By Song Huang. **dsigma** is a pure-python galaxy-galaxy lensing
      pipeline designed for the Hyper-Suprime Cam survey. It should be
      flexible enough to work with other surveys after adapting the same
      data format.

Cluster Lensing
~~~~~~~~~~~~~~~

-  `cluster-lensing - Galaxy Cluster and Weak Lensing
   Tools <https://github.com/jesford/cluster-lensing>`__

   -  By `Jes Ford <http://jesford.github.io/>`__. **cluster-lensing**
      is a set of tools to calculate galaxy cluster halo properties and
      weak lensing shear and magnification profiles.

-  `Python codes for ongoing cluster analysis of the LSST/DESC cluster
   group <https://github.com/nicolaschotard/Clusters>`__

   -  Some of the relevant notebooks can be found
      `here <https://github.com/lsst-france/LSST_notebooks>`__

Weak Lensing Mass Map
~~~~~~~~~~~~~~~~~~~~~

-  `Glimpse - Sparsity based weak lensing mass-mapping
   tool <https://github.com/CosmoStat/Glimpse>`__

   -  By [François Lanusse].
      `Glimpse <http://www.cosmostat.org/software/glimpse>`__ is a weak
      lensing mass-mapping tool relying a robust sparsity-based
      regularisation scheme to recover high resolution convergence from
      either gravitational shear alone or from a combination of shear
      and flexion. Please also see `Lanusse et
      al. 2016 <https://arxiv.org/abs/1603.01599>`__

Micro Lensing
-------------

-  `Microlensing Source <http://microlensing-source.org/overview/>`__

   -  A website that summaries a lot of useful resources and data for
      microlensing science.
   -  It also hosts the `Microlensing Data
      Challenge <http://microlensing-source.org/data-challenge/>`__
   -  The data for the challenge can be found `on
      Github <https://github.com/microlensing-data-challenge/data-challenge-1>`__

-  `Microlensing Hack Session at CCA,
   2019 <https://hack.microlensing.science/>`__

   -  There is `a summary of
      resources <https://hack.microlensing.science/resources/>`__ for
      micro-lensing analysis and `a series of interesting micro-lensing
      projects <https://hack.microlensing.science/projects/>`__

Software
~~~~~~~~

-  `muLAn - gravitational MICROlensing Analysis
   Software <https://github.com/muLAn-project/muLAn>`__

   -  **muLAn** is an easy-to-use and flexile software to model
      gravitational microlensing events

-  `MulensModel - Microlensing Modelling
   package <https://github.com/rpoleski/MulensModel>`__

   -  By Radek Poleski. **MulensModel** can generate a microlensing
      light curve for a given set of microlensing parameters, fit that
      light curve to some data, and return a chi2 value

-  `LIA - Gravitational microlensing detection algorithm using machine
   learning <https://github.com/dgodinez77/LIA>`__

   -  **LIA** is an open-source program for detecting microlensing
      events in wide-field surveys

-  `pyLIMA - open source for modeling microlensing
   events <https://github.com/ebachelet/pyLIMA/>`__

   -  Document for **pyLIMA** can be found
      `here <https://ebachelet.github.io/pyLIMA/>`__

-  `VBBinaryLensing - Microlensing light curve
   calculation <https://github.com/valboz/VBBinaryLensing>`__

   -  By Valerio Bozza. **VBBinaryLensing** is a tool for forward
      modelling of gravitational microlensing events using the advanced
      contour integration method It supports single and binary lenses.
