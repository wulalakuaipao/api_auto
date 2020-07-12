# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 20:06
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_unittest_learn.py
#什么是单元测试  unit 某个部分 某个模块 某个类 去进行测试
#为什么要做单元测试

#1）我们可以来测试我们自己的代码
# 2）我们可以利用单元测试来完成我们的自动化


#unittest pytest 测试单框架
import unittest

#测试用例===准备好 测试期望结果 expected   类：TestCase
#执行测试  类：TestSuite  类：TestTextRunner
#测试报告 类：TestTextRunner 执行/出具报告

#下节课
#一致 pass 不一致Failed<===测试结果<====实际结果与期望结果进行比对<====assert断言！！！！！

#开始对加法进行单元测试了
class TestAdd(unittest.TestCase):#继承
    def setUp(self):#开始-->在每一条用例执行之前
        print('----开始执行测试了---')#准备工作/准备测试环境

    def tearDown(self):#结束-->在每一条用例执行结束之后
        print('----测试执行完毕了----')#清场工作/清除测试环境

    #写用例 test_一定要用这个开头！！！！
    def test_001(self):#测试两个正数相加
        a=1
        b=2
        # expected=4
        c=a+b
        # try:
        #     self.assertEqual(expected,c)
        # except AssertionError as e:
        #     print('001用例执行失败，错误是{}'.format(e))
        #     raise e
        print('两个正数测试结果是:{}'.format(c))

    def test_002(self):#测试一正一负相加
        a=-1
        b=2
        expected=2
        c=a+b
        try:
            self.assertEqual(expected,c)
        except AssertionError as e:
            print('002用例执行失败，错误是{}'.format(e))
            raise e
        print('一正一负测试结果是:{}'.format(c))

    def test_003(self):#测试两个负数相加
        a=-1
        b=-2
        expected=-2
        c=a+b
        try:
            self.assertEqual(expected,c)
        except AssertionError as e:
            print('003用例执行失败，错误是{}'.format(e))
            raise e
        print('两个负数测试结果是:{}'.format(c))

    def test_004(self):#测试两个0相加
        a=0
        b=0
        expected=1
        c=a+b
        try:
            self.assertEqual(expected,c)
        except AssertionError as e:
            print('004用例执行失败，错误是{}'.format(e))#logger加进来了！
            raise e
        print('两个0测试结果是:{}'.format(c))



#开始对减法进行单元测试了
class TestSub(unittest.TestCase):#继承
    def setUp(self):#开始-->在每一条用例执行之前
        print('----开始执行测试了---')#准备工作/准备测试环境

    def tearDown(self):#结束-->在每一条用例执行结束之后
        print('----测试执行完毕了----')#清场工作/清除测试环境

    #写用例 test_一定要用这个开头！！！！
    def test_two_positive(self):#测试两个正数相减
        a=1
        b=2
        c=a-b
        print('两个正数测试结果是:{}'.format(c))

    def test_positive_negative(self):#测试一正一负相减
        a=-1
        b=2
        c=a-b
        print('一正一负测试结果是:{}'.format(c))

    def test_two_negative(self):#测试两个负数相减
        a=-1
        b=-2
        c=a-b
        print('两个负数测试结果是:{}'.format(c))

    def test_two_zero(self):#测试两个0相减
        a=0
        b=0
        c=a-b
        print('两个0测试结果是:{}'.format(c))


#用例执行的时候 按照ASCII编码执行的  所以要注意用例执行记得顺序
