# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 21:08
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_suite.py

import unittest
import HTMLTestRunnerNew #生成一个非常漂亮的HTML模板的模块
from week_8.class_0304 import class_unittest_learn
# from week_8.class_0304.class_unittest_learn import * #具体到类名

#
# #添加用例
suite=unittest.TestSuite()#测试套件---收集/存储用例

#方法一：
# suite.addTest(class_unittest_learn.TestAdd(1,1,2,'test_001'))#测试用例的实例
# suite.addTest(TestAdd('test_002'))#测试用例的实例
# suite.addTest(TestAdd('test_003'))#测试用例的实例
# suite.addTest(TestAdd('test_004'))#测试用例的实例
# # suite.addTest(TestSub('test_two_negative'))#测试用例的实例
# # suite.addTest(TestSub('test_two_zero'))#测试用例的实例

#LOADER专门来加载用例 两种方式 ddt装饰的用例 只能用loader方式
loader=unittest.TestLoader()#
#方法二：通过测试类来进行添加--
suite.addTest(loader.loadTestsFromTestCase(class_unittest_learn.TestAdd))
# suite.addTest(loader.loadTestsFromTestCase(TestSub))

#方法三：通过测试模块来进行添加
# suite.addTest(loader.loadTestsFromModule(class_unittest_learn))


##执行用例 TestTextRunner---也有一些知识点
with open('test_0304.html','wb') as file:
    # runner=unittest.TextTestRunner(stream=file,verbosity=2)#老版本的
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='20200304测试报告_py14',
                                            description='2020年的第一场报告',
                                            tester='乌拉拉')
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