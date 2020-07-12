# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 21:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : project_path.py
import os
#文件的路径 放到这里
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例的路径
case_path=os.path.join(project_path,'test_cases','test_api.xlsx')


#测试报告的路径
report_path=os.path.join(project_path,'test_result','test_report','test_report.html')
print(report_path)
#日志的路径
log_path=os.path.join(project_path,'test_result','test_log','test.log')

#配置文件的路径
conf_path=os.path.join(project_path,'conf','case.conf')

#第二种配置文件的路径
conf_path_new=os.path.join(project_path,'conf','case_new.conf')
