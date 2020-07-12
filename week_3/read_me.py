# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 13:46
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : read_me.py
#1-16
#循环的作业讲解：end的作用？print是默认后面有一个换行符
#函数的作业讲解

#1-18号 不上课-周五=--领奖

#1-21
#os路径操作
#1：Python文件的处理
#2:异常处理
#3：调试方法和技巧

#1-23
#1：类与对象
#2:类的不同类型的函数：类方法 静态方法 对象方法 初始化函数等
#3:类的继承

#1-24号开始放假（请各位根据老师留下的预习视频，做好预习）

for i in [1,2,3,4,5]:
    print('*'*i,end='')#
    print()

for i in range(1,6):
    print('*'*i,end='')
    print()
for j in [4,3,2,1,0]:
    print(' '*(j),end='')
    print(' * '*(5-j),end='')
    print()

# for i in [1,2,3,4,5]:
#     print('* '*i,end='')
#     print()

# @@@@*
# @@@* *
# @@* * *
# @* * * *
# * * * * *