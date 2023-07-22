# -*- coding: utf-8 -*-
"""
    :author: allen lv
    StringIO 读
"""
from io import StringIO
f1 = StringIO('Hello!\nHi\nGoodbye!\n')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())
