# -*- coding: utf-8 -*-
'''
Create on 2022/6/21 15:04

@author: xiachunhao

@description: 用于检测生成结果是否有问题

'''


import pandas as pd


def check_algo_result(result_list,sys_a_act_power_dict,sys_b_act_power_dict):
    '''
    :param result_list: 结果集合
    :param sys_a_act_power_dict: 系统A实际用电情况
    :param sys_b_act_power_dict: 系统B实际用电情况
    :return: 违反约束日期
    '''
    # 检查算法结果是否满足各种约束
    pass


if __name__ == "__main__":
    for i in range(3,5):
        print(i)

