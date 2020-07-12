# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 21:17
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_嵌套for循环.py

#嵌套for循环
# d={'name':{'boboji':'钵钵鸡','snow':'小雪','luren':'路人'},
#    'score':[99,100,120]}
# # print(d['name'])
# # print(d['score'])
# #字典里面嵌套了列表和字典
# #for循环遍历字典的时候  遍历的是key
# for key in d:
#     print(d[key])
#     for item in d[key]:
#         print(item)
# list1 = [[2, 3, 8, 4, 9, 5, 6],[5, 6, 10, 17, 11, 2]]
#请你利用刚刚所学的for循环 然后我们把每一个元素都读取出来
# for item in list1:
# #     print(item)#1
# #     for y in item:#2
# #         print(y,end=' ')
# #     print()#3
#演示嵌套循环的使用：
# r1=range(1,3)
# r2=range(1,3)
# for i in r1:
#     print('我是外层循环...')
#     for j in r2:
#         print('我是内层循环...')
#         print('i=%d,j=%d' %(i,j))

for i in range(1,6): #外层循环控制行数
    for j in range(1,6): #内层循环控制每一行打印的次数
        print('*',end='')
    #此处的print()的作用仅仅是为了换行
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')  #end=''是为了不换行
    # 此处的print()的作用仅仅是为了换行
    print()