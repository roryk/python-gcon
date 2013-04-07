#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name = "python-gcon",
      version = "0.0.1",
      author = "",
      author_email = "rory.kirchner@gmail.com",
      description = "Python API for interacting with several genome storage solutions.",
      license = "MIT",
      url = "https://github.com/roryk/gcon",
      namespace_packages = ["gcon"],
      packages = find_packages(),
      scripts = [],
      dependency_links=['http://github.com/roryk/basespace-python-sdk/tarball/master#egg=basespace-python-sdk-0.1.2'],
      install_requires = ['bioblend',
                          'BaseSpacePy']
    )
