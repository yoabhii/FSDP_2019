# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:48:30 2019

@author: user
"""

from bs4 import BeautifulSoup
import requests



cricket = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(cricket).text



soup = BeautifulSoup(source,"lxml")

print (soup.prettify())



right_table=soup.find('table', class_='table')

print (right_table.prettify())

A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll('tr'):
    # first row has no TH, but other rows have one TH and 6 TD
    cells = row.findAll('td') 
    # other than first row
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        #skip the sequence number column
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())  


from collections import OrderedDict

col_name = ["team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
