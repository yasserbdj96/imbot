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
    def __init__(self,json_data,sleep_time=2,url="",headless=True):
        imbot.about(self)
        with open(json_data) as f:
            self.json_data=json.load(f)
        chrome_options=Options()
        chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach",True)

        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        if headless==True:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver=webdriver.Chrome(options=chrome_options)
        #
        if "url" in self.json_data:
            self.url=self.json_data['url']
        else:
            self.url=url
        self.driver.get(self.url)
        self.sleep_time=sleep_time
    #run:
    def run(self,goto,**kwargs):
        operations=self.json_data[goto]['operations']
        #for i in range(len(operations)):
        get_list=[]
        for i, operation in enumerate(operations):
            try:
                #
                if "code" in operation:
                    code=operation['code']
                elif "arg_code" in operation:
                        #code=argm[int(operation['arg_code'])]
                        code=kwargs[operation['arg_code']]
                #
                types=operation['type']
                exec(f"self.driver.find_element('{types}','{code}')")
                #
                if operation['opt']=="click":
                    do="click()"
                    text=f"[✓] Clicking on element_by_{types} : '{code}'"
                    #
                    if "sleep" in operation:
                        sleep(operation['sleep'])
                    #
                    exec(f"self.driver.find_element('{types}','{code}').{do}")
                    hexor().c(text,"#299c52")
                    sleep(self.sleep_time)
                #
                elif operation['opt']=="put":
                    #
                    if "arg_data" in operation:
                        #data=argm[int(operation['arg_data'])]
                        data=kwargs[operation['arg_data']]
                    elif "data" in operation:
                        data=operation['data']
                    else:
                        data=input(hexor(True).c("Data is empty : ","#ff0000"))
                    #
                    if "sleep" in operation:
                        sleep(operation['sleep'])
                    #
                    do=f"send_keys('{data}')"
                    text=f"[✓] Putting data to element_by_{types} : '{code}'"
                    exec(f"self.driver.find_element('{types}','{code}').{do}")
                    hexor().c(text,"#299c52")
                    sleep(self.sleep_time)
                #
                elif operation['opt']=="get":
                    do=""
                    text=f"[✓] Get data from element_by_{types} : '{code}'"
                    #
                    if "arg_data" in operation:
                        #data=argm[int(operation['arg_data'])]
                        data=kwargs[operation['arg_data']]
                    elif "data" in operation:
                        data=operation['data']
                    else:
                        data=input(hexor(True).c("Data is empty : ","#ff0000"))
                    #
                    if "sleep" in operation:
                        sleep(operation['sleep'])
                    #
                    xxx=f"self.driver.find_element('{types}','{code}').get_attribute('{data}')"
                    hexor().c(text,"#299c52")
                    get_list.append(eval(xxx))
                    sleep(self.sleep_time)
            #
            except Exception as e:
                try:
                    #print(e)
                    #
                    if "code" in operation:
                        code=operation['code']
                    elif "arg_code" in operation:
                        #code=argm[int(operation['arg_code'])]
                        code=kwargs[operation['arg_code']]
                    #
                    types=operation['type']
                    hexor().c(f"[✗] We couldn't find : element_by_{types}:'{code}'","#ff0000")
                    sleep(self.sleep_time)
                    del code
                except Exception as e:
                    hexor().c("Erreur inconnue!.","#ff0000")
                    sleep(self.sleep_time)
                finally:
                    pass
            finally:
                pass
        return get_list
    #end:
    def end(self):
        self.driver.close()
    
    #about:
    def about(self):
        font_url="https://raw.githubusercontent.com/yasserbdj96/asciitext/main/fonts/ANSI_Shadow.txt"
        print(ascii.asciitext(font_url,"#imbot","#ff0000"))
        print(hexor(True,"hex").c((" "*24)+"Code by -> ","#fbbc05")+hexor(True,"hex").c("yasserbdj96","#34a853"))
        print(hexor(True,"hex").c((" "*24)+"V0.1.7","#ff0000"))
        print("")
#}END.
