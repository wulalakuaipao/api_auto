# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 21:07
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : get_data.py
from week_11.API_6_0327.API_6.common import project_path
from week_11.API_6_0327.API_6.common import read_config
import re
config = read_config.ReadConfig(project_path.conf_path)

class GetData:
    '''可以用来动态的更改 删除 获取数据'''
    COOKIE = None
    # LOAN_ID = None  # 新添加的标id初始值
    normal_user = config.get_str('data', 'normal_user')
    normal_pwd = config.get_str('data', 'normal_pwd')
    normal_member_id = config.get_str('data', 'normal_member_id')

def replace(target):
    p2 = '#(.*?)#'
    while re.search(p2, target):  # 查找参数的字符就matach object , True
        m = re.search(p2, target)  # 在目标字符串里面根据正则表达式来查找，有匹配的字符串就返回对象
        key = m.group(1)  # 传参就是只返回匹配的字符串，也就是当前组的匹配字符
        # print(key)
        value = getattr(GetData, key)  # 拿到我们需要去替换的值
        target = re.sub(p2, value, target, count=1)
    return target
# 类属性
# print(GetData.COOKIE)
# print(GetData().COOKIE)
# 类的反射可以动态的查看，增加，删除，更改类里面的属性
# 利用反射的方法来拿值
# print(getattr(GetData,'COOKIE'))#第一个参数是类名  第二个参数是属性的参数名
# print(hasattr(GetData,'COOKIE'))#第一个参数是类名  第二个参数是属性的参数名 返回值是布尔值
# print(setattr(GetData,'COOKIE','123456'))
# #第一个参数是类名  第二个参数是属性的参数名 第三个你要设置的新值
# print(getattr(GetData,'COOKIE'))
# print(delattr(GetData,'COOKIE'))#删除类的某个属性  #第一个参数是类名  第二个参数是属性的参数名
# #不常用
# print(getattr(GetData,'COOKIE'))
