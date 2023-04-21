# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""

class Person:
    def __init__(self, name):
        '''
         __init__方法会在类实例化对象时立即执行
        :param name:
        '''
        self.name = name;

    def sayHello(self):
        print('evening,{0}'.format(self.name))

p = Person('lv')
p.sayHello()