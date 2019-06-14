# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:48:36 2019

@author: hp
"""

spr_mkt={}

while True:
    
    item= input("Enter item >")
    price=int(input("enter the vaue"))
    
    if not price:
        break
    spr_mkt[item]=price
print(spr_mkt)    