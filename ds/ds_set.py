# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
s = set([1, 2, 3])
s.add(3)
s.add(4)

for i in s:
    print(i, end=',')
print('\n')

s.remove(4)
for i in s:
    print(i, end=',')

s1 = set([2, 3, 4])

print(s & s1)  # s & s1, result 2,3
print(s | s1)  # s | s1, result 1,2,3,4
