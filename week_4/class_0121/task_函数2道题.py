# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 20:44
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : task_函数2道题.py
# 1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# def judge_len(*args):
#     for arg in args:
#         if isinstance(arg,str):#这个是判断arg是不是字符串类型
#             if len(arg)>5:
#                 print('参数：{}，长度大于5'.format(arg))
#             else:
#                 print('参数：{}，长度不大于5'.format(arg))
#         elif isinstance(arg,list):#这个是判断arg是不是列表类型
#             if len(arg)>5:
#                 print('参数：{}，长度大于5'.format(arg))
#             else:
#                 print('参数：{}，长度不大于5'.format(arg))
#         elif isinstance(arg,tuple):#这个是判断arg是不是元组类型
#             if len(arg)>5:
#                 print('参数：{}，长度大于5'.format(arg))
#             else:
#                 print('参数：{}，长度不大于5'.format(arg))
#         else:
#             print('该函数不支持该{}类型的判断'.format(type(arg)))
# judge_len('hello','666',[1,3,4,5])

# 2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def judge_list(L):
    '''写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
    :arg L 调用函数的时候，传入的列表值'''
    if isinstance(L,list):
        if len(L)>2:
            return L[:2]
        else:
            print('长度小于2')
    else:
        print('传入的值并非列表值！')
print(judge_list([1,2,3]))