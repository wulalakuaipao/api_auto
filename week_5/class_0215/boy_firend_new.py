# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 20:42
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : boy_firend.py

#男朋友类 身高 喜欢运动 技术性 有钱 帅 会Python 优秀 赚钱 有责任 会家务
#做饭

#初始化函数--魔方函数 魔法函数

class BoyFriend:

    def __init__(self,age,height,name):#类的属性参数化
        self.age=age
        self.height=height
        self.name=name

    #函数
    def sport(self,*args):#第一个参数是self 类里面函数的标志
        print(self.name+'喜欢运动:{}'.format(args))

    @classmethod#类函数
    def cook(cls):#cls 类名
        print('会做饭会下厨')

    def coding(self):
        print('会写代码')

    @staticmethod#静态函数---跟普通函数一样的
    def info():#要写在类里面  但是跟类里面其他的函数以及属性 无调用关系
        print('这个是个人信息')

# #创建一个实例/对象
# p=BoyFriend(22,180,'梅西')
# p.sport('乒乓球','羽毛球','足球')
