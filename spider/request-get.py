# -*- coding: utf-8 -*-
"""
    :author: allen lv
    requests
"""
import requests

url = 'http://localhost:5000/hello'
r1 = requests.get(url)
print('r1.status_code: %d, r1.text: %s' % (r1.status_code, r1.text))


r2 = requests.get(url + '/lv')
print('r2.status_code: %d, r2.text: %s' % (r2.status_code, r2.text))


r3 = requests.get(url + '/args/lv?id=123&&age=23')
print('r3.status_code: %d, r3.text: %s' % (r3.status_code, r3.text))

r4 = requests.get(url + '/args/lv', { 'id': 123, 'age': 23})
print('r4.status_code: %d, r4.text: %s' % (r4.status_code, r4.text))