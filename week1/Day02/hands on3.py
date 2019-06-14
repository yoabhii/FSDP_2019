# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:09:25 2019

@author: hp
"""

month=input("enter the month>")
def day_in_month(month):
    if month in ("january","march","may","july","august","octuber","december"):
        return "31"
    elif month == "febuary":
        return "27 0r 28"
    else:
        return "30"
day_in_month(month)    