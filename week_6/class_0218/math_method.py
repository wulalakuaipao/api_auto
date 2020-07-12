# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 20:03
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_math.py

class MathMethod:
    '''这是一个数学类，里面包含了各种数学方法'''
    c=10

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):#对象函数
        '加法'
        return self.a+self.b+self.c

    @classmethod#类函数
    def sub(cls):
        return cls.c+10

    @staticmethod#静态函数
    def div():
        return 10

#测试代码
if __name__ == '__main__':
    #方法一
    t=MathMethod(4,5)#对象
    res=t.add()#对象调用方法
    res_3=t.div()
    print(res)

    #方法二：
    res_2=MathMethod(4,6).add()
    print(res_2)
