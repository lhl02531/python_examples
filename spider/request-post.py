# -*- coding: utf-8 -*-
"""
    :author: allen lv
    request post
"""
import requests

url = 'http://localhost:5000/'

r1 = requests.post(url + 'form')
print('r1.status_code: %d, r1.text: %s' % (r1.status_code, r1.text))

rdata = { "username": "lv", "password": "aa13520."}
# 表单
r2 = requests.post(url + 'form2', data=rdata)
print('r2.status_code: %d, r2.text: %s' % (r2.status_code, r2.text))

# json
r3 = requests.post(url + 'form4', json=rdata)
print('r3.status_code: %d, r3.text: %s' % (r3.status_code, r3.text))