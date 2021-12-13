# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""

# python ds list

# empty list
empty_list = []

numbers = [1, 2, 3]

l1 = [1, '123']

print("numbers[0]:%d,numbers[1]:%d,numbers[2]:%d" % (numbers[0], numbers[1], numbers[2]))
print("numbers[0]:%d,numbers[-1]:%d,numbers[-2]:%d" % (numbers[0], numbers[-1], numbers[-2]))
# add
# 1,2,3,5
numbers.append(5)
for i in numbers:
    print(i, end='')
print()

# insert
# 1,2,3,4,5
numbers.insert(3, 4)
for i in numbers:
    print(i, end='')
print()

# pop
# 1,2,3,4
numbers.pop()
# 1,2,3
numbers.pop(3)
for i in numbers:
    print(i, end='')
print()




