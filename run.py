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

# python run.py "headless=<True/False>" "json_data='<PATH/TO/JSON/FILE>'" "opiration_title='<TITLE_OF_OPIRATION>'" "argvs={'<ARGV_DATA_ID>':'<DATA_TO_INPUT>'}"
# EX:
# python run.py "headless=False" "json_data='./examples/google.json'" "opiration_title='search'" "argvs={'search_for':'yasserbdj96 on github'}"
# *    = All inputs must be entered.

#START{
from imbot import *

try:
    # for run as docker:
    import os
    headless = True if os.environ['headless']=="True" else False
    json_data = os.environ['json_data']
    opiration_title= os.environ['opiration_title']
    argvs=""
    try:
        argvsx=os.environ['argvs']
        
    except:
        argvsx=False
    argvs=argvsx
except:
    # for run as python script:
    import sys
    argvs=""
    argvsx=sys.argv[1:]
    for i in range(len(argvsx)):
        exec(argvsx[i])
    m=""
    if argvs!="":
        for key, value in argvs.items():
            m+=key+f"='{value}',"
        argvsx=m[:-1]
    else:
        argvs=False


p1=imbot(json_data,headless=headless)

if argvs!=False:
    exec(f"print(p1.run('{opiration_title}',{argvsx}))")
else:
    exec(f"print(p1.run('{opiration_title}'))")

# end
p1.end()
#}END.