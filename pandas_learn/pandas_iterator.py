# -*- coding: utf-8 -*-
"""
    :author: allen lv
    pandas 遍历
"""
import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_excel('nba.xlsx')

for i in df.index:
    for j in df.iloc[[i]]:
        print(df[j][i])
