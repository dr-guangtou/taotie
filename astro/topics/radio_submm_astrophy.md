# Resources and Tools for Radio and Submm Astronomy

**Just started**

-----

* [`casacore` - Suite of C++ libraries for radio astronomy data processing](https://github.com/casacore/casacore)
    - The `casacore` package contains the core libraries of the old `AIPS++/CASA` package. This split was made to get a better separation of core libraries and applications. `CASA` is now built on top of `Casacore`.
    - `python-casacore`: Python bindings for casacore, a library used in radio astronomy. Document can be [found here](http://casacore.github.io/python-casacore/) 

* [`pyuvdata` - A pythonic interface for radio astronomy interferometry data (uvfits, miriad, others)](https://github.com/RadioAstronomySoftwareGroup/pyuvdata)
    - `pyuvdata` defines a pythonic interface to interferometric data sets. Currently pyuvdata supports reading and writing of miriad, uvfits, and uvh5 files and reading of `CASA` measurement sets and FHD (Fast Holographic Deconvolution) visibility save files.
    - Online document is [here](https://pyuvdata.readthedocs.io/en/latest/)

* [`pyuvsim` - A comprehensive simulation package for radio interferometers in python](https://github.com/RadioAstronomySoftwareGroup/pyuvsim)
    - A number of analysis tools are available to simulate the output of a radio interferometer (CASA, OSKAR, FHD, PRISim, et al), however each makes numerical approximations to enable speed ups.

* [`wise` - Wavelet Image Segmentation and Evaluation tool](https://github.com/flomertens/wise)
    - `wise` is developed to address the issue of detecting significant features in radio interferometric images and obtaining reliable velocity field from cross-correlation of these regions in multi-epoch observations.
    - Detection of structural information is performed using the segmented wavelet decomposition (SWD) method.

* [`GaussPy` - A Python tool for implementing Autonomous Gaussian Decomposition](https://github.com/gausspy/gausspy)
    - Based on the work of [Autonomous Gaussian Decomposition](https://arxiv.org/abs/1409.2840)
* [`gausspyplus` - Fully automated Gaussian decomposition package for emission line spectra](https://github.com/mriener/gausspyplus)
    - `GaussPy+` is based on `GaussPy`: A python tool for implementing the Autonomous Gaussian Decomposition algorithm.

* [`Scintillometry` - A Package for Radio Baseband Data Reduction](https://github.com/mhvk/scintillometry)
    - `Scintillometry` is a package for reduction and analysis of radio baseband data, optimized for pulsar scintillometry science. [Online document is here](https://scintillometry.readthedocs.io/en/latest/)

* [`SoFiA` - The HI Source Finding Application](https://github.com/SoFiA-Admin/SoFiA)
    - `SoFiA`, the Source Finding Application, is a new HI source finding pipeline intended to find and parametrise galaxies in HI data cubes.
    - The version 2 which is reimplemented in `C` can be [found here](https://github.com/SoFiA-Admin/SoFiA-2)

* [`galario` - Gpu Accelerated Library for Analysing Radio Interferometer Observations](https://github.com/mtazzari/galario)
    - `galario` is a library that exploits the computing power of modern graphic cards (GPUs) to accelerate the comparison of model predictions to radio interferometer observations.