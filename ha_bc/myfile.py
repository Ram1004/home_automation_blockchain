#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:00:36 2018

@author: Ram
"""
import hashlib
import json
class Instructon:
    
    def __init__(self,address_inst, inst):
        self.address = address_inst
        self.instruction = inst
        
    def __split_instrction(self):
        return self.instruction[0:8] , self.instruction[8:16] 
    
    def call_smart_contract(self):
        from smartcontracts import SmartContract

        task_to_perform ,receiver =self.__split_instrction()
        """self.task = task
        self.receiver = receiver"""
        
        sm = SmartContract(self.address,task_to_perform,receiver)
         
        return sm.verified_task(),sm.verified_received()
    
class Block:
    
    def __init__(self,address_sender,instruction,previousHash = ''):
        self.Address = address_sender
        self.instruction = instruction
        self.previousHash = previousHash
        self.hash  = self.get_hash()
        self.__list_of_verified_address = ['0','abcd','asdff','adafsdf']
        self.verified_address = self.__verify_address()
        if self.verified_address == True:
            self.verified_task , self.verified_rec = self.__Instruction_process()
            
    def get_hash(self):
        hash_head = (bytearray(str(self.Address)+str(self.instruction)+str(self.previousHash),"utf-8"))
        inner_hash = hashlib.sha256(hash_head).hexdigest()
        #outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return inner_hash
    
    
    def __verify_address(self):
        add = str(self.Address)
        """for i in range(len(self.list_of_verified_address)):
            if add == self.list_of_verified_address[i]:
                print("Address Verified")
                self.t = True
            else:
                print('Not verified')
                self.t = False"""
        if add in self.__list_of_verified_address:
            print("-------YOUR INPUT IS VERIFIED------")
            return True
        else:
            print('Not verified')
            return False
        
    def __Instruction_process(self):
        if self.instruction == 'generis':
            return self.Address, self.instruction
        else:
            instt = Instructon(self.Address,self.instruction)
            task,receive = instt.call_smart_contract()
            return task , receive
                
    def get_previous_hash(self):
        return self.previousHash
    
    def current_hash(self):
        return self.hash  
    """def mine_block(self,difficulty):
        while self.hash.substring(0,difficulty) != []:
            self.nonce +=1
            self.hash = self.get_hash()
         print("MINED::",self.hash)"""

class BlockChain:
    
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 0
        
    def create_genesis_block(self):
        return Block(address_sender=0,instruction="generis",previousHash=0)
   
    
    def __get_new_block(self):
        return self.chain[len(self.chain) -1]
    
    def Insert_block(self,newblock):
        newblock.previousHash = self.__get_new_block().hash
        newblock.hash = newblock.get_hash()
        #newblock.mine_block(self.difficulty)
        self.chain.append(newblock)
                
    """def validate_chain(self):
        for i in range(1,len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.get_hash:
                return False
            if current_block.previousHash != previous_block.hash:
                return False
        return True"""


"""INSTRUCTION SHOULD BE OF 16 BIT CODE = TASK_TO_PERFORM = 8 BIT + RECEIVER = 8BIT"""
                        
Hometoken = BlockChain()
Hometoken.Insert_block(Block(address_sender= 'abcd' ,instruction= "abcdefghijklmnop"))
Hometoken.Insert_block(Block('sfed',2))
#him.Insert_block(Block(3,45))
#him.Insert_block(Block(4,23))
block_chain = Hometoken.chain

#him.validate_chain()

#him.chain[2].data = 4

#him.validate_chain()


ch = him.chain
"""
        
        
        
