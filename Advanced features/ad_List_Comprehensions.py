# -*- coding: utf-8 -*-
"""
    :author: allen lv
    列表生成式
"""
import os

'''
    [1,2,3,4,5]
    [2,4,6,8,10]
'''
l1 = [1, 2, 3, 4, 5]
l1 = [i * 2 for i in l1]
print(l1)
print(type(l1))

dir = [d for d in os.listdir('D:\\')]
print(dir)

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776
# 廖雪峰练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i, str)]
print(L2)
