# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
from types import MethodType
# 动态绑定属性和方法

class Student:
    pass


s1 = Student()
s1.name = 'lv'
print('name:', s1.name)
s2 = Student()
s2.name = 'wang'



def set_name(self, name):
    self.name = name

# 给实例绑定一个方法
s1.set_name = MethodType(set_name, s1)
s1.set_name('lv123')
print('name:', s1.name)

# s2.set_name('wang123'), set_name 是 s1的方法，不能应用 s2上
# 给类绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s1.set_score(100)
print('score:', s1.score)
s2.set_score(88)
print('score:', s2.score)
