# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 21:08
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_suite.py

import unittest
from week_7.class_0301.class_unittest_learn import *
#
# #添加用例
suite=unittest.TestSuite()#测试套件---收集/存储用例
suite.addTest(TestAdd('test_001'))#测试用例的实例
suite.addTest(TestAdd('test_002'))#测试用例的实例
suite.addTest(TestAdd('test_003'))#测试用例的实例
suite.addTest(TestAdd('test_004'))#测试用例的实例
suite.addTest(TestSub('test_two_negative'))#测试用例的实例
suite.addTest(TestSub('test_two_zero'))#测试用例的实例
#
#执行用例 TestTextRunner---也有一些知识点
with open('test.txt','w',encoding='utf-8') as file:
    runner=unittest.TextTestRunner(stream=file,verbosity=2)
    runner.run(suite)#执行测试套件里面的用例

#. 一条用例测试通过
#E 一条用例报错 error
#F 一条用例测试未通过 fail  期望！=实际


# file=open('test.log','w')
# try:
#     print(a)
# except Exception as e:
#     file.write(str(e))#strw w+ r+ a  a+   byte二进制  wb wb+ ab+ ab rb+
#     print('错误是：{}'.format(e))
#     raise e