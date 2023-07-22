# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


# 将 l1 每个元素都做一次平方操作
def f(x):
    return x * x


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = list(map(f, l1))
print(res)

# 将 l1 每个元素转化为字符
res1 = list(map(str, l1))
print(res1)


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    res = ''
    for i in range(len(name)):
        if(i==0):
            res += name[i].upper()
        else:
            res += name[i].lower()
    return res

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)