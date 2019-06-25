# Resource about C Programming Language

## Learning C

* **The best way to learn programming is, always, writing your own code!**

* [Why Code in C Anymore?....Instead of C++](http://www.drdobbs.com/cpp/why-code-in-c-anymore/240149452)
    - C still has a little advantage on the performance and portability.

* [CS2022: Introduction to C at Cornell](http://www.cs.cornell.edu/courses/cs2022/2011sp/)
    - Lecture slides are available.

* [learn-c.org free interactive C tutorial](https://www.learn-c.org/)

* [`30-seconds-of-c`](https://github.com/fredsiika/30-seconds-of-c)
    - Curated collection of useful C Programming tutorials, snippets, and projects that you can understand in 30 seconds or less

## Useful Libraries

### Performance

* [`mimalloc` - mimalloc is a compact general purpose allocator with excellent performance](https://github.com/microsoft/mimalloc)
    - By Microsoft. mimalloc (pronounced "me-malloc") is a general purpose allocator with excellent performance characteristics. It is a drop-in replacement for malloc and can be used in other programs without code changes.

### Numerical

* [`GSL` - GNU Scientific Library](https://www.gnu.org/software/gsl/)
    - The library provides a wide range of mathematical routines such as random number generators, special functions and least-squares fitting. There are over 1000 functions in total with an extensive test suite.
    - The [online reference manual can be found here](https://www.gnu.org/software/gsl/doc/html/index.html).

* [`FFTW`](http://www.fftw.org/)
    - `FFTW` is a C subroutine library for computing the discrete Fourier transform (DFT) in one or more dimensions, of arbitrary input size, and of both real and complex data (as well as of even/odd data, i.e. the discrete cosine/sine transforms or DCT/DST).
    - The [online manual can be found here](http://fftw.org/fftw3_doc/)

### Astronomy Related

* [`cfitsio` - ANSI C routines for reading and writing FITS format data files](https://github.com/healpy/cfitsio)

## Specific Topics

### Multiprocessing

### GPU Enhancement

## Code to Study

* [`sextractor` - Extract catalogs of sources from astronomical images](https://github.com/astromatic/sextractor)

* [`psfex` - Generate PSF super-tabulated models](https://github.com/astromatic/psfex)

* [`CCL` - DESC Core Cosmology Library](https://github.com/LSSTDESC/CCL)
    - Also teaches you how to interact with Python.

* [`Corrfunc` - fast correlation functions on the CPU](https://github.com/manodeep/Corrfunc)
    - `utils` are written in C; and wrapped in Python.

### On Interacting with Python

* [`sep` - Python and C library for source extraction and photometry](https://github.com/kbarbary/sep)
    - Using `Cython`.
* [`cosmology` - Some code for calculating cosmological distances](https://github.com/esheldon/cosmology)
    - By Erin Sheldon. Using `CPython`
* [`smatch` - Code to match points on the sphere using the healpix scheme](https://github.com/esheldon/smatch)
    - By Erin Sheldon. Using `CPython`