# Python Tools for Model Fitting and General Optimization

## Optimization Algorithms

* [__Solid__ - A Python framework for gradient-free optimization](https://github.com/100/Solid)
	- Include algorithms like Genetic Algorithm, Stimulated Annealing, Particle Swarm, Harmony Search, and Stochastic hill Climb

* [__GAFT__ - A Genetic Algorithm Framework in Python](https://github.com/PytLab/gaft)
	- 有一系列中文blog介绍背后设计和算法，非常适合学习遗传算法

* [__pyswarms__ - A research toolkit for particle swarm optimization in Python](https://github.com/ljvmiranda921/pyswarms)
	- Wikipedia introduction of [PSO: Particle Swarm Optimization](https://en.wikipedia.org/wiki/Particle_swarm_optimization)
	- Document includes a [very nice introducation of the PSO algorithm](https://pyswarms.readthedocs.io/en/latest/intro.html)

* [The Covariance Matrix Adaptation Evolution Strategy (CMA-ES) Algorihm](https://en.wikipedia.org/wiki/CMA-ES)
	- A stochastic derivative-free numerical optimization algorithm for difficult (non-convex, ill-conditioned, multi-modal, rugged, noisy) optimization problems in continuous search spaces.
	- [pycma - A Python implementation of CMA-ES](https://github.com/CMA-ES/pycma)

* [__proxmin__ - Proximal Minimization in Python](https://github.com/pmelchior/proxmin)
	- Based on the paper by [Fred Moolekamp & Peter Melchoir (2018)](https://link.springer.com/article/10.1007%2Fs11081-018-9380-y)
	* Includes algorithms like Alternating Direction Method of Multipliers (ADMM) and Block-Simultaneous Direction Method of Multipliers (bSDMM)
	* Used as the backend of multi-band deblending code [scarlet](https://github.com/fred3m/scarlet)

* [__pagmo2__ - A C++ / Python platform to perform parallel computations of optimisation tasks (global and local) via the asynchronous generalized island model](https://github.com/esa/pagmo2)
	- A a scientific library for massively parallel optimization used by ESA.
	- Document can be found [here](https://esa.github.io/pagmo2/)
	- Includes [a long list of global and local optimization algorithms](https://esa.github.io/pagmo2/docs/algorithm_list.html)

* [__symfit__ - Symbolic Fitting; fitting as it should be](https://github.com/tBuLi/symfit)
	- Pythonic way to do fitting.

* [__zfit__ - scalable pythonic fitting](https://github.com/zfit/zfit)
	- The __zfit__ package is a model manipulation and fitting library based on TensorFlow and optimised for simple and direct manipulation of probability density functions. Its main focus is on scalability, parallelisation and user friendly experience.

### Bayesian Optimization

* [__BayesianOptimization__ - Pure Python implementation of bayesian global optimization with gaussian processes](https://github.com/fmfn/BayesianOptimization)
	- Bayesian optimization works by constructing a posterior distribution of functions (gaussian process) that best describes the function you want to optimize.

* [__gaussbock__ - Fast parallel-iterative cosmological parameter estimation with Bayesian nonparametrics](https://github.com/moews/gaussbock)

* [__vbmc__ - Variational Bayesian Monte Carlo (VBMC) algorithm for posterior and model inference](https://github.com/lacerbi/vbmc)
	- VBMC is a novel approximate inference method designed to fit and evaluate computational models with a limited budget of likelihood evaluations (e.g., for computationally expensive models).
	- A Python implementation is planned.
