<h1>imbot</h1>

<p>imbot for making a bot to control any website.</p>

[![Python package](https://github.com/yasserbdj96/imbot/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/yasserbdj96/imbot/actions/workflows/python-app.yml) [![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/imbot/badge)](https://www.codefactor.io/repository/github/yasserbdj96/imbot)

<h2>Languages:</h2>
* python3

<h2>Supported Distributions:</h2>

| Distribution | Version Check     | Python Test Version | Supported | Status  | Everything works |
| :----------: | :---------------: | :-----------------: | :-------: | :----:  | :--------------: |
| Ubuntu       | 20.04.3           | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | Yes              |
| Windwos      | 11.6.4            | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | No               |
| MacOS        | 10.0.20348        | 3.6, 3.7, 3.8, 3.9  | Yes       | Working | No               |

<h2>Installation:</h2>

```
pip install imbot
```

<h2>Usage:</h2>

```python
from imbot import *

p1=imbot("<json_file>")

p1.run(<OPIRATION_TITLE>,n0,n1,n2....n)

p1.end()

"""
Default json code:
{
    "url":"<WEBSITE_URL>",
    "<OPIRATION_TITLE>":{
        "operations":[
           {"type":"<xpath/link_text/id/name/tag_name>","code":"<ELEMENT_CODE>","arg_code":"[n]","opt":"<click/put/get>","arg_data":"[n]","data":"<YOUR_DATA>","sleep":<Seconds>}
        ]
    }
}
"""

"""
Help:
# Types of finding elements : "type"=[id,name,xpath,link_text,partial_link_text,tag_name,class_name,css_selector]
# If you don't use the 'code' key, you must use the 'arg_code' key to enter data from your script.
# If you don't use the 'data' key, you must use the 'arg_data' key to enter data from your script.
# When using the 'put' option you must use 'data' or 'arg_data', Unlike the "click" option.
# When using the 'get' option you must use 'data' or 'arg_data', Unlike the "click" option, data=get_attribute("<src/herf/name/id>").
# 'arg_data' and 'arg_code' are numbers.
# 'arg_data' and 'arg_code' are the order of the element to be inserted from the list. //Example: p1.run(<OPIRATION_TITLE>,n0,n1,n2....n)
# 'data' and 'code' for entering data like password or username from json file (this is a common option if the variables you want to use are static).
# 'sleep' To wait for a certain period before starting an operation.

"""
```

<h2>Examples:</h2>

```python
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
```

<h2>Screenshot:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/imbot/main/screenshot/screenshot_1.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/imbot/main/screenshot/screenshot_1.png">
    </a>
</div>

<h2>Changelog History:</h2>

```
## 0.1.6 [29-05-2022]
 - Fix bugs.

## 0.1.5 [28-05-2022]
 - Add sleep.
 - Fix bugs.

## 0.1.3 [28-05-2022]
 - Add Return 'get_attribute' as a list.
 - Fix bugs.
 
## 0.1.2 [10-03-2022]
 - Fix bugs.

## 0.1.1 [10-03-2022]
 - Fix bugs.

## 0.1.0
- New build.

## 0.0.1
- First public release.
```

<h1></h1> 

<div align="center">
    <a href="http://yasserbdj96.github.io/">Go to this link to get more information</a>
    <br>
    <a href="https://github.com/yasserbdj96/imbot" align="center">
        <img align="center"  alt="" src="https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.imbot">
    </a>
</div>
