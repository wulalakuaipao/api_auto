# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 21:09
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : lear_001.py
def printmsg(*args):
    print(args)
    print('args的长度：',len(args))
def mad(a):
    print(a)
# t=(1,2,3)
# printmsg(t)
printmsg(*[{'a':1,'b':2,'expected':3},{'a':3,'b':-2,'expected':1}])
mad({1,2})
mad([1,2,3])
mad((1,2,3))