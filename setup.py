#!/usr/bin/env python

import setuptools

import samsungctl_legacy

setuptools.setup(
    name=samsungctl_legacy.__title__,
    version=samsungctl_legacy.__version__,
    description=samsungctl_legacy.__doc__,
    url=samsungctl_legacy.__url__,
    author=samsungctl_legacy.__author__,
    author_email=samsungctl_legacy.__author_email__,
    license=samsungctl_legacy.__license__,
    long_description=open("README.rst").read(),
    entry_points={
        "console_scripts": ["samsungctl-legacy=samsungctl-legacy.__main__:main"]
    },
    packages=["samsungctl_legacy"],
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
