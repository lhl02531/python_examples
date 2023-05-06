# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
import pickle

shoplistfile = 'shoplist.data'

shoplist  = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
# 转储对象至文件
pickle.dump(shoplist, f)

f.close()

f = open(shoplistfile, 'rb')
# 从文件中载入对象
storeList = pickle.load(f)

print(storeList)