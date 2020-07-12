#!/usr/bin/python
# -*- coding: <utf-8> -*-
# _Author_ = 'shuai'
# Data：2020/1/4 10:24
from configparser import ConfigParser


# 作业
# 写一个配置类  有以下几个函数：
# 1：读取整数
# 2：读取浮点数
# 3：读取布尔值
# 4：读取其他类型的数据 list tuple dict eval()
# 5：读取字符串
class Read_Config:

    def __init__(self, file_name):
        self.cf = ConfigParser()
        self.cf.read(file_name, encoding='utf-8')

    def read_int(self, section, option):
        '''从配置文件里面获取一个整数'''
        value = self.cf.getint(section, option)
        return value

    def read_float(self, section, option):
        '''从配置文件里面获取一个浮点数'''
        value = self.cf.getfloat(section, option)
        return value

    def read_bool(self, section, option):
        '''从配置文件里面获取一个布尔值'''
        value = self.cf.getboolean(section, option)
        return value

    def read_str(self, section, option):
        '''从配置文件里面获取一个字符串'''
        value = self.cf.get(section, option)
        return value

    def read_data(self, section, option):
        '''从配置文件里面获取其他类型的数据 list tuple dict eval()'''
        value = self.cf.get(section, option)
        return eval(value)


if __name__ == '__main__':
    val1 = Read_Config('case.conf').read_int('CASE', 'age')
    print(val1)
