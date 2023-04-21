# -*- coding: utf-8 -*-
"""
    :author: allen lv
    元组， list 遍历
"""
from collections.abc import Iterable

l1 = [1, 2, 3]
t1 = (1, 2, 3)
d = {
    1: 'a',
    2: 'b'
}
# list 遍历
for i in l1:
    print(i)
# 元组 遍历
for i in t1:
    print(i)

# list 遍历, enumerate()
for index, value in enumerate(l1):
    print('{}:{}'.format(index, value))

print(isinstance(l1, Iterable))
print(isinstance(t1, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(d, Iterable))
print(isinstance(1, Iterable))




