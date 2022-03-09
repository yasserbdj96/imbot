"""
Default json code:
{
    "url":"<WEBSITE_URL>",
    "<OPIRATION_TITLE>":{
        "operations":[
           {"type":"<xpath/link_text/id/name/tag_name>","code":"<ELEMENT_CODE>","arg_code":"[n]","opt":"<click/put>","arg_data":"[n]","data":"<YOUR_DATA>"}
        ]
    }
}
"""

from imbot import *

# Examples
# Open the website link:
p1=imbot("./home/runner/work/imbot/imbot/examples/github.json")

# Login:
p1.run("login",'<YOUR_PASSWORD>')
# login==OPIRATION_TITLE
# <YOUR_PASSWORD> == "arg_data":"0" //Bearing in mind that the order of the variable is 0

# To the profile page:
p1.run("profile")
# profile==OPIRATION_TITLE

# read the list of repositories:
Lines=open('list.txt','r').readlines()

# Strips the newline character
for i in range(len(Lines)):
    repositorie=Lines[i].strip()
    # To the repositorie:
    p1.run("go2repositorie",repositorie)# repositorie=="arg_code":"0" //Bearing in mind that the order of the variable is 0
    # make operations:
    p1.run("hide_repositorie",repositorie)# repositorie=="arg_data":"0" //Bearing in mind that the order of the variable is 0
    # To the home page:
    p1.run("go2home")

# end
p1.end()
