# -*- coding: utf-8 -*-
"""
    :author: allen lv
    多重继承
"""


# 动物分为哺乳类和鸟类
# 可以按照能飞能跑分类，分成能飞派和能跑派
class Animal(object):
    pass


# 哺乳类 和 鸟类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 能飞，能跑类
class Flyable(object):
    def flying(self):
        print('flying')


class Runnable(object):
    def running(self):
        print('running')


# Dog 类
class Dog(Mammal, Runnable):
    pass


# Parrot 类
class Parrot(Bird, Flyable):
    pass
