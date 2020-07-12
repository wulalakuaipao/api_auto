#!/usr/bin/python
# -*- coding: <utf-8> -*-
#_Author_ = 'shuai'  
# Data：2020/1/8 18:59
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "ls", "111111", "mybatis")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用预处理语句创建表
sql = "select * from user where username =\'张三\'"
try:

    cursor.execute(sql)  # 执行SQL语句
    results = cursor.fetchall()  # 获取所有记录列表
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")
# 关闭光标对象
cursor.close()
# 关闭数据库连接
db.close()