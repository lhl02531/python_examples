# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""

class Robot:
    """robot 机器人类"""

    count = 0   # count, 类变量,使用Robot.count
    def __init__(self, name):
        # name 对象变量
        self.name = name
        Robot.count +=1


    def die(self):
        print('{0} is dieing'.format(self.name))
        Robot.count -= 1

        if(Robot.count == 0):
            print('{0} is the last one'.format(self.name))
        else:
            print('there are still {0} working'.format(Robot.count))

    def say_hi(self):
        print('hi, my mater, robot {0} is working'.format(self.name))

    @classmethod
    def how_many(cls):
        """ 类方法, 装饰器"""
        print('we have {:d} robots'.format(cls.count))


#   开始使用类
droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('R2-D2')
droid2.say_hi()
Robot.how_many()

droid2.die()
droid1.die()
Robot.how_many()