<div align="center">
  <h1>imbot</h1>
  <strong>imbot - create a bot to control any website.</strong>
</div>
<br>


[![Test on Ubuntu latest](https://github.com/yasserbdj96/imbot/actions/workflows/python-app-on-linux.yml/badge.svg)](https://github.com/yasserbdj96/imbot/actions/workflows/python-app-on-linux.yml)
[![pypi-setup](https://github.com/yasserbdj96/imbot/actions/workflows/pypi-setup.yml/badge.svg)](https://github.com/yasserbdj96/imbot/actions/workflows/pypi-setup.yml)
[![Docker image](https://github.com/yasserbdj96/imbot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/yasserbdj96/imbot/actions/workflows/docker-image.yml)
[![Github Container Registry](https://github.com/yasserbdj96/imbot/actions/workflows/gcr.yml/badge.svg)](https://github.com/yasserbdj96/imbot/actions/workflows/gcr.yml)
[![Upload to PYPI](https://github.com/yasserbdj96/imbot/actions/workflows/pipup.yml/badge.svg)](https://github.com/yasserbdj96/imbot/actions/workflows/pipup.yml)
[![Mirror and run GitLab CI](https://github.com/yasserbdj96/imbot/actions/workflows/push-gitLab.yml/badge.svg)](https://github.com/yasserbdj96/imbot/actions/workflows/push-gitLab.yml)
[![Deploy static content to Pages](https://github.com/yasserbdj96/imbot/actions/workflows/pages.yml/badge.svg)](https://github.com/yasserbdj96/imbot/actions/workflows/pages.yml)
[![CodeQL](https://github.com/yasserbdj96/imbot/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/yasserbdj96/imbot/actions/workflows/codeql-analysis.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/imbot/badge)](https://www.codefactor.io/repository/github/yasserbdj96/imbot)
[![Supported Versions](https://img.shields.io/pypi/pyversions/imbot.svg)](https://pypi.org/project/imbot) 
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.imbot&format=true)](https://github.com/yasserbdj96/imbot)
[![Docker pulls](https://img.shields.io/docker/pulls/yasserbdj96/imbot)](https://hub.docker.com/r/yasserbdj96/imbot/)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red)](https://github.com/yasserbdj96/imbot)
[![Stars](https://img.shields.io/github/stars/yasserbdj96/imbot?color=red)](https://github.com/yasserbdj96/imbot)
[![Forks](https://img.shields.io/github/forks/yasserbdj96/imbot?color=red)](https://github.com/yasserbdj96/imbot)
[![Watching](https://img.shields.io/github/watchers/yasserbdj96/imbot?label=Watchers&color=red&style=flat-square)](https://github.com/yasserbdj96/imbot)
![GitHub contributors](https://img.shields.io/github/contributors/yasserbdj96/imbot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/yasserbdj96/imbot)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/yasserbdj96/imbot)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/yasserbdj96/imbot)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/yasserbdj96/imbot)
![GitHub last commit](https://img.shields.io/github/last-commit/yasserbdj96/imbot)
[![GitHub license](https://img.shields.io/github/license/yasserbdj96/imbot)](https://github.com/yasserbdj96/imbot)
[![Join the chat at https://gitter.im/yasserbdj96/imbot](https://badges.gitter.im/yasserbdj96/imbot.svg)](https://gitter.im/yasserbdj96/imbot?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


<h2>Languages:</h2>
* python3

<h2>Requirements</h2>
[✓] hexor<br>
[✓] asciitext<br>
[✓] selenium


<h2>Docker pull,build & run:</h2>

```bash
# pull:
❯ docker pull yasserbdj96/imbot:latest

# build:
❯ docker build -t docker.io/yasserbdj96/imbot:latest .

# run:
❯ docker run -e headless=<True/False>* -e json_data='<PATH_TO_YOUR_JSON_FILE>*' -e opiration_title='<TITLE_OF_OPIRATION>*' -e argvs='<ARGV_DATA_ID>="<DATA_TO_INPUT>"' -i -t imbot:latest
# EX:
# docker run -e headless=True -e json_data="google.json" -e opiration_title="search" -e  argvs='search_for="yasserbdj96 on github"' -i -t imbot:latest
# *    = All inputs must be entered.
```

<h2>Github Packages pull,build & run:</h2>

```bash
# pull:
❯ docker pull ghcr.io/yasserbdj96/imbot:latest

# build:
❯ docker build -t ghcr.io/yasserbdj96/imbot:latest .

# run:
❯ docker run -e headless=<True/False>* -e json_data='<PATH_TO_YOUR_JSON_FILE>*' -e opiration_title='<TITLE_OF_OPIRATION>*' -e argvs='<ARGV_DATA_ID>="<DATA_TO_INPUT>"' -i -t ghcr.io/yasserbdj96/imbot:latest
# EX:
# docker run -e headless=True -e json_data="google.json" -e opiration_title="search" -e  argvs='search_for="yasserbdj96 on github"' -i -t ghcr.io/yasserbdj96/imbot:latest
# *    = All inputs must be entered.
```

<h2>Python Package Installation:</h2>

```
# Install from pypi:
❯ pip install imbot
# OR
❯ python -m pip install imbot

# Local install:
❯ git clone https://github.com/yasserbdj96/imbot.git
❯ cd imbot
❯ pip install -r requirements-pypi.txt
❯ sudo python setup.py install

# Uninstall:
❯ pip uninstall imbot
```

<h2>Run without installation:</h2>

```
❯ git clone https://github.com/yasserbdj96/imbot.git
❯ cd imbot
❯ pip install -r requirements.txt
❯ python run.py --headless <True/False> --json_data '<PATH_TO_YOUR_JSON_FILE>*' --opiration_title '<TITLE_OF_OPIRATION>*' --argvs '{"<ARGV_DATA_ID>":"<DATA_TO_INPUT>"}' --exec_path '<CHROMEDRIVER_PATH>'
# EX:
# python run.py --headless False --json_data './imbot-examples/google.json' --opiration_title 'search' --argvs '{"search_for":"yasserbdj96 github"}' --exec_path './chromedriver'
# *    = All inputs must be entered.

# Run with Makefile:
❯ make run headless=<True/False> json_data='<PATH_TO_YOUR_JSON_FILE>*' opiration_title='<TITLE_OF_OPIRATION>*' argvs='{"<ARGV_DATA_ID>":"<DATA_TO_INPUT>"}' exec_path='<CHROMEDRIVER_PATH>'
```

<h2>Usage:</h2>

```python
from imbot import *

p1=imbot(json_data="<PATH_TO_JSON_FILE>*",sleep_time=2,url="<URL_TO_JSON_FILE>*",headless=True,exec_path="<CHROMEDRIVER_PATH>")

p1.run(<OPIRATION_TITLE>*,<VARIABLE_NAME>)
# *    = All inputs must be entered.

p1.end()

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
```

<h2>Examples:</h2>

```python
from imbot import *

# Examples
# Example 1:
# Open the website link:
p1=imbot("google.json")#,headless=False

# Here, search for a movie poster in Google Images and get the link:
print(p1.run("search",search_for="yasserbdj96 on github"))
print(p1.run("search",search_for="luffy one piece"))

# end
p1.end()
```

<h2>Screenshot:</h2>

<div align="center">
    <a href="https://raw.githubusercontent.com/yasserbdj96/imbot/main/screenshot/screenshot.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/imbot/main/screenshot/screenshot.png">
    </a>
    <a href="https://raw.githubusercontent.com/yasserbdj96/imbot/main/screenshot/screenshot_1.png">
        <img alt="yasserbdj96" height="100" src="https://raw.githubusercontent.com/yasserbdj96/imbot/main/screenshot/screenshot_1.png">
    </a>
</div>

<br>
<h2>Changelog History:</h2>
<a href="https://raw.githubusercontent.com/yasserbdj96/imbot/main/CHANGELOG">Click to See changelog History</a>

<br>
<h2>Limitations:</h2>
# Types of finding elements : "element_by"=[id,name,xpath,link_text,partial_link_text,tag_name,class_name,css_selector]<br>
# If you don't use the 'code' key, you must use the 'element_arg' key to enter data from your script.<br>
# If you don't use the 'data' key, you must use the 'arg_data' key to enter data from your script.<br>
# When using the 'put' option you must use 'data' or 'arg_data', Unlike the "click" option.<br>
# When using the 'get' option you must use 'data' or 'arg_data', Unlike the "click" option, data=get_attribute("<src/herf/name/id>").<br>
# 'arg_data' and 'element_arg' are 'variable name'.<br>
# 'arg_data' and 'element_arg' are the variable name of the element to be inserted from the list. //Example: p1.run(<OPIRATION_TITLE>,password="123456789")<br>
# 'data' and 'element_code' for entering data like password or username from json file (this is a common option if the variables you want to use are static).<br>
# 'sleep' To wait for a certain period before starting an operation.

<br>
<h2>Development By:</h2>

Developer / Author: [yasserbdj96](https://github.com/yasserbdj96)

<br>
<h2>License:</h2>
<p>The content of this repository is bound by the following <a href="https://raw.githubusercontent.com/yasserbdj96/imbot/main/LICENSE">LICENSE</a>.</p>

<br>
<h2>Support:</h2>
<p>If you like `imbot` and want to see it improve furthur or want me to create intresting projects , You can buy me a coffee </p>
<div align="center">
    <a href="https://ko-fi.com/yasserbdj96">
        <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="imbot by yasserbdj96">
    </a><br>
    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9<br>
</div>

<br><br>

<p align="center">
  <samp>
    <a href="https://yasserbdj96.github.io/">website</a> .
    <a href="https://github.com/yasserbdj96">github</a> .
    <a href="https://gitlab.com/yasserbdj96">gitlab</a> .
    <a href="https://www.linkedin.com/in/yasserbdj96">linkedin</a> .
    <a href="https://twitter.com/yasserbdj96">twitter</a> .
    <a href="https://instagram.com/yasserbdj96">instagram</a> .
    <a href="https://www.facebook.com/yasserbdj96">facebook</a> .
    <a href="https://www.youtube.com/@yasserbdj96">youtube</a> .
    <a href="https://pypi.org/user/yasserbdj96">pypi</a> .
    <a href="https://hub.docker.com/u/yasserbdj96">docker</a> .
    <a href="https://t.me/yasserbdj96">telegram</a> .
    <a href="https://gitter.im/yasserbdj96/yasserbdj96">gitter</a> .
    <a href="mailto:yasser.bdj96@gmail.com">e-mail</a> .
    <a href="https://ko-fi.com/yasserbdj96">sponsor</a>
  </samp>
</p>
