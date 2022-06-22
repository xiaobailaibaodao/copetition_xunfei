# -*- coding: utf-8 -*-
'''
Create on 2022/6/22 9:34

@author: xiachunhao

'''


class Tool:


    @classmethod
    def identify_useful_position(cls,chrom,sys_type):
        # 方式一：只考虑为使用的位置
        # 识别出当前系统的 还未使用 位置及资源
        usefull_position_list = []
        zero_position = np.where(chrom[sys_type] == 0)[0]
        resource_position = np.where(chrom[0] > 0)[0]
        if len(resource_position) == 0 or len(zero_position) == 0:
            return usefull_position_list

        ret_position_list = list(set(zero_position).intersection(resource_position))
        if len(ret_position_list) == 0:
            return usefull_position_list
        ret_position_list.sort()

        # 判断逻辑
        for i in range(len(ret_position_list)):
            if i == 0:
                usefull_position_list.append([ret_position_list[i]])
                continue
            if usefull_position_list[-1][-1] + 1 == ret_position_list[i]:
                usefull_position_list[-1].append(ret_position_list[i])
            else:
                usefull_position_list.append([ret_position_list[i]])

        return usefull_position_list


    @classmethod
    def identify_useful_position2(cls, chrom, sys_type):
        # 方式二：考虑资源可用位置(包括未满载使用位置)
        # 识别可用位置,只要资源可用
        resource_position = np.where(chrom[0] > 0)[0]
        if sys_type == 1:
            use_position = np.where(chrom[sys_type] < 2500)
        else:
            use_position = np.where(chrom[sys_type] < 5000)



if __name__ == "__main__":
    import numpy as np

    l = [1,2,3,5,6,9,11]
    usefull_position_list = []
    for i in range(len(l)):
        if i == 0:
            usefull_position_list.append([l[i]])
            continue
        if usefull_position_list[-1][-1] + 1 == l[i]:
            usefull_position_list[-1].append(l[i])
        else:
            usefull_position_list.append([l[i]])
    print(usefull_position_list)

