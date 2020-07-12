# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 20:13
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : phone.py

#微信 2019
#微信的功能：语音 信息  发红包 视频 群聊 朋友圈 小程序 收藏 支付 摇一摇 定位

#微信：第一版
#加好友  发信息

#写一个微信类
#了解类的语法 关键字 class
#class 类名:
   #类的说明
   #类体 属性-->变量 函数-->普通函数
#类名 标识符  驼峰命名  WeChat weChatFunction
class WeChat:
    '''这一个微信类'''
    #属性
    year='2011'#微信产生的年份
    company='腾讯'#所属公司
    PM='张小龙'#产品经理是谁

    #函数
    def add_friends(self):
        '''添加好友'''
        print('具有添加好友的功能')

    def send_msg(self):
        '''发送信息'''
        print('具有发送信息的功能')

#抽象的东西 具有继承的特性 复用性高
#调用：实例化--->类名()
t=WeChat()#对象/实例
print(t.PM)#调用属性
t.send_msg()#调用函数
