#!/usr/bin/python
# -*- coding: <utf-8> -*-
#_Author_ = 'shuai'  
# Data：2020/2/10 17:03
# 导入wxpy
from wxpy import *
# 初始化机器人,扫码登录
bot = Bot()
# 搜索自己的好友列表'你想找的好友名称'
my_fridend =bot.friends().search("穿行")[0]

@bot.register(my_fridend)
def print_msg(msg):
    print()


embed()
