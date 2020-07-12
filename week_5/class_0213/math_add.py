# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 20:07
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : add.py
#只考虑整数的相加
def add(a,b):
    '''完成a+b的操作并且返回a+b的值'''
    return a+b

def add_2(*args):
    sum=0
    for item in args:
        sum+=item
    return sum

def add_five_positive_numbers(a,b,c,d,e):
    print(a+b+c+d+e)

#测试代码可以这样做
# print(add_2(1,2,3,4,5))
if __name__ == '__main__':#程序执行的入口，只有当你运行当前py文件的时候  main下面的代码才会执行
     print(add_2(1,2,3,4,5))