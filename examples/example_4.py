#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
from imbot import imbot

# Example:4
#Open github website, login and delete a list of repositories:
p4=imbot("github.json",5)
p4.run("login",'<USERNAME>','<PASSWORD>')
f=open("list.txt","r").read().split('\n')#type of list is "<USERNAME>/<REPOSITORY_NAME>" in any line
for x in f:
    p4.run("repository_delete",x,'<PASSWORD>')
p4.end()
#e