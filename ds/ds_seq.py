# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# 切片，第1位指起始位置，第二位指结束位置,[start, end)
# 第三位是step, 通常为1
# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 从某一字符串中切片 #
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# list  & string step
print('step test 1', name[::2])
print('step test 2', name[::2])