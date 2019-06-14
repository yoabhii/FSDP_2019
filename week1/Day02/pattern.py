# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:43:04 2019

@author: hp
"""

def pat(n):
    for i in range(0,n):
        print('*'*i)
    for i in range(n,0,-1):
        print('*'*i)
n=int(input("Enter a number>"))
print(n)
pat(n)