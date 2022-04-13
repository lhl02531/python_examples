# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


def func_var(a=5, *numbers, **phonebooks):
    print('a', a)
    for i in numbers:
        print('i,', i)
    for k, v in phonebooks.items():
        print('k:', k, 'v:', v)


func_var(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)

# 可变参数有些没搞懂
