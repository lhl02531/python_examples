# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
#  切片,
#  浅拷贝
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]

# 左闭右开
print(a[0:3])   # output [1,2,3]
print(a[:3])    # 等价于 a[0:3]

# 打印最后一个数
print(a[-1])        # [6]
print(a[-2:])       # [5,6]
print(a[-2:-1])     # [5]

# 倒转
print(a[::-1])


