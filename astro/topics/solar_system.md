# Planet Science and Small Bodies in the Solar System

**Just started**

----

## For astrophysicists who is mainly interested in identifying/getting rid of known asteroids in their data:

* Web-based service, good for just checking a few targets: [IAU Minor Planet Center -- Minor Planet Checker](https://www.minorplanetcenter.net/cgi-bin/checkmp.cgi)
    - Only accept certain formats (coordinates need to be sexagesimal, or you need to format your observations in [MPC80COL format](https://www.minorplanetcenter.net/iau/info/OpticalObs.html))
    - No (officially supported) API
* Command-line program that can be executed locally: [astcheck](https://www.projectpluto.com/pluto/devel/astcheck.htm)
    - If you need to check for asteroids regularly and/or have a large number of targets, this is for you
    - You do need to maintain an up-to-date copy of either the [ASTORB dataset](ftp://ftp.lowell.edu/pub/elgb/astorb.html) or the [MPCORB dataset](http://www.projectpluto.com/mpcorb.htm)
    - Be careful about the epochs: it only works when the epoch of your observation matches/is near the epoch of the ASTORB/MPCORB dataset. In other words, be careful if you are checking archival data (you will need to integrate the orbits back to the epoch you want -- use [integrat](https://www.projectpluto.com/pluto/integrat.htm) to do that)
    
## Small Bodies

### Asteroid and Near-Earth Object Survey

* [IAU Minor Planet Center](https://www.minorplanetcenter.net/)
  - [NEO Confirmation Page](https://www.minorplanetcenter.net/iau/NEO/toconfirm_tabular.html)
  - [Possible Comet Confirmation Page](https://www.minorplanetcenter.net/iau/NEO/pccp_tabular.html)
  - [Minor Planet Database](https://www.minorplanetcenter.net/db_search)
  - [MPChecker -- checking for known asteroids/comets](https://www.minorplanetcenter.net/cgi-bin/checkmp.cgi)
  
* [NASA/JPL Center for Near Earth Object Studies](https://cneos.jpl.nasa.gov/)
  - [Small-Body Database](https://ssd.jpl.nasa.gov/horizons.cgi)
    - [PYTHON wrapper: astroquery.jplhorizons](https://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html)
  - [SENTRY -- impact risk of known objects](https://cneos.jpl.nasa.gov/sentry/)
  - [SCOUT -- impact risk of to-be-confirmed objects](https://cneos.jpl.nasa.gov/scout/#/)
  
* [ESA NEODyS](https://newton.spacedys.com/neodys/index.php?pc=7.0)

#### Minor Planet Center Related (be aware: may be outdated/not maintained)

* [`mpc-fetch.py` - fetches properties of all objects that match search params](https://minorplanetcenter.net/mpc-fetch.py)
* [`astroquery.mpc` - Minor Planet Center Queries](https://astroquery.readthedocs.io/en/latest/mpc/mpc.html)
* [`mpc-client` - A python client for the Minor Planet Center's MPC web service](https://github.com/qdonnellan/mpc-client)

### Characterization

* [PYTHON -- Photometry Pipeline](https://photometrypipeline.readthedocs.io/en/latest/)
* [ADAM](https://github.com/matvii/ADAM) -- asteroid shape reconstruction from resolved observations

### General Tools

* [__sbpy__ - A Python package for small bodies research](https://github.com/NASA-Planetary-Science/sbpy)
    - __sbpy__ is a community effort to build a Python package for small-body planetary astronomy in the form of an astropy affiliated package. See the [__sbpy__ website for more](http://mommermi.github.io/)
    - Include functionalities for planning observations, modeling photometry, fitting astrometry and orbit, analysing spectroscopic data, simulating and analysing cometary gas and dust coma, estimating size/albedo of asteroid, enhancing images, and analysing lightcurve.
    - [__sbpy__ Tutorials and Workshops Materials](https://github.com/NASA-Planetary-Science/sbpy-tutorial)

#### [Solar System Geometry](https://naif.jpl.nasa.gov/naif/solar_system_geometry.pdf)

* [__SPICE__ - An Observation Geometry System for Space Science Missions](https://naif.jpl.nasa.gov/naif/)
    - NASA's Navigation and Ancillary Information Facility (NAIF) offers NASA flight projects and NASA funded researchers an observation geometry information system named "SPICE" to assist scientists in planning and interpreting scientific observations from space-based instruments aboard robotic planetary spacecraft.  
    - [The __SPICE__ Toolkit](https://naif.jpl.nasa.gov/naif/toolkit.html) is available in C, Fortran, IDL, and Matlab.
    - [__SpiceyPy__ - Python wrapper for the NAIF C SPICE Toolkit](https://github.com/AndrewAnnex/SpiceyPy)
        - [Online document can be found here](https://spiceypy.readthedocs.io/en/master/)

#### Object Detection

* [__spiops__ - Extension of SPICE functionalities for ESA Missons](https://github.com/esaSPICEservice/spiops)
    - __spiops__ is a library aimed to help scientists and engineers that deal with Solar System Geometry mainly for planetary science


* [__SALTAD__](https://github.com/NASA-Planetary-Science/SALTAD)
    - __SALTAD__ is comprised of a series of C language function modules for image processing multiframe image data to detect moving asteroids in a star cluttered background.

## Planets

* [Gazetteer of Planetary Nomenclature](https://planetarynames.wr.usgs.gov/)
    - The Gazetteer of Planetary Nomenclature is maintained by the Planetary Geomatics Group of the USGS Astrogeology Science Center.

### Modeling and Simulating Planet

* [__Beam__ - A Monte Carlo Radiative Transfer Code for studies of Saturn's Rings](https://github.com/physicsguy42/BEAM_beta)
* [__mpc-fetch.py__ - fetches properties of all objects that match search params](https://minorplanetcenter.net/mpc-fetch.py)
* [__astroquery.mpc__ - Minor Planet Center Queries](https://astroquery.readthedocs.io/en/latest/mpc/mpc.html)
* [__mpc-client__ - A python client for the Minor Planet Center's MPC web service](https://github.com/qdonnellan/mpc-client)