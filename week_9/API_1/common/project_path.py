# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 21:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : project_path.py
import os

# 文件的路径 放到这里
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试用例的路径
case_path = os.path.join(project_path, 'test_cases', 'test_api.xlsx')
# print(case_path)
