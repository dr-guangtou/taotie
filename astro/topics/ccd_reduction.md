# Image Redcution and CCD Related

* On the general topic of optical/NIR detector and data reduction.

## Tutorial and Guide

* [A guide to CCD data reduction and stellar photometry using astropy and affiliated packages](https://github.com/mwcraig/ccd-reduction-and-photometry-guide)
    - Only use __astropy__ affiliated Python packages.

## Software

### Display CCD Images

* [__SAOImage DS9__ - Astronomical imaging and data visualization application](http://ds9.si.edu/site/Home.html)
    - DS9 supports FITS images and binary tables, multiple frame buffers, region manipulation, and many scale algorithms and colormaps. DS9 is actually a very powerful tool for displaying and manipulating image. [Here is a very nice guide](http://www.jb.man.ac.uk/~gbendo/Sci/Pict/DS9guide.pdf)
    - [__pyds9__ - Python connection to SAOimage DS9 via XPA](https://github.com/ericmandel/pyds9)

* [__imexam__ by astropy - Python version of the famous imexamine in IRAF](https://github.com/spacetelescope/imexam)
    - __imexam__ is a python tool for simple image examination, and plotting, with similar functionality to IRAF's imexamine. [Online document is here](https://imexam.readthedocs.io/en/latest/)

* [__ginga__ - astronomical FITS file viewer](https://github.com/ejeschke/ginga)
    - __Ginga__ is a toolkit designed for building viewers for scientific image data in Python, visualizing 2D pixel data in numpy arrays. [Online document is here](https://ginga.readthedocs.io/en/latest/)

* [__regions__ by astropy - Astropy affiliated package for region handling](https://github.com/astropy/regions)

### General Reduction

* Modern imaging surveys or major astronomical cameras are often equipped with speciallized data reduction pipelines. For example:
    - [DECam Community Pipeline](https://www.noao.edu/noao/staff/fvaldes/CPDocPrelim/PL201_3.html)
    - [The Elixir System for CFHT MegaCam](https://www.cfht.hawaii.edu/Instruments/Elixir/)
    - [The HSC Pipeline](https://hsc.mtk.nao.ac.jp/pipedoc/pipedoc_6_e/index.html)
* [__ccdproc__ - Astropy affiliated package for reducing optical/IR CCD data](https://github.com/astropy/ccdproc)
    - __ccdproc__ is is an affiliated package for the AstroPy package for basic data reductions of CCD images. The ccdproc package provides many of the necessary tools for processing of ccd images built on a framework to provide error propagation and bad pixel tracking throughout the reduction process. [Documents can be found here](https://ccdproc.readthedocs.io/en/latest/)

### Image Detrend and Correction

#### Cosmic Ray Removal

* [__astroscrappy__ by astropy - Speedy Cosmic Ray Annihilation Package in Python](https://github.com/astropy/astroscrappy)
    - __Astro-SCRAPPY__ is designed to detect cosmic rays in images (numpy arrays), based on Pieter van Dokkum's __L.A.Cosmic__ algorithm.
* [The original __L.A.Cosmic__ code - Laplacian Cosmic Ray Identification](http://www.astro.yale.edu/dokkum/lacosmic/)
    - [__lacosmicx__ - A fast implementation of the LA Cosmic algorithm](https://github.com/cmccully/lacosmicx)

#### Satellite Trail Removal 

* [__ASTRiDE__ - Automated Streak Detection for Astronomical Images](https://github.com/dwkim78/ASTRiDE)
    - By Dae-Won Kim. __ASTRiDE__ aims to detect streaks in astronomical images using a "border" of each object 
* [__pyradon__ - Python tools for streak detection in astronomical images using the Fast Radon Transform](https://github.com/guynir42/pyradon)
    - By Guy Nir. Based on [Optimal and Efficient Streak Detection in Astronomical Images](https://arxiv.org/abs/1806.04204). The [Matlab version is here](https://github.com/guynir42/radon)

#### "Brighter-Fatter" Effect

* The "Brighter-Fatter" effect is a direct consequence of the distortions of the drift electric field sourced by charges accumulated within the CCD during the exposure and experienced by forthcoming light-induced charges in the same exposure. It affects both deep-depleted and thinned CCD sensors.
* [The brighter-fatter effect and pixel correlations in CCD sensors](https://ui.adsabs.harvard.edu/abs/2014JInst...9C3048A/abstract)
* [The Brighter-Fatter and other sensor effects in CCD simulations for precision astronomy](https://ui.adsabs.harvard.edu/abs/2015JInst..10C5015W/abstract)
* [Exploring the Brighter-fatter Effect with the Hyper Suprime-Cam](https://ui.adsabs.harvard.edu/abs/2018AJ....155..258C/abstract)
* [Brighter-fatter effect in near-infrared detectors -- I. Theory of flat auto-correlations](https://arxiv.org/abs/1906.01846)
    - [__nghxrg__ - Teledyne HxRG Read Noise Generator](https://github.com/BJRauscher/nghxrg)
* [Brighter-fatter effect in near-infrared detectors -- II. Auto-correlation analysis of H4RG-10 flats](https://arxiv.org/abs/1906.01847)
* [Is Flat fielding Safe for Precision CCD Astronomy?](https://ui.adsabs.harvard.edu/abs/2017PASP..129h4502B/abstract)


### Astrometric Calibration

* [__Astrometry.net__ -- automatic recognition of astronomical images](https://github.com/dstndstn/astrometry.net)
	- Made by Dustin Lang. The best astrometric calibration tool on the market.
* [__SCAMP__ from Astromatic.net](https://www.astromatic.net/software/scamp)
    - __SCAMP__ reads SExtractor catalogs and computes astrometric and photometric solutions for any arbitrary sequence of FITS images in a completely automatic way.

### Photometric Calibration

* [__FGCM__ - Forward Global Calibration Method](https://github.com/erykoff/fgcm)
    - Based on the algorithm developed in [Forward Global Photometric Calibration of the Dark Energy Survey in Burke et al. 2018](http://adsabs.harvard.edu/abs/2018AJ....155...41B)
    - The [FGCM Cookbook](https://github.com/lsst/fgcmcal/blob/master/cookbook/README.md) is very good place to start.
    - The [Global Photometric Calibration in LSST with FGCM](https://github.com/lsst/fgcmcal)

### Image Reproection and Co-addition

* [__drizzle__ - A package for combining dithered images into a single image](https://github.com/spacetelescope/drizzle)
    - The drizzle library is a Python package for combining dithered images into a single image. This library is derived from code used in DrizzlePac. Like DrizzlePac, most of the code is implemented in the C language.
    - [The original __drizzlepac__ library for HST images](https://github.com/spacetelescope/drizzlepac)
    - [The online document for __DrizzlePac__](https://drizzlepac.readthedocs.io/en/latest/#)

* [__reproject__ by astropy - Python-based Astronomical image reprojection](https://github.com/astropy/reproject)
    - By reprojection, we mean the re-gridding of images from one world coordinate system to another (for example changing the pixel resolution, orientation, coordinate system).
* [__SWarp__ by Astromatic.net](https://www.astromatic.net/software/swarp)
    - __SWarp__ is a program that resamples and co-adds together FITS images using any arbitrary astrometric projection defined in the WCS standard

* [__Montage__ - Image Mosaic Software for Astronomers](http://montage.ipac.caltech.edu/)
    - __Montage__ is a toolkit for assembling Flexible Image Transport System (FITS) images into custom mosaics. [Online document is here](http://montage.ipac.caltech.edu/docs/index.html)
    - It is also on [Github](https://github.com/Caltech-IPAC/Montage). And there is an [Image Mosaic Service](http://hachi.ipac.caltech.edu:8080/montage) for 2MASS, SDSS, WISE images.
    - [__montage-wrapper__ - Python wrapper for the Montage mosaicking toolkit](https://github.com/astropy/montage-wrapper)
        - This package provides a python wrapper to the Montage Astronomical Image Mosaic Engine
        - [Jupyter notebooks illustrating the use of the Python version of Montage](https://github.com/Caltech-IPAC/MontageNotebooks)
