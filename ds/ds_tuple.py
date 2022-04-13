# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
# tuple 不可变，尝试修改元组中的元素会报错

# tuple empty
empty_tuple = ()
# tuple 1个元素,记得逗号
t1 = (1,)

# TypeError: 'tuple' object does not support item assignment
# t1[0] = 2

list1 = [1, 2, 3]
print(type(list1))
print(type(tuple(list1)))
