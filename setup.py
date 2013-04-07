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
      install_requires = ['bioblend']
    )
