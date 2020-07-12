# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 21:16
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : http_request.py
# 2：编写一个类：你们自行去设计，要求写一个类， 初始化函数 对象函数
# 包含 根据你不同的选择完成get请求 OR post请求 ，
# 其中url 需要做参数化，并且最后要拿到响应结果
import  requests

class HttpRequest:
    def __init__(self,url,method='get'):
        self.url=url
        self.method=method

    def http_request(self):
        '''url:请求的url地址
           method:请求的方式 get post可以选择'''
        if self.method.lower()=='get':
            # print('正在发起get请求')
            try:
                resp=requests.get(self.url)
            except Exception as e:
                print('错误是{}'.format(e))
        else:
            # print('正在发起post请求')
            try:
                resp=requests.post(self.url)
            except Exception as e:
                print('错误是{}'.format(e))

        return resp.text#返回结果
if __name__ == '__main__':
    result=HttpRequest('http://www.lemfix.com').http_request()
    print(result)