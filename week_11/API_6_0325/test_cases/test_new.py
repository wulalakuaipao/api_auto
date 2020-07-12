# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 20:09
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : test_cases.py
import unittest
from ddt import ddt,data
from API_6.common.my_log import MyLog
from API_6.common.http_request import HttpRequest
from API_6.common.do_excel_new import DoExcel
from API_6.common import project_path

#测试充值
test_data=DoExcel(project_path.case_path,'recharge').read_data()#获取测试数据
my_log=MyLog()
COOKIES=None#设置cookies的初始值为None

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):#测试之前的准备工作
        pass

    def tearDown(self):
        pass

    #写用例
    @data(*test_data)
    # @unpack
    def test_cases(self,case):
        global TestResult#全局变量
        global COOKIES#声明是一个全局变量
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])
        self.t=DoExcel(project_path.case_path,case['sheet_name'])#写入测试结果的对象

        #发起测试
        my_log.info('-------正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'],case['CaseId'],case['Title']))
        my_log.info('测试数据是：{}'.format(case))
        resp=HttpRequest().http_request(method,url,param,cookies=COOKIES)#传参
        #实实在在的http请求发生之后才去加一个判断，判断是否产生了cookies
        if resp.cookies:#判断请求的cookies是否为空 不为空其实就是True
            COOKIES=resp.cookies#我们可以更新COOKIES这个全局变量的值
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

