# Transients and Other Time Series Science

* Focusing on the detection and analysis of any object that shows flux variation.
    - For example: variable stars, TDE, and eclipsing binaries.
    - **Exoplanet** and **supernova** are also trasients, but they have much broader impact therefore they have their own topics.

## Transient Notification

- [__pycgn__ - Python package for processing Gamma-ray Coordinates Network (GCN) notices and circulars ](https://github.com/lpsinger/pygcn)
    * Anonymous VOEvent client for receiving GCN/TAN notices in XML format

## Data Access

- [__ztfquery__ - Access ZTF data from Python](https://github.com/MickaelRigault/ztfquery)
    * By Mickael Rigault. __ztfquery__ is a python tool to download ZTF (and SEDM) data

## Differential Photometry

- [__lemon__ - Differential photometry for humans (and astronomers)](https://github.com/vterron/lemon)
    * By Víctor Terrón. __LEMON__ is a differential-photometry pipeline, written in Python, that determines the changes in the brightness of astronomical objects over time and compiles their measurements into light curves.
- [__hotpants__ - High Order Transform of Psf ANd Template Subtraction code](https://github.com/acbecker/hotpants)
    * By Andy Becker.
- [__astrobase__ - Python modules for light curve work and variable star astronomy](https://github.com/waqasbhatti/astrobase)
    * By [Waqas Bhatti](https://wbhatti.org/). It includes implementations of several period-finding algorithms, batch work drivers for working on large collections of light curves, and a small web-app useful for reviewing and classifying light curves by stellar variability type.

## Trasient Identification and Classification

- [__avocado__ - Photometric Classification of Astronomical Transients and Variables With Biased Spectroscopic Samples](https://github.com/kboone/avocado)
    * __Avocado__ is a general photometric classification code that is designed to produce classifications of arbitrary astronomical transients and variable objects. 
    * The original codebase of avocado was developed for and won the [2018 Kaggle PLAsTiCC challenge](https://www.kaggle.com/c/PLAsTiCC-2018). 

- [__astrorapid__ - Real-time Automated Photometric IDentification (RAPID) of astronomical transients using deep learning](https://github.com/daniel-muthukrishna/astrorapid)
    * By [Daniel Muthukrishna](http://www.danielmuthukrishna.com/). __RAPID__ (Real-time Automated Photometric IDentification) can classify multiband photometric light curves into several different transient classes. It uses a deep recurrent neural network to produce time-varying classifications.

- [__astrodash__ - Deep learning for the automated spectral classification of supernovae](https://github.com/daniel-muthukrishna/astrodash)
    * By [Daniel Muthukrishna](http://www.danielmuthukrishna.com/). Software to classify the type, age, redshift and host for any supernova spectra. Two platforms exists: a python library that enables a user to classify several spectra (can classify thousands of spectra in seconds), and also a graphical interface that enables a user to view and classify a spectrum. 

- [__UPSILoN__- Automated Classification of Periodic Variable Stars Using Machine Learning](https://github.com/dwkim78/upsilon)
    * __UPSILoN__ (AUtomated Classification of Periodic Variable Stars using MachIne LearNing)

- [__SuperNNova__ - Open Source Photometric classification](https://github.com/supernnova/SuperNNova/)
    * Using recurrent network technique. Based on [SuperNNova: an open-source framework for Bayesian, Neural Network based supernova classification](https://arxiv.org/abs/1901.06384)

## Lightcurve and Exoplanet

- [__lightkurve__ - A friendly package for Kepler & TESS time series analysis in Python](https://github.com/KeplerGO/lightkurve)
    * __Lightkurve__ is a community-developed, open-source Python package which offers a beautiful and user-friendly way to analyze astronomical flux time series data, in particular the pixels and lightcurves obtained by NASA's Kepler and TESS exoplanet missions.

- [__eleanor__ - light curves from TESS](https://github.com/afeinstein20/eleanor)
    * __eleanor__ is a python package to extract target pixel files from TESS Full Frame Images and produce systematics-corrected light curves for any star observed by the TESS mission.

- [__starry__ - Analytic occultation light curves for astronomy](https://github.com/rodluger/starry)
    * By [Rodrigo Luger](https://rodluger.github.io/). Based on [a very nice paper](https://docs.google.com/viewer?url=https://github.com/rodluger/starry/raw/master-pdf/tex/starry.pdf)

- [__everest__ - EPIC Variability Extraction and Removal for Exoplanet Science Targets](https://github.com/rodluger/everest)
    * A pipeline for de-trending K2 light curves with pixel level decorrelation and Gaussian processes.]

- [__wotan__ - Automagically remove trends from time-series data](https://github.com/hippke/wotan)
    * By [Michael Hippke](http://www.jaekle.info/). Offers free and open source algorithms to automagically remove trends from time-series data.
