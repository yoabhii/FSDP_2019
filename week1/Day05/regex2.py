# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:01:18 2019

@author: hp
"""

import re
email_list= list()

while True:
    email= input("enter email>")
    if not email:
        break
    email_list.append(email)

valid=[]
for email in email_list:
    if re.match(r'^[a-z0-9_-]+@[a-z0-9_-]+.[a-z-]{2,4}$',email):
        valid.append(email)
        
print("valid email:",sorted(valid))        