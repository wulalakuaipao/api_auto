# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 20:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : human_vs_pc.py
# 1：人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
import random

class HumanVsPC:

    # fist_dict={'1':'剪刀','2':'石头','3':'布'}
    def __init__(self):
        self.fist_dict = {'1': '剪刀', '2': '石头', '3': '布'}

    def choose_role(self):
        '''选择角色'''
        role_dict = {'1': '曹操', '2': '张飞', '3': '刘备'}
        while True:
            num = input('请输入你要选择的角色：1 曹操 2张飞 3 刘备')
            if num in role_dict.keys():
                print('获取的角色是{}'.format(role_dict[num]))
                return role_dict[num]  # 返回角色的名字
            else:
                print('输入的角色不正确,请重新选择')
                continue

    def human_fist(self, role):
        '''角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字'''
        while True:
            num = input('请出拳：1剪刀 2石头 3布')
            if num in self.fist_dict.keys():
                print('{}出拳为:{}'.format(role, self.fist_dict[num]))
                return int(num)
            else:
                print('出拳错误,请重新出拳')

    def pc_fist(self):
        '''电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果'''
        num = random.randint(1, 3)
        print('PC出拳为{}'.format(self.fist_dict[str(num)]))
        return num

    def human_vs_pc(self):
        '''人机对战
        a 记录 human赢
        b 记录pc赢
        c 记录平局'''
        a = 0
        b = 0
        c = 0
        role = self.choose_role()  # 调用类里面的其他函数 self.函数名
        while True:
            human_fist = self.human_fist(role)
            pc_fist = self.pc_fist()
            if human_fist - pc_fist in (1, -2):  # human赢
                a += 1
                print('{}赢了'.format(role))
            elif human_fist - pc_fist in (-1, 2):  # pc赢
                b += 1
                print('pc赢了')
            else:
                c += 1
                print('两者平局')
            while True:
                choice = input('是否继续对战，y:继续 n:退出')
                if choice == 'y':
                    flag = 1  # 标记为继续
                    break

                elif choice == 'n':
                    flag = 2  # 标记为退出状态
                    break
                else:
                    print('输入选项错误，请重新输入')
                    continue
            if flag == 1:  # 这里继续判断
                continue
            else:
                break

        print('这次对战，{}赢了{}局，pc赢了{}局，平局{}次'.format(role, a, b, c))


if __name__ == '__main__':
    HumanVsPC().human_vs_pc()
# '请出拳：1剪刀 2石头 3布'
