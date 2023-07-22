# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""


# 只保留奇数
def is_odd(n):
    return n % 2 != 0


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 去掉序列中的空元素，包括 NULL, 空字符串，只包含空格字符
def not_empty(str):
    # 前者去掉 null, '', 后者去掉 '   '
    return str and str.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 回数
def is_palindrome(n):
    res = 0
    tmp = n
    while tmp != 0:
        last_digit = tmp % 10
        res = res * 10 + last_digit
        tmp = tmp // 10
    return res == n


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')