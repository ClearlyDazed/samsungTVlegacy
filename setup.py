#!/usr/bin/env python

import setuptools

import samsungTVlegacy

setuptools.setup(
    name=samsungTVlegacy.__title__,
    version=samsungTVlegacy.__version__,
    description=samsungTVlegacy.__doc__,
    url=samsungTVlegacy.__url__,
    author=samsungTVlegacy.__author__,
    author_email=samsungTVlegacy.__author_email__,
    license=samsungTVlegacy.__license__,
    long_description=open("README.rst").read(),
    entry_points={
        "console_scripts": ["samsungTVlegacy=samsungTVlegacy.__main__:main"]
    },
    packages=["samsungTVlegacy"],
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
