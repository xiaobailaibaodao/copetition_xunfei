# -*- coding: utf-8 -*-
'''
Create on 2022/6/20 11:07

@author: xiachunhao

'''

import pandas as pd
import numpy

from system_tool import ObjSystem

class Read:

    special_month = [1,7,8,9,12]
    normal_p = {"峰": 1.0621,"平": 0.6272, "谷": 0.267}
    specail_high_p = 1.1252
    demand_price = 40
    max_power_resource = 5000

    def __init__(self,input_data_file):
        self.read_from_excel(input_data_file)


    def read_from_excel(self,input_data_file):
        # 从Excel读取输入数据
        self.power_df,device_df,price_df = pd.read_excel(input_data_file,sheet_name=[0,1,2],converters={'dtime':pd.Timestamp}).values()   # sheet_name = [多个sheet] 返回的字典

        # 设备信息
        for index,row in device_df.iterrows():
            if row['Is_stor'] == True:
                self.system_b = ObjSystem(row['device_name'],row['Is_stor'],row['norm_power'],row['Is_need'])
            else:
                self.system_a = ObjSystem(row['device_name'],row['Is_stor'],row['norm_power'],row['Is_need'])

        # 每天每个时段功率数据
        self.power_df = self.power_df.sort_values(by=['dtime'])
        print("测试数据总量: ",len(self.power_df))


        print("success!")


    def per_kw_price(self,date):
        # 根据月份、时间确定电价
        month = date.month
        hour = date.hour

        price = 0
        period_type = ''
        # 特殊月份 高峰时段电价 稍贵
        if (hour >= 9 and hour < 12) or (17 <= hour < 22):     # todo 假设选择 左闭右开 区间
            period_type = "峰"
        elif (hour >= 8 and hour < 9) or (12 <= hour < 17) or (hour >= 22 and hour < 23):
            period_type = "平"
        else:
            period_type = "谷"

        if month in self.special_month and period_type == "峰":
            price = self.specail_high_p
        else:
            price = self.normal_p[period_type]
        return price


if __name__ == "__main__":

    input_data_file = '../input/基于柔性负荷任务的需量优化策略挑战赛公开数据/【算法题数据集】基于柔性负荷任务的需量优化策略挑战赛.xlsx'
    read = Read(input_data_file)

