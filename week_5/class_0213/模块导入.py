# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 20:06
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 模块导入.py

#我重新写两个函数--low
#调用已有写好的函数？？？

#导入模块 多种方式讲解 import
#导入模块的时候--->一层一层的定位，除开顶级目录---一层一层一层的剥开
#第一种方法： import
# import week_5.class_0213.math_add#导入指定路径下面的add模块
# res=week_5.class_0213.math_add.add(4,5)
# print(res)

#第二种方法：import..as..  as取别名
# import week_5.class_0213.math_add as t#导入指定路径下面的add模块
# res=t.add(4,5)
# print(res)

#第三种方式:from...import...
# from week_5.class_0213.math_add import add,add_2#具体到函数名/模块名
# from week_5.class_0213.math_add import *#*代表所有函数
# res=add(6,7)
# res_2=add_2(1,2,3,4)
# print(res)
# print(res_2)

#第四种方式:from...import...as
# from week_5.class_0213.math_add import add_five_positive_numbers as a5
# a5(1,2,3,4,5)


from week_5.class_0213.math_add import add_2
add_2(1,3)