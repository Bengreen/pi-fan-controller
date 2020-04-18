#!/usr/bin/env python

import setuptools
import os


def find_version():
    tag = os.environ.get("TAG", "0.0.0")
    return tag


setuptools.setup(
    name="pyfan",
    version=find_version(),
    description="Raspberry PI fan controller",
    author="Ben Greene",
    author_email="BenJGreene@gmail.com",
    url="https://www.undefined.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
    },
    zip_safe=False,
    install_requires=[
        "gpiozero==1.5.1",
        "RPi.GPIO==0.7.0",
    ],
    setup_requires=[
    ],
    extras_require={
        # "dev": [
        # ]
    },
    entry_points={
    },
)
