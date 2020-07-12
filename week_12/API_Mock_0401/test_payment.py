# -*- coding:utf-8 _*-
# @author:mongo
# @time: 2018/12/17
# @email:3126972006@qq.com
# @function：
# 支付测试类：
# 1.正确的用户信息，支付成功
# 2，正确用户信息，支付失败
# 3，超时，超时再成功
# 4，超时，超时再失败
import unittest
from unittest import mock

from week_12.API_Mock_0401 import payment


class PaymentTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_pay_success(self):
        pay = payment.Payment()
        # 模拟方法的调用的时候不要加括号（）
        dd = "{'a':1,'b':2}"
        pay.requestOutofSystem = mock.Mock(return_value=dd)  # 模拟第三方支付接口返回200
        print('是否被调用：', pay.requestOutofSystem.called)
        resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
        print('是否被调用：',pay.requestOutofSystem.called)
        self.assertEqual('success', resp)

    def test_pay_fail(self):
        pay = payment.Payment()
        # 模拟方法的调用的时候不要加括号（）
        pay.requestOutofSystem = mock.Mock(return_value=500)  # 模拟第三方支付接口返回500
        resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
        self.assertEqual('fail', resp)
        pay.requestOutofSystem.assert_called() # 断言是否被调用一次
        pay.requestOutofSystem.assert_called_with('12345678', 100) # 断言被调用且传参正确

    def test_pay_retry_success(self):
        pay = payment.Payment()
        # 模拟方法的调用的时候不要加括号（）
        # side_effect 和return_value 同时存在的时候，只有side_effect有用
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 200], return_value=200)  # 模拟第三方支付接口返回200
        resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
        print('被调用的次数：', pay.requestOutofSystem.call_count)
        print('被调用时的传参：',pay.requestOutofSystem.call_args)
        self.assertEqual('success', resp)

    def test_pay_retry_fail(self):
        pay = payment.Payment()
        # 模拟方法的调用的时候不要加括号（）
        # side_effect 和return_value 同时存在的时候，只有side_effect有用
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500], return_value=200)  # 模拟第三方支付接口返回200
        resp = pay.doPay(user_id=1, card_num='12345678', amount=100)
        self.assertEqual('fail', resp)

    def tearDown(self):
        pass
