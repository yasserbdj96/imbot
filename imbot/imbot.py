#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com 
#s
"""
help:
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import json
from hexor import hexor

#start imbot class:
class imbot:
    #__init__
    def __init__(self,json_data,sleep_time=2):
        with open(json_data) as f:
            self.json_data=json.load(f)
        chrome_options=Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=chrome_options)
        self.driver.get(self.json_data['url'])
        self.sleep_time=sleep_time
    #run:
    def run(self,goto,*argm):
        self.operations=self.json_data[goto]['operations']
        for i in range(len(self.operations)):
            try:
                if "code" in self.operations[i]:
                    exec(f"self.driver.find_element_by_{self.operations[i]['type']}('{self.operations[i]['code']}')")
                    code=self.operations[i]['code']
                elif "arg_code" in self.operations[i]:
                    exec(f"self.driver.find_element_by_{self.operations[i]['type']}('{argm[int(self.operations[i]['arg_code'])]}')")
                    code=argm[int(self.operations[i]['arg_code'])]
                    print(code)
                if self.operations[i]['opt']=="click":
                    do="click()"
                    text=f"click on {code}"
                elif self.operations[i]['opt']=="put":
                    try:
                        data=self.operations[i]['data']
                    except:
                        try:
                            data=argm[int(self.operations[i]['arg_data'])]
                        except:
                            data=input(hexor(True).c("Empty field : ","#ff0000"))
                    do=f"send_keys('{data}')"
                    text=f"put data in {code}"
                hexor().c(text,"#299c52")
                exec(f"self.driver.find_element_by_{self.operations[i]['type']}('{code}').{do}")
                sleep(self.sleep_time)
            except:
                try:
                    hexor().c("We couldn't find : "+code,"#ff0000")
                    sleep(self.sleep_time)
                    del code
                except:
                    hexor().c("Erreur inconnue!.","#ff0000")
                    sleep(self.sleep_time)
    #end:
    def end(self):
        self.driver.close()
#e