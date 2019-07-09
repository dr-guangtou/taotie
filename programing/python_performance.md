# Performance Optimization for Python

## Basics

- [Basic tips for optimizing the performace of your Python code](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

- [Code for the book "High Performance Python" by Micha Gorelick and Ian Ozsvald with OReilly](https://github.com/mynameisfiber/high_performance_python)

## Interfacing with C/C++

- [Interfacing with C from Scipy lecture notes](https://scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#introduction)
	* Very nice overview and examples of four approaches.
	1. [Python/C API](https://docs.python.org/3/c-api/index.html)
		- [Extending Python3.7 with C or C++](https://docs.python.org/3/extending/extending.html)
	2. [`ctypes` -  A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
		- It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.
	3. [`SWIG`](http://www.swig.org/exec.html)
		- `SWIG` is an interface compiler that connects programs written in C and C++ with scripting languages such as Python
	4. [`Cython` - C-Extensions for Python](https://cython.org/)
		- [Basic tutorial of `Cython`](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html)
		- [Tutorial on how to use Cython to optimize Python code by Adrian Price-Whelan](https://github.com/adrn/cython-tutorial)
		- [Cython tutorial by Pauli Virtanen from 2011](https://python.g-node.org/python-summerschool-2011/_media/materials/cython/cython-slides.pdf)

### Only for C++ 

- [`Boost.Python`](https://www.boost.org/doc/libs/1_70_0/libs/python/doc/html/index.html)
	* `Boost.Python`, a C++ library which enables seamless interoperability between C++ and the Python programming language.

- [`pybind11` - Seamless operability between C++11 and Python](https://github.com/pybind/pybind11)
	* `pybind11` is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code.
	* This is used by the `LSST` developers, please see the [DM `Pybind11` style guide](https://developer.lsst.io/pybind11/style.html) for details.

## `Numba` and other JIT

- [Optimizing Python in the Real World: NumPy, Numba, and the NUFFT by Jake VanderPlas](https://jakevdp.github.io/blog/2015/02/24/optimizing-python-with-numpy-and-numba/)

### Making Numpy faster

- [jax - GPU- and TPU-backed NumPy with differentiation and JIT compilation by Google](https://github.com/dr-guangtou/taotie/new/master)
	* JAX is Autograd and XLA, brought together for high-performance machine learning research.

- [autograd - Efficiently computes derivatives of numpy code](https://github.com/HIPS/autograd)

### Other packages

- [How to speed up Python by scikit-learn](https://scikit-learn.org/stable/developers/performance.html)

## Parallel computing in Python

### Tutorial

- [An introduction to parallel programming using Python's multiprocessing module](https://sebastianraschka.com/Articles/2014_multiprocessing.html)
- [Speed Up Your Algorithms Part 3 — Parallel-ization](https://towardsdatascience.com/speed-up-your-algorithms-part-3-parallelization-4d95c0888748)

### Software

- [mpi4py - Python bindings for MPI](https://github.com/mpi4py/mpi4py)
- [joblib - a set of tools to provide lightweight pipelining in Python](https://github.com/joblib/joblib)
- [loky - Robust and reusable Executor for joblib](https://github.com/tomMoral/loky)
- [schwimmbad - A common interface to processing pools](https://github.com/adrn/schwimmbad)

