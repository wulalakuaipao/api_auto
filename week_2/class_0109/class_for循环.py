# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 20:49
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_for循环.py

#for循环是不会进入到死循环  自身就有限定次数
#for 循环  关键字for  一般用来遍历元素 或者是利用遍历元素的次数来控制循环
# s='12345'#8
#s=(1,2,3,[4,5,6],'hello')
# s=[1,2,3,[4,5,6],'hello']
# s={'name':'小雪','age':18}
# for y in s:#y 是一个变量  依次访问s这个字符串里面的元素并赋值给y
#     print('hello 我是for循环')
#     print(y)

#for循环遍历字典的时候  遍历的是key
#for循环 in 后面的数据必须是可迭代 元素是可数的： 字符串 列表 元组 字典

# num=0#记录符合条件的人数
# for i in '1111111111':
#     age=int(input('请输入你的年龄'))
#     sex=input('请输入你的性别：m表示男性，f表示女性')
#     if 10<=age<=12 and sex=='f':
#         print('恭喜你可以计入我们的足球队')
#         num+=1#只有进入到这个if条件语句下面 才是满足的
#     else:
#         print('很遗憾，你不能加入我们的足球队')
# print('符合条件的人数是{}'.format(num))

