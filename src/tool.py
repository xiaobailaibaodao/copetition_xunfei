# -*- coding: utf-8 -*-
'''
Create on 2022/6/22 9:34

@author: xiachunhao

'''


class Tool:


    @classmethod
    def identify_useful_position(cls,chrom,sys_type):
        # 方式一：只考虑未使用的位置
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
            use_position = np.where(chrom[sys_type] < 2500)[0]
        else:
            use_position = np.where(chrom[sys_type] < 5000)[0]
        ret_position_list = list(set(use_position).intersection(resource_position))
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
    def simply_allocate_resources(cls, start_index, end_index):
        # 分配资源规则
        pass


    @classmethod
    def greed_distribute_resource(cls, chrom, sys_type, act_power, sys_norm_power,index):
        # 贪心分配初始资源位置 - 一次性分配12个时间节点
        start_index = index
        current_index = index
        chrom[sys_type, start_index:start_index+6] = sys_norm_power    # 每个时间节点5分钟
        chrom[0, start_index:start_index+6] = [chrom[0, i] - chrom[sys_type, i] for i in range(start_index, start_index+6)]
        per_node_power = Tool.per_node_power(act_power, sum(chrom[sys_type]), 18,sys_norm_power)        # 假设就两次
        start_index = start_index + 6
        chrom[sys_type, start_index:start_index+6] = per_node_power
        chrom[0, start_index:start_index+6] = [chrom[0, i] - chrom[sys_type, i] for i in range(start_index, start_index+6)]

        current_position = start_index + 6 + 1    # todo 间隔一个空档
        second_position = current_position
        chrom[sys_type,current_position:current_position+12] = per_node_power
        chrom[0,current_position:current_position+12] = [chrom[0, i] - chrom[sys_type, i] for i in range(current_position, current_position+12)]

        current_position = current_position+12
        # 剩余电量
        total_nodes, sing_node = divmod(act_power - sum(chrom[sys_type]), sys_norm_power)
        if total_nodes > 0:
            chrom[sys_type, current_position:current_position + int(total_nodes)] = sys_norm_power
            chrom[0, current_position:current_position + int(total_nodes)] = [chrom[0, i] - chrom[2, i] for i in range(current_position,current_position + int(total_nodes))]
            current_position = current_position + int(total_nodes)

        if sing_node > 0 and total_nodes >= 0:
            chrom[sys_type, current_position] = sing_node
            chrom[0, current_position] = chrom[0, current_position] - sing_node

        current_position += 1     # 换系统时，直接从空白处开始赋值

        # todo 放电过程确定
        if sys_type == 2:
            element = current_position-second_position
            chrom[sys_type,current_position+1:current_position+1+element] = chrom[sys_type,second_position:current_position]*-1

        return current_position




    @classmethod
    def update_all_resources(cls, chrom, start, end, r_list):
        '''
        :param start: 起始位置
        :param end: 结束位置
        :param r_list: 消耗资源
        :return:
        '''

        p_list = range(start, end + 1)
        for i in range(len(p_list)):
            chrom[0, p_list[i]] = chrom[0, p_list[i]] - r_list[i]


    @classmethod
    def per_node_power(cls,act_power,assigned_power,nodes_num,sys_norm_power):
        # 计算每个时间节点分配资源
        unassign_power = act_power - assigned_power
        if unassign_power <= 0:
            per_node_power = 0.0001  # todo 随机给的一个足够小值，证明工作
        else:
            per_node_power = min(unassign_power / nodes_num, sys_norm_power)
        return per_node_power


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

