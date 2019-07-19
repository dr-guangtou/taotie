Stellar Physics and Stellar Population
======================================

Stellar Evolution Code
----------------------

-  `MESA - Modules for Experiments in Stellar
   Astrophysics <http://mesa.sourceforge.net/>`__

   -  The most important **open** 1-D stellar evolution code on the
      market.

-  `stars - A Stellar Evolution
   Code <https://www.ast.cam.ac.uk/~stars/>`__

   -  The classic.

-  `BINSTAR - a detailed binary stellar evolution
   code <https://www.ast.cam.ac.uk/~rgi/binstar.html>`__

Hydro-simulation
~~~~~~~~~~~~~~~~

-  `MAEXTROeX - A C++/F90 low Mach number stellar hydrodynamics
   code <https://github.com/AMReX-Astro/MAESTROeX>`__

   -  `MAESTROeX <https://amrex-astro.github.io/MAESTROeX/index.html>`__
      solves the equations of low Mach number hydrodynamics for
      stratified atmospheres/stars with a general equation of state.

Isochrones
----------

Softwares
~~~~~~~~~

-  `isochrones - Provides simple interface for interacting with stellar
   model grids <https://github.com/timothydmorton/isochrones>`__

   -  The central goal of isochrones is to standardize model-grid-based
      stellar parameter inference, and to enable such inference under
      different sets of stellar models.
   -  Online `documents is
      here <https://isochrones.readthedocs.io/en/latest/>`__

Libraries
~~~~~~~~~

-  `MIST - MESA Isochrones & Stellar
   Tracks <http://waps.cfa.harvard.edu/MIST/>`__

   -  Key papers: `Choi et
      al. 2016 <http://adsabs.harvard.edu/abs/2016ApJ...823..102C>`__

-  `PARSEC: stellar tracks and isochrones with the PAdova and TRieste
   Stellar Evolution Code <http://stev.oapd.inaf.it/cgi-bin/cmd>`__

   -  Key papers: `Bressan et
      al. 2012 <https://arxiv.org/abs/1208.4498>`__
   -  `Interpolated PARSEC Stellar Evolution
      Tracks <https://philrosenfield.github.io/padova_tracks/>`__

-  `Padova database of stellar evolutionary tracks and
   isochrones <http://pleiadi.pd.astro.it/>`__
-  `YaPSI - Yale-Postdam Stellar
   Isochrones <http://www.astro.yale.edu/yapsi/>`__
-  `Geneva Grids of Stellar Evolution
   Models <http://obswww.unige.ch/~ekstrom/WWW/evol/recherche/database.html>`__

   -  `Interactive online tool to generate
      isochrones <https://www.unige.ch/sciences/astro/evolution/en/database/syclist/>`__

-  `BaSTI - A Bag of Stellar Tracks and
   Isocrhones <http://basti.oa-teramo.inaf.it/>`__

Stellar Spectra Libraries and SED
---------------------------------

Observed
~~~~~~~~

-  `Pickles et al. 1998
   library <https://www.eso.org/sci/facilities/paranal/decommissioned/isaac/tools/lib.html>`__

   -  The spectral range is 1150-25000 Anstroms, sampling 5 Angstroms.
      131 stellar spectra.
   -  The `Pickles library can also be found
      here <http://www.stsci.edu/hst/observatory/crds/pickles_atlas.html>`__

-  `The Indo-U.S. Library of Coudé Feed Stellar
   Spectra <https://www.noao.edu/cflib/>`__

   -  1273 stars obtained with the 0.9m Coudé Feed telescope at Kitt
      Peak National Observatory
   -  Original dispersion of 0.44 Angstroms/pixel, at a resolution of ~1
      Angstroms FWHM.
   -  Cover the entire wavelength range of 3460 Angstroms to 9464
      Angstroms

-  `MILES Stellar
   Library <http://www.iac.es/proyecto/miles/pages/stellar-libraries.php>`__

   -  **MILES**: ~1000 stars spanning a large range in atmospheric
      parameters. The spectra were obtained at the 2.5m INT telescope
      and cover the range 3525-7500 Å at 2.5 Å (FWHM) spectral
      resolution
   -  **CaII Triplet Library**: 700 stars with spectra around the Ca II
      triplet region. Cover the spectral range between 8350-9020 Å at
      1.5 Å (FWHM)

-  `The X-Shooter Spectral Library <http://xsl.u-strasbg.fr/>`__

   -  The current release contains more than 200 stars. 3000–25000 Å all
      stellar spectra observed at a resolving power of R = λ/Δλ ~ 10000
      with the medium-resolution spectrograph X-Shooter

-  `MaStar - MaNGA Stellar
   Library <https://www.sdss.org/surveys/mastar/>`__

   -  A stellar spectral library with a very comprehensive stellar
      parameter coverage, a large sample size, and high quality
      calibrations, using the same instrument as used by the MaNGA
      survey
   -  Wavelength: 362-1035 nm, resolution R~2000; More than 8000 stars
      in wide areas of the sky.

-  `STELIB Stellar
   Library <http://svo2.cab.inta-csic.es/vocats/v2/stelib/>`__

   -  A stellar Library for stellar population synthesis models
   -  An homogeneous library of stellar spectra in the visible range
      (3200 to 9500A), including stars of all spectral types, luminosity
      classes and metallicity. The spectral resolution of our Stellar
      Library is about 3A FWHM.

-  `ÉLODIE Stellar Library <http://atlas.obs-hp.fr/elodie/>`__

   -  A stellar database of 1959 spectra for 1503 stars, observed with
      the echelle spectrograph ÉLODIE on the 193 cm telescope at the
      Observatoire de Haute Provence.
   -  Wavelength range is 400-680 nm. For the purpose of population
      synthesis, the original resolution R=42 000 has been reduced to
      R=10 000 at lambda=550 nm, or more precisely to a gaussian
      instrumental profile of FWHM~0.55 A over the whole range of
      wavelengths.

-  `INGS Stellar Library <https://lco.global/~apickles/INGS/>`__

   -  INGS is a compendium of 143 stellar-type spectra formed from
      spectra of stars of similar type from 3 sources: 1) IUE: 1153A to
      3201A, 2A/pixel, 2) NGSL v2: 1600A to 11000A; 3) SpeX/IRTF: 8110A
      to 25000+A, 2.5,3,5A/pixel

-  `The Gaia FGK Benchmark
   Stars <https://www.blancocuaresma.com/s/benchmarkstars>`__

   -  Library of high resolution and high signal to noise ratio stellar
      spectra
   -  A homogeneous library in the visual range (480-680 nm) of high
      resolution and signal to noise ratio (S/N) spectra corresponding
      to the 34 Benchmark Stars and 5 metal-poor candidates.

Near-Mid Infrared
^^^^^^^^^^^^^^^^^

-  `IRTF Extended Spectral
   Library <http://irtfweb.ifa.hawaii.edu/~spex/IRTF_Extended_Spectral_Library/>`__

   -  A collection of 0.7-2.5 μm (with a subset from 0.8 to 5.2 μm)
      mostly stellar spectra observed at a resolving power of R ≡ λ/Δλ ~
      2000 with the medium-resolution spectrograph, SpeX. Please see
      `Villaume et al. 2017 for
      details <https://arxiv.org/abs/1705.08906>`__
   -  The original `IRTF spectral library is available
      here <http://irtfweb.ifa.hawaii.edu/~spex/IRTF_Spectral_Library/>`__

-  `SpeX Prism
   Library <http://pono.ucsd.edu/~adam/browndwarfs/spexprism/>`__

   -  A repository of low-resolution, near-infrared spectra, primarily
      of low-temperature dwarf stars and brown dwarfs
   -  Resolutions are R~75-200. Wavelength coverage is 0.65-2.55 microns
      in a single order

Theoretical
~~~~~~~~~~~

-  `MARCS - a grid of one-dimensional, hydrostatic, plane-parallel and
   spherical LTE model atmospheres <http://marcs.astro.uu.se/>`__

   -  The MARCS site contains about 52,000 stellar atmospheric models of
      spectral types F, G and K in 3 different formats and also flux
      sample files indicating rough surface fluxes.

-  `SYNTHE - synthetic library of stellar
   spectra <http://cdsarc.u-strasbg.fr/viz-bin/qcat?J/A+A/442/1127>`__

   -  Covers the wavelength region from 2500 Å to 1.05 μm at a spectral
      resolution of σ=6.4 km/s, R=20,000.

-  `UVBLUE - A High-resolution Theoretical Library of Stellar
   Spectra <https://www.inaoep.mx/~modelos/uvblue/uvblue.html>`__

   -  A high-resolution library of synthetic spectra of stars covering
      the ultraviolet wavelength range.
   -  Stellar spectra cover the wavelength interval from 850 to 4700 Å,
      at a spectral resolving power R = λ/Δ λ = 50,000. The grid
      consists of 1770 SEDs

-  `Paula Coelho’s Theoretical Spectra of Stars and Stellar
   Populations <http://specmodels.iag.usp.br/>`__

   -  A new theoretical library which covers 3000 <= Teff <= 25 000 K,
      -0.5 <= log g <= 5.5 and 12 chemical mixtures covering 0.0017 <= Z
      <= 0.049 at both scaled-solar and alpha-enhanced compositions.

Tools for Stellar Physics
~~~~~~~~~~~~~~~~~~~~~~~~~

-  `BEAST - Bayesian Extinction and Stellar
   Tool <https://github.com/BEAST-Fitting/beast>`__

   -  Fits the ultraviolet to near-infrared photometric SEDs of stars to
      extract stellar and dust extinction parameters. See `Gordon et
      al. 2016 <http://adsabs.harvard.edu/abs/2016ApJ...826..104G>`__
      for details.
   -  Online document is
      `here <https://beast.readthedocs.io/en/latest/>`__

-  `ThePayne - Artificial Neural-Net compression and fitting of
   synthetic spectral grids <https://github.com/pacargile/ThePayne>`__

   -  By `Phillip Cargile <https://www.cfa.harvard.edu/~pcargile/>`__
      and `Yuan-Sen Ting <https://www.sns.ias.edu/~ting/>`__. Artificial
      Neural-Net compression and fitting of ab initio synthetic spectral
      grids.

-  `TheCannon - a data-driven method for determining stellar parameters
   and abundances from stellar
   spectra <https://github.com/annayqho/TheCannon>`__

   -  By `Anna Ho <https://annayqho.github.io/>`__. A data-driven method
      for determining stellar labels (physical parameters and chemical
      abundances) from stellar spectra in the context of large
      spectroscopic surveys.

-  `brutus - Modeling stellar photometry with “brute force”
   methods <https://github.com/joshspeagle/brutus>`__

   -  By Josh Speagle. A Pure Python package whose core modules involve
      using “brute force” Bayesian inference to derive distances,
      reddenings, and stellar properties from photometry using a grid of
      stellar models.

-  `Starfish - Tools for Flexible Spectroscopic
   Inference <https://github.com/iancze/Starfish>`__

   -  By `Ian Czekala <http://iancze.github.io/>`__. Starfish is a set
      of tools used for spectroscopic inference. We designed the package
      to robustly determine stellar parameters using high resolution
      spectral models

-  `MOOG - a code that performs a variety of LTE line analysis and
   spectrum synthesis
   tasks <http://www.as.utexas.edu/~chris/moog.html>`__

   -  Old fashion but classic.
   -  If you use Python, try Andy Casey’s `Installing MOOG the Easy
      Way <https://github.com/andycasey/moog>`__

-  `StePar - an automatic code used to infer stellar atmospheric
   parameters using the EW
   method <https://github.com/hmtabernero/StePar>`__

   -  Please see `Tabernero et
      al. 2019 <https://arxiv.org/pdf/1907.06512.pdf>`__ for more
      details.

-  `MINESweeper - MIST Isochrones with NEsted
   Sampling <https://github.com/pacargile/MINESweeper>`__

   -  Isochrone fitting code using latest mass-tracks from the MIST
      models.
   -  Model interpolation and nested-sampling inference of observed
      stellar SED and/or parameters using the latest MIST stellar
      evolution models.
   -  Based on the work of `Cargile et
      al. 2019 <https://arxiv.org/pdf/1907.07690.pdf>`__

Stellar Population Synthesis or SED Fitting
-------------------------------------------

-  This `sedfitting.org page <http://www.sedfitting.org/Models.html>`__
   is a very good one-stop shopping place for all SED related resources.

   -  There is also a `review
      paper <http://www.sedfitting.org/Paper_vs1.0_online/walcher_ms.html>`__

Tools for Generating or Manipulating Stellar Population Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `FSPS - Flexible Stellar Population
   Synthesis <https://github.com/cconroy20/fsps>`__

   -  If you want to see how sausage is made, this is it, including
      every details of stellar population synthesis. Original code in
      **Frotran**. Supports different isochrones and libraries.
   -  `python-fsps <http://dfm.io/python-fsps/current/>`__ can help you
      use it in **Python**
   -  `cloudyfsps - Python interface between FSPS and
      Cloudy <https://github.com/nell-byler/cloudyfsps>`__

-  `sedpy - Utilities for astronomical spectral energy
   distributions <https://github.com/bd-j/sedpy>`__

   -  By Ben Johnson. Modules for storing and operating on astronomical
      source spectral energy distributions.
   -  Has nice function to handle filters and measure SED from spectrum.

-  `PopStar - generating simple stellar populations from synthetic
   evolution and atmosphere
   models <https://github.com/astropy/PopStar>`__

   -  PopStar generates single-age, single-metallicity populations
      (i.e. star clusters). It supports different initial mass
      functions, multiplicity perscriptions, reddening laws, filter
      functions, atmosphere models, and evolution models.
   -  Support a large variety of theoretical models.

Tools for SED or Spectral Fitting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `prospector - Python code for Stellar Population Inference from
   Spectra and SEDs <https://github.com/bd-j/prospector>`__

   -  By Ben Johnson. Conduct principled inference of stellar population
      properties from photometric and/or spectroscopic data.
   -  Bayesian method, can use **emcee**, **nestle**, and **dynesty** as
      sampling tool
   -  Can fit spectrum and/or SED.

-  `fastpp - C++ version of the SED fitting code FAST (Kriek et
   al. 2009); <https://github.com/cschreib/fastpp>`__

   -  By Corentin Schreiber. “it’s faster, uses less memory, and has
      more features.”
   -  Based on model grid.
   -  Can fit spectrum and/or SED.

-  `STARLIGHT - Spectra decomposition
   code <http://www.starlight.ufsc.br/>`__

   -  Written in Fortran, using simulated annealing algorithm with
      Markov chains.
   -  `The manual written by Cid
      Fernandes <http://minerva.ufsc.br/starlight/files/papers/Manual_StCv04.pdf>`__
      is a very good introduction of the SSP decomposition business.
   -  Mostly used for spectral fitting.

-  `pPXF - Penalized
   Pixel-Fitting <http://www-astro.physics.ox.ac.uk/~mxc/software/#ppxf>`__

   -  By Michelle Cappellari. Extract the stellar or gas kinematics and
      stellar population from galaxy spectra via full spectrum fitting.
   -  Available in Python and IDL. Can fit spectrum.

-  `iSEDfit - IDL routines to fit
   SED <https://github.com/moustakas/impro>`__

   -  By John Moustakas. Part of the **impro** suite. `Website for
      downloading library and documents is
      here <http://www.sos.siena.edu/~jmoustakas/isedfit/>`__
   -  Based on model grid, only fit SED.

-  `Firefly – A Full Spectral Fitting
   Code <https://github.com/FireflySpectra/firefly_release>`__

   -  FIREFLY is a chi-squared minimisation fitting code for deriving
      the stellar population properties of stellar systems, be these
      observed galaxy or star cluster spectra, or model spectra from
      simulations. Document can be `found
      here <http://www.icg.port.ac.uk/firefly/>`__

-  `cigale - Python version of the Code Investigating GALaxy
   Emission <https://gitlab.lam.fr/cigale/cigale/>`__

   -  `Full document can be found here <https://cigale.lam.fr/>`__

-  `FIT3D - a tool for fitting stellar populations and emission lines in
   optical
   spectroscopy <http://www.astroscu.unam.mx/~sfsanchez/FIT3D/>`__

   -  FIT3D is a package for fitting optical spectra to deblend the
      underlying stellar population and the ionized gas, and extract
      physical information from each component. Focusing on IFU surveys.
   -  Fit full spectrum. In Python or Perl

-  `BEAGLE - BayEsian Analysis of GaLaxy
   sEds <http://www.jacopochevallard.org/beagle/>`__

   -  A new-generation tool to model and interpret galaxy spectral
      energy distributions (SEDs) developed by Jacopo Chevallard (ESA)
      and Stephane Charlot (IAP).

Stellar Population Models:
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `MILES - Population synthesis for the 21st
   Century <http://miles.iac.es/>`__

   -  The new extended MILES
      (`E-MILES <http://adsabs.harvard.edu/abs/2016MNRAS.463.3409V>`__)
      models covering from 1680Å to 5.0μm
   -  Provides useful `online
      tools <http://www.iac.es/proyecto/miles/pages/webtools.php>`__ to
      use the stellar library and SSP models.

-  `BPASS - Binary Population and Spectral Synthesis
   code <https://bpass.auckland.ac.nz/>`__

   -  Best binary population model on the market.

-  `PEGASE - Projet d’Etude des GAlaxies par Synthese
   Evolutive <http://astro.u-strasbg.fr/~morgan/PEGASE.html>`__
