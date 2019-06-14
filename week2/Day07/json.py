# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:34:14 2019

@author: user

import json
import requests

city =input("enter the city name>")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
response.content
data=response.json()

print("Wind Speed:",data["wind"]["speed"])
print("Sunset Rise and set timing:",data["sys"]["sunrise"])
print("Weather Condition:",data["weather"][0]["main"])