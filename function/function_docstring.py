# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


def maximum(x, y):
    """

    :param x:
    :param y:
    :return: 两数较大值，相等返回none
    """
    if x > y:
        return x
    elif x == y:
        print('x ==y')
    else:
        return y


print(maximum(23, 42))
print(maximum(42, 23))
print(maximum(42, 42))
print(maximum.__doc__)
