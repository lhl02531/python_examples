# -*- coding: utf-8 -*-
"""
    :author: allen lv
    pandas 简单使用
"""
import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_excel('nba.xlsx')
print(df.to_string())
print('--------------------------')
print('输出一列或多列')
print(df['Name'])   # 输出单列
print(df[['Name', 'Team', 'Position']])     # 输出多列
print('--------------------------')
print('输出一行或多行')
print(df.iloc[0])   # 第一行
print(df.iloc[[0]])   # 第一行
print(df.iloc[[0,1,2]])     # 多行
print('type df.iloc[0]: ', type(df.iloc[0]))
print('type df.iloc[[0,1]]: ', type(df.iloc[[0,1]]) )
print('--------------------------')
print('输出一格或一个区域')
print(df['Name'][0])       # 一格
print(df[['Name', 'Team', 'Number']][0:16]) # 一个区域



