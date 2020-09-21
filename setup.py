#!/usr/bin/env python
"""
EST Client
==========
"""
import os
from setuptools import setup

setup(
    name = "est",
    version = "0.2.1",
    author = "Laurent Luce",
    author_email = "laurentluce49@yahoo.com",
    description = ('Client to interact with an EST server - RFC 7030.'),
    license = "MIT",
    keywords = "Enrollment secure transport",
    packages=['est'],
    install_requires=[
        'pyOpenSSL',
        'asn1crypto',
        'requests'
    ],
    long_description='Client to interact with an EST server - RFC 7030.',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
