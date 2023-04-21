# -*- coding: utf-8 -*-
"""
    :author: allen lv
    生成器
"""
'''
生成器，generator
个人理解
如果长度过大的列表， 只需要使用前几项，那么这时候列表的空间就浪费
如果list 的每个项都可以通过某种运行得到，
python 的生成器， 一种一边循环一边计算的机制
生成器的语法跟列表生成式类似，只是把[]改成()
'''


#
# # 列表生成式
# l1 = [1, 2, 3, 4, 5]
# l2 = [i * i for i in l1]
# # 生成器
# g1 = (i * i for i in l1)
# print(type(l1))
# print(type(g1))
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for n in fib(6):
    print(n)
