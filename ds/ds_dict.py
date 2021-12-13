# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
# dict, key-value
d = {1: 'a', 2: 'b', 3: 'c'}
# a
print(d.get(1))

# 判断key
# false
print(4 in d)
# none
print(d.get(4))

# for
for k, v in d.items():
    print("%d:%s" % (k, v))
for k in d.keys():
    print(k)