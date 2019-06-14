# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:40:07 2019s

@author: hp
"""

import re
number_list= list()

while True:
    number= input("enter number>")
    if not number:
        break
    number_list.append(number)
    
result_list=[]
for number in number_list:
    if re.match(r'^[+-]?\d*\.\d*$', number):
        result_list.append(True)
    else:
         result_list.append(False)
         
print(result_list) 
        