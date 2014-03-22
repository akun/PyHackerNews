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

        'pylint-django==0.3'
        'coverage==3.7.1',
        'django-nose==1.2',

        'Sphinx==1.2.2',
        'rst2pdf==0.93',
        'hieroglyph==0.6.5',
    ],
    test_suite='nose.collector',
)
