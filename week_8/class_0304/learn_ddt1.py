#!/usr/bin/python
# -*- coding: <utf-8> -*-
# _Author_ = 'shuai'
# Data：2020/1/7 14:40
import unittest
from ddt import ddt, data, unpack
@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data([1, 2, 3])
    def test_1(self, value):
        print('test_1 value is ', value)
        #打印的值是test_1 value is  [1, 2, 3]

    @data([1, 2, 3])
    @unpack
    def test_2(self, a, b, c):
        print('unpack test ', a, b, c)

        #打印值为unpack test  1 2 3


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
