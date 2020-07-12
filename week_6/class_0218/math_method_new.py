# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 20:15
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : math_method_new.py

#继承：只有类与对象有
#我要新写一个类  具有math_method里面的所有函数和属性值 除了div以外
#除此之外 新增一个函数 完成多个参数的相加并返回相加和
#继承：class 子类（父类）：
      #类体：属性和函数
from week_6.class_0218.math_method import MathMethod#具体到类名

class MathMethodNew(MathMethod):#继承
    '''这是一个数学类，里面包含了各种数学方法'''

    def __init__(self):#重写 override
        self.a=10
        self.b=11

    def add(self):#重写的特点：函数名一样（子类与父类） 重写之后以重写为准
        #重写的范围:参数  函数体  return
        #除了函数名以外 哪哪都可以进行修改
        return self.a+self.b+self.c

    @classmethod
    def sub(cls):
        return 99

    #拓展  父类里面没有 只有子类有的 就是拓展函数
    def add_args(self,*args):#*args 子类特有的方法的 只能在子类调用 父类无权限去进行调用
        sum=0
        for item in args:
            sum+=item
        return sum

if __name__ == '__main__':
    res=MathMethodNew().add()
    # res=MathMethodNew().add_args(1,2,3,4,5)
    print(res)
    print(MathMethodNew.sub())
#有精力的-->可以自行去拓展多继承/超继承