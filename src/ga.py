# -*- coding: utf-8 -*-
'''
Create on 2022/6/21 10:34

@author: xiachunhao

'''

import numpy as np

class GA:
    '''
        遗传算法，尝试使用geatpy
    '''

    def __init__(self,sub_instance,sys_a_act_power,sys_b_act_power,pre_day_plan=''):
        '''
        :param sub_instance: 某天的回路功率数据
        :param pre_day_plan: 前一天计划 (如果为空，则表示不允许跨天)
        '''
        self.instance = sub_instance
        self.sys_a_act_power = sys_a_act_power
        self.sys_b_act_power = sys_b_act_power
        self.pre_day_plan = pre_day_plan
        # self.population = np.zeros((len(),len()),dtype=int)
        # 每个个体 二维数组[[系统A],[系统B]] 一组解


    def solver(self):
        # 启发式优化
        self.initial_solution1()


    # 初始解
    def initial_solution1(self):
        # 构造初始解 - 测试思路是否正确
        # todo 方案一：首先按照自然天进行安排，不能跨天
        print("构造初始解，不允许跨天操作")



    # 进化

    # 交叉

    # 变异

    def evalue_score(self):
        # 调控后得分 - 即目标函数
        pass


    def calculate_total_cost(self):
        # 计算产生 总电费 = 电量电费 + 需量电费
        # 电量电费 = 峰平谷各段时间电费之和
        # 需量电费 = 最高功率 * 单位需量电价
        pass
