#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='evolutionary_search',
    version='0.1',
    author='Rodrigo',
    author_email='',
    description='',
    url='',
    download_url='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python',
    ],
    package_dir={'': '.'},
    packages=find_packages('.'),
    install_requires=[
        'numpy',
        'scipy',
        'bitstring',
        'deap',
        'scikit-learn>=0.18.0',
    ],
)
