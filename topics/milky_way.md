# Tools and Resources for Milky Way Related Research 

* Focusing on the dynamic and stellar population sides.

## Galactic Dynamics

### Courses

* [Dynamics and Astrophysics of Galaxies by Jo Bovy](http://astro.utoronto.ca/~bovy/AST1420/notes/index.html#)
* [Dynamics of Collisionless Systems by Frank van den Bosch](http://www.astro.yale.edu/vdbosch/galdyn.html)

### Tools

* [gala - Galactic and gravitational dynamics in Python](https://github.com/adrn/gala)
    * By [Adrian Price-Whelan](http://adrian.pw/). Provide a class-based and user-friendly interface to fast (C or Cython-optimized) implementations of common operations such as gravitational potential and force evaluation, orbit integration, dynamical transformations, and chaos indicators for nonlinear dynamics.
    * Online [document is here](http://gala.adrian.pw/en/latest/)
* [galpy - Galactic Dynamics in Python](https://github.com/jobovy/galpy)
    * By [Jo Bovy](http://astro.utoronto.ca/~bovy/). It supports orbit integration in a variety of potentials, evaluating and sampling various distribution functions, and the calculation of action-angle coordinates for all static potentials.
    * Online [document is here](https://galpy.readthedocs.io/en/v1.4.0/)
* [thejoker - A custom Monte Carlo sampler for the (gravitational) two-body problem](https://github.com/adrn/thejoker)
    * By Adrian Price-Whelan. The Joker [1] is a custom Monte Carlo sampler for the two-body problem and is therefore useful for constraining star-star or star-planet systems
* [wendy - A one-dimensional gravitational N-body code](https://github.com/jobovy/wendy)
    * By Jo Bovy. `wendy` solves the one-dimensional gravitational N-body problem to machine precision with an efficient algorithm [O(log N) / particle-collision]. Alternatively, it can solve the problem with approximate integration, but with exact forces.
* [GALAXY N-body simulation package](http://www.physics.rutgers.edu/galaxy/)
    * By Jerry Sellwood. The [manual](http://www.physics.rutgers.edu/~sellwood/manual.pdf) is here.

## Galactic Chemical Evolution

### Tools

* [kimmy - Galactic chemical evolution in python](https://github.com/jobovy/kimmy)
    - By Jo Bovy. `kimmy` contains simple tools to study chemical evolution in galaxies.

## Spectra of Milky Way Stars

### Spectroscopic Surveys

* [APOGEE - The APO Galactic Evolution Experiment](https://www.sdss.org/surveys/apogee/)
* [GALAH - GALactic Archaeology with HERMES](https://galah-survey.org/)
    - Using HERMES on AAT. Resolution: R~28,000.
* [RAVE – the Radial Velocity Experiment](https://www.rave-survey.org/project/)
* [LAMOST - Large Sky Area Multi-Object Fiber Spectroscopic Telescope](http://dr4.lamost.org/)

### Tools

* [apogee - Tools for dealing with APOGEE data](https://github.com/jobovy/apogee)


## Stellar structures in the Milky Way

* [galstreams - Milky Way Streams Footprint Library and Toolkit for Python](https://github.com/cmateu/galstreams)
    * It includes a compilation of spatial information for known stellar streams and overdensities in the Milky Way (MW) and Python tools for visualizing them.

## `Gaia` related 

### Python tools:

* [pyia - A Python package for working with Gaia data](https://github.com/adrn/pyia) 
* [gaia_tools - Tools for working with the ESA/Gaia data and related data sets](https://github.com/jobovy/gaia_tools)
* [The Gaia DR1 TGAS completeness and a new stellar inventory of the solar neighborhood](https://github.com/jobovy/tgas-completeness)