#!/usr/bin/python
# -*- coding: <utf-8> -*-
#_Author_ = 'shuai'  
# Data：2019/12/28 11:16
import os
#文件的路径放到这里
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#测试用例的路径
case_path=os.path.join(project_path,'test_cases','test_api.xlsx')
# print(case_path)