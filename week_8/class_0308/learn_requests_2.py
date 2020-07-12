# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 21:41
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_requests_2.py
import requests
# url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'#接口地址
url='http://test.lemonban.com/futureloan/mvc/api/member/login'#接口地址
param={'mobilephone':'18813989999','pwd':'123456'}#字典的形式存储参数数据
#头部
headers = {'user-agent': 'Mozilla/5.0'}#模拟从Firefox浏览器发送出去的
resp_1=requests.post(url,data=param,headers=headers)#返回一个消息实体
print(resp_1.text)#字符串类型
# print(resp.json())#字典类型
#响应结果：状态码 响应报文 响应头 cookies
print('状态码:',resp_1.status_code)
print('响应头:',resp_1.headers)
print('cookies是:',resp_1.cookies)
print('请求头:',resp_1.request.headers)

#充值：
# url='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'#接口地址
# param={'mobilephone':'18813989999','amount':'10000'}#字典的形式存储参数数
# resp=requests.post(url,data=param,cookies=resp_1.cookies)#返回一个消息实体
# print('充值结果:',resp.text)#字符串类型