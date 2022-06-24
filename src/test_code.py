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


def draw_gante_picture(df):
    # 将结果通过甘特图展示，发现优化点
    pass


if __name__ == "__main__":

    input_data_file = '../input/基于柔性负荷任务的需量优化策略挑战赛公开数据/【算法题数据集】基于柔性负荷任务的需量优化策略挑战赛.xlsx'
    power_df = pd.read_excel(input_data_file)  # sheet_name = [多个sheet] 返回的字典
    power_df['date'] = power_df['dtime'].apply(lambda x: str(x).split()[0])
    sample_instance = power_df[power_df['date']=='2022-01-01']

    draw_gante_picture(sample_instance)


