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
l1 = [1, 2, 3, 4, 5]
# l2 = [i * i for i in l1]
# # 生成器
g1 = (i * i for i in l1)
# print(type(l1))
print(g1)
print(type(g1))
for i in g1:
    print(i)

def fib(max):
    n, a, b = 0, 0, 1

    while n < max:
        yield b
        a, b = b, a + b
        n += 1


for n in fib(6):
    print(n)


# 杨辉三角
# def triangles():
#     # https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128#0
#     L1 = [1]
#     L2 = [1,1]
#     while True:
#         yield L1
#         L1 = L2
#         L2 = [1] + [L2[i] + L2[i + 1] for i in range(len(L2) - 1)] + [1]







def triangles():
    L1 = [1]
    L2 = [1,1]
    while True:
        yield L1
        L1 = L2
        L2 = [1] + [ L1[i] + L1[i+1] for i in range(len(L1)-1)] +[1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
   
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')