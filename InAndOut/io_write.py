# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
poem ="""
    早发白帝城
     唐 李白
朝辞白帝彩云间，千里江陵一日还。
两岸猿声啼不住，轻舟已过万重山。 
"""
f = open('poem.txt', 'w',encoding='utf-8')

f.write(poem)
f.close()

