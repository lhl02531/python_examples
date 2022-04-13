# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


def func_kw(a, b=3, c=1):
    print('a is', a, 'b is', b, 'c is', c)


func_kw(3, 7)
func_kw(2, c=5)
func_kw(c=50, a=100)
