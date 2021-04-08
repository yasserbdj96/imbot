#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com 
#s
from setuptools import setup, find_packages

# Setting up
setup(
    name="imbot",
    version='0.0.1',
    author="Yasser BDJ (Ro0t96)",
    author_email="by.root96@gmail.com",
    description='"imbot" for making a bot to control any website from json file.',
    long_description_content_type="text/markdown",
    long_description=open('README.rst').read(),
    packages=find_packages(),
    project_urls={  # Optional
        'Author Github': "https://github.com/byRo0t96",
        'Source Code': 'https://github.com/byRo0t96/imbot',
    },
    install_requires=['selenium'],
    keywords=['python','imbot'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
#e