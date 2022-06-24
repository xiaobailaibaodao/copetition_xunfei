# -*- coding: utf-8 -*-
'''
Create on 2022/6/20 11:06

@author: xiachunhao

'''

import time
from read_input_data import Read
from model import Model

def run_main(input_data_file):
    # 程序主入口
    read = Read(input_data_file)

    model = Model(read)
    model.opt_solver()


if __name__ == "__main__":
    # todo 通过建模方式求解每天方案

    start_time = time.time()
    print("主程序开始执行: ",start_time)
    input_data_file = '../input/基于柔性负荷任务的需量优化策略挑战赛公开数据/【算法题数据集】基于柔性负荷任务的需量优化策略挑战赛.xlsx'

    run_main(input_data_file)

    print("主程序执行结束: ",time.time()-start_time)
