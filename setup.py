#!/usr/bin/env python3 
from setuptools import setup, find_packages

setup(
    name="tangods-softimax-pie754",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Device server for the PI E754 motion controller at Softimax",
    author="Igor Beinik",
    author_email="igor.beinik@maxiv.lu.se",
    license="GPLv3",
    url="https://gitlab.maxiv.lu.se/softimax/tangods-softimax-pie754",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['pytango', 'pipython'],
    entry_points={
        'console_scripts': [
            'SoftiPIE754 = SoftiPIE754.SoftiPIE754:main',
        ],
    },
)
