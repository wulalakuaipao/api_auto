# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 21:04
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_内置函数.py
# Python内置函数
# 函数的其他参数类型
# str list tuple dict
# 字符串：不可变 元素是有序的 有索引 支持切片的操作
# 增删改查操作
s='hello World Hello Python'

# 查：根据索引/切片取值
# 改：不支持 TypeError: 'str' object does not support item assignment
# 删：不支持
# 增：不支持
# 内置函数：字符串.函数(参数列表)
print(s.format('发年终奖了没有？'))

# print(s.capitalize())
# print(s.count('l'))
# print(s.find('Hello'))#找到了 就返回遇到的第一个字母的索引 没有找到就返回-1
# print(s.join(['1','2','4','6']))
# print(s.lower())
# s.translate() s.maketrans() s.swapcase() ??用这连个函数去做一个题目
# s=s.replace('l','@',1)#替换的意思
s = 'hhhhhhhello World Hello Pythonhhhhhh'
# print(s.split('l',2))#切割函数 根据元素对字符串进行切割 返回的数据类型是列表
# 列表里面的元素都是字符串
# print(s.strip('h'))#去除字符串头或尾指定的元素
# print(s.swapcase())#调换大小写 大写变小写 小写变大写

# print(s.index('l'))
# s.index()
# s.islower()
# s.isupper()
# s.isdigit()
# s.isspace()
# 元组 列表 字典的内置函数+变量的位置
