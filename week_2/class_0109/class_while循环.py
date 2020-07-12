# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 20:16
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_while循环.py

#while循环 关键字 while  while后面加条件
#while后面的条件可以是--->布尔值 非空的 空数字 比较运算 逻辑运算 成员运算
#执行逻辑：先判断 --条件成立 True 执行代码 执行完毕之后 再判断  如果满足就 继续执行 再判断
                #--条件不成立 False over

#请输出100次 hello 我是while循环到控制台
#1:防止while循环进入死循环 你就要限制他的次数  达到指定的次数后 break
# c=0
# while True:
#     print('hello 我是while循环')
#     c=c+1#每循环一次我就加1
#     if c==10:
#         break#终止循环，结束循环


#2：不要让while 表达式成为永真式
# c=0
# while c<10:#c=0 1 2 3 4 5 6 7 8 9
#     print('hello 我是while循环')
#     c=c+1#每循环一次我就加1  c=1 2 3 4 5 6 7 8 9 10

#课堂练习
# 2.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，
# 输出满足条件的总人数--->
# c=0
# while True:
#     age=int(input('请输入你的年龄'))
#     sex=input('请输入你的性别：m表示男性，f表示女性')
#     if 10<=age<=12 and sex=='f':
#         print('恭喜你可以计入我们的足球队')
#         num+=1#只有进入到这个if条件语句下面 才是满足的
#     else:
#         print('很遗憾，你不能加入我们的足球队')
#     #每完成一次询问 我们就加1
#     c=c+1
#     if c==3:#简化一下
#         break

c=0#统计循环次数
num=0#统计符合条件的人数 符合加入足球队的人数
while c<3:
    age=int(input('请输入你的年龄'))
    sex=input('请输入你的性别：m表示男性，f表示女性')

    if 10<=age<=12 and sex=='f':
        print('恭喜你可以计入我们的足球队')
        num+=1#只有进入到这个if条件语句下面 才是满足的
    else:
        print('很遗憾，你不能加入我们的足球队')

    #每完成一次询问 我们就加1
    c=c+1
