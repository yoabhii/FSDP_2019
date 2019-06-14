# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:57:20 2019

@author: hp
"""

days=()
while True:
    user_input = input("Enter values")
    days.append(user_input)
    
    if not user_input:
        break
print("enter the loaction and value to add")
while True:
    value = input("Enter values>")    
    loaction=input("Enter loaction>")
    days.insert(loaction,user_input)
    
    if not loaction