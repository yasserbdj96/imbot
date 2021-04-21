#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
from imbot import imbot

# Example:3
#Open github website, login & delete a repository:
p3=imbot("github.json")
p3.run("login",'<USERNAME>','<PASSWORD>')
p3.run("repository_delete",'<USERNAME>/<REPOSITORY_NAME>','<PASSWORD>')
p3.end()
#e