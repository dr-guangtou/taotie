# Radio and Sub-millimeter Astronomy

**Just started**

-----

* [__casacore__ - Suite of C++ libraries for radio astronomy data processing](https://github.com/casacore/casacore)
    - The __casacore__ package contains the core libraries of the old __AIPS++/CASA__ package. This split was made to get a better separation of core libraries and applications. __CASA__ is now built on top of __Casacore__.
    - __python-casacore__: Python bindings for casacore, a library used in radio astronomy. Document can be [found here](http://casacore.github.io/python-casacore/) 

* [__pyuvdata__ - A pythonic interface for radio astronomy interferometry data (uvfits, miriad, others)](https://github.com/RadioAstronomySoftwareGroup/pyuvdata)
    - __pyuvdata__ defines a pythonic interface to interferometric data sets. Currently pyuvdata supports reading and writing of miriad, uvfits, and uvh5 files and reading of __CASA__ measurement sets and FHD (Fast Holographic Deconvolution) visibility save files.
    - Online document is [here](https://pyuvdata.readthedocs.io/en/latest/)

* [__pyuvsim__ - A comprehensive simulation package for radio interferometers in python](https://github.com/RadioAstronomySoftwareGroup/pyuvsim)
    - A number of analysis tools are available to simulate the output of a radio interferometer (CASA, OSKAR, FHD, PRISim, et al), however each makes numerical approximations to enable speed ups.

* [__wise__ - Wavelet Image Segmentation and Evaluation tool](https://github.com/flomertens/wise)
    - __wise__ is developed to address the issue of detecting significant features in radio interferometric images and obtaining reliable velocity field from cross-correlation of these regions in multi-epoch observations.
    - Detection of structural information is performed using the segmented wavelet decomposition (SWD) method.

* [__GaussPy__ - A Python tool for implementing Autonomous Gaussian Decomposition](https://github.com/gausspy/gausspy)
    - Based on the work of [Autonomous Gaussian Decomposition](https://arxiv.org/abs/1409.2840)
* [__gausspyplus__ - Fully automated Gaussian decomposition package for emission line spectra](https://github.com/mriener/gausspyplus)
    - __GaussPy+__ is based on __GaussPy__: A python tool for implementing the Autonomous Gaussian Decomposition algorithm.

* [__Scintillometry__ - A Package for Radio Baseband Data Reduction](https://github.com/mhvk/scintillometry)
    - __Scintillometry__ is a package for reduction and analysis of radio baseband data, optimized for pulsar scintillometry science. [Online document is here](https://scintillometry.readthedocs.io/en/latest/)

* [__SoFiA__ - The HI Source Finding Application](https://github.com/SoFiA-Admin/SoFiA)
    - __SoFiA__, the Source Finding Application, is a new HI source finding pipeline intended to find and parametrise galaxies in HI data cubes.
    - The version 2 which is reimplemented in __C__ can be [found here](https://github.com/SoFiA-Admin/SoFiA-2)

* [__galario__ - Gpu Accelerated Library for Analysing Radio Interferometer Observations](https://github.com/mtazzari/galario)
    - __galario__ is a library that exploits the computing power of modern graphic cards (GPUs) to accelerate the comparison of model predictions to radio interferometer observations.
