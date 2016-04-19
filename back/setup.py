#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name = 'taiga-contrib-google-auth',
    version = ":versiontools:taiga_contrib_github_auth:",
    description = "The Taiga plugin for github authentication",
    long_description = "",
    keywords = 'taiga, github, auth, plugin',
    author = 'HanWool Lee',
    author_email = 'kudnya@gmail.com',
    url = 'https://github.com/seyriz/taiga-contrib-google-auth',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 1 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
