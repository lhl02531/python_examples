# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


def func_local(x):
    print('x is now, %d' % x)
    x = 30
    print('x in function now, %d' % x)


x = 50
func_local(x)
print('x out of function, %d' % x)
