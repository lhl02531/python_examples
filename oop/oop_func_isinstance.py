# -*- coding: utf-8 -*-
"""
    :author: allen lv
    isinstance() 判断对象是否属于该类型
"""


class Animal(object):
    pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


# object -> Animal -> Dog -> Husky
a = Animal()
d = Dog()
h = Husky()
# h 对象
print(isinstance(h, Husky))     # True
print(isinstance(h, Dog))     # True
print(isinstance(h, Animal))     # True
# d 对象
print(isinstance(d, Dog))     # True
print(isinstance(d, Animal))     # True
print(isinstance(d, Husky))     # True, Husky 是子类
