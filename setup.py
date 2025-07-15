#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="epsilon-framework",
    version="0.1.0",
    description="Information-Consciousness Field Theory Framework",
    author="Brieuc de La Fournière", 
    author_email="ael@ifelse.world",
    url="https://if-else-world.github.io/epsilon/",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0", 
        "matplotlib>=3.5.0",
        "scikit-learn>=1.0.0",
        "scikit-image>=0.19.0",
        "pandas>=1.3.0",
        "seaborn>=0.11.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3.8+",
    ],
)
