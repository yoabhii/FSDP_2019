# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:10:56 2019

@author: user
"""

import requests
ur1 = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=1e7a8783a971a4562b49"
current_USD_in_INR = requests.get(ur1).json()['USD_INR']
print("Equivalent INR:",round( float(input("Enter USD"))*current_USD_in_INR,2))