# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


def print_max(a, b):
    if (a > b):
        print(a)
    elif (b > a):
        print(b)
    else:
        print("%d, %d" % (a, b))


print_max(3, 5)
print_max(5, 3)
print_max(5, 5)

x = 4
y = 6
print_max(x, y)
