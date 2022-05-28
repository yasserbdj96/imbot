#!/usr/bin/env python
# coding:utf-8
#code by:YasserBDJ96
#email:yasser.bdj96@gmail.com

#START{
from setuptools import setup,find_packages
setup(
    name="imbot",
    version="0.1.3",
    author="YasserBDJ96",
    author_email="yasser.bdj96@gmail.com",
    description='''imbot for making a bot to control any website.''',
    long_description_content_type="text/markdown",
    long_description=open('README.md','r').read(),
    license='''MIT License''',
    packages=find_packages(),
    url="https://yasserbdj96.github.io/",
    project_urls={
        'Source Code': "https://github.com/yasserbdj96/imbot",
        'Instagram': "https://www.instagram.com/yasserbdj96/",
    },
    install_requires=['selenium','hexor','asciitext'],
    keywords=['yasserbdj96','python','bot','website bot','robot'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Topic :: Communications :: Email'
    ],
    python_requires=">=3.x.x"
)
#}END.
