# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Yasaman Moradi Fard",
    author_email="yasaman.moradi.fard@fau.de",
    packages=find_packages(),
    install_requires=["random"]
)