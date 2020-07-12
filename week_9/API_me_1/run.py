#!/usr/bin/python
# -*- coding: <utf-8> -*-
#_Author_ = 'shuai'  
# Data：2019/12/27 18:59
from week_9.API_me_1.common.do_excel import DoExcel
from week_9.API_me_1.common.http_request import HttpRequest
from week_9.API_me_1.common import project_path
# 完成用例的测试
# 1:读取到测试数据
test_data = DoExcel(project_path.case_path, 'test_cases').read_data()
# 2:执行测试:遍历--根据Key取值
for case in test_data:
    method = case['Method']
    url = case['Url']
    param = eval(case['Params'])
    # 发起测试
    print('---正在测试{}模块里面第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
    resp = HttpRequest().http_request(method, url, param)
    print('实际结果：{}'.format(resp.json()))  # http发送请求拿到的实际返回值
    # 对比结果
    if resp.json() == eval(case['ExpectedResult']):
        TestResult = 'Pass'
    else:
        TestResult = 'Failed'
    print('该条用例测试结论：{}'.format(TestResult))
    # 需要写回什么？实际结果/测试结论
    t = DoExcel(project_path.case_path, 'test_cases')
    t.write_back(case['CaseId'] + 1, 8, resp.text)
    t.write_back(case['CaseId'] + 1, 9, TestResult)