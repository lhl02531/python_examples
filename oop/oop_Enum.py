# -*- coding: utf-8 -*-
"""
    :author: allen lv
    枚举类
"""
from enum import Enum


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


# The special attribute __members__ is a read-only ordered mapping of names to members.
# It includes all names defined in the enumeration, including the aliases:
for name, member in Weekday.__members__.items():
    print(name, member, member.value)


## 测试


class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')