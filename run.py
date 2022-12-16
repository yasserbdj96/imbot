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

# python run.py --headless <True/False> --json_data '<PATH_TO_YOUR_JSON_FILE>*' --opiration_title '<TITLE_OF_OPIRATION>*' --argvs '{"<ARGV_DATA_ID>":"<DATA_TO_INPUT>"}' --exec_path '<CHROMEDRIVER_PATH>'
# EX:
# python run.py --headless False --json_data './imbot-examples/google.json' --opiration_title 'search' --argvs '{"search_for":"yasserbdj96 github"}' --exec_path './chromedriver'
# *    = All inputs must be entered.

#START{
from imbot import *
import argparse

try:
    try:
        # for run as docker:
        import os
        headless = True if os.environ['headless']=="True" else False
        json_data = os.environ['json_data']
        opiration_title= os.environ['opiration_title']
        argvs=""
        exec_path=""
        try:
            argvs=os.environ['argvs']
        except:
            argvs=False
        who_is="docker"
        
    except:
        parser=argparse.ArgumentParser()

        parser.add_argument("--headless", help="Foo the program")
        parser.add_argument("--json_data", help="Foo the program")
        parser.add_argument("--opiration_title", help="Foo the program")
        parser.add_argument("--argvs", help="Foo the program")
        parser.add_argument("--exec_path", help="Foo the program")

        args=parser.parse_args()

        json_data=args.json_data
        headless=args.headless
        opiration_title=args.opiration_title
        argvs=args.argvs
        exec_path=args.exec_path

        who_is="script"
        #print(json_data,headless,opiration_title,argvs,exec_path)


    if exec_path!="" and exec_path!=None:
        p1=imbot(json_data,headless=headless,exec_path=exec_path)
    else:
        p1=imbot(json_data,headless=headless)

    if argvs!=False and argvs!="" and argvs!=None:
        import json
        argvs=json.loads(argvs)
        #
        m=""
        for key, value in argvs.items():
            m+=key+f"='{value}',"
        argvs=m[:-1]
        exec(f"print(p1.run('{opiration_title}',{argvs}))")
    else:
        exec(f"print(p1.run('{opiration_title}'))")
    # end
    p1.end()

except:
    if who_is=="docker":
        cm='''docker run -e headless=<True/False>* -e json_data='<PATH_TO_YOUR_JSON_FILE>*' -e opiration_title='<TITLE_OF_OPIRATION>*' -e argvs='<ARGV_DATA_ID>="<DATA_TO_INPUT>"' -i -t imbot:latest'''
    else:
        cm='''python run.py --headless <True/False> --json_data '<PATH_TO_YOUR_JSON_FILE>*' --opiration_title '<TITLE_OF_OPIRATION>*' --argvs '{"<ARGV_DATA_ID>":"<DATA_TO_INPUT>"}' --exec_path '<CHROMEDRIVER_PATH>' '''
    print("Usage : "+cm)
    print("# *    = All inputs must be entered.")
#}END.
