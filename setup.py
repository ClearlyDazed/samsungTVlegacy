#!/usr/bin/env python

import setuptools

import samsungctl

setuptools.setup(
    name=samsungctl.__title__,
    version=samsungctls.__version__,
    description=samsungctl.__doc__,
    url=samsungctl.__url__,
    author=samsungctl.__author__,
    author_email=samsungctl.__author_email__,
    license=samsungctl.__license__,
    long_description=open("README.rst").read(),
    entry_points={
        "console_scripts": ["samsungctl-plus=samsungctl.__main__:main"]
    },
    packages=["samsungctl-plus"],
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
