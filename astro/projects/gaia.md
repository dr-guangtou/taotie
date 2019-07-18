# Gaia

* _Gaia_ is an ambitious mission to chart a three-dimensional map of our Galaxy, the Milky Way, in the process revealing the composition, formation and evolution of the Galaxy. _Gaia_ will provide unprecedented positional and radial velocity measurements with the accuracies needed to produce a stereoscopic and kinematic census of about one billion stars in our Galaxy and throughout the Local Group. This amounts to about 1 per cent of the Galactic stellar population.

* Right now we are at _Gaia_ DR2 (06/2019)

## Basic Information:

- [_Gaia_ website at ESA](http://sci.esa.int/gaia/)
- [_Gaia_ data and tools summary page](https://www.cosmos.esa.int/web/gaia/data)
- All data are available from the ESA [_Gaia_ Data Archive](http://gea.esac.esa.int/archive/)
    * Also at [_Gaia_ at CDS](http://cdsweb.u-strasbg.fr/gaia); [_Gaia_ at ARI](http://gaia.ari.uni-heidelberg.de/); [_Gaia_ at AIP](https://gaia.aip.de/); and [_Gaia_ at ASDC](http://gaiaportal.asdc.asi.it/)
    * And all _Gaia_ data can be directly downloaded from [here in .csv format](http://cdn.gea.esac.esa.int/Gaia/)

### Data Release:

- [_Gaia_ Data Release 1](http://sci.esa.int/gaia/58275-data-release-1/)
- [_Gaia_ Data Release 2](http://sci.esa.int/gaia/60243-data-release-2/)
    * [Online documents](http://gea.esac.esa.int/archive/documentation/GDR2/index.html)
    * [_Gaia_ DR2 data models](http://gea.esac.esa.int/archive/documentation/GDR2/Gaia_archive/chap_datamodel/)
    * [_Gaia_ DR2 known issues](https://www.cosmos.esa.int/web/gaia/dr2-known-issues)
    * [Official tutorials to use _Gaia_ DR2 data](http://gea.esac.esa.int/archive-help/index.html)
    * [Video guide for scientists](https://www.cosmos.esa.int/web/gaia/guide-to-scientists#video6)

### Using _Gaia_ Data

* [Estimating distances from parallaxes. IV. Distances to 1.33 billion stars in Gaia data release 2](http://www.mpia.de/~calj/gdr2_distances/main.html)
    - The "BailerJones" catalog of distance.
* [Tutorials on the use of (Gaia) astrometry in astronomical data analysis or inference problems](https://github.com/agabrown/astrometry-inference-tutorials)
    - By Anthony Brown. This is a **must read**
    - Also see his [example of the construction of a sample of sources from Gaia DR2 with all recommend data quality filtering applied](https://github.com/agabrown/gaiadr2-6dgold-example)
    - And [Python code for calculating the Renormalized Unit Weight Error from the Gaia DR2 table columns](https://github.com/agabrown/gaiadr2-ruwe-tools)
* Slides about [_Gaia_ DR2 astrometry](https://www.cosmos.esa.int/documents/29201/1770596/Lindegren_GaiaDR2_Astrometry_extended.pdf/1ebddb25-f010-6437-cb14-0e360e2d9f09)
* Slides about [Working with _Gaia_ Data](https://www.cosmos.esa.int/documents/915837/915858/2016_11_02_dr1Workshop_AlcioneMora.pdf/39b2492b-e74c-4b28-bd1f-71258b25fd08)
* The _Gaia_ TAP+ catalog can be accessed through __astroquery.gaia__ module. Here is a [Python example for DR2](https://gea.esac.esa.int/archive-help/tutorials/python_cluster/index.html)
* [Exploring Gaia data with TOPCAT and STILTS](http://www.euro-vo.org/sites/default/files/documents/tutorial-topcat-stilts_2018Nov.pdf)
* [Gaia-Kepler.fun](https://gaia-kepler.fun/)
    - This website provides cross-matched catalogs of Gaia data for stars observed by Kepler/K2

### Social Media

- [Twitter handle: @ESAGaia](https://twitter.com/ESAGaia)

## Important Documents:

### Special Issues:

* There are too many important publications about the _Gaia_ mission, instrument, data reduction, and data release. Most of these "official" publications are compiled into two special issues of the Astronomy & Astrophysics:
    - [A&A Special Issue: _Gaia_ Data Release 1](https://www.aanda.org/component/toc/?task=topic&id=641)
    - [A&A Special Issue: _Gaia_ Data Release 2](https://www.aanda.org/component/toc/?task=topic&id=922)

## Important Publications:

* For using DR2 data, the most important ones are:
    - [Gaia Data Release 2](https://www.aanda.org/articles/aa/pdf/2018/08/aa33955-18.pdf)
    - [Gaia Data Release 2 - Summary of the contents and survey properties](https://www.aanda.org/articles/aa/pdf/2018/08/aa33051-18.pdf)
    - [Gaia Data Release 2 - Using Gaia parallaxes](https://www.aanda.org/articles/aa/pdf/2018/08/aa32964-18.pdf)
    - [Gaia Data Release 2 - Cross-match with external catalogues: algorithms and results](https://www.aanda.org/articles/aa/pdf/2019/01/aa34142-18.pdf)


## Softwares and Tools:

* [__PyGaia__ - Python toolkit for basic Gaia data simulation, manipulation, and analysis](https://github.com/agabrown/PyGaia)
    - By Anthony Brown. PyGaia provides python modules for the simulation of Gaia data and their errors, as well modules for the manipulation and analysis of the Gaia catalogue data
* [__gaia_tools__ - Tools for working with the @ESAGaia data and related data sets](https://github.com/jobovy/gaia_tools)
    - By Jo Bovy. Tools for working with the ESA/Gaia data and related data sets (APOGEE, GALAH, LAMOST DR2, and RAVE).
* [__GaiaTools__ - A collection of scripts for analyzing the data from the Gaia satellite](https://github.com/GalacticDynamics-Oxford/GaiaTools)
    - By the Oxford's Galactic Dynamics group.

* [Gaia TAP+ through __astroquery.gaia__](https://astroquery.readthedocs.io/en/latest/gaia/gaia.html)
* [__find_gaia_dr2.py__](http://cds.u-strasbg.fr/resources/doku.php?id=cdsclient:doc-find_gaia_dr2)
    - By CDS. Depends on __python-cdsclient__
* [Gaia Sky - a real-time, 3D, astronomy visualisation software](https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/)

## Conferences and Sprints

* [_Gaia_ Sprints](http://gaia.lol/)
    * A project to support exploration and scientific use of the Gaia Data Releases.
    * There are a lot of interesting discussions and ideas can be found in the sprint website.

* [KITP Project 2019: Dynamical Models for Stars and Gas in Galaxies in the Gaia Era](https://www.kitp.ucsb.edu/activities/gaia19)
    * Most of the [talks can be found on line](http://online.kitp.ucsb.edu/online/gaia19/)
    * There is also a associated conference: [In the Balance: Stasis and Disequilibrium in the Milky Way](https://www.kitp.ucsb.edu/activities/gaia-c19)

* [Gaia Data Workshop - Heidelberg 2018](http://gaia.ari.uni-heidelberg.de/gaia-workshop-2018/)
    * A lot of useful slides are available here.
* [Gaia Data Release 2 London workshop](https://www.gaia.ac.uk/science/workshops/gaia-dr2-london-may18)

* [49th Saas-Fee Advanced Course - The Milky Way in the Gaia Era](https://www.physik.uzh.ch/events/sf2019/)
    * Video lectures and course materials are available.
