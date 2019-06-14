# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:44:02 2019

@author: hp
"""

name='RESTART'
str1 = name.replace('R','$')
str2 = str1.replace('$','R',1)

name1 = name[1:]
str1 = name1.replace('R','$')
print(name[0]+str1)
