# CCD and Image Reduction Related

* On the general topic of optical/NIR detector and data reduction.

## Tutorial and Guide

* [A guide to CCD data reduction and stellar photometry using astropy and affiliated packages](https://github.com/mwcraig/ccd-reduction-and-photometry-guide)
    - Only use `astropy` affiliated Python packages.

## Software

### Display CCD Images

* ['SAOImage DS9` - Astronomical imaging and data visualization application](http://ds9.si.edu/site/Home.html)
    - DS9 supports FITS images and binary tables, multiple frame buffers, region manipulation, and many scale algorithms and colormaps. DS9 is actually a very powerful tool for displaying and manipulating image. [Here is a very nice guide](http://www.jb.man.ac.uk/~gbendo/Sci/Pict/DS9guide.pdf)
    - [`pyds9` - Python connection to SAOimage DS9 via XPA](https://github.com/ericmandel/pyds9)

* [`imexam` by astropy - Python version of the famous imexamine in IRAF](https://github.com/spacetelescope/imexam)
    - `imexam` is a python tool for simple image examination, and plotting, with similar functionality to IRAF's imexamine. [Online document is here](https://imexam.readthedocs.io/en/latest/)

* [`ginga` - astronomical FITS file viewer](https://github.com/ejeschke/ginga)
    - `Ginga` is a toolkit designed for building viewers for scientific image data in Python, visualizing 2D pixel data in numpy arrays. [Online document is here](https://ginga.readthedocs.io/en/latest/)

* [`regions` by astropy - Astropy affiliated package for region handling](https://github.com/astropy/regions)

### General Reduction

* Modern imaging surveys or major astronomical cameras are often equipped with speciallized data reduction pipelines.
* [`ccdproc` - Astropy affiliated package for reducing optical/IR CCD data](https://github.com/astropy/ccdproc)
    - `ccdproc` is is an affiliated package for the AstroPy package for basic data reductions of CCD images. The ccdproc package provides many of the necessary tools for processing of ccd images built on a framework to provide error propagation and bad pixel tracking throughout the reduction process. [Documents can be found here](https://ccdproc.readthedocs.io/en/latest/)

### Image Detrend and Correction

* [`astroscrappy` by astropy - Speedy Cosmic Ray Annihilation Package in Python](https://github.com/astropy/astroscrappy)
    - `Astro-SCRAPPY` is designed to detect cosmic rays in images (numpy arrays), based on Pieter van Dokkum's `L.A.Cosmic` algorithm.
* [The original `L.A.Cosmic` code - Laplacian Cosmic Ray Identification](http://www.astro.yale.edu/dokkum/lacosmic/)
    - [`lacosmicx` - A fast implementation of the LA Cosmic algorithm](https://github.com/cmccully/lacosmicx)

### Astrometric Calibration

* [`Astrometry.net` -- automatic recognition of astronomical images](https://github.com/dstndstn/astrometry.net)
	- Made by Dustin Lang. The best astrometric calibration tool on the market.
* [`SCAMP` from Astromatic.net](https://www.astromatic.net/software/scamp)
    - `SCAMP` reads SExtractor catalogs and computes astrometric and photometric solutions for any arbitrary sequence of FITS images in a completely automatic way.

### Photometric Calibration

* [`FGCM` - Forward Global Calibration Method](https://github.com/erykoff/fgcm)
    - Based on the algorithm developed in [Forward Global Photometric Calibration of the Dark Energy Survey in Burke et al. 2018](http://adsabs.harvard.edu/abs/2018AJ....155...41B)
    - The [FGCM Cookbook](https://github.com/lsst/fgcmcal/blob/master/cookbook/README.md) is very good place to start.
    - The [Global Photometric Calibration in LSST with FGCM](https://github.com/lsst/fgcmcal)

### Image Reproection and Co-addition

* [`drizzle` - A package for combining dithered images into a single image](https://github.com/spacetelescope/drizzle)
    - The drizzle library is a Python package for combining dithered images into a single image. This library is derived from code used in DrizzlePac. Like DrizzlePac, most of the code is implemented in the C language.
    - [The original `drizzlepac` library for HST images](https://github.com/spacetelescope/drizzlepac)
    - [The online document for `DrizzlePac`](https://drizzlepac.readthedocs.io/en/latest/#)

* [`reproject` by astropy - Python-based Astronomical image reprojection](https://github.com/astropy/reproject)
    - By reprojection, we mean the re-gridding of images from one world coordinate system to another (for example changing the pixel resolution, orientation, coordinate system).
* [`SWarp` by Astromatic.net](https://www.astromatic.net/software/swarp)
    - `SWarp` is a program that resamples and co-adds together FITS images using any arbitrary astrometric projection defined in the WCS standard

* [`Montage` - Image Mosaic Software for Astronomers](http://montage.ipac.caltech.edu/)
    - `Montage` is a toolkit for assembling Flexible Image Transport System (FITS) images into custom mosaics. [Online document is here](http://montage.ipac.caltech.edu/docs/index.html)
    - It is also on [Github](https://github.com/Caltech-IPAC/Montage). And there is an [Image Mosaic Service](http://hachi.ipac.caltech.edu:8080/montage) for 2MASS, SDSS, WISE images.
    - [`montage-wrapper` - Python wrapper for the Montage mosaicking toolkit](https://github.com/astropy/montage-wrapper)
        - This package provides a python wrapper to the Montage Astronomical Image Mosaic Engine
        - [Jupyter notebooks illustrating the use of the Python version of Montage](https://github.com/Caltech-IPAC/MontageNotebooks)
