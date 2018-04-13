#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:10:41 2018

@author: himanshu
"""

class users:
    def __init__(self,task):
        self.task = task
        self.switch_off = 'ijklmnop'
        self.switch_on = 'abcdefgh'
    def verified_task_to_perform(self):
        if self.task == self.switch_off:
            return '***'
        if self.task == self.switch_on:
            return '###'
