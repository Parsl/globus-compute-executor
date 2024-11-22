import os
import re
from pathlib import Path

from setuptools import find_namespace_packages, setup

REQUIRES = [
    "globus-compute-sdk==2.31.0",
    "parsl==2024.11.18",
]

TEST_REQUIRES = [
    "flake8==3.8.0",
    "pytest>=7.2",
    "pytest-mock",
    "pyfakefs",
    "coverage",
    # easy mocking of the `requests` library
    "responses",
]

DEV_REQUIRES = TEST_REQUIRES + [
    "pre-commit",
]


def parse_version():
    # single source of truth for package version
    version_string = ""
    version_pattern = re.compile(r'__version__ = "([^"]*)"')
    with open(os.path.join("globus_compute_executor", "version.py")) as f:
        for line in f:
            match = version_pattern.match(line)
            if match:
                version_string = match.group(1)
                break
    if not version_string:
        raise RuntimeError("Failed to parse version information")
    return version_string


directory = Path(__file__).parent
long_description = (directory / "PyPI.md").read_text()


setup(
    name="globus-compute-executor",
    version=parse_version(),
    packages=find_namespace_packages(
        include=["globus_compute_executor", "globus_compute_executor.*"]
    ),
    package_data={"globus_compute_executor": ["py.typed"]},
    description="Globus Compute adapter for plugging into Parsl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=REQUIRES,
    extras_require={
        "dev": DEV_REQUIRES,
        "test": TEST_REQUIRES,
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    keywords=["Globus Compute", "FaaS", "Function Serving"],
    author="Globus Compute Team",
    author_email="support@globus.org",
    license="Apache License, Version 2.0",
    url="https://github.com/globus/globus-compute",
)
