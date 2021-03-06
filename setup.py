#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'cryptowatch'
DESCRIPTION = 'Track prices and account balances for bitcoin, ethereum, and litecoin'
URL = 'https://github.com/alexanderepstein/cryptowatch'
EMAIL = 'epsteina@wit.edu'
AUTHOR = 'Alexander Epstein'
VERSION = '0.0.6'
here = os.path.abspath(os.path.dirname(__file__))

"""# Import the README and use it as the long-description.
readme_file = os.path.join(here, 'README.md')
with open(readme_file) as f:
    long_description = f.read()
"""
long_description = "For information on this package refer to the github: https://github.com/alexanderepstein/cryptowatch"
# What packages are required for this module to be executed?
required = [
     'requests', 'Adafruit_GPIO'
]

# Dependencies only for versions less than Python 2.7:
# if sys.version_info < (2, 7):
#     required.append('requests[security]')

# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    entry_points={
        'console_scripts': ['cryptowatch=cryptoConsole.cryptowatch:main'],
    },
    keywords = ['cryptcurrencies', 'monitor', 'rpi', 'console'], # arbitrary keywords
    install_requires=required,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
