# Basic Tools for Astrophysical Research

## Data format used in astronomy

* [Flexible Image Transport System (FITS)](https://archive.stsci.edu/fits/)
	- The default standard for the exchange of data in astronomy now
	- The [full document of FITS](https://fits.gsfc.nasa.gov/users_guide/usersguide.pdf) and [the MAST data format guidelines](https://archive.stsci.edu/data_format.html)
	- [CFITSIO](https://heasarc.gsfc.nasa.gov/fitsio/) is a library of C and Fortran subroutines for reading and writing data files in FITS.
	- [`astropy.io.fits`](https://docs.astropy.org/en/stable/io/fits/) can help you deal with FITS files in Python
* [Advanced Scientific Data Format (ASDF)](https://github.com/spacetelescope/asdf)
	- Next generation interchange format for scientific data developed by STScI
	- It follows the new [ASDF Standard](https://asdf-standard.readthedocs.io/en/latest/)
* [`HDF5` - High-performance data management and storage suite](https://www.hdfgroup.org/solutions/hdf5/)
	- In the age of big data, HDF5 format is also becoming more popular in astronomy. For example, many hydro-simulations use HDF5 to store large and complex data.
	- [h5py is a Pythonic interface to the HDF5 binary data format](https://www.h5py.org/)
	- [`fits2hdf` is a FITS to HDFITS conversion utility](https://github.com/telegraphic/fits2hdf)
* If you use Python, it is also convenient to use the [`pickle`](https://docs.python.org/3/library/pickle.html) and [`dill`](https://pypi.org/project/dill/) (an even better `pickle`) module for serializing and de-serializing python objects to the majority of the built-in python types.

## World Coordinate Systems (WCS)

* [FITS World Coordinate System (WCS)](https://fits.gsfc.nasa.gov/fits_wcs.html)
	- [`wcslib`](http://www.atnf.csiro.au/people/mcalabre/WCS/wcslib/index.html) is a C library, supplied with a full set of Fortran wrappers, that implements the "World Coordinate System" (WCS) standard in FITS
	- All the tools that deals with FITS format can also deal with WCS information (normally stored in the header). For example, the [`astropy.wcs`](http://docs.astropy.org/en/stable/wcs/)
* [Generalized World Coordinate System](https://gwcs.readthedocs.io/en/latest/)
	- [`gwcs` - provides tools for managing WCS in a general way](https://github.com/spacetelescope/gwcs)
* [`stwcs` - WCS based distortion models and coordinate transformation](https://github.com/spacetelescope/stwcs)
* [`tweakwcs` - Algorithms for matching and aligning catalogs and for tweaking the WCS so as to minimize catalog mismatch errors](https://github.com/spacetelescope/tweakwcs)
	- `tweakwcs` is a package that provides core algorithms for computing and applying corrections to WCS objects such as to minimize mismatch between image and reference catalogs. Currently only aligning images with FITS WCS and JWST gWCS are supported.

## Flux standards

* [The Absolute Magnitude of the Sun](http://mips.as.arizona.edu/~cnaw/sun.html)
	- [Link to download the default composite spectrum of the Sun](http://mips.as.arizona.edu/~cnaw/sun_composite.fits)

* [ESO's RA Ordered List of Spectrophotometric Standards](https://www.eso.org/sci/observing/tools/standards/spectra/stanlis.html)
* [NAOJ's Optical Spectrophotometric Standard Stars](https://www.naoj.org/Observing/Instruments/FOCAS/Detail/UsersGuide/Observing/StandardStar/Spec/SpecStandard.html)
* [ESO's Landolt Equatorial Standards](http://www.eso.org/sci/observing/tools/standards/Landolt.html)

## Plan an observation

* [astroplan - Python package to help astronomers plan observations](https://github.com/astropy/astroplan)
* [iObserve](http://onekilopars.ec/iobserve/)
	- The free on-line version is [here](https://www.arcsecond.io/iobserve)
* [Object Visibility by ING](http://catserver.ing.iac.es/staralt/)
* [JSkyCalc -- A Convenient, Portable Observing Aid](https://www.dartmouth.edu/~physics/labs/skycalc/flyer.html)
* [Keck telescopes' own planning tool](https://www2.keck.hawaii.edu/software/obsplan/obsplan.php)
* [Astronomical Observatory Sites by Latitude and Longitude](http://www.eso.org/~ndelmott/obs_sites.html)

## Flux unit conversion

* [NICMOS Units Conversion Form](http://www.stsci.edu/hst/nicmos/tools/conversion_form.html)
* [Magnitude/Flux Density Converter: Point Sources](http://ssc.spitzer.caltech.edu/warmmission/propkit/pet/magtojy/)

## Filter Response Curves

* [Response curved collected in sedpy package by Ben Johnson](https://github.com/bd-j/sedpy/tree/master/sedpy/data/filters)
* [tynt - Color filter approximations in Python](https://github.com/bmorris3/tynt)
	- By Brett Morris. `tynt` is a super lightweight package containing approximate transmittance curves for more than five hundred astronomical filters, weighing in at just under 150 KB. Document can be found [here](https://tynt.readthedocs.io/en/latest/)

## Extinction calculator

* [NED's extinction calculator](https://ned.ipac.caltech.edu/extinction_calculator)
* [3-D Dust Mapping with Pan-STARRS 1](http://argonaut.skymaps.info)
	- [Query service](http://argonaut.skymaps.info/query)

## Coordinate Service

* [RA, DEC Flexible converter](http://www.astrouw.edu.pl/~jskowron/ra-dec/)
* [NED's coordinate calculator](https://ned.ipac.caltech.edu/coordinate_calculator)

## Managing Catalogs

* [`astropy.table`](https://docs.astropy.org/en/stable/table/) is a flexible Python module that can handle a variant types of tables.
* [`TOPCAT` - Tool for OPerations on Catalogues And Tables](http://www.star.bris.ac.uk/~mbt/topcat/)
	- Really powerful GUI tool to deal with tables. It is written as a Java application.
	- Have great functions for cross-matching catalogs, querying on-line databases, and making publication-grade figures.
	- [`STILTS` - Starlink Tables Infrastructure Library Tool Set] provides most of `TOPCAT`'s capabilities in command line.

### Table cross-match

* [`smatch` - Code to match points on the sphere using the healpix scheme](https://github.com/esheldon/smatch)
	- By Erin Sheldon. Very fast cross-match tool, C-code wrapped in Python.
* [`nway` - Bayesian cross-matching of astronomical catalogues](https://github.com/JohannesBuchner/nway)
	- Bayesian match probabilities based on astronomical sky coordinates (RA, DEC)
* [`C3` - Command-line Catalogue Cross-matching Tool](http://dame.dsf.unina.it/c3.html)
* [`xmatch` - Cross match of catalogs](https://git.ias.u-psud.fr/abeelen/xmatch)
	- By Alexandre Beelen.

## Cosmology Calculator

* [ICRAR's Cosmology Calculator](http://cosmocalc.icrar.org)
	- Based on the [celestial R-code](https://github.com/asgr/celestial)
* [Ned Wright's Cosmology Calculator](http://www.astro.ucla.edu/%7Ewright/CosmoCalc.html)

## Simulate Galaxy Spectrum

* [SpecGen - Mock Galaxy Spectra Generator](http://specgen.icrar.org)

## Sky Projection Maps of Surveys

* [AstroMap - generating sky projection maps for astronomical surveys](http://astromap.icrar.org)
