#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:13:49 2018

@author: ram
"""
import hashlib
import datetime

class Block:
    
    def __init__(self,previousHash,data,timestamp):
        self.previousHash = previousHash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()
    def get_hash(self):
        header_bin = (str(self.previousHash) + str(self.data) + str(self.timestamp)).encode()
        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest().encode()
        return outer_hash
    def get_previousHash(self):
        return self.previousHash
    def get_Transaction(self):
        return self.transaction
    def create_genesis_block():
        return Block("0","0",datetime.datetime.now())
    
