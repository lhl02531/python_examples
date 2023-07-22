# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
with open('poem.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line.strip())
