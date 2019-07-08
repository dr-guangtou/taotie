# Basic Reference for Learning Python

 There are clearly too many guide and tutorial for Python, some of which are quite good. Here is just a personal selection.

----

## Basic

* [Hitchhiker's Guide to Python](https://github.com/realpython/python-guide)
    - The actual guide book is [here](docs.python-guide.org)

* [A Byte of Python](https://python.swaroopch.com/)
    - "A Byte of Python" is a free book on programming using the Python language. It serves as a tutorial or guide to the Python language for a beginner audience.

* [Awesome Python](https://github.com/vinta/awesome-python)
    - A curated list of awesome Python frameworks, libraries, software and resources.

## Dig Deeper

* [All Algorithms implemented in Python](https://github.com/TheAlgorithms/Python)
    - These implementations are for learning purposes. They may be less efficient than the implementations in the Python standard library.

* Python Standard Library is a very good place to start learning Python:
    - There are a lot of useful tools in the standard library.
    - [A brief tour of the standard library](https://docs.python.org/3/tutorial/stdlib.html#operating-system-interface)
    - [The Reference of the Python Standard Library](https://docs.python.org/3/library/)

## Managing Python Packages

### [Anaconda](https://www.anaconda.com/)

* `Anaconda` distribution is the easiest way to perform Python/R data science and machine learning on all platforms. It can help you create environments with different Python versions, and manage libraries and dependencies in Python.
    - It is an easy way to start with Python programming without worrying too much about installing packages all by yourself.
    - [Getting started with `Anaconda`](https://docs.anaconda.com/anaconda/user-guide/getting-started/) and the [`Anaconda` tutorials](https://docs.anaconda.com/anaconda/navigator/tutorials/) are good places to start.

* [`AstroConda` - Conda for astronomers](https://astroconda.readthedocs.io/en/latest/)
    - `AstroConda` is a free Conda channel maintained by the Space Telescope Science Institute (STScI) 
### `pip`: Python Package Installer

* One important reason to use `Python` in science is that there are already a huge number of great tools prepared to make your life easier.
* The most useful tool is [`pip` - The Python Package Installer](https://pip.pypa.io/en/stable/).
    - `pip` is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes
    - [This complete reference guide](https://pip.pypa.io/en/stable/reference/) is very useful.
    - [What Is Pip? A Guide for New Pythonistas](https://realpython.com/what-is-pip/)

* [`pip-tools` - A set of tools to keep your pinned Python dependencies fresh](https://github.com/jazzband/pip-tools)
    - A set of command line tools to help you keep your pip-based packages fresh, even when you've pinned them.

## Start-up Package

* The most basic packages you want to use on daily bases.

* `Scipy` ecosystem:
    * [`Numpy` - Base N-dimensional array package](https://www.numpy.org/)
    * [`SciPy` - Fundamental library for scientific computing](https://github.com/scipy/scipy/)
    * [`SymPy` - a Python library for symbolic mathematics](https://www.sympy.org/en/index.html)
    * [Numpy and Scipy Documentation](https://docs.scipy.org/doc/)
    * [Quickstart tutorial of `Numpy`](https://www.numpy.org/devdocs/user/quickstart.html)
    * [Scipy Lecture Notes - One document to learn numerics, science, and data with Python](https://scipy-lectures.org/)
    * [A Visual Intro to NumPy and Data Representation](https://jalammar.github.io/visual-numpy/)

* [`pandas` - Python Data Analysis Library](http://pandas.pydata.org/)
    - `pandas` is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
    - [Online document of `pandas`](http://pandas.pydata.org/pandas-docs/stable/)

* [`matplotlib` - Comprehensive 2D Plotting](https://docs.scipy.org/doc/)
    - `Matplotlib` is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
    - [Online document of `matplotlib`](https://matplotlib.org/users/index.html); and the [`matplotlib` gallery](https://matplotlib.org/gallery/index.html) are very helpful resources to learn.

* [`Bokeh` - ](https://bokeh.pydata.org/en/latest/)
    - `Bokeh` is an interactive visualization library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of versatile graphics, and to extend this capability with high-performance interactivity over very large or streaming datasets.
    - [`Bokeh` user guide](https://bokeh.pydata.org/en/latest/docs/user_guide.html#userguide) and the [reference guide](https://bokeh.pydata.org/en/latest/docs/reference.html#refguide) are very useful. The [gallery of examples](https://bokeh.pydata.org/en/latest/docs/gallery.html) is also a good place to start.

* Interactive Python computing:
    * [`Jupyter` environment](https://jupyter.org/)
        - Project `Jupyter` exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages.
        - The `Jupyter` Notebook App is a server-client application that allows editing and running notebook documents via a web browser.
    * [`IPython` - Interactive computing](http://ipython.org/)
        - `IPython` provides a rich architecture for interactive computing
        - [`nbviewer` - A simple way to share Jupyter notebooks](https://nbviewer.jupyter.org/)
    * [Jupyter/IPython Notebook Quick Start Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/index.html)

* [`scikit-learn` - Machine learning in Python](https://github.com/scikit-learn/scikit-learn)
    - `scikit-learn` is a Python module for machine learning built on top of SciPy.
    - [Online document of `scikit-learn`](https://scikit-learn.org/stable/user_guide.html) and [`scikit-learn` Tutorials](https://scikit-learn.org/stable/tutorial/index.html)

* [`scikit-image` - Image processing in Python](https://scikit-image.org/)
    - `scikit-image` is a collection of algorithms for image processing. 
    - [Tutorials of `skimage`](https://github.com/scikit-image/skimage-tutorials) and [gallery of examples](https://scikit-image.org/docs/dev/auto_examples/) are very useful.

* [`astropy` - Community Python library for astronomer](https://www.astropy.org/)
    - The `Astropy` Project is a community effort to develop a common core package for Astronomy in Python and foster an ecosystem of interoperable astronomy packages.
    - [Online document of `astropy` is here](http://docs.astropy.org/en/stable/index.html)
    - [`Learn.Astropy` - Tutorials, documentation, and examples of `astropy`](http://learn.astropy.org/)

* [`Scrapy` - A fast high-level web crawling & scraping framework for Python](https://scrapy.org/)
    - An open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way.

## Tricks and Tips