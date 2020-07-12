# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 20:56
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : we_chat_1.0.py
from week_6.class_0218.we_chat import WeChat

class WeChat_1(WeChat):

    def send_red_bag(self,money,numbers=1,stat=1):#发红包
        '''money:是发送红包的总金额  范围是0.01-200
           numbers:红包的个数 1 1个  x 指定个数
           stat:状态 1 表示平分 2表示随机'''
        if 0.01<=money<=200:
            if numbers!=1:#发送多个
                if stat==1:
                    print('共计发送{}个红包，每个金额是{}'.format(numbers,money/numbers))
                else:#不均分 个数还是指定的 对不对
                    pass
            else:
                print('发送1个红包，金额是{}元'.format(money))
        else:
            print('金额必须在0.01-200之间')