# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
import time
# https://blog.csdn.net/gogowhh/article/details/127546349
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
# chrome 会自动进行更新，我的情况是找不到对应的 driver 会闪退
# 我不知道是不是这个问题，所以我加了这个选项果然就不闪退了
# 可能是 driver 版本， 可以 selenium版本，如果不行就回退
option.add_experimental_option("detach",True)
# 去掉 chrome 上面的选项卡
option.add_experimental_option('excludeSwitches', ['enable-automation'])
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service, options=option)

driver.get('https://www.jd.com/')
input_elem = driver.find_element(by=By.ID, value="key")
input_elem.send_keys("篮球")
input_elem_1 = driver.find_element(by=By.CSS_SELECTOR, value="#key")
input_elem.send_keys("足球")

submit_button = driver.find_element(by=By.CLASS_NAME, value="button")
submit_button.click()


# hot_search = driver.find_element(by=By.CLASS_NAME, value="c-font-medium c-color-t opr-toplist1-subtitle_3FULy")
# hot_search.click()






