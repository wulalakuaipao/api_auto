# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 21:12
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : http_request.py

#requests模块
#pip install requests

#requests 完成http请求 get post
#一级宝典  基础使用  二级宝典 保你http请求 平安无事
import requests

#get请求
res=requests.get('http://www.lemfix.com/topics/179')#消息实体 以及状态码
print(res.text)#获取响应结果

#post请求
# res_2=requests.post('http://www.baidu.com')
# print(res_2)


#编写一个类： 初始化函数  对象函数  你们自行去设计 要求写一个类 根据你不同的选择完成get请求 OR post请求
#url 需要做参数化  要拿到响应结果

class HttpRequest:
    def __init__(self,url):
        self.url=url

    def get(self):
        pass

    def post(self):
        pass
