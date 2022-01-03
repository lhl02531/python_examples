# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""

#
x = 50


def func_global():
    global x
    print('global x is %d' % x)
    x = 30
    print('global x is %d' % x)


func_global()
print('global x is %d, out of function' % x)
