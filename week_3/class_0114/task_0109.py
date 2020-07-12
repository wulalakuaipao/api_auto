# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 20:34
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_0109.py
# 1-14#格式化输出---居然不会？？？
# print('hello{},我要说{}，今天是{}'.format('yeah','今天晚上20:00开课','周一'))
# 答疑的事情--周天休息  过年期间也是休息的

# 作业讲解：持续30分钟（
# while里面已经有退出条件了，还来一个if什么break
# 如何防止while进入死循环 1）while后面的条件表达式不要是永真式  2）加变量 break
# 1.利用while循环 完成1-100的整数数字相加和
# 1)我是不是要想办法 拿到1 2 3 。。。。100这100个整数
# a=0#这个就是你的自己人
# sum=0#存储求和的变量
# while a<100:#永真式
#     a=a+1#1 2 3 4
#     sum+=a#是不是每次把a的值 加到sum变量里面去
#     print(a)#打印出a的值
#     # if a==100:#如果a=100 就不要继续循环 break
#     #     break
# print(sum)

# for 循环容易忘记是一个一个出来的，不是一块出来了
# 2.利用for循环 完成1-10的整数数字相加和
sum = 0  # 求和的变量
for item in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    # print(item)
    sum += item  # sum=sum+item
print(sum)

sum1 = 0  # 求和的变量
for item in range(1,11):
    # print(item)
    sum1 += item  # sum=sum+item
print(sum1)
