# -*- coding: utf-8 -*-
"""
    :author: allen lv
    StringIO 写
"""
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

