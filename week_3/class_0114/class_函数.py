# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 20:35
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_函数.py

#函数的定义
#编写函数
#函数的调用



#len type()  int() str() float()
#函数的语法：
# def 函数名(参数1,参数2,参数3):#如果有参数  那么你调用函数的时候必须要传对应个数的参数
#     #函数体 你的函数要实现什么功能 用代码去表示
#     #return 表达式（可写可不写 主要是根据你的需求 来制定）

#函数的调用：函数名()

# def send_msg(tel,msg='吃饱了没？'):#形参/位置参数
#     '''完成发送短信的功能
#     tel:收信息的人的手机号码
#     msg:想要发送的任何信息内容'''
#     print('发送给{}，信息是:{}'.format(tel,msg))#调用这个print函数？？？
#     return#当你调用这个函数的时候  会返回return后面的表达式的值
#
# #调用函数
# # send_msg('15096090550','流浪人同学吃饭了没有！')#实参
# send_msg('18688776767','今天长胖了没有?')
#定义函数的时候 有几个位置参数  调用函数的时候 就要传几个参 一个都不能少
#如果参数列表里面有默认参数  当你调用函数该默认值不传值的时候 就会取这个默认值
#定义函数的时候 位置参数在默认值参数之前

#*args, **kwargs
#*args 动态参数/不定长参数

# def add(*args):#arguments
#     print('args的参数类型是',args)
#     for item in args:
#         print('参数值：',item)
#
# a=[[1,2],[3,4,5]]
# # add(1,2,3,4,5)
# add(*a)#解包/脱外套
#求任意5个数之和
# def add(*args):#arguments
#     print('args的参数类型是',args)
#     sum=0
#     for item in args:
#         print('参数值：',item)
#         sum+=item
#     print('求和的值是：',sum)
#
# add(1,5,9,10,45)
# *args 动态参数/不定长参数   元组
# **kwargs  key word arguments关键字参数 键值对  字典

a = [1, 2, 3, 4, 5]    # 列表list
b = {'1': 12, '2': 3}  # 字典dict
c = (2,34,4,5)         # 元组tuple
d = {2,3,4,56,7}       # 集合set
print(type(a))
print(type(b))
print(type(c))
print(type(d))
# <class 'list'>
# <class 'dict'>
# <class 'tuple'>
# <class 'set'>
def call_person(**kwargs):
    print('kwargs的数据类型是:',type(kwargs))
    print('kwargs的数据类型是:',kwargs)
call_person(name='华华',msg='来吃老坛酸菜泡面啦！')
