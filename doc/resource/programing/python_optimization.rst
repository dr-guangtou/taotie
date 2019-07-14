Python Tools for Model Fitting and General Optimization
=======================================================

Optimization Algorithms
-----------------------

-  `Solid - A Python framework for gradient-free
   optimization <https://github.com/100/Solid>`__

   -  Include algorithms like Genetic Algorithm, Stimulated Annealing,
      Particle Swarm, Harmony Search, and Stochastic hill Climb

-  `GAFT - A Genetic Algorithm Framework in
   Python <https://github.com/PytLab/gaft>`__

   -  有一系列中文blog介绍背后设计和算法，非常适合学习遗传算法

-  `pyswarms - A research toolkit for particle swarm optimization in
   Python <https://github.com/ljvmiranda921/pyswarms>`__

   -  Wikipedia introduction of `PSO: Particle Swarm
      Optimization <https://en.wikipedia.org/wiki/Particle_swarm_optimization>`__
   -  Document includes a `very nice introducation of the PSO
      algorithm <https://pyswarms.readthedocs.io/en/latest/intro.html>`__

-  `The Covariance Matrix Adaptation Evolution Strategy (CMA-ES)
   Algorihm <https://en.wikipedia.org/wiki/CMA-ES>`__

   -  A stochastic derivative-free numerical optimization algorithm for
      difficult (non-convex, ill-conditioned, multi-modal, rugged,
      noisy) optimization problems in continuous search spaces.
   -  `pycma - A Python implementation of
      CMA-ES <https://github.com/CMA-ES/pycma>`__

-  `proxmin - Proximal Minimization in
   Python <https://github.com/pmelchior/proxmin>`__

   -  Based on the paper by `Fred Moolekamp & Peter Melchoir
      (2018) <https://link.springer.com/article/10.1007%2Fs11081-018-9380-y>`__
   -  Includes algorithms like Alternating Direction Method of
      Multipliers (ADMM) and Block-Simultaneous Direction Method of
      Multipliers (bSDMM)
   -  Used as the backend of multi-band deblending code
      `scarlet <https://github.com/fred3m/scarlet>`__

-  `pagmo2 - A C++ / Python platform to perform parallel computations of
   optimisation tasks (global and local) via the asynchronous
   generalized island model <https://github.com/esa/pagmo2>`__

   -  A a scientific library for massively parallel optimization used by
      ESA.
   -  Document can be found `here <https://esa.github.io/pagmo2/>`__
   -  Includes `a long list of global and local optimization
      algorithms <https://esa.github.io/pagmo2/docs/algorithm_list.html>`__

-  `symfit - Symbolic Fitting; fitting as it should
   be <https://github.com/tBuLi/symfit>`__

   -  Pythonic way to do fitting.

-  `zfit - scalable pythonic fitting <https://github.com/zfit/zfit>`__

   -  The **zfit** package is a model manipulation and fitting library
      based on TensorFlow and optimised for simple and direct
      manipulation of probability density functions. Its main focus is
      on scalability, parallelisation and user friendly experience.

Bayesian Optimization
~~~~~~~~~~~~~~~~~~~~~

-  `BayesianOptimization - Pure Python implementation of bayesian global
   optimization with gaussian
   processes <https://github.com/fmfn/BayesianOptimization>`__

   -  Bayesian optimization works by constructing a posterior
      distribution of functions (gaussian process) that best describes
      the function you want to optimize.

-  `gaussbock - Fast parallel-iterative cosmological parameter
   estimation with Bayesian
   nonparametrics <https://github.com/moews/gaussbock>`__

-  `vbmc - Variational Bayesian Monte Carlo (VBMC) algorithm for
   posterior and model inference <https://github.com/lacerbi/vbmc>`__

   -  VBMC is a novel approximate inference method designed to fit and
      evaluate computational models with a limited budget of likelihood
      evaluations (e.g., for computationally expensive models).
   -  A Python implementation is planned.
