# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""

# python ds list

# empty list
empty_list = []
print(type(empty_list))
empty_list_1 = list()
print(type(empty_list_1))

numbers = [1, 2, 3]
# 打印元素
print("numbers[0]: %d,numbers[1]: %d,numbers[2]: %d" % (numbers[0], numbers[1], numbers[2]))
print("numbers[0]: %d,numbers[-1]: %d,numbers[-2]: %d" % (numbers[0], numbers[-1], numbers[-2]))
print('--------------------------------------')
print('--------------------------------------')
print('list append 方法')
# list方法
# append 添加元素
# 1,2,3,5
numbers.append(5)
for i in numbers:
    print(i, end='')
print()

# insert 插入元素
# 1,2,3,4,5

print('--------------------------------------')
print('--------------------------------------')
print('list insert 方法')
numbers.insert(3, 4)
for i in numbers:
    print(i, end='')
print()
# pop
# 1,2,3,4

print('--------------------------------------')
print('--------------------------------------')
print('list pop 方法')
numbers.pop()

for i in numbers:
    print(i, end='')
print()

print('--------------------------------------')
print('--------------------------------------')

