#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com 
#s
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import json

#start imbot class:
class imbot:
    #__init__
    def __init__(self,json_data,do,sleep_time=2):
        with open(json_data) as f:
            self.json_data=json.load(f)
        chrome_options=Options()
        chrome_options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome()
        self.driver.get(self.json_data[do]['url'])
        self.xpaths=self.json_data[do]['xpaths']
        self.sleep_time=sleep_time
    
    #do_click:
    def do_click(driver,xpath,sleep_time):
        print("clicking on : "+xpath)
        driver.find_element_by_xpath(xpath).click()
        sleep(sleep_time)
    
    #do_put:
    def do_put(driver,xpath,put,sleep_time):
        print("putting data to : "+xpath)
        driver.find_element_by_xpath(xpath).send_keys(put)
        sleep(sleep_time)
        
    #end:
    def end(self):
        self.driver.close()
    #run:
    def run(self):
        #print(self.json_data)
        for i in range(len(self.xpaths)):
            try:
                self.driver.find_element_by_xpath(self.xpaths[i]['xpath'])
                if self.xpaths[i]['opt']=="click":
                    imbot.do_click(self.driver,self.xpaths[i]['xpath'],self.sleep_time)
                elif self.xpaths[i]['opt']=="put":
                    try:
                        data=self.xpaths[i]['data']
                    except:
                        data=input("Empty field:")
                    imbot.do_put(self.driver,self.xpaths[i]['xpath'],data,self.sleep_time)
            except:
                print("We couldn't find : "+self.xpaths[i]['xpath'])
                
#e