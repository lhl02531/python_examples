# -*- coding: utf-8 -*-
"""
    :author: allen lv
    type()

"""
import types
# type()
class Person:
    pass


def fn():
    pass


p = Person()
p1 = Person()
a = 1
print(type(a))
# 判断基础类型
print('判断基础类型',type(a) == int)
# 判断函数
print('判断函数',type(fn) == types.FunctionType)
# 判断类
print('判断类',type(p) == type(p1))
