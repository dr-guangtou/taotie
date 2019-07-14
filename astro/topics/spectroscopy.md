# Spectroscopic Data Reduction and Analysis

## General Tools

- [__specutils__ - An Astropy coordinated package for astronomical spectroscopy](https://github.com/astropy/specutils)
    * Provides a shared set of Python representations of astronomical spectra and basic tools to operate on these spectra.

- [__linetools__ - This is a package for the analysis of 1d astronomical spectra, especially quasar and galaxy spectra](https://github.com/linetools/linetools)
    * Still under development. Its core developers work primarily on UV/optical/IR absorption line research, so most of the functionality is aimed at the identification and analysis of absorption lines. The eventual goal is to provide a set of tools useful for both absorption and emission lines.
    * [Online document is here](https://linetools.readthedocs.io/en/latest/)

## Visualization

- [__specviz__ - An interactive astronomical 1D spectra analysis tool](https://github.com/spacetelescope/specviz)
    * Made by STScI. An gui-based interactive analysis tool for one dimensional astronomical data using Python.

- [__cubeviz__ - Data analysis package for cubes](https://github.com/spacetelescope/cubeviz)
    * Made by STScI. __CubeViz__, a visualization and analysis tool for data cubes from integral field units (IFUs). [Online document is here](https://cubeviz.readthedocs.io/en/latest/)

## Data Reduction Pipeline

- [__Pypelt__ - The Python Spectroscopic Data Reduction Pipeline](https://github.com/pypeit/PypeIt)
    * PypeIt is a Python based data reduction pipeline (DRP) written oringinally for echelle spectroscopy and since expanded to low-resolution spectrometers.
    * [arclines - Database of arc lines from optical-IR spectrographs](https://github.com/pypeit/arclines)

- MaNGA data reduction and analysis pipeline
    * [__mangadap__ - The MaNGA Data Analysis Pipeline](https://github.com/sdss/mangadap)
        * The MaNGA data-analysis pipeline (MaNGA DAP) is the survey-led software package that analyzes the data produced by the MaNGA data-reduction pipeline (MaNGA DRP) to produced physical properties derived from the MaNGA spectroscopy.

- [__GIST__ - Galaxy IFU Spectroscopy Tool](https://abittner.gitlab.io/thegistpipeline/index.html)
    * A convenient, all-in-one framework for the scientific analysis of fully reduced, (integral-field) spectroscopic data.

- [__TDOSE__ - Three Dimensional Optimal Spectral Extraction](https://github.com/kasperschmidt/TDOSE)
    * Python pipeline to extract spectra of both point sources and extended sources from integral field data cubes

- [__pydis__ - A simple longslit spectroscopy pipeline in Python](https://github.com/TheAstroFactory/pydis)
    * The goal of pyDIS is to provide a turn-key solution for reducing and understanding longslit spectroscopy, which could ideally be done in real time. Currently we are using many simple assumptions to get a quick-and-dirty solution, and modeling the workflow after the robust industry standards set by IRAF.

- [__speclite__ - Lightweight utilities for working with spectroscopic data](https://github.com/dkirkby/speclite)
    * By David Kirby. This package provides a set of lightweight utilities for working with spectroscopic data in astronomy.

## Redshift or Radial Velocity Measurement

- [__grizli__ - Grism redshift & line analysis software for space-based slitless spectroscopy](https://github.com/gbrammer/grizli)
    - By [Gabriel Brammer](http://www.stsci.edu/~brammer/).

- [__redrock__ - Redshift fitting for spectroperfectionism](https://github.com/desihub/redrock)
    * This is DESI's redshift measurement tool

- [__redmonster__ - Python utilieties for redshift measurement](https://github.com/timahutchinson/redmonster)
    * __redmonster__ is a project to develop a sophisticated and flexible set of Python utilities for redshift measurement, physical parameter measurement, and classification of one-dimensional astronomical spectra.
    * Originally designed for eBOSS and the paper can be [found here](https://arxiv.org/abs/1607.02432)
