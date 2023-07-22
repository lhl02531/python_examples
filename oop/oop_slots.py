# -*- coding: utf-8 -*-
"""
    :author: allen lv
    slots, 用 tuple 限制允许绑定的属性
"""
class Student:
    __slots__ =  ['name', 'age']

s = Student()
s.name = 'lv'
s.age = 18
s.score = 88    # 报错
