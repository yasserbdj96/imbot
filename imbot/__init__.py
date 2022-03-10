#!/usr/bin/env python
# coding:utf-8
#code by:YasserBDJ96
#email:yasser.bdj96@gmail.com

#START{
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import json
from hexor import hexor
from asciitext import *

#start imbot class:
class imbot:
    #__init__
    def __init__(self,json_data,sleep_time=2,url=""):
        with open(json_data) as f:self.json_data=json.load(f)
        chrome_options=Options()
        chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=chrome_options)
        #
        if "url" in self.json_data:
            self.url=self.json_data['url']
        else:
            self.url=url

        self.driver.get(self.url)
        self.sleep_time=sleep_time
    #run:
    def run(self,goto,*argm):
        operations=self.json_data[goto]['operations']
        for i in range(len(operations)):
            try:
                #
                if "code" in operations[i]:
                    code=operations[i]['code']
                elif "arg_code" in operations[i]:
                        code=argm[int(operations[i]['arg_code'])]
                #
                types=operations[i]['type']
                exec(f"self.driver.find_element_by_{types}('{code}')")
                #
                if operations[i]['opt']=="click":
                    do="click()"
                    text=f"[✓] Clicking on element_by_{types} : '{code}'"
                #
                elif operations[i]['opt']=="put":
                    #
                    if "arg_data" in operations[i]:
                        data=argm[int(operations[i]['arg_data'])]
                    elif "data" in operations[i]:
                        data=operations[i]['data']
                    else:
                        data=input(hexor(True).c("Data is empty : ","#ff0000"))
                    do=f"send_keys('{data}')"
                    text=f"[✓] Putting data to element_by_{types} : '{code}'"
                #
                exec(f"self.driver.find_element_by_{types}('{code}').{do}")
                hexor().c(text,"#299c52")
                sleep(self.sleep_time)
            except:
                try:
                    #
                    if "code" in operations[i]:
                        code=operations[i]['code']
                    elif "arg_code" in operations[i]:
                        code=argm[int(operations[i]['arg_code'])]
                    #
                    types=operations[i]['type']
                    hexor().c(f"[✗] We couldn't find : element_by_{types}:'{code}'","#ff0000")
                    sleep(self.sleep_time)
                    del code
                except:
                    hexor().c("Erreur inconnue!.","#ff0000")
                    sleep(self.sleep_time)
    #end:
    def end(self):
        self.driver.close()
    
    #about:
    def about(self):
        font_url="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/fonts/ANSI_Shadow.txt"
        print(ascii.asciitext(font_url,"#imbot","#ff0000"))
        hexor().c("https://github.com/yasserbdj96","#299c52")
        print("")
#}END.