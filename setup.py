#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2014 Building Energy Inc
:license: see LICENSE for details.
"""
from setuptools import setup, find_packages

setup(
    name='stats',
    version='0.0.1',
    description='stats demo app',
    long_description=open('README.md').read(),
    author='Aleck Landgraf',
    author_email='aleck.landgraf@buildingenergy.com',
    url='http://github.com/buildingenergy/seed_demo_app',
    license='Apache2',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
