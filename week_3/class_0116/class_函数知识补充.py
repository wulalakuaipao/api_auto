# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 21:17
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_函数知识补充.py
# def talk_to_teacher(msg):
#     print('跟华华老师说：{}'.format(msg))
#
# def send_msg(tel,msg):
#     print('发送给：{}'.format(tel))
#     talk_to_teacher(msg)#函数的调用

# send_msg('15096097590','老师尽量讲到类与对象吧！')#


#变量的作用域：全局变量 局部变量
#函数内 局部变量
#函数外 全局变量
# msg='全局变量：Python14期的秀儿是跳坑王'#全局'

def send_msg():#参数 形式上的参数 占坑的参数 表示调用函数的时候 必须传递2个参数
    global msg#声明这个变量是全局变量
    msg='局部变量：华华是个挖坑王'#局部
    print('发送的信息是：{}'.format(msg))
    msg='局部变量：华华是个挖坑王，14期的秀儿是跳坑王'

def talk_to_teacher():
    print('跟老师交谈，交谈的内容是：{}'.format(msg))


send_msg()
talk_to_teacher()

# print(msg)


#1：函数内 局部变量,只作用在函数内， 函数外:全局变量
#2：当函数有局部变量就用局部的，否则就用全局的
#3：如果在函数内部声明某个变量是全局变量 global  当前模块内 可以调用这个变量
