# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 20:05
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : task_循环&函数.py
# 8:求 0—7 所能组成的奇数个数
#奇数：x%2!=0
#0-7 组成奇数的个数--数据范围：0-7777777
#怎么生成这些数字？range(0,77777778)
# y=0#记录奇数的个数
# for x in range(0,77777778):#0 1 2 3 4 5 6 7
#     if '8' not in str(x) and '9' not in str(x):#强制转成字符串
#         if x%2!=0:
#             y+=1
# print('奇数的个数是：{}'.format(y))


# 9:购物车程序需求：
# 1：启动程序后，让用户在控制台输入工资，然后打印商品信息（随便你们自己用什么方式存储商品，
# 记得要有商品的编号、名称以及价格）
# 2：允许用户根据商品编号购买商品
# 3：用户选择商品后，监测余额是否足够，如果足够就直接扣款，不够就提醒用户，不能购买这个商品。
# 4：可随时退出，退出后，打印已购买商品和余额

#输入工资 input
#商品信息：商品的编号 名称 价格--->字典
#已选择商品的总额要存储 if
#随时退出的机制  埋点-n 退出

# #商品列表
# goods={'1':['iphone',8800],
#        '2':['mac pro',11740],
#        '3':['xiaomi',5400],
#        '4':['辣条',5],
#        '5':['柠檬茶',4]}
#
# #展示商品给用户看
# for key in goods:#读取的是key 1 2 3 4 5
#     print('你可以购买的商品如下所示：{}'.format(goods[key]))
#
# salary=input('请输入你的工资')#只支持整数
# total=0#购买商品的资金总额
# while True:
#     goods_id=input('请输入你要购买的商品编号')#goods_id 商品编号
#     if goods_id in goods:#判断你输入的商品编好是否存在
#        total+=goods[goods_id][1]#加上商品的价格
#        if total<=int(salary):
#            print('购买的商品名称是:{}'.format(goods[goods_id][0]))
#            print('扣除金额:{}'.format(goods[goods_id][1]))
#            print('剩余工资{}'.format(int(salary)-total))
#            continue
#        else:
#            print('工资不够，不能购买')
#            break
#     elif goods_id=='n':
#             print('退出购买')
#             break
#     else:
#         print('商品id不存在')
#         continue

#函数的作业
# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
# 如果字符串不在字典中，则添加到字典中，并返回新的字典。
# import random
# def get_key(d,s):
#     while True:
#         key=s+str(random.randint(1,100))
#         if key in d.keys():#key 在d 里面 那就重新执行while循环
#             continue
#         else:#如果不在 就break 结束循环
#             break
#     return key
#
# def judge_dict(d,s):
#     '''判断字符串是否是字典中的值，不是就加入到字典中
#     d:字典
#     s:传入的字符串'''
#     if s not in d.values():
#         key=get_key(d,s)#利用函数 获取唯一的key
#         d[key]=s#添加字符串到d这个字典里面去
#     return d
#
# d={'python13':'钵钵鸡'}
# res=judge_dict(d,'python13')
# print(res)


# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
#def define 定义一个函数
def football_team(x,y,k,sex_1='f'):
    '''组建女子足球队
    x:最小年龄
    y：最大的年龄
    sex:指定组建队伍的性别
    k:指定询问的次数'''
    count=0#存储满足条件的人数
    a=0#记录询问的次数
    while True:
        age=int(input('请输入你的年龄：'))
        sex=input('请输入你的性别：')
        if x<=age<=y and sex==sex_1:
            count+=1
        a+=1
        if a==k:
            break
    print('符合条件的总人数{}'.format(count))

football_team(10,18,5,'m')