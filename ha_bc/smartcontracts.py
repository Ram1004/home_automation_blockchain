#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:22:32 2018

@author: Ram
"""

class SmartContract:
    def __init__(self,sender,task_to_perform,receiver):
        self.sender = sender
        self.task_to_perform = task_to_perform
        self.receiver = receiver
        self.task_perform = " "
        self.task_to_perform_v = self.sender_user()
    
    def sender_user(self):
        
        list_users = ['abcd','xyzf']
        
        """for i in list_users:
            if self.sender==i:
                print("SENDER IS USER")
                self.task_to_perform = self.users_contract()
            else:
                self.task_to_perform = self.device_contract()
                break"""
        if self.sender in list_users:
            print("----- INSTRUCTION CALLED BY USER ------")
            return self.users_contract()
        else:
            print("SENDER IS DEVICE")
            return self.device_contract()
    
    def users_contract(self):
        from user import users
        u = users(self.task_to_perform)
        return u.verified_task_to_perform()
        
    def device_contract(self):
         from device import devices
         d = devices(self.sender,self.task)
         return d.verified_task_to_perform()
     
    def verified_task(self):
        return self.task_to_perform_v
    
    def verified_received(self):
        return self.receiver
        
         
