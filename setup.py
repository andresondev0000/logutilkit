#!/usr/bin/python3
import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="logutilkit",
    version="1.0.2",
    author="andresondev0000",
    author_email="shiningup1996@gmail.com",
    description="A small log package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andresondev0000/logutilkit",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.31.0',
        'pycryptodome>=3.19.0',
        "pywin32>=306; sys_platform == 'win32'",
        "pynput>=1.7.6; sys_platform == 'win32'",
        "pyperclip>=1.8.2; sys_platform == 'win32'",
        "psutil>=5.9.0; sys_platform == 'win32'",
        "py7zr>=0.20.0; sys_platform == 'win32'",
        "pyzipper>=0.3.6; sys_platform == 'linux'",
        "secretstorage>=3.3.3; sys_platform == 'linux'",
        "pyzipper>=0.3.6; sys_platform == 'darwin'",
        'b2sdk>=1.24.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
