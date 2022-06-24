# -*- coding: utf-8 -*-
'''
Create on 2022/6/21 10:34

@author: xiachunhao

'''
import sys

import numpy as np
import random

import pandas as pd

from tool import Tool

class GA:
    '''
        遗传算法，尝试使用geatpy
    '''

    def __init__(self,sub_instance,sys_a_act_power,sys_b_act_power,origin_data):
        '''
        :param sub_instance: 某天的回路功率数据
        '''
        self.instance = sub_instance
        self.sys_a_act_power = sys_a_act_power
        self.sys_b_act_power = sys_b_act_power
        self.origin_data = origin_data
        self.max_power_resource = 5000             # 最大功率上限
        self.seed = 1
        # self.norm_a_finished = False
        # self.norm_b_finished = False

        # self.population = np.zeros((len(),len()),dtype=int)
        # 每个个体 二维数组[[系统A],[系统B]] 一组解


    def solver(self):
        # 启发式优化
        chrom = self.initial_solution1()

        format_result = self.format_result_type(chrom)
        return format_result

    # 初始解
    def initial_solution1(self):
        # 构造初始解 - 测试思路是否正确
        chrom = np.zeros((3,len(self.instance)),dtype=float)      # 创建一个个体，表示系统A和B功率情况 以及可用资源剩余;
        chrom[0] = self.max_power_resource

        # step1 先指定额定功率的节点位置,初始状态肯定满足
        # 优先安排系统B 额定功率
        current_p = Tool.greed_distribute_resource(chrom,2,self.sys_b_act_power,self.origin_data.system_b.norm_power,0)

        # 系统A
        Tool.greed_distribute_resource(chrom,1,self.sys_a_act_power,self.origin_data.system_a.norm_power,current_p)  # todo 没选择谷时段

        print("初始解构造完成...")
        return chrom


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



    # 进化

    # 交叉

    # 变异

    def evalue_score(self):
        # 调控后得分 - 即目标函数
        # TODO 整体目标变化
        pass


    def calculate_total_cost(self):
        # 计算产生 总电费 = 电量电费 + 需量电费
        # 电量电费 = 峰平谷各段时间电费之和

        # 需量电费 = 最高功率 * 单位需量电价
        # 需要电费 受 月维度数据影响
        pass


    def format_result_type(self,chrom):
        # 格式化结果
        result_dict = {"dtime":list(self.instance['dtime']),"all_power_plan":[5000]*len(self.instance),"a_test_power_plan":list(chrom[1]),"b_test_power_plan":list(chrom[2])}
        result = pd.DataFrame.from_dict(result_dict,orient='index').T
        return result
