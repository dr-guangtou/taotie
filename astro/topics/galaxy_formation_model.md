# Models for Galaxy Formation and Evolution

## Reviews

* [Galaxy Formation Thory](https://ui.adsabs.harvard.edu/abs/2010PhR...495...33B/abstract)
    - By Andrew Benson. A 58 pages review article in 2010. Although some aspects of it need to be updated. This remains as a wonderful place to start learning about galaxy formation.

* [Theoretical Challenges in Galaxy Formation](https://arxiv.org/abs/1612.06891)
    - ARA&A review by Thorsten Naab & Jeremiah Ostriker with a theoretical point of view.

* [The Evolution of Galaxy Structure over Cosmic Time](https://arxiv.org/abs/1403.2783)
    - ARA&A review by Christopher Conselice with an observational point of view.

* [The Connection Between Galaxies and Their Dark Matter Halos](https://arxiv.org/abs/1804.03097)
    - ARA&A review by Risa Wechsler & Jeremy Tinker from a galaxy-halo connection point of view.

* [Lighting Up Dark Matter Haloes](https://www.mdpi.com/2075-4434/7/2/56)
    - Review article by Gabriella De Lucia on _Galaxies_.

## Semi-Analytic Model

<img src="https://github.com/dr-guangtou/taotie/blob/master/doc/fig/galaxies/sam_list.png" width="80%">

> "Semi-analytic galaxy formation models are established tools for connecting the predicted hierarchical growth of dark matter haloes to the observed properties of the galaxy population. Semi-analytic models employ a forward-modelling approach and are constructed such that they contain as much as possible of the baryonic physics that is thought to be relevant to galaxy evolution, albeit at a simplified, macroscopic level. The simplified, macroscopic nature of semi-analytic models means that they are computationally inexpensive to evaluate." - [Mitchell et al. 2017](https://arxiv.org/pdf/1709.08647.pdf)

* There are a whole bunch of SAM available now, we will focus on the ones with source codes in public or the ones with a clear trace of publications.

* [__Galacticus__ - A Semi-Analytic Model of Galaxy Formation](https://bitbucket.org/galacticusdev/galacticus/wiki/Home)
    - Based on the paper by Andrew Benson: [Galacticus: A Semi-Analytic Model of Galaxy Formation](https://arxiv.org/abs/1008.1786)
    - Written in Fortran. Currently only support Linux OS.
    - Mock galaxy catalog for the __MDPL2__ N-body simulation can be [found in the MultiDark-Galaxies project](http://skiesanduniverses.org/page/page-3/page-22/)
    - The tools for interacting with and analyzing the outputs of __Galacticus__ is written in __Perl__. [A PDF document of these tools can be found here](https://users.obs.carnegiescience.edu/abenson/galacticus/GalacticusAnalysisPerl.pdf)

* [__Shark__ - A new, flexible semi-analytic model of galaxy formation](https://github.com/ICRAR/shark)
    - Based on the work led by Claudia Lagos: [Shark: introducing an open source, free, and flexible semi-analytic model of galaxy formation](https://ui.adsabs.harvard.edu/abs/2018MNRAS.481.3573L/abstract)
    - [Online document is here](https://shark-sam.readthedocs.io/en/latest/)
    - Written in C++ with __OpenMP__ support.
    - __Shark__ has been implemented with several models for gas cooling, active galactic nuclei, stellar and photo-ionization feedback, and star formation (SF). 
    - __Shark__ is based on the new cluster finder __VELOCIRAPTOR__ and merger tree builder __TreeFrog__ developed by the same group.

* [__SAGE__ - Semi-Analytic Galaxy Evolution galaxy formation model](https://github.com/sage-home/sage-model)
    - __SAGE__ is a publicly available code-base for modelling galaxy formation in a cosmological context. A description of the model and its default calibration results can be found in [Croton et al. (2016)](https://arxiv.org/abs/1601.04709). These calibration results can also be explored in an [iPython notebook](https://github.com/darrencroton/sage/blob/master/output/SAGE_MM.ipynb) showcasing the key figures here. SAGE is a significant update to that previously used in [Croton et al. (2006)](https://arxiv.org/abs/astro-ph/0508046). 
    - __SAGE__ is written in C and was built to be modular and customisable. It will run on any N-body simulation whose trees are organised in a supported format and contain a minimum set of basic halo properties.
    - Mock galaxy catalog for the __MDPL2__ N-body simulation can be [found in the MultiDark-Galaxies project](http://skiesanduniverses.org/page/page-3/page-22/)
    - [__rsage__ - The Reionization using Semi-Analytic Galaxy Evolution model](https://github.com/jacobseiler/rsage)
        * An augmented version of the __SAGE__ model that self-consistently couples galaxy evolution with the evolution of ionized gas during the Epoch of Reionization. 
    
* [__L-Galaxies__ - Munich Galaxy Formation Model](http://galformod.mpa-garching.mpg.de/public/LGalaxies/index.php)
    - The public version is [available on GitHub](https://github.com/LGalaxiesPublicRelease/LGalaxies_PublicRepository)
    - The most recent reference is the paper led by [Bruno Henriques](http://galformod.mpa-garching.mpg.de/public/LGalaxies/Henriques2014a.pdf). A supplementary material is [also available](http://galformod.mpa-garching.mpg.de/public/LGalaxies/munich_sam.pdf) that contains more details of the model. And here is a [presentation that helps you understand the key recipe of the mode](http://galformod.mpa-garching.mpg.de/public/LGalaxies/LGalaxies_slides.pdf) 
    - The __L-Galaxies__ model galaxy catalog for the Millennium simulations can be [found here](http://gavo.mpa-garching.mpg.de/Millennium/)
    - [L-Galaxies Dust Analysis](https://github.com/scottclay/Lgalaxies_Dust) - Implementation of detailed dust modelling into the Henriques 2015 version of L-Galaxies. The data analysis pipeline is [available here](https://github.com/scottclay/Lgalaxies_Analysis)

* [__GALFORM__: Galactic Modeling](http://star-www.dur.ac.uk/~cole/merger_trees/galform_2000/)
    - Originally based on the classic paper by [Shaun Cole et al. 2010](https://ui.adsabs.harvard.edu/abs/2000MNRAS.319..168C/abstract). The new version of __GALFORM__ model is presented in the work led by [Cedric Lacey et al. 2016](https://ui.adsabs.harvard.edu/abs/2016MNRAS.462.3854L/abstract)
    - This is also known as the "Durham" galaxy formation model.

* The "Santa Cruz" Galaxy Formation Model
    - Originally based on the work by [Rachel Somerville & Joel Primack 1998](https://ui.adsabs.harvard.edu/abs/1999MNRAS.310.1087S/abstract)
    - The updated version is presented in the work: [Star formation in semi-analytic galaxy formation models with multiphase gas by Somerville, Popping, & Trager 2015](https://ui.adsabs.harvard.edu/abs/2015MNRAS.453.4337S/abstract)

* __GAEA__ - GAlaxy Evolution and Assembly model
    - Based on the work ["Galaxy assembly, stellar feedback and metal enrichment: the view from the GAEA model" by Michaela Hirschmann, Gabriella De Lucia, & Fabio Fontanot 2015](https://ui.adsabs.harvard.edu/abs/2016MNRAS.461.1760H/abstract)

* [__MORGANA__ - MOdel for the Rise of GAlaxies aNd Active nuclei](http://adlibitum.oats.inaf.it/monaco/Homepage/morgana.html)
    - Originally based on the work led by [Pierluigi Monaco et al. 2007](https://ui.adsabs.harvard.edu/abs/2007MNRAS.375.1189M/abstract). 

* __GalICS__ - Galaxies In Cosmological Simulations
    - Originally based on the work led by [Steve Hatton et al. 2005](https://ieeexplore.ieee.org/document/8148635). The updated __V2.0__ is presented in the work led by [Cattaneo et al. 2017](https://ui.adsabs.harvard.edu/abs/2017MNRAS.471.1401C/abstract)

## Semi-Empirical Model (SEM)

* This is a relative new approach for modeling galaxy formation. The key difference with SAM is that it does not focus on the detailed recipe for physical processes involved in galaxy formation.  Instead, it relies on the assumption that **empirical** relation can be established between the star formation rate and the halo accretion rate (or between stellar mass and halo mass). One key advantage of this approach is that it can run on N-body simulations much faster and hence can be directly constrained by a series of observations at different epochs through Bayesian analysis.
* Some important early works on this topic include: [Behroozi et al. 2010](https://ui.adsabs.harvard.edu/abs/2010ApJ...717..379B/abstract), [Moster et al. 2010](https://ui.adsabs.harvard.edu/abs/2010ApJ...710..903M/abstract).

* [__UniverseMachine__ - Empirical Model for Galaxy Formation](https://bitbucket.org/pbehroozi/universemachine/src/master/)
    - Developed by Peter Behroozi. Based on the work ["UniverseMachine: The Correlation between Galaxy Growth and Dark Matter Halo Assembly from z=0-10"](https://arxiv.org/abs/1806.07893)
    - The __UniverseMachine__ applies simple empirical models of galaxy formation to dark matter halo merger trees. For each model, it generates an entire mock universe, which it then observes in the same way as the real Universe to calculate a likelihood function. It includes an advanced MCMC algorithm to explore the allowed parameter space of empirical models that are consistent with observations. 
    - The [data release by benchmark __UniverseMachine__ model can be found here](https://www.peterbehroozi.com/data.html)

* [__Emerge__ - Empirical ModEl for the foRmation of GalaxiEs](https://ui.adsabs.harvard.edu/abs/2018MNRAS.477.1822M/abstract)
    - __emerge__ is an empirical model for the formation of galaxies since z~10
    - Based on the publication by [Benjamin Moster, Thorsten Naab, & Simon White 2018](https://ui.adsabs.harvard.edu/abs/2018MNRAS.477.1822M/abstract)

* [Model by Aldo Rodríguez-Puebla](https://ui.adsabs.harvard.edu/abs/2017MNRAS.470..651R/abstract)
    - Based on the publication ["Constraining the galaxy-halo connection over the last 13.3 Gyr: star formation histories, galaxy mergers and structural properties" by Rodríguez-Puebla et al. 2017](https://ui.adsabs.harvard.edu/abs/2017MNRAS.470..651R/abstract)

* [__STEEL__ - a STatistical sEmi-Empirical modeL](https://ui.adsabs.harvard.edu/abs/2019MNRAS.483.2506G/abstract)
    - Based on the publication ["A statistical semi-empirical model: satellite galaxies in groups and clusters" by Grylls et al. 2019](https://ui.adsabs.harvard.edu/abs/2019MNRAS.483.2506G/abstract)


## Other Model

* Here is a list of model for galaxy formation that can not be easily classied as SAM or SEM.

* [The Iκϵα model of feedback-regulated galaxy formation](https://ui.adsabs.harvard.edu/abs/2019arXiv190610135S/abstract)
    -  In __Iκϵα__, a galaxy's star formation rate is set by the balance between energy injected by feedback from massive stars and energy lost by the deepening of the potential of its host dark matter halo due to cosmological accretion.
