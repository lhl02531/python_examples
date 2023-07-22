# -*- coding: utf-8 -*-
"""
    :author: allen lv
    类的私有属性
"""
class Student():

    def __init__(self, name, score):
        # 私有变量， 以__开头
        self.__name = name
        self.__score = score

    def print(self):
        print('student name: {}, score:{}'.format(self.__name, self.__score))

    # 私有属性的读或写
    def set__name(self, name):
        self.__name = name

    def set__score(self, score):
        self.__score = score

    def get__name(self):
        return self.__name

    def get__score(self):
        return self.__score

s1 = Student('lv', 95)
s1.print()
s2 = Student('wang', 96)
s2.print()
# 直接读私有属性会报错
# print(s1.__name)
# print(s1.__score)

print(s1.get__name())
print(s2.get__name())
s1.set__name('lv123')
s2.set__name('wang123')
print(s1.get__name())
print(s2.get__name())
