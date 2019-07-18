# Astrophysical and Cosmological Simulations

## Tools

### Analysing Data from Simulation

* [The __yt__ project](https://yt-project.org/)
    - __yt__ is an open-source, permissively-licensed python package for analyzing and visualizing volumetric data. [Source code is available on Github](https://github.com/yt-project/yt)
    - There is a list of useful [extensions of __yt__](https://yt-project.org/extensions.html)
    - [__unyt__ - Handle, manipulate, and convert data with units in Python](https://github.com/yt-project/unyt)

* [__Pynbody__ - an analysis package for astrophysical N-body and Smooth Particle Hydrodynamics simulations](https://pynbody.github.io/pynbody/index.html)
    - [Source code available on Github](https://github.com/pynbody/pynbody)

* [__Pylians__ - Libraries to analyze numerical simulations](https://github.com/franciscovillaescusa/Pylians)
    - __Pylians__ stands for Python libraries for the analysis of numerical simulations. They are a set of python libraries, written in python, cython and C, whose purposes is to facilitate the analysis of numerical simulations (both N-body and hydro).

* [__tipsy__ - The Theoretical Image Processing SYstem for visualizing/analyzing n-body simulations](https://github.com/N-BodyShop/tipsy)

#### Halo and Subhalo Finder

* For an overview and comparison of current algorithms:
    * [Haloes gone MAD: The Halo-Finder Comparison Project](https://arxiv.org/abs/1104.0949)
    * [Subhaloes going Notts: the subhalo-finder comparison project](https://arxiv.org/abs/1203.3695)
    * [Galaxies going MAD: the Galaxy-Finder Comparison Project](https://arxiv.org/abs/1210.2578)

* [__Rockstar__ - Robust Overdensity Calculation using K-Space Topologically Adaptive Refinement](https://bitbucket.org/gfcstanford/rockstar/src/master/)
    - By Peter Behroozi. Based on [Phase-Space Temporal Halo Finder and the Velocity Offsets of Cluster Cores](https://arxiv.org/abs/1110.4372)
    - __rockstar__ identifies dark matter halos, substructure, and tidal features. The approach is based on adaptive hierarchical refinement of friends-of-friends groups in six phase-space dimensions and one time dimension, which allows for robust (grid-independent, shape-independent, and noise-resilient) tracking of substructure.

* [__FoF__ - Friends-of-friends method to find groups](https://faculty.washington.edu/trq/hpcc/tools/fof.html)
    - A particle belongs to a friends-of-friends group if it is within some linking length of any other particle in the group. After all such groups are found, those with less than a specified minimum number of group members are rejected.

#### Merger Tree Construction

* For an overview and comparison of current algorithms:
    - [Sussing Merger Trees: The Merger Trees Comparison Project](https://arxiv.org/abs/1307.3577)
    - [Sussing Merger Trees: Stability and Convergence](https://arxiv.org/abs/1604.01463)

* [__consistent-trees__ - Gravitationally Consistent Merger Trees](https://bitbucket.org/pbehroozi/consistent-trees/src/master/)
    - By Peter Behroozi. Based on [Gravitationally Consistent Halo Catalogs and Merger Trees for Precision Cosmology](https://arxiv.org/abs/1110.4370)

* [__VELOCIraptor__ - Galaxy/(sub)Halo finder for N-body simulations](https://github.com/pelahi/VELOCIraptor-STF)
    - By Pascal Jahan Elahi.
    - Also see [__TreeFrog__ - Software to build Halo Merger Trees/compare halo catalogs](https://github.com/pelahi/TreeFrog)
    - And [__VELOCIraptor_Python_Tools__ - python tools for manipulating velociraptor data](https://github.com/pelahi/VELOCIraptor_Python_Tools)

### N-body Simulation

* [__HACC__ - Hardware/Hybrid Accelerated Cosmology Code](https://xgitlab.cels.anl.gov/hacc/HACCKernels/tree/master)
    - A recently developed and evolving cosmology N-body code framework, designed to run efficiently on diverse computing architectures and to scale to millions of cores and beyond. See [publication here for details](https://arxiv.org/abs/1410.2805)
    - [Some relevant codes are available on Gitlab](https://xgitlab.cels.anl.gov/hacc)

* [__GreeM__ - Massively Parallel TreePM Code for Large Cosmological N-body Simulations](https://academic.oup.com/pasj/article/61/6/1319/1462224)

* [__COLA__ - COmoving Lagrangian Acceleration](https://github.com/HAWinther/MG-PICOLA-PUBLIC)
    - Based on the work: [COLA with scale-dependent growth: applications to screened modified gravity models](https://arxiv.org/abs/1703.00879)
    - [Parallel COLA cosmological simulation + 2LPT initial condition generator + FoF halo finder](https://github.com/junkoda/cola_halo)

* [__Quijote-simulations__](https://github.com/franciscovillaescusa/Quijote-simulations)
    - The Quijote simulations are a set of 34500 N-body simulations. They are designed for two main tasks: 1) Quantify the information content on cosmological observables; 2) Provide enough statistics to train machine learning algorithms

* [__UNIT__ - Universe N-body simulations for the Investigation of Theoretical models from galaxy surveys](http://www.unitsims.org/)
    - Based on the work by [Chia-Hsun Chuang et al. 2018](https://arxiv.org/pdf/1811.02111.pdf)
    - __Unit__ uses FastPM (Feng et al. 2016) to generate the paired initial conditions with fixed-amplitude.

* [__MICE__ - Marenostrum Institut de Ciències de l'Espai Simulations](http://maia.ice.cat/mice/)
    - A suit of cosmological simulations. Lots of data are already available in public.

### Hydrodynamic and MHD Simulation

#### SPH: Smoothed Particle Hydrodynamics

* [__Gadget-2__ - A code for cosmological simulations of structure formation](https://wwwmpa.mpa-garching.mpg.de/gadget/)
    * __Gadget-2__ is a freely available code for cosmological N-body/SPH simulations on massively parallel computers with distributed memory. There are multiple spin-off of __Gadget__ now.
    * [__MP-Gadget__ - massively-parallel cosmology simulator](https://github.com/MP-Gadget/MP-Gadget)
        * This version of Gadget is derived from main P-Gadget / Gadget-2. It is the source code used to run the BlueTides simulation

* [__SWIFT__ - SPH With Inter-dependent Fine-grained Tasking](http://swift.dur.ac.uk)
    * __SWIFT__ is a hydrodynamics and gravity code for astrophysics and cosmology.
    * [Source codes can be found on GitLab](https://gitlab.cosma.dur.ac.uk/swift/swiftsim)

* [__GIZMO__ by Phil Hopkins](http://www.tapir.caltech.edu/~phopkins/Site/GIZMO.html)
    * __GIZMO__ is a flexible, massively-parallel, multi-physics simulation code. The [public version code can be found here](https://bitbucket.org/phopkins/gizmo-public/src/default/)
    * It introduces new Lagrangian Godunov-type methods that allow you to solve the fluid equations with a moving particle distribution that is automatically adaptive in resolution and avoids the advection errors, angular momentum conservation errors, and excessive diffusion problems that limit the applicability of “adaptive mesh” (AMR) codes, while simultaneously avoiding the low-order errors inherent to simpler methods like smoothed-particle hydrodynamics (SPH).

* [__Gasoline__ - Particle hydrodynamics have never been smoother](https://gasoline-code.com/)
    * Gasoline is a modern SPH simulation code for astrophysical problems. [Source code is available publicly](https://github.com/N-BodyShop/gasoline)

* [__flecsph__ - A Parallel and Distributed SPH Implementation Based on the FleCSI](https://github.com/laristra/flecsph)
    * This project implements smoothed particles hydrodynamics (SPH) method of simulating fluids and gases using the FleCSI framework. Currently, particle affinity and gravitation is handled using the parallel implementation of the octree data structure provided by FleCSI.

#### AMR: Adaptive Mesh Refinement

* [__AMReX-Codes__ - Block-Structured AMR Software Framework and Applications](https://amrex-codes.github.io/)
    - [__AMReX__ - A software framework for massively parallel, block-structured adaptive mesh refinement (AMR) applications](https://amrex-codes.github.io/amrex/)
    - [__AMReX__ Astrophysics - An Astrophysical Hydrodynamics Code Suite](https://amrex-astro.github.io/)
        * __AMReX__ Astrophysics codes can model subsonic convection and compressible flows in stars, explosive burning in stellar environments, and large scale structure on cosmological scales. They share a common design and an open development model.
        * [__Castro__ - An adaptive mesh, astrophysical radiation hydrodynamics simulation code](https://github.com/AMReX-Astro/Castro)
        * [__MAESTRO__ - A low Mach number stellar hydrodynamics code](https://github.com/AMReX-Astro/MAESTRO)
        * [__Nyx__ - An adaptive mesh, N-body hydro cosmological simulation code](https://github.com/AMReX-Astro/Nyx)

* [__ENZO__ - adaptive mesh-refinement simulation code](https://enzo-project.github.io/)
    - __Enzo__ is a community-developed adaptive mesh refinement simulation code, designed for rich, multi-physics hydrodynamic astrophysical calculations. [Source codes are available on Github](https://github.com/enzo-project/enzo-dev)

* [__FLASH5__ - multiphysics, multiscale simulation code](https://github.com/ECP-Astro/FLASH5)

#### Moving Mesh Approach

* [__Arepo__ - Galilean-invariant cosmological hydrodynamical simulations on a moving mesh](https://www.h-its.org/arepo/)
    - The __AREPO__ code is a cosmological hydrodynamical simulation code on a fully dynamic unstructured mesh. Code is not publicly available yet.

## Projects

### Cosmological Simulations

#### N-Body Simulations

* [CosmoSim Database](https://www.cosmosim.org/)
    - The Spanish MultiDark Consolider project supports efforts to identify and detect matter, including dark matter simulations of the universe. Including __SMDPL__, __MDPL__, __MDPL2__, __BigMDPL__, __Bolshoi__, and __BolshoiP__ simulations.

* [HACC Simulation Data Portal](https://cosmology.alcf.anl.gov/)
    - This webpage provides access to results from large cosmological simulations carried out with __HACC__, the Hardware/Hybrid Accelerated Cosmology Code, developed primarily at Argonne
    - [Mira-Titan Universe Simulations](https://cosmology.alcf.anl.gov/transfer/miratitan)
        * A suite of eleven cosmological models, evolving almost 33 billion particles each in a (2.1Gpc)^3 volume.
    - [Outer Rim Simulation](https://cosmology.alcf.anl.gov/outerrim)
        * A LCDM simulation evolving more than 1 trillion particles in a (4.225Gpc)^3 volume.
    - [QContinuum Simulation](https://cosmology.alcf.anl.gov/transfer/qcontinuum)
        * A LCDM simulation evolving more than 0.5 trillion particles in a (1.3Gpc)3 volume.

* [VIRGO: Cosmological N-Body Simulations](https://wwwmpa.mpa-garching.mpg.de/galform/virgo/)
    - The VIRGO Consortium is an international grouping of scientists carrying out supercomputer simulations of the formation of galaxies, galaxy clusters, large-scale structure, and of the evolution of the intergalactic medium.
    - [The Millennium Simulation Project](https://wwwmpa.mpa-garching.mpg.de/galform/virgo/millennium/index.shtml)
    - [The Hubble Volume Project](https://wwwmpa.mpa-garching.mpg.de/galform/virgo/hubble/index.shtml)

#### Hydrodynamic or MHB Simulations

* [The Illustris Simulation - Towards a predictive theory of galaxy formation](http://www.illustris-project.org/)
    * The Illustris project is a large cosmological simulation of galaxy formation, completed in late 2013, using a state of the art numerical code and a comprehensive physical model.
    * All the data have been [released to public](http://www.illustris-project.org/data/).  See the [About page] for general information.

* [The IllustrisTNG Project](http://www.tng-project.org/)
    * The IllustrisTNG project is an ongoing series of large, cosmological magnetohydrodynamical simulations of galaxy formation.
    * Some of the IllustrisTNG data have been [released to the public](http://www.tng-project.org/data/)

* [The EAGLE Project - Evolution and Assembly of GaLaxies and their Environments](http://icc.dur.ac.uk/Eagle/)
    * [Public data release is available here](http://icc.dur.ac.uk/Eagle/database.php)

* [Auriga project - High resolution disc galaxy simulations in a cosmological context](https://wwwmpa.mpa-garching.mpg.de/auriga/)
    * The Auriga Project is a large suite of high-resolution magneto-hydrodynamical simulations of Milky Way-sized galaxies, simulated in a fully cosmological environment by means of the 'zoom-in' technique. It is simulated with the state-of-the-art hydrodynamic moving mesh code AREPO, and includes a comprehensive galaxy formation model based on the successful cosmological simulation Illustris.

* [BlueTides Simulation](http://bluetides-project.org/)
    * BlueTides was run on the BlueWaters super computer at NCSA with an allocation of 2.6 million node-hours. It simulated the universe from z=99 to z=8.0.
    * Bluetides is the largest hydrodynamic simulation ever performed at such high redshift.

* [The BAHAMAS Project - BAryons and HAloes of MAssive Systems](http://www.astro.ljmu.ac.uk/~igm/BAHAMAS/)
    * BAHAMAS is a first attempt to do large-scale structure (LSS) cosmology using self-consistent full cosmological hydrodynamical simulations.
