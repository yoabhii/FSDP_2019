# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:51:23 2019

@author: hp
"""

year=int(input("Enter the year to find leap year or not>"))
def leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return 'true'
    else:
        return 'false'
leap_year(year)
 