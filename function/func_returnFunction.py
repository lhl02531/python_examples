# -*- coding: utf-8 -*-
"""
    :author: allen lv
    返回函数，同时也是闭包
"""


def lazy_sum(*args):
    def sum():
        res = 0
        for i in args:
            res += i
        return res

    return sum


f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1())
print(f2())
print(f2 == f1)  # 即便传入不同参数，也是不同的函数



# 闭包
def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

f = createCounter()
print(f())
print(f())