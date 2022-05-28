"""
Default json code:
{
    "url":"<WEBSITE_URL>",
    "<OPIRATION_TITLE>":{
        "operations":[
           {"type":"<xpath/link_text/id/name/tag_name>","code":"<ELEMENT_CODE>","arg_code":"[n]","opt":"<click/put/get>","arg_data":"[n]","data":"<YOUR_DATA>"}
        ]
    }
}

Help:
# Types of finding elements : "type"=[id,name,xpath,link_text,partial_link_text,tag_name,class_name,css_selector]
# If you don't use the 'code' key, you must use the 'arg_code' key to enter data from your script.
# If you don't use the 'data' key, you must use the 'arg_data' key to enter data from your script.
# When using the 'put' option you must use 'data' or 'arg_data', Unlike the "click" option.
# When using the 'get' option you must use 'data' or 'arg_data', Unlike the "click" option, data=get_attribute("<src/herf/name/id>").
# 'arg_data' and 'arg_code' are numbers.
# 'arg_data' and 'arg_code' are the order of the element to be inserted from the list. //Example: p1.run(<OPIRATION_TITLE>,n0,n1,n2....n)
# 'data' and 'code' for entering data like password or username from json file (this is a common option if the variables you want to use are static).

"""

from imbot import *

# Examples
# Example 1:
# Open the website link:
p1=imbot("github.json")

# about & logo:
p1.about()

# Login:
p1.run("login",'<YOUR_PASSWORD>')
# login==OPIRATION_TITLE
# <YOUR_PASSWORD> == "arg_data":"0" 
# Bearing in mind that the order of the variable is 0. Example: p1.run(<OPIRATION_TITLE>,n0,n1,n2....n)

# To the profile page:
# p1.run("profile")
# profile==OPIRATION_TITLE

# To home page:
# p1.run("go2home")

# read the list of repositories:
Lines=open('list.txt','r').readlines()

# Strips the newline character
#for i in range(len(Lines)):
for i, Line in enumerate(Lines):
    repositorie=Line.strip()
    # To the repositorie:
    p1.run("go2repositorie",repositorie)# repositorie=="arg_code":"0" //Bearing in mind that the order of the variable is 0
    # make operations:
    p1.run("hide_repositorie",repositorie)# repositorie=="arg_data":"0" //Bearing in mind that the order of the variable is 0
    # To the home page:
    p1.run("go2home")

# end
p1.end()

# Example 2:
# Open the website link:
p2=imbot("google.json")

# Here, search for a movie poster in Google Images and get the link:
print(p2.run("search","Game.Of.Thrones.Conquest.And.Rebellion.2017"))
print(p2.run("search","DEJA.VU.2018"))

# end
p2.end()
