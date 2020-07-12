# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 20:52
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : run.py


import unittest
from API_6.ext import HTMLTestRunnerNew
from API_6.common import project_path
from API_6.test_cases import test_register#具体到模块
from API_6.test_cases import test_recharge#具体到模块

#新建一个测试集
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_register))
suite.addTest(loader.loadTestsFromModule(test_recharge))

#执行用例 生成测试报告
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='py14 0313测试报告',
                                            description='py14 0313测试报告',
                                            tester='霹雳无敌的oppa')
    runner.run(suite)#执行用例  传入suite suite里面是我们收集的测试用例
