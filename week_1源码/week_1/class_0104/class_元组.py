# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 20:55
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_元组.py
# 元组：tuple ()
# 1:空元组 查看数据的类型 type()
# t=()
# 2：当我们的元组里面的只有一个数据的时候 加一个逗号 保持元组的属性
# t=('hello',)
# 3:元组里面的数据可以是任意数据类型, 元素以逗号来进行分隔
# t=(1,0.03,True,'hello',(8,'lemon',99.9))
# 4:元组取值怎么取？方法同 字符串  表示元组是有索引的 从0开始数  也会有正序和倒序
# 元组取单个值 元组名[索引值]
# print(t[0])

# 5：支持切片 要取索引值为偶数的值  同字符串一样
# print(t[::2])

# 6：嵌套元组的取值 元组里面还有元组或者是其他数据类型
# t=(1,0.03,True,'hello',(8,'lemon',99.9))
# # print(t[-1][-2][-2])
# t[-1]='孙悟空'
# 7:元组是一个有序不可变数据类型  你一旦尝试去修改值的话
# 报错：TypeError: 'tuple' object does not support item assignment

# 特殊情况
t = (1, 0.03, True, 'hello', (8, 'lemon', 99.9), ['刘晴', '行者无疆'])
t[-1][0] = 'Python大法好！'
print(t)
