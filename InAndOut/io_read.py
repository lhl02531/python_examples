# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
f = open('poem.txt', 'r', encoding='utf-8')

while True:
    line = f.readline()
    # 文件结束
    if len(line) == 0:
        break
    # readline 已经有换行符
    print(line, end='')

f.close()