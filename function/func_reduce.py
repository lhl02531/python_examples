# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
from functools import reduce
from math import pow
l1 = [1, 2, 3, 4, 5]


def add(x, y):
    return x + y


res = reduce(add, l1)
print(res)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce( lambda x, y: x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    s1 = s.split('.')
    cal = lambda x, y: x * 10 + y
    # 整数
    dec = reduce(cal, map(char2num, s1[0]))
    fra = reduce(cal, map(char2num, s1[1])) * pow(10, -1 * len(s1[1]))
    return dec + fra

'ss'.strip()
print(str2float('123.456'))
