# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 20:41
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_01.py
import os
# print('hello')
# import keyword
# print(keyword.kwlist)

# 缩进 tab
# if 1:
#  print(6666)
#  print(9000)
#
# print('Python大法好！')

# \n 换行符
# print('8888\n'
#       '9999\n'
#       '1111\n')

# 三个成对的单引号/双引号 可以保持内容的格式 进行输出
# print(""" python大法好！
#           信Python得永生！""")

# 单引号 双引号 三引号  成对的括起来的内容是字符串
'心晴'
"h"
'''华华'''
"""1"""

# 我想对华华说:'啊 Python真牛逼！'
# 单双引号互斥  用\转义 变成普通的字符 不是字符串的双引号或者单引号
# print("我想对华华说:\"啊 Python真牛逼！\"")


# 注释：代码就不会再运行
# 单行注释  快捷键 ctrl+/
# """ """  ''' ''' 成对的三个单引号或者三个双引号 可以注释多行
"""print(" python大法好！
          信Python得永生！")
print(88888)
print(66666)"""

# print()
# print(1,2,3,'hello')
# input()从控制台获取一个数据  数据类型都是str 字符串类型
print('年龄:',input('请输入年龄：'))


# 变量：给某个标识符赋值 才叫变量 必须要赋值 才有意义
# 赋值不需要指明类型  所见即所得的代码  type
a = 10
snow = 100.09
snow_1 = 0
_1 = 'hello'
print(type(snow_1))

# python常见的数据类型
# 数字：整数  浮点数
# 布尔值： boolean True False
# 字符串：str 成对 "" '' """""" ''' '''括起来的内容 才是字符串
# 元组 列表 字典 集合

#
# 浮点数： float 关键字 1整数: int 关键字 1 10.0 2.0 有小数点
int_a = 0  # 整数

sum = 0
a = 0
while a < 100:
    a = a + 1  # a=99的时候 那么a=a+1 就是100 那么就sum+=a  就是sum=sum+100  所以上面a<100就行 不是a<=100
    sum += a
print(sum)
