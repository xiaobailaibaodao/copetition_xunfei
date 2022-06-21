# -*- coding: utf-8 -*-
'''
Create on 2022/6/20 15:07

@author: xiachunhao

'''

import time
from ga import GA

# 通过GA
# 正好尝试试用一下Geatpy工具

class Model:

    def __init__(self,instance_data):
        self.instance_data = instance_data


    def opt_solver(self):

        if self.instance_data.empty:
            print("输入数据为空！")
            return

        self.instance_data['日期'] = self.instance_data['dtime'].apply(lambda x:time.strptime(x,'%Y-%m-%d'))
        self.instance_data = self.instance_data[self.instance_data['日期'] == '2022-05-01']   # 随机选择一天进行测试

        for d,sub_instance in self.instance_data.groupby('日期'):
            # 柔性负荷系统实际用电量
            sys_a_act_power = sub_instance['a_test_power']
            sys_b_act_power = sub_instance['b_test_power']

            # 调用算法
            print("开始GA算法过程: ")
            ga = GA(sub_instance,sys_a_act_power,sys_b_act_power)
            ga.solver()




    # todo 方案二：允许跨天

    # 迭代优化

    # todo 求解器模型 - 天维度建模
