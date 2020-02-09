# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:28:07 2020

@author: Administrator
"""

import numpy as np
import pandas as pd
frame1=pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))
print(frame1)
#   w  x   y   z
#a  0  1   2   3
#b  4  5   6   7
#c  8  9  10  11

print(frame1.columns[1])
#x

print(frame1.values[:,1])
#[1 5 9]

print(frame1.values[:2,1])
#[1 5]  the top 2 values of column 2
print('*****')

print(frame1[:2]['x'])
#a    1
#b    5
#Name: x, dtype: int32
print('*****')

d1={'name':['zhangsan','lisi'],'age':['22','32'],'tel':['10001','10086']}
df1=pd.DataFrame(d1)
print(df1)
#  age      name    tel     the key is column name
#0  22  zhangsan  10001
#1  32      lisi  10086