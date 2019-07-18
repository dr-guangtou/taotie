Write a Python package
======================

Developer Guide
~~~~~~~~~~~~~~~

-  `LSST DM Developer Guide <https://developer.lsst.io>`__

   -  LSST的数据管理系统的开发指南是天文领域里非常具有参考价值的
   -  Python编程风格：\ `DM Python style
      guide <https://developer.lsst.io/python/style.html>`__
   -  类似的还有 `SKA develop
      portal <https://developerskatelescopeorg.readthedocs.io/en/latest/>`__
      (建设中…)

Structure
~~~~~~~~~

-  “Dress for the job you want, not the job you have.”

-  `Structuring Your
   Project <https://docs.python-guide.org/writing/structure/>`__

   -  从组织文件到代码结构，比较好的入门阅读

-  `How To Package Your Python
   Code <https://python-packaging.readthedocs.io/en/latest/index.html>`__

   -  可读性也很强: aims to put forth an opinionated and specific
      pattern to make trouble-free packages for community use

-  `Cookiecutter - A logical, reasonably standardized, but flexible
   project structure for doing and sharing data science
   work <https://drivendata.github.io/cookiecutter-data-science/>`__

   -  一个很好的组织基于数据的项目的例子，其中关于“Keep secrets and
      configuration out of version control”的部分很有用。

Code Format
~~~~~~~~~~~

-  It is good practice to follow well-established code format. Not only
   it can help you write codes that are nice looking and easy to
   maintain, it will help others to read and contribute to the code.
-  For Python, `the PEP8 style
   guide <https://www.python.org/dev/peps/pep-0008/>`__ is the most
   important one. Some of these rules feel unecessary and annoying, but
   there are always good reasons behind them.
-  `autopep8: A tool that automatically formats Python code to conform
   to the PEP 8 style guide <https://github.com/hhatto/autopep8>`__
-  `black: The uncompromising Python code
   formatter <https://github.com/python/black>`__

   -  Blackened code looks the same regardless of the project you’re
      reading. Formatting becomes transparent after a while and you can
      focus on the content instead.

-  `yapf: A formatter for Python files from
   Google <https://github.com/google/yapf>`__

**setup.py**
~~~~~~~~~~~~

-  `A Human’s Ultimate Guide to
   setup.py <https://github.com/kennethreitz/setup.py>`__

   -  This is very good template for using **setup.py**

Readme
~~~~~~

-  `Art of README <https://github.com/noffle/art-of-readme>`__

   -  `中文版 <https://github.com/noffle/art-of-readme/blob/master/README-zh.md>`__
      基本上，想学习如何写好Readme看这篇就够了

-  `readme-md-generator - CLI that generates beautiful README.md
   files <https://github.com/kefranabg/readme-md-generator>`__

   -  **readme-md-generator** will suggest you default answers by
      reading your package.json and git configuration.

Document
~~~~~~~~

General instructions
^^^^^^^^^^^^^^^^^^^^

-  `Writing change-controlled
   documentation <https://developer.lsst.io/project-docs/change-controlled-docs.html>`__

   -  Manual provided by LSST DM team

-  `LSST DM的Documenting Python APIs with
   Docstrings <https://developer.lsst.io/python/numpydoc.html#py-docstring-short-summary>`__

   -  Also very good example by LSST DM. LSST adopts the **Numpydoc**
      format.

Tools
^^^^^

-  `sphinx - Python documentation
   generator <https://www.sphinx-doc.org/en/1.5/index.html>`__

   -  **Sphinx** is a tool that makes it easy to create intelligent and
      beautiful documentation.
   -  **Sphinx** uses
      `reStructuredText <http://docutils.sourceforge.net/rst.html>`__ as
      its markup language, and many of its strengths come from the power
      and straightforwardness of **reStructuredText** and its parsing
      and translating suite, the
      `Docutils <http://docutils.sourceforge.net/>`__.
   -  `First steps with
      sphinx <https://www.sphinx-doc.org/en/1.5/tutorial.html>`__
   -  `On Markdown v.s.
      reStructuredText <https://gist.github.com/dupuy/1855764>`__:
      **Markdown** is easy to use; **reStructuredText** is more
      extensible and powerful.
   -  `Brandon’s Sphinx Tutorial from PyCon
      2013 <https://buildmedia.readthedocs.org/media/pdf/brandons-sphinx-tutorial/latest/brandons-sphinx-tutorial.pdf>`__
   -  `Sphinx Tutorial by Eric
      Holscher <https://sphinx-tutorial.readthedocs.io/start/>`__ is the
      best place to start. The `GitHub repo
      itself <https://github.com/ericholscher/sphinx-tutorial>`__ is a
      very good example.
   -  `Sphinx Themes <https://sphinx-themes.org/>`__

-  `pandoc - A universal document converter <https://pandoc.org/>`__

   -  If you need to convert files from one markup format into another,
      **pandoc** is your swiss-army knife. e.g. It can convert
      **reStructuredText** to/from **Markdown**.

-  `rinohtype - The Python document
   processor <https://github.com/brechtm/rinohtype>`__

   -  **Rinohtype** is a document processor in the style of **LaTeX**.
      It renders structured documents to PDF based on a document
      template and a style sheet.
   -  `A Simple Tutorial on How to document your Python Project using
      Sphinx and
      Rinohtype <https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b>`__

-  `numpydoc – Numpy’s Sphinx
   extensions <https://github.com/numpy/numpydoc>`__

   -  `The numpydoc docstring format
      guide <https://numpydoc.readthedocs.io/en/latest/format.html>`__

-  `Doxygen - Generate documentation from source
   code <http://www.doxygen.nl/>`__

   -  **Doxygen** is the de facto standard tool for generating
      documentation from annotated C++ sources, but it also supports
      other popular programming languages such as C, Objective-C, C#,
      PHP, Java, Python, IDL.
   -  `The Doxygen document site for Galsim is a very good
      example <http://galsim-developers.github.io/GalSim/index.html>`__

-  `Read the Docs - Technical documentation lives
   here <https://readthedocs.org/>`__

   -  Read the Docs simplifies software documentation by automating
      building, versioning, and hosting of your docs for you.

Test
~~~~

-  `Testing Your Code from the Hitchhiker’s Guide to
   Python <https://docs.python-guide.org/writing/tests/>`__

   -  A nice summary of multiple approaches of unit test in Python.

-  `Getting Started With Testing in Python from
   RealPython <https://realpython.com/python-testing/>`__

   -  Another very nice introduction, convering **unittest**,
      **pytest**, and **nose**.

-  `LSST DM: Python Unit Testing
   Guide <https://developer.lsst.io/python/testing.html>`__

   -  LSST DM standard is a very good example：LSST tests should be
      written using the **unittest** framework, with default test
      discovery, and should support being run using the **pytest** test
      runner

-  `unittest — Unit testing
   framework <https://docs.python.org/3/library/unittest.html>`__

   -  Basic unit test in Python. The `list of assertion methods is
      here <https://docs.python.org/3/library/unittest.html#assert-methods>`__

-  `pytest - helps you write better
   programs <https://docs.pytest.org/en/latest/>`__

   -  The **pytest** framework makes it easy to write small tests, yet
      scales to support complex functional testing for applications and
      libraries.
   -  `Examples and customization tricks for
      pytest <https://docs.pytest.org/en/latest/example/>`__: this is
      very useful.

-`nose2 - Nicer testing for
Python <https://github.com/nose-devs/nose2>`__ \* **nose2**\ ’s purpose
is to extend unittest to make testing nicer and easier to understand.

Code Coverage
^^^^^^^^^^^^^

-  `Code coverage <https://en.wikipedia.org/wiki/Code_coverage>`__:

..

   In computer science, test coverage is a measure used to describe the
   degree to which the source code of a program is executed when a
   particular test suite runs. A program with high test coverage,
   measured as a percentage, has had more of its source code executed
   during testing, which suggests it has a lower chance of containing
   undetected software bugs compared to a program with low test
   coverage. – Wikipedia

-  `Coverage.py - Code coverage testing for
   Python <https://github.com/nedbat/coveragepy>`__

   -  **Coverage.py** measures code coverage, typically during test
      execution. It uses the code analysis tools and tracing hooks
      provided in the Python standard library to determine which lines
      are executable, and which have been executed.
   -  `Quick start
      guide <https://coverage.readthedocs.io/en/v4.5.x/#quick-start>`__
   -  `pytest has a pytest-cov
      plugin <https://pytest-cov.readthedocs.io/en/latest/>`__

-  `Codecov - Empower developers with tools to improve code quality and
   testing <https://github.com/codecov>`__

   -  It is web service that improves your code review workflow and
      quality. Free for open source. Plans starting at $2.50/month per
      repository. You can login with your **GitHub** or **Bitbucket**
      account.
   -  `Here is a Python example for
      Codecov <https://github.com/codecov/example-python>`__

Optimization
~~~~~~~~~~~~

-  `Optimizing Python Code - Scipy Lecture
   Notes <http://www.scipy-lectures.org/advanced/optimizing/>`__

   -  

      1. Make it work; 2: Make it work reliably; 3: Optimization

   -  No optimization without measuring: profiling and timing
   -  Moving computation or memory allocation outside a for loop;
      Vectorizing for loops; Broadcasting; Use in place operations; Be
      easy on the memory: use views, and not copies;

-  `LSST DM Python performance
   profiling <https://developer.lsst.io/python/profiling.html>`__

   -  Very good guide.

-  `The Python
   Profilers <https://docs.python.org/3/library/profile.html>`__

   -  Python comes with a series of profiling tools. The most useful
      ones are **cProfile**, **profile**, and **pstats** (convert
      profiling results into a report)

-  `Profiling Python using cProfile: a concrete
   case <https://julien.danjou.info/guide-to-python-profiling-cprofile-concrete-case-carbonara/>`__

   -  **cProfile** 对于发现程序中的瓶颈很有帮助

-  `line_profiler and kernprof - Line-by-line profiling for
   Python <https://github.com/rkern/line_profiler>`__

   -  **line_profiler** is a module for doing line-by-line profiling of
      functions. **kernprof** is a convenient script for running either
      line_profiler or the Python standard library’s cProfile or profile
      modules, depending on what is available.
   -  Can use **cProfile** to identify “hotspot” (function that is the
      “bottleneck”), then use **line_profiler** to exame the issue
      carefully.

Visualization
^^^^^^^^^^^^^

-  `gprof2dot - Converts profiling output to a dot
   graph <https://github.com/jrfonseca/gprof2dot>`__

   -  A general tool to convert different profiling software output to a
      dot graph.

-  `SnakeViz - An in-browser Python profile
   viewer <https://jiffyclub.github.io/snakeviz>`__

   -  **SnakeViz** is a viewer for Python profiling data that runs as a
      web application in your browser.

-  `pycallgraph - Python module that creates call graphs for Python
   programs <https://github.com/gak/pycallgraph>`__

   -  No longer maintained by the original author, but still available
      through a fork:
      `pycallgraph2 <https://github.com/daneads/pycallgraph2>`__
