# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:49:40 2019

@author: user

"""

import pandas as pd
from selenium import webdriver

url = "https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome(executable_path="C:\Users\user\Downloads")
 
driver.get(ur1)
right_table=driver.find_element_by_class_name('ur1')
 
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data) 
df.to_csv("data/former.csv")


driver.quit()


