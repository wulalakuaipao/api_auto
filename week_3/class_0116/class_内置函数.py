# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 20:38
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_内置函数.py

#元组 有序的不可变的数据类型
# t=('hello',2,3,4,1,2,1,1,1)
# print(t.count(1))
# print(t.index('h'))#返回你遇到的第一个元素的索引位置

# 列表 有序可变的数据类型
# L=['hello',2,3,4,1,2,1,1,6666]
#增:增加  insert
# L.append('路人')#对列表进行操作 增加一个元素到末尾---最常见最常用
#L.insert(2,'刘晴')#插入元素到列表的指定位置
#L.extend(['6666','秀儿','Python14'])#添加列表到L里面去  增加多个元素

# 删
# print(L.pop(0))#如果不指定索引 那么默认删除最后一个元素  否则删除指定索引位置的值
# print(L)
# L.clear()#清空列表

#改 赋值操作
# L[0]='华华'

# 查：切片/根据索引取值

#其他的内置函数
# L.reverse()
# L=[2,3,4,1,6666]
# L.sort(reverse=False)#针对数字类型的列表
# print(L.count(1))
# print(L.index(6666))

# 字典
d={1:'666',
   1.01:"这是华华老师的视力",
   False:[1,2,3,4,5],
   (1,2,3):[6,7,8],
   '''name''':{'name':'oppa','address':'火星','age':18,'tel':'110'}}
#增改 如果key存在的话 那么就是重新赋值  如果key不存在的 就是新增一个值
# d[1]=999
# d['class_name']='Python14期秀儿班'
# print(d)
# 删 pop
# print(d.pop('name'))
# print(d.popitem())
# print(d)
print(d.keys())#获取字典所有的key 这个数据类型也是可迭代  for循环支持
print(d.values())#获取字典所有的value 这个数据类型也是可迭代 for循环支持
#查：根据key来查询