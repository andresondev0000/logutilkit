#!/usr/bin/python3
import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="logutilkit",
    version="1.0.1",
    author="andresondev0000",
    author_email="shiningup1996@gmail.com",
    description="A small log package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andresondev0000/logutilkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
