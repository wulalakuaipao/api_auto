# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 21:35
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_字典.py
#字典：dict {}

#1:空字典 查看数据的类型 type()
# d={}
# print(type(d))
#2:字典的数据格式： key：value形式的
#key:不可变数据类型-->  整数 浮点数 布尔值 元组 字符串
#value:任意数据类型都支持-->整数 浮点数 布尔值 元组 字符串 列表 字典
#key必须是唯一的 0 1 True False 引起注意
d={1:'666',
   1.01:"这是华华老师的视力",
   False:[1,2,3,4,5],
   (1,2,3):[6,7,8],
   "name":('juzi','钵钵鸡',"行进者",'和姑娘'),
   'name':'hello 你的大头鬼',
   '''name''':{'name':'oppa','address':'火星','age':18,'tel':'110'}}
print(d)
#3:字典是可变的数据类型，无序的---没有索引
#True 1  False 0
# print(d[False])
#4：取值 取值方式： 字典名[key] 根据key去取值
# print(d['class_14']['name'])

#可变的数据类型
# d['class_14']['name']='不想要昵称'
# print(d)
