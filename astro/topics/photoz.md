# Photometric Redshift Tools and Algorithms

* In this new era of extragalactic and cosmological surveys, photometric redshift becomes increasingly more important. And in recent years, there have been many exciting new developments for the photo-z algorithms.

## Template Based

- [EAZY - photometric redshift code](https://github.com/gbrammer/eazy-photoz)
    * __EAZY__ is a photometric redshift code designed to produce high-quality redshifts for situations where complete spectroscopic calibration samples are not available. See [Brammer, van Dokkum & Coppi 2008](http://adsabs.harvard.edu/abs/2008ApJ...686.1503B) for details.
    * [eazy-py - Pythonic photometric redshift tools based on EAZY](https://github.com/gbrammer/eazy-py)

## Machine Learning

- [ANNZ - Machine learning methods for astrophysics](https://github.com/IftachSadeh/ANNZ)
    * By Iftach Sadeh. ANNZ uses both regression and classification techniques for estimation of single-value photo-z (or any regression problem) solutions and PDFs. Includes several "traditional" machine learning algorithms (ANN, BDT, KNN)
- [MLZ - Machine Learning for photo-Z](https://github.com/mgckind/MLZ)
    * MLZ is a python code that computes photometric redshift PDFs using machine learning techniques, providing optional extra information.
- [frankenz - A photometric redshift monstrosity](https://github.com/joshspeagle/frankenz)
    * By Josh Speagle. __frankenz__ is a Pure Python implementation of a variety of methods to quickly yet robustly perform (hierarchical) Bayesian inference using large (but discrete) sets of (possibly noisy) models with (noisy) photometric data.

## Gaussian Process

- [Delight - Photometric redshift via Gaussian processes with physical kernels](https://github.com/ixkael/Delight)
    * By [Boris Leistedt](https://ixkael.github.io/). See [Leistedt & Hogg 2016](https://arxiv.org/abs/1612.00847) for details.


## Clustering

- [the-wizz - A clustering redshift estimation code for us folks](https://github.com/morriscb/the-wizz)
    * By Chris Morrison. __the-wizz__ is a clustering redshift estimating tool designed with ease of use for end users in mind.
    * For information on the method see Schmidt et al. 2013, Menard et al. 2013, and Rahman et al. 2015, 2016b. Details on this implementation can be found in Morrison et al. 2017
