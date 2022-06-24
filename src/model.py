# -*- coding: utf-8 -*-
'''
Create on 2022/6/20 15:07

@author: xiachunhao

'''

import time
import pandas as pd
from ga import GA

# 通过GA
# 正好尝试试用一下Geatpy工具

class Model:

    def __init__(self,instance_data):
        self.instance_data = instance_data
        self.power_data = instance_data.power_df
        self.total_result_df = pd.DataFrame()


    def opt_solver(self):

        self.power_data['日期'] = self.power_data['dtime'].apply(lambda x: str(x).split()[0])
        # self.power_data = self.power_data[self.power_data['日期'] == '2022-06-01']   # todo 随机选择一天进行测试

        for d,sub_instance in self.power_data.groupby('日期'):
            # 柔性负荷系统实际用电量
            print("开始处理 {} 柔性负荷优化".format(d))
            if len(sub_instance) <= 6:
                print("数据不足，不予分配....")
                continue

            sub_instance.reset_index(inplace=True,drop=True)
            sub_instance = sub_instance.drop(labels=len(sub_instance)-1,axis=0)     # todo 不允许跨天操作

            sys_a_act_power = sub_instance['a_test_power'].sum()
            sys_b_act_power = sub_instance[sub_instance['b_test_power'] > 0]['b_test_power'].sum()

            # 调用算法
            print("开始GA算法过程: ")
            ga = GA(sub_instance,sys_a_act_power,sys_b_act_power,self.instance_data)
            day_plan_result = ga.solver()

            # 合并结果
            self.total_result_df = self.total_result_df.append(day_plan_result)

        self.total_result_df['d'] = self.total_result_df['dtime'].astype('str')
        self.total_result_df = self.total_result_df[['d','a_test_power_plan','b_test_power_plan']]
        output_model = pd.read_csv('../input/基于柔性负荷任务的需量优化策略挑战赛公开数据/提交示例.csv')
        output_model = output_model[['dtime','all_power_plan']]
        output_model['d'] = output_model['dtime'].apply(lambda x: pd.Timestamp(x))
        output_model['d'] = output_model['d'].astype("str")
        output_model = pd.merge(output_model,self.total_result_df,how='left',on='d')
        out_result = output_model[['dtime','all_power_plan','a_test_power_plan','b_test_power_plan']]
        out_result.to_csv('../output/提交结果.csv',index=False,encoding='utf8')
        print("处理结束....")


    # 迭代优化

    # todo 求解器模型 - 天维度建模
