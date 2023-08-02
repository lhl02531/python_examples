# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.baidu.com')

print(driver.title)