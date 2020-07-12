# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 20:57
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 异常处理.py
# username=input('请输入用户名：')
# password=input('请输入密码：')
# if username=='admin' and password=='admin':
#     print('登录成功！')
# else:
#     print('用户名或密码不正确，登录失败！')

# print(a)

# a=10
# try:#监控语句
#     print(a)
# except Exception as e:#知道错/什么错/精确打击--确定错误类型
#     print('try里面的代码出错:{}'.format(e))
#
# #NameError(错误类型：属性值): name 'a' is not defined（错误信息）
# #异常处理的多种方式：try..except...
# #try:监控代码  except 处理方式
# file=open('log.txt','a+',encoding='utf-8')
# b=[1,2,3,4,5]
# try:
#     print(b[9])
# except IndexError as e:
#     print('try里面的代码出错:{}'.format(e))
#     file.write(str(e))
#     file.write('\n')
#     file.close()

# try...except..finally...
# try:
#     file=open('test.txt',encoding='utf-8')#r
#     file.write('我是Python14的老师华华')
# except Exception as e:
#     print('try里面的代码报错:{}'.format(e))
# finally:
#     file.close()
# print(file.closed)

# try...except..else(不常用）
# try:
#     a=10
#     b=5
#     print(a+b)
# except Exception as e:
#     print('try里面的代码报错:{}'.format(e))
# else:
#     c=10
#     d=15
#     print(c+d)
#     print('try下面的代码有正常执行！')

# def football_team(x,y,k,sex_1='f'):
#     '''组建女子足球队
#     x:最小年龄
#     y：最大的年龄
#     sex:指定组建队伍的性别
#     k:指定询问的次数'''
#     count=0#存储满足条件的人数
#     a=0#记录询问的次数
#     while True:
# #         try:
# #             age=int(input('请输入你的年龄：'))
# #         except Exception as e:
# #             print('错误是{}'.format(e))
# #         else:
# #             sex=input('请输入你的性别：')
# #             if x<=age<=y and sex==sex_1:
# #                 count+=1
# #             a+=1
# #             if a==k:
# #                 break
#     print('符合条件的总人数{}'.format(count))
#
# football_team(10,18,3,'m')

# with...as.. 上下文管理器
with open('log.txt') as file:
    res = file.read()
    print(res)
print(file.closed)
