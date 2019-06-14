# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:24:57 2019

@author: user
"""

import json
import requests

Host = "https://en7nkjj5n8k68.x.pipedream.net"


headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("https://en7nkjj5n8k68.x.pipedream.net/get?firstname=Dev&language=English")
    return response

print (get_method().text)