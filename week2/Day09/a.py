# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:54:21 2019

@author: user
"""
from bs4 import BeautifulSoup
import requests

url= "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url).text
soup = BeautifulSoup(source,"lxml")

print (soup.prettify())



right_table=soup.find('table', class_='table')

print (right_table.prettify())


#Generate lists
rank=[]
team=[]
matches=[]
points=[]
rating=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td') 
    if len(cells)==5:
        rank.append(cells[0].text.strip())
        team.append(cells[1].text.strip())
        matches.append(cells[2].text.strip())
        points.append(cells[3].text.strip())
        rating.append(cells[4].text.strip())
        

from collections import OrderedDict

col_name = ["Pos","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[rank,team,matches,points,rating]))

import pandas as pd
df = pd.DataFrame(col_data, index= rank) 
df.to_csv("former.csv", index=False)
