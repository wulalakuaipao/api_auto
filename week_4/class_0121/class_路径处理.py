# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 21:07
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_路径处理.py
# 概念：相对路径 绝对路径
# 相对路径：参照物的变化 目标的变化
# 绝对路径:直接右键copy path
# file=open('../../py14.txt',encoding='utf-8')
# print(file.read())

# os 可以完成对路径的读取
import os

# 获取路径的3个函数
# path_1 = os.getcwd()  # 获取当前的工作目录
# path_2 = os.path.realpath(__file__)  # __file__ 表示当前文件
# path_3 = os.path.basename(__file__)  # 当前文件的文件名字
# print(path_1)
# print(path_2)
# print(path_3)
# 打印出来的
# E:\第九期\python自动化\课堂源码\API自动化-课堂源码\week_4\class_0121
# E:\第九期\python自动化\课堂源码\API自动化-课堂源码\week_4\class_0121\class_路径处理.py
# class_路径处理.py

# 切割路径的用法：
path_2 = os.path.realpath(__file__)  # 获取当前文件所在的绝对路径  还会包含文件名在内
print(os.path.split(os.path.split(os.path.split(path_2)[0])[0]))  # os.getcwd()

# 拼接路径
path_2 = os.path.realpath(__file__)  # 获取当前路径
print('path_2:', path_2)

path_4 = os.path.split(path_2)[0]  # 切割后获取返回元祖的索引尾0的值 就是头部
print('path_4:', path_4)
# os.path.join()
# path_5=os.path.join(path_4,'py14.txt')#地址的拼接
# print('path_5:',path_5)

# 加号也是拼接
path_5 = path_4 + '\\test14.txt'
print('path_5:', path_5)
file = open(path_5, encoding='utf-8')
print(file.read())
