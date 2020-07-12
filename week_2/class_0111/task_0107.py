# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 20:03
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : task_0107.py
# 一个5位数，判断它是不是回文数。即12321 是回文数，个位与万位相同，十位与千位相同。根据判断打印出相关信息。
#45654
#获取一个5位数
# a=input('请输入5位数：')#input获取的数据 是字符串 str
# if a.isdigit() and len(a)==5:#判断他是否是纯数字
#     if a[0]==a[-1] and a[1]==a[-2] and a[0]!='0':
#         print('该数字：{}是回文数'.format(a))
#     else:
#         print('该数字：{}不是回文数'.format(a))
# else:
#     print('输入有误，请输入5位数字！')

#7题
dishes={'平价菜':{'手撕包菜':10,'苦瓜炒蛋':12,'农家小炒肉':13},
        '凉菜':{'凉拌黄瓜':8,'凉拌皮蛋':9},
        '小锅现炒':{'水煮鱼':22}}
dish_type=input('请输入你要选择的菜品类目:')
if dish_type in dishes.keys():#判断你输入的菜品类目是否存在
    dish_name=input('请输入你要选择的菜名：')
    if dish_name in dishes[dish_type].keys():
        print('你选择的菜名是{}，价格是{}元'.format(dish_name,dishes[dish_type][dish_name]))
    else:
        print('你输入的菜名不存在！')
else:
    print('你输入的品类不存在！')
