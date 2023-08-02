# -*- coding: utf-8 -*-
"""
    :author: allen lv
    pandas 数据筛选
"""

import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_excel('nba.xlsx')

# 数据进行筛选
# Salary > 1500000
players = df[ df['Salary'] > 1500000 ]
print(players)