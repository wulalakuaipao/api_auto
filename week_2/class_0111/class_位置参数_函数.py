# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 21:13
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_位置参数_函数.py

def add(a, b):  # 形式参数/位置参数  这个表示 当你在调用函数的时候 要输入2个参数
    '这个是一个加法函数 完成两个数相加的功能'
    # a=1
    # b=2
    c = a + b  # 函数代码块 a+b的值存到c变量里面
    # return c#return不是必须的 但是每个函数 你不写的时候 也会默认给你加一个没有任何表达式的return


# 求任意两数之和
# print(add(1,2))#实参-->当你调用函数的时候 传递的参数
# # result=add(1,2)
# print(add(3,4))
# print(add(101,505)+10086)
# print('add函数执行结果是：',result)

add(1, 2, 3)
