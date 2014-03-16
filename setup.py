#!/usr/bin/env python


import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='PyHackerNews',
    version='0.0.1',
    description='Hacker News, write in Python',
    author='akun',
    url='https://github.com/akun/PyHackerNews',
    packages=[
        'pyhn',
    ],
    package_dir={'pyhn': 'pyhn'},
    install_requires=[
        'Django==1.6.2',
        'python-social-auth==0.1.22',
        'nose==1.3.0',
        'Sphinx==1.1.3',
    ],
    test_suite='nose.collector',
)
