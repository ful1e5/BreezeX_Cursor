#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="bxpkg",
    version="1.1.1",
    description="Generate 'BreezeX' cursor theme from PNGs file",
    url="https://github.com/ful1e5/BreezeX_Cursor",
    packages=["bxpkg"],
    package_dir={"bxpkg": "bxpkg"},
    author="Kaiz Khatri",
    author_email="kaizmandhu@gamil.com",
    install_requires=["clickgen==1.1.9"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3.8",
    zip_safe=True,
)
