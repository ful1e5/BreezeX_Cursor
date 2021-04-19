#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="bxpkg",
    version="1.1.1",
    description="Generate 'BreezeX' cursor theme from PNGs file",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    author="Kaiz Khatri",
    author_email="kaizmandhu@gamil.com",
    install_requires=["clickgen==1.1.9"],
    url="https://github.com/ful1e5/BreezeX_Cursor",
    project_urls={
        "Bug Tracker": "https://github.com/ful1e5/BreezeX_Cursor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires=">=3.8",
    zip_safe=True,
)
