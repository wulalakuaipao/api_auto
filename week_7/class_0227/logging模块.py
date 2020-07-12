# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 21:47
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : logging模块.py
import logging

# python里面自带的logging模块
# 什么是日志？
# 日志的作用是什么？
# 日志的等级？debug-info-warning-error-critical/fatal
# 日志收集器logger       默认日志收集器 root logger
# 日志输出渠道 handlers  控制台 console file txt test.log


# 1：定义一个日志收集器并且还要设置级别 getLogger
my_logger = logging.getLogger('python14')
my_logger.setLevel('DEBUG')

# 2:formatter 是可以自己去配置的
# 指定输出渠道还要设置级别 StreamHandler--控制台  FileHandler 输出指定文件
formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息]:%(message)s')
ch = logging.StreamHandler()
ch.setLevel('INFO')  # 设置级别
ch.setFormatter(formatter)  # 设置格式

fh = logging.FileHandler('test.log', encoding='utf-8')
fh.setLevel('INFO')  # 设置级别
fh.setFormatter(formatter)  # 设置格式

# 3:对接 最终输出的信息是取两者的交集
my_logger.addHandler(ch)
my_logger.addHandler(fh)

my_logger.debug('this is debug msg')
my_logger.info('我是Python14期的主讲老师：华华')
my_logger.warning('this is warning msg')
my_logger.error('我今天缺课了！')
my_logger.critical('this is critical msg')

my_logger.removeHandler(fh)  # fh ch
my_logger.removeHandler(ch)  # 一定要记得移除掉
