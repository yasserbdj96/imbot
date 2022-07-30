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

# docker build -t imbot:latest .
# docker run -e headless=<True/False>* -e json_data='<PATH/TO/JSON/FILE>*' -e opiration_title='<TITLE_OF_OPIRATION>*' -e argvs='<ARGV_DATA_ID>="<DATA_TO_INPUT>"' -i -t imbot:latest
# EX:
# docker run -e headless=True -e json_data="google.json" -e opiration_title="search" -e  argvs='search_for="yasserbdj96 on github"' -i -t imbot:latest
# *    = All inputs must be entered.

#START{
FROM python:3.10

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99

WORKDIR /wrdir

COPY ./run.py /wrdir
COPY ./imbot /wrdir/imbot
COPY ./requirements.txt /wrdir/requirements.txt

# Add the path of json file here:
# 'google.json' just an example.
# you can add more then one file.
COPY ./examples/google.json /wrdir

RUN pip install --upgrade --no-cache-dir -r ./requirements.txt
RUN rm ./requirements.txt # remove requirements file from container.

CMD ["python", "run.py"]
#}END.