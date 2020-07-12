#!/usr/bin/python
# -*- coding: <utf-8> -*-
#_Author_ = 'shuai'  
# Data：2020/1/8 11:34
import unittest
from ddt import ddt,data,file_data,unpack
test_data1=[[2,3],[4,5]]
@ddt
class Demotest(unittest.TestCase):
    def setup(self):
        print('this is the setup')
    @data(2,3)
    def testb(self,value):
        print(value)
        print('this is test b')
        # 2
        # this is test b
        # 3
        # this is test b
    @data(*test_data1)
    @unpack
    def testa(self,value):
        print(value)
        print('this is test a')
        # [2, 3]
        # this is test a
        # [4, 5]
        # this is test a
    @data([2, 3],[4, 5])
    @unpack
    def testc(self, first,second):
        print(first)
        print(second)
        print('this is test c')
        # 2
        # 3
        # this is test c
        # 4
        # 5
        # this is test c
    # @file_data('/data_dic.json')
    # def test_dic(self,value):
    #     print(value)
    #     print('this is dic')
    # @file_data('/data.yml')
    # def test_yml(self, value):
    #     print(value)
    #     print('this is yml')
    def teardown(self):
        print('this is the down')
if __name__ == '__main__':
    unittest.main()
    suite=unittest.TestLoader.getTestCaseNames(Demotest)
    #suite = unittest.TestLoader().loadTestsFromTestCase(demotest)
    #unittest.TextTestRunner(verbosity=2).run(suite)