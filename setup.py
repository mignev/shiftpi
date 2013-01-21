#!/usr/bin/env python

from __future__ import with_statement
from shiftpi import version as shiftpi_version
import distutils.core
import os

# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

distutils.core.setup(name='shiftpi',
      version=shiftpi_version,
      description="ShiftPi is the easiest way to work with 74HC595 shift registers on your Raspberry Pi in Arduino style :). If you are an Arduino fan ... you'l love it :)",
      author='Marian Ignev',
      author_email='m@ignev.net',
      url='http://m.ignev.net/code/shiftpi',
      packages=['shiftpi'],
      long_description=read('README.md'),
      # install_requires = ['RPi.GPIO'],
      classifiers=[
          'Operating System :: POSIX',
          'Operating System :: POSIX :: BSD',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Shells',
          'Topic :: Utilities',
          ],
     )