# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
"""
1, 什么是正则表达式？编写一些规范查找需要的字符串
2，正则表达式的一个组成： 原义字符和元字符
3，如何Python来解析？
4，正则表达式的场景？
---参数化
---查找一些特殊的字符：邮箱，手机号码，身份证号码。
"""
import re

target = "{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
p = 'normal_user'  # 原义字符的查抄
p2 = '#(.*?)#'  # 圆括号代表正则表达式里面组的概念
m = re.search(p2, target)  # 在目标字符串里面根据正则表达式来查找，有匹配的字符串就返回对象
print(m)
print(m.group())  # 不传参的时候返回表达式和匹配的字符串一起
print(m.group(1))  # 传参就是只返回匹配的字符串，也就是当前组的匹配字符
mm = re.findall(p2, target)  # 找到所有的匹配的的字符，返回是一个列表
print(mm)

target2 = re.sub(p2, '18688775656', target,count=1)
print(target2)
