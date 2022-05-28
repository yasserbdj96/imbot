# docker build -t imbot .
# docker run -i -t imbot
#
FROM ubuntu 
LABEL maintainer "Sean Pianka <pianka@eml.cc>"

## For chromedriver installation: curl/wget/libgconf/unzip
RUN apt-get update -y && apt-get install -y wget curl unzip libgconf-2-4
## For project usage: python3/python3-pip/chromium/xvfb
RUN apt-get update -y && apt-get install -y xvfb python3 python3-pip 


# install manually all the missing libraries
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Download, unzip, and install chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Create directory for project name (ensure it does not conflict with default debian /opt/ directories).
WORKDIR /wrdir

## Your python project dependencies
#RUN pip3 install selenium
## or install from dependencies.txt, comment above and uncomment below
#COPY requirements.txt .
#RUN pip3 install -r requirements.txt


## Copy over project/script (feel free to combine these if your project is a combination of both directories and top-level files)
### For projects which are modules
#COPY app/ .
## For projects which are single scripts
COPY ./examples /wrdir
COPY ./imbot /wrdir/imbot
COPY ./requirements.txt /wrdir/requirements.txt
COPY ./run.sh /wrdir/run.sh

RUN pip install --no-cache-dir --upgrade -r /wrdir/requirements.txt


# Set display port and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null


# Bash script to invoke xvfb, any preliminary commands, then invoke project
#CMD ["Xvfb",":99","-screen","0","640x480x8","-nolisten","tcp","&&","python3","examples.py"]
#COPY run.sh .
CMD /bin/bash run.sh

#












#FROM python:3.9

#WORKDIR /wrdir

#COPY ./examples /wrdir
#COPY ./imbot /wrdir/imbot
#COPY ./requirements.txt /wrdir/requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /wrdir/requirements.txt

#CMD ["python", "examples.py"]