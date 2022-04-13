# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
# 次方，3^3
print('3的3次方  = {}'.format(3 ** 3))


# 整除，向下取整
print('13 // 4  = {}'.format(13 // 4))

# << 向左移动位数，2 移动两位就是 2*2*2  = 8
print('2 << 2 = {}'.format(2 << 2))

# >> 向右移动位数，11= 1011 移动1位就是 101=1+4=5
print('11 >> 1 = {}'.format(11 >> 1))

'''
    python 判断用到与或非跟其他语言不一样
    not 是布尔非
    and 是布尔与
    or  是布尔或    
    True, False 跟其他语言也不一样
'''

if not False:
    print('测试布尔非')
if False and True:
    print('测试布尔与')
else:
    print('测试布尔与')
if True or False:
    print('测试布尔或')
