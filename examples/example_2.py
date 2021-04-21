#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
from imbot import imbot

# Example:1
#Open github website, login & go to your profile:
p2=imbot("github.json")
p2.run("login",'<USERNAME>','<PASSWORD>')
p2.run("profile")
p2.end()
#e