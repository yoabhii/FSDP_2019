# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:32:06 2019

@author: hp
"""

a1= int(input("enter score of assingment1>"))
print(a1)
a2=int(input("enter score of assingment2>"))
print(a2)
a3=int(input("enter score of assingment3>"))
print(a3)
e1=int(input("enter score of exam1>"))
print(e1)
e2=int(input("enter score of exam2>"))
print(e2)
score = (( a1 + a2 + a3 ) *0.1) + ((e1 + e2 ) * 0.35)
print("weighted score="+str(score))