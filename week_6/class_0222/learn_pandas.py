# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 21:20
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_pandas.py
#pandas numpy
#pip install pandas

import pandas as pd

df=pd.read_excel('python_14.xlsx')
print(df.index.values)
s=[]
# print(df.ix[[1,2],['a','b','c']].values)
for i in df.index.values:
    s.append(df.ix[i,['a']].to_dict())
print(s)