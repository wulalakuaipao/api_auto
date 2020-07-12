# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 20:48
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_requests.py
import requests
url='http://47.107.168.87:8080/futureloan/mvc/api/member/register'#接口地址
param={'mobilephone':'18813989999','pwd':'123456','regname':'lemonhuahua'}#字典的形式存储参数数据
# =====注册请求======
# 发送一个get请求 用params
resp=requests.get(url,params=param)#返回一个消息实体
print(resp.text)#字符串类型
print(resp.json())#字典类型
print(type(resp.text))#字符串类型
print(type(resp.json()))#字典类型  当你返回的数据是一个json字符串的时候 才可以用这个方法

#发送一个post请求 用data
resp=requests.post(url,data=param)#返回一个消息实体
print(resp.text)#字符串类型
print(resp.json())#字典类型
print(type(resp.text))#字符串类型
print(type(resp.json()))#字典类型

#字符串--->字典  json.loads() key:value 都必须是双引号 null--》None
#python字典--->json格式的字符串  json.dumps()

#======登录请求=====
# url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'#接口地址
# param={'mobilephone':'18813989999','pwd':'123456'}#字典的形式存储参数数据

# url='http://www.lemfix.com'
#发送一个get请求
# resp=requests.get(url)#返回一个消息实体,params=param
# print(resp.text)#字符串类型
# print(resp.json())#字典类型

#发送一个post请求
# resp=requests.post(url,data=param)#返回一个消息实体
# print(resp.text)#字符串类型
# print(resp.json())#字典类型


#{"status":1,"code":"10001","data":null,"msg":"登录成功"}  text
# {'data': None, 'status': 1, 'msg': '登录成功', 'code': '10001'} json

import json
# s="{'status':1,'code':'10001','data':null,'msg':'登录成功'}"#错误的示范！！！
# s='{"status":1,"code":"10001","data":null,"msg":"登录成功"}'#正确的示范
# value=json.loads(s)
# print(value)

# value=json.dumps({'data': None, 'status': 1, 'msg': '登录成功', 'code': '10001'},ensure_ascii=False)
# print(value)

#字符串--->字典  json.loads() key:value 都必须是双引号 null--》None
#python字典--->json格式的字符串  json.dumps()