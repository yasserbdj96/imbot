#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
from imbot.imbotversion import __version__
from setuptools import setup,find_packages

setup(
    name="imbot",
    version=__version__,
    author="yasserbdj96",
    author_email="yasser.bdj96@gmail.com",
    description='''imbot - create a bot to control any website.''',
    long_description_content_type="text/markdown",
    long_description=open('README_PYPI.md','r', encoding="utf8").read(),
    license='''Apache Software License''',
    packages=find_packages(),
    project_urls={
        'Source': "https://github.com/yasserbdj96/imbot",
        'WebSite': "https://yasserbdj96.github.io/imbot",
        #'Documentation': "https://yasserbdj96.github.io/imbot",
        'Chat': "https://gitter.im/yasserbdj96/imbot",
        'Author WebSite':"https://yasserbdj96.github.io/"
    },
    install_requires=['selenium','hexor','asciitext'],
    keywords=['yasserbdj96','python','bot','website bot','robot'],
        classifiers=[
        "Environment :: Web Environment",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP"
    ],
    python_requires=">=3.x.x"
)
#}END.
