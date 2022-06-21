# -*- coding: utf-8 -*-
'''
Create on 2022/6/20 13:58

@author: xiachunhao

'''


class ObjSystem:

    def __init__(self,device_name,is_stor,norm_power,is_need):
        self.device_name = device_name
        self.is_stor = is_stor
        self.norm_power = norm_power
        self.is_need = is_need

    def __str__(self):
        return "设备名: %s, 是否柔性系统B: %s, 设备额定功率: %s, 设备是否必须: %s" % (self.device_name,self.is_stor,self.norm_power,self.is_need)

