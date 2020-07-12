# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 10:33
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : read_me.py

# 2-18(周一）
# 1:类的继承
# 2：为何要写类？(复用性？可继承？）
# 3：requests模块的学习和使用
# 4：加法减法的类编写

# 2-20(周三)
# 1：http的response 这里继续讲完--ok
# 2：类与对象的作业讲解
# 3:调试debug 要加进来进行讲解

# 2-22（周五）
# 4：Excel的操作 安装openpyxl模块 然后进行操作
#:pandas的课程讲解

# 周一
# 配置文件
# logging模块

# 单元测试
# ddt

while 1:
    a = input('请输入你的数字')
    try:
        if a == '1':
            print('你出拳头')

        if a == '2':
            print('你出剪刀')

        if a == '3':
            print('你出布')
        break
    except:
        print('你出错了，请重新输入66666')
        continue