# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 20:09
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_cases.py
import unittest
from ddt import ddt,data
from API_6.common.my_log import MyLog
from API_6.common.http_request import HttpRequest
from API_6.common.do_excel import DoExcel
from API_6.common import project_path

#测试注册--传参
test_data=DoExcel(project_path.case_path,'register').read_data('RegisterCASE')#获取测试数据
my_log=MyLog()

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试之前的准备工作
        self.t=DoExcel(project_path.case_path,'register')#写入测试结果的对象

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    # @unpack
    def test_cases(self,case):
        global TestResult#全局变量
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])

        #发起测试
        my_log.info('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        my_log.info('测试数据是：{}'.format(case))
        resp=HttpRequest().http_request(method,url,param)
        try:
            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            TestResult='Pass'#请注意这里
        except AssertionError as e:
            TestResult = 'Failed'
            my_log.error('http请求测试用例出错了，错误是：{}'.format(e))
            raise e#处理完异常之后  不要留在家里 要抛出去！ raise e
        finally:
            self.t.write_back(case['CaseId']+1, 8, resp.text)#请注意这里
            self.t.write_back(case['CaseId']+1, 9, TestResult)

        my_log.info('实际结果：{}'.format(resp.json()))#http发送请求拿到的实际返回值

