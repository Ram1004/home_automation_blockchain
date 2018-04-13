#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 21:58:30 2018

@author: ram
"""

class devices:
    def __init__(self,device,task):
        self.device = device
        self.task = task
        self.switch_off = "AAA"
        self.switch_on = "BBB"
        self.list_of_devices = ['1234','4567','0987']
    def verified_task_to_perform(self):
        if self.task == self.switch_off:
            return "###"
        if self.task == self.switch_on:
            return "***"
    def check_device(self):
        for i in self.list_of_devices:
            if self.device == i:
                
           
