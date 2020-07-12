# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 20:03
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : read_config.py
from configparser import ConfigParser
# 作业
# 写一个配置类  有以下几个函数：
# 1：读取整数
# 2：读取浮点数
# 3：读取布尔值
# 4：读取其他类型的数据 list tuple dict eval()
# 5：读取字符串

class ReadConfig:

    def __init__(self, file_name):
        self.cf = ConfigParser()
        self.cf.read(file_name, encoding='utf-8')

    def get_int(self, section, option):
        '''从配置文件里面获取一个整数'''
        value = self.cf.getint(section, option)  # section  option
        return value

    def get_float(self, section, option):
        '''从配置文件里面获取一个浮点数'''
        value = self.cf.getfloat(section, option)  # section  option
        return value

    def get_bool(self, section, option):
        '''从配置文件里面获取一个布尔值'''
        value = self.cf.getboolean(section, option)  # section  option
        return value

    def get_str(self, section, option):
        '''从配置文件里面获取一个字符串'''
        value = self.cf.get(section, option)  # section  option
        return value

    def get_data(self, section, option):
        '''从配置文件里面获取一个元组 字典 列表等类型的数据'''
        value = self.cf.get(section, option)  # section  option
        return eval(value)

if __name__ == '__main__':
    # res = ReadConfig('case.conf').get_data('CASE', 'a')
    res = ReadConfig('case.conf').get_int('CASE', 'age')
    # print(type(res))
    print(res)