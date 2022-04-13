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
print('取值')

# 打印a
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