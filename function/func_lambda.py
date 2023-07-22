# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
import math


def c1(r):
    return math.pi * r * r


print(c1(3))
print(c1(5))

c2 = lambda r: math.pi * r * r
print(c2(3))
print(c2(5))

# 小测试
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017451447842528
# def is_odd(n):
#     return n % 2 == 1
is_odd = lambda n: n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
