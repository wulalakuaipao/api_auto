# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 20:54
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_条件语句.py
#简单的条件判断语句
#1:if 只有当if后面的条件满足的时候 才会执行if下面的代码
# sex=input('请输入你的性别：')
# if sex=='女':#只对一种情况做了处理  True
#     print('和华华老师一起shopping吧！')

#2:if...else... :当if后面的条件满足的时候 执行if的代码
# if后面的条件不满足，就会执行else下面的代码
#以下是满足班级之星的条件：
# task_score=100#分数
# absence=0#缺勤的次数
# task_score=int(input('请输入你的分数：'))
# absence=int(input('请输入你的缺勤次数：'))
# if task_score==100 and absence==0:
#     print('恭喜你，荣获班级之星的荣誉！')
# else:#else后面不能加条件！！！！
#     print('不好意思，你的分数是{},缺勤{}次，离班级之星还有一定的距离！加油！'
#           .format(task_score,absence))

##if 后面的条件 可以是 逻辑 比较 成员 True False 0 1
# s={}#空数据 0 False---False  #非空数据 1 True---True
# if s:#
#     print('我最喜欢花呗了！')
# else:
#     print('我最不喜欢花呗了！')

#3：if...elif..else
#if elif 后面都可以加条件
# name=input('请输入你对象的名字')
# height=int(input('请输入你对象的身高'))
# if name=='马云':
#     print('这样的对象挺好的')
# elif name!='马云':
#     if height==175:
#         print('这样的对象挺好的')
#     else:
#        print('没啥好说的')

#4:红绿灯
# color=input('请输入你看到的灯的颜色：')
# if color=='red':
#     print('请不要乱动！现在是红灯 有危险！')
# elif color=='yellow':
#     print('请耐心等候！现在是黄灯，不要闯黄灯！')
# elif color=='green':
#     print('请注意过往车辆，现在可以安全通行！')
# else:
#     print('这个颜色不对，你是否有色盲啊！')
#
# if最前面  elif 中间 else最后面
# score=int(input('请输入你的分数'))
# if 0<=score<=100:#
#     if score>90:
#         print('优秀！')
#     elif score>80:
#         print('良好')
#     elif score>=60:
#         print('及格')
# else:# 0<score<=100
#     print('分数不在正确的范围类')

d={'vampire':'123456','nancy':'666666'}
#相当于我们存在数据库里面的用户信息

# name=input('请输入你的用户名：')
# if name in d.keys():
#     pwd=input('请输入你的密码：')
#     if pwd == d[name]:#d[name]
#         print('登录成功')
#     else:
#         print('密码错误')
# else:
#     print('用户名错误')

import datetime
print(str(datetime.datetime(2019, 12, 18, 13, 46)))