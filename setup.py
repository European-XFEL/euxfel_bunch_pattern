#!/usr/bin/env python
from os.path import dirname
from setuptools import setup, find_packages


def _get_version_string():
    try:
        from karabo.packaging.versioning import get_package_version
    except ImportError:
        print("WARNING: Karabo framework not found! Version will be blank!")
        return ''

    return get_package_version(dirname(__file__))

setup(name='xfel_bunch_pattern',
      version=_get_version_string(),
      description='',
      long_description='',
      url='',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      package_data={},
      requires=[],
      )
