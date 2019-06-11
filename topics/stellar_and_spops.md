# Tools and Resources about Stellar Physics and Stellar Population

## Stellar Evolution Code

* [MESA - Modules for Experiments in Stellar Astrophysics](http://mesa.sourceforge.net/)
    - The most important **open** 1-D stellar evolution code on the market.
* [stars - A Stellar Evolution Code](https://www.ast.cam.ac.uk/~stars/)
    - The classic.
* [BINSTAR - a detailed binary stellar evolution code](https://www.ast.cam.ac.uk/~rgi/binstar.html)

## Isochrones

### Softwares

* [isochrones - Provides simple interface for interacting with stellar model grids](https://github.com/timothydmorton/isochrones)
    - The central goal of isochrones is to standardize model-grid-based stellar parameter inference, and to enable such inference under different sets of stellar models.
    - Online [documents is here](https://isochrones.readthedocs.io/en/latest/)

### Libraries

* [MIST - MESA Isochrones & Stellar Tracks](http://waps.cfa.harvard.edu/MIST/)
    - Key papers: [Choi et al. 2016](http://adsabs.harvard.edu/abs/2016ApJ...823..102C)
* [PARSEC: stellar tracks and isochrones with the PAdova and TRieste Stellar Evolution Code](http://stev.oapd.inaf.it/cgi-bin/cmd)
    - Key papers: [Bressan et al. 2012](https://arxiv.org/abs/1208.4498)
    - [Interpolated PARSEC Stellar Evolution Tracks](https://philrosenfield.github.io/padova_tracks/)
* [Padova database of stellar evolutionary tracks and isochrones](http://pleiadi.pd.astro.it/)
* [YaPSI - Yale-Postdam Stellar Isochrones](http://www.astro.yale.edu/yapsi/)
* [Geneva Grids of Stellar Evolution Models](http://obswww.unige.ch/~ekstrom/WWW/evol/recherche/database.html)
    - [Interactive online tool to generate isochrones](https://www.unige.ch/sciences/astro/evolution/en/database/syclist/)
* [BaSTI - A Bag of Stellar Tracks and Isocrhones](http://basti.oa-teramo.inaf.it/)

## Stellar Spectra Libraries and SED

### Observed

### Theoretical

* [MARCS - a grid of one-dimensional, hydrostatic, plane-parallel and spherical LTE model atmospheres](http://marcs.astro.uu.se/)
    - The MARCS site contains about 52,000 stellar atmospheric models of spectral types F, G and K in 3 different formats and also flux sample files indicating rough surface fluxes.

### Tools

* [BEAST - Bayesian Extinction and Stellar Tool](https://github.com/BEAST-Fitting/beast)
    - Fits the ultraviolet to near-infrared photometric SEDs of stars to extract stellar and dust extinction parameters. See [Gordon et al. 2016](http://adsabs.harvard.edu/abs/2016ApJ...826..104G) for details.
    - Online document is [here](https://beast.readthedocs.io/en/latest/)
* [ThePayne - Artificial Neural-Net compression and fitting of synthetic spectral grids](https://github.com/pacargile/ThePayne)
    - By [Phillip Cargile](https://www.cfa.harvard.edu/~pcargile/) and [Yuan-Sen Ting](https://www.sns.ias.edu/~ting/). Artificial Neural-Net compression and fitting of ab initio synthetic spectral grids.
* [TheCannon - a data-driven method for determining stellar parameters and abundances from stellar spectra](https://github.com/annayqho/TheCannon)
    - By [Anna Ho](https://annayqho.github.io/). A data-driven method for determining stellar labels (physical parameters and chemical abundances) from stellar spectra in the context of large spectroscopic surveys.
* [brutus - Modeling stellar photometry with "brute force" methods](https://github.com/joshspeagle/brutus)
    * By Josh Speagle. A Pure Python package whose core modules involve using "brute force" Bayesian inference to derive distances, reddenings, and stellar properties from photometry using a grid of stellar models.
* [Starfish - Tools for Flexible Spectroscopic Inference](https://github.com/iancze/Starfish)
    - By [Ian Czekala](http://iancze.github.io/). Starfish is a set of tools used for spectroscopic inference. We designed the package to robustly determine stellar parameters using high resolution spectral models
* [MOOG - a code that performs a variety of LTE line analysis and spectrum synthesis tasks](http://www.as.utexas.edu/~chris/moog.html)
    - Old fashion but classic.
    - If you use Python, try Andy Casey's [Installing MOOG the Easy Way](https://github.com/andycasey/moog)


## Stellar Population Synthesis or SED Fitting

* This [`sedfitting.org` page](http://www.sedfitting.org/Models.html) is a very good one-stop shopping place for all SED related resources.
    - There is also a [review paper](http://www.sedfitting.org/Paper_vs1.0_online/walcher_ms.html)

### Tools:

* [FSPS - Flexible Stellar Population Synthesis](https://github.com/cconroy20/fsps)
    - If you want to see how sausage is made, this is it, including every details of stellar population synthesis. Original code in `Frotran`. Supports different isochrones and libraries.
    - [`python-fsps`](http://dfm.io/python-fsps/current/) can help you use it in `Python`
    - [`cloudyfsps` - Python interface between FSPS and Cloudy](https://github.com/nell-byler/cloudyfsps)
* [sedpy - Utilities for astronomical spectral energy distributions](https://github.com/bd-j/sedpy)
    - By Ben Johnson. Modules for storing and operating on astronomical source spectral energy distributions.  
    - Has nice function to handle filters and measure SED from spectrum.
* [PopStar - generating simple stellar populations from synthetic evolution and atmosphere models](https://github.com/astropy/PopStar)
    - PopStar generates single-age, single-metallicity populations (i.e. star clusters). It supports different initial mass functions, multiplicity perscriptions, reddening laws, filter functions, atmosphere models, and evolution models.
    - Support a large variety of theoretical models.

### SED or Spectral Fitting

* [prospector - Python code for Stellar Population Inference from Spectra and SEDs](https://github.com/bd-j/prospector)
    - By Ben Johnson. Conduct principled inference of stellar population properties from photometric and/or spectroscopic data. 


### Models:

* [MILES - Population synthesis for the 21st Century](http://miles.iac.es/)
    - The new extended MILES ([E-MILES](http://adsabs.harvard.edu/abs/2016MNRAS.463.3409V)) models covering from 1680Å to 5.0μm
    - Provides useful [online tools](http://www.iac.es/proyecto/miles/pages/webtools.php) to use the stellar library and SSP models.
* [BPASS - Binary Population and Spectral Synthesis code](https://bpass.auckland.ac.nz/)
    - Best binary population model on the market.
* [PEGASE - Projet d'Etude des GAlaxies par Synthese Evolutive](http://astro.u-strasbg.fr/~morgan/PEGASE.html)