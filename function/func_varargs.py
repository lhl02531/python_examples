# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


def func_var(a=5, *numbers, **phonebooks):
    print('a', a)
    for i in numbers:
        print('numbers,', i)
    print('phonebooks')
    for k, v in phonebooks.items():
        print('k:', k, 'v:', v)

#  1,2,3 会形成元组，填入 number
# Jack=1123, John=2231, Inge=1560 会形成字典, 填入phonebooks
func_var(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)
