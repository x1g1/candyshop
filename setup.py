#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup

from candyshop import (__author__, __email__, __version__, __url__,
                       __description__)


def read_requirements(reqfile):
    with open(reqfile, 'r') as r:
        reqs = filter(None, r.read().split('\n'))
    return [re.sub(r'\t*# pyup.*', r'', x) for x in reqs]


setup(
    name='candyshop',
    version=__version__,
    author=__author__,
    author_email=__email__,
    url=__url__,
    description=__description__,
    long_description=open('README.rst').read(),
    packages=['candyshop'],
    package_dir={'candyshop': 'candyshop'},
    include_package_data=True,
    install_requires=read_requirements('requirements.txt'),
    license=open('COPYING.rst').read(),
    zip_safe=False,
    keywords=['odoo', 'requirements'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=read_requirements('requirements-dev.txt')
)
