# Solar System Related

**Just started**

----

## Data

* [IAU Minor Planet Center](https://minorplanetcenter.net/iau/mpc.html)
    - The MPC is responsible for the designation of minor bodies in the solar system: minor planets; comets; and natural satellites. The MPC is also responsible for the efficient collection, computation, checking and dissemination of astrometric observations and orbits for minor planets and comets
    - For [data available from the minor planet center](https://minorplanetcenter.net/data)
    - [MPC Web Service](https://minorplanetcenter.net//web_service): is providing a web service interface to users, allowing them to programmatically fetch minor planet properties data from the MPC's database. 
    - [Minor Planet & Comet Ephemeris Service](https://www.minorplanetcenter.net/iau/MPEph/MPEph.html)

* [Gazetteer of Planetary Nomenclature](https://planetarynames.wr.usgs.gov/)
    - The Gazetteer of Planetary Nomenclature is maintained by the Planetary Geomatics Group of the USGS Astrogeology Science Center.

## Tools

* [`sbpy` - A Python package for small bodies research](https://github.com/NASA-Planetary-Science/sbpy)
    - `sbpy` is a community effort to build a Python package for small-body planetary astronomy in the form of an astropy affiliated package. See the [`sbpy` website for more](http://mommermi.github.io/)
    - Include functionalities for planning observations, modeling photometry, fitting astrometry and orbit, analysing spectroscopic data, simulating and analysing cometary gas and dust coma, estimating size/albedo of asteroid, enhancing images, and analysing lightcurve.
    - [`sbpy` Tutorials and Workshops Materials](https://github.com/NASA-Planetary-Science/sbpy-tutorial)

### [Solar System Geometry](https://naif.jpl.nasa.gov/naif/solar_system_geometry.pdf)

* [`SPICE` - An Observation Geometry System for Space Science Missions](https://naif.jpl.nasa.gov/naif/)
    - NASA's Navigation and Ancillary Information Facility (NAIF) offers NASA flight projects and NASA funded researchers an observation geometry information system named "SPICE" to assist scientists in planning and interpreting scientific observations from space-based instruments aboard robotic planetary spacecraft.  
    - [The `SPICE` Toolkit](https://naif.jpl.nasa.gov/naif/toolkit.html) is available in C, Fortran, IDL, and Matlab.
    - [`SpiceyPy` - Python wrapper for the NAIF C SPICE Toolkit](https://github.com/AndrewAnnex/SpiceyPy)
        - [Online document can be found here](https://spiceypy.readthedocs.io/en/master/)

* [`spiops` - Extension of SPICE functionalities for ESA Missons](https://github.com/esaSPICEservice/spiops)
    - `spiops` is a library aimed to help scientists and engineers that deal with Solar System Geometry mainly for planetary science

### Object Detection

* [`SALTAD`](https://github.com/NASA-Planetary-Science/SALTAD)
    - `SALTAD` is comprised of a series of C language function modules for image processing multiframe image data to detect moving asteroids in a star cluttered background.

### Minor Planet Center Related 

* [`mpc-fetch.py` - fetches properties of all objects that match search params](https://minorplanetcenter.net/mpc-fetch.py)
* [`astroquery.mpc` - Minor Planet Center Queries](https://astroquery.readthedocs.io/en/latest/mpc/mpc.html)
* [`mpc-client` - A python client for the Minor Planet Center's MPC web service](https://github.com/qdonnellan/mpc-client)

### Modeling and Simulating Planet

* [`Beam` - A Monte Carlo Radiative Transfer Code for studies of Saturn's Rings](https://github.com/physicsguy42/BEAM_beta)