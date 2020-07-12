# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 20:42
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : boy_firend.py

#男朋友类 身高 喜欢运动 技术性 有钱 帅 会Python 优秀 赚钱 有责任 会家务
#做饭

class BoyFriend:

    #属性
    sex='男'
    age=28
    height=180
    weght=150
    name='彭于晏'

    #函数
    def sport(self,*args):#第一个参数是self 类里面函数的标志
        print('类的函数里面打印self',self)
        print(self.name+'喜欢运动:{}'.format(args))
        self.coding()
        return 666

    @classmethod#类函数
    def cook(cls):#cls 类名
        cls().coding()
        print(cls.name+'会做饭会下厨')

    def coding(self):
        print('会写代码')

    @staticmethod#静态函数---跟普通函数一样的
    def info():#要写在类里面  但是跟类里面其他的函数以及属性 无调用关系
        print('这个是个人信息')

# #创建一个实例/对象
p=BoyFriend()
p.cook()


# p.info()
# BoyFriend.info()
# print('类外面打印对象p:',p)
#
# res=p.sport('爬山','爬树')
# print(res)

# t=BoyFriend()
# print('类外面打印对象t:',t)
#
# t.sport()
# print('我男朋友的名字是：{}'.format(p.name))
# p.cook()
# p.coding()

#除了self cls 以外  类里面的函数跟普通函数是一模一样的。

#类里面的函数 三种类型   对象函数  类函数  静态函数
#对象函数：这个函数只能被对象调用
#类函数：类函数可以被类以及对象调用 @classmethod修饰一个
#静态函数：静态的可以被类以及对象调用 @staticmethod修饰一个