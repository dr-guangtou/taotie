# Write a Python package

### Developer Guide

- [LSST DM Developer Guide](https://developer.lsst.io)
	* LSST的数据管理系统的开发指南是天文领域里非常具有参考价值的
	* Python编程风格：[DM Python style guide](https://developer.lsst.io/python/style.html) 
	* 类似的还有 [SKA develop portal](https://developerskatelescopeorg.readthedocs.io/en/latest/) (建设中...)


### Structure 

- "Dress for the job you want, not the job you have."

- [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
	* 从组织文件到代码结构，比较好的入门阅读
	
- [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/index.html)
	* 可读性也很强: aims to put forth an opinionated and specific pattern to make trouble-free packages for community use

- [Cookiecutter - A logical, reasonably standardized, but flexible project structure for doing and sharing data science work](https://drivendata.github.io/cookiecutter-data-science/)
	* 一个很好的组织基于数据的项目的例子，其中关于“Keep secrets and configuration out of version control”的部分很有用。

### `setup.py`

- [A Human's Ultimate Guide to setup.py](https://github.com/kennethreitz/setup.py)
    - This is very good template for using `setup.py` 


### Readme 

- [Art of README](https://github.com/noffle/art-of-readme)
	- [中文版](https://github.com/noffle/art-of-readme/blob/master/README-zh.md) 基本上，想学习如何写好Readme看这篇就够了

### Document

- [Writing change-controlled documentation](https://developer.lsst.io/project-docs/change-controlled-docs.html)
	* LSST数据管理系统提供的指南

- [LSST DM的Documenting Python APIs with Docstrings](https://developer.lsst.io/python/numpydoc.html#py-docstring-short-summary)
	* LSST数据管理系统的代码文档规范，很好的例子。LSST使用Numpydoc格式

### Test 

- [LSST DM的Python Unit Testing Guide](https://developer.lsst.io/python/testing.html)
	* LSST数据管理系统的代码测试规范：LSST tests should be written using the unittest framework, with default test discovery, and should support being run using the pytest test runner

### Visualization

- [pycallgraph - Python module that creates call graphs for Python programs](https://github.com/gak/pycallgraph)
	* 可惜原作者已经不再维护了，有一个还在更新的fork: [pycallgraph2](https://github.com/daneads/pycallgraph2)

### Optimization

- [Optimizing Python Code - Scipy Lecture Notes](http://www.scipy-lectures.org/advanced/optimizing/)
	* 1. Make it work; 2: Make it work reliably; 3: Optimization
	* No optimization without measuring: profiling and timing
	* Moving computation or memory allocation outside a for loop; Vectorizing for loops; Broadcasting; 
	  Use in place operations; Be easy on the memory: use views, and not copies; 

- [Profiling Python using cProfile: a concrete case](https://julien.danjou.info/guide-to-python-profiling-cprofile-concrete-case-carbonara/)
	* `cProfile` 对于发现程序中的瓶颈很有帮助
	
- [LSST DM Python performance profiling]
