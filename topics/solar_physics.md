# Resource about Solar Physics

## Mission and Data

* [Solar Dynamics Observatory](https://sdo.gsfc.nasa.gov/)

* [Interface Region Imaging Spectrograph (IRIS)](http://iris.lmsal.com/mission.html)
    - The primary goal of the Interface Region Imaging Spectrograph (IRIS) explorer is to understand how the solar atmosphere is energized

## Tools

### General Data Analysis Tools

* [`SolarSoftWare` (`SSW`)](https://sohowww.nascom.nasa.gov/solarsoft/)
    - The `SolarSoft` system is a set of integrated software libraries, data bases, and system utilities which provide a common programming and data analysis environment for Solar Physics. Mostly written in `IDL`.

* [`SunPy` - Python for Solar Physics](https://sunpy.org/)
    - The community-developed, free and open-source solar data analysis environment for Python. [Source code on Github](https://github.com/sunpy/sunpy)
    - [Document is here](https://docs.sunpy.org/en/stable/) and here is the [New comers' guide to `SunPy`](https://docs.sunpy.org/en/stable/guide/tour.html)
    - [`SSWIDL` to `SunPy` cheat sheet](https://docs.sunpy.org/en/stable/guide/ssw.html)

* [`sunkit-image` - A image processing toolbox for Solar Physics](https://github.com/sunpy/sunkit-image)
    - `sunkit-image` is a a open-source toolbox for solar physics image processing. Currently it is experimental library for various solar physics specific image processing routines.

### Telescope or Mission Specific Tools 

* [`irispy` - A SunPy-affiliated package which provides tools to analyze data from IRIS](https://github.com/sunpy/irispy)
    - `IRISPy` is a SunPy-affiliated package that provides the tools to read in and analyze data from the IRIS solar-observing satellite in Python.

* [`drms` - Access HMI, AIA and MDI data with Python](https://github.com/sunpy/drms)
    - The `drms` module provides an easy-to-use interface for accessing HMI, AIA and MDI data with Python. It uses the publicly accessible JSOC DRMS server by default

* [`dkist` - A Python library for obtaining, processing and interacting with calibrated DKIST data](https://github.com/DKISTDC/dkist)
    - The [Daniel K. Inouye Solar Telescope](https://dkist.nso.edu/) (DKIST, formerly the Advanced Technology Solar Telescope, ATST)

### Other Useful Tools

* [`solarbextrapolation` - Extrapolation framework for Solar Magnetic Fields](https://github.com/sunpy/solarbextrapolation)
    - `solarbextrapolation` is a library for extrapolating 3D magnetic fields from line-of-sight magnetograms

* [`demreg` - Calculate the Differential Emission Measure (DEM) from solar data using regularised inversion](https://github.com/ianan/demreg)
    - Written in IDL. More on the [Regularized DEM Maps](http://www.astro.gla.ac.uk/~iain/demreg/map/)

* [`MagneticFragmentation`](https://github.com/fraserwatson/MagneticFragmentation)
    - The algorithms required to divide SDO/HMI magnetograms into individual magnetic fragments, based on a 'downhill' segmentation.

* [`Pysolar` - a collection of Python libraries for simulating the irradiation of any point on earth by the sun](https://github.com/pingswept/pysolar)

* [`EBTEL` - Enthalpy-Based Thermal Evolution of Loops model](https://github.com/rice-solar-physics/EBTEL)
    - Written in IDL, for [Highly Efficient Modeling of Dynamic Coronal Loops](https://arxiv.org/abs/0710.0185)
    - [`ebtel++` - C++ implementation of the two-fluid EBTEL model](https://github.com/rice-solar-physics/ebtelPlusPlus)

* [`IonPopSolver` - Code for computing effective temperature and ion population fractions from temperature and density timeseries](https://github.com/rice-solar-physics/IonPopSolver)
    - Based on [A numerical tool for the calculation of non-equilibrium ionisation states in the solar corona and other astrophysical plasma environments](https://www.aanda.org/component/article?access=bibcode&bibcode=&bibcode=2009A%2526A...502..409BFUL)

* [`eitwave` - EIT Wave Detection (AGU 2011)](https://github.com/sunpy/eitwave)

### Atomic Database

* [`CHIANTI` - An Atomic Database for Spectroscopic Diagnostics of Astrophysical Plasmas](http://www.chiantidatabase.org/)
    - This is a general astrophysical database, but it is frequently used in solar physics. It is [distributed within `SSW`](http://www.chiantidatabase.org/instructions.html).
    - [`fiasco` - A Python interface to the CHIANTI atomic database](https://github.com/wtbarnes/fiasco)
        * [Online document is here](https://fiasco.readthedocs.io/en/latest/)
    - [`ChiantiPy` - the Python interface to the CHIANTI atomic database for astrophysical spectroscopy](https://github.com/chianti-atomic/ChiantiPy)