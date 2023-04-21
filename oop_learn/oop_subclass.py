# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""

class  SchoolMember:
    """父类， 学校成员类"""
    def  __init__(self, name, age):
        self.name = name
        self.age = age
        print('init SchoolMember: {}'.format(self.name), end='  ')

    def tell(self):
        print('name:{}, age: {}'.format(self.name, self.age))


class Teacher(SchoolMember):
    """老师类"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('init teacher:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary:{:d}'.format(self.salary))


class Student(SchoolMember):
    """学生类"""
    def __init__(self, name, age, id):
        SchoolMember.__init__( self, name, age)
        self.id = id
        print('init student:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('id: {}'.format(self.id))


t = Teacher('teacher AAAAAA', 38, 6000)
s = Student('student BBBBBB',12, 'student')

members = [t, s]
for member in members:
    member.tell()