# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
# empty dict
emptyDict = {}
#
# dict, key-value
d = {1: 'a', 2: 'b', 3: 'c'}
print('--------------------------------------')
print('赋值')
# 赋值
d[3] = 'd'

print(d)
print('--------------------------------------')
print('取值')


# [] 获取key不存在，则直接报错, d[4]
# get 获取key不存在，则返回默认值
print(d[1])
print(d.get(1))

# 判断key
# False
print('--------------------------------------')
print('判断')
print(4 in d)
print(1 in d)
# None
print(d.get(4))

# for
for k, v in d.items():
    print("%d:%s" % (k, v))
for k in d.keys():
    print(k)


for k in d.values():
    print(k)

print(type(d.values()))