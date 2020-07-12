# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 20:03
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_mysql.py

from mysql import connector
from API_6.common.read_config import ReadConfig
from API_6.common import project_path
class DoMysql:
    '''操作数据库的类，专门进行数据的读取'''

    def do_mysql(self,query,flag=1):
        '''
        :query sql查询语句
        :flag 标志 1 获取一条数据 2获取多条数据'''
        db_config=ReadConfig(project_path.conf_path).get_data('DB','db_config')

        cnn=connector.connect(**db_config)#建立一个链接
        cursor=cnn.cursor()

        cursor.execute(query)

        if flag==1:
            res=cursor.fetchone()#返回的元组
        else:
            res=cursor.fetchall()#返回的是列表嵌套元组

        return res
if __name__ == '__main__':
    query='select max(Id) from loan where MemberID=1123888'
    res=DoMysql().do_mysql(query,1)
    print('数据库的查询结果1：{}'.format(res))