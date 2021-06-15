#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 22:43:46 2021

@author: bilalqureshi
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())


browser.get('https://addressify.com.au/')
browser.implicitly_wait(20)
browser.find_element_by_name("address").send_keys("19 martin pl, sydney")

listElements=browser.find_elements(By.XPATH,"//li[@class='ui-menu-item']//a")

print("Total Suggestions are", len(listElements))
for ele in listElements:
    print(ele.text)