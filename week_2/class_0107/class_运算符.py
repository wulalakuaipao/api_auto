# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 20:16
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_运算符.py

#1算术运算符：1000-100+400 + - * / %
#+ - 100/100
#疑问：是否 算术运算符只能用在数字里面呢？
# s1='刘晴'
# s2='是个好学生'
# print(s1+s2)
# L1=[1,2,3,4]
# L2=('hello','python')
# print(s1*2)

#集合--课后去拓展。
#/  整数 书本上有  保留几位的小数
#%  模运算 取余运算  5%3 2
#判断奇数偶数  x%2==0 x%2==1
#随机给你100个数  请你用代码 帮我统计出来 里面一共有多少个奇数 多少个偶数
#请你分别求出100以内 偶数的和 以及奇数的和
#身份证号码： 要求你根据身份号码的特征 帮我判断 有几个男生 几个女生

#2比较运算符：比较左右两边的值的情况
#>= >  <= < == !=
#也是一种运算  运算结果是布尔值 True False 0 1
# print('GET'=='Get')#Python里面是区分大小写的
# print([1,2,3]==[1,2])
#情况： 期望结果是否等于实际结果 ==

#3赋值运算符 = += -=
# x=1
# x+=2#x=x+2--x=3
# x-=4#x=x-4-->x=-1
# print(x)
#+= -=
#累加数据的时候 我们就会用到这个 适合字符串 数字
#求和1-100之间的整合和
# sum=0
# for i in range(101):
#     sum+=i#sum=sum+i
# print(sum)

# #逻辑运算符 and or
# #课后去拓展 not 优先级-- not>and>or---这里更正一下
# #and 且  and左右两边的条件 必须同时成立  真真为真  其他情况都为假
# #or 或  or左右两边有一方成立就成立      假假为假  其他情况都为真
# #也是一种运算  运算结果是布尔值 True False 0 1
# x=2
# y=10
# print(x>0 and y<0)
# #数据金额要正确  钱包/卡余额够---才能发送成功

#成员运算符 in 存在 not in 不存在
#也是一种运算  运算结果是布尔值 True False 0 1

s1=['liu','xiaoxue','fish']
d={'name':'nancy','hobby':'coding'}#字典任何情况都是默认判断key或者是取key
print('nancy' not in d['name'])