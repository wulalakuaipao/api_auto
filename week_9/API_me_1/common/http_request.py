#!/usr/bin/python
# -*- coding: <utf-8> -*-
#_Author_ = 'shuai'  
# Data：2019/12/28 10:10
import  requests

class HttpRequest:
    '''该类完成http的get以及post请求，并返回结果'''

    def http_request(self, method, url, param):
        '''根据请求方法来决定发起get请求还是post请求
        method: http的请求方式get post
        url:发送请求的接口地址
        param:随接口发送的请求参数 以字典格式传递
        rtype:有返回值，返回结果是响应报文'''
        # Python的upper()方法将字符串中的小写字母转为大写字母。
        if method.upper() == 'GET':
            try:
                resp = requests.get(url, params=param)
            except Exception as e:
                print('get请求出错了：{}'.format(e))#格式化输出,学开发才了解.
        elif method.upper() == 'POST':
            try:
                resp = requests.post(url, data=param)
            except Exception as e:
                print('post请求出错了：{}'.format(e))
        else:
            print('不支持该种方式')
            resp = None
        return resp
# 测试代码
if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'  # 接口地址
    param = {'mobilephone': '18813989999', 'pwd': '123456', 'regname': 'lemonhuahua'}  # 字典的形式存储参数数据
    method = 'get'
    resp = HttpRequest().http_request(method, url, param)
    print(resp.text)
    print(resp.headers)