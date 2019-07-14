# Performance Optimization for Python

## Basics

- [Basic tips for optimizing the performace of your Python code](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

- [Code for the book "High Performance Python" by Micha Gorelick and Ian Ozsvald with OReilly](https://github.com/mynameisfiber/high_performance_python)

## Interfacing with C/C++

- [Interfacing with C from Scipy lecture notes](https://scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#introduction)
	* Very nice overview and examples of four approaches.
	1. [Python/C API](https://docs.python.org/3/c-api/index.html)
		- [Extending Python3.7 with C or C++](https://docs.python.org/3/extending/extending.html)
	2. [__ctypes__ -  A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
		- It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.
	3. [__SWIG__](http://www.swig.org/exec.html)
		- __SWIG__ is an interface compiler that connects programs written in C and C++ with scripting languages such as Python
	4. [__Cython__ - C-Extensions for Python](https://cython.org/)
		- [Basic tutorial of __Cython__](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html)
		- [Tutorial on how to use Cython to optimize Python code by Adrian Price-Whelan](https://github.com/adrn/cython-tutorial)
		- [Cython tutorial by Pauli Virtanen from 2011](https://python.g-node.org/python-summerschool-2011/_media/materials/cython/cython-slides.pdf)

### Only for C++ 

- [__Boost.Python__](https://www.boost.org/doc/libs/1_70_0/libs/python/doc/html/index.html)
	* __Boost.Python__, a C++ library which enables seamless interoperability between C++ and the Python programming language.

- [__pybind11__ - Seamless operability between C++11 and Python](https://github.com/pybind/pybind11)
	* __pybind11__ is a lightweight header-only library that exposes C++ types in Python and vice versa, mainly to create Python bindings of existing C++ code.
	* This is used by the __LSST__ developers, please see the [DM __Pybind11__ style guide](https://developer.lsst.io/pybind11/style.html) for details.

## Using Just-in-Time (JIT) Compiler

- [__pypy__ -  a fast, compliant alternative implementation of the Python language](http://pypy.org/)

- [__numba__ - makes Python code fast](http://numba.pydata.org/)
	- __Numba__ is an open source JIT compiler that translates a subset of Python and __NumPy__ code into fast machine code.  __Numba__only supports LLVM.
	- __Numba__ offers a range of options for parallelizing your code for CPUs and GPUs, often with only minor code changes.
	- [__Numpy__ supports in __Numba__](http://numba.pydata.org/numba-doc/0.15.1/numpy_support.html)
	- __Numba__ has a __vectorize__ and __guvectorize__ decorators that can be very useful.

- [__hope__ - A Python Just-In-Time compiler for astrophysical computations](https://github.com/jakeret/hope)
	- __hope__ is a specialized method-at-a-time JIT compiler written in Python for translating Python source code into C++ and compiles this at runtime.
	- Has not been updated for three yeears.

### Tutorial and notes

- [Optimizing Python in the Real World: NumPy, Numba, and the NUFFT by Jake VanderPlas](https://jakevdp.github.io/blog/2015/02/24/optimizing-python-with-numpy-and-numba/)

### Making Numpy faster

- [jax - GPU- and TPU-backed NumPy with differentiation and JIT compilation by Google](https://github.com/google/jax)
	* JAX is Autograd and XLA, brought together for high-performance machine learning research.

- [autograd - Efficiently computes derivatives of numpy code](https://github.com/HIPS/autograd)

### Other packages

- [How to speed up Python by scikit-learn](https://scikit-learn.org/stable/developers/performance.html)


## Parallel computing in Python

### Tutorial

- [An introduction to parallel programming using Python's multiprocessing module](https://sebastianraschka.com/Articles/2014_multiprocessing.html)
- [Speed Up Your Algorithms Part 3 — Parallel-ization](https://towardsdatascience.com/speed-up-your-algorithms-part-3-parallelization-4d95c0888748)

### Software

#### Common tools:

- [mpi4py - Python bindings for MPI](https://github.com/mpi4py/mpi4py)
- [joblib - a set of tools to provide lightweight pipelining in Python](https://github.com/joblib/joblib)
- [loky - Robust and reusable Executor for joblib](https://github.com/tomMoral/loky)
- [schwimmbad - A common interface to processing pools](https://github.com/adrn/schwimmbad)

#### More "Big Data" approach:

- [__Dask__ - Parallel computing with task scheduling](https://dask.org/)
	* __Dask__ provides advanced parallelism for analytics, enabling performance at scale for the tools you love
	* __Dask__ is open source and freely available. It is developed in coordination with other community projects like __Numpy__, __Pandas__, and __Scikit-Learn__.
	* [Official __Dask__ tutorial using Jupyter notebook](https://github.com/dask/dask-tutorial)

