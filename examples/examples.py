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


"""
Default json code:
{
    "url":"<WEBSITE_URL>",
    "<OPIRATION_TITLE>":{
        "operations":[
           {"type":"<xpath/link_text/id/name/tag_name>","code":"<ELEMENT_CODE>","arg_code":"<VARIABLE_NAME>","opt":"<click/put/get>","arg_data":"<VARIABLE_NAME>","data":"<YOUR_DATA>","sleep":<Seconds>}
        ]
    }
}

Help:
# Types of finding elements : "type"=[id,name,xpath,link_text,partial_link_text,tag_name,class_name,css_selector]
# If you don't use the 'code' key, you must use the 'arg_code' key to enter data from your script.
# If you don't use the 'data' key, you must use the 'arg_data' key to enter data from your script.
# When using the 'put' option you must use 'data' or 'arg_data', Unlike the "click" option.
# When using the 'get' option you must use 'data' or 'arg_data', Unlike the "click" option, data=get_attribute("<src/herf/name/id>").
# 'arg_data' and 'arg_code' are 'variable name'.
# 'arg_data' and 'arg_code' are the variable name of the element to be inserted from the list. //Example: p1.run(<OPIRATION_TITLE>,password="123456789")
# 'data' and 'code' for entering data like password or username from json file (this is a common option if the variables you want to use are static).
# 'sleep' To wait for a certain period before starting an operation.

"""

#START{
from imbot import *

# Examples
# Example 1:
# Open the website link:
p1=imbot("github.json",headless=False)

# Login:
p1.run("login",passw='<YOUR_PASSWORD>')
# login==>OPIRATION_TITLE
# passw=<YOUR_PASSWORD> ==> "arg_data":"passw" 
# Bearing in mind that the name of the variable is 'passw'.

# To the profile page:
# p1.run("profile")
# profile==OPIRATION_TITLE

# To home page:
# p1.run("go2home")

# read the list of repositories:
Lines=open('github_list.txt','r').readlines()

# Strips the newline character
#for i in range(len(Lines)):
for i, Line in enumerate(Lines):
    repositorie=Line.strip()
    # To the repositorie:
    p1.run("go2repositorie",repo=repositorie)# repositorie=="arg_code":"repo" //Bearing in mind that the name of the variable is 'repo'
    # make operations:
    p1.run("hide_repositorie",repo=repositorie)# repositorie=="arg_data":"repo" //Bearing in mind that the name of the variable is 'repo'
    # To the home page:
    p1.run("go2home")

# end
p1.end()

# Example 2:
# Open the website link:
p2=imbot("google.json")#,headless=False

# Here, search for a movie poster in Google Images and get the link:
print(p2.run("search",search_for="yasserbdj96 on github"))
print(p2.run("search",search_for="luffy one piece"))

# end
p2.end()
#}END.