# -*- coding: utf-8 -*-
'''
Create on 2022/6/21 10:34

@author: xiachunhao

'''
import sys

import numpy as np
import random
from tool import Tool

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
        self.max_power_resource = 5000             # 最大功率上限
        self.seed = 1
        self.norm_a_finished = False
        self.norm_b_finished = False

        self.pre_day_plan = pre_day_plan
        # self.population = np.zeros((len(),len()),dtype=int)
        # 每个个体 二维数组[[系统A],[系统B]] 一组解


    def solver(self):
        # 启发式优化
        self.initial_solution1()


    # 初始解
    def initial_solution1(self):
        # 构造初始解 - 测试思路是否正确
        print("构造初始解，不允许跨天操作")
        chrom = np.zeros((3,len(self.instance)),dtype=int)      # 创建一个个体，表示系统A和B功率情况 以及可用资源剩余;
        chrom[0] = self.max_power_resource

        # 优先安排系统A额定功率 （或者安排系统B 或者取两者较大值）
        candidate_position = Tool.identify_useful_position(chrom,1)


        # step1 先指定额定功率的节点位置
        # step2 普通功率(也可能会包含额定功率)



    # todo 如果是系统B进行充电，则不影响系统A使用
    def choose_one_hour_position(self,chrom,sys_type,norm_power_position_list):
        '''
        选择系统至少工作一小时的索引位置
        :param chrom: 当前个体
        :param sys_type: 柔性负荷系统A = 1，柔性负荷系统B = 2
        :return: start_position,end_position
        '''
        s = 0
        start_position = 0
        end_position = 0
        count = 0
        find_flag = False
        while s < len(self.instance) and count < 12:       # 一小时12个时间节点
            if chrom[0,s] > 0 and (chrom[sys_type,s] == 0 or s in norm_power_position_list):
                # 满足约束
                count += 1
                if not find_flag:
                    start_position = s
                end_position = s   # 无论如何都更新结束位置
                s += 1
                continue
            find_flag = False
            s += 1
            count = 0

        if count < 12:
            print("无法安排连续一个小时的系统负荷工作,请检查逻辑......")
            start_position = end_position = 0
        return start_position,end_position


    def upadate_resources(self,chrom,start_p,end_p,sub_power,sys_type):
        '''
        :param start_p: 起始位置
        :param end_p: 结束位置
        :param sub_power: 需要分配资源
        :param sys_type: 柔性系统类型
        :return:
        '''
        update_points_list = []
        for i in range(start_p,end_p+1):
            if chrom[sys_type,i] == self.instance.system_a.norm_power:
                continue
            update_points_list.append(i)

        # 分配每个位置更新资源数量
        if sub_power == 0:
            aver_power = 0.0001
        if len(update_points_list) == 0:
            aver_power = 0
        else:
            aver_power = sub_power / len(sub_power)

        chrom[sys_type,update_points_list] = aver_power



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
