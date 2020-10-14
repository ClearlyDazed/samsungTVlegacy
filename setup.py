#!/usr/bin/env python

import setuptools

import samsungctl

setuptools.setup(
    name=samsungctl_plus.__title__,
    version=samsungctl_plus.__version__,
    description=samsungctl_plus.__doc__,
    url=samsungctl_plus.__url__,
    author=samsungctl_plus.__author__,
    author_email=samsungctl_plus.__author_email__,
    license=samsungctl_plus.__license__,
    long_description=open("README.rst").read(),
    entry_points={
        "console_scripts": ["samsungctl_plus=samsungctl.__main__:main"]
    },
    packages=["samsungctl_plus"],
    install_requires=[],
    extras_require={
        "websocket": ["websocket-client"],
        "interactive_ui": ["curses"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
    ],
)
