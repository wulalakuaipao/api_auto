# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 21:14
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_Python文件处理.py
#1：Python文件的处理
# 配置文件 txt html ---内置函数 open()
#open()函数的作用#打开或者是创建文件
#file:你要打开或者是创建的目标文件的文件名
#mode：打开的模式 只读 只写 读写 追加
#encoding：如果你要读取或者是写入的内容里面包含了中文  encoding=utf-8
file=open('test15.txt','a+',encoding='utf-8')#打开的文件对象 存在file这个变量里面
#模式：r 只读 r+读写
#w 只写  file存在的话清空在写  如果file不存在 新建一个再写
#w+ 读写
# a 追加 append 只写 file存在的话直接追加在后面  如果file不存在 新建一个再写
#a+ 追加读写 只写 file存在的话直接追加在后面  如果file不存在 新建一个再写

#读写数据
# res=file.read(5)#指定的读的元素个数 就读指定的 否则 读全部的
# for i in range(1,20):
#     res=file.readline()#读取一行
#     if i==3:
#         print(res)
# res=file.readlines()#返回值的结果是列表 然后每一行值为列表的一个元素
# print(res)

#读写操作
# file.write('lemonclass')#io.UnsupportedOperation: not writable
file.seek(1,0)#移动光标 按位去移动 一个汉字 占3个位 一个英文占一位
# 第一个参数 你要移动多少个偏移量 第二个参数 相对于谁去移动
#0 头部 1  当前位置  2 最末尾
res=file.read()
print("res:",res)

#因为a+ w+ 读取内容的时候 光标在最后面  所以读取不到任何内容
#移动光标 seek(3,0)