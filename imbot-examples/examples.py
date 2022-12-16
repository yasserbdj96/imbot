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
           {"element_by":"<xpath/link_text/id/name/tag_name>","element_code":"<ELEMENT_CODE>","element_arg":"<VARIABLE_NAME>","opt":"<click/put/get>","arg_data":"<VARIABLE_NAME>","data":"<YOUR_DATA>","sleep":<Seconds>}
        ]
    }
}

Help:
# Types of finding elements : "element_by"=[id,name,xpath,link_text,partial_link_text,tag_name,class_name,css_selector]
# If you don't use the 'code' key, you must use the 'element_arg' key to enter data from your script.
# If you don't use the 'data' key, you must use the 'arg_data' key to enter data from your script.
# When using the 'put' option you must use 'data' or 'arg_data', Unlike the "click" option.
# When using the 'get' option you must use 'data' or 'arg_data', Unlike the "click" option, data=get_attribute("<src/herf/name/id>").
# 'arg_data' and 'element_arg' are 'variable name'.
# 'arg_data' and 'element_arg' are the variable name of the element to be inserted from the list. //Example: p1.run(<OPIRATION_TITLE>,password="123456789")
# 'data' and 'element_code' for entering data like password or username from json file (this is a common option if the variables you want to use are static).
# 'sleep' To wait for a certain period before starting an operation.

"""

#START{
from imbot import *

# Example 1:
# Open the website link:
p2=imbot("imbot-examples/google.json")#,headless=False

# Here, search for a github user in Google and get All his social media links:
print(p2.run("search",search_for="yasserbdj96 on github"))

# end
p2.end()
#}END.
