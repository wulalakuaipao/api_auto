# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 21:32
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_函数_2.py

def robot(name,msg):#形参
    print('hello，{}，{}！'.format(name,msg))#函数的作用是向melody问好
    #隐式的给你添加一个没有任何表达式的 return
    return 'python14'

#当你调用函数的时候 才会生效
robot('华华','你好弱呀！今天上课效果不好！是不是因为大家太累了！')
robot('钵钵鸡','今天没有跳坑，表现不错')
robot('yoyo','注意预习我，问的问题太简单了！看看是哪里出现问题了！')
robot('刘晴','今天问的问题很高端哟')
robot('特立独行的鱼','今天的装扮很酷炫哟！')

sum=0
for i in range(0,7777778):
    if i%2!=0:
        sum+=1
print('奇数个数是',sum)