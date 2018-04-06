#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ENAbler',
    version='0.1.0',

    description='programmatic ENA submission',

    url='https://github.com/SGBC/ENAbler',
    download_url='https://github.com/SGBC/ENAbler/tarball/0.1.0',
    author='Hadrien Gourlé, Oskar Karlsson',
    author_email='hadrien.gourle@slu.se, oskar.e.karlsson@slu.se',

    license='MIT',
    packages=find_packages(),

    tests_require=['nose'],
    include_package_data=True,

    entry_points={
        'console_scripts': ['enabler = enabler.app:main'],
    }
)
