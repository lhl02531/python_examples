# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service, options=option)

driver.get('https://www.jd.com/')
link_elem = driver.find_element(by=By.LINK_TEXT, value="家用电器")
link_elem.click()


handlers = driver.window_handles
for h in handlers:
    if h != driver.current_window_handle:
        driver.switch_to.window(h)
    print("当前句柄是:", driver.title)